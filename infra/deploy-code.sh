#!/usr/bin/env bash
#
# Deploy the P&ID extraction service to Azure WITHOUT Docker.
#
# App Service runs it on the built-in Python 3.12 runtime, so there is no image
# and no Container Registry. ~$14/month:
#   App Service B1 $13.14 + Storage ~$1 + Static Web Apps Free $0
#
# Usage:
#   export LITELLM_API_KEY=sk-...
#   export SUFFIX=ku01            # 3-8 lowercase alphanumerics, globally unique
#   ./infra/deploy-code.sh
#
# Re-running is safe: resources are created only when missing, then the app is
# redeployed. For the container path instead, use ./infra/deploy.sh
set -euo pipefail

# On Windows/Git Bash the pip-installed "az" is a Python script whose shebang
# loses quoting: any argument containing a space arrives split in two, so
# --startup-file and --query silently break. az.bat passes argv through intact.
if command -v az.bat >/dev/null 2>&1; then
  az() { az.bat "$@"; }
fi

RG="${RG:-rg-autohazop}"
LOCATION="${LOCATION:-southeastasia}"
SWA_LOCATION="${SWA_LOCATION:-eastasia}"
SUFFIX="${SUFFIX:?set SUFFIX to 3-8 lowercase alphanumerics, e.g. export SUFFIX=ku01}"

STORAGE="stautohazop${SUFFIX}"
PLAN="asp-autohazop"
WEBAPP="pid-extract-${SUFFIX}"
SWA="swa-autohazop-${SUFFIX}"
BLOB_CONTAINER="pid-results"

LITELLM_BASE_URL="${LITELLM_BASE_URL:-https://scgc-llmproxy.scg.com}"
EXTRACT_MODEL="${EXTRACT_MODEL:-gpt-5.5}"
: "${LITELLM_API_KEY:?export LITELLM_API_KEY before running}"

STARTUP="gunicorn --bind=0.0.0.0:8000 --workers 1 --threads 8 --timeout 1800 --access-logfile '-' app:app"

say() { printf '\n=== %s ===\n' "$1"; }

say "Subscription"
az account show --query "{subscription:name,state:state}" -o table

say "Registering providers"
for ns in Microsoft.Web Microsoft.Storage; do
  az provider register -n "$ns" --only-show-errors >/dev/null
done

say "Resource group ${RG}"
az group create -n "$RG" -l "$LOCATION" -o none

say "Storage account ${STORAGE}"
az storage account show -n "$STORAGE" -g "$RG" -o none 2>/dev/null \
  || az storage account create -n "$STORAGE" -g "$RG" -l "$LOCATION" \
       --sku Standard_LRS --kind StorageV2 --min-tls-version TLS1_2 -o none

STORAGE_CONN="$(az storage account show-connection-string -n "$STORAGE" -g "$RG" --query connectionString -o tsv)"
az storage container create --name "$BLOB_CONTAINER" --connection-string "$STORAGE_CONN" -o none

say "App Service plan ${PLAN} (Linux B1)"
az appservice plan show -n "$PLAN" -g "$RG" -o none 2>/dev/null \
  || az appservice plan create -n "$PLAN" -g "$RG" -l "$LOCATION" --is-linux --sku B1 -o none

say "Web app ${WEBAPP} (Python 3.12, code deploy)"
az webapp show -n "$WEBAPP" -g "$RG" -o none 2>/dev/null \
  || az webapp create -n "$WEBAPP" -g "$RG" -p "$PLAN" --runtime "PYTHON:3.12" -o none

say "App settings"
az webapp config appsettings set -n "$WEBAPP" -g "$RG" --settings \
  SCM_DO_BUILD_DURING_DEPLOYMENT=true \
  LITELLM_BASE_URL="$LITELLM_BASE_URL" \
  LITELLM_API_KEY="$LITELLM_API_KEY" \
  EXTRACT_MODEL="$EXTRACT_MODEL" \
  STORAGE_BACKEND=blob \
  BLOB_CONTAINER="$BLOB_CONTAINER" \
  AZURE_STORAGE_CONNECTION_STRING="$STORAGE_CONN" \
  ALLOWED_ORIGINS="${ALLOWED_ORIGINS:-*}" \
  LOG_LEVEL=INFO -o none

say "Startup command and Always On"
# --workers 1 is required: the job registry lives in process memory.
az webapp config set -n "$WEBAPP" -g "$RG" --startup-file "$STARTUP" --always-on true -o none
az webapp config set -n "$WEBAPP" -g "$RG" \
  --generic-configurations '{"healthCheckPath":"/healthz"}' -o none

say "Building the deployment archive"
./infra/make-zip.sh

say "Deploying (Azure runs pip install on the server)"
az webapp deploy -n "$WEBAPP" -g "$RG" --src-path pid-extract-deploy.zip --type zip -o none

say "Seeding existing results into Blob"
az storage blob upload-batch -d "$BLOB_CONTAINER" --destination-path "results" \
  -s ./backend/static/data --pattern "*.json" --overwrite \
  --connection-string "$STORAGE_CONN" -o none

API_URL="https://$(az webapp show -n "$WEBAPP" -g "$RG" --query defaultHostName -o tsv)"

say "Waiting for the app to answer"
for i in $(seq 1 40); do
  if curl -fsS --max-time 10 "${API_URL}/healthz" >/dev/null 2>&1; then
    echo "healthz OK after ${i} attempt(s)"
    break
  fi
  sleep 15
done
curl -fsS "${API_URL}/api/config" || {
  echo "App did not come up. Logs:"
  echo "  az webapp log tail -n ${WEBAPP} -g ${RG}"
  exit 1
}

say "Static Web App ${SWA} (Free)"
az staticwebapp show -n "$SWA" -g "$RG" -o none 2>/dev/null \
  || az staticwebapp create -n "$SWA" -g "$RG" -l "$SWA_LOCATION" --sku Free -o none

SWA_URL="https://$(az staticwebapp show -n "$SWA" -g "$RG" --query defaultHostname -o tsv)"
SWA_TOKEN="$(az staticwebapp secrets list -n "$SWA" -g "$RG" --query 'properties.apiKey' -o tsv)"

say "Building the SPA against ${API_URL}"
NUXT_PUBLIC_EXTRACT_API_BASE="$API_URL" npm run generate

npx --yes @azure/static-web-apps-cli deploy ./.output/public \
  --deployment-token "$SWA_TOKEN" --env production

say "Locking CORS to the Static Web App origin"
az webapp config appsettings set -n "$WEBAPP" -g "$RG" \
  --settings ALLOWED_ORIGINS="$SWA_URL" -o none
az webapp restart -n "$WEBAPP" -g "$RG" -o none

say "Done"
echo "  Web app  : ${SWA_URL}"
echo "  API      : ${API_URL}"
echo "  Config   : ${API_URL}/api/config"
echo "  Blob     : ${STORAGE}/${BLOB_CONTAINER}   inputs/ + results/"
echo
echo "Teardown (stops all charges):  az group delete -n ${RG} --yes --no-wait"

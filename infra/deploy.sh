#!/usr/bin/env bash
#
# Deploy the P&ID extraction service to Azure.
#
# Student-safe footprint (~$19/month, see infra/README.md):
#   Container Registry Basic + App Service Linux B1 + Storage (Blob) + Static Web Apps Free
#
# Usage:
#   export OPENAI_API_KEY=sk-...
#   export SUFFIX=ku01              # 3-8 lowercase alphanumerics, makes names globally unique
#   ./infra/deploy.sh
#
# Re-running is safe: every resource is created only if missing, and the image
# is rebuilt and the web app restarted.
set -euo pipefail

RG="${RG:-rg-autohazop}"
LOCATION="${LOCATION:-southeastasia}"
SWA_LOCATION="${SWA_LOCATION:-eastasia}"
SUFFIX="${SUFFIX:?set SUFFIX to 3-8 lowercase alphanumerics, e.g. export SUFFIX=ku01}"
TAG="${TAG:-v1}"

ACR="acrautohazop${SUFFIX}"
STORAGE="stautohazop${SUFFIX}"
PLAN="asp-autohazop"
WEBAPP="app-pid-extract-${SUFFIX}"
SWA="swa-autohazop-${SUFFIX}"
BLOB_CONTAINER="pid-results"

: "${OPENAI_API_KEY:?export OPENAI_API_KEY before running}"

say() { printf '\n=== %s ===\n' "$1"; }

# ---------------------------------------------------------------- preflight
say "Preflight"
az account show --query "{subscription:name, state:state}" -o table
for ns in Microsoft.Web Microsoft.ContainerRegistry Microsoft.Storage; do
  az provider register -n "$ns" --only-show-errors >/dev/null
done

# Azure for Students often lacks quota for some SKUs/regions. Fail early and loudly.
# list-locations returns display names ("Southeast Asia"); normalise to slugs before matching.
if ! az appservice list-locations --sku B1 --linux-workers-enabled --query '[].name' -o tsv \
     | tr -d "\r" | tr "[:upper:]" "[:lower:]" | tr -d " " | grep -qx "$LOCATION"; then
  echo "ERROR: App Service B1 (Linux) is not available to this subscription in '${LOCATION}'."
  echo "Available regions:"
  az appservice list-locations --sku B1 --linux-workers-enabled -o table
  echo
  echo "Set LOCATION to one of the above and re-run. Do NOT fall back to the F1 Free tier:"
  echo "it caps CPU at 60 min/day and has no Always On, so long extractions get killed."
  exit 1
fi

# ---------------------------------------------------------------- resources
say "Resource group ${RG}"
az group create -n "$RG" -l "$LOCATION" -o none

say "Container Registry ${ACR} (Basic, ~\$5/mo)"
az acr show -n "$ACR" -g "$RG" -o none 2>/dev/null \
  || az acr create -n "$ACR" -g "$RG" --sku Basic --admin-enabled true -o none

say "Building image in the cloud (no local Docker needed, always linux/amd64)"
az acr build --registry "$ACR" --image "pid-extract:${TAG}" ./services/pid-extract

say "Storage account ${STORAGE} (~\$1/mo)"
az storage account show -n "$STORAGE" -g "$RG" -o none 2>/dev/null \
  || az storage account create -n "$STORAGE" -g "$RG" -l "$LOCATION" \
       --sku Standard_LRS --kind StorageV2 --min-tls-version TLS1_2 -o none

STORAGE_CONN="$(az storage account show-connection-string -n "$STORAGE" -g "$RG" --query connectionString -o tsv)"
az storage container create --name "$BLOB_CONTAINER" --connection-string "$STORAGE_CONN" -o none

say "App Service plan ${PLAN} (Linux B1, ~\$13/mo)"
az appservice plan show -n "$PLAN" -g "$RG" -o none 2>/dev/null \
  || az appservice plan create -n "$PLAN" -g "$RG" -l "$LOCATION" --is-linux --sku B1 -o none

say "Web app ${WEBAPP}"
az webapp show -n "$WEBAPP" -g "$RG" -o none 2>/dev/null \
  || az webapp create -n "$WEBAPP" -g "$RG" -p "$PLAN" \
       --deployment-container-image-name "${ACR}.azurecr.io/pid-extract:${TAG}" -o none

ACR_USER="$(az acr credential show -n "$ACR" --query username -o tsv)"
ACR_PASS="$(az acr credential show -n "$ACR" --query 'passwords[0].value' -o tsv)"
az webapp config container set -n "$WEBAPP" -g "$RG" \
  --container-image-name "${ACR}.azurecr.io/pid-extract:${TAG}" \
  --container-registry-url "https://${ACR}.azurecr.io" \
  --container-registry-user "$ACR_USER" \
  --container-registry-password "$ACR_PASS" -o none

say "App settings"
az webapp config appsettings set -n "$WEBAPP" -g "$RG" --settings \
  OPENAI_API_KEY="$OPENAI_API_KEY" \
  STORAGE_BACKEND=blob \
  BLOB_CONTAINER="$BLOB_CONTAINER" \
  AZURE_STORAGE_CONNECTION_STRING="$STORAGE_CONN" \
  ALLOWED_ORIGINS="${ALLOWED_ORIGINS:-*}" \
  WEBSITES_PORT=8000 \
  LOG_LEVEL=INFO -o none

az webapp config set -n "$WEBAPP" -g "$RG" --always-on true -o none
az webapp config set -n "$WEBAPP" -g "$RG" \
  --generic-configurations '{"healthCheckPath":"/healthz"}' -o none

say "Seeding existing extraction fixtures into Blob"
az storage blob upload-batch -d "$BLOB_CONTAINER" -s ./backend/static/data \
  --pattern "*.json" --overwrite --connection-string "$STORAGE_CONN" -o none

az webapp restart -n "$WEBAPP" -g "$RG" -o none
API_URL="https://$(az webapp show -n "$WEBAPP" -g "$RG" --query defaultHostName -o tsv)"

say "Waiting for the container to come up"
for i in $(seq 1 30); do
  if curl -fsS --max-time 10 "${API_URL}/healthz" >/dev/null 2>&1; then
    echo "healthz OK after ${i} attempt(s)"
    break
  fi
  sleep 10
done
curl -fsS "${API_URL}/healthz" || {
  echo "Service did not become healthy. Check logs:"
  echo "  az webapp log tail -n ${WEBAPP} -g ${RG}"
  exit 1
}

# ---------------------------------------------------------------- frontend
say "Static Web App ${SWA} (Free tier)"
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
echo "  Extract API : ${API_URL}"
echo "  Frontend    : ${SWA_URL}"
echo
echo "Teardown (stops all charges):  az group delete -n ${RG} --yes --no-wait"

#!/usr/bin/env bash
#
# Deploy the HAZOP backend (analysis agent + AEGUS assistant) to App Service.
#
# It rides on the SAME plan as aah-app, so it adds no monthly cost. The SPA and
# the extraction API stay on aah-app; this app only serves /api/ and /static/.
#
# Usage:
#   export LITELLM_API_KEY=sk-...
#   ./infra/deploy-hazop.sh
#
# Re-running is safe: resources are created only when missing, then redeployed.
set -euo pipefail

# az.bat passes argv through intact; the pip-installed "az" shim splits any
# argument containing a space, which breaks --startup-file.
if command -v az.bat >/dev/null 2>&1; then
  az() { az.bat "$@"; }
fi

RG="${RG:-rg-autohazop}"
PLAN="${PLAN:-asp-autohazop}"
WEBAPP="${WEBAPP:-aah-hazop}"
EXTRACT_APP="${EXTRACT_APP:-aah-app}"

LITELLM_BASE_URL="${LITELLM_BASE_URL:-https://scgc-llmproxy.scg.com}"
: "${LITELLM_API_KEY:?export LITELLM_API_KEY before running}"

# The SPA sends one shared secret to both backends, so this must match aah-app.
DEMO_TOKEN="${DEMO_TOKEN:-$(az webapp config appsettings list -n "$EXTRACT_APP" -g "$RG" \
  --query "[?name=='DEMO_TOKEN'].value | [0]" -o tsv)}"
[ -n "$DEMO_TOKEN" ] || { echo "Could not read DEMO_TOKEN from ${EXTRACT_APP}"; exit 1; }

# Generated workbooks are mirrored to the same storage account the extraction
# results already use, under a hazop/ prefix. Without this the download links
# and the assistant's worksheet die with the next deploy, which wipes wwwroot.
STORAGE_CONN="${STORAGE_CONN:-$(az webapp config appsettings list -n "$EXTRACT_APP" -g "$RG" \
  --query "[?name=='AZURE_STORAGE_CONNECTION_STRING'].value" -o tsv | head -1)}"
BLOB_CONTAINER="${BLOB_CONTAINER:-$(az webapp config appsettings list -n "$EXTRACT_APP" -g "$RG" \
  --query "[?name=='BLOB_CONTAINER'].value" -o tsv | head -1)}"
[ -n "$STORAGE_CONN" ] || echo "  WARNING: no storage connection string; workbooks will not survive a redeploy"

# --chdir backend: the archive keeps backend/ and skills/ side by side because
# the assistant resolves its knowledge base by walking up from backend/module/.
# --workers 1: Socket.IO run state lives in process memory.
STARTUP="gunicorn --chdir backend --bind=0.0.0.0:8000 --workers 1 --threads 8 --timeout 1800 --access-logfile '-' app:app"

say() { printf '\n=== %s ===\n' "$1"; }

say "Web app ${WEBAPP} on plan ${PLAN}"
az webapp show -n "$WEBAPP" -g "$RG" -o none 2>/dev/null \
  || az webapp create -n "$WEBAPP" -g "$RG" -p "$PLAN" --runtime "PYTHON:3.12" -o none

say "App settings"
az webapp config appsettings set -n "$WEBAPP" -g "$RG" --settings \
  SCM_DO_BUILD_DURING_DEPLOYMENT=true \
  LITELLM_BASE_URL="$LITELLM_BASE_URL" \
  LITELLM_API_KEY="$LITELLM_API_KEY" \
  LITELLM_MODELS="${LITELLM_MODELS:-gpt-5.5,GPT 5.4,claude-opus-4-8,claude-opus-4-7,Gemini 3.0 pro}" \
  DEMO_TOKEN="$DEMO_TOKEN" \
  AZURE_STORAGE_CONNECTION_STRING="$STORAGE_CONN" \
  BLOB_CONTAINER="${BLOB_CONTAINER:-pid-results}" \
  LOG_LEVEL=INFO -o none

say "Startup command, Always On, WebSockets"
az webapp config set -n "$WEBAPP" -g "$RG" \
  --startup-file "$STARTUP" --always-on true --web-sockets-enabled true -o none

say "Building the deployment archive"
./infra/make-hazop-zip.sh

say "Deploying (Azure runs pip install on the server)"
# The deploy API often returns 504 while Oryx is still installing, even though
# the deployment goes on to succeed. The health check below is the real gate.
az webapp deploy -n "$WEBAPP" -g "$RG" --src-path hazop-deploy.zip --type zip -o none   || echo "  deploy API reported an error; waiting to see whether the app comes up anyway"

API_URL="https://$(az webapp show -n "$WEBAPP" -g "$RG" --query defaultHostName -o tsv)"

say "Waiting for the app to answer"
for i in $(seq 1 40); do
  code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 \
    -H "X-Demo-Token: ${DEMO_TOKEN}" "${API_URL}/api/models" || true)"
  if [ "$code" = "200" ]; then echo "up after ${i} attempt(s)"; break; fi
  echo "  attempt ${i}: HTTP ${code}"
  sleep 15
done
[ "$code" = "200" ] || { echo "App did not come up (last HTTP ${code})."; exit 1; }

say "Done"
echo "  HAZOP API : ${API_URL}"
echo "  Next: rebuild the SPA with NUXT_PUBLIC_HAZOP_API_BASE=${API_URL} and redeploy ${EXTRACT_APP}"

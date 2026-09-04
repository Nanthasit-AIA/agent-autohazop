# Deploying the P&ID extraction service

The extraction feature runs as its own container (`services/pid-extract`), separate from the
HAZOP agent in `backend/`. This directory deploys **only** the extraction service and the SPA.

## Cost

The architecture deck priced this shape at **$111.65/month**. An Azure for Education / Azure
for Students subscription carries roughly a **$100 total credit**, so that footprint runs dry
in under a month — and App Service Premium V3 is frequently quota-blocked on student
subscriptions anyway. Same architecture, student-safe SKUs:

| Resource | SKU here | Deck's SKU | ~$/mo here |
|---|---|---|---|
| Container Registry | Basic | Basic | 5.00 |
| App Service Plan | **Linux B1** | Premium P0V3 | 13.14 |
| Storage Account (Blob) | Standard_LRS | Standard_LRS | ~1.00 |
| Static Web Apps | **Free** | Standard | 0.00 |
| Azure Monitor | free tier | — | 0.00 |
| PostgreSQL Flexible | **not deployed** | B1ms | 0.00 (was 27.81) |
| Key Vault | **not deployed** | deployed | 0.00 |
| **Total** | | | **~$19** |

About five months of runway instead of under one. Postgres is skipped because nothing in the
codebase reads or writes a database — extraction results are JSON blobs.

List prices, region-dependent. Check the real burn with:

```bash
az consumption usage list --top 20 -o table
```

## Two ways to deploy

**Portal + ZIP (fastest, no Docker).** App Service runs Python directly from code, so
there is no image to build and no Container Registry. This is the demo path — see below.
Roughly **$14/month**.

The same thing scripted, if you have the Azure CLI, is `./infra/deploy-code.sh` — identical
resources and settings, one command instead of the Portal walkthrough.

**Container from ACR.** Keeps the architecture in the deck: a real image, pulled from a
registry. Needs the Azure CLI but still no local Docker, since `az acr build` builds in the
cloud. `./infra/deploy.sh` does it end to end. Roughly **$19/month**.

The Dockerfile stays in the repo either way, so switching later costs nothing.

---

# Portal deploy, step by step

About 15 minutes. Pick a short suffix (`ku01` below) — web app and storage account names
must be globally unique across Azure.

## A. Storage — 2 minutes

1. **Create resource → Storage account.** Resource group `rg-autohazop` (create it here),
   name `stautohazop ku01` without the space, region **Southeast Asia**, Standard / LRS.
2. Open it → **Data storage → Containers → + Container**, name it `pid-results`.
3. **Security + networking → Access keys → Show**, copy the **Connection string** for key1.
   You need it in step B2.

## B. The API — 6 minutes

1. **Create resource → Web App.**
   - Resource group `rg-autohazop`, name `pid-extract-ku01`
   - **Publish: Code** (not Container)
   - **Runtime stack: Python 3.12**, OS Linux, region Southeast Asia
   - **Pricing plan: Basic B1** — not Free F1, see the note below

2. Open the app → **Settings → Environment variables**, add:

   | Name | Value |
   |---|---|
   | `SCM_DO_BUILD_DURING_DEPLOYMENT` | `true` |
   | `LITELLM_BASE_URL` | `https://scgc-llmproxy.scg.com` |
   | `LITELLM_API_KEY` | your proxy key |
   | `EXTRACT_MODEL` | `gpt-5.5` |
   | `STORAGE_BACKEND` | `blob` |
   | `BLOB_CONTAINER` | `pid-results` |
   | `AZURE_STORAGE_CONNECTION_STRING` | from step A3 |
   | `ALLOWED_ORIGINS` | `*` — tightened in step D |

   `SCM_DO_BUILD_DURING_DEPLOYMENT` is the one people forget. Without it Azure skips
   `pip install` and the app starts with no dependencies.

3. **Configuration → General settings**:
   - **Startup Command**:
     `gunicorn --bind=0.0.0.0:8000 --workers 1 --threads 8 --timeout 1800 --access-logfile '-' app:app`
   - **Always On: On**
   - Save.

   `--workers 1` is not optional. The job registry lives in process memory, so a poll has to
   reach the process that started the job.

4. Build the archive locally and upload it:

   ```bash
   ./infra/make-zip.sh
   ```

   Then browse to `https://pid-extract-ku01.scm.azurewebsites.net/ZipDeployUI` and drag
   `pid-extract-deploy.zip` onto the page. Wait for the build to finish — it runs
   `pip install -r requirements.txt` on the server.

5. Check what the running instance is wired to:

   ```bash
   curl https://pid-extract-ku01.azurewebsites.net/api/config
   ```

   Expect `"provider":"litellm:…"` and `"storage":"blob"`.

6. Optional: **Monitoring → Health check → /healthz**.

## C. The web app — 5 minutes

1. **Create resource → Static Web App.** Resource group `rg-autohazop`, name
   `swa-autohazop-ku01`, plan **Free**, region **East Asia** (Static Web Apps has no
   Southeast Asia region). **Deployment source: Other** — this skips the GitHub wiring.
2. Open it → **Overview → Manage deployment token**, copy it.
3. Build with the API URL baked in, then upload. The Nuxt build is static, so the URL is
   fixed at build time:

   ```bash
   NUXT_PUBLIC_EXTRACT_API_BASE=https://pid-extract-ku01.azurewebsites.net npm run generate
   ```
   ```bash
   npx @azure/static-web-apps-cli deploy ./.output/public --deployment-token PASTE_TOKEN --env production
   ```

4. Open the Static Web App URL from its Overview blade. Upload a P&ID and run an extraction.

## D. Lock CORS — 1 minute

Back in the Web App → **Environment variables** → set `ALLOWED_ORIGINS` to the Static Web App
origin, e.g. `https://swa-autohazop-ku01.azurestaticapps.net`. Save; the app restarts.

## Confirm Blob holds both halves

Storage account → **Containers → pid-results**. After one extraction you should see
`inputs/<job_id>/<drawing>` and `results/<name>.json`.

To seed your six existing results, use **Upload** with *Advanced → Upload to folder* set to
`results`.

## Portal costs

App Service B1 $13.14 + Storage ~$1 + Static Web Apps Free $0 = **~$14/month**. Cheaper than
the container path because there is no Container Registry.

---

## Prerequisites

- **Azure CLI** — `winget install Microsoft.AzureCLI`, then `az login`
- **Node 20+** — for `npm run generate` (the script builds and deploys the SPA)
- Docker Desktop is **not** required: `az acr build` builds the image in Azure, which also
  avoids the arm64/amd64 mismatch you get building on an ARM laptop.

## Deploy

```bash
export LITELLM_API_KEY=sk-...
```
```bash
export SUFFIX=ku01
```
```bash
./infra/deploy.sh
```

`SUFFIX` is 3–8 lowercase alphanumerics; registry, storage account, and web app names must be
globally unique across all of Azure. Re-running is safe — every resource is created only when
missing, then the image is rebuilt and the app restarted.

Override defaults with `RG`, `LOCATION` (default `southeastasia`), `SWA_LOCATION`
(default `eastasia` — Static Web Apps has no Southeast Asia region), and `TAG`.

The script prints both URLs at the end and locks the API's CORS to the Static Web App origin.

## Redeploy after a code change

```bash
az acr build --registry acrautohazop$SUFFIX --image pid-extract:v1 ./services/pid-extract
```
```bash
az webapp restart -n app-pid-extract-$SUFFIX -g rg-autohazop
```

## Running it day to day

### Local

```bash
.\scripts\local-start.ps1
```
```bash
.\scripts\local-stop.ps1
```

`local-start.ps1` creates `services/pid-extract/.venv` on first run, seeds the result store,
and starts the extraction API (:8000), the HAZOP agent (:5000) and the UI (:3000). Add
`-Tunnel` for a public Cloudflare URL, `-Model gemini-3.5-flash` for faster demos, and
`-DemoToken <secret>` to require a password.

`local-stop.ps1` only touches those three ports and cloudflared, so nothing else on the
machine is affected.

### Azure

The deployed app is `aah-app` — it serves both the SPA and the API from one origin.

```bash
az webapp stop  -n aah-app -g rg-autohazop
```
```bash
az webapp start -n aah-app -g rg-autohazop
```

**Stopping the web app does not stop the bill.** App Service charges for the *plan*
(`asp-autohazop`, B1), not for whether an app on it happens to be running. Stopping is for
taking the demo offline, not for saving money.

To actually stop charges you either delete the resource group (below) and redeploy when
needed — about 15 minutes — or downgrade the plan while idle:

```bash
az webapp config set -n aah-app -g rg-autohazop --always-on false
```
```bash
az appservice plan update -n asp-autohazop -g rg-autohazop --sku F1
```

F1 is free but caps CPU at 60 minutes/day and cannot keep Always On, so a long extraction
can be killed mid-run. Go back to B1 before a demo with `--sku B1`, then re-enable Always On.

### Redeploying after a code change

```bash
./infra/make-zip.sh
```
```bash
az webapp deploy -n aah-app -g rg-autohazop --src-path pid-extract-deploy.zip --type zip
```

If the frontend changed, rebuild it into the archive first:

```bash
NUXT_PUBLIC_EXTRACT_API_BASE="" NUXT_PUBLIC_DEMO_TOKEN=<secret> npm run generate && rm -rf services/pid-extract/spa && cp -r .output/public services/pid-extract/spa
```

## Teardown

Deleting the resource group is the only reliable way to stop all charges:

```bash
az group delete -n rg-autohazop --yes --no-wait
```

## Things that will bite you

**Gunicorn must stay at `--workers 1`.** `pid/jobs.py` keeps the job registry in process
memory, so a `GET /api/jobs/<id>` poll has to land on the process that started the job. More
worker processes means polls randomly 404. Concurrency comes from `--threads 8` instead;
extraction is I/O-bound on the OpenAI call, so threads are the right shape here.

**Why extraction is a job, not a plain POST.** App Service closes idle HTTP requests after
about 230 seconds and that limit cannot be raised. A P&ID extraction routinely runs longer, so
`POST /api/extract` returns `202` with a job id immediately and the client polls. Results are
written to Blob *before* the job is marked done, so a finished extraction survives a restart.
An in-flight one does not: the job disappears and the client is told to retry.

**Always On is enabled** (`--always-on true`). Without it App Service unloads the container
when idle and kills any running extraction thread. It is included in the B1 price.

**Health probe is `/healthz`**, which deliberately touches neither the LLM nor storage — a bad
`LITELLM_API_KEY` should surface as a failed extraction, not as a container Azure keeps
restarting.

## Hardening, once it works end to end

- **Managed identity instead of the storage connection string.** `az webapp identity assign`,
  grant *Storage Blob Data Contributor* on the storage account, then delete the
  `AZURE_STORAGE_CONNECTION_STRING` app setting and add `AZURE_STORAGE_ACCOUNT`. No code
  change — `BlobStore` already falls through to `DefaultAzureCredential`.
- **Key Vault for `LITELLM_API_KEY`** via a Key Vault reference in app settings. Effectively
  free at this request volume. This is the deck's Key Vault box.
- **GitHub Actions** to run `az acr build` + `az webapp restart` on push to `main` — the deck's
  CI/CD arrow. Needs a federated credential or a service principal secret.

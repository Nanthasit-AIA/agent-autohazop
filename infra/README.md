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

## Prerequisites

- **Azure CLI** — `winget install Microsoft.AzureCLI`, then `az login`
- **Node 20+** — for `npm run generate` (the script builds and deploys the SPA)
- Docker Desktop is **not** required: `az acr build` builds the image in Azure, which also
  avoids the arm64/amd64 mismatch you get building on an ARM laptop.

## Deploy

```bash
export OPENAI_API_KEY=sk-...
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
`OPENAI_API_KEY` should surface as a failed extraction, not as a container Azure keeps
restarting.

## Hardening, once it works end to end

- **Managed identity instead of the storage connection string.** `az webapp identity assign`,
  grant *Storage Blob Data Contributor* on the storage account, then delete the
  `AZURE_STORAGE_CONNECTION_STRING` app setting and add `AZURE_STORAGE_ACCOUNT`. No code
  change — `BlobStore` already falls through to `DefaultAzureCredential`.
- **Key Vault for `OPENAI_API_KEY`** via a Key Vault reference in app settings. Effectively
  free at this request volume. This is the deck's Key Vault box.
- **GitHub Actions** to run `az acr build` + `az webapp restart` on push to `main` — the deck's
  CI/CD arrow. Needs a federated credential or a service principal secret.

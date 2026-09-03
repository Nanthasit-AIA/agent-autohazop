# pid-extract

P&ID extraction as a standalone service. Upload one or more P&ID PDFs/images plus a process
description; get back structured JSON matching `pid/schema.py` (`PIDResponse`).

Split out of `backend/` so it can be containerized and deployed on its own. The HAZOP agent
stays in `backend/app.py` and is unaffected.

## API

| Method | Path | Behaviour |
|---|---|---|
| `GET` | `/healthz` | Liveness. Touches neither the LLM nor storage. |
| `GET` | `/api/config` | What this instance is wired to: provider, model, storage backend. |
| `POST` | `/api/extract` | multipart: `name`, `description`, `file` (repeatable). Returns `202 {job_id, name}`. |
| `GET` | `/api/jobs/<job_id>` | `{status, name, error}`; on `done` also `{result}`. `404` if unknown. |
| `GET` | `/api/results/<name>` | A previously saved result, `{ok, file_name, data}`. |

Extraction takes minutes, so it runs as a background job and the client polls. See
`infra/README.md` for why.

`result` and `data` both have the shape `{"pid_data": {...}, "metadata": {...}}` — the same
layout the six fixtures in `backend/static/data/` use, and what the SPA expects.

## Run locally

With Docker Desktop, from the repo root:

```bash
cp .env.example .env
```
```bash
docker compose up --build
```

Compose mounts `backend/static/data` at the store's `results/` prefix, so the existing
fixtures are immediately readable at `GET /api/results/h2o2`. Uploads land in `/data/inputs`.

Without Docker:

```bash
pip install -r services/pid-extract/requirements.txt
```
```bash
cd services/pid-extract && LITELLM_BASE_URL=https://scgc-llmproxy.scg.com LITELLM_API_KEY=sk-... LOCAL_STORE_DIR=../../backend/static/data python app.py
```

## Smoke test

```bash
curl -fsS http://localhost:8000/healthz
```
```bash
curl -fsS http://localhost:8000/api/results/h2o2 | head -c 300
```
```bash
curl -sS -X POST -F name=h2o2_docker -F "description=Hydrogen peroxide process" -F "file=@backend/static/image/h2o2.pdf" http://localhost:8000/api/extract
```
```bash
curl -sS http://localhost:8000/api/jobs/PASTE_JOB_ID_HERE
```

## Configuration

Every value is an environment variable; see `.env.example`.

| Variable | Default | Notes |
|---|---|---|
| `LITELLM_BASE_URL` | — | The LiteLLM proxy. `/v1` is appended if missing. |
| `LITELLM_API_KEY` | — | Proxy key. Checked per request, **not** at import, so bad credentials never break `/healthz`. |
| `EXTRACT_MODEL` | `gpt-5.5` | Must match a model id from the proxy's `/v1/models` exactly. |
| `LLM_BASE_URL` / `LLM_API_KEY` | unset | Deployment-level override; wins over `LITELLM_*`. |
| `OPENAI_API_KEY` | unset | Fallback only, used when no LiteLLM/LLM credential is set. |
| `STORAGE_BACKEND` | `local` | `local` or `blob`. |
| `LOCAL_STORE_DIR` | `data` | When `local`. |
| `BLOB_CONTAINER` | `pid-results` | When `blob`. |
| `AZURE_STORAGE_CONNECTION_STRING` | unset | When `blob`. Leave empty and set `AZURE_STORAGE_ACCOUNT` to use a managed identity. |
| `ALLOWED_ORIGINS` | `*` | Comma-separated CORS allowlist. |

## Storage layout

Both backends use the same two prefixes, so local and Azure match:

```
inputs/<job_id>/<filename>     the uploaded drawings
results/<name>.json            the extraction output
```

Uploads are written to the store in the request handler, and the worker reads
them back out before calling the model. So the extraction path is the same one
a re-run would take, the container holds no upload state, and every drawing
that produced a result is still there to audit against it. The result records
its inputs under `metadata.inputs`.

## LiteLLM notes

Extraction goes through the LiteLLM proxy using the **Responses API**
(`client.responses.parse` with `text_format=PIDResponse`), which the proxy
supports.

What it does **not** support is the Files API — it answers
`files_settings is not set`. So files are not uploaded and referenced by id;
their bytes are inlined into the request as data URIs: PDFs as
`input_file` + `file_data`, images as `input_image` + `image_url`. That is the
one real difference from calling OpenAI directly, and it is why
`_upload_vision_file` no longer exists.

Model ids must be copied exactly from `/v1/models`. The proxy lists some
display names with spaces (`GPT 5.1`, `GPT 5-mini`) that it then rejects as
invalid; the slug-style ids (`gpt-5.5`, `gemini-3.5-flash`, `claude-opus-4-8`)
work. Check what your key can actually call:

```bash
curl -H "Authorization: Bearer $LITELLM_API_KEY" $LITELLM_BASE_URL/v1/models
```

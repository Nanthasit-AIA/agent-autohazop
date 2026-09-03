# pid-extract

P&ID extraction as a standalone service. Upload one or more P&ID PDFs/images plus a process
description; get back structured JSON matching `pid/schema.py` (`PIDResponse`).

Split out of `backend/` so it can be containerized and deployed on its own. The HAZOP agent
stays in `backend/app.py` and is unaffected.

## API

| Method | Path | Behaviour |
|---|---|---|
| `GET` | `/healthz` | Liveness. Touches neither the LLM nor storage. |
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

Compose mounts `backend/static/data` as the result store, so the existing fixtures are
immediately readable at `GET /api/results/h2o2`.

Without Docker:

```bash
pip install -r services/pid-extract/requirements.txt
```
```bash
cd services/pid-extract && OPENAI_API_KEY=sk-... LOCAL_STORE_DIR=../../backend/static/data python app.py
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

Every value is an environment variable; see `.env.example`. The ones that matter:

| Variable | Default | Notes |
|---|---|---|
| `OPENAI_API_KEY` | — | Required. Read per request, **not** at import, so a bad key never breaks `/healthz`. |
| `LLM_BASE_URL` | unset | Unset → api.openai.com. Set to a LiteLLM/OpenRouter proxy to change providers. |
| `EXTRACT_MODEL` | `gpt-5.1-2025-11-13` | |
| `STORAGE_BACKEND` | `local` | `local` or `blob`. |
| `LOCAL_STORE_DIR` | `data` | When `local`. |
| `BLOB_CONTAINER` | `pid-results` | When `blob`. |
| `AZURE_STORAGE_CONNECTION_STRING` | unset | When `blob`. Leave empty and set `AZURE_STORAGE_ACCOUNT` to use a managed identity instead. |
| `ALLOWED_ORIGINS` | `*` | Comma-separated CORS allowlist. |

## On swapping in LiteLLM

`LLM_BASE_URL` is the seam, but it is not a free swap. `extractor.py` calls
`client.responses.parse(text_format=PIDResponse)` — OpenAI's Responses API with native
structured output. LiteLLM's proxy does not fully support that endpoint. Actually moving
providers means rewriting extraction to `json_schema` chat completions and re-validating
output quality against the fixtures in `backend/static/data/`.

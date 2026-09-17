import hmac, io, os, tempfile, uuid
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_file, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

from pid import jobs
from pid.extractor import extract_pid, extract_pid_multi_files_single_call
from pid.llm import default_model, default_provider, get_llm_config, provider_label
from pid.logging_conf import logger
from pid.modify import modify_pid_json
from pid.review_excel import export_pid_review_excel, import_pid_review_excel
from pid.storage import get_store, slugify_filename

# Scoped to this service's own .env. Bare load_dotenv() walks up the tree and would
# silently pick up an unrelated .env from a parent directory.
load_dotenv(Path(__file__).parent / ".env")

ALLOWED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".webp"}
MAX_UPLOAD_BYTES = 25 * 1024 * 1024

# Shared-secret gate. Unset means open, which is right for local dev; set it
# whenever the service is reachable from outside the machine, so that finding
# the port is not the same as being able to spend the LLM budget.
DEMO_TOKEN = os.getenv("DEMO_TOKEN", "").strip()

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_UPLOAD_BYTES
CORS(
    app,
    origins=[o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",")],
    allow_headers=["Content-Type", "X-Demo-Token"],
)

@app.before_request
def require_token():
    if not DEMO_TOKEN or request.method == "OPTIONS":
        return None
    # Gate the API only. /healthz must answer probes, and the SPA's own files
    # have to load before it can send the token it carries.
    if not request.path.startswith("/api/"):
        return None
    supplied = request.headers.get("X-Demo-Token") or request.args.get("token", "")
    if not hmac.compare_digest(supplied, DEMO_TOKEN):
        return jsonify({"ok": False, "error": "Unauthorized"}), 401
    return None

@app.before_request
def log_request():
    logger.info("%s %s", request.method, request.path)

@app.get("/healthz")
def healthz():
    # Liveness only - no LLM or storage call, so bad credentials never fail the probe.
    return jsonify({"ok": True})

@app.get("/api/config")
def api_config():
    """What this instance is wired to. Handy for confirming a deployment."""
    prov = default_provider()
    return jsonify({
        "ok": True,
        "provider": provider_label(prov),
        "model": default_model(prov),
        "storage": os.getenv("STORAGE_BACKEND", "local"),
    })

@app.get("/api/llm-config")
def api_llm_config():
    """Provider/model groups for the UI picker. Only configured providers appear."""
    return jsonify(get_llm_config())

@app.post("/api/extract")
def api_extract():
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip()
    node_define = request.form.get("node_define", "").strip()
    intention = request.form.get("intention", "").strip()
    llm_provider = request.form.get("llm_provider", "").strip() or default_provider()
    llm_model = request.form.get("llm_model", "").strip() or None
    files = request.files.getlist("file")

    if not files:
        return jsonify({"ok": False, "error": "No file received"}), 400

    store = get_store()
    job_id = uuid.uuid4().hex
    uploaded: list[tuple[str, str]] = []  # (filename, storage key)

    for f in files:
        if not f.filename:
            continue
        safe = secure_filename(f.filename)
        if Path(safe).suffix.lower() not in ALLOWED_EXTENSIONS:
            return jsonify({
                "ok": False,
                "error": f"Unsupported file type: {f.filename}",
            }), 400
        key = store.put_input(job_id, safe, f.read())
        uploaded.append((safe, key))

    if not uploaded:
        return jsonify({"ok": False, "error": "No valid file received"}), 400

    result_name = slugify_filename(name or Path(uploaded[0][0]).stem)

    def work() -> dict:
        # Read the drawings back out of the store, so the extraction path is the
        # same one a re-run would take and the container holds no upload state.
        loaded = [(fname, store.get_input(key)) for fname, key in uploaded]

        kwargs = dict(
            process_description=description,
            node_define=node_define,
            intention=intention,
            llm_provider=llm_provider,
            model=llm_model,
        )
        if len(loaded) == 1:
            pid_data, usage_meta = extract_pid(loaded[0], **kwargs)
        else:
            pid_data, usage_meta = extract_pid_multi_files_single_call(loaded, **kwargs)

        usage_meta["inputs"] = [key for _, key in uploaded]
        # What JsonDisplay renders; served by /api/inputs below.
        usage_meta["source_files"] = [f"/api/inputs/{key}" for _, key in uploaded]

        payload = {
            "pid_data": pid_data.model_dump(by_alias=True),
            "metadata": usage_meta,
        }
        # Persist before the job is marked done, so the result outlives the container.
        store.save_result(result_name, payload)
        return payload

    jobs.submit_with_id(job_id, result_name, work)
    logger.info("Queued job %s for '%s' (%d file(s))", job_id, result_name, len(uploaded))
    return jsonify({"ok": True, "job_id": job_id, "name": result_name}), 202

@app.get("/api/jobs/<job_id>")
def api_job(job_id: str):
    job = jobs.get(job_id)
    if job is None:
        return jsonify({"ok": False, "error": "Unknown job"}), 404

    body = {
        "ok": job["status"] != "error",
        "status": job["status"],
        "name": job["name"],
        "error": job["error"],
    }
    if job["status"] == "done":
        body["result"] = job["result"]
    return jsonify(body), 200

@app.get("/api/results/<name>")
def api_result(name: str):
    data = get_store().load_result(name)
    if data is None:
        return jsonify({"ok": False, "error": "File not found"}), 404
    return jsonify({
        "ok": True,
        "file_name": f"{slugify_filename(name)}.json",
        "data": data,
    }), 200

@app.get("/api/inputs/<path:key>")
def api_input(key: str):
    """Stream a stored drawing back out - for the viewer next to the extracted JSON."""
    if not key.startswith("inputs/") or ".." in key:
        return jsonify({"ok": False, "error": "Not found"}), 404
    try:
        data = get_store().get_input(key)
    except Exception:
        return jsonify({"ok": False, "error": "Not found"}), 404
    from pid.prompt import MIME_BY_SUFFIX
    mime = MIME_BY_SUFFIX.get(Path(key).suffix.lower(), "application/octet-stream")
    return send_file(io.BytesIO(data), mimetype=mime, download_name=Path(key).name)

@app.post("/api/modify")
def api_modify():
    """LLM-driven patch of a stored result. Re-reads the original drawings from the store."""
    file_name = request.form.get("file_name", "").strip()
    instruction = request.form.get("instruction", "").strip()
    llm_provider = request.form.get("llm_provider", "").strip() or default_provider()
    llm_model = request.form.get("llm_model", "").strip() or None

    if not file_name:
        return jsonify({"ok": False, "error": "file_name is required"}), 400
    if not instruction:
        return jsonify({"ok": False, "error": "instruction is required"}), 400

    store = get_store()
    base_name = slugify_filename(Path(file_name).stem)
    combined = store.load_result(base_name)
    if combined is None:
        return jsonify({"ok": False, "error": f"Result not found: {base_name}"}), 404

    # Drawings: anything newly uploaded, else the inputs the result was made from.
    files: list[tuple[str, bytes]] = []
    for f in request.files.getlist("file"):
        if f.filename:
            safe = secure_filename(f.filename)
            if Path(safe).suffix.lower() not in ALLOWED_EXTENSIONS:
                return jsonify({"ok": False, "error": f"Unsupported file type: {f.filename}"}), 400
            files.append((safe, f.read()))
    if not files:
        for key in combined.get("metadata", {}).get("inputs", []):
            try:
                files.append((Path(key).name, store.get_input(key)))
            except Exception as e:
                logger.warning("Could not reload input %s for modify: %s", key, e)

    try:
        new_combined, _ = modify_pid_json(
            combined, instruction, files, llm_provider=llm_provider, model=llm_model,
        )
    except ValueError as e:
        return jsonify({"ok": False, "error": f"Validation failed: {e}"}), 422
    except Exception as e:
        logger.exception("modify_pid_json failed")
        return jsonify({"ok": False, "error": str(e)}), 500

    store.save_result(base_name, new_combined)
    return jsonify({"ok": True, "data": new_combined, "file_name": f"{base_name}.json"})

@app.post("/api/review/export")
def api_review_export():
    """Stored result -> engineer-review workbook, returned as a download."""
    payload = request.get_json(silent=True) or {}
    name = (payload.get("name") or payload.get("file_name") or "pid_review").strip()
    data = payload.get("data")
    if not data:
        data = get_store().load_result(slugify_filename(Path(name).stem))
    if not data:
        return jsonify({"ok": False, "error": "No PID data received"}), 400

    try:
        with tempfile.TemporaryDirectory() as tmp:
            xlsx_path = export_pid_review_excel(data=data, out_dir=tmp, name=name)
            buf = io.BytesIO(xlsx_path.read_bytes())
        buf.seek(0)
        return send_file(
            buf,
            as_attachment=True,
            download_name=xlsx_path.name,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    except Exception as e:
        logger.exception("Review Excel export failed")
        return jsonify({"ok": False, "error": str(e)}), 500

@app.post("/api/review/import")
def api_review_import():
    """Reviewed workbook -> stored result (replaces pid_data, keeps the old metadata)."""
    name = (request.form.get("name") or "reviewed_pid").strip()
    review_file = request.files.get("file")
    if not review_file or not review_file.filename:
        return jsonify({"ok": False, "error": "No review file received"}), 400
    if not review_file.filename.lower().endswith(".xlsx"):
        return jsonify({"ok": False, "error": "Review file must be .xlsx"}), 400

    try:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / secure_filename(review_file.filename)
            review_file.save(path)
            pid_data, errors, warnings = import_pid_review_excel(path)
    except Exception as e:
        logger.exception("Review Excel import failed")
        return jsonify({"ok": False, "error": str(e)}), 500

    if errors:
        return jsonify({"ok": False, "error": "Review file has errors", "errors": errors, "warnings": warnings}), 422

    store = get_store()
    base_name = slugify_filename(Path(name).stem)
    existing = store.load_result(base_name) or {}
    metadata = dict(existing.get("metadata", {}))
    metadata["reviewed_from"] = review_file.filename
    combined = {"pid_data": pid_data, "metadata": metadata}
    store.save_result(base_name, combined)
    return jsonify({"ok": True, "file_name": f"{base_name}.json", "data": combined, "warnings": warnings})

# ---------------------------------------------------------------- SPA
# Optional. When SPA_DIR is set, this service also serves the built frontend,
# so the whole app lives on one origin: no CORS, and no rebuilding the SPA
# every time the API hostname changes. Unset, it stays a pure API.
SPA_DIR = os.getenv("SPA_DIR", "").strip()

if SPA_DIR:
    SPA_ROOT = (Path(__file__).parent / SPA_DIR).resolve()

    @app.get("/")
    def spa_index():
        return send_from_directory(SPA_ROOT, "index.html")

    @app.get("/<path:filename>")
    def spa_files(filename: str):
        # Never let the catch-all answer for the API surface.
        if filename.startswith(("api/", "healthz")):
            return jsonify({"ok": False, "error": "Not found"}), 404
        candidate = (SPA_ROOT / filename).resolve()
        if candidate.is_file() and candidate.is_relative_to(SPA_ROOT):
            return send_from_directory(SPA_ROOT, filename)
        return send_from_directory(SPA_ROOT, "index.html")  # SPA route fallback

    logger.info("Serving SPA from %s", SPA_ROOT)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))

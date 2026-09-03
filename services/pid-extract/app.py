import os, uuid
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename

from pid import jobs
from pid.extractor import extract_pid, extract_pid_multi_files_single_call
from pid.llm import EXTRACT_MODEL, provider_label
from pid.logging_conf import logger
from pid.storage import get_store, slugify_filename

# Scoped to this service's own .env. Bare load_dotenv() walks up the tree and would
# silently pick up an unrelated .env from a parent directory.
load_dotenv(Path(__file__).parent / ".env")

ALLOWED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".webp"}
MAX_UPLOAD_BYTES = 25 * 1024 * 1024

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_UPLOAD_BYTES
CORS(app, origins=[o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",")])

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
    return jsonify({
        "ok": True,
        "provider": provider_label(),
        "model": EXTRACT_MODEL,
        "storage": os.getenv("STORAGE_BACKEND", "local"),
    })

@app.post("/api/extract")
def api_extract():
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip()
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

        if len(loaded) == 1:
            pid_data, usage_meta = extract_pid(
                loaded[0],
                process_description=description,
            )
        else:
            pid_data, usage_meta = extract_pid_multi_files_single_call(
                loaded,
                process_description=description,
            )

        usage_meta["inputs"] = [key for _, key in uploaded]

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))

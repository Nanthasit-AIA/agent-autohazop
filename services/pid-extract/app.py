import os, tempfile
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename

from pid import jobs
from pid.extractor import extract_pid, extract_pid_multi_files_single_call
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
    # Liveness only - no LLM or storage call, so a bad key never fails the probe.
    return jsonify({"ok": True})

@app.post("/api/extract")
def api_extract():
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip()
    files = request.files.getlist("file")

    if not files:
        return jsonify({"ok": False, "error": "No file received"}), 400

    tmpdir = tempfile.mkdtemp(prefix="pid-extract-")
    saved_paths: list[str] = []
    for f in files:
        if not f.filename:
            continue
        safe = secure_filename(f.filename)
        if Path(safe).suffix.lower() not in ALLOWED_EXTENSIONS:
            return jsonify({
                "ok": False,
                "error": f"Unsupported file type: {f.filename}",
            }), 400
        path = Path(tmpdir) / safe
        f.save(path)
        saved_paths.append(str(path))

    if not saved_paths:
        return jsonify({"ok": False, "error": "No valid file received"}), 400

    result_name = slugify_filename(name or Path(saved_paths[0]).stem)

    def work() -> dict:
        try:
            if len(saved_paths) == 1:
                pid_data, usage_meta = extract_pid(
                    saved_paths[0],
                    process_description=description,
                )
            else:
                pid_data, usage_meta = extract_pid_multi_files_single_call(
                    saved_paths,
                    process_description=description,
                )

            payload = {
                "pid_data": pid_data.model_dump(by_alias=True),
                "metadata": usage_meta,
            }
            # Persist before the job is marked done, so the result outlives the container.
            get_store().save(result_name, payload)
            return payload
        finally:
            for p in saved_paths:
                Path(p).unlink(missing_ok=True)
            try:
                os.rmdir(tmpdir)
            except OSError:
                pass

    job_id = jobs.submit(result_name, work)
    logger.info("Queued job %s for '%s' (%d file(s))", job_id, result_name, len(saved_paths))
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
    data = get_store().load(name)
    if data is None:
        return jsonify({"ok": False, "error": "File not found"}), 404
    return jsonify({
        "ok": True,
        "file_name": f"{slugify_filename(name)}.json",
        "data": data,
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))

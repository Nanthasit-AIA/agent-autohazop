import os, time
from pathlib import Path

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO

from utils import search_file
from decorators import logger
from module.ext_module import extract_pid, extract_pid_multi_files_single_call
from module.agent_module import run_hazop_agent
from utils import save_pid_json

app = Flask(__name__, static_folder="static")
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
DATA_DIR = Path(app.root_path) / "static" / "data"

@app.before_request
def log_request():
    logger.info(
        f" {request.method} {request.path} | args={dict(request.args)} | form={dict(request.form)}"
    )
# ---------- Extract agent via Socket.IO -----------------
@app.route("/api/full", methods=["POST"])
def api_full():
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip()

    logger.info("🟦 /api/full received")
    logger.info(f"name: {name}")
    logger.info(f"description: {description}")

    socketio.emit("file_status", {
        "status": "working",
        "file_name": name,
        "error": "",
    })

    # ----------------------------
    # 1) UPLOAD FILES
    # ----------------------------
    files = request.files.getlist("file")

    if not files:
        return jsonify({"ok": False, "error": "No file received"}), 400

    upload_dir = Path("static") / "uploads"
    upload_dir.mkdir(parents=True, exist_ok=True)

    saved_paths = []
    for f in files:
        if not f.filename:
            continue

        save_path = upload_dir / f.filename
        f.save(save_path)
        saved_paths.append(str(save_path))

        logger.info(f"file saved to: {save_path}")

    if not saved_paths:
        return jsonify({"ok": False, "error": "No valid file received"}), 400

    # ----------------------------
    # 2) RUN EXTRACTOR
    # ----------------------------
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

        # ----------------------------
        # 3) SAVE JSON USING NAME
        # ----------------------------
        json_path = save_pid_json(
            pid_data=pid_data,
            metadata=usage_meta,
            image_path=saved_paths[0],
            out_dir="static/data",
            name=name or None,
        )

        # ----------------------------
        # 4) RELOAD JSON → same format as /api/search
        # ----------------------------
        base_name = name or Path(json_path).stem
        result = search_file(base_name, Path("static/data"))

    except Exception as e:
        logger.exception("Full extract failed")

        socketio.emit("file_status", {
            "status": "error",
            "file_name": name,
            "error": str(e),
        })

        return jsonify({"ok": False, "error": str(e)}), 500

    # ----------------------------
    # 5) CLEANUP ALL UPLOADED FILES
    # ----------------------------
    for path in saved_paths:
        try:
            Path(path).unlink(missing_ok=True)
            logger.info(f"cleaned file: {path}")
        except Exception as cleanup_err:
            logger.warning(f"Failed to remove {path}: {cleanup_err}")

    # (Optional extra cleanup: remove the folder if empty)
    try:
        if not any(upload_dir.iterdir()):
            upload_dir.rmdir()
            logger.info("removed empty uploads folder")
    except:
        pass

    # ----------------------------
    # 6) EMIT RESULT TO FRONTEND
    # ----------------------------
    time.sleep(2)
    socketio.emit("file_status", {
        "status": "loading_complete" if result.get("ok") else "error",
        "file_name": result.get("file_name", base_name),
        "error": result.get("error", ""),
    })

    return jsonify(result), (200 if result.get("ok") else 400)

@app.route("/api/search", methods=["GET"])
def api_search():
    name = request.args.get("name", "")

    logger.info("🟩 /api/search received")
    logger.info(f"search name = {name}")

    socketio.emit(
        "file_status",
        {
            "status": "working",
            "file_name": name,
            "error": "",
        },
    )

    result = search_file(name, DATA_DIR)

    status_code = 200
    if not result.get("ok", False):
        if result.get("error") == "File not found":
            status_code = 404
        else:
            status_code = 400
    time.sleep(2)
    socketio.emit(
        "file_status",
        {
            "status": "loading_complete" if result.get("ok") else "error",
            "file_name": result.get("file_name", name),
            "error": result.get("error", ""),
        },
    )
    logger.info(f"SocketIO emit: {result}")
    return jsonify(result), status_code

# ---------- HAZOP analysis agent via Socket.IO ----------
@socketio.on("hazop_start")
def handle_hazop_start(data):
    logger.info(f"hazop_start received: {len(data.get('selections', []))} selections")
    pid_data = data.get("pid_data", {})
    selections = data.get("selections", [])

    raw_name = (data.get("file_name") or "").strip()
    if not raw_name:
        raw_name = "hazop_output.xlsx"

    root, ext = os.path.splitext(raw_name)
    if not ext:
        raw_name = root + ".xlsx"

    file_name = raw_name

    output_folder = (data.get("output_folder") or "default").strip()
    if not output_folder:
        output_folder = "default"

    base_dir = os.path.join("static", "hazop", output_folder)
    os.makedirs(base_dir, exist_ok=True)

    excel_path = os.path.join(base_dir, file_name)
    token_log_path = os.path.join(base_dir, "token_log.csv")
    error_log_path = os.path.join(base_dir, "error_log.csv")
    llm_response_log_path = os.path.join(base_dir, "llm_response_log.csv")
    parsed_excel_path = os.path.join(base_dir, "parsed_rows.xlsx")

    logger.info(f"HAZOP start: {excel_path}")
    logger.info(f"Selections count: {len(selections)}")

    sid = request.sid

    def background_task():
        try:
            for key, tokens_used in run_hazop_agent(
                pid_data=pid_data,
                excel_path=excel_path,
                token_log_path=token_log_path,
                error_log_path=error_log_path,
                llm_response_log_path=llm_response_log_path,
                parsed_excel_path=parsed_excel_path,
                selections=selections,
            ):
                try:
                    line_id, param, guide_word = key.split(":")
                except ValueError:
                    line_id, param, guide_word = key, "", ""

                socketio.emit(
                    "hazop_progress",
                    {
                        "line_id": line_id,
                        "parameter": param,
                        "guide_word": guide_word,
                        "tokens_used": tokens_used,
                    },
                    room=sid,
                )

            socketio.emit(
                "hazop_complete",
                {
                    "ok": True,
                    "folder": base_dir,
                    "file_name": os.path.basename(excel_path),
                },
                room=sid,
            )

        except Exception as e:
            logger.exception(f"HAZOP background task error: {e}")
            socketio.emit(
                "hazop_complete",
                {
                    "ok": False,
                    "error": str(e),
                    "folder": base_dir,
                    "file_name": os.path.basename(excel_path),
                },
                room=sid,
            )

    socketio.start_background_task(background_task)

if __name__ == "__main__":
    logger.info("Starting Flask/SocketIO server on port 5000")
    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=True,
        allow_unsafe_werkzeug=True,
    )

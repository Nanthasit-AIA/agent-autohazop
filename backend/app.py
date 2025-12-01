from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO
from pathlib import Path
import os

from utils import search_file
from decorators import logger
from module.agent_module import run_hazop_agent


app = Flask(__name__, static_folder="static")
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

DATA_DIR = Path(app.root_path) / "static" / "data"


@app.before_request
def log_request():
    logger.info(
        f"➡️ {request.method} {request.path} | args={dict(request.args)} | form={dict(request.form)}"
    )


@app.route("/api/full", methods=["POST"])
def api_full():
    name = request.form.get("name", "")
    description = request.form.get("description", "")
    file = request.files.get("file")

    logger.info("🟦 /api/full received")
    logger.info(f"name: {name}")
    logger.info(f"description: {description}")
    logger.info(f"file: {file.filename if file else None}")

    # TODO: implement full extract pipeline
    return jsonify({"ok": True}), 200


@app.route("/api/search", methods=["GET"])
def api_search():
    name = request.args.get("name", "")

    logger.info("🟩 /api/search received")
    logger.info(f"search name = {name}")
    result = search_file(name, DATA_DIR)

    status_code = 200
    if not result.get("ok", False):
        if result.get("error") == "File not found":
            status_code = 404
        else:
            status_code = 400

    socketio.emit(
        "file_status",
        {
          "status": "loading_complete" if result.get("ok") else "error",
          "file_name": result.get("file_name", name),
          "error": result.get("error", "")
        },
    )
    logger.info(f"SocketIO emit: {result}")
    return jsonify(result), status_code


# ---------- HAZOP agent Socket.IO ----------
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

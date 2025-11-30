from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO
from pathlib import Path

from utils import search_file  # 👈 import from utils
from decorators import logger


app = Flask(__name__, static_folder="static")
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

DATA_DIR = Path(app.root_path) / "static" / "data"

@app.before_request
def log_request():
    logger.info(f"➡️ {request.method} {request.path} | args={dict(request.args)} | form={dict(request.form)}")


@app.route("/api/full", methods=["POST"])
def api_full():
    name = request.form.get("name", "")
    description = request.form.get("description", "")
    file = request.files.get("file")

    logger.info("🟦 /api/full received")
    logger.info(f"name: {name}")
    logger.info(f"description: {description}")
    logger.info(f"file: {file.filename if file else None}")

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

    # optional: emit status for your indicator animation
    socketio.emit("file_status", {
        "status": "loading_complete" if result.get("ok") else "error",
        "file_name": result.get("file_name", name),
        "error": result.get("error", "")
    })

    logger.info(f"SocketIO emit: {result}")

    return jsonify(result), status_code

if __name__ == "__main__":

    logger.info("🚀 Starting Flask + SocketIO server on port 5000")

    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=True,
        allow_unsafe_werkzeug=True,
    )


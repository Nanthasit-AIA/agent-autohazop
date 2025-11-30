from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO
from pathlib import Path

from utils import search_file  # 👈 import from utils

app = Flask(__name__, static_folder="static")
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

DATA_DIR = Path(app.root_path) / "static" / "data"


@app.route("/api/search", methods=["GET"])
def api_search():
    name = request.args.get("name", "")

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

    return jsonify(result), status_code

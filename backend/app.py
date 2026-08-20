import json, os, re, shutil, time
from datetime import datetime
from pathlib import Path

import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO

from utils import search_file, _slugify_filename
from decorators import logger
from module.ext_module import extract_pid, extract_pid_multi_files_single_call, _upload_vision_file
from module.agent_module import run_hazop_agent
from module.ag_template_modulee import run_hazop_agent_1
from module.hazop_export_module import hazop_lopa_preview_dataframe
from module.llm_module import (
    get_llm_config,
    get_llm_client,
    default_chat_model,
    model_presets_for_client,
)
from module.modify_module import modify_pid_json
from utils import save_pid_json

app = Flask(__name__, static_folder="static")
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
DATA_DIR = Path(app.root_path) / "static" / "data"


def sanitize_hazop_output_folder(value: str | None) -> str:
    """Reduce a client-supplied folder to a single safe path segment."""
    raw = str(value or "").strip().replace("\\", "/").strip("/")
    if not raw:
        return "default"

    lowered = raw.lower()
    for prefix in ("static/hazop/", "backend/static/hazop/"):
        if lowered.startswith(prefix):
            raw = raw[len(prefix):]
            lowered = raw.lower()
            break

    folder = Path(raw).name
    folder = re.sub(r"[^A-Za-z0-9._-]+", "_", folder).strip("._")
    return folder or "default"


def static_download_url(path: Path) -> str:
    static_root = Path(app.root_path) / "static"
    return f"/static/{path.resolve().relative_to(static_root.resolve()).as_posix()}"


def _json_safe(value):
    try:
        if pd.isna(value):
            return ""
    except (TypeError, ValueError):
        pass
    if isinstance(value, datetime):
        return value.isoformat()
    if hasattr(value, "item"):
        try:
            return value.item()
        except Exception:
            pass
    return value


def build_hazop_result_payload(
    excel_path: str,
    parsed_excel_path: str,
    token_log_path: str,
    error_log_path: str,
    row_limit: int = 200,
) -> dict:
    """Summary of a finished run for the UI: preview rows, totals and a download link."""
    payload = {
        "source_file": os.path.basename(excel_path),
        "download_url": "",
        "columns": [],
        "rows": [],
        "row_count": 0,
        "shown_count": 0,
        "truncated": False,
        "token_total": 0,
        "error_count": 0,
        "knowledge_sources": [],
        "payload_error": "",
    }

    try:
        if os.path.exists(excel_path):
            payload["download_url"] = static_download_url(Path(excel_path))

        # Prefer the plain parsed rows; the export workbook is styled, so its
        # machine-readable copy lives on the "Raw Data" sheet.
        df = None
        if os.path.exists(parsed_excel_path):
            df = pd.read_excel(parsed_excel_path)
        elif os.path.exists(excel_path):
            try:
                df = pd.read_excel(excel_path, sheet_name="Raw Data")
            except Exception:
                df = pd.read_excel(excel_path)

        if df is not None:
            preview = hazop_lopa_preview_dataframe(df).fillna("")
            payload["row_count"] = int(len(df))
            payload["truncated"] = len(preview) > row_limit
            preview = preview.head(row_limit)
            payload["shown_count"] = int(len(preview))
            payload["columns"] = [str(c) for c in preview.columns]
            payload["rows"] = [
                {str(k): _json_safe(v) for k, v in row.items()}
                for row in preview.to_dict(orient="records")
            ]

        if os.path.exists(token_log_path):
            token_df = pd.read_csv(token_log_path)
            if "TotalTokens" in token_df.columns:
                payload["token_total"] = int(
                    pd.to_numeric(token_df["TotalTokens"], errors="coerce").fillna(0).sum()
                )
            if "KnowledgeSources" in token_df.columns:
                sources = set()
                for value in token_df["KnowledgeSources"].dropna().astype(str):
                    for source in value.split("|"):
                        source = source.strip()
                        if source:
                            sources.add(source)
                payload["knowledge_sources"] = sorted(sources)

        if os.path.exists(error_log_path):
            payload["error_count"] = int(len(pd.read_csv(error_log_path)))
    except Exception as exc:
        logger.warning("Failed to build HAZOP result payload: %s", exc)
        payload["payload_error"] = str(exc)

    return payload


def remove_or_retarget_existing(path: str, suffix: str, label: str, reason: str) -> str:
    """Delete a previous artifact, or fall back to a suffixed path if it is locked.

    On Windows an open workbook cannot be deleted, so rather than failing the run
    we write to <name>_reanalysis_<timestamp><ext> instead.
    """
    if not os.path.exists(path):
        return path
    try:
        os.remove(path)
        logger.info(f"Removed previous HAZOP {label} for {reason}: {path}")
        return path
    except OSError as exc:
        root, ext = os.path.splitext(path)
        replacement = f"{root}_reanalysis_{suffix}{ext or '.xlsx'}"
        logger.warning(
            f"Could not remove previous HAZOP {label} for {reason}: {path}. "
            f"Using new artifact path {replacement}. Error: {exc}"
        )
        return replacement


def sanitize_hazop_file_name(value: str | None) -> str:
    """Reduce a client-supplied file name to a safe .xlsx leaf name."""
    raw = Path(str(value or "").strip()).name
    if not raw:
        raw = "hazop_output.xlsx"
    root, ext = os.path.splitext(raw)
    if not ext:
        raw = root + ".xlsx"
    return re.sub(r"[^A-Za-z0-9._ -]+", "_", raw).strip(" ._") or "hazop_output.xlsx"


@app.route("/api/llm-config", methods=["GET"])
def api_llm_config():
    return jsonify(get_llm_config())


@app.route("/api/models", methods=["GET"])
def api_models():
    presets = model_presets_for_client()
    default_preset = next((p for p in presets if p["configured"]), None)
    return jsonify({
        "ok": True,
        "default_model": default_preset["model"] if default_preset else default_chat_model,
        "default_provider": default_preset["provider"] if default_preset else "own_api",
        "models": [p["model"] for p in presets],
        "model_presets": presets,
    })


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
    node_define = request.form.get("node_define", "").strip()
    intention = request.form.get("intention", "").strip()
    llm_provider = request.form.get("llm_provider", "own_api").strip()
    llm_model = request.form.get("llm_model", "").strip() or None

    logger.info("🟦 /api/full received")
    logger.info(f"name: {name}")
    logger.info(f"description: {description}")
    logger.info(f"llm_provider: {llm_provider}, llm_model: {llm_model}")

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
        extract_kwargs = {
            "process_description": description,
            "node_define": node_define,
            "intention": intention,
            "llm_provider": llm_provider,
        }
        if llm_model:
            extract_kwargs["model"] = llm_model

        if len(saved_paths) == 1:
            pid_data, usage_meta = extract_pid(saved_paths[0], **extract_kwargs)
        else:
            pid_data, usage_meta = extract_pid_multi_files_single_call(saved_paths, **extract_kwargs)

        # ----------------------------
        # 3) PERSIST SOURCE IMAGES before saving JSON
        # ----------------------------
        base_name = _slugify_filename(name) if name else Path(saved_paths[0]).stem
        sources_dir = Path("static") / "data" / "sources" / base_name
        sources_dir.mkdir(parents=True, exist_ok=True)
        source_files_urls = []
        for p in saved_paths:
            src = Path(p)
            dest = sources_dir / src.name
            shutil.copy2(src, dest)
            source_files_urls.append(f"/static/data/sources/{base_name}/{src.name}")
        usage_meta["source_files"] = source_files_urls

        # ----------------------------
        # 4) SAVE JSON USING NAME
        # ----------------------------
        json_path = save_pid_json(
            pid_data=pid_data,
            metadata=usage_meta,
            image_path=saved_paths[0],
            out_dir="static/data",
            name=name or None,
        )

        # ----------------------------
        # 5) RELOAD JSON → same format as /api/search
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


# ---------- Modify / Fix existing JSON ----------
@app.route("/api/modify", methods=["POST"])
def api_modify():
    file_name = request.form.get("file_name", "").strip()
    instruction = request.form.get("instruction", "").strip()
    llm_provider = request.form.get("llm_provider", "own_api").strip()
    llm_model = request.form.get("llm_model", "").strip() or None

    if not file_name:
        return jsonify({"ok": False, "error": "file_name is required"}), 400
    if not instruction:
        return jsonify({"ok": False, "error": "instruction is required"}), 400

    # Strip .json extension if present so we get the bare base name
    base_name = file_name[:-5] if file_name.endswith(".json") else file_name

    client = get_llm_client(llm_provider)
    file_ids: list[str] = []
    upload_dir = Path("static") / "uploads"
    upload_dir.mkdir(parents=True, exist_ok=True)
    user_saved: list[Path] = []

    # Upload any user-provided file
    for f in request.files.getlist("file"):
        if not f.filename:
            continue
        p = upload_dir / f.filename
        f.save(p)
        user_saved.append(p)
        try:
            fid = _upload_vision_file(str(p), client)
            file_ids.append(fid)
        except Exception as e:
            logger.warning("Failed to upload user file %s: %s", f.filename, e)

    # Attach original P&ID images from metadata.source_files
    json_path = Path("static/data") / f"{base_name}.json"
    if json_path.exists():
        try:
            saved_data = json.loads(json_path.read_text(encoding="utf-8"))
            for url in (saved_data.get("metadata") or {}).get("source_files", []):
                local = Path(url.lstrip("/"))
                if local.exists():
                    try:
                        fid = _upload_vision_file(str(local), client)
                        file_ids.append(fid)
                    except Exception as e:
                        logger.warning("Failed to upload source image %s: %s", local, e)
        except Exception as e:
            logger.warning("Could not read source_files from %s: %s", json_path, e)

    try:
        new_combined, _ = modify_pid_json(
            file_name=base_name,
            instruction=instruction,
            file_ids=file_ids,
            llm_provider=llm_provider,
            model=llm_model or "gpt-5.5-2026-04-23",
        )
    except ValueError as e:
        return jsonify({"ok": False, "error": f"Validation failed: {e}"}), 422
    except Exception as e:
        logger.exception("modify_pid_json failed")
        return jsonify({"ok": False, "error": str(e)}), 500
    finally:
        for p in user_saved:
            p.unlink(missing_ok=True)

    return jsonify({"ok": True, "data": new_combined, "file_name": f"{base_name}.json"})


# ---------- HAZOP analysis agent via Socket.IO ----------
@socketio.on("hazop_start")
def handle_hazop_start(data):
    logger.info(f"hazop_start received: {len(data.get('selections', []))} selections")
    pid_data = data.get("pid_data", {})
    selections = data.get("selections", [])
    llm_provider = (data.get("llm_provider") or "own_api").strip()
    llm_model = (data.get("llm_model") or "").strip() or None

    file_name = sanitize_hazop_file_name(data.get("file_name"))
    output_folder = sanitize_hazop_output_folder(data.get("output_folder"))

    base_dir = os.path.join("static", "hazop", output_folder)
    os.makedirs(base_dir, exist_ok=True)

    excel_path = os.path.join(base_dir, file_name)
    token_log_path = os.path.join(base_dir, "token_log.csv")
    error_log_path = os.path.join(base_dir, "error_log.csv")
    llm_response_log_path = os.path.join(base_dir, "llm_response_log.csv")
    parsed_excel_path = os.path.join(base_dir, "parsed_rows.xlsx")

    # Re-analysis control. append_output keeps prior rows (the previous behaviour);
    # reset_output and the default both start clean, so a re-run does not silently
    # accumulate rows from earlier runs into the same workbook.
    reset_output = bool(data.get("reset_output"))
    append_output = bool(data.get("append_output"))

    if not append_output:
        reason = "re-analysis" if reset_output else "fresh analysis"
        suffix = datetime.now().strftime("%Y%m%d_%H%M%S")
        excel_path = remove_or_retarget_existing(excel_path, suffix, "export workbook", reason)
        file_name = os.path.basename(excel_path)
        parsed_excel_path = remove_or_retarget_existing(parsed_excel_path, suffix, "parsed raw workbook", reason)
        token_log_path = remove_or_retarget_existing(token_log_path, suffix, "token log", reason)
        error_log_path = remove_or_retarget_existing(error_log_path, suffix, "error log", reason)
        llm_response_log_path = remove_or_retarget_existing(llm_response_log_path, suffix, "LLM response log", reason)

    logger.info(f"HAZOP start: {excel_path}")
    logger.info(f"Selections count: {len(selections)}")

    sid = request.sid

    def background_task():
        try:
            hazop_kwargs = {
                "pid_data": pid_data,
                "excel_path": excel_path,
                "token_log_path": token_log_path,
                "error_log_path": error_log_path,
                "llm_response_log_path": llm_response_log_path,
                "parsed_excel_path": parsed_excel_path,
                "selections": selections,
                "llm_provider": llm_provider,
            }
            if llm_model:
                hazop_kwargs["model_name"] = llm_model

            for key, tokens_used in run_hazop_agent_1(**hazop_kwargs):
                try:
                    line_id, param, guide_word = key.split(":", 2)
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
                    "result": build_hazop_result_payload(
                        excel_path, parsed_excel_path, token_log_path, error_log_path
                    ),
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
                    "result": build_hazop_result_payload(
                        excel_path, parsed_excel_path, token_log_path, error_log_path
                    ),
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

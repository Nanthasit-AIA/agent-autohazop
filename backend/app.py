import hashlib
import hmac
import json
import os, re
import zipfile
from datetime import datetime
from io import BytesIO
from pathlib import Path

import pandas as pd
from flask import Flask, abort, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO

from decorators import logger
from module.agent_module import run_hazop_agent
from module.assistant_module import run_hazop_assistant
from module.ag_template_modulee import run_hazop_agent_1
from module.hazop_export_module import hazop_lopa_preview_dataframe
from module import hazop_store
from module.llm_module import (
    default_chat_model,
    model_presets_for_client,
)

app = Flask(__name__, static_folder="static")
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Shared-secret gate, matching services/pid-extract. Unset means open, which is
# right for local dev; set it whenever this is reachable from outside the
# machine, since a HAZOP run spends real LLM budget.
DEMO_TOKEN = os.getenv("DEMO_TOKEN", "").strip()

ASSISTANT_FILE_MAX_FILES = int(os.getenv("ASSISTANT_FILE_MAX_FILES", "4"))
ASSISTANT_FILE_MAX_BYTES = int(os.getenv("ASSISTANT_FILE_MAX_BYTES", str(8 * 1024 * 1024)))
ASSISTANT_FILE_TEXT_LIMIT = int(os.getenv("ASSISTANT_FILE_TEXT_LIMIT", "12000"))
# Refuse an oversized body at the socket instead of buffering it, since the
# per-file check below only runs once the upload is already in memory.
app.config["MAX_CONTENT_LENGTH"] = ASSISTANT_FILE_MAX_FILES * ASSISTANT_FILE_MAX_BYTES + 2 * 1024 * 1024


@app.before_request
def require_token():
    """Same gate as services/pid-extract: /api/ only, so /static/ downloads
    (which are plain <a download> links and cannot send a header) still work."""
    if not DEMO_TOKEN or request.method == "OPTIONS":
        return None
    if not request.path.startswith("/api/"):
        return None
    supplied = request.headers.get("X-Demo-Token") or request.args.get("token", "")
    if not hmac.compare_digest(supplied, DEMO_TOKEN):
        logger.warning("Rejected %s %s: bad or missing token", request.method, request.path)
        return jsonify({"ok": False, "error": "Unauthorized"}), 401
    return None


@socketio.on("connect")
def handle_connect(auth):
    if DEMO_TOKEN and (not auth or auth.get("token") != DEMO_TOKEN):
        logger.warning("Rejected socket connection: bad or missing token")
        return False
    return None


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


def limit_text(text: str, limit: int = ASSISTANT_FILE_TEXT_LIMIT):
    text = text or ""
    if len(text) <= limit:
        return text, False
    return text[:limit].rstrip(), True

def decode_upload_text(raw: bytes) -> str:
    for encoding in ("utf-8-sig", "utf-16", "cp874", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")

def is_probably_text(raw: bytes) -> bool:
    sample = raw[:4096]
    if not sample:
        return False
    if b"\x00" in sample:
        return False
    control_bytes = sum(1 for byte in sample if byte < 32 and byte not in {9, 10, 12, 13})
    return control_bytes / max(len(sample), 1) < 0.08

def dataframe_preview_text(df: pd.DataFrame, row_limit: int = 30) -> str:
    df = df.fillna("")
    df = df.loc[:, ~df.columns.astype(str).str.startswith("Unnamed")]
    preview = df.head(row_limit)
    return preview.to_csv(index=False)

def archive_preview_text(raw: bytes, limit: int = 80) -> str:
    with zipfile.ZipFile(BytesIO(raw)) as archive:
        names = archive.namelist()[:limit]
    if not names:
        return "Archive contains no readable file entries."
    return "Archive file list:\n" + "\n".join(f"- {name}" for name in names)

def binary_preview_text(raw: bytes, filename: str, mimetype: str = "") -> str:
    digest = hashlib.sha256(raw).hexdigest()
    hex_preview = raw[:96].hex(" ")
    lines = [
        "Binary or unsupported structured file accepted.",
        f"Filename: {filename}",
        f"MIME type: {mimetype or 'unknown'}",
        f"Size bytes: {len(raw)}",
        f"SHA256: {digest}",
    ]
    if hex_preview:
        lines.append(f"First 96 bytes (hex): {hex_preview}")
    lines.append("Text content was not extracted. Use this file as attachment metadata only unless a parser is added.")
    return "\n".join(lines)

def extract_assistant_upload(file_storage):
    filename = Path(file_storage.filename or "uploaded_file").name
    extension = Path(filename).suffix.lower()
    mimetype = str(getattr(file_storage, "mimetype", "") or "")
    payload = {
        "filename": filename,
        "extension": extension,
        "mimetype": mimetype,
        "size_bytes": 0,
        "text": "",
        "truncated": False,
        "error": "",
        "extraction_method": "",
        "extraction_note": "",
    }

    try:
        raw = file_storage.read()
        payload["size_bytes"] = len(raw)

        if not raw:
            payload["error"] = "Uploaded file is empty."
            return payload

        if len(raw) > ASSISTANT_FILE_MAX_BYTES:
            payload["error"] = f"File is larger than {ASSISTANT_FILE_MAX_BYTES // (1024 * 1024)} MB and was not read."
            return payload

        if extension in {".txt", ".md", ".csv", ".json", ".log"}:
            text = decode_upload_text(raw)
            payload["extraction_method"] = "text"
        elif extension in {".xlsx", ".xls"}:
            sheets = pd.read_excel(BytesIO(raw), sheet_name=None, nrows=80)
            sheet_texts = []
            for sheet_name, df in list(sheets.items())[:6]:
                columns = ", ".join(str(col) for col in df.columns)
                sheet_texts.append(
                    f"Sheet: {sheet_name}\nColumns: {columns}\nPreview:\n{dataframe_preview_text(df)}"
                )
            text = "\n\n".join(sheet_texts)
            payload["extraction_method"] = "spreadsheet"
        elif extension == ".pdf":
            try:
                try:
                    from pypdf import PdfReader
                except Exception:
                    from PyPDF2 import PdfReader

                reader = PdfReader(BytesIO(raw))
                pages = []
                for idx, page in enumerate(reader.pages[:8]):
                    pages.append(f"Page {idx + 1}:\n{page.extract_text() or ''}")
                text = "\n\n".join(pages)
                payload["extraction_method"] = "pdf"
            except Exception as exc:
                payload["error"] = f"PDF text extraction is not available: {exc}"
                text = binary_preview_text(raw, filename, mimetype)
                payload["extraction_method"] = "binary_metadata"
        elif extension == ".docx":
            try:
                from docx import Document

                doc = Document(BytesIO(raw))
                text = "\n".join(paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip())
                payload["extraction_method"] = "docx"
            except Exception as exc:
                payload["error"] = f"DOCX text extraction is not available: {exc}"
                text = binary_preview_text(raw, filename, mimetype)
                payload["extraction_method"] = "binary_metadata"
        elif extension == ".pptx":
            try:
                from pptx import Presentation

                prs = Presentation(BytesIO(raw))
                slide_texts = []
                for idx, slide in enumerate(prs.slides[:30], start=1):
                    texts = []
                    for shape in slide.shapes:
                        if hasattr(shape, "text") and str(shape.text or "").strip():
                            texts.append(str(shape.text).strip())
                    if texts:
                        slide_texts.append(f"Slide {idx}:\n" + "\n".join(texts))
                text = "\n\n".join(slide_texts) or "PowerPoint file accepted, but no text was extracted from slide shapes."
                payload["extraction_method"] = "pptx"
            except Exception as exc:
                payload["error"] = f"PPTX text extraction is not available: {exc}"
                text = binary_preview_text(raw, filename, mimetype)
                payload["extraction_method"] = "binary_metadata"
        else:
            if is_probably_text(raw) or mimetype.startswith("text/"):
                text = decode_upload_text(raw)
                payload["extraction_method"] = "generic_text"
            elif zipfile.is_zipfile(BytesIO(raw)):
                try:
                    text = archive_preview_text(raw)
                    payload["extraction_method"] = "archive_listing"
                    payload["extraction_note"] = "Archive content was not deeply extracted; only the file list was read."
                except Exception as exc:
                    payload["error"] = f"Archive listing is not available: {exc}"
                    text = binary_preview_text(raw, filename, mimetype)
                    payload["extraction_method"] = "binary_metadata"
            else:
                text = binary_preview_text(raw, filename, mimetype)
                payload["extraction_method"] = "binary_metadata"
                payload["extraction_note"] = "File was accepted, but text could not be extracted from this binary format."

        payload["text"], payload["truncated"] = limit_text(text)
    except Exception as exc:
        logger.exception("Failed to extract assistant upload")
        payload["error"] = str(exc)

    return payload

def parse_assistant_payload():
    if request.files or request.form.get("payload"):
        raw_payload = request.form.get("payload") or "{}"
        try:
            payload = json.loads(raw_payload)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid assistant payload JSON: {exc}") from exc

        if not isinstance(payload, dict):
            payload = {}

        upload_files = request.files.getlist("files") + request.files.getlist("file")
        valid_uploads = [item for item in upload_files if item and item.filename]
        payload["uploaded_files"] = [
            extract_assistant_upload(item)
            for item in valid_uploads[:ASSISTANT_FILE_MAX_FILES]
        ]

        if len(valid_uploads) > ASSISTANT_FILE_MAX_FILES:
            payload["uploaded_file_warning"] = (
                f"Only the first {ASSISTANT_FILE_MAX_FILES} files were read."
            )

        return payload

    return request.get_json(silent=True) or {}

@app.route("/static/hazop/<path:subpath>")
def hazop_static(subpath):
    """Serve a generated workbook, restoring it from Blob if the disk copy is
    gone. Stays outside /api/ because the download is a plain <a download>
    link, which cannot send the token header."""
    base = (Path(app.root_path) / "static" / "hazop").resolve()
    target = (base / subpath).resolve()
    if base != target and base not in target.parents:
        abort(404)
    if not hazop_store.ensure_local(target):
        abort(404)
    return send_from_directory(target.parent, target.name)


@app.route("/api/assistant/chat", methods=["POST"])
def api_assistant_chat():
    try:
        payload = parse_assistant_payload()
        result = run_hazop_assistant(payload)
        return jsonify({"ok": True, **result}), 200
    except ValueError as e:
        return jsonify({"ok": False, "error": str(e)}), 400
    except Exception as e:
        logger.exception("HAZOP assistant failed")
        return jsonify({"ok": False, "error": str(e)}), 500


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

            hazop_store.mirror([excel_path, parsed_excel_path])
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
            hazop_store.mirror([excel_path, parsed_excel_path])
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

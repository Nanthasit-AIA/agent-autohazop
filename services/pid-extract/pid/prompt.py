import base64
from pathlib import Path
from typing import Sequence

_PROMPT_DIR = Path(__file__).parent

def _load_skill() -> tuple[str, str]:
    system = (_PROMPT_DIR / "skill.md").read_text(encoding="utf-8")
    user_template = (_PROMPT_DIR / "skill_user.md").read_text(encoding="utf-8")
    return system, user_template

PID_SYSTEM_PROMPT, _PID_USER_TEMPLATE = _load_skill()

MIME_BY_SUFFIX = {
    ".pdf": "application/pdf",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
}

def content_part(filename: str, data: bytes) -> dict:
    """
    Inline one uploaded file as a Responses API content part.

    The LiteLLM proxy does not expose the Files API (it answers
    "files_settings is not set"), so bytes travel in the request as a data URI
    rather than being uploaded first and referenced by id.
    """
    suffix = Path(filename).suffix.lower()
    mime = MIME_BY_SUFFIX.get(suffix)
    if mime is None:
        raise ValueError(f"Unsupported file type for extraction: {filename}")

    data_uri = f"data:{mime};base64,{base64.b64encode(data).decode()}"

    if mime == "application/pdf":
        return {"type": "input_file", "filename": filename, "file_data": data_uri}
    return {"type": "input_image", "image_url": data_uri}

def build_pid_input(
    process_description: str,
    files: Sequence[tuple[str, bytes]],
    *,
    node_define: str = "",
    intention: str = "",
) -> list[dict]:
    """`files` is a sequence of (filename, raw bytes)."""
    node_define_text = node_define.strip() or "(not provided — auto-define nodes based on the P&ID layout)"
    intention_text = intention.strip() or "(not provided — derive from P&ID and process description)"

    user_text = _PID_USER_TEMPLATE.format(
        node_define=node_define_text,
        intention=intention_text,
        process_description=process_description,
    )

    content: list[dict] = [{"type": "input_text", "text": user_text}]
    content.extend(content_part(name, data) for name, data in files)

    return [{"role": "user", "content": content}]

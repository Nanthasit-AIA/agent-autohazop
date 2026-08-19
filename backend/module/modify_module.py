import copy
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Any

from module.llm_module import get_llm_client, build_llm_metadata
from module.schema_json import PIDResponse
from decorators import logger, timeit_log

_PROMPT_DIR = Path(__file__).parent / "prompt"
MODIFY_SYSTEM_PROMPT = (_PROMPT_DIR / "skill_modify_json.md").read_text(encoding="utf-8")

DEFAULT_MODEL = "gpt-5.5-2026-04-23"

# Maps section name → the field used as item identifier
_ID_FIELD: dict[str, str | None] = {
    "equipment": "id",
    "valves": "id",
    "instruments": "id",
    "connections": "line_id",
    "line_level_connections": "line_id",
    "node_define": "node_id",
    "utility_lines": "utility_type",
    "system_inputs": None,
    "system_outputs": None,
    "process_description": None,
    "intention": None,
}


def _strip_code_fence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        start = 1
        end = len(lines) - 1 if lines[-1].strip() == "```" or lines[-1].strip().startswith("```") else len(lines)
        text = "\n".join(lines[start:end]).strip()
    return text


def _get_output_text(resp: Any) -> str:
    text = getattr(resp, "output_text", None)
    if text:
        return str(text)
    chunks = []
    for item in (getattr(resp, "output", None) or []):
        for c in (getattr(item, "content", None) or []):
            t = getattr(c, "text", None)
            if t:
                chunks.append(str(t))
    return "\n".join(chunks)


def _apply_patches(pid_data: dict, patches: list[dict]) -> dict:
    result = copy.deepcopy(pid_data)

    for patch in patches:
        section = patch.get("section")
        op = patch.get("op")
        patch_id = patch.get("id")
        value = patch.get("value")

        if not section or not op:
            logger.warning("Skipping malformed patch: %s", patch)
            continue

        if section not in _ID_FIELD:
            logger.warning("Unknown section in patch: %s", section)
            continue

        id_field = _ID_FIELD[section]

        if id_field is None:
            # Primitive or whole-list field
            if op == "replace":
                result[section] = value
        else:
            items = result.get(section)
            if not isinstance(items, list):
                items = []

            if op == "replace":
                result[section] = [
                    value if str(item.get(id_field, "")) == str(patch_id) else item
                    for item in items
                ]
            elif op == "add":
                items = list(items)
                items.append(value)
                result[section] = items
            elif op == "remove":
                result[section] = [
                    item for item in items
                    if str(item.get(id_field, "")) != str(patch_id)
                ]

    return result


@timeit_log
def modify_pid_json(
    file_name: str,
    instruction: str,
    file_ids: list[str],
    *,
    llm_provider: str = "own_api",
    model: str = DEFAULT_MODEL,
    data_dir: str = "static/data",
) -> tuple[dict, dict]:
    """Apply a targeted LLM patch to a saved P&ID JSON file.

    Returns (new_combined_dict, usage_meta).
    Raises ValueError if the patched document fails PIDResponse validation.
    Raises RuntimeError if LLM call fails or patch JSON is unparseable.
    """
    json_path = Path(data_dir) / f"{file_name}.json"
    if not json_path.exists():
        raise FileNotFoundError(f"JSON not found: {json_path}")

    combined = json.loads(json_path.read_text(encoding="utf-8"))
    pid_data: dict = combined.get("pid_data", combined)
    old_metadata: dict = combined.get("metadata", {})

    client = get_llm_client(llm_provider)

    content: list[dict] = [
        {
            "type": "input_text",
            "text": (
                f"Current P&ID JSON:\n{json.dumps(pid_data, ensure_ascii=False)}"
                f"\n\nModification request:\n{instruction}"
            ),
        }
    ]
    content.extend({"type": "input_file", "file_id": fid} for fid in file_ids)

    start = time.perf_counter()
    resp = client.responses.create(
        model=model,
        instructions=MODIFY_SYSTEM_PROMPT,
        input=[{"role": "user", "content": content}],
    )
    latency = time.perf_counter() - start

    raw_text = _get_output_text(resp)
    clean_text = _strip_code_fence(raw_text)

    try:
        patches = json.loads(clean_text)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"LLM did not return valid JSON patch: {e}\nRaw: {raw_text[:500]}") from e

    if not isinstance(patches, list):
        raise RuntimeError(f"Expected JSON array of patches, got: {type(patches).__name__}")

    new_pid_data = _apply_patches(pid_data, patches)

    try:
        PIDResponse(**new_pid_data)
    except Exception as exc:
        raise ValueError(f"Patched document failed schema validation: {exc}") from exc

    usage_meta = build_llm_metadata(resp, latency)
    usage_meta["modified_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    usage_meta["source_files"] = old_metadata.get("source_files", [])

    new_combined = {"pid_data": new_pid_data, "metadata": usage_meta}
    json_path.write_text(json.dumps(new_combined, indent=2, ensure_ascii=False), encoding="utf-8")

    logger.info("modify_pid_json: applied %d patch(es) to %s", len(patches), json_path)
    return new_combined, usage_meta

import copy
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Sequence

from .llm import get_llm_client, build_llm_metadata, default_model
from .schema import PIDResponse
from .prompt import content_part
from .logging_conf import logger, timeit_log

MODIFY_SYSTEM_PROMPT = (Path(__file__).parent / "skill_modify_json.md").read_text(encoding="utf-8")

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
    combined: dict,
    instruction: str,
    files: Sequence[tuple[str, bytes]] = (),
    *,
    llm_provider: str = "litellm",
    model: str | None = None,
) -> tuple[dict, dict]:
    """Apply a targeted LLM patch to a P&ID document.

    `combined` is the stored {"pid_data", "metadata"} document; `files` are
    (filename, bytes) pairs of the source drawings, inlined for the model.
    Loading and saving are the caller's job, so this works against any store.

    Returns (new_combined_dict, usage_meta).
    Raises ValueError if the patched document fails PIDResponse validation.
    Raises RuntimeError if LLM call fails or patch JSON is unparseable.
    """
    pid_data: dict = combined.get("pid_data", combined)
    old_metadata: dict = combined.get("metadata", {})

    client = get_llm_client(llm_provider)
    model = model or default_model(llm_provider)

    content: list[dict] = [
        {
            "type": "input_text",
            "text": (
                f"Current P&ID JSON:\n{json.dumps(pid_data, ensure_ascii=False)}"
                f"\n\nModification request:\n{instruction}"
            ),
        }
    ]
    content.extend(content_part(name, data) for name, data in files)

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

    usage_meta = build_llm_metadata(resp, latency, llm_provider)
    usage_meta["modified_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    usage_meta["inputs"] = old_metadata.get("inputs", [])

    new_combined = {"pid_data": new_pid_data, "metadata": usage_meta}

    logger.info("modify_pid_json: applied %d patch(es)", len(patches))
    return new_combined, usage_meta

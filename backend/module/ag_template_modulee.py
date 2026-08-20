from __future__ import annotations

import csv
import io
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional, Tuple

import pandas as pd

from decorators import logger, timeit_log
from module.knowledge_module import build_generation_knowledge_context
from module.llm_module import get_openai_sdk, get_llm_client, build_llm_metadata, _call_with_retries
from module.prompt.hzp_promptt import (
    HAZOP_LOPA_HEADERS_20,
    build_file_search_hazop_prompt,
)

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


SUPPORTED_VECTOR_FILE_EXTENSIONS = {
    ".pdf", ".txt", ".md", ".json", ".jsonl", ".csv", ".py",
    ".yaml", ".yml", ".docx", ".xlsx", ".xls",
}

DEFAULT_VECTOR_STORE_CONFIG_PATH = "hazop_vector_store_config.json"
DEFAULT_VECTOR_STORE_NAME = "hazop_db"
DEFAULT_RESPONSES_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5-2026-04-23")

# Where HAZOP reference knowledge comes from.
#   "local"              -> local skill/standards library via knowledge_module (no vector store)
#   "openai_file_search" -> OpenAI hosted vector store via the file_search tool
KNOWLEDGE_SOURCE_LOCAL = "local"
KNOWLEDGE_SOURCE_FILE_SEARCH = "openai_file_search"
DEFAULT_KNOWLEDGE_SOURCE = (
    os.getenv("HAZOP_KNOWLEDGE_SOURCE", KNOWLEDGE_SOURCE_LOCAL).strip().lower()
    or KNOWLEDGE_SOURCE_LOCAL
)


def knowledge_sources_from_context(context_text: str) -> List[str]:
    """Pull the SOURCE: lines out of a built knowledge context, for trace logging."""
    sources: List[str] = []
    for line in str(context_text or "").splitlines():
        if line.startswith("SOURCE: "):
            source = line[len("SOURCE: "):].strip()
            if source and source not in sources:
                sources.append(source)
    return sources


# =============================================================================
# Vector store setup - Option 2: upload files once and reuse vector_store_id
# =============================================================================

def collect_supported_files(source_folder: str | os.PathLike[str]) -> List[Path]:
    """Collect files that can be uploaded to OpenAI vector stores."""
    folder = Path(source_folder)
    if not folder.exists():
        raise FileNotFoundError(f"source_folder not found: {folder}")
    if not folder.is_dir():
        raise NotADirectoryError(f"source_folder is not a directory: {folder}")

    files = [
        path for path in folder.rglob("*")
        if path.is_file() and path.suffix.lower() in SUPPORTED_VECTOR_FILE_EXTENSIONS
    ]
    files = sorted(files, key=lambda p: str(p).lower())
    if not files:
        raise ValueError(f"No supported files found under {folder}")
    return files


@timeit_log
def create_hazop_vector_store_from_folder(
    source_folder: str | os.PathLike[str],
    *,
    vector_store_name: str = DEFAULT_VECTOR_STORE_NAME,
    config_path: str | os.PathLike[str] = DEFAULT_VECTOR_STORE_CONFIG_PATH,
) -> str:
    client = get_openai_sdk()
    files = collect_supported_files(source_folder)

    vector_store = client.vector_stores.create(name=vector_store_name)
    vector_store_id = vector_store.id

    streams = []
    try:
        for path in files:
            streams.append(open(path, "rb"))
        batch = client.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store_id,
            files=streams,
        )
    finally:
        for stream in streams:
            try:
                stream.close()
            except Exception:
                pass

    config = {
        "vector_store_id": vector_store_id,
        "vector_store_name": vector_store_name,
        "source_folder": str(Path(source_folder).resolve()),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "file_count": len(files),
        "files": [str(path) for path in files],
        "batch_status": getattr(batch, "status", None),
        "batch_file_counts": getattr(batch, "file_counts", None).model_dump()
        if hasattr(getattr(batch, "file_counts", None), "model_dump")
        else str(getattr(batch, "file_counts", "")),
    }
    Path(config_path).write_text(json.dumps(config, indent=2), encoding="utf-8")
    return vector_store_id


def load_vector_store_id(
    config_path: str | os.PathLike[str] = DEFAULT_VECTOR_STORE_CONFIG_PATH,
) -> Optional[str]:
    """Load vector_store_id from environment or config file."""
    env_id = os.getenv("HAZOP_VECTOR_STORE_ID")
    if env_id:
        return env_id.strip()

    path = Path(config_path)
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
        vector_store_id = data.get("vector_store_id")
        if vector_store_id:
            return str(vector_store_id).strip()
    return None


def get_or_create_vector_store_id(
    *,
    vector_store_id: Optional[str] = None,
    source_folder: Optional[str | os.PathLike[str]] = None,
    config_path: str | os.PathLike[str] = DEFAULT_VECTOR_STORE_CONFIG_PATH,
    create_if_missing: bool = False,
) -> str:
    """Resolve vector_store_id for File Search.

    Priority:
    1) explicit vector_store_id argument
    2) HAZOP_VECTOR_STORE_ID in .env
    3) config file
    4) create from source_folder only when create_if_missing=True
    """
    if vector_store_id:
        return vector_store_id.strip()

    loaded_id = load_vector_store_id(config_path)
    if loaded_id:
        return loaded_id

    if create_if_missing and source_folder:
        return create_hazop_vector_store_from_folder(
            source_folder,
            config_path=config_path,
        )

    raise ValueError(
        "No vector_store_id found. Run create_hazop_vector_store_from_folder(...) once, "
        "set HAZOP_VECTOR_STORE_ID in .env, or pass vector_store_id=... to run_hazop_agent_1."
    )


# =============================================================================
# P&ID topology parsing
# =============================================================================

def _extract_parsed_pid_data(pid_data: dict) -> dict:
    """Return the actual parsed P&ID payload from supported API/JSON shapes.

    Supported input formats:
    1) OpenAI parsed response style:
       {"choices": [{"message": {"parsed": {...}}}]}
    2) Wrapped saved file style:
       {"pid_data": {...}, "metadata": {...}}
    3) Direct topology style:
       {"process_description": ..., "equipment": ..., "connections": ...}
    4) Optional generic wrapper:
       {"parsed": {...}}
    """
    if not isinstance(pid_data, dict):
        raise TypeError(f"pid_data must be dict; got {type(pid_data).__name__}")

    if "choices" in pid_data:
        choices = pid_data.get("choices") or []
        if choices and isinstance(choices[0], dict):
            message = choices[0].get("message") or {}
            if isinstance(message, dict):
                parsed = message.get("parsed")
                if isinstance(parsed, dict):
                    return parsed

                # Some saved responses may store JSON in message.content.
                content = message.get("content")
                if isinstance(content, str) and content.strip():
                    try:
                        parsed_content = json.loads(content)
                        if isinstance(parsed_content, dict):
                            return parsed_content.get("pid_data", parsed_content)
                    except Exception:
                        pass

    wrapped = pid_data.get("pid_data")
    if isinstance(wrapped, dict):
        return wrapped

    parsed = pid_data.get("parsed")
    if isinstance(parsed, dict):
        return parsed

    return pid_data


def _safe_json_dumps(data: Any, *, max_chars: Optional[int] = None) -> str:
    """Compact JSON text for passing the complete P&ID payload to the LLM."""
    try:
        text = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    except TypeError:
        text = json.dumps(str(data), ensure_ascii=False)

    if max_chars is not None and max_chars > 0 and len(text) > max_chars:
        return text[:max_chars] + "...[TRUNCATED]"
    return text


def _as_id_list(items: Any) -> List[str]:
    """Normalize a list of ids/dicts into a list of string ids."""
    if items is None:
        return []
    if not isinstance(items, list):
        items = [items]

    out: List[str] = []
    for item in items:
        if isinstance(item, dict):
            value = item.get("id") or item.get("tag") or item.get("name") or item.get("line_id")
        else:
            value = item
        if value is not None and str(value).strip():
            out.append(str(value).strip())
    return out


def _lookup_catalog_records(ids: List[str], catalog_by_id: Dict[str, dict]) -> List[dict]:
    records: List[dict] = []
    for item_id in ids:
        records.append(catalog_by_id.get(item_id, {"id": item_id}))
    return records


def _fallback_ref(ref_id: Any, catalog_by_id: Dict[str, dict]) -> Optional[dict]:
    if ref_id is None or str(ref_id).strip() == "":
        return None
    ref = str(ref_id).strip()
    return catalog_by_id.get(ref, {"id": ref, "name": ref, "type": "external_or_boundary_reference", "context": "Boundary or external reference not listed in equipment catalog."})


def _match_related_utilities(
    utility_lines: List[Any],
    *,
    ids_to_match: List[str],
    valve_ids: List[str],
) -> List[dict]:
    """Find utilities related to selected connection by text match or valve overlap."""
    related: List[dict] = []
    match_terms = [str(x).lower() for x in ids_to_match if x]
    valve_set = set(valve_ids)

    for utility in utility_lines:
        if not isinstance(utility, dict):
            continue

        util_valves = set(_as_id_list(utility.get("valves", [])))
        if valve_set and util_valves and valve_set.intersection(util_valves):
            related.append(utility)
            continue

        text = _safe_json_dumps(utility).lower()
        if any(term and term in text for term in match_terms):
            related.append(utility)

    return related


@timeit_log
def list_all_process(pid_data: dict) -> List[dict]:
    """Return process-level information from either wrapped or direct P&ID JSON."""
    parsed = _extract_parsed_pid_data(pid_data)

    return [{
        "system_input": parsed.get("system_inputs", []),
        "system_output": parsed.get("system_outputs", []),
        "process_description": parsed.get("process_description", ""),
        "intention": parsed.get("intention", parsed.get("design_intention", "")),
        "full_pid_json": _safe_json_dumps(parsed),
    }]


def list_all_connections(pid_data: dict) -> List[dict]:
    """Extract node-level topology packages from multiple P&ID JSON formats.

    Handles both common formats used in this project:
    - direct/wrapped P&ID topology with equipment/valves/instruments/connections;
    - grouped node format with connection-level fields such as node, node_boundary,
      included_equipment, included_lines, plus optional line_level_connections.

    Each returned package includes a full compact copy of the parsed P&ID JSON so the
    API prompt can send the complete topology context to the LLM.
    """
    parsed = _extract_parsed_pid_data(pid_data)

    process_description = parsed.get("process_description", "")
    intention = parsed.get("intention", parsed.get("design_intention", ""))
    system_inputs = parsed.get("system_inputs", [])
    system_outputs = parsed.get("system_outputs", [])
    equipment_list = parsed.get("equipment", []) or []
    valves_catalog = parsed.get("valves", []) or []
    instruments_catalog = parsed.get("instruments", []) or []
    utility_lines = parsed.get("utility_lines", []) or []
    full_pid_json = _safe_json_dumps(parsed)

    equipment_by_id = {
        str(eq.get("id")): eq for eq in equipment_list
        if isinstance(eq, dict) and eq.get("id")
    }
    valves_by_id = {
        str(v.get("id")): v for v in valves_catalog
        if isinstance(v, dict) and v.get("id")
    }
    instruments_by_id = {
        str(inst.get("id")): inst for inst in instruments_catalog
        if isinstance(inst, dict) and inst.get("id")
    }

    # Format A: parsed["connections"]. Format B may additionally include
    # parsed["line_level_connections"]. Include both so UI selections can target
    # either grouped HAZOP nodes or detailed line-level nodes.
    connection_records: List[dict] = []
    for key in ("connections", "line_level_connections"):
        records = parsed.get(key, []) or []
        if isinstance(records, list):
            for rec in records:
                if isinstance(rec, dict):
                    rec = dict(rec)
                    rec["_connection_source"] = key
                    connection_records.append(rec)

    query_infos: List[dict] = []
    seen_line_ids: set[str] = set()

    for idx, conn in enumerate(connection_records, start=1):
        line_id = str(conn.get("line_id") or conn.get("id") or f"NODE-{idx}")
        if line_id in seen_line_ids:
            continue
        seen_line_ids.add(line_id)

        from_id = conn.get("from_id") or conn.get("from") or conn.get("source")
        to_id = conn.get("to_id") or conn.get("to") or conn.get("target")

        explicit_node = conn.get("node") or conn.get("name")
        node = (
            str(explicit_node)
            if explicit_node
            else (f"{from_id} → {to_id}" if from_id and to_id else (str(from_id or to_id or line_id)))
        )

        node_boundary = conn.get("node_boundary", "")
        flow_direction = conn.get("flow_direction", "")
        context = conn.get("context", "")

        line_valve_ids = _as_id_list(conn.get("valves", []))
        line_instrument_ids = _as_id_list(conn.get("instruments", []))
        included_equipment_ids = _as_id_list(conn.get("included_equipment", []))
        included_line_ids = _as_id_list(conn.get("included_lines", []))

        line_valves = _lookup_catalog_records(line_valve_ids, valves_by_id)
        line_instruments = _lookup_catalog_records(line_instrument_ids, instruments_by_id)
        included_equipment_records = _lookup_catalog_records(included_equipment_ids, equipment_by_id)

        from_equipment = _fallback_ref(from_id, equipment_by_id)
        to_equipment = _fallback_ref(to_id, equipment_by_id)

        ids_to_match = [
            str(x) for x in [from_id, to_id, line_id, node] if x
        ] + included_equipment_ids + line_valve_ids + line_instrument_ids

        related_utility_lines = _match_related_utilities(
            utility_lines,
            ids_to_match=ids_to_match,
            valve_ids=line_valve_ids,
        )

        query_infos.append({
            "line_id": line_id,
            "from_id": from_id,
            "to_id": to_id,
            "node": node,
            "node_boundary": node_boundary,
            "context": context,
            "flow_direction": flow_direction,
            "connection_source": conn.get("_connection_source", "connections"),
            "connection_record": conn,
            "included_equipment_ids": included_equipment_ids,
            "included_equipment": included_equipment_records,
            "included_line_ids": included_line_ids,
            "valve_ids": line_valve_ids,
            "instrument_ids": line_instrument_ids,
            "valves": line_valves,
            "instruments": line_instruments,
            "from_equipment": from_equipment,
            "to_equipment": to_equipment,
            "related_utility_lines": related_utility_lines,
            "process_description": process_description,
            "intention": intention,
            "system_inputs": system_inputs,
            "system_outputs": system_outputs,
            "utility_lines": utility_lines,
            "equipment_catalog": equipment_list,
            "valves_catalog": valves_catalog,
            "instruments_catalog": instruments_catalog,
            "full_pid_json": full_pid_json,
        })

    # Fallback for process JSON with no explicit connection list.
    if not query_infos:
        query_infos.append({
            "line_id": "PROCESS-NODE-1",
            "from_id": "",
            "to_id": "",
            "node": parsed.get("node", "Overall process node"),
            "node_boundary": parsed.get("node_boundary", "Overall process boundary inferred from full P&ID JSON."),
            "context": process_description,
            "flow_direction": "",
            "connection_source": "fallback_process_node",
            "connection_record": {},
            "included_equipment_ids": _as_id_list([eq.get("id") for eq in equipment_list if isinstance(eq, dict)]),
            "included_equipment": equipment_list,
            "included_line_ids": [],
            "valve_ids": _as_id_list([v.get("id") for v in valves_catalog if isinstance(v, dict)]),
            "instrument_ids": _as_id_list([inst.get("id") for inst in instruments_catalog if isinstance(inst, dict)]),
            "valves": valves_catalog,
            "instruments": instruments_catalog,
            "from_equipment": None,
            "to_equipment": None,
            "related_utility_lines": utility_lines,
            "process_description": process_description,
            "intention": intention,
            "system_inputs": system_inputs,
            "system_outputs": system_outputs,
            "utility_lines": utility_lines,
            "equipment_catalog": equipment_list,
            "valves_catalog": valves_catalog,
            "instruments_catalog": instruments_catalog,
            "full_pid_json": full_pid_json,
        })

    logger.info(f"Extracted {len(query_infos)} HAZOP topology package(s) from P&ID JSON")
    return query_infos


# =============================================================================
# CSV parsing and validation
# =============================================================================

def _strip_code_fence(text: str) -> str:
    text = str(text or "").strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text


def parse_hazop_csv_20(
    result_text: str,
    *,
    expected_rows: int = 25,
    require_exact_rows: bool = True,
) -> List[List[str]]:
    """Parse and validate strict 20-column HAZOP/LOPA CSV output."""
    clean = _strip_code_fence(result_text)
    reader = csv.reader(io.StringIO(clean))
    rows: List[List[str]] = []

    for row in reader:
        if not row or not any(str(cell).strip() for cell in row):
            continue
        row = [str(cell).strip() for cell in row]
        # Drop accidental header row if produced despite instructions.
        if [c.lower() for c in row] == [h.lower() for h in HAZOP_LOPA_HEADERS_20]:
            continue
        if len(row) != len(HAZOP_LOPA_HEADERS_20):
            raise ValueError(
                f"Invalid CSV row length {len(row)}; expected {len(HAZOP_LOPA_HEADERS_20)}. Row={row}"
            )
        rows.append(row)

    if require_exact_rows and len(rows) != expected_rows:
        raise ValueError(f"Expected {expected_rows} CSV rows; got {len(rows)}")

    return rows


def _tokens_from_meta(meta: Dict[str, Any]) -> Dict[str, Any]:
    tokens = meta.get("tokens", {}) if isinstance(meta, dict) else {}
    return {
        "prompt": tokens.get("prompt"),
        "completion": tokens.get("completion"),
        "total": tokens.get("total"),
    }


def _response_output_text(response: Any) -> str:
    output_text = getattr(response, "output_text", None)
    if output_text:
        return str(output_text)

    # Fallback for SDK versions where output_text helper is absent.
    output = getattr(response, "output", None)
    if output:
        chunks: List[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for c in content:
                text = getattr(c, "text", None)
                if text:
                    chunks.append(str(text))
        if chunks:
            return "\n".join(chunks)

    return str(response)


# =============================================================================
# Responses API call with File Search
# =============================================================================

@timeit_log
def generate_hazop_with_file_search(
    input_data: Dict[str, Any],
    *,
    vector_store_id: Optional[str] = None,
    llm_provider: str = "own_api",
    model_name: str = DEFAULT_RESPONSES_MODEL,
    max_num_results: int = 12,
    reasoning_effort: Optional[str] = None,
    verbosity: Optional[str] = None,
) -> Tuple[str, Dict[str, Any]]:
    """Call the Responses API for one HAZOP deviation.

    Knowledge comes from one of two places:
      - vector_store_id set  -> OpenAI file_search over that hosted vector store
      - vector_store_id None -> local skill/standards library, injected into the prompt
    """
    client = get_llm_client(llm_provider)

    call_input = dict(input_data)
    knowledge_sources: List[str] = []
    if not vector_store_id:
        knowledge_context = build_generation_knowledge_context(call_input)
        call_input["knowledge_context"] = knowledge_context
        knowledge_sources = knowledge_sources_from_context(knowledge_context)

    prompt = build_file_search_hazop_prompt(**call_input)

    request_kwargs: Dict[str, Any] = {
        "model": model_name,
        "input": prompt,
    }
    if vector_store_id:
        request_kwargs["tools"] = [
            {
                "type": "file_search",
                "vector_store_ids": [vector_store_id],
                "max_num_results": max_num_results,
            }
        ]

    # The SDK/model may support these for GPT-5.x. Keep optional to avoid breaking older models.
    if reasoning_effort:
        request_kwargs["reasoning"] = {"effort": reasoning_effort}
    if verbosity:
        request_kwargs["text"] = {"verbosity": verbosity}

    start = time.perf_counter()

    def _do_call():
        return client.responses.create(**request_kwargs)

    response = _call_with_retries(
        _do_call,
        max_retries=3,
        context=f"hazop_file_search:{input_data.get('line_id')}:{input_data.get('parameter')}:{input_data.get('guide_word')}",
    )
    latency = time.perf_counter() - start
    meta = build_llm_metadata(response, latency)
    meta["vector_store_id"] = vector_store_id or ""
    meta["knowledge_source"] = (
        KNOWLEDGE_SOURCE_FILE_SEARCH if vector_store_id else KNOWLEDGE_SOURCE_LOCAL
    )
    meta["knowledge_sources"] = knowledge_sources
    meta["model"] = meta.get("model") or model_name
    return _response_output_text(response), meta


# =============================================================================
# Main HAZOP agent runner
# =============================================================================

def _compact_list(items: Any) -> str:
    if items is None:
        return ""
    if not isinstance(items, list):
        return str(items)
    out: List[str] = []
    for item in items:
        if isinstance(item, dict):
            tag = item.get("id") or item.get("tag") or item.get("name") or item.get("type") or item.get("line_id")
            if tag:
                extra = item.get("context") or item.get("function") or item.get("type") or item.get("flow_direction")
                out.append(f"{tag} ({extra})" if extra else str(tag))
            else:
                out.append(_safe_json_dumps({k: item[k] for k in list(item)[:4]}))
        else:
            out.append(str(item))
    return "; ".join(out)


def _equipment_to_text(equipment: Any) -> str:
    if not equipment:
        return ""
    if isinstance(equipment, dict):
        eq_id = equipment.get("id") or equipment.get("tag") or equipment.get("name", "")
        eq_type = equipment.get("type", "")
        context = equipment.get("context", "")
        parts = [str(x) for x in [eq_id, eq_type, context] if x]
        return " | ".join(parts)
    return str(equipment)


def _build_input_data(info: dict, param: str, guide_word: str) -> Dict[str, str]:
    from_eq = info.get("from_equipment") or {}
    to_eq = info.get("to_equipment") or {}
    utilities = info.get("related_utility_lines") or info.get("utility_lines") or []

    return {
        "line_id": str(info.get("line_id", "")),
        "node": str(info.get("node", "")),
        "node_boundary": str(info.get("node_boundary", "")),
        "from_equipment": _equipment_to_text(from_eq),
        "to_equipment": _equipment_to_text(to_eq),
        "included_equipment": _compact_list(info.get("included_equipment", [])),
        "included_lines": _compact_list(info.get("included_line_ids", [])),
        "valves": _compact_list(info.get("valves", [])) or ", ".join(map(str, info.get("valve_ids", []) or [])),
        "instruments": _compact_list(info.get("instruments", [])) or ", ".join(map(str, info.get("instrument_ids", []) or [])),
        "system_inputs": _compact_list(info.get("system_inputs", [])),
        "system_outputs": _compact_list(info.get("system_outputs", [])),
        "utility_lines": _compact_list(utilities),
        "flow_direction": str(info.get("flow_direction", "")),
        "context": str(info.get("context", "")),
        "process_description": str(info.get("process_description", "")),
        "intention": str(info.get("intention", "")),
        "connection_record_json": _safe_json_dumps(info.get("connection_record", {})),
        "full_pid_json": str(info.get("full_pid_json", "")),
        "guide_word": str(guide_word),
        "parameter": str(param),
    }


@timeit_log
def run_hazop_agent_1(
    pid_data: dict,
    excel_path: str,
    token_log_path: str,
    error_log_path: str,
    llm_response_log_path: str,
    parsed_excel_path: str,
    selections: List[Dict[str, str]],
    token_limit: int = 200000,
    *,
    llm_provider: str = "own_api",
    vector_store_id: Optional[str] = None,
    source_folder: Optional[str | os.PathLike[str]] = None,
    vector_store_config_path: str | os.PathLike[str] = DEFAULT_VECTOR_STORE_CONFIG_PATH,
    create_vector_store_if_missing: bool = False,
    model_name: str = DEFAULT_RESPONSES_MODEL,
    max_num_results: int = 12,
    max_generation_retries: int = 1,
    reasoning_effort: Optional[str] = None,
    verbosity: Optional[str] = None,
    knowledge_source: str = DEFAULT_KNOWLEDGE_SOURCE,
) -> Generator[Tuple[str, int], None, None]:
    """Generate HAZOP rows using OpenAI File Search over a pre-uploaded vector store.

    Recommended setup:
        create_hazop_vector_store_from_folder("hazop_sources")

    Recommended run:
        run_hazop_agent_1(..., vector_store_id="vs_...")

    If vector_store_id is not passed, the function loads HAZOP_VECTOR_STORE_ID from .env
    or hazop_vector_store_config.json.

    knowledge_source selects where reference knowledge comes from. The default is
    "local", which uses the on-disk skill/standards library and needs no vector
    store. Set HAZOP_KNOWLEDGE_SOURCE=openai_file_search (or pass knowledge_source)
    to fall back to the OpenAI hosted vector store.
    """
    resolved_vector_store_id: Optional[str] = None
    if knowledge_source == KNOWLEDGE_SOURCE_FILE_SEARCH:
        resolved_vector_store_id = get_or_create_vector_store_id(
            vector_store_id=vector_store_id,
            source_folder=source_folder,
            config_path=vector_store_config_path,
            create_if_missing=create_vector_store_if_missing,
        )
    elif vector_store_id:
        # Explicit id always wins, whatever the configured default is.
        resolved_vector_store_id = vector_store_id.strip()

    logger.info(
        "HAZOP knowledge source: %s%s",
        knowledge_source,
        f" (vector_store_id={resolved_vector_store_id})" if resolved_vector_store_id else "",
    )

    headers = HAZOP_LOPA_HEADERS_20

    query_infos = list_all_connections(pid_data)
    info_by_line: Dict[str, dict] = {str(info.get("line_id")): info for info in query_infos}

    df = pd.read_excel(excel_path) if os.path.exists(excel_path) else pd.DataFrame(columns=headers)
    df = df.reindex(columns=headers)

    token_df = pd.read_csv(token_log_path) if os.path.exists(token_log_path) else pd.DataFrame(columns=[
        "Timestamp", "LineID", "Parameter", "GuideWord", "Model", "VectorStoreID",
        "KnowledgeSource", "KnowledgeSources",
        "PromptTokens", "CompletionTokens", "TotalTokens", "ResponseID", "LatencySeconds"
    ])

    error_df = pd.read_csv(error_log_path) if os.path.exists(error_log_path) else pd.DataFrame(columns=[
        "Timestamp", "LineID", "Parameter", "GuideWord", "RawOutput", "Reason", "Attempt"
    ])

    llm_response_df = pd.read_csv(llm_response_log_path) if os.path.exists(llm_response_log_path) else pd.DataFrame(columns=[
        "Timestamp", "LineID", "Parameter", "GuideWord", "RawOutput", "ResponseID", "VectorStoreID"
    ])

    for sel in selections:
        line_id = str(sel.get("line_id", ""))
        param = str(sel.get("parameter", ""))
        guide_word = str(sel.get("guide_word", ""))

        if not line_id or not param or not guide_word:
            continue

        info = info_by_line.get(line_id)
        if not info:
            logger.warning(f"[Skip] line_id {line_id} not found in pid_data")
            continue

        input_data = _build_input_data(info, param, guide_word)

        result_text = ""
        rows: List[List[str]] = []
        meta: Dict[str, Any] = {}
        last_error: Optional[str] = None

        for attempt in range(1, max_generation_retries + 2):
            try:
                result_text, meta = generate_hazop_with_file_search(
                    input_data,
                    vector_store_id=resolved_vector_store_id,
                    llm_provider=llm_provider,
                    model_name=model_name,
                    max_num_results=max_num_results,
                    reasoning_effort=reasoning_effort,
                    verbosity=verbosity,
                )
                rows = parse_hazop_csv_20(result_text, expected_rows=25, require_exact_rows=True)
                last_error = None
                break
            except Exception as e:
                last_error = repr(e)
                logger.warning(
                    f"[Retryable generation/parse issue] {line_id}:{param}:{guide_word} "
                    f"attempt {attempt}/{max_generation_retries + 1}: {last_error}"
                )
                if attempt >= max_generation_retries + 1:
                    error_entry = {
                        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "LineID": line_id,
                        "Parameter": param,
                        "GuideWord": guide_word,
                        "RawOutput": result_text,
                        "Reason": last_error,
                        "Attempt": attempt,
                    }
                    error_df = pd.concat([error_df, pd.DataFrame([error_entry])], ignore_index=True)
                    error_df.to_csv(error_log_path, index=False)
                    rows = []
                    break

        if not rows:
            continue

        tokens = _tokens_from_meta(meta)
        total_tokens = tokens.get("total")
        if total_tokens is not None and int(total_tokens) > token_limit:
            logger.warning(f"[Skipped] {line_id}:{param}:{guide_word} — {total_tokens} tokens exceeds limit {token_limit}")
            continue

        # Log raw LLM output.
        response_entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "LineID": line_id,
            "Parameter": param,
            "GuideWord": guide_word,
            "RawOutput": result_text,
            "ResponseID": meta.get("id"),
            "VectorStoreID": resolved_vector_store_id or "",
        }
        llm_response_df = pd.concat([llm_response_df, pd.DataFrame([response_entry])], ignore_index=True)
        llm_response_df.to_csv(llm_response_log_path, index=False)

        df_parsed = pd.DataFrame(rows, columns=headers)

        # Merge into parsed_excel_path.
        if os.path.exists(parsed_excel_path):
            df_existing = pd.read_excel(parsed_excel_path)
            df_existing = df_existing.loc[:, ~df_existing.columns.duplicated()].reindex(columns=headers)
            df_combined = pd.concat([df_existing, df_parsed.reindex(columns=headers)], ignore_index=True)
        else:
            df_combined = df_parsed.reindex(columns=headers)
        df_combined.to_excel(parsed_excel_path, index=False)

        # Main HAZOP output.
        df = pd.concat([df, df_parsed.reindex(columns=headers)], ignore_index=True)
        df.to_excel(excel_path, index=False)

        # Token / metadata log.
        token_row = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "LineID": line_id,
            "Parameter": param,
            "GuideWord": guide_word,
            "Model": meta.get("model", model_name),
            "VectorStoreID": resolved_vector_store_id or "",
            "KnowledgeSource": meta.get("knowledge_source", ""),
            "KnowledgeSources": " | ".join(meta.get("knowledge_sources") or []),
            "PromptTokens": tokens.get("prompt"),
            "CompletionTokens": tokens.get("completion"),
            "TotalTokens": tokens.get("total"),
            "ResponseID": meta.get("id"),
            "LatencySeconds": meta.get("latency_s"),
        }
        token_df = pd.concat([token_df, pd.DataFrame([token_row])], ignore_index=True)
        token_df.to_csv(token_log_path, index=False)

        yield f"{line_id}:{param}:{guide_word}", int(total_tokens or 0)

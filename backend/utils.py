from pathlib import Path
import json
import csv
from typing import Any

from module.schema_json import PIDResponse
from decorators import logger, timeit_log

@timeit_log
def save_pid_json(
    pid_data: PIDResponse,
    image_path: str | Path,
    out_dir: str = "data",
    *,
    suffix: str = ".pido3_t_2.json",
    indent: int = 2,
) -> Path:
    img_path = Path(image_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / f"{img_path.stem}{suffix}"
    json_text = pid_data.model_dump_json(indent=indent, by_alias=True)
    out_path.write_text(json_text, encoding="utf-8")

    return out_path

@timeit_log
def summarize_pid_components(json_path: Path):
    if not json_path.exists():
        logger.error(f"File not found: {json_path}")
        return

    data = json.loads(json_path.read_text(encoding="utf-8"))
    try:
        parsed = data["choices"][0]["message"]["parsed"]
    except (KeyError, TypeError) as e:
        logger.error(f"Invalid format in JSON file: {e}")
        return

    logger.info("=== Summary of P&ID Components ===")
    equipment = parsed.get("equipment", [])
    logger.info(f"[Equipment] Count: {len(equipment)}")
    for eq in equipment:
        logger.debug(f"  - ID: {eq.get('id')}, Name: {eq.get('name')}, Type: {eq.get('type')}")

    valves = parsed.get("valves", [])
    logger.info(f"[Valves] Count: {len(valves)}")
    for v in valves:
        logger.debug(f"  - ID: {v.get('id')}, Type: {v.get('type')}, Location: {v.get('location')}")
    instruments = parsed.get("instruments", [])
    logger.info(f"[Instruments] Count: {len(instruments)}")
    for i in instruments:
        logger.debug(f"  - ID: {i.get('id')}, Function: {i.get('function')}, Location: {i.get('location')}")

@timeit_log
def search_file(name: str, data_dir: str | Path = "static/data") -> dict[str, Any]:
    """
    Search for <name>.json or <name>.csv inside data_dir and return dict
    ready for jsonify() in Flask.
    """
    name = name.strip()
    if not name:
        return {"ok": False, "error": "Empty file name"}

    data_dir = Path(data_dir)
    json_path = data_dir / f"{name}.json"
    csv_path = data_dir / f"{name}.csv"

    file_used: str | None = None
    data: Any = None

    try:
        if json_path.exists():
            file_used = json_path.name
            data = json.loads(json_path.read_text(encoding="utf-8"))
        elif csv_path.exists():
            file_used = csv_path.name
            with csv_path.open(newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                data = list(reader)
        else:
            return {"ok": False, "error": "File not found"}

        return {
            "ok": True,
            "file_name": file_used,
            "data": data,
        }
    except Exception as e:
        logger.error(f"Error reading file '{name}': {e}")
        return {"ok": False, "error": str(e)}

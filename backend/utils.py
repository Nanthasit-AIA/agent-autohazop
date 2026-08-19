import json, csv, re
from pathlib import Path
from typing import Any, Union

from module.schema_json import PIDResponse
from decorators import logger, timeit_log

PathLike = Union[str, Path]

def _slugify_filename(raw: str) -> str:
    """
    Turn an arbitrary name into a safe filename:
    - lowercases
    - replaces spaces with '_'
    - strips non-alphanumeric/_/-
    - ensures not empty
    """
    s = raw.strip().lower()
    s = s.replace(" ", "_")
    s = re.sub(r"[^a-z0-9_\-]+", "", s)
    return s or "pid_result"

@timeit_log
def save_pid_json(
    pid_data: PIDResponse,
    metadata: dict,
    image_path: PathLike,
    out_dir: str = "data",
    *,
    name: str | None = None,
    suffix: str = ".json",
    indent: int = 2,
) -> Path:
    img_path = Path(image_path)
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    if name:
        base = _slugify_filename(name)
    else:
        base = img_path.stem

    save_path = out_path / f"{base}{suffix}"
    combined = {
        "pid_data": pid_data.model_dump(by_alias=True),
        "metadata": metadata,
    }
    json_text = json.dumps(combined, indent=indent, ensure_ascii=False)
    save_path.write_text(json_text, encoding="utf-8")
    return save_path

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

def search_file(name: str, data_dir: str | Path = "static/data") -> dict[str, Any]:
    name = name.strip()
    logger.info(f"🔍 search_file() called with name='{name}' dir='{data_dir}'")

    if not name:
        return {"ok": False, "error": "Empty file name"}

    data_dir = Path(data_dir)
    base_name = Path(name).stem if Path(name).suffix.lower() in {".json", ".csv"} else name

    # Try the name as given first, then its slugified form, so a display name
    # like "Naphtha Tank" still resolves to a file saved as "naphtha_tank".
    candidate_names: list[str] = []
    for candidate in (base_name, _slugify_filename(base_name)):
        if candidate and candidate not in candidate_names:
            candidate_names.append(candidate)

    file_used: str | None = None
    data: Any = None

    try:
        for candidate in candidate_names:
            json_path = data_dir / f"{candidate}.json"
            csv_path = data_dir / f"{candidate}.csv"

            if json_path.exists():
                file_used = json_path.name
                data = json.loads(json_path.read_text(encoding="utf-8"))
                break
            if csv_path.exists():
                file_used = csv_path.name
                with csv_path.open(newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    data = list(reader)
                break
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

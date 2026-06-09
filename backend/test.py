def list_all_connections(pid_data: dict):
    """
    Normalize pid_data shape and return a list of per-line dictionaries.
    Each entry includes:
      - line-level info (line_id, from_id, to_id, node, context)
      - line valve / instrument IDs + detailed objects
      - from/to equipment objects (if applicable)
      - global pid_data context: system_inputs, system_outputs,
        full equipment / valves / instruments catalogs, utility_lines
    """
    # --- Detect shape ---
    if "choices" in pid_data:
        # old style: OpenAI chat completion wrapper
        parsed = pid_data["choices"][0]["message"]["parsed"]
    elif "pid_data" in pid_data and isinstance(pid_data["pid_data"], dict):
        # new style: file wrapper with metadata
        parsed = pid_data["pid_data"]
    else:
        # already the bare P&ID JSON
        parsed = pid_data

    # --- Global/top-level context from pid_data ---
    process_description = parsed.get("process_description", "")

    system_inputs = parsed.get("system_inputs", [])
    system_outputs = parsed.get("system_outputs", [])

    equipment_list = parsed.get("equipment", [])
    valves_catalog = parsed.get("valves", [])
    instruments_catalog = parsed.get("instruments", [])
    utility_lines = parsed.get("utility_lines", [])

    # Build quick lookup maps by id
    equipment_by_id = {
        eq.get("id"): eq for eq in equipment_list if isinstance(eq, dict) and eq.get("id")
    }
    valves_by_id = {
        v.get("id"): v for v in valves_catalog if isinstance(v, dict) and v.get("id")
    }
    instruments_by_id = {
        inst.get("id"): inst
        for inst in instruments_catalog
        if isinstance(inst, dict) and inst.get("id")
    }

    connections = parsed.get("connections", [])

    query_infos = []
    for conn in connections:
        line_id = conn.get("line_id")
        from_id = conn.get("from_id")
        to_id = conn.get("to_id")

        node = (
            f"{from_id} → {to_id}"
            if from_id and to_id
            else (from_id or to_id or "")
        )

        context = conn.get("context", "")
        line_valve_ids = conn.get("valves", []) or []
        line_instrument_ids = conn.get("instruments", []) or []

        # Detailed objects for the valves/instruments on this line
        line_valves = [
            valves_by_id.get(v_id, {"id": v_id})
            for v_id in line_valve_ids
        ]
        line_instruments = [
            instruments_by_id.get(i_id, {"id": i_id})
            for i_id in line_instrument_ids
        ]

        # If from_id / to_id are equipment tags, attach full equipment objects
        from_equipment = equipment_by_id.get(from_id)
        to_equipment = equipment_by_id.get(to_id)

        # Utility lines relevant to this connection
        # (e.g. from_id / to_id match a utility_type like "Cooling water to E-225")
        related_utility_lines = [
            u for u in utility_lines
            if u.get("utility_type") in (from_id, to_id)
        ]

        query_infos.append(
            {
                # --- core connection info ---
                "line_id": line_id,
                "from_id": from_id,
                "to_id": to_id,
                "node": node,
                "context": context,

                # --- line-level valve/instrument info ---
                "valve_ids": line_valve_ids,
                "instrument_ids": line_instrument_ids,
                "valves": line_valves,              # list of dicts
                "instruments": line_instruments,    # list of dicts

                # --- related equipment / utilities ---
                "from_equipment": from_equipment,   # dict or None
                "to_equipment": to_equipment,       # dict or None

                # --- global context copied onto each row ---
                "process_description": process_description,
                "system_inputs": system_inputs,
                "system_outputs": system_outputs,
                "utility_lines": utility_lines,
            }
        )

    return query_infos

import json

def main():
    # 1) Load the real P&ID JSON
    with open(r"C:\Users\idtcu\agent-autohazop\backend\static\data\c4-009.json", "r", encoding="utf-8") as f:
        pid_data = json.load(f)

    # 2) Run the function
    infos = list_all_connections(pid_data)

    # 3) Basic checks
    print("Total connections:", len(infos))

    # Print first 1–2 entries to inspect structure
    if infos:
        from itertools import islice
        for i, info in enumerate(islice(infos, 0, 2)):
            print(f"\n--- Connection #{i} ---")
            print("line_id:", info.get("line_id"))
            print("node:", info.get("node"))
            print("valve_ids:", info.get("valve_ids"))
            print("instrument_ids:", info.get("instrument_ids"))
            print("from_equipment:", info.get("from_equipment"))
            print("to_equipment:", info.get("to_equipment"))
            print(json.dumps(info, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

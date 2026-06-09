import os
from datetime import datetime
from typing import Generator, Tuple, List, Dict
import pandas as pd

from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from typing import Generator, Tuple , Any
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback

from decorators import logger, timeit_log
from module.llm_module import get_chat_model
from module.prompt.hzp_promptt import few_shot_prompt
import sys
sys.stdout.reconfigure(encoding="utf-8")

@timeit_log
def list_all_process(pid_data: dict):
    parsed = pid_data["choices"][0]["message"]["parsed"]

    system_input = parsed.get("system_inputs", [])
    system_output = parsed.get("system_outputs", [])
    process_description = parsed.get("process_description", "")

    query_infos = []
    query_infos.append({
        "system_input": system_input,
        "system_output": system_output,
        "process_description": process_description
    })
    return query_infos

def list_all_connections(pid_data: dict):
    """
    NOTE:
      - line-level info (line_id, from_id, to_id, node, context)
      - line valve / instrument IDs + context
      - from/to equipment objects (if applicable)
      - global pid_data context: system_inputs, system_outputs,
        full equipment / valves / instruments catalogs, utility_lines
    """

    if "choices" in pid_data:
        parsed = pid_data["choices"][0]["message"]["parsed"]
    elif "pid_data" in pid_data and isinstance(pid_data["pid_data"], dict):
        parsed = pid_data["pid_data"]
    else:
        parsed = pid_data

    process_description = parsed.get("process_description", "")

    system_inputs = parsed.get("system_inputs", [])
    system_outputs = parsed.get("system_outputs", [])

    equipment_list = parsed.get("equipment", [])
    valves_catalog = parsed.get("valves", [])
    instruments_catalog = parsed.get("instruments", [])
    utility_lines = parsed.get("utility_lines", [])

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

        line_valves = [
            valves_by_id.get(v_id, {"id": v_id})
            for v_id in line_valve_ids
        ]
        line_instruments = [
            instruments_by_id.get(i_id, {"id": i_id})
            for i_id in line_instrument_ids
        ]

        from_equipment = equipment_by_id.get(from_id)
        to_equipment = equipment_by_id.get(to_id)

        related_utility_lines = [
            u for u in utility_lines
            if u.get("utility_type") in (from_id, to_id)
        ]

        query_infos.append(
            {
                # --- Core connection info ---
                "line_id": line_id,
                "from_id": from_id,
                "to_id": to_id,
                "node": node,
                "context": context,

                # --- Node-Level valve/instrument info ---
                "valve_ids": line_valve_ids,
                "instrument_ids": line_instrument_ids,
                "valves": line_valves,              # list of dicts
                "instruments": line_instruments,    # list of dicts

                # --- Node-Level equipment / utilities ---
                "from_equipment": from_equipment,   # dict or None
                "to_equipment": to_equipment,       # dict or None

                # --- Global context ---
                "process_description": process_description,
                "system_inputs": system_inputs,
                "system_outputs": system_outputs,
                "utility_lines": utility_lines,
            }
        )

    return query_infos

def run_hazop_agent_1(
    pid_data: dict,
    excel_path: str,
    token_log_path: str,
    error_log_path: str,
    llm_response_log_path: str,
    parsed_excel_path: str,
    selections: List[Dict[str, str]],
    token_limit: int = 20000,
) -> Generator[Tuple[str, int], None, None]:
    valid_guide_ws = [
        "No", "More", "Less", "As well as", "Part of", "Reverse",
        "Other than", "Early", "Late", "Before", "After", "No/Low"
    ]

    valid_params = [
        "Flow", "Pressure", "Temperature", "Level", "Composition",
        "Phase", "Utility", "Power", "Instrument", "Human Action",
        "Maintenance", "Operation Timing", "Concentration"
    ]

    headers = [
        "Node",
        "Guide Word",
        "Parameter",
        "Deviation",
        "Cause",
        "Consequence",
        "Severity",
        "Likelihood",
        "Risk Ranking",
        "Safeguards",
        "Recommendations",
        "Responsibility",
        "Severity_Basis",
        "Likelihood_p_Basis",
    ]

    # --- 1) 14-column parser for the new CSV schema ---
    @timeit_log
    def parse_llm_result(raw_out: str, i: int = 5) -> list[list[str]]:
        """
        Parse a single CSV line from the LLM into a list of values ordered by `headers`.

        OUTPUT FORMAT - INTEGRATED HAZOP/LOPA CSV
        Return ONLY CSV rows with exactly 20 comma-separated fields in this order:
        Node, Design Intention, Parameter, Guide Word, Deviation, Cause, Consequence,
        Initial Severity, Initial Likelihood, Initial Risk Ranking,
        IPLs, IPL Independent, IPL Effective, IPL Auditable,
        Safeguards, Final Severity, Final Likelihood, Final Risk Ranking,
        Recommendations, Comments_Actions
        """
        parts = [p.strip() for p in str(raw_out).split(",")]

        expected_len = len(headers)  # 14
        if len(parts) < expected_len:
            parts += [""] * (expected_len - len(parts))
        elif len(parts) > expected_len:
            parts = parts[:expected_len - 1] + [", ".join(parts[expected_len - 1:]).strip()]

        result = {col: "" for col in headers}

        # Base fields
        result["Node"] = parts[0]
        result["Guide Word"] = parts[1] if parts[1] in valid_guide_ws else ""
        result["Parameter"] = parts[2] if parts[2] in valid_params else ""
        result["Deviation"] = parts[3]
        result["Cause"] = parts[4]
        result["Consequence"] = parts[5]

        # Risk numbers (try int, else keep raw)
        sev = parts[6]
        lik = parts[7]
        rr  = parts[8]

        result["Severity"] = int(sev) if isinstance(sev, str) and sev.isdigit() else sev
        result["Likelihood"] = int(lik) if isinstance(lik, str) and lik.isdigit() else lik
        result["Risk Ranking"] = int(rr) if isinstance(rr, str) and rr.isdigit() else rr

        # Text fields
        result["Safeguards"] = parts[9]
        result["Recommendations"] = parts[10]
        result["Responsibility"] = parts[11]
        result["Severity_Basis"] = parts[12]
        result["Likelihood_p_Basis"] = parts[13]

        return [[result[col] for col in headers]]

    def parse_llm_result_to_rows(result_text: str) -> list[list[str]]:
        rows: list[list[str]] = []

        for line in str(result_text).strip().splitlines():
            if not line.strip():
                continue
            try:
                line_rows = parse_llm_result(line)
            except Exception:
                continue

            for r in line_rows:
                if len(r) == len(headers):
                    rows.append(r)

        return rows

    # --- build query infos from pid_data ---
    query_infos = list_all_connections(pid_data)
    print(query_infos)
    info_by_line: Dict[str, dict] = {info["line_id"]: info for info in query_infos}

    df = pd.read_excel(excel_path) if os.path.exists(excel_path) else pd.DataFrame(columns=headers)
    token_df = pd.read_csv(token_log_path) if os.path.exists(token_log_path) else pd.DataFrame(columns=[
        "Timestamp", "LineID", "Parameter", "GuideWord", "Model",
        "PromptTokens", "CompletionTokens", "TotalTokens"
    ])
    error_df = pd.read_csv(error_log_path) if os.path.exists(error_log_path) else pd.DataFrame(columns=[
        "Timestamp", "LineID", "Parameter", "GuideWord", "RawOutput", "Reason"
    ])
    llm_response_df = pd.read_csv(llm_response_log_path) if os.path.exists(llm_response_log_path) else pd.DataFrame(columns=[
        "Timestamp", "LineID", "Parameter", "GuideWord", "RawOutput"
    ])

    llm, model_name = get_chat_model()
    hazop_chain = LLMChain(llm=llm, prompt=few_shot_prompt)

    # helper for compact string from list[dict|str]
    def to_compact_str_list(items: Any) -> str:
        if not isinstance(items, list):
            return str(items) if items else ""
        out: list[str] = []
        for it in items:
            if isinstance(it, dict):
                tag = it.get("id") or it.get("tag") or it.get("name") or it.get("type")
                if tag:
                    out.append(str(tag))
                else:
                    # very compact fallback: first 1–2 keys
                    out.append(str({k: it[k] for k in list(it)[:2]}))
            else:
                out.append(str(it))
        return "; ".join(out)

    for sel in selections:
        line_id = sel.get("line_id")
        param = sel.get("parameter")
        guide_word = sel.get("guide_word")

        if not line_id or not param or not guide_word:
            continue

        info = info_by_line.get(line_id)
        if not info:
            logger.warning(f"[Skip] line_id {line_id} not found in pid_data")
            continue

        # --- Extract clean strings for prompt ---

        from_eq = info.get("from_equipment") or {}
        to_eq = info.get("to_equipment") or {}

        from_eq_str = (
            from_eq.get("id")
            or from_eq.get("tag")
            or from_eq.get("name")
            or ""
        )

        to_eq_str = (
            to_eq.get("id")
            or to_eq.get("tag")
            or to_eq.get("name")
            or ""
        )

        valve_strs: list[str] = []
        for v in info.get("valves", []):
            if not isinstance(v, dict):
                valve_strs.append(str(v))
                continue
            tag = v.get("id") or v.get("tag") or v.get("name")
            if tag:
                valve_strs.append(str(tag))

        instr_strs: list[str] = []
        for inst in info.get("instruments", []):
            if not isinstance(inst, dict):
                instr_strs.append(str(inst))
                continue
            tag = inst.get("id") or inst.get("tag") or inst.get("name")
            if tag:
                instr_strs.append(str(tag))

        system_inputs_str = to_compact_str_list(info.get("system_inputs", []))
        system_outputs_str = to_compact_str_list(info.get("system_outputs", []))
        # you can choose local utilities if you want:
        # util_source = info.get("related_utility_lines") or info.get("utility_lines", [])
        util_source = info.get("utility_lines", [])
        utility_lines_str = to_compact_str_list(util_source)

        from_eq = info.get("from_equipment") or {}
        to_eq = info.get("to_equipment") or {}

        input_data = {
            "line_id": info["line_id"],
            "node": info["node"],

            # Prefer equipment IDs (tags) rather than raw dicts
            "from_equipment": from_eq.get("id", "") if isinstance(from_eq, dict) else "",
            "to_equipment": to_eq.get("id", "") if isinstance(to_eq, dict) else "",

            # Use *IDs* for local valves/instruments
            "valves": ", ".join(info.get("valve_ids", [])),
            "instruments": ", ".join(info.get("instrument_ids", [])),

            # Global context – stringify each item defensively
            "system_inputs": "; ".join(map(str, info.get("system_inputs", []))),
            "system_outputs": "; ".join(map(str, info.get("system_outputs", []))),
            "utility_lines": "; ".join(map(str, info.get("utility_lines", []))),

            "context": info.get("context", ""),
            "process_description": info.get("process_description", ""),
            "parameter": param,
            "guide_word": guide_word,
        }


        print(input_data)

        with get_openai_callback() as cb:
            try:
                result = hazop_chain.run(**input_data)

                rows = parse_llm_result_to_rows(result)

                if not rows:
                    logger.warning(
                        f"[Warning] No valid rows for {info['line_id']}:{param}:{guide_word} "
                        f"(LLM output probably malformed CSV)"
                    )
                    error_entry = {
                        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "LineID": info["line_id"],
                        "Parameter": param,
                        "GuideWord": guide_word,
                        "RawOutput": result,
                        "Reason": f"Invalid or no rows parsed (expected {len(headers)} columns per row)"
                    }
                    error_df = pd.concat([error_df, pd.DataFrame([error_entry])], ignore_index=True)
                    error_df.to_csv(error_log_path, index=False)
                    continue

            except Exception as e:
                logger.error(f"[Error] {info['line_id']}:{param}:{guide_word} — {e}")
                continue

            if cb.total_tokens > token_limit:
                logger.warning(f"[Skipped] {line_id}:{param}:{guide_word} — {cb.total_tokens} tokens")
                continue

            tokens_used = cb.total_tokens

        # Log raw LLM output
        response_entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "LineID": line_id,
            "Parameter": param,
            "GuideWord": guide_word,
            "RawOutput": result,
        }
        llm_response_df = pd.concat([llm_response_df, pd.DataFrame([response_entry])], ignore_index=True)
        llm_response_df.to_csv(llm_response_log_path, index=False)

        # Build DataFrame ONLY from current selection's rows
        df_parsed = pd.DataFrame(rows, columns=headers)

        # --- merge into parsed_excel_path ---
        if os.path.exists(parsed_excel_path):
            df_existing = pd.read_excel(parsed_excel_path)
            df_existing = df_existing.loc[:, ~df_existing.columns.duplicated()]
            df_existing = df_existing.reindex(columns=headers)
            df_parsed = df_parsed.reindex(columns=headers)
            df_combined = pd.concat([df_existing, df_parsed], ignore_index=True)
        else:
            df_combined = df_parsed.reindex(columns=headers)

        df_combined.to_excel(parsed_excel_path, index=False)

        # --- main HAZOP output ---
        df = pd.concat([df, df_parsed], ignore_index=True)
        df.to_excel(excel_path, index=False)

        # token log
        token_row = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "LineID": line_id,
            "Parameter": param,
            "GuideWord": guide_word,
            "Model": model_name,
            "PromptTokens": cb.prompt_tokens,
            "CompletionTokens": cb.completion_tokens,
            "TotalTokens": cb.total_tokens,
        }
        token_df = pd.concat([token_df, pd.DataFrame([token_row])], ignore_index=True)
        token_df.to_csv(token_log_path, index=False)

        yield f"{line_id}:{param}:{guide_word}", tokens_used

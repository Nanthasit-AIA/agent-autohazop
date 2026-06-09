from __future__ import annotations
import re
from typing import Optional, Tuple, Dict, List

# ============================================================
# 1) Base checklist text
# ============================================================

CAUSE_CHECKLIST_50 = """MANDATORY ENGINEERING CAUSE CHECKLIST (MUST appear once each)
1.Pressure instrument failure (gauge; transmitter; sensor)
2.Temperature instrument failure (thermometer; transmitter; sensor)
3.Level instrument failure (indicator; transmitter; sensor)
4.Flow instrument failure (meter; sensor; transmitter)
5.Incorrect instrument calibration or setpoint
6.Control valve malfunction (stuck; leakage; actuator failure)
7.Incorrect valve selection or specification
8.Proportional/regulating valve malfunction
9.Pneumatic valve failure or loss of actuator signal
10.Vent valve malfunction (fails closed/open during transfer or discharge)
11.Pipeline leakage (joint failure; crack; corrosion; gasket)
12.Pipeline blockage or obstruction (fouling; deposits; freezing; solids)
13.Incorrect installation or poor layout of piping/equipment
14.Vessel leakage or rupture (design or fatigue failure)
15.Pump mechanical failure (seal; impeller; shaft; cavitation)
16.Compressor or fan mechanical failure (motor; bearing; impeller)
17.Vacuum pump failure (cannot achieve required vacuum)
18.Refrigerant/utility line rupture or internal leak
19.Cylinder rupture or containment breach
20.Drain hole blockage or inadequate drainage
21.Equipment overheating (heater runaway; thermal stress)
22.Abnormal wear/erosion leading to loss of containment
23.Abnormal utility supply pressure (too high or too low)
24.Abnormal cryogenic source (LN2 evaporation; boil-off; loss of supply)
25.Abnormal water supply (insufficient cooling or cleaning water)
26.Abnormal gas supply (N2; compressed air; other utility failure)
27.Power failure (loss of electricity to motors; fans; instruments)
28.Cooling system failure (no circulation; fouling; exchanger blocked)
29.Heating system failure (heater not starting or insufficient duty)
30.Heating system uncontrolled (heater operating without cutoff)
31.Utility connection leakage (joints; hoses; couplings)
32.Pressure regulator malfunction (failure of PRV or regulator valve)
33.Upstream overpressure (abnormal feed source pressure)
34.Downstream restriction (blockage; closed valve; isolation)
35.Reverse flow due to pressure imbalance or check valve failure
36.Reaction runaway / abnormal process temperature rise
37.Abnormal mixing ratio (incorrect blending; poor agitation)
38.Incorrect feed ratio or dosage deviation
39.Abnormal circulation imbalance (inlet > outlet; unequal flows)
40.Vessel operating empty or insufficient level (dry running)
41.Vessel operating overfilled (high level)
42.Internal decomposition of process medium (gas release; thermal breakdown)
43.Ambient high temperature (external fire; hot weather)
44.Ambient low temperature (cold weather; freezing)
45.External mechanical impact or vibration
46.Abnormal source contamination (impurities; off-spec feed)
47.Human error in operation (wrong valve; wrong sequence)
48.Incorrect operating sequence (early or late action)
49.Insufficient operating time (too short cycle; premature termination)
50.Excessive operating time (too long cycle; delayed termination)"""


# ============================================================
# 2) Canonical cause lookup (ID -> text) used for payload building
#    IMPORTANT: Do not change IDs.
# ============================================================

CAUSE_LOOKUP: Dict[int, str] = {
    1: "Pressure instrument failure (gauge; transmitter; sensor)",
    2: "Temperature instrument failure (thermometer; transmitter; sensor)",
    3: "Level instrument failure (indicator; transmitter; sensor)",
    4: "Flow instrument failure (meter; sensor; transmitter)",
    5: "Incorrect instrument calibration or setpoint",
    6: "Control valve malfunction (stuck; leakage; actuator failure)",
    7: "Incorrect valve selection or specification",
    8: "Proportional/regulating valve malfunction",
    9: "Pneumatic valve failure or loss of actuator signal",
    10: "Vent valve malfunction (fails closed/open during transfer or discharge)",
    11: "Pipeline leakage (joint failure; crack; corrosion; gasket)",
    12: "Pipeline blockage or obstruction (fouling; deposits; freezing; solids)",
    13: "Incorrect installation or poor layout of piping/equipment",
    14: "Vessel leakage or rupture (design or fatigue failure)",
    15: "Pump mechanical failure (seal; impeller; shaft; cavitation)",
    16: "Compressor or fan mechanical failure (motor; bearing; impeller)",
    17: "Vacuum pump failure (cannot achieve required vacuum)",
    18: "Refrigerant/utility line rupture or internal leak",
    19: "Cylinder rupture or containment breach",
    20: "Drain hole blockage or inadequate drainage",
    21: "Equipment overheating (heater runaway; thermal stress)",
    22: "Abnormal wear/erosion leading to loss of containment",
    23: "Abnormal utility supply pressure (too high or too low)",
    24: "Abnormal cryogenic source (LN2 evaporation; boil-off; loss of supply)",
    25: "Abnormal water supply (insufficient cooling or cleaning water)",
    26: "Abnormal gas supply (N2; compressed air; other utility failure)",
    27: "Power failure (loss of electricity to motors; fans; instruments)",
    28: "Cooling system failure (no circulation; fouling; exchanger blocked)",
    29: "Heating system failure (heater not starting or insufficient duty)",
    30: "Heating system uncontrolled (heater operating without cutoff)",
    31: "Utility connection leakage (joints; hoses; couplings)",
    32: "Pressure regulator malfunction (failure of PRV or regulator valve)",
    33: "Upstream overpressure (abnormal feed source pressure)",
    34: "Downstream restriction (blockage; closed valve; isolation)",
    35: "Reverse flow due to pressure imbalance or check valve failure",
    36: "Reaction runaway / abnormal process temperature rise",
    37: "Abnormal mixing ratio (incorrect blending; poor agitation)",
    38: "Incorrect feed ratio or dosage deviation",
    39: "Abnormal circulation imbalance (inlet > outlet; unequal flows)",
    40: "Vessel operating empty or insufficient level (dry running)",
    41: "Vessel operating overfilled (high level)",
    42: "Internal decomposition of process medium (gas release; thermal breakdown)",
    43: "Ambient high temperature (external fire; hot weather)",
    44: "Ambient low temperature (cold weather; freezing)",
    45: "External mechanical impact or vibration",
    46: "Abnormal source contamination (impurities; off-spec feed)",
    47: "Human error in operation (wrong valve; wrong sequence)",
    48: "Incorrect operating sequence (early or late action)",
    49: "Insufficient operating time (too short cycle; premature termination)",
    50: "Excessive operating time (too long cycle; delayed termination)",
}

ALL_CAUSE_IDS: List[int] = list(range(1, 51))


# ============================================================
# 3) Deviation template -> Cause Eligibility Matrix
#    NOTE: Flow uses More/Low/No/Reverse (we normalize Flow+Less -> Low)
#    If case not found, fallback to ALL 50.
# ============================================================

CAUSE_ELIGIBILITY_MATRIX: Dict[str, List[int]] = {
    "Flow|More":    [4, 5, 6, 8, 9, 15, 18, 22, 23, 32, 33, 39, 45, 47, 48, 50],
    "Flow|Low":     [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 20, 23, 25, 27, 28, 34, 39, 45, 47, 48, 49],
    "Flow|No":      [4, 6, 7, 10, 11, 12, 13, 15, 17, 23, 27, 34, 40, 41, 47, 48, 49],
    "Flow|Reverse": [6, 12, 33, 34, 35, 39, 47, 48],
    "Pressure|More": [1, 5, 6, 10, 11, 12, 14, 23, 32, 33, 34, 35, 36, 42, 47, 48],
    "Pressure|Less": [1, 5, 7, 10, 11, 13, 15, 16, 17, 19, 22, 23, 24, 26, 27, 31, 34, 39, 45, 47, 48],
    "Temperature|More": [2, 5, 21, 27, 28, 30, 36, 42, 43, 47, 48],
    "Temperature|Less": [2, 5, 18, 23, 24, 25, 27, 28, 29, 44, 47, 48],
    "Level|More": [3, 5, 6, 10, 12, 20, 22, 34, 39, 41, 47, 48, 50],
    "Level|Less": [3, 5, 11, 15, 20, 39, 40, 47, 48, 49],
    "Level|No":   [3, 11, 15, 27, 34, 40, 47, 48, 49],
    "Concentration|More": [25, 37, 38, 42, 46, 47, 48, 50],
    "Concentration|Less": [19, 25, 37, 38, 46, 47, 48, 49],
    "Composition|Other Than": [11, 18, 19, 22, 31, 37, 38, 42, 45, 46, 47, 48],
}

# Deviation aliases from UI (you can add more)
_UI_DEVIATION_ALIAS: Dict[str, str] = {
    "More": "More",
    "Less": "Less",
    "No": "No",
    "Reverse": "Reverse",
    "Other Than": "Other Than",

    "Low": "Low",
    "Low Flow": "Low",
    "Less Flow": "Low",
    "No Flow": "No",
}

def normalize_parameter_deviation(parameter: str, deviation: str) -> Tuple[str, str]:
    p = (parameter or "").strip().title()
    d_raw = (deviation or "").strip()

    if d_raw.lower() == "other than":
        d = "Other Than"
    else:
        d = _UI_DEVIATION_ALIAS.get(d_raw, d_raw.strip().title())

    if p == "Flow" and d == "Less":
        d = "Low"

    return p, d

def get_eligible_cause_ids(parameter: str, deviation: str) -> List[int]:
    """
    Matrix lookup. If key not present (out of deviation template),
    fallback to ALL 50 causes.
    """
    p, d = normalize_parameter_deviation(parameter, deviation)
    key = f"{p}|{d}"
    return CAUSE_ELIGIBILITY_MATRIX.get(key, ALL_CAUSE_IDS)[:]


# ============================================================
# 4) Instrument-type matching + valve-aware + equipment-aware
#    + auto-filter of inapplicable causes
# ============================================================

INST_PATTERNS = {
    "pressure": re.compile(r"^(P[TI]|PI|PT|PG|PDT|DP(T|I)|DPG)\b", re.IGNORECASE),
    "temperature": re.compile(r"^(T[TI]|TI|TT|TG)\b", re.IGNORECASE),
    "level": re.compile(r"^(L[TI]|LI|LT|LG)\b", re.IGNORECASE),
    "flow": re.compile(r"^(F[TI]|FI|FT|FG|FE)\b", re.IGNORECASE),
}

VALVE_PATTERN = re.compile(r"^(FV|LV|PV|TV|CV|SV|XV|V)\b[-_ ]?\d*.*$", re.IGNORECASE)

PUMP_PATTERN = re.compile(r"^(P)\b[-_]?\d+.*$", re.IGNORECASE)          # P-225A, P225A
COMP_PATTERN = re.compile(r"^(K)\b[-_]?\d+.*$", re.IGNORECASE)          # compressor K-101
VESSEL_PATTERN = re.compile(r"^(V)\b[-_]?\d+.*$", re.IGNORECASE)        # V-225
HX_PATTERN = re.compile(r"^(E|HX)\b[-_]?\d+.*$", re.IGNORECASE)         # E-225, HX-10
REACTOR_PATTERN = re.compile(r"^(R)\b[-_]?\d+.*$", re.IGNORECASE)       # R-210
COLUMN_PATTERN = re.compile(r"^(C)\b[-_]?\d+.*$", re.IGNORECASE)        # C-220

def _norm_list(xs: Optional[List[str]]) -> List[str]:
    return [str(x).strip() for x in (xs or []) if str(x).strip()]

def classify_instruments(instruments: List[str]) -> Dict[str, List[str]]:
    """
    Returns dict buckets with typed instruments.
    """
    instruments = _norm_list(instruments)
    out = {"pressure": [], "temperature": [], "level": [], "flow": [], "all": instruments[:]}

    for inst in instruments:
        for k, pat in INST_PATTERNS.items():
            if pat.search(inst):
                out[k].append(inst)
    return out

def classify_valves(valves: List[str]) -> List[str]:
    valves = _norm_list(valves)
    return [v for v in valves if VALVE_PATTERN.search(v)]

def classify_equipment(from_id: str = "", to_id: str = "", node: str = "", context: str = "") -> Dict[str, List[str]]:
    """
    Extract equipment tags from from_id/to_id/node/context.
    This is more robust than only using node.
    """
    text = " | ".join([from_id or "", to_id or "", node or "", context or ""]).strip()

    tokens = re.findall(r"\b[A-Za-z]{1,3}[-_]?\d+[A-Za-z]?\b", text)
    tokens = [t.strip() for t in tokens if t.strip()]

    buckets = {"pump": [], "compressor": [], "vessel": [], "hx": [], "reactor": [], "column": [], "all": []}
    for t in tokens:
        buckets["all"].append(t)
        if PUMP_PATTERN.match(t): buckets["pump"].append(t)
        if COMP_PATTERN.match(t): buckets["compressor"].append(t)
        if VESSEL_PATTERN.match(t): buckets["vessel"].append(t)
        if HX_PATTERN.match(t): buckets["hx"].append(t)
        if REACTOR_PATTERN.match(t): buckets["reactor"].append(t)
        if COLUMN_PATTERN.match(t): buckets["column"].append(t)

    for k in list(buckets.keys()):
        seen = set()
        uniq = []
        for x in buckets[k]:
            if x not in seen:
                seen.add(x)
                uniq.append(x)
        buckets[k] = uniq

    return buckets

def _prefix_tags(tags: List[str], base_text: str) -> str:
    return f"{', '.join(tags)} – {base_text}" if tags else base_text

INSTR_CAUSE_TO_TYPE = {1: "pressure", 2: "temperature", 3: "level", 4: "flow"}
VALVE_CAUSES = {6, 7, 8, 9, 10, 32, 34, 35}

# Equipment-aware causes (attach best matching equipment if present)
EQUIP_CAUSES: Dict[int, List[str]] = {
    14: ["vessel", "all"],                              # vessel leak/rupture
    15: ["pump", "all"],                                # pump failure
    16: ["compressor", "all"],                          # compressor/fan failure
    17: ["pump", "compressor", "all"],                  # vacuum pump failure (site dependent)
    21: ["hx", "reactor", "column", "vessel", "all"],   # overheating anywhere
    28: ["hx", "all"],                                  # cooling system failure (often exchanger)
    29: ["hx", "reactor", "column", "vessel", "all"],   # heating failure
    30: ["hx", "reactor", "column", "vessel", "all"],   # heating uncontrolled
    36: ["reactor", "column", "vessel", "all"],         # runaway
    40: ["vessel", "all"],                              # operating empty
    41: ["vessel", "all"],                              # overfilled
    42: ["reactor", "vessel", "column", "all"],         # decomposition
}

def decorate_cause_text(
    cause_id: int,
    base_text: str,
    *,
    instruments: List[str],
    valves: List[str],
    from_id: str = "",
    to_id: str = "",
    node: str = "",
    context: str = ""
) -> str:
    """
    Adds context tags:
    - Instrument-type matching for causes 1-4 (only matching instruments)
    - Valve tags for valve-related causes
    - Equipment tags inferred from from_id/to_id/node/context for equipment-related causes
    """
    inst_by_type = classify_instruments(instruments)
    valve_tags = classify_valves(valves)
    equip = classify_equipment(from_id=from_id, to_id=to_id, node=node, context=context)

    # 1) Instrument-aware
    if cause_id in INSTR_CAUSE_TO_TYPE:
        k = INSTR_CAUSE_TO_TYPE[cause_id]
        return _prefix_tags(inst_by_type.get(k, []), base_text)

    # 2) Valve-aware
    if cause_id in VALVE_CAUSES:
        return _prefix_tags(valve_tags, base_text)

    # 3) Equipment-aware
    if cause_id in EQUIP_CAUSES:
        for bucket in EQUIP_CAUSES[cause_id]:
            tags = equip.get(bucket, [])
            if tags:
                return _prefix_tags(tags, base_text)
        return base_text

    return base_text

def auto_filter_cause_ids(
    cause_ids: List[int],
    *,
    instruments: List[str],
    valves: List[str],
    from_id: str = "",
    to_id: str = "",
    node: str = "",
    context: str = "",
    enable_auto_filter: bool = True
) -> List[int]:
    """
    Auto-removes causes that are not plausible given line tags.
    - Instrument causes 1-4 require a matching typed instrument tag
    - Valve causes require at least one valve tag
    - Equipment causes require at least one detectable equipment tag
    Safety: if it filters everything, it returns the original list.
    """
    if not enable_auto_filter:
        return cause_ids[:]

    inst_by_type = classify_instruments(instruments)
    valve_tags = classify_valves(valves)
    equip = classify_equipment(from_id=from_id, to_id=to_id, node=node, context=context)

    filtered: List[int] = []
    for cid in cause_ids:
        # Instrument causes 1-4 require matching typed instruments
        if cid in INSTR_CAUSE_TO_TYPE:
            k = INSTR_CAUSE_TO_TYPE[cid]
            if not inst_by_type.get(k):
                continue

        # Valve causes require valves
        if cid in VALVE_CAUSES and not valve_tags:
            continue

        # Equipment causes require equipment tag(s)
        if cid in EQUIP_CAUSES and not equip.get("all"):
            continue

        filtered.append(cid)

    return filtered if filtered else cause_ids[:]


# ============================================================
# 5) Payload builder for your LLM prompt input
# ============================================================

def build_eligible_causes_payload(
    parameter: str,
    deviation: str,
    *,
    instruments: Optional[List[str]] = None,
    valves: Optional[List[str]] = None,
    from_id: str = "",
    to_id: str = "",
    node: str = "",
    context: str = "",
    enable_auto_filter: bool = True
) -> Dict:
    """
    Returns a payload you can inject into your prompt:
    {
      "parameter": "...",
      "deviation": "...",
      "key": "Parameter|Deviation",
      "fallback_all_50": bool,
      "eligible_cause_ids": [...],
      "eligible_causes": [{"cause_id":1,"cause":"PT-101 – Pressure instrument failure..."}, ...]
    }
    """
    instruments = _norm_list(instruments)
    valves = _norm_list(valves)

    p, d = normalize_parameter_deviation(parameter, deviation)
    key = f"{p}|{d}"

    ids = get_eligible_cause_ids(p, d)

    ids = auto_filter_cause_ids(
        ids,
        instruments=instruments,
        valves=valves,
        from_id=from_id,
        to_id=to_id,
        node=node,
        context=context,
        enable_auto_filter=enable_auto_filter
    )

    eligible_causes: List[Dict] = []
    for cid in ids:
        base_text = CAUSE_LOOKUP[cid]
        decorated = decorate_cause_text(
            cid,
            base_text,
            instruments=instruments,
            valves=valves,
            from_id=from_id,
            to_id=to_id,
            node=node,
            context=context
        )
        eligible_causes.append({"cause_id": cid, "cause": decorated})

    return {
        "parameter": p,
        "deviation": d,
        "key": key,
        "fallback_all_50": (key not in CAUSE_ELIGIBILITY_MATRIX),
        "enable_auto_filter": enable_auto_filter,
        "eligible_cause_ids": ids,
        "eligible_causes": eligible_causes,
    }


# ============================================================
# 6) Post-LLM hard validator (recommended)
#    Enforces: no duplicates, no extra, (optionally) no missing.
# ============================================================

def validate_llm_cause_ids(
    used_cause_ids: List[int],
    *,
    parameter: str,
    deviation: str,
    instruments: Optional[List[str]] = None,
    valves: Optional[List[str]] = None,
    from_id: str = "",
    to_id: str = "",
    node: str = "",
    context: str = "",
    enable_auto_filter: bool = True,
    require_full_coverage: bool = True
) -> None:
    """
    Validate that the LLM used only eligible causes.

    If require_full_coverage=True:
      used set must equal eligible set
    else:
      used set must be subset of eligible set
    """
    if len(set(used_cause_ids)) != len(used_cause_ids):
        raise ValueError("Duplicate cause_id detected in LLM output")

    payload = build_eligible_causes_payload(
        parameter,
        deviation,
        instruments=instruments,
        valves=valves,
        from_id=from_id,
        to_id=to_id,
        node=node,
        context=context,
        enable_auto_filter=enable_auto_filter
    )
    eligible = set(payload["eligible_cause_ids"])
    used = set(used_cause_ids)

    extra = sorted(list(used - eligible))
    if extra:
        raise ValueError(f"LLM used non-eligible cause_id(s): {extra}")

    if require_full_coverage:
        missing = sorted(list(eligible - used))
        if missing:
            raise ValueError(f"LLM missed eligible cause_id(s): {missing}")


# ============================================================
# 7) Convenience: Build the exact text block to inject into your prompt
#    (e.g., under <START-DATA> as "Eligible Causes:")
# ============================================================

def build_cause_block_for_prompt(payload: Dict) -> str:
    """
    Returns a neat, deterministic cause list block:
    1) "cause_id.cause"
    """
    lines = []
    for item in payload.get("eligible_causes", []):
        lines.append(f'{item["cause_id"]}. {item["cause"]}')
    return "\n".join(lines)


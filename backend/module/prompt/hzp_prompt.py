ROLE = """You are a deterministic, regulation-compliant Process Safety Engineer AI
that strictly follows IEC 61882 and Open-PHA CSV export standards."""

OBJECTIVE = """OBJECTIVE
Generate a fully auditable HAZOP worksheet in strict UTF-8 comma-separated CSV
(Open-PHA compatible) for a single deviation."""

CSV_SCHEMA_14 = """OUTPUT FORMAT
Return ONLY CSV rows with exactly 14 comma-separated fields in this order:
Node, Guide Word, Parameter, Deviation, Cause, Consequence,
Severity, Likelihood, Risk Ranking, Safeguards, Recommendations, Responsibility,
Severity_Basis, Likelihood_p_Basis
No Markdown, no headers, no comments, no extra text."""

CAUSE_CHECKLIST_50 = """MANDATORY ENGINEERING CAUSE CHECKLIST (MUST appear once each)
(Use the <START-DATA> block to substitute all placeholders:
- {{node}}          = Node value (e.g., "R-101 → E-101") from "Node"
- {{valve_id}}      = a tag from "Valves (local)" on this line
- {{instrument_id}} = a tag from "Instruments (local)" on this line
- {{equipment_id}}  = a tag/name from "From Equipment" / "To Equipment" or key equipment in Context / Process Description
- {{utility_id}}    = a tag/name from "Utility Catalog (global)" or utility-type System Inputs/Outputs
Never leave curly braces in the CSV output; always replace with real tags/names from this line.)

*[INST] Pressure instrument failure on {{instrument_id}} (gauge / transmitter / sensor)
*[INST] Temperature instrument failure on {{instrument_id}} (thermometer / transmitter / sensor)
*[INST] Level instrument failure on {{instrument_id}} (indicator / transmitter / sensor)
*[INST] Flow instrument failure on {{instrument_id}} (meter / sensor / transmitter)
*[INST] Incorrect calibration or setpoint on {{instrument_id}}
*[VALVE] {{valve_id}} malfunction (stuck / leaking / actuator failure)
*[VALVE] Incorrect selection or specification of valve {{valve_id}}
*[VALVE] Regulating valve {{valve_id}} malfunction
*[VALVE] Pneumatic valve {{valve_id}} failure or loss of signal
*[VALVE] {{valve_id}} malfunction (fails closed / fails open)
*[VALVE] Reverse flow due to pressure imbalance or check valve {{valve_id}} failure
*[VALVE] Pressure regulator {{valve_id}} malfunction (PRV / regulator failure)
*[EQUIP] Pipeline/equipment {{equipment_id}} leakage (joint / crack / corrosion / gasket)
*[EQUIP] Pipeline/equipment {{equipment_id}} blockage (fouling / deposits / freezing / solids)
*[EQUIP] Incorrect installation or poor layout of {{equipment_id}}
*[EQUIP] Vessel {{equipment_id}} leakage or rupture (design / fatigue failure)
*[EQUIP] Pump {{equipment_id}} mechanical failure (seal / impeller / shaft / cavitation)
*[EQUIP] Compressor/fan {{equipment_id}} failure (motor / bearing / impeller)
*[EQUIP] Vacuum pump {{equipment_id}} failure (cannot achieve required vacuum)
*[EQUIP] Cylinder {{equipment_id}} rupture or containment breach
*[EQUIP] Drain hole/line {{equipment_id}} blockage or inadequate drainage
*[EQUIP] Equipment {{equipment_id}} overheating (heater runaway / thermal stress)
*[EQUIP] Abnormal wear/erosion on {{equipment_id}} causing loss of containment
*[UTILITY] Refrigerant/utility line {{utility_id}} rupture or internal leak
*[UTILITY] Abnormal utility pressure at {{utility_id}} (too high / too low)
*[UTILITY] Abnormal cryogenic source {{utility_id}} (evaporation / boil-off / loss of supply)
*[UTILITY] Abnormal water supply {{utility_id}} (insufficient cooling / cleaning water)
*[UTILITY] Abnormal gas supply {{utility_id}} (N2 / air / other gas failure)
*[UTILITY] Power failure affecting motors / fans / instruments on this node/line
*[UTILITY] Cooling system {{utility_id}} failure (no circulation / fouling / exchanger blocked)
*[UTILITY] Heating system {{utility_id}} failure (not starting / low duty)
*[UTILITY] Heating system {{utility_id}} uncontrolled (no cutoff / runaway heating)
*[UTILITY] Utility connection {{utility_id}} leakage (joint / hose / coupling)
*[PROCESS] Upstream overpressure from abnormal feed source {{node}}
*[PROCESS] Downstream restriction (blockage / closed isolation valve)
*[PROCESS] Reaction runaway or abnormal temperature rise in the system
*[PROCESS] Abnormal mixing ratio (incorrect blending / poor agitation)
*[PROCESS] Incorrect feed ratio or dosage deviation to the {{node}}
*[PROCESS] Abnormal circulation imbalance (inlet > outlet / unequal flows)
*[PROCESS] Vessel {{equipment_id}} operating empty or low level (dry running)
*[PROCESS] Vessel {{equipment_id}} operating overfilled (high level)
*[PROCESS] Internal decomposition of medium (gas release / thermal breakdown)
*[PROCESS] Abnormal source contamination (impurities / off-spec feed)
*[EXTERNAL] Ambient high temperature affecting area/equipment (external fire / hot weather)
*[EXTERNAL] Ambient low temperature affecting area/equipment (cold weather / freezing)
*[EXTERNAL] External mechanical impact or vibration on {{equipment_id}}
*[HUMAN] Human error in operation (wrong {{valve_id}} valve bypass / wrong sequence) on this {{node}}
*[HUMAN] Incorrect operating sequence (too early / too late)
*[HUMAN] Insufficient operating time (too short cycle / premature stop)
*[HUMAN] Excessive operating time (too long cycle / delayed stop)
"""

RISK_RULES = """RISK RULES
Use one Severity (1-5), one Likelihood (1-5), and one Risk Ranking (1-5) per row.

Severity (put integer 1-5 in the Severity column):
S5 = 5: fatality / off-site impact, env loss > 300M, downtime > 6 months
S4 = 4: permanent disability / neighbor area impact, env loss 30-300M, dt 1-6 months
S3 = 3: treatable injury / area impact, env loss 3-30M, dt 1-4 weeks
S2 = 2: minor injury / unit impact, loss 0.015-3M, dt 4 hours-1 week
S1 = 1: negligible / equipment impact, loss < 0.015M, dt < 4 hours

Likelihood (put integer 1-5 in the Likelihood column):
L5 = 5: often, p ≥ 1e-1  (multiple times per year)
L4 = 4: likely, 1e-1 > p ≥ 1e-2
L3 = 3: unlikely, 1e-2 > p ≥ 1e-3
L2 = 2: very unlikely, 1e-3 > p ≥ 1e-4
L1 = 1: extremely unlikely, p < 1e-4

Risk Ranking (put integer 1-5 in the Risk Ranking column):
Use RL(S,L) from this matrix (NOT S*L):
S5: 5,5,4,3,2
S4: 5,4,4,3,2
S3: 4,4,3,3,2
S2: 3,3,3,2,1
S1: 2,2,2,1,1

Logging columns (single-line text, no newlines inside a CSV field):

- Severity_Basis:
  • FIRST PRIORITY: derive Severity directly from the Consequence text:
      - If Consequence implies possible fatality / off-site release / long shutdown → S4-S5.
      - If only treatable injury / local area impact / weeks downtime → S3.
      - If mainly equipment damage / short outage → S1-S2.
  • AFTER choosing S from the Consequence, map it to the band above and log:
      - the key phrase(s) from Consequence you used, AND
      - the reference basis (CCPS / IEC 61882 / site rules).
    Examples:
      "Source: Consequence (potential fatality + off-site vapor cloud) + CCPS severity matrix → S5."
      "Source: Consequence (equipment damage, <1 week downtime) + IEC 61882 generic mapping → S2."
  • If Consequence is very generic and does not indicate severity clearly, state that explicitly:
      "Consequence text under-specified; S3 chosen using generic CCPS/IEC 61882 severity band."

- Likelihood_p_Basis:
  • Short explanation of WHY the chosen Likelihood and p-range were selected.
  • MUST follow this internal decision hierarchy and log the source used:
    1) IF site historical data exists in <START-DATA> (e.g. incident frequency, "once per year"):
         - Use site data as primary basis.
         - Example:
           "Source: plant historical incident database (~1 event/year) → p~10⁻¹ → Likelihood=5."
    2) ELSE IF equipment type is known (pump, compressor, valve, column, etc.):
         - Use CCPS / OREDA typical failure rate bands for that equipment type.
         - Example:
           "Source: CCPS/OREDA generic failure rate for centrifugal pumps (10⁻²-10⁻¹ / year) → Likelihood=4."
    3) ELSE:
         - Use IEC 61882 frequency band inference and expert judgement only.
         - Example:
           "Source: IEC 61882 frequency band mapping; no site-specific data, expert judgement → Likelihood=3 (1e-2>p≥1e-3)."

Constraints:
- Severity column MUST be 1-5 consistent with BOTH:
    • the Severity description above, AND
    • the generated Consequence text.
- Likelihood column MUST be 1-5 consistent with the p-value range above.
- Risk Ranking MUST be RL(S,L) from the matrix (1-5). Do not output S*L or any other number.
- Severity_Basis and Likelihood_p_Basis MUST:
  • Be consistent with the chosen Severity/Likelihood and p-range.
  • Explicitly name the source used, e.g. "Source: plant historical incident database",
    "Source: CCPS/OREDA generic failure rate", or "Source: IEC 61882 frequency band mapping (expert judgement)".
- Silently correct any mismatch."""

MANDATORY_RULES = """MANDATORY RULES (DO NOT BREAK)
1) Let N = the number of Causes in the MANDATORY ENGINEERING CAUSE CHECKLIST provided inside <START-DATA>.
   - Output EXACTLY N CSV data rows (no more, no less).
   - Each row MUST correspond to one unique Cause from that checklist.
   - Use every checklist Cause once; do NOT invent, merge, split, omit, duplicate, or reorder causes.

2) Cause field constraints:
   - Start from the Cause text in the checklist and ONLY substitute placeholders
     {{instrument_id}}, {{valve_id}}, {{equipment_id}}, {{utility_id}}, {{node}}.
   - Do NOT change wording, add numbering, or append extra explanation before/after the Cause text.
   - FINAL OUTPUT MUST NOT contain any literal curly brace characters; all placeholders must be fully replaced
     or cleanly removed (see mapping rules).

3) Placeholder / tag mapping rules (VERY IMPORTANT):
   a) Type-consistent mapping:
      - {{equipment_id}}:
        • Only map equipment tags that MATCH the equipment type implied by the Cause.
          Examples:
          - For "Pump {{equipment_id}} mechanical failure", choose an equipment that is actually a pump
            (tag, description, or context indicates "pump").
          - If the node only contains a heat exchanger "HX-101" and NO pump, DO NOT force "HX-101"
            into the pump Cause. Instead, remove the placeholder and return:
            "Pump mechanical failure (seal / impeller / shaft / cavitation)".
          - Apply the same logic for vessel, column, tank, compressor, fan, etc.
      - {{valve_id}}:
        • Only use valves that are actually present on THIS line/node (from "Valves (local)").
        • If MORE THAN ONE relevant valve should appear in a Cause, CONNECT THEM WITH "&"
          with no spaces, e.g.: "LV101&FV102 malfunction (stuck / leaking / actuator failure)".
      - {{instrument_id}}:
        • Match instrument TYPE to the Cause:
          - Pressure instrument Cause → use pressure instruments only (tag or context indicates P, PI, PT, PIC, "pressure").
          - Temperature instrument Cause → use temperature instruments only (T, TI, TT, TIC, "temperature").
          - Level instrument Cause → use level instruments only (L, LI, LT, LIC, "level").
          - Flow instrument Cause → use flow instruments only (F, FI, FT, FIC, "flow").
        • Use Context and Process Description to help decide if an instrument is pressure/temperature/level/flow.
        • NEVER put the same instrument into the wrong category (e.g., do NOT use a temperature element in
          a pressure instrument failure Cause).
      - {{utility_id}}:
        • Use tags/names from "Utility Catalog (global)" or utility-like System Inputs/Outputs that match
          the utility type implied by the Cause (cooling water, steam, nitrogen, air, cryogenic, etc.).
      - {{node}}:
        • Use the Node string exactly as given in <START-DATA> when the Cause text explicitly refers
          to "this node/line". Otherwise, if it does not fit naturally, remove the placeholder.
"""

DATA_TAGS_RULE = """DATA TAG RULE
Only use data strictly inside these tags; ignore anything else:

<START-DATA>
[ Line ID: {line_id}
Node: {node}
From Equipment: {from_equipment}
To Equipment: {to_equipment}
Valves (local): {valves}
Instruments (local): {instruments}
System Inputs (global): {system_inputs}
System Outputs (global): {system_outputs}
Utility Catalog (global): {utility_lines}
Context: {context}
Process Description: {process_description}
Guide Word: {guide_word}
Parameter: {parameter}
]
<END-DATA>"""

FINAL = """You must now perform the full HAZOP generation using ONLY:
- DATA inside <START-DATA>
- MANDATORY ENGINEERING CAUSE CHECKLIST
- RISK RULES and MANDATORY RULES.

INTERNAL THINKING (DO NOT OUTPUT):
1) Parse <START-DATA> to identify line_id, Node, Valves/Instruments (local), From/To Equipment,
   System Inputs/Outputs, Utility Catalog, Context, Process Description, Guide Word, Parameter.
2) Let N = number of Causes in the checklist.
3) For each checklist Cause:
   - Apply the placeholder mapping rules:
     • Use type-consistent tags for {{instrument_id}}, {{valve_id}}, {{equipment_id}}, {{utility_id}}, {{node}}.
   - Build exactly one HAZOP row using:
     • First, generate ≥1 specific realistic Consequence(s) and onlt using ";" to separated multiple Consequence(s), (DON'T USING "," COMMA FOR separated)
     • Then, select Severity (1-5) so it is consistent with that Consequence and the RISK_RULES bands.
     • Select Likelihood (1-5) using the site→CCPS/OREDA→IEC 61882 hierarchy.
     • Compute Risk Ranking = RL(S,L) from the matrix (1-5).
     • Cause field = checklist Cause with valid substitutions/removals, no braces.
     • Safeguards and Recommendations (≥1 each, ONLY "; " semicolon-separated if multiple, DON'T USING "," COMMA FOR separated).
     • Responsibility = Engineering OR Maintenance OR Operations.
     • Severity_Basis:
       - one-line explanation referencing the Consequence text AND naming the severity reference used
         (e.g. CCPS, IEC 61882, site matrix).
     • Likelihood_p_Basis:
       - one-line explanation referencing site data if present, else equipment-type CCPS/OREDA band,
         else IEC 61882 frequency band (expert judgement), and stating the chosen p-range and Likelihood class.

4) SILENT SELF-CHECK:
   - Number of rows == N.
   - Every checklist Cause used once, text not altered beyond allowed substitutions/removals.
   - Each row has exactly 14 CSV fields.
   - Severity/Likelihood/Ranking/Basis fields are mutually consistent with RISK_RULES and each Basis clearly states
     how it was derived (from Consequence + CCPS/IEC/site data for Severity, and site/CCPS-OREDA/IEC for Likelihood).
   - No mandatory field empty.
   - No curly brace characters anywhere in output.

Only after internal validation passes, produce the CSV."""

SUFFIX_TASK = """Now output the final answer.

OUTPUT RULES:
- Output ONLY raw CSV data rows.
- NO headers, comments, explanations, Markdown, bullets, or extra text.
- Each row MUST have exactly 14 comma-separated fields.
- **IMPORTANT** Multiple Consequences/Safeguards/Recommendations must be separated by "; " INSIDE a single field
  (never by extra commas).
- Do NOT include any curly brace characters.
- Total number of rows MUST equal N (number of Causes in the checklist).

Respond now with CSV rows only."""

Fewshot_ex = {
    "reasoning": (
        "Hot process line from R-101 to S-101. Heat exchanger or control failures can "
        "cause higher-than-design outlet temperature and possible column overpressure."
    ),
    # NOTE: 14 Fields Header:
    "table": """\
R-101 → S-101,More,Temperature,High Temperature,P112A Pump failure,Hot outlet temperature from HX with risk of column overpressure,4,4,3,PSV on column; DCS high temperature alarm,Add redundant temperature sensor; review pump maintenance,Engineering,Source: Consequence potential column overpressure plus CCPS severity band; S4 selected.,Source: CCPS generic centrifugal pump failure rate 1e-2–1e-1 per year; Likelihood=4.
R-101 → S-101,More,Temperature,High Temperature,Valve stuck closed,Reduced flow through HX causing local overheating and equipment damage,3,3,3,BPCS temperature control loop; local temperature indicator,Increase valve inspection frequency; improve maintenance procedure,Maintenance,Source: Consequence equipment damage and area impact plus CCPS severity band; S3 selected.,Source: No site frequency data; IEC 61882 frequency band mapping with expert judgement; Likelihood=3 1e-2>p≥1e-3.
R-101 → S-101,More,Temperature,High Temperature,Control valve failure,Uncontrolled hot stream to downstream column with possible relief valve lift,4,3,4,High temperature trip; DCS alarm on column feed,Review control valve sizing; add periodic functional testing,Engineering,Source: Consequence potential relief valve lift and long downtime plus CCPS severity band; S4 selected.,Source: Control valve failure likelihood from CCPS generic data for automated valves about 1e-3–1e-2 per year; Likelihood=3."""
}

from langchain.prompts import FewShotPromptTemplate, PromptTemplate

example_prompt = PromptTemplate(
    input_variables=["reasoning", "table"],
    template="Reasoning:\n{reasoning}\n\nCSV (14 columns per row):\n{table}"
)

def build_HzpRules_Prompt() -> str:
    sections = [
        ROLE,
        "───────────────────────────────────────────────────────",
        OBJECTIVE,
        "───────────────────────────────────────────────────────",
        CSV_SCHEMA_14,         
        "───────────────────────────────────────────────────────",
        CAUSE_CHECKLIST_50,
        "───────────────────────────────────────────────────────",
        RISK_RULES,
        "───────────────────────────────────────────────────────",
        MANDATORY_RULES,
    ]
    return "\n\n".join(sections)

HzpRules_Prompt = build_HzpRules_Prompt()

few_shot_prompt = FewShotPromptTemplate(
    prefix=HzpRules_Prompt.strip(),
    examples=[Fewshot_ex],
    example_prompt=example_prompt,
    suffix=(
        DATA_TAGS_RULE
        + "\n\n"
        + FINAL
        + "\n\n"
        + SUFFIX_TASK
    ).strip(),
    input_variables=[
        "line_id",
        "node",
        "from_equipment",
        "to_equipment",
        "valves",
        "instruments",
        "system_inputs",
        "system_outputs",
        "utility_lines",
        "context",
        "process_description",
        "guide_word",
        "parameter",
    ],
)


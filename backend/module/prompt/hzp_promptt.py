"""Prompt pack for topology-aware HAZOP/LOPA generation with OpenAI File Search.

This version is designed for Option 2:
- Upload HAZOP guide files once to an OpenAI vector store.
- During each agent run, pass only topology/P&ID node data plus vector_store_id.
- The model must call file_search to retrieve cause rules, IPL/likelihood guidance,
  risk matrix, HAZOP workflow, output template, and matched few-shot context.

Output contract:
- one selected node and one selected deviation per call
- exactly 5 causes per deviation
- exactly 5 consequences per cause
- exactly 25 CSV rows per deviation
- 20-column Integrated HAZOP/LOPA worksheet style
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Optional

HAZOP_LOPA_HEADERS_20 = [
    "Node",
    "Design Intention",
    "Parameter",
    "Guide Word",
    "Deviation",
    "Cause",
    "Consequence",
    "Initial Severity",
    "Initial Likelihood",
    "Initial Risk Ranking",
    "IPLs",
    "IPL Independent",
    "IPL Effective",
    "IPL Auditable",
    "Safeguards",
    "Final Severity",
    "Final Likelihood",
    "Final Risk Ranking",
    "Recommendations",
    "Comments_Actions",
]

CSV_SCHEMA_HAZOP_LOPA_20 = """OUTPUT FORMAT - INTEGRATED HAZOP/LOPA CSV
Return ONLY CSV rows with exactly 20 comma-separated fields in this order:
Node, Design Intention, Parameter, Guide Word, Deviation, Cause, Consequence,
Initial Severity, Initial Likelihood, Initial Risk Ranking,
IPLs, IPL Independent, IPL Effective, IPL Auditable,
Safeguards, Final Severity, Final Likelihood, Final Risk Ranking,
Recommendations, Comments_Actions

Mapping to Integrated HAZOP/LOPA worksheet:
- Guide Word = GW
- Deviation = DEVIATION
- Cause = CAUSES
- Consequence = CONSEQUENCES
- Initial Severity / Initial Likelihood / Initial Risk Ranking = first S L R
- IPLs = IPLs credited for likelihood reduction
- IPL Independent / IPL Effective / IPL Auditable = Meet IPL criteria columns
- Safeguards = non-IPL safeguards or controls that are not credited as IPL
- Final Severity / Final Likelihood / Final Risk Ranking = mitigated S L R
- Recommendations = HAZOP recommendations
- Comments_Actions = comments / actions / opportunity for improvements

Strict CSV rules:
- No Markdown, no header row, no comments outside CSV rows.
- Each output row must have exactly 20 fields.
- Free-text fields must be single-line text.
- Do not use raw commas inside any free-text field; replace internal commas with semicolons.
- Use semicolon plus space to separate multiple items inside one field.
- Do not use newline characters inside any field.
- Do not leave placeholders, curly braces, or source-copy artifacts in the output.
"""

ROLE = """ROLE
You are a deterministic Process Safety Engineer AI specialized in HAZOP and LOPA worksheet generation.
You follow IEC 61882-style HAZOP reasoning and integrated HAZOP/LOPA worksheet practice.
You must reason like a HAZOP leader: node boundary first, design intent second, guide word and parameter third, then credible initiating causes, consequences, initial risk, IPLs/safeguards, mitigated risk, and recommendations.
"""

FILE_SEARCH_RULES = """MANDATORY FILE SEARCH RULES
You are connected to an OpenAI vector store through file_search.
Before generating the CSV rows, use file_search to retrieve relevant evidence from the uploaded HAZOP knowledge base.
Search for these items as needed:
1) Step 4 cause-selection rules from cause.json.
2) HAZOP workflow steps from HAZOP-GUIDE-SKILL.
3) Initiating event likelihood and IPL probability / credit rules from HAZOP-IPL-LIKELIHOOD and HAZOP_LOPA-GUIDE.
4) Risk ranking matrix from HAZOP-RISK-LEVEL-GUIDE.
5) Integrated HAZOP/LOPA output template from HAZOP-OUTPUT-TEMPLATE.
6) Matched case examples from the Naphtha Tank worksheet and De-C5 tower worksheet when topology matches.

Use retrieved text as engineering evidence and style guidance.
Do not copy retrieved worksheet wording verbatim. Preserve engineering intent and tags where applicable but paraphrase in professional Process Safety Engineer wording.
"""

LOCAL_KNOWLEDGE_RULES = """MANDATORY REFERENCE KNOWLEDGE RULES
You have NO search tools available. Do not call file_search or any other tool, and
never emit tool-call syntax such as <file_search.query ...> in your output.
All reference evidence you may use is supplied inline in the REFERENCE KNOWLEDGE
section of this prompt. Use it for:
1) Step 4 cause-selection rules.
2) HAZOP workflow steps.
3) Initiating event likelihood and IPL probability / credit rules.
4) Risk ranking matrix.
5) Integrated HAZOP/LOPA output template.
6) Matched case examples when topology matches.

Use the supplied text as engineering evidence and style guidance.
Do not copy supplied wording verbatim. Preserve engineering intent and tags where applicable but paraphrase in professional Process Safety Engineer wording.
If the supplied knowledge does not cover something, state that explicitly rather than inventing a basis.
"""

TOPOLOGY_MATCH_RULES = """CASE MATCHING AND FEW-SHOT USE RULES
Always compare the current topology data with the embedded few-shot cases and retrieved source documents.

Case A - Naphtha Tank / Transfer Pump match:
Use the Naphtha few-shot case when the node or process data contains any strong combination of these cues:
- Naphtha, tank storage, storage tank, 100T-01, transfer pump, 100P-01A/B, HPU, UV-0101, UV-0102, PCV-0101, PCV-0102, PVV-0102, EH0101, LSLL-0102A, LSHH-0102A.
When matched, keep approximately 75-80 percent engineering fidelity to the Naphtha worksheet logic while paraphrasing every column.
Do not force exact wording. Keep tags and scenario structure when the topology supports them.

Case B - De-C5 Tower match:
Use the De-C5 few-shot case when the node or process data contains any strong combination of these cues:
- De-C5, C5 tower, T-00, column, reboiler, E-05, feed FIC-001, FV-001, FIC-005, FV-005, FV-003, PIC-002, TIC-012, PI-004, PSV-003A/B, P-06A/B.
When matched, keep approximately 75-80 percent engineering fidelity to the De-C5 worksheet logic while paraphrasing every column.
Do not force exact wording. Keep tags and scenario structure when the topology supports them.

If the matched few-shot case contains fewer than 25 complete rows for the selected deviation, complete the worksheet by generating the best credible missing cause-consequence scenarios from the node topology, retrieved cause rules, and HAZOP guide rules.
If neither case matches, do not force either case. Generate from topology and retrieved HAZOP rules.
"""

PARAPHRASE_RULES = """MANDATORY PARAPHRASE AND PROFESSIONAL STYLE RULES
Before writing the final CSV response, silently paraphrase all free-text columns into Process Safety Engineer specialist style.
This applies to Node, Design Intention, Deviation, Cause, Consequence, IPLs, Safeguards, Recommendations, and Comments_Actions.
Requirements:
- Keep engineering meaning, risk logic, equipment tags, instrument tags, and credit values unchanged where supported.
- Improve clarity, specificity, and auditability.
- Avoid casual language and vague phrasing.
- Do not copy worksheet sentences directly from source files.
- Maintain approximately 75-80 percent technical correctness relative to matched source cases; use best engineering judgement to complete missing rows.
- Do not expose the paraphrasing step. Output only the final CSV rows.
"""

HAZOP_METHOD_RULES = """HAZOP METHOD RULES - FOLLOW THIS ORDER
1) Confirm the system boundary as the selected Node.
2) Define design intent from Process Description, Context, From Equipment, To Equipment, flow direction, operating pressure, operating temperature, inventory, utility purpose, and production purpose when available.
3) Derive the selected deviation by coupling Guide Word and Parameter.
4) Identify credible initiating causes and consequences:
   - Cause must directly create the selected deviation.
   - Consequence must be the credible escalation from the cause and deviation.
   - Ignore IPLs and safeguards when writing the Consequence field.
   - Evaluate initial Severity, Likelihood, and Risk Ranking before safeguards/IPLs.
5) Identify IPLs and non-IPL safeguards:
   - IPLs must be independent, effective, and auditable to receive credit.
   - Record IPL credit in the IPLs field as (-1), (-2), etc.
   - Put controls that are not credited as IPL in Safeguards.
6) Evaluate Final Severity, Final Likelihood, and Final Risk Ranking after valid IPL credit only.
7) Recommend actions when final risk is not clearly tolerable or where proof testing, alarm response, inspection, procedure, or SIF classification is needed.
"""

CAUSE_GENERATION_RULES = """CAUSE GENERATION RULES - EXACTLY 5 CAUSES PER DEVIATION
For the selected Guide Word and Parameter, generate exactly 5 causes.
Use the selected node boundary and only use equipment, valves, instruments, and utilities inside the node or direct node interface.

Cause hierarchy:
1) Prefer tagged local valves, instruments, equipment, utilities, and control loops in START-DATA.
2) Prefer retrieved cause.json rules that match the selected Parameter and Guide Word.
3) If fewer than 5 tagged causes are visible, create remaining causes from credible generic node-local failure modes using the actual equipment type.
4) Do not invent unrelated equipment tags. If a tag is unavailable, use equipment name/type from the node.
5) Do not duplicate causes. Separate valve mechanical failure, instrument false reading, controller failure, utility failure, operator line-up error, and equipment mechanical failure.
6) Reject double jeopardy as a normal initiating cause.
7) Reject natural events or external process impacts unless explicitly stated as a design case.
8) Reject arbitrary manual valve error for maintenance bypass/tie-in valves not normally operated.
9) Do not use a consequence, deviation, safeguard failure, low level, high pressure, cavitation, fire, explosion, or loss of containment as the Cause itself.
"""

CONSEQUENCE_GENERATION_RULES = """CONSEQUENCE GENERATION RULES - EXACTLY 5 CONSEQUENCES PER CAUSE
For each of the 5 causes, generate exactly 5 consequences.
Each consequence must be a distinct credible escalation path from the same cause and selected deviation.
Consequences must be specific to the node and process material.
Consequences must not assume alarms, interlocks, PSV, operator response, or safeguards.
Consequence wording should follow HAZOP practice: immediate process effect; equipment/integrity effect; safety/LOPC effect where credible; environmental or asset/production effect where credible.
A no-safety/no-further-study consequence may be used only when genuinely applicable.
"""

NUMBERING_RULES = """NUMBERING RULES
Use worksheet-style numbering inside Deviation, Cause, Consequence, IPLs, Safeguards, Recommendations, and Comments_Actions.
- Deviation: 1. <Deviation text> for the selected deviation in this call.
- Cause: 1.C <Cause text> where C = 1 to 5.
- Consequence: 1.C.K <Consequence text> where K = 1 to 5.
- IPLs: use 1.C.K.1, 1.C.K.2, etc. for multiple IPLs.
- Safeguards: use 1.C.K.S1, 1.C.K.S2, etc. for non-IPL safeguards.
- Recommendations: use 1.C.K.R1, 1.C.K.R2, etc.
Total rows = 5 causes x 5 consequences = 25 rows.
"""

RISK_RULES = """RISK RULES - SCG / INTEGRATED HAZOP-LOPA STYLE
Severity / Consequence category:
S5 = 5: multiple fatalities or severe environmental damage or property loss > 10,000,000 USD.
S4 = 4: fatality or irreversible health effects or significant environmental damage or property loss 1,000,000-10,000,000 USD.
S3 = 3: lost-time injury or media coverage environmental damage or property loss 100,000-1,000,000 USD.
S2 = 2: medical treatment case or some environmental damage or property loss 10,000-100,000 USD.
S1 = 1: minor injury or minor environmental damage or property loss 0-10,000 USD.

Likelihood / Frequency category:
L1 = 1: very likely to occur; p >= 1e-1 per year.
L2 = 2: likely during plant lifetime; 1e-1 > p >= 1e-2 per year.
L3 = 3: unlikely but possible during plant lifetime; 1e-2 > p >= 1e-3 per year.
L4 = 4: very unlikely; 1e-3 > p >= 1e-4 per year.
L5 = 5: extremely unlikely; p < 1e-4 per year.

Risk Ranking R uses categories R1-R4:
R1 = Category I / intolerable.
R2 = Category II / undesirable.
R3 = Category III / tolerable with controls.
R4 = Category IV / tolerable as-is or opportunity for improvement.

Risk matrix R(L,S), columns S1 S2 S3 S4 S5:
L1: R4, R2, R2, R1, R1
L2: R4, R3, R2, R2, R1
L3: R4, R4, R3, R2, R1
L4: R4, R4, R4, R3, R2
L5: R4, R4, R4, R4, R3

IPL credit:
- Each valid IPL credit (-1) increases likelihood category by one step toward L5.
- Each valid IPL credit (-2) increases likelihood category by two steps toward L5.
- Final Likelihood = min(5, Initial Likelihood + total valid IPL credit).
- Final Severity normally equals Initial Severity unless inherently safer design eliminates or changes the consequence.
- Final Risk Ranking = R(Final Likelihood, Final Severity).
- If an IPL is not independent, effective, and auditable, put it in Safeguards or mark criteria No and do not apply credit.
- Do not multiply S x L. Use only R1-R4 categories above.
"""

IPL_AND_SAFEGUARD_RULES = """IPL AND SAFEGUARD RULES
Credited IPL examples when independent, effective, and auditable:
- SIF or interlock with defined action and proof test.
- PSV, PVV, breather valve, emergency vent, or thermal relief valve when correctly sized and maintained.
- Independent alarm plus operator action when alarm is clear, timely, trained, proceduralized, and independent from the initiating event.
- Overflow line or open vent when correctly designed with no credible impediment.
- Mechanical stop, captive key, car seal, or lock system when it prevents the scenario.

Common safeguards / non-IPL examples:
- BPCS control loop not independent from the initiating event.
- Local indicator, local gauge, normal operator monitoring, routine check, PM program, design margin, or alarm with insufficient response basis.
- Equipment design features that are not auditable as IPLs.

When no credible IPL exists, write "No credited IPL identified" and set IPL Independent, IPL Effective, and IPL Auditable to No.
"""

FEW_SHOT_CASE_LIBRARY = r"""FEW-SHOT CASE LIBRARY - PARAPHRASED REFERENCE SCENARIOS
These rows are not complete worksheets. They are style and engineering-logic examples only.
When topology matches, use the relevant case pattern with about 75-80 percent engineering fidelity and complete exactly 25 rows for the selected deviation.
Do not copy these rows exactly. Paraphrase into Process Safety Engineer specialist style.

Naphtha Tank / Transfer Pump examples:
Naphtha Tank Storage 100T-01 with Transfer Pump 100P-01A/B,Naphtha is stored as buffer inventory and transferred to HPU through 100P-01A/B at normal transfer flow,Flow,No/Less,1. No/Less Flow,1.1 UV-0101 closes on the tank inlet path,1.1.1 Tank inventory decreases while transfer demand continues; pump suction deteriorates; cavitation and mechanical seal leakage may lead to local pool fire,3,1,R2,1.1.1.1 LAL-0101A with operator response (-1); 1.1.1.2 IS-10 LSLL-0102A stops 100P-01A/B (-1),Yes,Yes,Yes,1.1.1.S1 Routine tank level monitoring,3,3,R3,1.1.1.R1 Confirm SIL classification and proof-test interval for IS-10 low-low level pump trip,Paraphrased Naphtha reference pattern
Naphtha Tank Storage 100T-01 with Transfer Pump 100P-01A/B,Naphtha is stored as buffer inventory and transferred to HPU through 100P-01A/B at normal transfer flow,Flow,No/Less,1. No/Less Flow,1.1 UV-0101 closes on the tank inlet path,1.1.2 Upstream transfer line becomes blocked against the process unit outlet; line pressure may rise but design rating prevents loss of containment; no safety escalation is expected,1,1,R4,No credited IPL identified,No,No,No,1.1.2.S1 Line design pressure margin and upstream pump limitation,1,1,R4,1.1.2.R1 No additional action required when design margin is verified,Paraphrased Naphtha reference pattern
Naphtha Tank Storage 100T-01 with Transfer Pump 100P-01A/B,Naphtha is stored as buffer inventory and transferred to HPU through 100P-01A/B at normal transfer flow,Flow,No/Less,1. No/Less Flow,1.2 UV-0102 closes on the pump suction outlet,1.2.1 Naphtha supply to 100P-01A/B is lost; pump cavitation and seal damage may cause hydrocarbon leakage and fire exposure,3,1,R2,1.2.1.1 IS-10 ZSC-0102 stops the naphtha transfer pump (-1),Yes,Yes,Yes,1.2.1.S1 Operator awareness of abnormal pump suction condition,3,2,R2,1.2.1.R1 Verify ZSC-0102 trip classification and functional test interval,Paraphrased Naphtha reference pattern
Naphtha Tank Storage 100T-01 with Transfer Pump 100P-01A/B,Naphtha is stored as buffer inventory and transferred to HPU through 100P-01A/B at normal transfer flow,Flow,No/Less,1. No/Less Flow,1.2 UV-0102 closes on the pump suction outlet,1.2.2 Blocked-in naphtha between closed valve and downstream equipment can thermally expand; small-bore piping or gasket leak may result in flammable liquid release,3,1,R2,1.2.2.1 PSV-0101 thermal relief valve (-2),Yes,Yes,Yes,1.2.2.S1 Inspection of blocked-in liquid segments,3,3,R3,1.2.2.R1 Verify thermal relief sizing and discharge destination,Paraphrased Naphtha reference pattern
Naphtha Tank Storage 100T-01 with Transfer Pump 100P-01A/B,Naphtha is stored as buffer inventory and transferred to HPU through 100P-01A/B at normal transfer flow,Flow,No/Less,1. No/Less Flow,1.3 100P-01A/B stops unexpectedly,1.3.1 HPU feed is interrupted; buffer inventory prevents immediate production loss but prolonged outage can reduce downstream feed continuity,2,1,R2,No credited IPL identified,No,No,No,1.3.1.S1 Standby pump availability and operator monitoring,2,1,R2,1.3.1.R1 Confirm pump auto-start or operating response for transfer continuity,Paraphrased Naphtha reference pattern
Naphtha Tank Storage 100T-01 with Transfer Pump 100P-01A/B,Naphtha is stored as buffer inventory and transferred to HPU through 100P-01A/B at normal transfer flow,Flow,No/Less,1. No/Less Flow,1.3 100P-01A/B stops unexpectedly,1.3.2 Continuous upstream naphtha inflow with no transfer-out can increase 100T-01 level; overfill can create loss of containment and pool fire,4,1,R1,1.3.2.1 LAH-0101A with operator response (-1); 1.3.2.2 IS-9 LSHH-0102A closes UV-0101 (-1),Yes,Yes,Yes,1.3.2.S1 Routine tank level surveillance,4,3,R2,1.3.2.R1 Confirm SIL classification for IS-9 high-high level inlet isolation,Paraphrased Naphtha reference pattern
Naphtha Tank Storage 100T-01 with Transfer Pump 100P-01A/B,Naphtha tank vapor space is maintained by nitrogen blanketing and pressure relief devices,Pressure,High,1. High Pressure,1.1 PCV-0102 fails closed on pressure control outlet path,1.1.1 Tank pressure increases; roof or weak seam damage can release hydrocarbon vapor and liquid; ignition may cause pool fire,4,1,R1,1.1.1.1 PVV-0102 (-2); 1.1.1.2 EH0101 emergency vent (-2),Yes,Yes,Yes,1.1.1.S1 Vent inspection and tank pressure monitoring,4,5,R4,1.1.1.R1 Verify PVV-0102 and EH0101 sizing for credible overpressure cases,Paraphrased Naphtha reference pattern
Naphtha Tank Storage 100T-01 with Transfer Pump 100P-01A/B,Naphtha tank vapor space is maintained by nitrogen blanketing and pressure relief devices,Pressure,Low,1. Low Pressure,1.1 PCV-0101 fails closed on nitrogen blanketing supply,1.1.1 Tank vacuum develops during pump-out or cooling; shell deformation or air ingress can create loss of containment and fire potential,4,1,R1,1.1.1.1 PVV-0102 vacuum relief (-2),Yes,Yes,Yes,1.1.1.S1 Nitrogen supply pressure indication,4,3,R2,1.1.1.R1 Add or verify low-pressure alarm on 100T-01 vapor space,Paraphrased Naphtha reference pattern
Naphtha Tank Storage 100T-01 with Transfer Pump 100P-01A/B,Naphtha tank vapor space and liquid inventory respond to ambient and process temperature changes,Temperature,High,1. High Temperature,1.1 Thermal expansion of naphtha inventory,1.1.1 Vapor pressure and tank pressure increase; roof damage and hydrocarbon release may occur followed by pool fire if ignition is present,4,2,R2,1.1.1.1 PVV-0102 (-2); 1.1.1.2 EH0101 emergency vent (-2),Yes,Yes,Yes,1.1.1.S1 Temperature monitoring and vent maintenance,4,5,R4,1.1.1.R1 Confirm emergency vent basis includes maximum credible liquid/vapor expansion,Paraphrased Naphtha reference pattern

De-C5 Tower examples:
De-C5 Tower T-00,C5 and lighter components are stripped from feed by controlled feed flow pressure tower temperature and reboiler duty,Flow,No,1. No Flow,1.1 FV-001 fails closed on the feed control valve to E-02,1.1.1 Reboiler duty continues while feed is lost; T-00 pressure rises and level falls; overpressure can lead to hydrocarbon release with fire or explosion,5,1,R1,1.1.1.1 PI-004 high-pressure alarm with boardman action (-1); 1.1.1.2 TIC-012 BPCS temperature control (-1); 1.1.1.3 PSV-003A/B (-2),Yes,Yes,Yes,1.1.1.S1 LIC-001 low-level alarm; 1.1.1.S2 TI-008 to TI-014 high-temperature alarms,5,5,R3,1.1.1.R1 Verify IPL independence and proof-test basis for credited pressure and temperature protection,Paraphrased De-C5 reference pattern
De-C5 Tower T-00,C5 and lighter components are stripped from feed by controlled feed flow pressure tower temperature and reboiler duty,Flow,No,1. No Flow,1.2 FIC-005 reads low and drives FV-005 closed on bottom circulation,1.2.1 Bottom circulation decreases without credible safety health or environmental impact; no further hazard escalation is expected,1,1,R4,No credited IPL identified,No,No,No,1.2.1.S1 Operator monitoring of bottom circulation trend,1,1,R4,1.2.1.R1 No additional action required when no SHE or asset consequence is confirmed,Paraphrased De-C5 reference pattern
De-C5 Tower T-00,C5 and lighter components are stripped from feed by controlled feed flow pressure tower temperature and reboiler duty,Flow,No,1. No Flow,1.3 FV-003 fails closed on medium-pressure steam to E-05,1.3.1 Reboiler heat input is lost; T-00 level rises due to reduced boil-up; hydrocarbon relief to atmosphere via PSV can create pool fire exposure,5,1,R1,1.3.1.1 TI-014 low-bottom-temperature alarm with boardman action (-1); 1.3.1.2 LIC-001 BPCS level control (-1),Yes,Yes,Yes,1.3.1.S1 PI-004 PI-011 and PA-005 high-pressure alarms,5,3,R2,1.3.1.R1 Consider independent high-level interlock to cut feed to T-00,Paraphrased De-C5 reference pattern
De-C5 Tower T-00,C5 and lighter components are stripped from feed by controlled feed flow pressure tower temperature and reboiler duty,Flow,No,1. No Flow,1.3 FV-003 fails closed on medium-pressure steam to E-05,1.3.2 Liquid level can continue rising until tower skirt loading becomes limiting; structural failure may release hydrocarbons and cause pool fire,5,1,R1,1.3.2.1 Tower skirt design for full liquid load (-2); 1.3.2.2 LIC-001 BPCS level control (-1),Yes,Yes,Yes,1.3.2.S1 Low bottom temperature alarm; 1.3.2.S2 high pressure alarms,5,4,R3,1.3.2.R1 Develop SOP for operator response to TI-014 low-temperature alarm,Paraphrased De-C5 reference pattern
De-C5 Tower T-00,C5 and lighter components are stripped from feed by controlled feed flow pressure tower temperature and reboiler duty,Flow,No,1. No Flow,1.4 LV-003 fails closed on condensate drum level-control path,1.4.1 Loss of liquid withdrawal function can create the same escalation as steam-side no-flow; tower level and pressure may increase with hydrocarbon release potential,5,1,R1,1.4.1.1 Use same credited IPL basis as FV-003 no-steam high-level scenario when independent and applicable,Yes,Yes,Yes,1.4.1.S1 Alarm and operator monitoring basis as applicable,5,3,R2,1.4.1.R1 Verify equivalency before referencing the same IPL set,Paraphrased De-C5 reference pattern
De-C5 Tower T-00,C5 and lighter components are stripped from feed by controlled feed flow pressure tower temperature and reboiler duty,Flow,No,1. No Flow,1.5 HV-001 fails closed on T-00 bottom outlet,1.5.1 No outlet flow from T-00 causes level accumulation; hydrocarbon relief through PSV-003A/B can create atmospheric release and pool fire,5,1,R1,1.5.1.1 Same IPL basis as FV-003 no-steam overfill consequence when independent and applicable,Yes,Yes,Yes,1.5.1.S1 Level and pressure alarms,5,3,R2,1.5.1.R1 Verify bottom outlet isolation scenario in the relief and alarm response basis,Paraphrased De-C5 reference pattern
De-C5 Tower T-00,C5 and lighter components are stripped from feed by controlled feed flow pressure tower temperature and reboiler duty,Flow,No,1. No Flow,1.5 HV-001 fails closed on T-00 bottom outlet,1.5.2 Bottom outlet blockage raises pressure and liquid load; skirt failure and hydrocarbon release can lead to pool fire,5,1,R1,1.5.2.1 Tower skirt design for full liquid load (-2),Yes,Yes,Yes,1.5.2.S1 PI-004 PI-011 and PA-005 high pressure alarms,5,4,R3,1.5.2.R1 Confirm tower support load case under blocked outlet condition,Paraphrased De-C5 reference pattern
De-C5 Tower T-00,C5 and lighter components are stripped from feed by controlled feed flow pressure tower temperature and reboiler duty,Flow,No,1. No Flow,1.5 HV-001 fails closed on T-00 bottom outlet,1.5.3 P-06A/B loses suction; pump damage and hydrocarbon leakage may create a localized fire case,3,1,R2,1.5.3.1 FIC-005 low-flow alarm with boardman action (-1),Yes,Yes,Yes,1.5.3.S1 Multiple mechanical pump seal is not credited if not auditable,3,2,R2,1.5.3.R1 Develop PM inspection and seal reliability program for P-06A/B,Paraphrased De-C5 reference pattern
De-C5 Tower T-00,C5 and lighter components are stripped from feed by controlled feed flow pressure tower temperature and reboiler duty,Flow,More,1. More Flow,1.1 FV-001 opens excessively because FIC-001 reads falsely low,1.1.1 High feed raises T-00 liquid inventory; skirt overload and tower collapse may cause hydrocarbon release and pool fire,5,1,R1,1.1.1.1 Same IPL basis as no-flow high-level structural consequence when independent and applicable,Yes,Yes,Yes,1.1.1.S1 Level and pressure alarms,5,4,R3,1.1.1.R1 Check independence before crediting the same IPL set,Paraphrased De-C5 reference pattern
De-C5 Tower T-00,C5 and lighter components are stripped from feed by controlled feed flow pressure tower temperature and reboiler duty,Flow,More,1. More Flow,1.2 FV-005 fails open on bottom circulation line,1.2.1 Minimum-flow circulation increases without credible SHE consequence; no further study is required for this consequence path,1,1,R4,No credited IPL identified,No,No,No,1.2.1.S1 Operator monitoring of circulation flow,1,1,R4,1.2.1.R1 No action required unless operability margin is unacceptable,Paraphrased De-C5 reference pattern
De-C5 Tower T-00,C5 and lighter components are stripped from feed by controlled feed flow pressure tower temperature and reboiler duty,Flow,More,1. More Flow,1.3 FIC-003 reads falsely low and opens FV-003 on steam service,1.3.1 Excess reboiler duty overheats T-00; pressure rises; hydrocarbon release and fire or explosion may occur,5,1,R1,1.3.1.1 PSV-003A/B (-2),Yes,Yes,Yes,1.3.1.S1 High-temperature alarm; 1.3.1.S2 operator monitoring,5,3,R2,1.3.1.R1 Review steam-flow control loop and consider independent high-temperature trip,Paraphrased De-C5 reference pattern
De-C5 Tower T-00,C5 and lighter components are stripped from feed by controlled feed flow pressure tower temperature and reboiler duty,Flow,More,1. More Flow,1.3 FIC-003 reads falsely low and opens FV-003 on steam service,1.3.2 Overboiling can dry out T-00 bottom section; P-06A/B may vibrate from loss of suction; pump leakage and small fire case can result,3,1,R2,1.3.2.1 Same IPL basis as P-06A/B loss-suction consequence when independent and applicable,Yes,Yes,Yes,1.3.2.S1 Pump low-flow alarm and seal monitoring,3,2,R2,1.3.2.R1 Verify pump protection under excessive boil-up condition,Paraphrased De-C5 reference pattern
"""


VECTORDB_PREFLIGHT_RULES = """VECTORDB PREFLIGHT CHECK RULES
Before running HAZOP/LOPA generation in the application layer, call the VectorDB check skill against HAZOP_VECTOR_STORE_ID.
The check must verify that the vector store can retrieve these evidence groups:
1) cause-selection rules;
2) HAZOP workflow;
3) initiating-event likelihood and IPL credit rules;
4) risk ranking matrix;
5) integrated HAZOP/LOPA output template;
6) matched few-shot case evidence for Naphtha Tank or De-C5 Tower where applicable.
If any mandatory evidence group has no retrieved chunk above the score threshold, stop generation and report which knowledge group is missing or weak.
Use the retrieved preflight report as audit evidence for the generation run.
"""

DATA_TAGS_RULE = """INPUT DATA TAGS
Use data inside START-DATA plus retrieved file_search evidence. START-DATA includes both the selected node package and the complete parsed P&ID JSON.

<START-DATA>
Line ID: {line_id}
Node: {node}
Node Boundary: {node_boundary}
From Equipment: {from_equipment}
To Equipment: {to_equipment}
Included Equipment: {included_equipment}
Included Lines: {included_lines}
Valves Local: {valves}
Instruments Local: {instruments}
System Inputs Global: {system_inputs}
System Outputs Global: {system_outputs}
Utility Catalog Global: {utility_lines}
Flow Direction: {flow_direction}
Context: {context}
Process Description: {process_description}
Design Intention: {intention}
Selected Guide Word: {guide_word}
Selected Parameter: {parameter}
Connection Record JSON: {connection_record_json}
Full Parsed P&ID JSON: {full_pid_json}
<END-DATA>
"""

FINAL_TASK = """GENERATION TASK
Generate HAZOP/LOPA rows for the selected Node, Parameter, and Guide Word.
Derive the Deviation field from Guide Word + Parameter, e.g. No/Less Flow, High Pressure, Low Level, or High Temperature.

Internal workflow - do not output:
1) Use file_search to retrieve the applicable guide, cause, IPL, risk, template, and matched case evidence.
2) Parse START-DATA and define the node boundary and design intention.
   - Use the selected node fields first.
   - Use Full Parsed P&ID JSON as complete topology context to resolve missing equipment; valves; instruments; utilities; flow direction; interlocks; safeguards; and node interfaces.
   - If the selected connection is a grouped node; use Node Boundary; Included Equipment; Included Lines; and Connection Record JSON as the controlling node scope.
3) Detect whether the Naphtha Tank or De-C5 Tower few-shot case matches.
4) Generate exactly 5 credible node-local causes for the selected deviation.
5) For each cause, generate exactly 5 credible consequences while ignoring IPLs and safeguards.
6) For every row, assign initial S/L/R, identify credited IPLs and non-IPL safeguards, apply only valid IPL credit, then assign final S/L/R.
7) Before final response, paraphrase every free-text column into Process Safety Engineer specialist style.
8) Validate silently:
   - exactly 25 rows;
   - exactly 20 fields per row;
   - exactly 5 unique causes;
   - exactly 5 consequences under each cause;
   - no raw commas inside free-text fields;
   - no empty critical fields;
   - no unresolved placeholders;
   - risk rankings match the matrix.

Only after validation passes, output the CSV rows.
"""

SUFFIX_TASK = """OUTPUT RULES
- Output ONLY raw CSV data rows.
- No header row.
- No Markdown.
- No explanations.
- Each row must have exactly 20 comma-separated fields.
- Total output must be exactly 25 rows.
- Free-text fields must not contain raw commas; use semicolons instead.
- Multiple IPLs, safeguards, recommendations, or comments must be separated by semicolon plus space inside one field.
- No newline inside any field.
- No curly braces.
"""


def build_HzpRules_Prompt(*, local_knowledge: bool = False) -> str:
    # In local-knowledge mode there is no file_search tool, so the vector-store
    # instructions are swapped out; leaving them in makes the model emit
    # tool-call syntax into the CSV.
    sections = [
        ROLE,
        LOCAL_KNOWLEDGE_RULES if local_knowledge else FILE_SEARCH_RULES,
    ]
    if not local_knowledge:
        sections.append(VECTORDB_PREFLIGHT_RULES)
    sections += [
        TOPOLOGY_MATCH_RULES,
        PARAPHRASE_RULES,
        CSV_SCHEMA_HAZOP_LOPA_20,
        HAZOP_METHOD_RULES,
        CAUSE_GENERATION_RULES,
        CONSEQUENCE_GENERATION_RULES,
        NUMBERING_RULES,
        RISK_RULES,
        IPL_AND_SAFEGUARD_RULES,
        FEW_SHOT_CASE_LIBRARY,
    ]
    return "\n\n".join(section.strip() for section in sections if section.strip())


HzpRules_Prompt = build_HzpRules_Prompt()
HzpRules_Prompt_Local = build_HzpRules_Prompt(local_knowledge=True)


def _clean_prompt_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list, tuple)):
        return str(value)
    return str(value)


def build_file_search_hazop_prompt(**kwargs: Any) -> str:
    data = {
        "line_id": _clean_prompt_value(kwargs.get("line_id", "")),
        "node": _clean_prompt_value(kwargs.get("node", "")),
        "node_boundary": _clean_prompt_value(kwargs.get("node_boundary", "")),
        "from_equipment": _clean_prompt_value(kwargs.get("from_equipment", "")),
        "to_equipment": _clean_prompt_value(kwargs.get("to_equipment", "")),
        "included_equipment": _clean_prompt_value(kwargs.get("included_equipment", "")),
        "included_lines": _clean_prompt_value(kwargs.get("included_lines", "")),
        "valves": _clean_prompt_value(kwargs.get("valves", "")),
        "instruments": _clean_prompt_value(kwargs.get("instruments", "")),
        "system_inputs": _clean_prompt_value(kwargs.get("system_inputs", "")),
        "system_outputs": _clean_prompt_value(kwargs.get("system_outputs", "")),
        "utility_lines": _clean_prompt_value(kwargs.get("utility_lines", "")),
        "flow_direction": _clean_prompt_value(kwargs.get("flow_direction", "")),
        "context": _clean_prompt_value(kwargs.get("context", "")),
        "process_description": _clean_prompt_value(kwargs.get("process_description", "")),
        "intention": _clean_prompt_value(kwargs.get("intention", "")),
        "connection_record_json": _clean_prompt_value(kwargs.get("connection_record_json", "")),
        "full_pid_json": _clean_prompt_value(kwargs.get("full_pid_json", "")),
        "guide_word": _clean_prompt_value(kwargs.get("guide_word", "")),
        "parameter": _clean_prompt_value(kwargs.get("parameter", "")),
    }
    # Retrieved knowledge is appended outside .format() so that braces in the
    # source markdown cannot break prompt formatting.
    knowledge_context = str(kwargs.get("knowledge_context", "") or "").strip()

    rules = HzpRules_Prompt_Local if knowledge_context else HzpRules_Prompt
    data_block = DATA_TAGS_RULE.format(**data).strip()
    final_task = FINAL_TASK.strip()

    if knowledge_context:
        # Redirect the two inline file_search instructions at the supplied knowledge.
        data_block = data_block.replace(
            "plus retrieved file_search evidence",
            "plus the REFERENCE KNOWLEDGE section below",
        )
        final_task = final_task.replace(
            "1) Use file_search to retrieve the applicable guide, cause, IPL, risk, "
            "template, and matched case evidence.",
            "1) Use the REFERENCE KNOWLEDGE section for the applicable guide, cause, "
            "IPL, risk, template, and matched case evidence.",
        )

    parts = [
        rules,
        data_block,
    ]
    if knowledge_context:
        parts.append(
            "REFERENCE KNOWLEDGE (retrieved from the HAZOP skill and standards library).\n"
            "Use it as the basis for causes, consequences, safeguards and recommendations. "
            "If it does not cover something, say so explicitly rather than inventing a basis.\n\n"
            + knowledge_context
        )
    parts.append(final_task)
    parts.append(SUFFIX_TASK.strip())

    return "\n\n".join(parts)


class LegacyPromptAdapter:
    """Small compatibility adapter for old code that called few_shot_prompt.format(**kwargs)."""

    input_variables = [
        "line_id", "node", "node_boundary", "from_equipment", "to_equipment",
        "included_equipment", "included_lines", "valves", "instruments",
        "system_inputs", "system_outputs", "utility_lines", "flow_direction", "context",
        "process_description", "intention", "connection_record_json", "full_pid_json",
        "guide_word", "parameter", "knowledge_context",
    ]

    def format(self, **kwargs: Any) -> str:
        return build_file_search_hazop_prompt(**kwargs)


few_shot_prompt = LegacyPromptAdapter()

# =============================================================================
# VECTORDB CHECK SKILL FOR HAZOP_VECTOR_STORE_ID
# =============================================================================

IMPORTANT_HAZOP_VECTOR_QUERIES: Dict[str, str] = {
    "cause_rules": (
        "Step 4 cause-selection rules from cause.json for HAZOP causes by guide word "
        "and parameter; reject non-credible causes; node-local tagged equipment and instruments"
    ),
    "hazop_workflow": (
        "HAZOP-GUIDE-SKILL workflow steps node boundary design intention guide word parameter "
        "deviation cause consequence safeguard recommendation"
    ),
    "ipl_likelihood": (
        "HAZOP-IPL-LIKELIHOOD HAZOP_LOPA-GUIDE initiating event likelihood frequency band "
        "IPL probability credit independent effective auditable"
    ),
    "risk_matrix": (
        "HAZOP-RISK-LEVEL-GUIDE risk ranking matrix severity likelihood R1 R2 R3 R4 "
        "SCG integrated HAZOP LOPA matrix"
    ),
    "output_template": (
        "HAZOP-OUTPUT-TEMPLATE integrated HAZOP LOPA worksheet output columns Initial Severity "
        "Initial Likelihood IPLs Final Severity Recommendations Comments_Actions"
    ),
    "naphtha_case": (
        "Naphtha Tank 100T-01 transfer pump 100P-01A/B UV-0101 UV-0102 PCV-0101 "
        "PVV-0102 EH0101 LSLL-0102A LSHH-0102A HPU HAZOP worksheet"
    ),
    "dec5_case": (
        "De-C5 Tower T-00 C5 column reboiler E-05 FIC-001 FV-001 FIC-005 FV-005 "
        "FV-003 PIC-002 TIC-012 PSV-003A/B P-06A/B HAZOP worksheet"
    ),
}

MANDATORY_HAZOP_VECTOR_GROUPS: List[str] = [
    "cause_rules",
    "hazop_workflow",
    "ipl_likelihood",
    "risk_matrix",
    "output_template",
]


@dataclass
class VectorDBHit:
    """One retrieved VectorDB chunk used as auditable HAZOP evidence."""

    group: str
    query: str
    filename: str
    file_id: str
    score: float
    text: str


@dataclass
class VectorDBGroupCheck:
    """Retrieval status for one required HAZOP knowledge group."""

    group: str
    query: str
    ok: bool
    best_score: float
    hit_count: int
    hits: List[VectorDBHit]


@dataclass
class VectorDBCheckReport:
    """Complete pre-generation VectorDB check report."""

    vector_store_id: str
    ok: bool
    missing_groups: List[str]
    weak_groups: List[str]
    groups: List[VectorDBGroupCheck]


def _truncate_text(text: str, limit: int = 1200) -> str:
    text = " ".join(str(text or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def _post_openai_json(path: str, payload: Dict[str, Any], api_key: Optional[str] = None) -> Dict[str, Any]:
    """POST JSON to the OpenAI API using only Python stdlib."""

    key = api_key or os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY is not set. Set it in your environment or pass api_key=...")

    req = urllib.request.Request(
        url=f"https://api.openai.com/v1{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI API error {exc.code}: {body}") from exc


def search_hazop_vector_store(
    query: str,
    *,
    vector_store_id: Optional[str] = None,
    api_key: Optional[str] = None,
    max_num_results: int = 8,
    score_threshold: float = 0.10,
    rewrite_query: bool = True,
) -> List[Dict[str, Any]]:
    """Search HAZOP_VECTOR_STORE_ID and return raw Vector Store chunks.

    This uses the OpenAI Vector Store Search endpoint directly:
    POST /v1/vector_stores/{vector_store_id}/search
    """

    vs_id = vector_store_id or os.getenv("HAZOP_VECTOR_STORE_ID")
    if not vs_id:
        raise ValueError("HAZOP_VECTOR_STORE_ID is not set. Set it in your environment or pass vector_store_id=...")

    payload: Dict[str, Any] = {
        "query": query,
        "max_num_results": max(1, min(int(max_num_results), 50)),
        "rewrite_query": rewrite_query,
        "ranking_options": {
            "ranker": "auto",
            "score_threshold": score_threshold,
        },
    }
    result = _post_openai_json(f"/vector_stores/{vs_id}/search", payload, api_key=api_key)
    return list(result.get("data", []))


def _hit_from_raw(group: str, query: str, raw: Dict[str, Any]) -> VectorDBHit:
    content = raw.get("content") or []
    text_parts = []
    for item in content:
        if isinstance(item, dict):
            text_parts.append(item.get("text", ""))
    return VectorDBHit(
        group=group,
        query=query,
        filename=str(raw.get("filename", "")),
        file_id=str(raw.get("file_id", "")),
        score=float(raw.get("score", 0.0) or 0.0),
        text=_truncate_text("\n".join(text_parts), 1200),
    )


def check_hazop_vector_store(
    *,
    vector_store_id: Optional[str] = None,
    api_key: Optional[str] = None,
    node_context: str = "",
    selected_parameter: str = "",
    selected_guide_word: str = "",
    score_threshold: float = 0.10,
    max_num_results: int = 8,
    include_case_examples: bool = True,
) -> VectorDBCheckReport:
    """Check whether HAZOP_VECTOR_STORE_ID contains the important data required for generation.

    Use this before calling the HAZOP generator. Mandatory groups must be retrievable:
    cause rules, HAZOP workflow, IPL/likelihood, risk matrix, and output template.
    Case examples are checked when include_case_examples=True, but they are not mandatory.
    """

    vs_id = vector_store_id or os.getenv("HAZOP_VECTOR_STORE_ID")
    if not vs_id:
        raise ValueError("HAZOP_VECTOR_STORE_ID is not set. Set it in your environment or pass vector_store_id=...")

    queries = dict(IMPORTANT_HAZOP_VECTOR_QUERIES)
    if not include_case_examples:
        queries.pop("naphtha_case", None)
        queries.pop("dec5_case", None)

    context_suffix = " ".join(
        part for part in [node_context, selected_parameter, selected_guide_word] if part
    ).strip()

    group_checks: List[VectorDBGroupCheck] = []
    missing_groups: List[str] = []
    weak_groups: List[str] = []

    for group, base_query in queries.items():
        query = f"{base_query} {context_suffix}".strip()
        raw_hits = search_hazop_vector_store(
            query,
            vector_store_id=vs_id,
            api_key=api_key,
            max_num_results=max_num_results,
            score_threshold=score_threshold,
            rewrite_query=True,
        )
        hits = [_hit_from_raw(group, query, raw) for raw in raw_hits]
        best_score = max((h.score for h in hits), default=0.0)
        ok = len(hits) > 0 and best_score >= score_threshold

        if group in MANDATORY_HAZOP_VECTOR_GROUPS and not hits:
            missing_groups.append(group)
        elif group in MANDATORY_HAZOP_VECTOR_GROUPS and not ok:
            weak_groups.append(group)

        group_checks.append(
            VectorDBGroupCheck(
                group=group,
                query=query,
                ok=ok,
                best_score=best_score,
                hit_count=len(hits),
                hits=hits,
            )
        )

    return VectorDBCheckReport(
        vector_store_id=vs_id,
        ok=not missing_groups and not weak_groups,
        missing_groups=missing_groups,
        weak_groups=weak_groups,
        groups=group_checks,
    )


def vector_db_report_to_dict(report: VectorDBCheckReport) -> Dict[str, Any]:
    """Convert the VectorDB check report to a JSON-serializable dictionary."""

    return asdict(report)


def format_vector_db_check_report(report: VectorDBCheckReport, *, include_chunks: bool = True) -> str:
    """Return a human-readable audit report for debugging and generation logs."""

    lines: List[str] = []
    lines.append(f"Vector Store ID: {report.vector_store_id}")
    lines.append(f"Overall status: {'PASS' if report.ok else 'FAIL'}")
    if report.missing_groups:
        lines.append(f"Missing mandatory groups: {', '.join(report.missing_groups)}")
    if report.weak_groups:
        lines.append(f"Weak mandatory groups: {', '.join(report.weak_groups)}")

    for group in report.groups:
        lines.append("")
        lines.append(
            f"[{group.group}] {'OK' if group.ok else 'NOT OK'} | "
            f"hits={group.hit_count} | best_score={group.best_score:.3f}"
        )
        lines.append(f"Query: {group.query}")
        if include_chunks:
            for i, hit in enumerate(group.hits[:3], start=1):
                lines.append(f"  {i}. {hit.filename} | score={hit.score:.3f} | file_id={hit.file_id}")
                lines.append(f"     {hit.text}")

    return "\n".join(lines)


def assert_hazop_vector_store_ready(**kwargs: Any) -> VectorDBCheckReport:
    """Raise an error if mandatory HAZOP evidence is missing before generation."""

    report = check_hazop_vector_store(**kwargs)
    if not report.ok:
        raise RuntimeError(
            "HAZOP vector store is not ready.\n"
            + format_vector_db_check_report(report, include_chunks=False)
        )
    return report


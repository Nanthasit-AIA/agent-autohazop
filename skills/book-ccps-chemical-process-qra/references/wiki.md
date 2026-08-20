# CCPS Chemical Process Quantitative Risk Analysis - Book Wiki

## Source Card

- Source slug: `ccps-chemical-process-qra`
- Domain: `qra`
- Primary topic wiki: `risk-criteria-qra`
- Primary procedural skill: `risk-criteria-qra`
- Secondary skills: `relief-effluent-fire-explosion-consequence`
- Tags: `qra`, `event-tree`, `fault-tree`, `frequency`, `consequence`, `risk-integration`
- Pages: 632
- Usable text pages in current extraction: 625
- Indexed topic hits: 3128
- Top signals: QRA/risk criteria:932, Consequence analysis:672, Fire/explosion:479, Reliability data:452, Incident/human factors:244
- Source quality: text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-chemical-process-qra/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source to discipline quantitative risk assumptions and risk-criteria decisions.

## Decisions This Source Can Support

- Whether frequency, consequence, vulnerability, occupancy, and ignition/exposure assumptions are explicit.
- Whether the selected risk metric and tolerability criterion are project-approved.
- Whether uncertainty and sensitivity are visible enough for decision making.

## Source-Derived Playbook

- Separate qualitative screening from quantitative claims and identify the missing numeric basis.
- Challenge event-tree/fault-tree branches for dependence, enabling conditions, and double counting.
- State whether the output is a screening recommendation, a calculation input request, or a blocked decision.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| QRA/risk criteria | 932 | 1, 5-10, 12, 14, 16, 19, 21-24, 26, 28-38, 41, 43-47, 50-82, 84-89, 92-99, ... | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Consequence analysis | 672 | 6, 9-12, 15, 19, 23-35, 37-38, 45-47, 50, 52, 58-59, 65, 67-72, 74-75, 86, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Fire/explosion | 479 | 10, 25, 27-28, 30, 32-33, 35-36, 45-47, 50, 52, 59, 63, 65, 69, 71-72, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Reliability data | 452 | 6, 10-11, 16, 19, 23, 25-27, 30-31, 33-37, 50, 67, 77, 79-80, 230, 232-233, ... | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| Incident/human factors | 244 | 25-27, 32-34, 38, 79, 96, 98, 148, 166, 206, 216, 221-223, 229, 231, 235-236, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Relief/effluent | 131 | 15, 33-34, 36, 46, 64, 106-109, 113-114, 145, 147, 149, 151-154, 156, 160-161, 164-165, ... | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| HAZOP/PHA | 52 | 6, 15-16, 26-27, 31, 34, 44, 51-52, 63, 81, 86, 93, 96-97, 197, 236, ... | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Inherent safety/siting | 41 | 11, 15, 50-51, 62, 74, 104, 181, 201, 206, 221, 238, 260, 342-343, 347, ... | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| LOPA/IPL | 38 | 32, 34-36, 46, 52, 63, 92, 254, 256-260, 297, 567, 625 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| PSM/MOC/documentation | 38 | 51, 78, 85, 87, 92-93, 95-97, 192, 200, 244, 303, 347, 383, 395-396, 400, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| SIS/SIL | 31 | 23, 36, 143, 267, 270, 278, 300, 304, 409, 416-418, 420-421, 434, 437-438, 482, ... | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| Security review | 15 | 33, 165, 175, 207, 231, 280, 291, 293, 295, 450, 497, 500, 504, 518 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |
| Alarm management | 3 | 234-235, 238 | Challenge alarm rationalization, priority, response time, standing/flood alarms, operator action, and IPL claims. |

## HAZOP Injection Pattern

When this wiki is selected for a HAZOP row:

1. State the matched source signal and confidence tier.
2. Restate the node/deviation/design-intent context from project data.
3. Improve the cause so it names the failed item, failure mode, human/organizational condition, external event, or initiating event.
4. Improve the consequence as an unmitigated event path before safeguards.
5. Test safeguards for independence, timing, auditability, and effectiveness before giving credit.
6. Recommend action only for a real gap: missing design basis, calculation, weak safeguard, missing procedure, missing inspection/test, missing MOC, missing training, or missing documentation.
7. Mark blocked decisions explicitly when project-specific criteria or data are absent.

## Missing-Basis Checklist

- [ ] Project risk criteria
- [ ] Frequency data source
- [ ] Consequence model/endpoints
- [ ] Occupancy, ignition, vulnerability, and exposure basis
- [ ] Sensitivity/uncertainty treatment
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `ccps-chemical-process-qra`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-chemical-process-qra qra event-tree fault-tree frequency consequence risk-integration HAZOP cause consequence safeguard recommendation`
- `ccps-chemical-process-qra QRA/risk criteria Consequence analysis Fire/explosion Reliability data missing basis project criteria data assumptions`
- `ccps-chemical-process-qra AutoHAZOP node deviation scenario review quality gate`
- `ccps-chemical-process-qra evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `risk-criteria-qra` and secondary skills `relief-effluent-fire-explosion-consequence` when the decision requires a specialist workflow.

# The Alarm Management Handbook - Book Wiki

## Source Card

- Source slug: `alarm-management-handbook`
- Domain: `alarm_management`
- Primary topic wiki: `alarm-management`
- Primary procedural skill: `alarm-management-rationalization`
- Secondary skills: none
- Tags: `alarm-management`, `operator-response`, `rationalization`, `standing-alarms`, `alarm-flood`
- Pages: 275
- Usable text pages in current extraction: 274
- Indexed topic hits: 449
- Top signals: Alarm management:176, PSM/MOC/documentation:152, HAZOP/PHA:28, Consequence analysis:24, SIS/SIL:23
- Source quality: text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-alarm-management-handbook/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Treat alarms as engineered operator-support functions, not generic safeguards.

## Decisions This Source Can Support

- Whether an alarm is only awareness, an operator response safeguard, or a candidate IPL.
- Whether priority, setpoint, response time, standing/flood behavior, and operator action are documented.
- Whether alarm changes require rationalization, shelving/bypass controls, proof of response, or MOC.

## Source-Derived Playbook

- Check detectability, diagnosis time, action time, and consequence arrival time before crediting an alarm.
- Challenge any alarm credited as an IPL for independence from the initiating event and BPCS failure.
- Convert weak alarm recommendations into rationalization, response-procedure, training, testing, or nuisance-alarm actions.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| Alarm management | 176 | 3, 8-13, 15, 19-22, 24-28, 34-39, 42, 44-45, 47-48, 51-52, 54, 58-59, 62-63, 65-66, ... | Challenge alarm rationalization, priority, response time, standing/flood alarms, operator action, and IPL claims. |
| PSM/MOC/documentation | 152 | 8, 11, 13, 15, 26-28, 33, 35, 41-42, 45, 47, 53-54, 70, 74, 76, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| HAZOP/PHA | 28 | 11, 55, 71, 83, 94, 100, 120, 145-147, 150-151, 157, 160, 169, 192, 202, ... | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Consequence analysis | 24 | 63-64, 100, 115, 148, 152, 156, 169, 231, 242, 249, 273, 275 | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| SIS/SIL | 23 | 11, 38, 40, 145, 151, 157-158, 169, 202, 231-232, 275 | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| Incident/human factors | 14 | 34, 124, 139-140, 174, 190, 215-217, 262, 264, 272-274 | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| LOPA/IPL | 9 | 145, 147, 150-151, 169, 209, 227, 274 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| Fire/explosion | 9 | 34-36, 64, 153, 215, 270 | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Relief/effluent | 8 | 151-152 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Security review | 3 | 61, 122, 155 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |
| Inherent safety/siting | 2 | 253, 260 | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| Reliability data | 1 | 190 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |

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

- [ ] Alarm philosophy/rationalization record
- [ ] Setpoint and priority basis
- [ ] Operator response time and action verification
- [ ] Standing/flood alarm data
- [ ] Bypass/shelving controls and MOC
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `alarm-management-handbook`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `alarm-management-handbook alarm-management operator-response rationalization standing-alarms alarm-flood HAZOP cause consequence safeguard recommendation`
- `alarm-management-handbook Alarm management PSM/MOC/documentation HAZOP/PHA Consequence analysis missing basis project criteria data assumptions`
- `alarm-management-handbook AutoHAZOP node deviation scenario review quality gate`
- `alarm-management-handbook evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `alarm-management-rationalization` and secondary skills none when the decision requires a specialist workflow.

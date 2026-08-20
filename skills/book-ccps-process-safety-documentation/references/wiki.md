# CCPS Process Safety Documentation - Book Wiki

## Source Card

- Source slug: `ccps-process-safety-documentation`
- Domain: `psm_documentation`
- Primary topic wiki: `psm-rbps-moc-documentation`
- Primary procedural skill: `process-safety-management-rbps-moc-docs`
- Secondary skills: none
- Tags: `documentation`, `records`, `process-knowledge`, `pha`, `audit`, `moc`
- Pages: 418
- Usable text pages in current extraction: 417
- Indexed topic hits: 2240
- Top signals: PSM/MOC/documentation:1361, HAZOP/PHA:303, Incident/human factors:251, QRA/risk criteria:95, Consequence analysis:93
- Source quality: outline/bookmark count: 452; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-process-safety-documentation/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source to turn technical gaps into auditable process-safety management actions.

## Decisions This Source Can Support

- Whether the gap is PSI, procedure, training, MOC, PSSR, mechanical integrity, emergency management, audit, or action tracking.
- Whether a recommendation names an accountable management-system deliverable.
- Whether documentation is sufficient to support later HAZOP/LOPA/SIS decisions.

## Source-Derived Playbook

- Translate vague 'review/update' actions into specific records, owners, acceptance criteria, and verification evidence.
- Flag MOC/PSSR needs when design, procedure, alarm, interlock, relief, operating envelope, or equipment service changes.
- Keep technical and management-system recommendations linked to the scenario that created the need.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| PSM/MOC/documentation | 1361 | 2-5, 8-9, 12-36, 38-45, 47-52, 54-60, 62, 64-67, 70-73, 79, 81-84, 86-87, 92, 94-96, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| HAZOP/PHA | 303 | 7, 9-10, 12, 16, 30, 33, 38, 40-41, 56, 84, 94, 96, 100-113, 115, ... | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Incident/human factors | 251 | 6-7, 9, 11-12, 18-19, 23-24, 30, 32, 39, 48-49, 54, 57-58, 101-103, 106, 115, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| QRA/risk criteria | 95 | 7-8, 11, 16-17, 56, 105, 115, 117, 119-120, 122-124, 134-135, 138, 141-143, 146, 148, ... | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Consequence analysis | 93 | 6, 8-11, 16, 39, 73-74, 76, 78-79, 86, 91, 97, 110, 114, 120-121, 135-137, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Fire/explosion | 70 | 6-8, 10-11, 15, 39, 56-57, 62-63, 66, 68, 76, 84, 91, 96-97, 105, 110, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Relief/effluent | 22 | 71, 84, 90-91, 93, 132, 136, 145, 157, 175-177, 186 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Reliability data | 14 | 6, 115, 117, 119, 140-141, 144-145, 158, 198, 342 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| Inherent safety/siting | 14 | 56, 106, 129, 136, 141, 144, 164, 168, 284, 388, 405 | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| SIS/SIL | 10 | 9, 338-339 | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| Security review | 6 | 240, 256, 384 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |
| Alarm management | 1 | 342 | Challenge alarm rationalization, priority, response time, standing/flood alarms, operator action, and IPL claims. |

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

- [ ] Process safety information
- [ ] Operating procedure/training record
- [ ] MOC/PSSR evidence
- [ ] Inspection/test/maintenance record
- [ ] Audit/action-tracking closure evidence
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `ccps-process-safety-documentation`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-process-safety-documentation documentation records process-knowledge pha audit moc HAZOP cause consequence safeguard recommendation`
- `ccps-process-safety-documentation PSM/MOC/documentation HAZOP/PHA Incident/human factors QRA/risk criteria missing basis project criteria data assumptions`
- `ccps-process-safety-documentation AutoHAZOP node deviation scenario review quality gate`
- `ccps-process-safety-documentation evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `process-safety-management-rbps-moc-docs` and secondary skills none when the decision requires a specialist workflow.

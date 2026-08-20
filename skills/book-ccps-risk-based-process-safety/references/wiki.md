# CCPS Guidelines for Risk Based Process Safety - Book Wiki

## Source Card

- Source slug: `ccps-risk-based-process-safety`
- Domain: `rbps`
- Primary topic wiki: `psm-rbps-moc-documentation`
- Primary procedural skill: `process-safety-management-rbps-moc-docs`
- Secondary skills: none
- Tags: `rbps`, `psm`, `process-safety-culture`, `management-system`, `risk-based`
- Pages: 708
- Usable text pages in current extraction: 708
- Indexed topic hits: 2462
- Top signals: PSM/MOC/documentation:1794, Incident/human factors:352, Fire/explosion:65, HAZOP/PHA:57, Consequence analysis:57
- Source quality: outline/bookmark count: 29; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-risk-based-process-safety/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| PSM/MOC/documentation | 1794 | 3-7, 9-18, 20-31, 33, 35-37, 39, 41, 43, 45, 47, 49, 51-63, 65-85, 88, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| Incident/human factors | 352 | 5, 7-11, 13-14, 16-18, 23-26, 47-48, 52, 54-55, 57-59, 63, 69-74, 79-80, 84, 87, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Fire/explosion | 65 | 8-9, 15, 87, 89, 115, 119, 134, 180-181, 187, 200, 217, 219-220, 243, 255, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| HAZOP/PHA | 57 | 7, 9, 11, 18, 92, 150, 190, 192, 195, 202, 213, 220-221, 240, 245-246, ... | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Consequence analysis | 57 | 14, 76, 119, 135, 187, 189, 233, 245, 264, 285, 296, 310, 334, 338, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| SIS/SIL | 30 | 10, 334-335, 350, 365, 372, 706-707 | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| Inherent safety/siting | 28 | 14, 26, 66, 224-225, 228-229, 233, 237-238, 241, 243, 248-249, 252, 440, 547, 656, ... | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| LOPA/IPL | 23 | 9, 14-15, 220, 229, 241, 252, 363, 581, 700-701 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| QRA/risk criteria | 21 | 17, 68, 220, 222, 229, 231, 234-235, 249, 252, 520, 581, 656, 697, 705 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Relief/effluent | 13 | 110, 187, 193, 225, 264, 332, 336-337, 474, 483, 581 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Security review | 12 | 275, 485, 515, 521-522, 533, 547-548 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |
| Reliability data | 7 | 194-195, 355, 364, 367, 599 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| Alarm management | 3 | 527, 540 | Challenge alarm rationalization, priority, response time, standing/flood alarms, operator action, and IPL claims. |

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
- Basis: `ccps-risk-based-process-safety`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-risk-based-process-safety rbps psm process-safety-culture management-system risk-based HAZOP cause consequence safeguard recommendation`
- `ccps-risk-based-process-safety PSM/MOC/documentation Incident/human factors Fire/explosion HAZOP/PHA missing basis project criteria data assumptions`
- `ccps-risk-based-process-safety AutoHAZOP node deviation scenario review quality gate`
- `ccps-risk-based-process-safety evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `process-safety-management-rbps-moc-docs` and secondary skills none when the decision requires a specialist workflow.

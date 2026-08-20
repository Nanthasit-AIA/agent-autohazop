# Lees' Loss Prevention in the Process Industries - Book Wiki

## Source Card

- Source slug: `lees-loss-prevention`
- Domain: `loss_prevention`
- Primary topic wiki: `loss-prevention-master-reference`
- Primary procedural skill: `hazop-hazan-study-leader`
- Secondary skills: `relief-effluent-fire-explosion-consequence`, `risk-criteria-qra`
- Tags: `loss-prevention`, `hazard-identification`, `risk-assessment`, `control`, `reference`
- Pages: 1468
- Usable text pages in current extraction: 1465
- Indexed topic hits: 7391
- Top signals: Consequence analysis:2397, Fire/explosion:1122, Incident/human factors:975, Relief/effluent:971, Inherent safety/siting:460
- Source quality: text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-lees-loss-prevention/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source as a routing and integration layer across hazard identification, assessment, and control.

## Decisions This Source Can Support

- Which specialist discipline should own the next check: HAZOP, LOPA/SIS, relief, QRA, reliability, PSM, incident learning, or siting.
- Whether a broad loss-prevention claim needs a narrower source before it can support a decision.
- Whether recommendations are balanced across prevention, protection, mitigation, emergency response, and management systems.

## Source-Derived Playbook

- Use broad coverage to identify missing specialist checks, not to overrule specialist data.
- Route quantitative or design-specific claims to the narrower skill/wiki before accepting them.
- Keep the final recommendation tied to the current node, deviation, cause, consequence, and evidence gap.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| Consequence analysis | 2397 | 9-11, 13, 15-16, 25, 27-32, 42-43, 47, 55, 59-65, 67, 71-72, 81-85, 88, 94, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Fire/explosion | 1122 | 10, 13, 15-16, 21, 25, 27, 29-30, 32, 35-37, 40, 42-43, 47, 53-55, 63-68, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Incident/human factors | 975 | 9-11, 13, 15-17, 19, 25-28, 32-33, 37-38, 42-43, 45, 47-49, 55-64, 68, 74, 78, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Relief/effluent | 971 | 9-10, 13, 16, 27-28, 30-31, 33, 42, 45, 64-65, 70-73, 84, 129, 145-146, 158, ... | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Inherent safety/siting | 460 | 9-10, 13, 16, 26-27, 31, 33, 37, 45-47, 59, 72-73, 101-103, 121-123, 129, 132, ... | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| QRA/risk criteria | 427 | 13, 26, 33, 37, 47, 55-56, 90-92, 97-98, 101, 105, 114, 116-118, 123, 125, ... | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| HAZOP/PHA | 332 | 26, 136, 143, 147, 151, 153, 177, 192, 202, 212, 224, 229-231, 233-236, 243, ... | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Reliability data | 275 | 163, 170-172, 178-181, 187-190, 192-193, 195, 197, 199-200, 205-208, 210, 212, 218-219, 221-223, 227-230, ... | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| PSM/MOC/documentation | 236 | 9-11, 16, 25, 37-38, 41, 43, 47, 49-50, 61, 82-83, 85, 116-118, 130, 139-147, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| SIS/SIL | 128 | 9-10, 19, 23, 33, 62, 75, 192, 237, 242, 327, 339, 346, 350-351, 401, ... | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| Security review | 38 | 17, 34, 40, 70, 88, 158, 280, 291, 314, 324, 360-362, 425, 448, 531, ... | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |
| LOPA/IPL | 26 | 9, 55, 61, 347, 426, 428, 595, 599, 708-710, 760, 764, 769 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| Alarm management | 4 | 732, 771 | Challenge alarm rationalization, priority, response time, standing/flood alarms, operator action, and IPL claims. |

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

- [ ] Specialist discipline owner
- [ ] Narrower source or calculation basis
- [ ] Project standard/criterion
- [ ] Scenario-specific evidence
- [ ] Verification and closure plan
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `lees-loss-prevention`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `lees-loss-prevention loss-prevention hazard-identification risk-assessment control reference HAZOP cause consequence safeguard recommendation`
- `lees-loss-prevention Consequence analysis Fire/explosion Incident/human factors Relief/effluent missing basis project criteria data assumptions`
- `lees-loss-prevention AutoHAZOP node deviation scenario review quality gate`
- `lees-loss-prevention evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `hazop-hazan-study-leader` and secondary skills `relief-effluent-fire-explosion-consequence`, `risk-criteria-qra` when the decision requires a specialist workflow.

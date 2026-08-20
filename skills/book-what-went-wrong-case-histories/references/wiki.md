# What Went Wrong - Case Histories - Book Wiki

## Source Card

- Source slug: `what-went-wrong-case-histories`
- Domain: `incident_learning`
- Primary topic wiki: `incident-learning-and-human-factors`
- Primary procedural skill: `incident-learning-root-cause-human-error`
- Secondary skills: none
- Tags: `case-history`, `incident-learning`, `maintenance`, `management-system`, `inherent-safety`
- Pages: 742
- Usable text pages in current extraction: 742
- Indexed topic hits: 2066
- Top signals: Fire/explosion:617, Incident/human factors:465, Consequence analysis:342, Relief/effluent:226, Inherent safety/siting:133
- Source quality: outline/bookmark count: 816; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-what-went-wrong-case-histories/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source to improve causal reasoning, human factors, and learning from prior incidents.

## Decisions This Source Can Support

- Whether a cause is a direct technical failure, human action, latent organizational weakness, or degraded barrier.
- Whether a recommendation changes the system rather than only reminding people to be careful.
- Whether repeat-event learning, design-for-error, maintenance, procedure, or supervision gaps are visible.

## Source-Derived Playbook

- Challenge blame-only wording and look for design, procedure, interface, maintenance, training, workload, and management-system contributors.
- Convert lessons into engineered, procedural, and audit-backed actions.
- Use incident patterns to ask better questions, not to assert plant-specific facts without evidence.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| Fire/explosion | 617 | 10, 18, 21, 23, 30-31, 41, 45, 47-50, 55-57, 60, 62-63, 69-73, 75, 83, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Incident/human factors | 465 | 6, 9-11, 14, 20, 22-24, 26-28, 31-33, 35-44, 47, 50, 57-58, 77, 86, 89, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Consequence analysis | 342 | 9, 12, 36, 53, 56-57, 68-72, 77-78, 82, 93, 95, 103-105, 111, 118, 126-127, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Relief/effluent | 226 | 18, 23, 29, 37, 48, 56, 59-60, 68-69, 87-88, 118, 124, 167, 169, 180-181, ... | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Inherent safety/siting | 133 | 7, 10, 21, 23, 26, 31, 33, 35, 38, 42-44, 50, 131, 176, 179, ... | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| HAZOP/PHA | 131 | 8, 24-25, 41-42, 276, 278, 321, 341, 425, 437, 442, 445, 466-467, 478, 497, ... | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| PSM/MOC/documentation | 105 | 10, 13, 21-28, 31, 33, 42, 44, 46-47, 50, 94, 97, 103, 118, 128, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| Reliability data | 13 | 205, 219, 280, 291, 337, 339, 575, 683, 698 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| QRA/risk criteria | 11 | 400, 535, 558, 669, 702, 707, 710 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| LOPA/IPL | 9 | 282, 383, 514, 535, 558, 572, 662 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| Security review | 8 | 266, 318-319, 559-560, 720 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |
| SIS/SIL | 5 | 37, 425, 686, 698, 700 | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| Alarm management | 1 | 692 | Challenge alarm rationalization, priority, response time, standing/flood alarms, operator action, and IPL claims. |

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

- [ ] Incident evidence and timeline
- [ ] Barrier failure analysis
- [ ] Human factors/task analysis
- [ ] Management-system causal evidence
- [ ] Action effectiveness verification
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `what-went-wrong-case-histories`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `what-went-wrong-case-histories case-history incident-learning maintenance management-system inherent-safety HAZOP cause consequence safeguard recommendation`
- `what-went-wrong-case-histories Fire/explosion Incident/human factors Consequence analysis Relief/effluent missing basis project criteria data assumptions`
- `what-went-wrong-case-histories AutoHAZOP node deviation scenario review quality gate`
- `what-went-wrong-case-histories evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `incident-learning-root-cause-human-error` and secondary skills none when the decision requires a specialist workflow.

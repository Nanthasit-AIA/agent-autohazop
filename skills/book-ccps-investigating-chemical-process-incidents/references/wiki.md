# CCPS Guidelines for Investigating Chemical Process Incidents - Book Wiki

## Source Card

- Source slug: `ccps-investigating-chemical-process-incidents`
- Domain: `incident_investigation`
- Primary topic wiki: `incident-learning-and-human-factors`
- Primary procedural skill: `incident-learning-root-cause-human-error`
- Secondary skills: none
- Tags: `incident-investigation`, `root-cause`, `evidence`, `recommendation`, `learning`
- Pages: 455
- Usable text pages in current extraction: 455
- Indexed topic hits: 1406
- Top signals: Incident/human factors:891, PSM/MOC/documentation:158, Fire/explosion:97, QRA/risk criteria:63, HAZOP/PHA:48
- Source quality: text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-investigating-chemical-process-incidents/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| Incident/human factors | 891 | 3-6, 8, 10, 12-19, 21-56, 58-63, 65-66, 68-80, 82-84, 87-88, 90-94, 96, 98-104, 106, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| PSM/MOC/documentation | 158 | 3, 8-10, 16-17, 24-25, 27, 31-32, 35, 39, 43-44, 46, 49-52, 54, 58, 62, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| Fire/explosion | 97 | 7-9, 14, 18, 38, 117, 123-124, 133-134, 137, 140, 143, 149, 153, 155, 158, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| QRA/risk criteria | 63 | 7-8, 14, 53, 62, 65, 69, 71-73, 77, 199, 214, 216, 234, 243, 249, ... | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| HAZOP/PHA | 48 | 8-9, 53-54, 60, 65-66, 69, 73, 75, 190, 216, 229, 234, 261, 263, 279, ... | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Relief/effluent | 36 | 9, 38, 83-85, 88, 99, 141-142, 153, 181, 183, 185, 200, 271, 321-322, 353, ... | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Consequence analysis | 29 | 18, 85, 124, 135, 141, 160, 189, 209, 231, 234, 273, 352, 377-378, 381, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Inherent safety/siting | 26 | 15, 80, 96, 109, 112, 206, 265, 269-270, 274, 279-280, 286, 348, 450, 452, ... | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| Reliability data | 20 | 7-8, 65, 76, 190, 204, 213, 224, 243, 264, 270, 333, 341, 363, 432, ... | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| LOPA/IPL | 16 | 8, 57, 268, 326, 334, 438, 440-441, 443 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| Security review | 12 | 81-82, 97-98, 146-147, 155, 273, 303, 306, 353 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |
| SIS/SIL | 10 | 9, 77, 127, 243, 247, 305, 386 | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |

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
- Basis: `ccps-investigating-chemical-process-incidents`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-investigating-chemical-process-incidents incident-investigation root-cause evidence recommendation learning HAZOP cause consequence safeguard recommendation`
- `ccps-investigating-chemical-process-incidents Incident/human factors PSM/MOC/documentation Fire/explosion QRA/risk criteria missing basis project criteria data assumptions`
- `ccps-investigating-chemical-process-incidents AutoHAZOP node deviation scenario review quality gate`
- `ccps-investigating-chemical-process-incidents evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `incident-learning-root-cause-human-error` and secondary skills none when the decision requires a specialist workflow.

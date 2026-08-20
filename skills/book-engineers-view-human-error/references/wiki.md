# An Engineer's View of Human Error - Book Wiki

## Source Card

- Source slug: `engineers-view-human-error`
- Domain: `human_factors`
- Primary topic wiki: `incident-learning-and-human-factors`
- Primary procedural skill: `incident-learning-root-cause-human-error`
- Secondary skills: none
- Tags: `human-error`, `human-factors`, `design-for-error`, `procedure`, `maintenance`
- Pages: 293
- Usable text pages in current extraction: 293
- Indexed topic hits: 604
- Top signals: Incident/human factors:418, Fire/explosion:43, Inherent safety/siting:32, HAZOP/PHA:28, Relief/effluent:26
- Source quality: text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-engineers-view-human-error/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| Incident/human factors | 418 | 1-2, 4-6, 8-9, 11-16, 18, 20-22, 24, 26-29, 32-34, 36, 38-42, 44, 46-53, 55-59, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Fire/explosion | 43 | 42, 44, 59, 66, 73, 76, 78, 83, 92, 102, 107, 112, 116, 121, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Inherent safety/siting | 32 | 5, 20, 39, 47-50, 64, 79, 81, 87, 91-92, 96, 127, 133, 159, 163, ... | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| HAZOP/PHA | 28 | 20, 73-74, 107, 164, 167, 172, 175, 177-178, 218-219, 221-222, 225, 244, 274, 288 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Relief/effluent | 26 | 32-33, 57, 63, 65, 67, 69-70, 103, 117, 147, 168, 171, 202, 219, 237, ... | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Consequence analysis | 23 | 32, 40, 72, 77, 125-128, 133, 138, 164, 183, 198, 200, 202-203, 206, 227, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Reliability data | 22 | 28, 143-144, 152, 154-155, 160, 162-163, 215 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| QRA/risk criteria | 6 | 144-145, 147-148, 164, 244 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| PSM/MOC/documentation | 4 | 130, 141, 167 | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| Security review | 2 | 49 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |

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
- Basis: `engineers-view-human-error`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `engineers-view-human-error human-error human-factors design-for-error procedure maintenance HAZOP cause consequence safeguard recommendation`
- `engineers-view-human-error Incident/human factors Fire/explosion Inherent safety/siting HAZOP/PHA missing basis project criteria data assumptions`
- `engineers-view-human-error AutoHAZOP node deviation scenario review quality gate`
- `engineers-view-human-error evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `incident-learning-root-cause-human-error` and secondary skills none when the decision requires a specialist workflow.

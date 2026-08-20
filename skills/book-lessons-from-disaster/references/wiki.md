# Lessons from Disaster - Book Wiki

## Source Card

- Source slug: `lessons-from-disaster`
- Domain: `incident_learning`
- Primary topic wiki: `incident-learning-and-human-factors`
- Primary procedural skill: `incident-learning-root-cause-human-error`
- Secondary skills: none
- Tags: `organizational-memory`, `recurring-accidents`, `incident-learning`, `management-system`
- Pages: 192
- Usable text pages in current extraction: 192
- Indexed topic hits: 426
- Top signals: Incident/human factors:184, Fire/explosion:98, Consequence analysis:43, HAZOP/PHA:31, Relief/effluent:22
- Source quality: text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-lessons-from-disaster/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| Incident/human factors | 184 | 3, 6, 9, 11, 13-15, 21, 23, 26, 29-31, 39-40, 44, 50, 64-65, 67, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Fire/explosion | 98 | 5, 12-13, 15, 17, 19-22, 28-30, 32-34, 39, 49-50, 53-54, 57-58, 60-62, 67-68, 84-85, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Consequence analysis | 43 | 12-13, 19-20, 22, 38-39, 49, 53, 62, 64, 85, 91, 93-94, 106-107, 112, 115-116, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| HAZOP/PHA | 31 | 44, 90, 98, 110-112, 126, 136, 138, 150, 166, 172, 186 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Relief/effluent | 22 | 17-19, 36, 49, 62, 84-87, 100, 107, 109, 147, 157, 165, 186 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Inherent safety/siting | 20 | 6, 17, 91-93, 95, 98, 167-168, 171, 184-185, 187 | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| PSM/MOC/documentation | 11 | 104, 107-108, 126, 138, 169, 188 | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| QRA/risk criteria | 9 | 98, 111-112, 126, 186, 190 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Reliability data | 8 | 38, 82-83, 109, 112-113, 186 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |

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
- Basis: `lessons-from-disaster`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `lessons-from-disaster organizational-memory recurring-accidents incident-learning management-system HAZOP cause consequence safeguard recommendation`
- `lessons-from-disaster Incident/human factors Fire/explosion Consequence analysis HAZOP/PHA missing basis project criteria data assumptions`
- `lessons-from-disaster AutoHAZOP node deviation scenario review quality gate`
- `lessons-from-disaster evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `incident-learning-root-cause-human-error` and secondary skills none when the decision requires a specialist workflow.

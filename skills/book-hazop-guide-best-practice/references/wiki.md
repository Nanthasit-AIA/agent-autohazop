# HAZOP Guide to Best Practice - Book Wiki

## Source Card

- Source slug: `hazop-guide-best-practice`
- Domain: `hazop`
- Primary topic wiki: `hazop-pha-security-review`
- Primary procedural skill: `hazop-hazan-study-leader`
- Secondary skills: none
- Tags: `hazop`, `study-leader`, `guideword`, `node`, `worksheet-quality`, `recommendation`
- Pages: 184
- Usable text pages in current extraction: 168
- Indexed topic hits: 691
- Top signals: HAZOP/PHA:490, Incident/human factors:52, PSM/MOC/documentation:48, SIS/SIL:28, LOPA/IPL:27
- Source quality: outline/bookmark count: 103; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-hazop-guide-best-practice/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source to improve HAZOP study discipline and worksheet quality.

## Decisions This Source Can Support

- Whether the node boundary and design intent are specific enough for the selected deviation.
- Whether each row has one initiating cause, one unmitigated consequence path, and correctly separated safeguards.
- Whether a recommendation closes a real gap instead of restating normal design intent.

## Source-Derived Playbook

- Start from node intent, process parameter, guide word, normal envelope, and credible abnormal state.
- Rewrite vague causes so they name the failed equipment, failure mode, human/organizational condition, or external event.
- Write consequences as unmitigated event paths before safeguards, then test safeguards for effectiveness and independence.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| HAZOP/PHA | 490 | 2, 4-8, 11-12, 16-22, 24-25, 27-30, 32-41, 43, 45-64, 66-72, 74-98, 100-103, 105-112, 114-119, ... | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Incident/human factors | 52 | 6, 11, 17, 19, 21, 28, 35, 53, 58, 64, 78, 82, 85-86, 88-90, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| PSM/MOC/documentation | 48 | 6, 17, 21, 39, 47, 59, 61, 63-64, 66-67, 69-73, 76-77, 83-84, 93-94, 98, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| SIS/SIL | 28 | 25, 63, 77, 80-81, 91, 105, 169-171, 175, 179, 183 | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| LOPA/IPL | 27 | 6, 78, 90-92, 168, 170-171, 178, 180 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| Inherent safety/siting | 12 | 5, 23, 41, 66, 86, 96, 160, 170, 180 | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| Relief/effluent | 11 | 26, 53, 56, 58, 100, 130, 160, 166 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| QRA/risk criteria | 10 | 29, 38, 48, 88, 90, 169, 182 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Consequence analysis | 6 | 24, 54, 91, 97, 105, 155 | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Fire/explosion | 4 | 91, 98, 155, 171 | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Reliability data | 3 | 79, 88, 139 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |

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

- [ ] Node boundary and design intent
- [ ] Normal operating envelope
- [ ] P&ID/process graph context
- [ ] Safeguard design basis
- [ ] Relief/alarm/interlock/procedure evidence
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `hazop-guide-best-practice`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `hazop-guide-best-practice hazop study-leader guideword node worksheet-quality recommendation HAZOP cause consequence safeguard recommendation`
- `hazop-guide-best-practice HAZOP/PHA Incident/human factors PSM/MOC/documentation SIS/SIL missing basis project criteria data assumptions`
- `hazop-guide-best-practice AutoHAZOP node deviation scenario review quality gate`
- `hazop-guide-best-practice evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `hazop-hazan-study-leader` and secondary skills none when the decision requires a specialist workflow.

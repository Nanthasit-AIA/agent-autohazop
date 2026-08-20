# CCPS Hazard Evaluation Procedures - Book Wiki

## Source Card

- Source slug: `ccps-hazard-evaluation-procedures`
- Domain: `hazop`
- Primary topic wiki: `hazop-pha-security-review`
- Primary procedural skill: `hazop-hazan-study-leader`
- Secondary skills: none
- Tags: `hazard-evaluation`, `pha`, `hazop`, `what-if`, `checklist`, `fmea`
- Pages: 220
- Usable text pages in current extraction: 218
- Indexed topic hits: 919
- Top signals: HAZOP/PHA:257, Incident/human factors:238, QRA/risk criteria:194, Consequence analysis:68, LOPA/IPL:49
- Source quality: text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-hazard-evaluation-procedures/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| HAZOP/PHA | 257 | 5, 7-9, 12-13, 15, 18, 21-22, 24-26, 28-29, 31-39, 41-42, 45, 50-56, 67-70, 72-74, ... | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Incident/human factors | 238 | 8, 16, 19-20, 22, 24, 26, 28, 31-39, 45, 48, 53, 56, 58-66, 68, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| QRA/risk criteria | 194 | 15-16, 18, 24, 32, 34, 56, 58-63, 72, 132-156, 158, 162, 165-166, 168, 211-214 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Consequence analysis | 68 | 14, 19-22, 24, 26, 28, 34, 62-63, 68, 70, 72, 87-89, 94-96, 107, 131-132, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| LOPA/IPL | 49 | 8, 19, 22, 26, 32, 60-61, 72, 97, 154-156, 158, 162, 166 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| Relief/effluent | 33 | 39, 46, 76, 79, 81-83, 85, 122, 173-175, 179-181, 184, 188, 190, 193, 203 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Fire/explosion | 29 | 19, 30, 49, 87-91, 94, 182-183, 189-190, 193, 203-204, 209-210 | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Inherent safety/siting | 24 | 24, 28, 30, 49, 65, 76, 85, 91, 94, 123, 179, 189, 197, 207, ... | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| Reliability data | 17 | 56, 72, 126, 130-131, 211, 214, 216 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| PSM/MOC/documentation | 9 | 19-20, 31, 53, 55, 101, 124 | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| Alarm management | 1 | 60 | Challenge alarm rationalization, priority, response time, standing/flood alarms, operator action, and IPL claims. |

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
- Basis: `ccps-hazard-evaluation-procedures`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-hazard-evaluation-procedures hazard-evaluation pha hazop what-if checklist fmea HAZOP cause consequence safeguard recommendation`
- `ccps-hazard-evaluation-procedures HAZOP/PHA Incident/human factors QRA/risk criteria Consequence analysis missing basis project criteria data assumptions`
- `ccps-hazard-evaluation-procedures AutoHAZOP node deviation scenario review quality gate`
- `ccps-hazard-evaluation-procedures evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `hazop-hazan-study-leader` and secondary skills none when the decision requires a specialist workflow.

# Safety and Security Review for Process Industries - Book Wiki

## Source Card

- Source slug: `safety-security-review-process-industries`
- Domain: `hazop_security_review`
- Primary topic wiki: `hazop-pha-security-review`
- Primary procedural skill: `hazop-hazan-study-leader`
- Secondary skills: `process-safety-security-review`
- Tags: `hazop`, `pha`, `what-if`, `sva`, `security-vulnerability`, `review-method`
- Pages: 186
- Usable text pages in current extraction: 185
- Indexed topic hits: 1493
- Top signals: HAZOP/PHA:1021, Security review:163, SIS/SIL:68, PSM/MOC/documentation:63, LOPA/IPL:40
- Source quality: outline/bookmark count: 254; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-safety-security-review-process-industries/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| HAZOP/PHA | 1021 | 4, 6-8, 12, 16-17, 20, 23-37, 39, 48, 50, 52-53, 61-63, 66-72, 74, 77, ... | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Security review | 163 | 4, 6-7, 12, 17, 20, 22, 24-26, 33-36, 45-46, 48, 50, 53-55, 61-63, 66-67, ... | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |
| SIS/SIL | 68 | 6, 12, 17, 27, 36, 38-43, 66, 176-177, 181, 184-185 | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| PSM/MOC/documentation | 63 | 7-8, 17, 20, 22, 25, 29, 33, 54-55, 72, 74-76, 79, 86, 98, 106, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| LOPA/IPL | 40 | 12, 16, 27, 36, 39-43, 45, 66, 171, 181, 185 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| Relief/effluent | 35 | 39-40, 77, 84, 102, 109, 142-143, 146-148, 150-152, 162-163, 166, 169 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Incident/human factors | 30 | 23, 27-28, 39, 44, 77, 89, 92, 94, 98, 141, 155, 169-171, 176, 178, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Fire/explosion | 22 | 10, 17, 40, 77-78, 105, 108, 115, 121-122, 166, 169-170, 177-178 | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| QRA/risk criteria | 19 | 24, 37-38, 41, 98-99, 106, 140, 169, 171, 182 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Consequence analysis | 14 | 26, 40, 44, 46, 70, 90, 141, 148, 153, 158, 170 | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Inherent safety/siting | 12 | 41, 43, 46, 72, 77-78, 87, 89, 100, 169, 171 | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| Reliability data | 6 | 17, 24, 41, 43, 78 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |

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
- Basis: `safety-security-review-process-industries`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `safety-security-review-process-industries hazop pha what-if sva security-vulnerability review-method HAZOP cause consequence safeguard recommendation`
- `safety-security-review-process-industries HAZOP/PHA Security review SIS/SIL PSM/MOC/documentation missing basis project criteria data assumptions`
- `safety-security-review-process-industries AutoHAZOP node deviation scenario review quality gate`
- `safety-security-review-process-industries evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `hazop-hazan-study-leader` and secondary skills `process-safety-security-review` when the decision requires a specialist workflow.

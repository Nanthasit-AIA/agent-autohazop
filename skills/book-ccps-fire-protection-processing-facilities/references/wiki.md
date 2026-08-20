# CCPS Fire Protection in Processing Facilities - Book Wiki

## Source Card

- Source slug: `ccps-fire-protection-processing-facilities`
- Domain: `fire_protection`
- Primary topic wiki: `relief-fire-explosion-consequence`
- Primary procedural skill: `relief-effluent-fire-explosion-consequence`
- Secondary skills: `inherently-safer-siting-layout`
- Tags: `fire-protection`, `fire-hazard-analysis`, `fire-risk`, `emergency-response`, `inspection-testing-maintenance`
- Pages: 471
- Usable text pages in current extraction: 471
- Indexed topic hits: 1912
- Top signals: Fire/explosion:970, Consequence analysis:382, Inherent safety/siting:215, PSM/MOC/documentation:93, Relief/effluent:79
- Source quality: outline/bookmark count: 436; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-fire-protection-processing-facilities/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source to strengthen release, relief, fire/explosion, and consequence-screening logic.

## Decisions This Source Can Support

- Whether the source term, material state, inventory, pressure/temperature, and release path are defined.
- Whether relief, flare/effluent, dispersion, fire, explosion, toxic, or environmental consequence assumptions are supported.
- Whether escalation and emergency response claims are engineering controls, safeguards, or only mitigations.

## Source-Derived Playbook

- Start with material, inventory, phase, isolation, release size, duration, and destination.
- Challenge relief/consequence recommendations for calculation basis, design assumptions, and endpoint criteria.
- Use missing-basis actions for sizing, capacity, dispersion, radiation, overpressure, toxic endpoint, or flare/effluent limits.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| Fire/explosion | 970 | 1-3, 5-10, 12-21, 23-45, 47-49, 53, 55-60, 62-63, 66-68, 70-72, 74, 76-82, 84, 87-95, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Consequence analysis | 382 | 11, 13, 39, 49-52, 55-56, 58-59, 68, 71, 73-74, 76-82, 85-86, 90, 92, 94, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Inherent safety/siting | 215 | 10-11, 13, 23, 37, 39, 42, 44, 46, 49, 59-60, 116, 119, 136, 138, ... | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| PSM/MOC/documentation | 93 | 3, 8, 10-11, 15, 23, 40, 43-49, 58, 60, 62, 75, 119, 143, 346-347, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| Relief/effluent | 79 | 71, 80, 106-107, 141-143, 197, 210, 223, 245, 253-254, 264-265, 274, 284, 305-306, 312, ... | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| QRA/risk criteria | 69 | 71-73, 76, 117, 122, 124, 128-132, 134-135, 424, 434, 440, 443, 449, 452-456, 469 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Incident/human factors | 35 | 11, 46-47, 58, 91, 107, 109, 111, 282, 292, 395, 397-398, 400, 402-403, 405, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| HAZOP/PHA | 21 | 8, 11, 44, 46-47, 64, 68, 75, 120, 122, 161, 403, 434, 439, 453 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Reliability data | 21 | 7, 122, 125-127, 452, 462, 469 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| LOPA/IPL | 13 | 8, 120-122, 452, 454, 463-464, 469 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| Security review | 8 | 66, 97, 99, 137, 316 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |
| SIS/SIL | 6 | 8, 201, 322 | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |

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

- [ ] Material properties and inventory
- [ ] Relief/design basis and capacity calculation
- [ ] Release scenario/source-term basis
- [ ] Dispersion/fire/explosion/toxic endpoint criteria
- [ ] Flare/effluent/disposal system basis
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `ccps-fire-protection-processing-facilities`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-fire-protection-processing-facilities fire-protection fire-hazard-analysis fire-risk emergency-response inspection-testing-maintenance HAZOP cause consequence safeguard recommendation`
- `ccps-fire-protection-processing-facilities Fire/explosion Consequence analysis Inherent safety/siting PSM/MOC/documentation missing basis project criteria data assumptions`
- `ccps-fire-protection-processing-facilities AutoHAZOP node deviation scenario review quality gate`
- `ccps-fire-protection-processing-facilities evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `relief-effluent-fire-explosion-consequence` and secondary skills `inherently-safer-siting-layout` when the decision requires a specialist workflow.

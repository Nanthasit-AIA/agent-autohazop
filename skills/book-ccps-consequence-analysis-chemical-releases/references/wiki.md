# CCPS Consequence Analysis of Chemical Releases - Book Wiki

## Source Card

- Source slug: `ccps-consequence-analysis-chemical-releases`
- Domain: `consequence_analysis`
- Primary topic wiki: `relief-fire-explosion-consequence`
- Primary procedural skill: `relief-effluent-fire-explosion-consequence`
- Secondary skills: none
- Tags: `consequence-analysis`, `release`, `dispersion`, `toxic`, `flammable`, `source-term`
- Pages: 348
- Usable text pages in current extraction: 348
- Indexed topic hits: 1379
- Top signals: Consequence analysis:553, Fire/explosion:501, Relief/effluent:200, QRA/risk criteria:46, Incident/human factors:20
- Source quality: outline/bookmark count: 106; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-consequence-analysis-chemical-releases/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| Consequence analysis | 553 | 1-5, 7-15, 17-18, 20, 22-33, 35, 53-55, 72-74, 76, 84, 91-95, 98-133, 136-138, 140-146, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Fire/explosion | 501 | 4, 9, 11-12, 14-15, 18-19, 22-27, 54, 69, 129, 142-151, 155-156, 161-162, 164-169, 172-179, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Relief/effluent | 200 | 4, 19, 23, 25, 27, 32-33, 50, 54-55, 69-70, 78, 144, 146, 150-155, 157-160, ... | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| QRA/risk criteria | 46 | 3-5, 7, 9-10, 17, 19-20, 24, 287, 303-305, 307-310, 313-314, 317-318, 329, 333-334 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Incident/human factors | 20 | 10, 18, 20, 25, 117, 149, 201-202, 265, 287, 307-310, 341-343 | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Reliability data | 16 | 7, 10-11, 296, 305, 307-309, 311-312 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| HAZOP/PHA | 13 | 10-11, 18, 103, 253-254, 306, 309, 333 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| PSM/MOC/documentation | 9 | 3-4, 11, 17, 19, 278, 333 | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| Inherent safety/siting | 8 | 156, 165-166, 227, 279, 287, 314, 342 | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| LOPA/IPL | 7 | 23, 307, 310, 312 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| Security review | 5 | 25, 201, 219, 261, 307 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |
| SIS/SIL | 1 | 266 | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |

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
- Basis: `ccps-consequence-analysis-chemical-releases`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-consequence-analysis-chemical-releases consequence-analysis release dispersion toxic flammable source-term HAZOP cause consequence safeguard recommendation`
- `ccps-consequence-analysis-chemical-releases Consequence analysis Fire/explosion Relief/effluent QRA/risk criteria missing basis project criteria data assumptions`
- `ccps-consequence-analysis-chemical-releases AutoHAZOP node deviation scenario review quality gate`
- `ccps-consequence-analysis-chemical-releases evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `relief-effluent-fire-explosion-consequence` and secondary skills none when the decision requires a specialist workflow.

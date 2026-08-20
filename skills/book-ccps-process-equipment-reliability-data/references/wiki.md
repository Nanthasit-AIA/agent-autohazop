# CCPS Process Equipment Reliability Data - Book Wiki

## Source Card

- Source slug: `ccps-process-equipment-reliability-data`
- Domain: `reliability_data`
- Primary topic wiki: `reliability-data`
- Primary procedural skill: `reliability-data-selection`
- Secondary skills: none
- Tags: `failure-rate`, `reliability-data`, `equipment`, `data-quality`, `mechanical-integrity`
- Pages: 312
- Usable text pages in current extraction: 311
- Indexed topic hits: 568
- Top signals: Reliability data:457, QRA/risk criteria:31, Incident/human factors:26, Consequence analysis:14, PSM/MOC/documentation:12
- Source quality: outline/bookmark count: 135; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-process-equipment-reliability-data/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source to challenge reliability and failure-rate assumptions for applicability and uncertainty.

## Decisions This Source Can Support

- Whether the equipment class, service, duty cycle, environment, failure mode, and data source match.
- Whether data are being used for screening, LOPA/SIL verification, QRA, maintenance, or mechanical integrity.
- Whether uncertainty, confidence, common cause, and inspection/proof-test assumptions are visible.

## Source-Derived Playbook

- Name the equipment boundary and failure mode before applying any rate or probability.
- Treat handbook values as inputs needing applicability review, not universal plant facts.
- Route safety-instrumented data to SIS/SIL verification when it affects PFD/PFH or SIL target acceptance.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| Reliability data | 457 | 1-2, 4-12, 14-24, 26-32, 35-36, 40-49, 51-55, 58, 62, 64, 68, 71-79, 84-85, 87-88, ... | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| QRA/risk criteria | 31 | 4, 7-9, 11-12, 16, 42, 52, 55, 64, 70-71, 73, 131, 134, 245, 249, ... | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Incident/human factors | 26 | 4, 9, 12-13, 17, 23, 44-45, 54, 79, 89, 96, 105, 107, 111, 113, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Consequence analysis | 14 | 3, 16, 42, 64, 73, 143, 289, 295 | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| PSM/MOC/documentation | 12 | 48, 80, 112, 227, 229-230, 249 | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| HAZOP/PHA | 9 | 4, 9, 11, 16, 27, 69, 131 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Fire/explosion | 7 | 46-47, 64, 73, 250, 289, 294 | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| LOPA/IPL | 6 | 8, 10, 132, 135, 138 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| Relief/effluent | 5 | 23, 69, 240, 291, 297 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| SIS/SIL | 1 | 125 | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |

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

- [ ] Equipment taxonomy and failure mode
- [ ] Operating/service context
- [ ] Approved reliability data source
- [ ] Proof-test/inspection interval
- [ ] Uncertainty and common-cause basis
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `ccps-process-equipment-reliability-data`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-process-equipment-reliability-data failure-rate reliability-data equipment data-quality mechanical-integrity HAZOP cause consequence safeguard recommendation`
- `ccps-process-equipment-reliability-data Reliability data QRA/risk criteria Incident/human factors Consequence analysis missing basis project criteria data assumptions`
- `ccps-process-equipment-reliability-data AutoHAZOP node deviation scenario review quality gate`
- `ccps-process-equipment-reliability-data evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `reliability-data-selection` and secondary skills none when the decision requires a specialist workflow.

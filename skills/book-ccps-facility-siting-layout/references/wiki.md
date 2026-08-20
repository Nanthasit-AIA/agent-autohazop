# CCPS Facility Siting and Layout - Book Wiki

## Source Card

- Source slug: `ccps-facility-siting-layout`
- Domain: `siting_layout`
- Primary topic wiki: `inherent-safety-siting-layout`
- Primary procedural skill: `inherently-safer-siting-layout`
- Secondary skills: none
- Tags: `facility-siting`, `layout`, `occupied-building`, `spacing`, `congestion`, `vulnerability`
- Pages: 163
- Usable text pages in current extraction: 156
- Indexed topic hits: 950
- Top signals: Inherent safety/siting:612, Fire/explosion:135, Consequence analysis:118, Relief/effluent:49, Incident/human factors:10
- Source quality: outline/bookmark count: 51; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-facility-siting-layout/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source to prefer inherent safety and layout/siting risk reduction before add-on protection.

## Decisions This Source Can Support

- Whether hazard can be eliminated, substituted, minimized, moderated, simplified, segregated, or relocated.
- Whether occupied building, congestion, drainage, escalation, access/egress, or emergency response exposure is relevant.
- Whether a safeguard is compensating for a design/layout issue that should be challenged earlier.

## Source-Derived Playbook

- Ask whether the inventory, pressure, temperature, material, location, or operating complexity can be reduced.
- Challenge siting/layout recommendations for exposure path, occupancy, separation, drainage, and escalation basis.
- Prefer durable design changes before administrative controls when the scenario permits.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| Inherent safety/siting | 612 | 2, 4-8, 10-11, 13-36, 38, 40, 42-48, 50-52, 54-56, 58, 60, 62-66, 68, 70-95, ... | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| Fire/explosion | 135 | 5, 13, 15-17, 19-20, 28, 32-35, 43, 64, 70-74, 76-78, 80-84, 87, 90, 92-95, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Consequence analysis | 118 | 7, 13, 16-18, 24, 28-34, 40, 49-51, 57-58, 60, 70, 72-73, 75-81, 88, 90-93, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Relief/effluent | 49 | 12, 29, 32-33, 36, 40, 58-59, 63-64, 66, 75, 79-80, 83, 94, 97, 101-102, ... | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Incident/human factors | 10 | 30, 62, 98, 105, 146, 150 | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Security review | 9 | 28-29, 33, 60-61 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |
| PSM/MOC/documentation | 5 | 105, 141, 146, 156, 158 | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| HAZOP/PHA | 4 | 15, 29, 50, 152 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| QRA/risk criteria | 4 | 15, 145-147 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| LOPA/IPL | 2 | 15, 92 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| SIS/SIL | 1 | 32 | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| Reliability data | 1 | 56 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |

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

- [ ] Inventory and layout basis
- [ ] Occupied building/siting criteria
- [ ] Escalation and drainage path
- [ ] Access/egress and emergency response assumptions
- [ ] Inherent safety option comparison
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `ccps-facility-siting-layout`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-facility-siting-layout facility-siting layout occupied-building spacing congestion vulnerability HAZOP cause consequence safeguard recommendation`
- `ccps-facility-siting-layout Inherent safety/siting Fire/explosion Consequence analysis Relief/effluent missing basis project criteria data assumptions`
- `ccps-facility-siting-layout AutoHAZOP node deviation scenario review quality gate`
- `ccps-facility-siting-layout evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `inherently-safer-siting-layout` and secondary skills none when the decision requires a specialist workflow.

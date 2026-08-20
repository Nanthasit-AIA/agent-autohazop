# Process Plants - Inherently Safer Design - Book Wiki

## Source Card

- Source slug: `process-plants-inherently-safer-design`
- Domain: `inherent_safety`
- Primary topic wiki: `inherent-safety-siting-layout`
- Primary procedural skill: `inherently-safer-siting-layout`
- Secondary skills: none
- Tags: `inherent-safety`, `intensification`, `substitution`, `attenuation`, `simplification`, `layout`
- Pages: 386
- Usable text pages in current extraction: 369
- Indexed topic hits: 1554
- Top signals: Inherent safety/siting:742, Fire/explosion:326, Consequence analysis:160, Incident/human factors:111, HAZOP/PHA:85
- Source quality: outline/bookmark count: 24; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-process-plants-inherently-safer-design/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| Inherent safety/siting | 742 | 2, 4-5, 8, 12-13, 16-20, 22, 24-53, 55-57, 59, 61, 63, 65, 67, 69, ... | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| Fire/explosion | 326 | 10, 12, 18, 22, 26, 35, 37, 43, 45-47, 52, 55, 59-60, 62, 64-65, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Consequence analysis | 160 | 10, 26-28, 30-31, 37, 43-47, 56, 59-60, 69, 86, 103-107, 109-113, 116-118, 129, 137, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Incident/human factors | 111 | 10, 12, 24, 40, 43, 51, 74, 88-89, 100, 118, 130, 132-133, 142, 148, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| HAZOP/PHA | 85 | 11, 40, 74, 100, 152, 163, 173-174, 203, 213-214, 222, 226-230, 233-234, 237-239, 248, ... | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| PSM/MOC/documentation | 71 | 12, 89, 96, 120, 133, 148, 173, 180, 211, 258-261, 265-266, 268-269, 271, 273, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| Relief/effluent | 38 | 43, 110, 112, 136, 142, 153-154, 162-164, 171-172, 237-238, 250, 314-315, 317-319, 322, 334, ... | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| QRA/risk criteria | 16 | 25, 53, 195, 250, 262, 355-356, 363, 365, 382 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| LOPA/IPL | 5 | 40-41, 211, 340 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |

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
- Basis: `process-plants-inherently-safer-design`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `process-plants-inherently-safer-design inherent-safety intensification substitution attenuation simplification layout HAZOP cause consequence safeguard recommendation`
- `process-plants-inherently-safer-design Inherent safety/siting Fire/explosion Consequence analysis Incident/human factors missing basis project criteria data assumptions`
- `process-plants-inherently-safer-design AutoHAZOP node deviation scenario review quality gate`
- `process-plants-inherently-safer-design evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `inherently-safer-siting-layout` and secondary skills none when the decision requires a specialist workflow.

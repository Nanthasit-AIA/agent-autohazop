# CCPS VCE, Flash Fire and BLEVE Characteristics - Book Wiki

## Source Card

- Source slug: `ccps-vce-flash-fire-bleve`
- Domain: `fire_explosion`
- Primary topic wiki: `relief-fire-explosion-consequence`
- Primary procedural skill: `relief-effluent-fire-explosion-consequence`
- Secondary skills: none
- Tags: `vce`, `flash-fire`, `bleve`, `overpressure`, `thermal-radiation`, `consequence`
- Pages: 402
- Usable text pages in current extraction: 394
- Indexed topic hits: 1155
- Top signals: Fire/explosion:683, Relief/effluent:248, Consequence analysis:149, Incident/human factors:56, Inherent safety/siting:10
- Source quality: text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-vce-flash-fire-bleve/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| Fire/explosion | 683 | 4, 6-10, 14-20, 22-23, 25-28, 30-37, 39, 41-42, 44, 46-47, 51-52, 54, 56-59, 62-63, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Relief/effluent | 248 | 7-8, 14-15, 31, 34, 46-47, 54, 68-70, 80-81, 83-85, 88-91, 94-96, 104-105, 107, 112, ... | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Consequence analysis | 149 | 6-9, 12-20, 22, 35, 56, 58-61, 70, 78, 80, 82, 86, 102, 122-124, 126-127, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Incident/human factors | 56 | 9, 12-15, 21, 23, 30-32, 35-37, 39, 41-42, 44-45, 50-51, 54, 56-58, 99-100, 128, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Inherent safety/siting | 10 | 14, 34, 40, 45, 48, 80, 139, 264, 277 | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| HAZOP/PHA | 3 | 234, 254-255 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| PSM/MOC/documentation | 3 | 19-21 | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| QRA/risk criteria | 2 | 16-17 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Reliability data | 1 | 246 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |

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
- Basis: `ccps-vce-flash-fire-bleve`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-vce-flash-fire-bleve vce flash-fire bleve overpressure thermal-radiation consequence HAZOP cause consequence safeguard recommendation`
- `ccps-vce-flash-fire-bleve Fire/explosion Relief/effluent Consequence analysis Incident/human factors missing basis project criteria data assumptions`
- `ccps-vce-flash-fire-bleve AutoHAZOP node deviation scenario review quality gate`
- `ccps-vce-flash-fire-bleve evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `relief-effluent-fire-explosion-consequence` and secondary skills none when the decision requires a specialist workflow.

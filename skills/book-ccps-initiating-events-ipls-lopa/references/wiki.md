# CCPS Initiating Events and IPLs in LOPA - Book Wiki

## Source Card

- Source slug: `ccps-initiating-events-ipls-lopa`
- Domain: `lopa`
- Primary topic wiki: `lopa-sil-sis`
- Primary procedural skill: `lopa-iel-conditional-modifier`
- Secondary skills: `reliability-data-selection`
- Tags: `lopa`, `initiating-event`, `ipl`, `pfd`, `independence`, `failure-rate`
- Pages: 381
- Usable text pages in current extraction: 366
- Indexed topic hits: 3065
- Top signals: LOPA/IPL:1326, SIS/SIL:336, Relief/effluent:336, Reliability data:309, Incident/human factors:250
- Source quality: outline/bookmark count: 99; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-initiating-events-ipls-lopa/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source to turn selected HAZOP rows into disciplined one-scenario LOPA checks.

## Decisions This Source Can Support

- Whether the scenario has one initiating event, one consequence, and explicit enabling conditions/conditional modifiers.
- Whether a safeguard qualifies as an IPL with independence, effectiveness, auditability, and timing.
- Whether likelihood reduction is supported without double counting BPCS, alarms, SIS, relief, procedures, or inspection.

## Source-Derived Playbook

- State the initiating event family before assigning or requesting frequency data.
- Separate safeguards from credited IPLs and state why each credited IPL is independent of the cause.
- Fail closed when risk criteria, frequency data, conditional modifiers, or IPL PFD/test basis are absent.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| LOPA/IPL | 1326 | 6, 9-14, 18, 22-24, 27-28, 31-64, 66-88, 90-92, 94, 96-108, 110, 112-122, 124, 126, ... | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| SIS/SIL | 336 | 14, 19, 21, 24-25, 28, 35, 37, 41, 47, 54, 59, 67, 71, 73, ... | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| Relief/effluent | 336 | 12-14, 19, 22, 36, 46, 52, 67-68, 72, 74, 76-77, 93, 127-129, 151, 155, ... | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Reliability data | 309 | 10, 12, 18-19, 21-22, 36-38, 43-47, 51, 53-54, 56-59, 63-64, 68-72, 82-84, 91, 96-97, ... | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| Incident/human factors | 250 | 10-11, 13, 18-19, 23-24, 38, 41, 44-45, 47-50, 52, 54-58, 63, 67, 69-70, 78-80, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| QRA/risk criteria | 136 | 10-11, 17-19, 34-35, 38-39, 42, 44, 47, 52, 62-64, 71, 88, 90, 92, 119, ... | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Fire/explosion | 115 | 14-15, 17-18, 52, 61, 120, 151-153, 171, 175, 177, 236-240, 257, 266, 268-270, 275-277, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| PSM/MOC/documentation | 72 | 10, 18-19, 32, 34-35, 41, 43, 45, 47-51, 53, 59, 64, 66-67, 69, 84-86, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| HAZOP/PHA | 68 | 11, 18-19, 24, 32, 35, 37-38, 40, 44, 47, 51-52, 59, 73-76, 80-81, 84, ... | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Consequence analysis | 67 | 39, 43, 47, 52-53, 60, 64, 75, 90-91, 153-155, 157-162, 171, 177, 228, 233, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Inherent safety/siting | 36 | 9-11, 42, 44, 47, 51, 55, 60-61, 63-64, 91-92, 147, 293, 319, 369, 375, ... | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| Alarm management | 10 | 72, 179-180, 186, 264, 319, 327-328, 339 | Challenge alarm rationalization, priority, response time, standing/flood alarms, operator action, and IPL claims. |
| Security review | 4 | 196, 321-322 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |

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

- [ ] Project LOPA rules and tolerable risk criteria
- [ ] Approved initiating-event frequency source
- [ ] Conditional modifier/enabling-condition basis
- [ ] IPL independence, audit, response-time, and proof-test evidence
- [ ] Common-cause and double-counting review
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `ccps-initiating-events-ipls-lopa`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-initiating-events-ipls-lopa lopa initiating-event ipl pfd independence failure-rate HAZOP cause consequence safeguard recommendation`
- `ccps-initiating-events-ipls-lopa LOPA/IPL SIS/SIL Relief/effluent Reliability data missing basis project criteria data assumptions`
- `ccps-initiating-events-ipls-lopa AutoHAZOP node deviation scenario review quality gate`
- `ccps-initiating-events-ipls-lopa evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `lopa-iel-conditional-modifier` and secondary skills `reliability-data-selection` when the decision requires a specialist workflow.

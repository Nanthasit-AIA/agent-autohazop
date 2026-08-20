# CCPS Enabling Conditions and Conditional Modifiers in LOPA - Book Wiki

## Source Card

- Source slug: `ccps-enabling-conditions-conditional-modifiers-lopa`
- Domain: `lopa`
- Primary topic wiki: `lopa-sil-sis`
- Primary procedural skill: `lopa-iel-conditional-modifier`
- Secondary skills: none
- Tags: `lopa`, `enabling-condition`, `conditional-modifier`, `occupancy`, `ignition`, `vulnerability`
- Pages: 136
- Usable text pages in current extraction: 124
- Indexed topic hits: 1232
- Top signals: LOPA/IPL:590, Consequence analysis:194, Fire/explosion:133, QRA/risk criteria:130, HAZOP/PHA:80
- Source quality: outline/bookmark count: 41; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-enabling-conditions-conditional-modifiers-lopa/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| LOPA/IPL | 590 | 6, 9-11, 13, 15, 17-18, 20-21, 27-29, 31-97, 99, 101-102, 105-109, 111, 114-115, 119-123, ... | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| Consequence analysis | 194 | 11, 15, 18, 21, 23, 31, 33, 43, 45-52, 56-57, 62-63, 68, 71-85, 87-88, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Fire/explosion | 133 | 9, 11, 16-18, 21, 43, 45, 47-48, 52, 60, 66-67, 69-70, 72-75, 77-84, 87-88, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| QRA/risk criteria | 130 | 9-10, 13, 15-19, 21-23, 28-29, 31-33, 37-38, 40-47, 49-50, 57, 67, 70, 74, 78-79, ... | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| HAZOP/PHA | 80 | 11, 15, 17-21, 23, 29, 31-34, 67, 99, 101, 105-109, 113-114, 119-120, 130, 134-135 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| PSM/MOC/documentation | 31 | 21, 28-29, 32, 35, 65-66, 68, 71, 83, 86, 89, 99, 127, 134 | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| Relief/effluent | 18 | 16, 39, 42, 52, 61-62, 82, 85, 88, 96, 104, 123 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Reliability data | 18 | 17, 19, 36, 39, 57, 105, 109, 115-116 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| SIS/SIL | 15 | 16, 25, 35, 39, 67, 135 | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| Incident/human factors | 9 | 20, 32, 34, 57-58, 71, 115 | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Inherent safety/siting | 9 | 38, 47-48, 78, 82-83, 89 | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| Alarm management | 3 | 39, 67, 85 | Challenge alarm rationalization, priority, response time, standing/flood alarms, operator action, and IPL claims. |
| Security review | 2 | 19, 70 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |

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
- Basis: `ccps-enabling-conditions-conditional-modifiers-lopa`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-enabling-conditions-conditional-modifiers-lopa lopa enabling-condition conditional-modifier occupancy ignition vulnerability HAZOP cause consequence safeguard recommendation`
- `ccps-enabling-conditions-conditional-modifiers-lopa LOPA/IPL Consequence analysis Fire/explosion QRA/risk criteria missing basis project criteria data assumptions`
- `ccps-enabling-conditions-conditional-modifiers-lopa AutoHAZOP node deviation scenario review quality gate`
- `ccps-enabling-conditions-conditional-modifiers-lopa evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `lopa-iel-conditional-modifier` and secondary skills none when the decision requires a specialist workflow.

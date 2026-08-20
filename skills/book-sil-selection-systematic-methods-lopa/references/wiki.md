# SIL Selection - Systematic Methods Including LOPA - Book Wiki

## Source Card

- Source slug: `sil-selection-systematic-methods-lopa`
- Domain: `lopa_sis`
- Primary topic wiki: `lopa-sil-sis`
- Primary procedural skill: `lopa-iel-conditional-modifier`
- Secondary skills: `sis-sil-verification-reliability`, `risk-criteria-qra`
- Tags: `sil-selection`, `lopa`, `sif`, `tolerable-risk`, `probability`, `fault-tree`
- Pages: 264
- Usable text pages in current extraction: 264
- Indexed topic hits: 2537
- Top signals: SIS/SIL:955, LOPA/IPL:369, QRA/risk criteria:326, Consequence analysis:228, Fire/explosion:222
- Source quality: outline/bookmark count: 208; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-sil-selection-systematic-methods-lopa/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| SIS/SIL | 955 | 3-4, 6-14, 16-36, 45-46, 49-51, 54-65, 74, 80-81, 84, 86-87, 89, 93-95, 97, 100, ... | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| LOPA/IPL | 369 | 1, 3, 5-6, 8, 10-12, 14, 16-18, 20-22, 24, 26, 28-30, 32, 34, 36, ... | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| QRA/risk criteria | 326 | 4-6, 13, 16, 19-20, 28, 35, 37, 39, 41-54, 66, 74-79, 89-90, 92-94, 97, ... | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Consequence analysis | 228 | 5, 12-13, 17, 28, 45, 53, 59, 64, 92-96, 98-106, 108-121, 136-137, 140-142, 147, ... | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Fire/explosion | 222 | 46, 51, 94, 97-99, 101-109, 112, 115-116, 118-120, 122, 126, 140-143, 145, 148, 152, ... | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Reliability data | 114 | 5, 68, 75-76, 78-87, 89-91, 123, 127, 132, 137, 155-156, 161-163, 166-167, 202, 216, ... | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| HAZOP/PHA | 101 | 4, 28, 32, 56-65, 147, 152, 200, 226, 229, 235, 255, 259-260, 264 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Incident/human factors | 99 | 7, 19-20, 44, 48, 50, 56, 58, 60, 63-64, 68, 74-75, 80, 93, 95-98, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Relief/effluent | 77 | 59, 61, 67-68, 85-86, 90, 99, 102, 106-107, 116, 127-132, 136, 147-148, 150, 154-156, ... | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| PSM/MOC/documentation | 22 | 24-25, 30-31, 56, 61-62, 64, 80, 131, 208, 219, 235 | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| Alarm management | 19 | 147, 151-153, 161, 242, 259 | Challenge alarm rationalization, priority, response time, standing/flood alarms, operator action, and IPL claims. |
| Inherent safety/siting | 5 | 30, 43, 111, 232 | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |

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
- Basis: `sil-selection-systematic-methods-lopa`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `sil-selection-systematic-methods-lopa sil-selection lopa sif tolerable-risk probability fault-tree HAZOP cause consequence safeguard recommendation`
- `sil-selection-systematic-methods-lopa SIS/SIL LOPA/IPL QRA/risk criteria Consequence analysis missing basis project criteria data assumptions`
- `sil-selection-systematic-methods-lopa AutoHAZOP node deviation scenario review quality gate`
- `sil-selection-systematic-methods-lopa evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `lopa-iel-conditional-modifier` and secondary skills `sis-sil-verification-reliability`, `risk-criteria-qra` when the decision requires a specialist workflow.

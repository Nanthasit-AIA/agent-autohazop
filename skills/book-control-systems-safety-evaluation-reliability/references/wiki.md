# Control Systems Safety Evaluation and Reliability - Book Wiki

## Source Card

- Source slug: `control-systems-safety-evaluation-reliability`
- Domain: `sis_reliability`
- Primary topic wiki: `lopa-sil-sis`
- Primary procedural skill: `sis-sil-verification-reliability`
- Secondary skills: `reliability-data-selection`
- Tags: `control-system`, `reliability`, `safety-evaluation`, `failure-rate`, `architecture`
- Pages: 476
- Usable text pages in current extraction: 476
- Indexed topic hits: 1180
- Top signals: Reliability data:583, SIS/SIL:338, QRA/risk criteria:184, HAZOP/PHA:16, Incident/human factors:16
- Source quality: text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-control-systems-safety-evaluation-reliability/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source to challenge SIS/SIF claims through lifecycle evidence, not labels.

## Decisions This Source Can Support

- Whether a claimed SIF has a defined hazardous event, safe state, sensor-logic-final element chain, and demand mode.
- Whether SIL target, PFD/PFH, proof-test interval, bypass controls, and independence from BPCS are supported.
- Whether the evidence belongs in HAZOP, LOPA, SRS, SIL verification, validation, or operations/maintenance.

## Source-Derived Playbook

- Map every claimed SIF to cause, consequence, safe state, response time, and equipment architecture.
- Challenge generic SIL statements unless the lifecycle and verification basis are present.
- Route reliability-data assumptions to approved plant/project sources before accepting PFD/PFH.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| Reliability data | 583 | 10-11, 16, 20, 24, 41, 44, 54, 60, 68-70, 75-76, 82-98, 101-107, 110, 112-114, ... | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| SIS/SIL | 338 | 10, 12, 15, 17, 19, 22-26, 53, 59, 75, 96-100, 103, 108-109, 112, 117, ... | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| QRA/risk criteria | 184 | 10, 20, 121-137, 167, 235-236, 274-275, 278, 282, 288-289, 291-294, 297-299, 308-309, 329-331, 335-336, ... | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| HAZOP/PHA | 16 | 40, 42-43, 46, 65, 67, 74, 460, 469, 475 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Incident/human factors | 16 | 64, 123, 219-221, 242-243, 377-378, 393 | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| PSM/MOC/documentation | 14 | 5, 10, 53, 106-107, 121, 134, 231, 245, 399-401, 405 | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| Relief/effluent | 8 | 57, 111, 297, 300, 303, 382 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Fire/explosion | 8 | 27, 183, 449, 451 | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Consequence analysis | 7 | 154, 389 | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| LOPA/IPL | 6 | 382-383, 394 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |

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

- [ ] SIL target allocation basis
- [ ] SRS/SIF definition
- [ ] PFD/PFH calculation and proof-test interval
- [ ] Independence from BPCS and common-cause review
- [ ] Validation, bypass, maintenance, and proof-test records
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `control-systems-safety-evaluation-reliability`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `control-systems-safety-evaluation-reliability control-system reliability safety-evaluation failure-rate architecture HAZOP cause consequence safeguard recommendation`
- `control-systems-safety-evaluation-reliability Reliability data SIS/SIL QRA/risk criteria HAZOP/PHA missing basis project criteria data assumptions`
- `control-systems-safety-evaluation-reliability AutoHAZOP node deviation scenario review quality gate`
- `control-systems-safety-evaluation-reliability evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `sis-sil-verification-reliability` and secondary skills `reliability-data-selection` when the decision requires a specialist workflow.

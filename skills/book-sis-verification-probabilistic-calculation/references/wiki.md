# SIS Verification - Probabilistic Calculation - Book Wiki

## Source Card

- Source slug: `sis-verification-probabilistic-calculation`
- Domain: `sis_reliability`
- Primary topic wiki: `lopa-sil-sis`
- Primary procedural skill: `sis-sil-verification-reliability`
- Secondary skills: none
- Tags: `sis`, `pfdavg`, `pfh`, `proof-test`, `common-cause`, `probabilistic-calculation`
- Pages: 385
- Usable text pages in current extraction: 385
- Indexed topic hits: 2074
- Top signals: SIS/SIL:1376, Reliability data:456, QRA/risk criteria:163, LOPA/IPL:18, PSM/MOC/documentation:16
- Source quality: text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-sis-verification-probabilistic-calculation/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| SIS/SIL | 1376 | 1, 4-9, 11-36, 38-39, 42-43, 47-51, 58-60, 62, 65-66, 68-69, 73-75, 77, 82, 85-86, ... | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| Reliability data | 456 | 6-9, 20, 30, 38-44, 46-51, 55-61, 64-66, 68-69, 72-73, 75, 79, 83-84, 86, 90-93, ... | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| QRA/risk criteria | 163 | 7, 18, 72-76, 78-81, 85, 88-89, 94, 118-119, 201, 203-207, 209-210, 215-216, 218, 220, ... | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| LOPA/IPL | 18 | 18-19, 22, 25, 27, 105, 121, 123, 235, 238 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| PSM/MOC/documentation | 16 | 15, 20-21, 99-100, 117, 119, 154, 160, 235, 305-306, 382 | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| HAZOP/PHA | 12 | 14, 25, 30, 36, 188, 200, 247-248, 287, 293, 382, 384 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Incident/human factors | 9 | 14-15, 26, 125, 129, 134 | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Relief/effluent | 8 | 32, 196, 200, 207 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Consequence analysis | 8 | 18, 22, 34, 95, 221, 230, 367 | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Fire/explosion | 5 | 32, 49, 221 | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Inherent safety/siting | 2 | 20, 147 | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| Security review | 1 | 23 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |

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
- Basis: `sis-verification-probabilistic-calculation`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `sis-verification-probabilistic-calculation sis pfdavg pfh proof-test common-cause probabilistic-calculation HAZOP cause consequence safeguard recommendation`
- `sis-verification-probabilistic-calculation SIS/SIL Reliability data QRA/risk criteria LOPA/IPL missing basis project criteria data assumptions`
- `sis-verification-probabilistic-calculation AutoHAZOP node deviation scenario review quality gate`
- `sis-verification-probabilistic-calculation evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `sis-sil-verification-reliability` and secondary skills none when the decision requires a specialist workflow.

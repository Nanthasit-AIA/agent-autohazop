# PDS Data Handbook for SIS - Book Wiki

## Source Card

- Source slug: `pds-data-handbook-sis`
- Domain: `sis_reliability`
- Primary topic wiki: `reliability-data`
- Primary procedural skill: `reliability-data-selection`
- Secondary skills: `sis-sil-verification-reliability`
- Tags: `pds`, `sis`, `failure-rate`, `reliability-data`, `proof-test`, `pfd`
- Pages: 112
- Usable text pages in current extraction: 111
- Indexed topic hits: 898
- Top signals: Reliability data:734, SIS/SIL:149, Relief/effluent:8, Consequence analysis:4, PSM/MOC/documentation:2
- Source quality: outline/bookmark count: 83; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-pds-data-handbook-sis/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| Reliability data | 734 | 2-5, 7-18, 20, 22, 24-33, 35-37, 39-67, 69-112 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| SIS/SIL | 149 | 2-5, 7-11, 13, 15-18, 20, 22, 24, 26-33, 35-37, 39, 41-43, 45, 47, 49, ... | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| Relief/effluent | 8 | 6, 20-22, 31, 99-100 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Consequence analysis | 4 | 65 | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| PSM/MOC/documentation | 2 | 34, 45 | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| Incident/human factors | 1 | 8 | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |

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
- Basis: `pds-data-handbook-sis`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `pds-data-handbook-sis pds sis failure-rate reliability-data proof-test pfd HAZOP cause consequence safeguard recommendation`
- `pds-data-handbook-sis Reliability data SIS/SIL Relief/effluent Consequence analysis missing basis project criteria data assumptions`
- `pds-data-handbook-sis AutoHAZOP node deviation scenario review quality gate`
- `pds-data-handbook-sis evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `reliability-data-selection` and secondary skills `sis-sil-verification-reliability` when the decision requires a specialist workflow.

# Functional Safety - IEC 61508 and Related Standards - Book Wiki

## Source Card

- Source slug: `functional-safety-straightforward-guide`
- Domain: `functional_safety`
- Primary topic wiki: `lopa-sil-sis`
- Primary procedural skill: `sis-sil-verification-reliability`
- Secondary skills: none
- Tags: `functional-safety`, `iec-61508`, `sil`, `safety-lifecycle`, `sif`
- Pages: 276
- Usable text pages in current extraction: 275
- Indexed topic hits: 1323
- Top signals: SIS/SIL:836, Reliability data:267, QRA/risk criteria:99, Incident/human factors:47, PSM/MOC/documentation:37
- Source quality: outline/bookmark count: 252; text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-functional-safety-straightforward-guide/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| SIS/SIL | 836 | 2, 4, 6-8, 10-11, 14, 17-19, 21-33, 36, 38-102, 104, 107, 109, 111, 113, ... | Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. |
| Reliability data | 267 | 7, 10, 16-17, 21-22, 25, 28, 32, 34, 43-45, 50, 58, 63-64, 74, 92, ... | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| QRA/risk criteria | 99 | 17-18, 20, 28, 30, 33, 44-48, 50-51, 53, 64, 92, 107, 116-120, 123-124, 146, ... | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Incident/human factors | 47 | 7, 16-17, 26, 30, 40, 45, 61, 97, 120-124, 130, 158, 204, 207-208, 245, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| PSM/MOC/documentation | 37 | 27, 38, 41, 56-57, 65, 69-70, 81, 87-89, 101, 164, 171, 193, 225-226, 228, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| HAZOP/PHA | 12 | 25, 27, 40, 65, 155, 176, 267, 275 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| Relief/effluent | 8 | 28, 47, 176-177, 179, 244 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| Fire/explosion | 6 | 43, 133, 176, 185-186 | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| LOPA/IPL | 4 | 46, 96, 275 | Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. |
| Consequence analysis | 4 | 81, 91, 205, 258 | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Inherent safety/siting | 3 | 57, 68, 87 | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |

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
- Basis: `functional-safety-straightforward-guide`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `functional-safety-straightforward-guide functional-safety iec-61508 sil safety-lifecycle sif HAZOP cause consequence safeguard recommendation`
- `functional-safety-straightforward-guide SIS/SIL Reliability data QRA/risk criteria Incident/human factors missing basis project criteria data assumptions`
- `functional-safety-straightforward-guide AutoHAZOP node deviation scenario review quality gate`
- `functional-safety-straightforward-guide evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `sis-sil-verification-reliability` and secondary skills none when the decision requires a specialist workflow.

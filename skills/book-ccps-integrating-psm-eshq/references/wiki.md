# CCPS Integrating PSM, ESH and Quality - Book Wiki

## Source Card

- Source slug: `ccps-integrating-psm-eshq`
- Domain: `psm_integration`
- Primary topic wiki: `psm-rbps-moc-documentation`
- Primary procedural skill: `process-safety-management-rbps-moc-docs`
- Secondary skills: none
- Tags: `psm`, `eshq`, `integration`, `management-system`, `audit`
- Pages: 200
- Usable text pages in current extraction: 191
- Indexed topic hits: 213
- Top signals: PSM/MOC/documentation:144, Incident/human factors:41, Consequence analysis:9, Relief/effluent:7, HAZOP/PHA:5
- Source quality: text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-integrating-psm-eshq/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source to turn technical gaps into auditable process-safety management actions.

## Decisions This Source Can Support

- Whether the gap is PSI, procedure, training, MOC, PSSR, mechanical integrity, emergency management, audit, or action tracking.
- Whether a recommendation names an accountable management-system deliverable.
- Whether documentation is sufficient to support later HAZOP/LOPA/SIS decisions.

## Source-Derived Playbook

- Translate vague 'review/update' actions into specific records, owners, acceptance criteria, and verification evidence.
- Flag MOC/PSSR needs when design, procedure, alarm, interlock, relief, operating envelope, or equipment service changes.
- Keep technical and management-system recommendations linked to the scenario that created the need.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| PSM/MOC/documentation | 144 | 5-6, 11, 16, 18, 24-26, 38-39, 48, 52, 54, 57, 62, 66-67, 73, 83, ... | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |
| Incident/human factors | 41 | 41-42, 60-61, 73, 82, 98, 118, 122, 133-134, 139, 141-142, 145, 152, 156-158, 169-170, ... | Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. |
| Consequence analysis | 9 | 41, 66-67, 170, 193-194 | Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. |
| Relief/effluent | 7 | 139, 142, 144-145 | Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. |
| HAZOP/PHA | 5 | 117, 144, 177, 193 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| QRA/risk criteria | 2 | 144, 194 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |
| Inherent safety/siting | 2 | 194 | Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. |
| Fire/explosion | 1 | 41 | Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. |
| Reliability data | 1 | 194 | Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. |
| Security review | 1 | 114 | Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. |

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

- [ ] Process safety information
- [ ] Operating procedure/training record
- [ ] MOC/PSSR evidence
- [ ] Inspection/test/maintenance record
- [ ] Audit/action-tracking closure evidence
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `ccps-integrating-psm-eshq`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-integrating-psm-eshq psm eshq integration management-system audit HAZOP cause consequence safeguard recommendation`
- `ccps-integrating-psm-eshq PSM/MOC/documentation Incident/human factors Consequence analysis Relief/effluent missing basis project criteria data assumptions`
- `ccps-integrating-psm-eshq AutoHAZOP node deviation scenario review quality gate`
- `ccps-integrating-psm-eshq evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `process-safety-management-rbps-moc-docs` and secondary skills none when the decision requires a specialist workflow.

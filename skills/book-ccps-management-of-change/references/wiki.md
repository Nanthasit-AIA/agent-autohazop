# CCPS Guidelines for Management of Change - Book Wiki

## Source Card

- Source slug: `ccps-management-of-change`
- Domain: `moc`
- Primary topic wiki: `psm-rbps-moc-documentation`
- Primary procedural skill: `process-safety-management-rbps-moc-docs`
- Secondary skills: none
- Tags: `moc`, `change-control`, `psm`, `temporary-change`, `pre-startup-review`
- Pages: 197
- Usable text pages in current extraction: 1
- Indexed topic hits: 1
- Top signals: PSM/MOC/documentation:1
- Source quality: text layer weak; limited working coverage; Text layer is weak; mark detailed claims as missing basis for detailed checklists.
- AI confidence tier: controlled-use - Use for qualitative review and conservative prompts; do not support detailed numeric, tabular, or chapter-specific claims.

## Role In AUTO HAZOP

Use this wiki as screening guidance with explicit missing-basis controls for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-ccps-management-of-change/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

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
| PSM/MOC/documentation | 1 | 197 | Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. |

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
- Basis: `ccps-management-of-change`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `ccps-management-of-change moc change-control psm temporary-change pre-startup-review HAZOP cause consequence safeguard recommendation`
- `ccps-management-of-change PSM/MOC/documentation missing basis project criteria data assumptions`
- `ccps-management-of-change AutoHAZOP node deviation scenario review quality gate`
- `ccps-management-of-change evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `process-safety-management-rbps-moc-docs` and secondary skills none when the decision requires a specialist workflow.

# Field Manual - CCPS Guidelines for Investigating Chemical Process Incidents

This is the dense working reference for `book-ccps-investigating-chemical-process-incidents`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `ccps-investigating-chemical-process-incidents`
- Domain family: `incident`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 455
- Usable text pages indexed: 455
- Indexed text characters: 895048
- Top evidence signals: Incident/human factors:891, PSM/MOC/documentation:158, Fire/explosion:97, QRA/risk criteria:63, HAZOP/PHA:48, Relief/effluent:36
- Primary shared skill: `incident-learning-root-cause-human-error`
- Secondary shared skills: none
- Source purpose: Use the source to improve causal reasoning, human factors, and learning from prior incidents.

## Source Navigation Hooks

- No reliable outline hooks were available from the current extraction.

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 448 | 17 | incident_human, qra_risk, fire_explosion, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 454 | 16 | incident_human, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 8 | 15 | lopa_ipl, hazop_pha, qra_risk, psm_moc_docs, incident_human, reliability, fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 453 | 14 | incident_human, psm_moc_docs, qra_risk, fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 450 | 14 | incident_human, inherent_siting, fire_explosion, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 433 | 14 | incident_human, fire_explosion, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 447 | 13 | incident_human, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 299 | 13 | incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 449 | 13 | incident_human, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 73 | 13 | qra_risk, incident_human, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 446 | 13 | incident_human, consequence, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 76 | 12 | incident_human, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 3-6, 8, 10, 12-19, 21-56, 58-63, 65-66, 68-80, 82-84, 87-88, 90-94, 96, 98-104, 106, .... Treat these pages as navigation anchors, not final proof.
- PSM/MOC/documentation: Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. Evidence pages: 3, 8-10, 16-17, 24-25, 27, 31-32, 35, 39, 43-44, 46, 49-52, 54, 58, 62, .... Treat these pages as navigation anchors, not final proof.
- Fire/explosion: Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. Evidence pages: 7-9, 14, 18, 38, 117, 123-124, 133-134, 137, 140, 143, 149, 153, 155, 158, .... Treat these pages as navigation anchors, not final proof.
- QRA/risk criteria: Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. Evidence pages: 7-8, 14, 53, 62, 65, 69, 71-73, 77, 199, 214, 216, 234, 243, 249, .... Treat these pages as navigation anchors, not final proof.
- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 8-9, 53-54, 60, 65-66, 69, 73, 75, 190, 216, 229, 234, 261, 263, 279, .... Treat these pages as navigation anchors, not final proof.
- Relief/effluent: Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. Evidence pages: 9, 38, 83-85, 88, 99, 141-142, 153, 181, 183, 185, 200, 271, 321-322, 353, .... Treat these pages as navigation anchors, not final proof.

## How To Attack A HAZOP Row

1. Match the row to the strongest topic signal above.
2. State whether this book is primary evidence, secondary support, or screening-only for the decision.
3. Rewrite the cause to name the failed item, failure mode, human/organizational condition, external event, or initiating event.
4. Rewrite the consequence as the unmitigated event path before safeguards.
5. Challenge every safeguard for independence, timing, effectiveness, auditability, and evidence.
6. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- Is the cause immediate technical failure, human action, latent organizational weakness, degraded barrier, or management-system failure?
- Does the recommendation change conditions or only ask people to be more careful?
- What barrier failed, why was it allowed to degrade, and how will recurrence be detected?
- Could design simplification, automation, physical constraint, procedure redesign, training, or audit make the action more robust?

## Anti-Patterns To Kill

- Blame-only causes such as 'operator error' without task, interface, procedure, or management-system context.
- Lessons learned that are not converted into durable controls.
- Actions that depend on memory, vigilance, or informal knowledge.

## Row Moves

- Rewrite human-error causes into system conditions and failed barriers.
- Add recurrence-prevention evidence: design change, procedure change, training verification, audit, or KPI.
- Use incident patterns to ask sharper questions without asserting plant-specific facts.

## Hard Decision Gates

- Whether a cause is a direct technical failure, human action, latent organizational weakness, or degraded barrier.
- Whether a recommendation changes the system rather than only reminding people to be careful.
- Whether repeat-event learning, design-for-error, maintenance, procedure, or supervision gaps are visible.

## Missing-Basis Triggers

- Incident evidence and timeline
- Barrier failure analysis
- Human factors/task analysis
- Management-system causal evidence
- Action effectiveness verification
- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Specialist Handoff

- Hand off to `incident-learning-root-cause-human-error` when the row needs the primary shared workflow.
- No secondary shared skill is configured; use the primary shared skill or project SME handoff when needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

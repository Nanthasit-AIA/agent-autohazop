# Field Manual - Lessons from Disaster

This is the dense working reference for `book-lessons-from-disaster`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `lessons-from-disaster`
- Domain family: `incident`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 192
- Usable text pages indexed: 192
- Indexed text characters: 394538
- Top evidence signals: Incident/human factors:184, Fire/explosion:98, Consequence analysis:43, HAZOP/PHA:31, Relief/effluent:22, Inherent safety/siting:20
- Primary shared skill: `incident-learning-root-cause-human-error`
- Secondary shared skills: none
- Source purpose: Use the source to improve causal reasoning, human factors, and learning from prior incidents.

## Source Navigation Hooks

- No reliable outline hooks were available from the current extraction.

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 112 | 14 | hazop_pha, qra_risk, consequence, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 116 | 9 | incident_human, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 115 | 9 | incident_human, consequence, fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 21 | 8 | fire_explosion, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 186 | 8 | hazop_pha, relief_effluent, consequence, qra_risk, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 107 | 7 | psm_moc_docs, consequence, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 17 | 7 | fire_explosion, relief_effluent, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 84 | 7 | relief_effluent, fire_explosion, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 126 | 7 | hazop_pha, incident_human, qra_risk, fire_explosion, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 75 | 7 | incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 6 | 7 | incident_human, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 111 | 6 | qra_risk, hazop_pha, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 3, 6, 9, 11, 13-15, 21, 23, 26, 29-31, 39-40, 44, 50, 64-65, 67, .... Treat these pages as navigation anchors, not final proof.
- Fire/explosion: Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. Evidence pages: 5, 12-13, 15, 17, 19-22, 28-30, 32-34, 39, 49-50, 53-54, 57-58, 60-62, 67-68, 84-85, .... Treat these pages as navigation anchors, not final proof.
- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 12-13, 19-20, 22, 38-39, 49, 53, 62, 64, 85, 91, 93-94, 106-107, 112, 115-116, .... Treat these pages as navigation anchors, not final proof.
- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 44, 90, 98, 110-112, 126, 136, 138, 150, 166, 172, 186. Treat these pages as navigation anchors, not final proof.
- Relief/effluent: Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. Evidence pages: 17-19, 36, 49, 62, 84-87, 100, 107, 109, 147, 157, 165, 186. Treat these pages as navigation anchors, not final proof.
- Inherent safety/siting: Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. Evidence pages: 6, 17, 91-93, 95, 98, 167-168, 171, 184-185, 187. Treat these pages as navigation anchors, not final proof.

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

# Field Manual - An Engineer's View of Human Error

This is the dense working reference for `book-engineers-view-human-error`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `engineers-view-human-error`
- Domain family: `incident`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 293
- Usable text pages indexed: 293
- Indexed text characters: 567561
- Top evidence signals: Incident/human factors:418, Fire/explosion:43, Inherent safety/siting:32, HAZOP/PHA:28, Relief/effluent:26, Consequence analysis:23
- Primary shared skill: `incident-learning-root-cause-human-error`
- Secondary shared skills: none
- Source purpose: Use the source to improve causal reasoning, human factors, and learning from prior incidents.

## Source Navigation Hooks

- No reliable outline hooks were available from the current extraction.

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 98 | 11 | incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 49 | 11 | incident_human, security, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 126 | 10 | fire_explosion, consequence, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 32 | 9 | incident_human, relief_effluent, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 239 | 8 | incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 162 | 8 | reliability, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 144 | 8 | incident_human, reliability, qra_risk, fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 4 | 8 | incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 9 | 8 | incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 14 | 7 | incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 20 | 7 | incident_human, hazop_pha, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 266 | 7 | incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 1-2, 4-6, 8-9, 11-16, 18, 20-22, 24, 26-29, 32-34, 36, 38-42, 44, 46-53, 55-59, .... Treat these pages as navigation anchors, not final proof.
- Fire/explosion: Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. Evidence pages: 42, 44, 59, 66, 73, 76, 78, 83, 92, 102, 107, 112, 116, 121, .... Treat these pages as navigation anchors, not final proof.
- Inherent safety/siting: Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. Evidence pages: 5, 20, 39, 47-50, 64, 79, 81, 87, 91-92, 96, 127, 133, 159, 163, .... Treat these pages as navigation anchors, not final proof.
- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 20, 73-74, 107, 164, 167, 172, 175, 177-178, 218-219, 221-222, 225, 244, 274, 288. Treat these pages as navigation anchors, not final proof.
- Relief/effluent: Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. Evidence pages: 32-33, 57, 63, 65, 67, 69-70, 103, 117, 147, 168, 171, 202, 219, 237, .... Treat these pages as navigation anchors, not final proof.
- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 32, 40, 72, 77, 125-128, 133, 138, 164, 183, 198, 200, 202-203, 206, 227, .... Treat these pages as navigation anchors, not final proof.

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

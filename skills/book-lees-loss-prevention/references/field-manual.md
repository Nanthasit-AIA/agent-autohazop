# Field Manual - Lees' Loss Prevention in the Process Industries

This is the dense working reference for `book-lees-loss-prevention`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `lees-loss-prevention`
- Domain family: `loss_prevention`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 1468
- Usable text pages indexed: 1465
- Indexed text characters: 6019021
- Top evidence signals: Consequence analysis:2397, Fire/explosion:1122, Incident/human factors:975, Relief/effluent:971, Inherent safety/siting:460, QRA/risk criteria:427
- Primary shared skill: `hazop-hazan-study-leader`
- Secondary shared skills: `relief-effluent-fire-explosion-consequence`, `risk-criteria-qra`
- Source purpose: Use the source as a routing and integration layer across hazard identification, assessment, and control.

## Source Navigation Hooks

- No reliable outline hooks were available from the current extraction.

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 28 | 62 | consequence, incident_human, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 460 | 60 | consequence, fire_explosion, relief_effluent, qra_risk, inherent_siting, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 442 | 47 | inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 612 | 45 | relief_effluent, fire_explosion, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 809 | 43 | consequence, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 610 | 42 | relief_effluent, consequence, fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 30 | 42 | fire_explosion, relief_effluent, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 806 | 32 | incident_human, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 609 | 32 | relief_effluent, psm_moc_docs, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 614 | 31 | relief_effluent, consequence, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 929 | 30 | consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 261 | 28 | hazop_pha, qra_risk, fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 9-11, 13, 15-16, 25, 27-32, 42-43, 47, 55, 59-65, 67, 71-72, 81-85, 88, 94, .... Treat these pages as navigation anchors, not final proof.
- Fire/explosion: Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. Evidence pages: 10, 13, 15-16, 21, 25, 27, 29-30, 32, 35-37, 40, 42-43, 47, 53-55, 63-68, .... Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 9-11, 13, 15-17, 19, 25-28, 32-33, 37-38, 42-43, 45, 47-49, 55-64, 68, 74, 78, .... Treat these pages as navigation anchors, not final proof.
- Relief/effluent: Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. Evidence pages: 9-10, 13, 16, 27-28, 30-31, 33, 42, 45, 64-65, 70-73, 84, 129, 145-146, 158, .... Treat these pages as navigation anchors, not final proof.
- Inherent safety/siting: Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. Evidence pages: 9-10, 13, 16, 26-27, 31, 33, 37, 45-47, 59, 72-73, 101-103, 121-123, 129, 132, .... Treat these pages as navigation anchors, not final proof.
- QRA/risk criteria: Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. Evidence pages: 13, 26, 33, 37, 47, 55-56, 90-92, 97-98, 101, 105, 114, 116-118, 123, 125, .... Treat these pages as navigation anchors, not final proof.

## How To Attack A HAZOP Row

1. Match the row to the strongest topic signal above.
2. State whether this book is primary evidence, secondary support, or screening-only for the decision.
3. Rewrite the cause to name the failed item, failure mode, human/organizational condition, external event, or initiating event.
4. Rewrite the consequence as the unmitigated event path before safeguards.
5. Challenge every safeguard for independence, timing, effectiveness, auditability, and evidence.
6. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- Which specialist discipline owns the next technical decision?
- Is this broad guidance enough for screening, or does the row need narrower HAZOP, LOPA/SIS, relief, QRA, reliability, PSM, incident, or siting evidence?
- Are prevention, protection, mitigation, emergency response, and management-system controls balanced?
- What project basis or calculation would turn this from useful guidance into accepted evidence?

## Anti-Patterns To Kill

- Using a broad reference to justify a narrow quantitative or design-specific decision.
- Letting a general recommendation hide the specialist check that is actually needed.
- Treating coverage breadth as evidence depth.

## Row Moves

- Route the row to the correct specialist skill before accepting final credit.
- Use broad loss-prevention logic to find missing controls and handoffs.
- Keep recommendations tied to the specific node/deviation/cause/consequence path.

## Hard Decision Gates

- Which specialist discipline should own the next check: HAZOP, LOPA/SIS, relief, QRA, reliability, PSM, incident learning, or siting.
- Whether a broad loss-prevention claim needs a narrower source before it can support a decision.
- Whether recommendations are balanced across prevention, protection, mitigation, emergency response, and management systems.

## Missing-Basis Triggers

- Specialist discipline owner
- Narrower source or calculation basis
- Project standard/criterion
- Scenario-specific evidence
- Verification and closure plan
- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Specialist Handoff

- Hand off to `hazop-hazan-study-leader` when the row needs the primary shared workflow.
- Hand off to `relief-effluent-fire-explosion-consequence`, `risk-criteria-qra` when those secondary workflows are needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

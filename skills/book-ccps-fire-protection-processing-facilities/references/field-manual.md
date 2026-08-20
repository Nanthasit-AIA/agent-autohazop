# Field Manual - CCPS Fire Protection in Processing Facilities

This is the dense working reference for `book-ccps-fire-protection-processing-facilities`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `ccps-fire-protection-processing-facilities`
- Domain family: `consequence`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 471
- Usable text pages indexed: 471
- Indexed text characters: 953878
- Top evidence signals: Fire/explosion:970, Consequence analysis:382, Inherent safety/siting:215, PSM/MOC/documentation:93, Relief/effluent:79, QRA/risk criteria:69
- Primary shared skill: `relief-effluent-fire-explosion-consequence`
- Secondary shared skills: `inherently-safer-siting-layout`
- Source purpose: Use the source to strengthen release, relief, fire/explosion, and consequence-screening logic.

## Source Navigation Hooks

- Acronyms
- 00con
- 1. Introduction
- 2. Management Overview
- 3. Fire Protection Strategy
- 4. Overview of Fire Prevention Elements
- 5. Fire Hazard Analysis
- 6. Fire Risk Assessment
- 7. Fire Protection Fundamentals
- 8. Specific Design Guidance
- 9. Installation of Fire Protection Systems
- 10. Inspection, Testing, and Maintenance
- 11. Fire Emergency Response
- Appendix A: Case Histories
- Appendix B: Understanding Fires
- Appendix C: Computer Tools for Design
- Appendix D: Sample Fire Pre-Plan
- 1.1 Scope

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 158 | 29 | inherent_siting, fire_explosion, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 441 | 28 | fire_explosion, relief_effluent, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 442 | 27 | fire_explosion, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 122 | 23 | qra_risk, fire_explosion, reliability, lopa_ipl, consequence, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 49 | 21 | inherent_siting, fire_explosion, psm_moc_docs, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 157 | 21 | inherent_siting, consequence, fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 44 | 20 | inherent_siting, fire_explosion, hazop_pha, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 48 | 19 | psm_moc_docs, fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 143 | 17 | relief_effluent, fire_explosion, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 443 | 16 | fire_explosion, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 38 | 16 | fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 359 | 16 | fire_explosion, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- Fire/explosion: Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. Evidence pages: 1-3, 5-10, 12-21, 23-45, 47-49, 53, 55-60, 62-63, 66-68, 70-72, 74, 76-82, 84, 87-95, .... Treat these pages as navigation anchors, not final proof.
- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 11, 13, 39, 49-52, 55-56, 58-59, 68, 71, 73-74, 76-82, 85-86, 90, 92, 94, .... Treat these pages as navigation anchors, not final proof.
- Inherent safety/siting: Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. Evidence pages: 10-11, 13, 23, 37, 39, 42, 44, 46, 49, 59-60, 116, 119, 136, 138, .... Treat these pages as navigation anchors, not final proof.
- PSM/MOC/documentation: Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. Evidence pages: 3, 8, 10-11, 15, 23, 40, 43-49, 58, 60, 62, 75, 119, 143, 346-347, .... Treat these pages as navigation anchors, not final proof.
- Relief/effluent: Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. Evidence pages: 71, 80, 106-107, 141-143, 197, 210, 223, 245, 253-254, 264-265, 274, 284, 305-306, 312, .... Treat these pages as navigation anchors, not final proof.
- QRA/risk criteria: Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. Evidence pages: 71-73, 76, 117, 122, 124, 128-132, 134-135, 424, 434, 440, 443, 449, 452-456, 469. Treat these pages as navigation anchors, not final proof.

## How To Attack A HAZOP Row

1. Match the row to the strongest topic signal above.
2. State whether this book is primary evidence, secondary support, or screening-only for the decision.
3. Rewrite the cause to name the failed item, failure mode, human/organizational condition, external event, or initiating event.
4. Rewrite the consequence as the unmitigated event path before safeguards.
5. Challenge every safeguard for independence, timing, effectiveness, auditability, and evidence.
6. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- What is the material, phase, inventory, pressure, temperature, isolation state, release path, and release duration?
- Is the consequence toxic, flammable, thermal radiation, overpressure, environmental, equipment damage, or business interruption?
- Are source term, endpoint criteria, relief capacity, flare/effluent limits, and escalation assumptions documented?
- Does the safeguard prevent the event, reduce release size, mitigate consequence, or only support emergency response?

## Anti-Patterns To Kill

- Jumping to severity without source-term or endpoint basis.
- Crediting relief/flare/emergency response without capacity, destination, or design-basis evidence.
- Treating fire/explosion protection as prevention when it only mitigates consequences.

## Row Moves

- State the unmitigated release/consequence path before listing safeguards.
- Turn weak consequence claims into specific calculation or design-basis requests.
- Separate prevention, protection, mitigation, escalation control, and emergency response.

## Hard Decision Gates

- Whether the source term, material state, inventory, pressure/temperature, and release path are defined.
- Whether relief, flare/effluent, dispersion, fire, explosion, toxic, or environmental consequence assumptions are supported.
- Whether escalation and emergency response claims are engineering controls, safeguards, or only mitigations.

## Missing-Basis Triggers

- Material properties and inventory
- Relief/design basis and capacity calculation
- Release scenario/source-term basis
- Dispersion/fire/explosion/toxic endpoint criteria
- Flare/effluent/disposal system basis
- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Specialist Handoff

- Hand off to `relief-effluent-fire-explosion-consequence` when the row needs the primary shared workflow.
- Hand off to `inherently-safer-siting-layout` when those secondary workflows are needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

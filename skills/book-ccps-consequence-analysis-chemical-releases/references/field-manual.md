# Field Manual - CCPS Consequence Analysis of Chemical Releases

This is the dense working reference for `book-ccps-consequence-analysis-chemical-releases`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `ccps-consequence-analysis-chemical-releases`
- Domain family: `consequence`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 348
- Usable text pages indexed: 348
- Indexed text characters: 591403
- Top evidence signals: Consequence analysis:553, Fire/explosion:501, Relief/effluent:200, QRA/risk criteria:46, Incident/human factors:20, Reliability data:16
- Primary shared skill: `relief-effluent-fire-explosion-consequence`
- Secondary shared skills: none
- Source purpose: Use the source to strengthen release, relief, fire/explosion, and consequence-screening logic.

## Source Navigation Hooks

- Guidelines for Consequence Analysis of Chemical Releases
- 1989 CPQRA Guidelines Acknowledgments
- Acronyms
- 1. Introduction
- 1.1 CPQRA Definitions
- 1.2 Consequence Analysis
- 2. Source Models
- 2.1 Discharge Rate Models
- 2.1.1 Background
- 2.1.2 Description
- 2.1.3 Example Problems
- 2.1.4 Discussion
- 2.2 Flash and Evaporation
- 2.2.1 Background
- 2.2.2 Description
- 2.2.3 Example Problems
- 2.2.4 Discussion
- 2.3 Dispersion Models

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 23 | 19 | consequence, fire_explosion, lopa_ipl, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 174 | 17 | fire_explosion, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 314 | 17 | fire_explosion, consequence, qra_risk, relief_effluent, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 173 | 17 | fire_explosion, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 202 | 17 | fire_explosion, consequence, relief_effluent, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 343 | 16 | fire_explosion, consequence, relief_effluent, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 144 | 16 | fire_explosion, relief_effluent, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 321 | 16 | fire_explosion, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 266 | 15 | consequence, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 146 | 15 | fire_explosion, consequence, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 287 | 15 | relief_effluent, fire_explosion, qra_risk, incident_human, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 308 | 15 | consequence, reliability, qra_risk, relief_effluent, fire_explosion, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 1-5, 7-15, 17-18, 20, 22-33, 35, 53-55, 72-74, 76, 84, 91-95, 98-133, 136-138, 140-146, .... Treat these pages as navigation anchors, not final proof.
- Fire/explosion: Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. Evidence pages: 4, 9, 11-12, 14-15, 18-19, 22-27, 54, 69, 129, 142-151, 155-156, 161-162, 164-169, 172-179, .... Treat these pages as navigation anchors, not final proof.
- Relief/effluent: Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. Evidence pages: 4, 19, 23, 25, 27, 32-33, 50, 54-55, 69-70, 78, 144, 146, 150-155, 157-160, .... Treat these pages as navigation anchors, not final proof.
- QRA/risk criteria: Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. Evidence pages: 3-5, 7, 9-10, 17, 19-20, 24, 287, 303-305, 307-310, 313-314, 317-318, 329, 333-334. Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 10, 18, 20, 25, 117, 149, 201-202, 265, 287, 307-310, 341-343. Treat these pages as navigation anchors, not final proof.
- Reliability data: Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. Evidence pages: 7, 10-11, 296, 305, 307-309, 311-312. Treat these pages as navigation anchors, not final proof.

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
- No secondary shared skill is configured; use the primary shared skill or project SME handoff when needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

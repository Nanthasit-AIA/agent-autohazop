# Field Manual - CCPS VCE, Flash Fire and BLEVE Characteristics

This is the dense working reference for `book-ccps-vce-flash-fire-bleve`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `ccps-vce-flash-fire-bleve`
- Domain family: `consequence`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 402
- Usable text pages indexed: 394
- Indexed text characters: 693640
- Top evidence signals: Fire/explosion:683, Relief/effluent:248, Consequence analysis:149, Incident/human factors:56, Inherent safety/siting:10, HAZOP/PHA:3
- Primary shared skill: `relief-effluent-fire-explosion-consequence`
- Secondary shared skills: none
- Source purpose: Use the source to strengthen release, relief, fire/explosion, and consequence-screening logic.

## Source Navigation Hooks

- No reliable outline hooks were available from the current extraction.

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 396 | 19 | fire_explosion, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 168 | 18 | fire_explosion, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 58 | 17 | consequence, fire_explosion, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 15 | 14 | consequence, relief_effluent, fire_explosion, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 14 | 14 | fire_explosion, relief_effluent, consequence, incident_human, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 399 | 13 | fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 158 | 12 | fire_explosion, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 258 | 11 | fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 317 | 11 | fire_explosion, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 236 | 10 | fire_explosion, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 235 | 10 | fire_explosion, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 123 | 10 | fire_explosion, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- Fire/explosion: Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. Evidence pages: 4, 6-10, 14-20, 22-23, 25-28, 30-37, 39, 41-42, 44, 46-47, 51-52, 54, 56-59, 62-63, .... Treat these pages as navigation anchors, not final proof.
- Relief/effluent: Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. Evidence pages: 7-8, 14-15, 31, 34, 46-47, 54, 68-70, 80-81, 83-85, 88-91, 94-96, 104-105, 107, 112, .... Treat these pages as navigation anchors, not final proof.
- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 6-9, 12-20, 22, 35, 56, 58-61, 70, 78, 80, 82, 86, 102, 122-124, 126-127, .... Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 9, 12-15, 21, 23, 30-32, 35-37, 39, 41-42, 44-45, 50-51, 54, 56-58, 99-100, 128, .... Treat these pages as navigation anchors, not final proof.
- Inherent safety/siting: Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. Evidence pages: 14, 34, 40, 45, 48, 80, 139, 264, 277. Treat these pages as navigation anchors, not final proof.
- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 234, 254-255. Treat these pages as navigation anchors, not final proof.

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

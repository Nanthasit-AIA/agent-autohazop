# Field Manual - CCPS Guidelines for Risk Based Process Safety

This is the dense working reference for `book-ccps-risk-based-process-safety`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `ccps-risk-based-process-safety`
- Domain family: `psm`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 708
- Usable text pages indexed: 708
- Indexed text characters: 1673593
- Top evidence signals: PSM/MOC/documentation:1794, Incident/human factors:352, Fire/explosion:65, HAZOP/PHA:57, Consequence analysis:57, SIS/SIL:30
- Primary shared skill: `process-safety-management-rbps-moc-docs`
- Secondary shared skills: none
- Source purpose: Use the source to turn technical gaps into auditable process-safety management actions.

## Source Navigation Hooks

- 08a
- 08b
- 12a
- 12b

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 439 | 30 | psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 447 | 27 | psm_moc_docs, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 613 | 27 | psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 433 | 23 | psm_moc_docs, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 616 | 21 | psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 617 | 20 | psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 609 | 19 | psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 623 | 19 | psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 450 | 18 | psm_moc_docs, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 59 | 17 | psm_moc_docs, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 214 | 17 | psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 454 | 17 | psm_moc_docs, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- PSM/MOC/documentation: Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. Evidence pages: 3-7, 9-18, 20-31, 33, 35-37, 39, 41, 43, 45, 47, 49, 51-63, 65-85, 88, .... Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 5, 7-11, 13-14, 16-18, 23-26, 47-48, 52, 54-55, 57-59, 63, 69-74, 79-80, 84, 87, .... Treat these pages as navigation anchors, not final proof.
- Fire/explosion: Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. Evidence pages: 8-9, 15, 87, 89, 115, 119, 134, 180-181, 187, 200, 217, 219-220, 243, 255, .... Treat these pages as navigation anchors, not final proof.
- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 7, 9, 11, 18, 92, 150, 190, 192, 195, 202, 213, 220-221, 240, 245-246, .... Treat these pages as navigation anchors, not final proof.
- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 14, 76, 119, 135, 187, 189, 233, 245, 264, 285, 296, 310, 334, 338, .... Treat these pages as navigation anchors, not final proof.
- SIS/SIL: Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. Evidence pages: 10, 334-335, 350, 365, 372, 706-707. Treat these pages as navigation anchors, not final proof.

## How To Attack A HAZOP Row

1. Match the row to the strongest topic signal above.
2. State whether this book is primary evidence, secondary support, or screening-only for the decision.
3. Rewrite the cause to name the failed item, failure mode, human/organizational condition, external event, or initiating event.
4. Rewrite the consequence as the unmitigated event path before safeguards.
5. Challenge every safeguard for independence, timing, effectiveness, auditability, and evidence.
6. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- Is the gap technical, procedural, training, MOC, PSSR, PSI, mechanical integrity, audit, emergency management, or action tracking?
- What record or deliverable would prove the gap is closed?
- Does the recommendation name owner, acceptance criteria, due trigger, and verification evidence?
- Would a future HAZOP/LOPA reviewer be able to trace the decision from the retained documentation?

## Anti-Patterns To Kill

- Recommendations that say 'review/update' with no deliverable.
- Treating missing process safety information as an acceptable assumption.
- Closing actions without evidence that controls were implemented and remain auditable.

## Row Moves

- Translate technical uncertainty into a named process-safety management deliverable.
- Trigger MOC/PSSR when design, operating envelope, procedure, alarm, trip, relief, or equipment service changes.
- Tie every management-system action back to the specific scenario and consequence.

## Hard Decision Gates

- Whether the gap is PSI, procedure, training, MOC, PSSR, mechanical integrity, emergency management, audit, or action tracking.
- Whether a recommendation names an accountable management-system deliverable.
- Whether documentation is sufficient to support later HAZOP/LOPA/SIS decisions.

## Missing-Basis Triggers

- Process safety information
- Operating procedure/training record
- MOC/PSSR evidence
- Inspection/test/maintenance record
- Audit/action-tracking closure evidence
- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Specialist Handoff

- Hand off to `process-safety-management-rbps-moc-docs` when the row needs the primary shared workflow.
- No secondary shared skill is configured; use the primary shared skill or project SME handoff when needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

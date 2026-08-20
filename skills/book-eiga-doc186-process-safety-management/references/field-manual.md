# Field Manual - EIGA Doc 186 - Process Safety Management

This is the dense working reference for `book-eiga-doc186-process-safety-management`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `eiga-doc186-process-safety-management`
- Domain family: `psm`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 27
- Usable text pages indexed: 27
- Indexed text characters: 62166
- Top evidence signals: PSM/MOC/documentation:91, Incident/human factors:18, HAZOP/PHA:3, Inherent safety/siting:2, Fire/explosion:1
- Primary shared skill: `process-safety-management-rbps-moc-docs`
- Secondary shared skills: none
- Source purpose: Use the source to turn technical gaps into auditable process-safety management actions.

## Source Navigation Hooks

- 1 Introduction
- 2 Scope and purpose
- 2.1 Scope
- 2.2 Purpose
- 3 Definitions
- 3.1 Publication terminology
- 3.1.1 Shall
- 3.1.2 Should
- 3.1.3 May
- 3.1.4 Will
- 3.1.5 Can
- 3.2 Technical definitions
- 3.2.1 Work control
- 4 Overview of process safety management elements
- 4.1 Process safety leadership
- 4.2 Risk identification and assessment
- 4.3 Risk management
- 4.4 Review and improvement

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 24 | 13 | psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 5 | 11 | psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 27 | 10 | psm_moc_docs, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 26 | 9 | psm_moc_docs, incident_human, fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 12 | 8 | psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 23 | 8 | psm_moc_docs, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 3 | 7 | psm_moc_docs, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 4 | 6 | psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 8 | 5 | psm_moc_docs, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 16 | 5 | psm_moc_docs, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 25 | 4 | psm_moc_docs, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 6 | 4 | psm_moc_docs, hazop_pha, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- PSM/MOC/documentation: Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. Evidence pages: 2-18, 23-27. Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 3, 6, 8, 10, 13, 22-23, 25-27. Treat these pages as navigation anchors, not final proof.
- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 6, 15-16. Treat these pages as navigation anchors, not final proof.
- Inherent safety/siting: Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. Evidence pages: 11, 19. Treat these pages as navigation anchors, not final proof.
- Fire/explosion: Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. Evidence pages: 26. Treat these pages as navigation anchors, not final proof.

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

# Field Manual - HAZOP Guide to Best Practice

This is the dense working reference for `book-hazop-guide-best-practice`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `hazop-guide-best-practice`
- Domain family: `hazop`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 184
- Usable text pages indexed: 168
- Indexed text characters: 257720
- Top evidence signals: HAZOP/PHA:490, Incident/human factors:52, PSM/MOC/documentation:48, SIS/SIL:28, LOPA/IPL:27, Inherent safety/siting:12
- Primary shared skill: `hazop-hazan-study-leader`
- Secondary shared skills: none
- Source purpose: Use the source to improve HAZOP study discipline and worksheet quality.

## Source Navigation Hooks

- Title page
- Copyright
- Foreword
- Foreword To Third Edition
- Foreword to Earlier Editions
- Chapter 1. Introduction
- 1.1 Aims and Objectives
- 1.2 Essential Features of HAZOP Study
- Chapter 2. Process Hazard Studies
- 2.1 HS 1-Concept Stage Hazard Review
- 2.2 HS 2-HAZID at Front-End Engineering Design (FEED) or Project Definition Stage
- 2.3 HS 3-Detailed Design Hazard Study
- 2.4 HS 4-Construction/Design Verification
- 2.5 HS 5-Pre-Commissioning Safety Review
- 2.6 HS 6-Project Close-Out/Post Start-Up Review
- 2.7 HS 0-Consideration of Inherently Safer or Less Polluting Systems
- 2.8 HS 7-Demolition/Abandonment Reviews
- 2.9 Overview of Hazard Studies

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 91 | 20 | lopa_ipl, hazop_pha, sis_sil, fire_explosion, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 78 | 19 | hazop_pha, incident_human, lopa_ipl | Use as a source-navigation anchor; verify before numeric/design claims. |
| 171 | 15 | incident_human, hazop_pha, lopa_ipl, sis_sil, fire_explosion, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 90 | 13 | hazop_pha, lopa_ipl, incident_human, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 97 | 12 | hazop_pha, consequence, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 11 | 12 | hazop_pha, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 32 | 11 | hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 170 | 11 | hazop_pha, sis_sil, inherent_siting, lopa_ipl | Use as a source-navigation anchor; verify before numeric/design claims. |
| 93 | 10 | hazop_pha, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 17 | 10 | hazop_pha, psm_moc_docs, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 80 | 9 | sis_sil, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 98 | 9 | hazop_pha, fire_explosion, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 2, 4-8, 11-12, 16-22, 24-25, 27-30, 32-41, 43, 45-64, 66-72, 74-98, 100-103, 105-112, 114-119, .... Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 6, 11, 17, 19, 21, 28, 35, 53, 58, 64, 78, 82, 85-86, 88-90, .... Treat these pages as navigation anchors, not final proof.
- PSM/MOC/documentation: Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. Evidence pages: 6, 17, 21, 39, 47, 59, 61, 63-64, 66-67, 69-73, 76-77, 83-84, 93-94, 98, .... Treat these pages as navigation anchors, not final proof.
- SIS/SIL: Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. Evidence pages: 25, 63, 77, 80-81, 91, 105, 169-171, 175, 179, 183. Treat these pages as navigation anchors, not final proof.
- LOPA/IPL: Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. Evidence pages: 6, 78, 90-92, 168, 170-171, 178, 180. Treat these pages as navigation anchors, not final proof.
- Inherent safety/siting: Prefer eliminate, substitute, minimize, moderate, simplify, and challenge layout/exposure. Evidence pages: 5, 23, 41, 66, 86, 96, 160, 170, 180. Treat these pages as navigation anchors, not final proof.

## How To Attack A HAZOP Row

1. Match the row to the strongest topic signal above.
2. State whether this book is primary evidence, secondary support, or screening-only for the decision.
3. Rewrite the cause to name the failed item, failure mode, human/organizational condition, external event, or initiating event.
4. Rewrite the consequence as the unmitigated event path before safeguards.
5. Challenge every safeguard for independence, timing, effectiveness, auditability, and evidence.
6. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- Is the node boundary tight enough to know what equipment, utilities, recycle, vent, drain, and relief paths are included?
- Does the deviation combine one guide word with one process parameter and one credible abnormal state?
- Does the cause name a failed item/failure mode instead of vague wording such as 'equipment failure'?
- Is the consequence written as the unmitigated path before safeguards are credited?

## Anti-Patterns To Kill

- Rows that mix several initiating events, safeguards, or consequences into one line.
- Recommendations that say 'review' without naming acceptance criteria or evidence to produce.
- Safeguards copied from design intent without checking effectiveness for the specific cause.

## Row Moves

- Rewrite generic causes into equipment + failure mode + condition.
- Separate normal control, alarms, trips, relief, procedures, passive design, and emergency response.
- Turn vague actions into basis requests: design basis, relief basis, alarm response time, procedure, inspection, or interlock logic.

## Hard Decision Gates

- Whether the node boundary and design intent are specific enough for the selected deviation.
- Whether each row has one initiating cause, one unmitigated consequence path, and correctly separated safeguards.
- Whether a recommendation closes a real gap instead of restating normal design intent.

## Missing-Basis Triggers

- Node boundary and design intent
- Normal operating envelope
- P&ID/process graph context
- Safeguard design basis
- Relief/alarm/interlock/procedure evidence
- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Specialist Handoff

- Hand off to `hazop-hazan-study-leader` when the row needs the primary shared workflow.
- No secondary shared skill is configured; use the primary shared skill or project SME handoff when needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

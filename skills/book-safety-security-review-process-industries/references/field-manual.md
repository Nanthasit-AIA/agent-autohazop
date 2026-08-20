# Field Manual - Safety and Security Review for Process Industries

This is the dense working reference for `book-safety-security-review-process-industries`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `safety-security-review-process-industries`
- Domain family: `hazop`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 186
- Usable text pages indexed: 185
- Indexed text characters: 295359
- Top evidence signals: HAZOP/PHA:1021, Security review:163, SIS/SIL:68, PSM/MOC/documentation:63, LOPA/IPL:40, Relief/effluent:35
- Primary shared skill: `hazop-hazan-study-leader`
- Secondary shared skills: `process-safety-security-review`
- Source purpose: Use the source to improve HAZOP study discipline and worksheet quality.

## Source Navigation Hooks

- Front Cover
- Safety and Security Review for the Process Industries
- Copyright Page
- Contents
- About the Author
- List of Acronyms
- Notice
- 1 Purpose
- 2 Scope
- 3 Objective and Description of PHA, What-If, and HAZOP Reviews
- 3.1 Definition
- 3.2 Objectives
- 3.3 Origins of Qualitative Safety Reviews
- 3.4 Limitations and Disadvantages
- 3.4.1 Limitations
- 3.4.1.1 Preliminary Hazard Analysis
- 3.4.1.2 What-If Reviews
- 3.4.1.3 HAZOP Reviews

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 151 | 47 | hazop_pha, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 150 | 40 | hazop_pha, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 142 | 40 | hazop_pha, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 154 | 38 | hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 144 | 37 | hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 146 | 36 | hazop_pha, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 148 | 36 | hazop_pha, relief_effluent, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 155 | 35 | hazop_pha, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 147 | 35 | hazop_pha, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 149 | 33 | hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 143 | 33 | hazop_pha, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 153 | 33 | hazop_pha, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 4, 6-8, 12, 16-17, 20, 23-37, 39, 48, 50, 52-53, 61-63, 66-72, 74, 77, .... Treat these pages as navigation anchors, not final proof.
- Security review: Add intentional-event, vulnerability, access-control, and cyber/physical interface prompts where relevant. Evidence pages: 4, 6-7, 12, 17, 20, 22, 24-26, 33-36, 45-46, 48, 50, 53-55, 61-63, 66-67, .... Treat these pages as navigation anchors, not final proof.
- SIS/SIL: Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. Evidence pages: 6, 12, 17, 27, 36, 38-43, 66, 176-177, 181, 184-185. Treat these pages as navigation anchors, not final proof.
- PSM/MOC/documentation: Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. Evidence pages: 7-8, 17, 20, 22, 25, 29, 33, 54-55, 72, 74-76, 79, 86, 98, 106, .... Treat these pages as navigation anchors, not final proof.
- LOPA/IPL: Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. Evidence pages: 12, 16, 27, 36, 39-43, 45, 66, 171, 181, 185. Treat these pages as navigation anchors, not final proof.
- Relief/effluent: Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. Evidence pages: 39-40, 77, 84, 102, 109, 142-143, 146-148, 150-152, 162-163, 166, 169. Treat these pages as navigation anchors, not final proof.

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
- Hand off to `process-safety-security-review` when those secondary workflows are needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

# Field Manual - CCPS Hazard Evaluation Procedures

This is the dense working reference for `book-ccps-hazard-evaluation-procedures`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `ccps-hazard-evaluation-procedures`
- Domain family: `hazop`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 220
- Usable text pages indexed: 218
- Indexed text characters: 310548
- Top evidence signals: HAZOP/PHA:257, Incident/human factors:238, QRA/risk criteria:194, Consequence analysis:68, LOPA/IPL:49, Relief/effluent:33
- Primary shared skill: `hazop-hazan-study-leader`
- Secondary shared skills: none
- Source purpose: Use the source to improve HAZOP study discipline and worksheet quality.

## Source Navigation Hooks

- No reliable outline hooks were available from the current extraction.

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 19 | 21 | incident_human, lopa_ipl, psm_moc_docs, fire_explosion, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 158 | 20 | incident_human, qra_risk, lopa_ipl | Use as a source-navigation anchor; verify before numeric/design claims. |
| 166 | 20 | qra_risk, lopa_ipl, consequence, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 155 | 19 | lopa_ipl, qra_risk, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 72 | 19 | incident_human, lopa_ipl, qra_risk, hazop_pha, reliability, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 168 | 18 | incident_human, qra_risk, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 60 | 18 | qra_risk, incident_human, lopa_ipl, alarm | Use as a source-navigation anchor; verify before numeric/design claims. |
| 32 | 17 | hazop_pha, incident_human, qra_risk, lopa_ipl | Use as a source-navigation anchor; verify before numeric/design claims. |
| 26 | 17 | incident_human, lopa_ipl, consequence, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 154 | 17 | qra_risk, incident_human, lopa_ipl | Use as a source-navigation anchor; verify before numeric/design claims. |
| 165 | 17 | incident_human, qra_risk, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 141 | 16 | qra_risk, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 5, 7-9, 12-13, 15, 18, 21-22, 24-26, 28-29, 31-39, 41-42, 45, 50-56, 67-70, 72-74, .... Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 8, 16, 19-20, 22, 24, 26, 28, 31-39, 45, 48, 53, 56, 58-66, 68, .... Treat these pages as navigation anchors, not final proof.
- QRA/risk criteria: Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. Evidence pages: 15-16, 18, 24, 32, 34, 56, 58-63, 72, 132-156, 158, 162, 165-166, 168, 211-214. Treat these pages as navigation anchors, not final proof.
- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 14, 19-22, 24, 26, 28, 34, 62-63, 68, 70, 72, 87-89, 94-96, 107, 131-132, .... Treat these pages as navigation anchors, not final proof.
- LOPA/IPL: Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. Evidence pages: 8, 19, 22, 26, 32, 60-61, 72, 97, 154-156, 158, 162, 166. Treat these pages as navigation anchors, not final proof.
- Relief/effluent: Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. Evidence pages: 39, 46, 76, 79, 81-83, 85, 122, 173-175, 179-181, 184, 188, 190, 193, 203. Treat these pages as navigation anchors, not final proof.

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

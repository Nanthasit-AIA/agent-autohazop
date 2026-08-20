# Field Manual - The Alarm Management Handbook

This is the dense working reference for `book-alarm-management-handbook`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `alarm-management-handbook`
- Domain family: `alarm`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 275
- Usable text pages indexed: 274
- Indexed text characters: 546491
- Top evidence signals: Alarm management:176, PSM/MOC/documentation:152, HAZOP/PHA:28, Consequence analysis:24, SIS/SIL:23, Incident/human factors:14
- Primary shared skill: `alarm-management-rationalization`
- Secondary shared skills: none
- Source purpose: Treat alarms as engineered operator-support functions, not generic safeguards.

## Source Navigation Hooks

- No reliable outline hooks were available from the current extraction.

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 151 | 16 | relief_effluent, alarm, hazop_pha, lopa_ipl, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 47 | 10 | alarm, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 157 | 9 | sis_sil, hazop_pha, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 274 | 9 | hazop_pha, psm_moc_docs, lopa_ipl, incident_human, alarm | Use as a source-navigation anchor; verify before numeric/design claims. |
| 63 | 9 | consequence, alarm | Use as a source-navigation anchor; verify before numeric/design claims. |
| 248 | 9 | psm_moc_docs, alarm | Use as a source-navigation anchor; verify before numeric/design claims. |
| 107 | 8 | psm_moc_docs, alarm | Use as a source-navigation anchor; verify before numeric/design claims. |
| 160 | 8 | psm_moc_docs, alarm, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 11 | 8 | alarm, hazop_pha, psm_moc_docs, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 271 | 7 | alarm | Use as a source-navigation anchor; verify before numeric/design claims. |
| 28 | 6 | alarm, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 208 | 6 | psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- Alarm management: Challenge alarm rationalization, priority, response time, standing/flood alarms, operator action, and IPL claims. Evidence pages: 3, 8-13, 15, 19-22, 24-28, 34-39, 42, 44-45, 47-48, 51-52, 54, 58-59, 62-63, 65-66, .... Treat these pages as navigation anchors, not final proof.
- PSM/MOC/documentation: Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. Evidence pages: 8, 11, 13, 15, 26-28, 33, 35, 41-42, 45, 47, 53-54, 70, 74, 76, .... Treat these pages as navigation anchors, not final proof.
- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 11, 55, 71, 83, 94, 100, 120, 145-147, 150-151, 157, 160, 169, 192, 202, .... Treat these pages as navigation anchors, not final proof.
- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 63-64, 100, 115, 148, 152, 156, 169, 231, 242, 249, 273, 275. Treat these pages as navigation anchors, not final proof.
- SIS/SIL: Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. Evidence pages: 11, 38, 40, 145, 151, 157-158, 169, 202, 231-232, 275. Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 34, 124, 139-140, 174, 190, 215-217, 262, 264, 272-274. Treat these pages as navigation anchors, not final proof.

## How To Attack A HAZOP Row

1. Match the row to the strongest topic signal above.
2. State whether this book is primary evidence, secondary support, or screening-only for the decision.
3. Rewrite the cause to name the failed item, failure mode, human/organizational condition, external event, or initiating event.
4. Rewrite the consequence as the unmitigated event path before safeguards.
5. Challenge every safeguard for independence, timing, effectiveness, auditability, and evidence.
6. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- What exact abnormal condition does the alarm detect, and does that detection occur early enough for effective action?
- What operator action is expected, how long does it take, and how is the response verified in training or drill records?
- Is the alarm independent of the initiating event and BPCS failure being analyzed?
- Is there evidence for priority, setpoint, shelving/bypass controls, standing alarm behavior, and alarm flood performance?

## Anti-Patterns To Kill

- Crediting an alarm as a safeguard without response time, action, or independence evidence.
- Using alarm count reduction as proof of safety improvement without scenario-level consequence review.
- Treating a control-system alarm and the failed control loop as independent layers.

## Row Moves

- Split 'operator responds to alarm' into detection, diagnosis, action, and verification requirements.
- Downgrade an alarm from IPL credit to warning-only when independence/timing/auditability is missing.
- Recommend rationalization or response-procedure update only when the current scenario exposes a specific gap.

## Hard Decision Gates

- Whether an alarm is only awareness, an operator response safeguard, or a candidate IPL.
- Whether priority, setpoint, response time, standing/flood behavior, and operator action are documented.
- Whether alarm changes require rationalization, shelving/bypass controls, proof of response, or MOC.

## Missing-Basis Triggers

- Alarm philosophy/rationalization record
- Setpoint and priority basis
- Operator response time and action verification
- Standing/flood alarm data
- Bypass/shelving controls and MOC
- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Specialist Handoff

- Hand off to `alarm-management-rationalization` when the row needs the primary shared workflow.
- No secondary shared skill is configured; use the primary shared skill or project SME handoff when needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

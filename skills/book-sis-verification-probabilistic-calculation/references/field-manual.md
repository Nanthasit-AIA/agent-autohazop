# Field Manual - SIS Verification - Probabilistic Calculation

This is the dense working reference for `book-sis-verification-probabilistic-calculation`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `sis-verification-probabilistic-calculation`
- Domain family: `sis`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 385
- Usable text pages indexed: 385
- Indexed text characters: 606051
- Top evidence signals: SIS/SIL:1376, Reliability data:456, QRA/risk criteria:163, LOPA/IPL:18, PSM/MOC/documentation:16, HAZOP/PHA:12
- Primary shared skill: `sis-sil-verification-reliability`
- Secondary shared skills: none
- Source purpose: Use the source to challenge SIS/SIF claims through lifecycle evidence, not labels.

## Source Navigation Hooks

- No reliable outline hooks were available from the current extraction.

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 118 | 35 | sis_sil, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 238 | 23 | sis_sil, reliability, lopa_ipl | Use as a source-navigation anchor; verify before numeric/design claims. |
| 184 | 21 | sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 203 | 19 | reliability, sis_sil, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 235 | 19 | sis_sil, lopa_ipl, qra_risk, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 143 | 19 | sis_sil, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 134 | 19 | reliability, sis_sil, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 201 | 18 | sis_sil, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 122 | 18 | sis_sil, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 188 | 18 | sis_sil, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 73 | 18 | sis_sil, reliability, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 271 | 18 | sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- SIS/SIL: Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. Evidence pages: 1, 4-9, 11-36, 38-39, 42-43, 47-51, 58-60, 62, 65-66, 68-69, 73-75, 77, 82, 85-86, .... Treat these pages as navigation anchors, not final proof.
- Reliability data: Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. Evidence pages: 6-9, 20, 30, 38-44, 46-51, 55-61, 64-66, 68-69, 72-73, 75, 79, 83-84, 86, 90-93, .... Treat these pages as navigation anchors, not final proof.
- QRA/risk criteria: Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. Evidence pages: 7, 18, 72-76, 78-81, 85, 88-89, 94, 118-119, 201, 203-207, 209-210, 215-216, 218, 220, .... Treat these pages as navigation anchors, not final proof.
- LOPA/IPL: Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. Evidence pages: 18-19, 22, 25, 27, 105, 121, 123, 235, 238. Treat these pages as navigation anchors, not final proof.
- PSM/MOC/documentation: Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. Evidence pages: 15, 20-21, 99-100, 117, 119, 154, 160, 235, 305-306, 382. Treat these pages as navigation anchors, not final proof.
- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 14, 25, 30, 36, 188, 200, 247-248, 287, 293, 382, 384. Treat these pages as navigation anchors, not final proof.

## How To Attack A HAZOP Row

1. Match the row to the strongest topic signal above.
2. State whether this book is primary evidence, secondary support, or screening-only for the decision.
3. Rewrite the cause to name the failed item, failure mode, human/organizational condition, external event, or initiating event.
4. Rewrite the consequence as the unmitigated event path before safeguards.
5. Challenge every safeguard for independence, timing, effectiveness, auditability, and evidence.
6. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- What is the SIF: sensor, logic solver, final element, safe state, trip setpoint, process safety time, and demand mode?
- Where is the SIL target allocation basis and how does it trace back to the hazardous event?
- Are PFD/PFH, proof-test interval, diagnostics, bypass control, and common-cause assumptions documented?
- Is the claimed SIS independent from the initiating BPCS/control failure?

## Anti-Patterns To Kill

- Calling something 'SIL rated' without SRS, target SIL, verification, validation, and proof-test evidence.
- Using generic failure rates without equipment boundary, service context, and data-source applicability.
- Treating the same instrument as both cause and protection.

## Row Moves

- Map any claimed trip to a named SIF and push missing lifecycle evidence into recommendations.
- Separate SIL selection questions from SIL verification questions.
- Route data-quality issues to reliability-data review before accepting PFD/PFH.

## Hard Decision Gates

- Whether a claimed SIF has a defined hazardous event, safe state, sensor-logic-final element chain, and demand mode.
- Whether SIL target, PFD/PFH, proof-test interval, bypass controls, and independence from BPCS are supported.
- Whether the evidence belongs in HAZOP, LOPA, SRS, SIL verification, validation, or operations/maintenance.

## Missing-Basis Triggers

- SIL target allocation basis
- SRS/SIF definition
- PFD/PFH calculation and proof-test interval
- Independence from BPCS and common-cause review
- Validation, bypass, maintenance, and proof-test records
- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Specialist Handoff

- Hand off to `sis-sil-verification-reliability` when the row needs the primary shared workflow.
- No secondary shared skill is configured; use the primary shared skill or project SME handoff when needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

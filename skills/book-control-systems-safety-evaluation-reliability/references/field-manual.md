# Field Manual - Control Systems Safety Evaluation and Reliability

This is the dense working reference for `book-control-systems-safety-evaluation-reliability`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `control-systems-safety-evaluation-reliability`
- Domain family: `sis`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 476
- Usable text pages indexed: 476
- Indexed text characters: 834872
- Top evidence signals: Reliability data:583, SIS/SIL:338, QRA/risk criteria:184, HAZOP/PHA:16, Incident/human factors:16, PSM/MOC/documentation:14
- Primary shared skill: `sis-sil-verification-reliability`
- Secondary shared skills: `reliability-data-selection`
- Source purpose: Use the source to challenge SIS/SIF claims through lifecycle evidence, not labels.

## Source Navigation Hooks

- No reliable outline hooks were available from the current extraction.

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 112 | 17 | reliability, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 235 | 16 | reliability, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 414 | 15 | sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 279 | 15 | sis_sil, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 282 | 14 | reliability, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 83 | 14 | reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 386 | 13 | sis_sil, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 373 | 13 | reliability, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 392 | 13 | sis_sil, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 289 | 13 | sis_sil, qra_risk, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 85 | 13 | reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 379 | 12 | sis_sil, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- Reliability data: Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. Evidence pages: 10-11, 16, 20, 24, 41, 44, 54, 60, 68-70, 75-76, 82-98, 101-107, 110, 112-114, .... Treat these pages as navigation anchors, not final proof.
- SIS/SIL: Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. Evidence pages: 10, 12, 15, 17, 19, 22-26, 53, 59, 75, 96-100, 103, 108-109, 112, 117, .... Treat these pages as navigation anchors, not final proof.
- QRA/risk criteria: Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. Evidence pages: 10, 20, 121-137, 167, 235-236, 274-275, 278, 282, 288-289, 291-294, 297-299, 308-309, 329-331, 335-336, .... Treat these pages as navigation anchors, not final proof.
- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 40, 42-43, 46, 65, 67, 74, 460, 469, 475. Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 64, 123, 219-221, 242-243, 377-378, 393. Treat these pages as navigation anchors, not final proof.
- PSM/MOC/documentation: Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. Evidence pages: 5, 10, 53, 106-107, 121, 134, 231, 245, 399-401, 405. Treat these pages as navigation anchors, not final proof.

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
- Hand off to `reliability-data-selection` when those secondary workflows are needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

# Field Manual - PDS Data Handbook for SIS

This is the dense working reference for `book-pds-data-handbook-sis`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `pds-data-handbook-sis`
- Domain family: `sis`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 112
- Usable text pages indexed: 111
- Indexed text characters: 217697
- Top evidence signals: Reliability data:734, SIS/SIL:149, Relief/effluent:8, Consequence analysis:4, PSM/MOC/documentation:2, Incident/human factors:1
- Primary shared skill: `reliability-data-selection`
- Secondary shared skills: `sis-sil-verification-reliability`
- Source purpose: Use the source to challenge SIS/SIF claims through lifecycle evidence, not labels.

## Source Navigation Hooks

- 1 INTRODUCTION
- 1.1 Objective and Scope
- 1.2 Benefits of Reliability Analysis - the PDS Method
- 1.3 The IEC 61508 and 61511 Standards
- 1.4 Organisation of Data Handbook
- 1.5 Abbreviations
- 2 RELIABILITY CONCEPTS
- 2.1 The Concept of Failure
- 2.2 Failure Rate and Failure Probability
- 2.2.1 Failure Rate Notation
- 2.2.2 Decomposition of Failure Rate
- 2.3 Reliability Measures and Notation
- 2.4 Reliability Parameters
- 2.4.1 Rate of Dangerous Undetected Failures
- 2.4.2 The Coverage Factor, c
- 2.4.3 Beta-factors and CMooN
- 2.4.4 Safe Failure Fraction, SFF
- 2.5 Main Data Sources

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 111 | 33 | reliability, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 9 | 22 | sis_sil, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 16 | 21 | reliability, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 33 | 19 | reliability, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 107 | 17 | reliability, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 99 | 17 | reliability, relief_effluent, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 11 | 16 | reliability, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 85 | 15 | reliability, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 29 | 14 | reliability, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 8 | 14 | sis_sil, reliability, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 45 | 14 | reliability, sis_sil, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 53 | 14 | reliability, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- Reliability data: Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. Evidence pages: 2-5, 7-18, 20, 22, 24-33, 35-37, 39-67, 69-112. Treat these pages as navigation anchors, not final proof.
- SIS/SIL: Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. Evidence pages: 2-5, 7-11, 13, 15-18, 20, 22, 24, 26-33, 35-37, 39, 41-43, 45, 47, 49, .... Treat these pages as navigation anchors, not final proof.
- Relief/effluent: Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. Evidence pages: 6, 20-22, 31, 99-100. Treat these pages as navigation anchors, not final proof.
- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 65. Treat these pages as navigation anchors, not final proof.
- PSM/MOC/documentation: Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. Evidence pages: 34, 45. Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 8. Treat these pages as navigation anchors, not final proof.

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

- Hand off to `reliability-data-selection` when the row needs the primary shared workflow.
- Hand off to `sis-sil-verification-reliability` when those secondary workflows are needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

# Field Manual - Functional Safety - IEC 61508 and Related Standards

This is the dense working reference for `book-functional-safety-straightforward-guide`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `functional-safety-straightforward-guide`
- Domain family: `sis`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 276
- Usable text pages indexed: 275
- Indexed text characters: 398233
- Top evidence signals: SIS/SIL:836, Reliability data:267, QRA/risk criteria:99, Incident/human factors:47, PSM/MOC/documentation:37, HAZOP/PHA:12
- Primary shared skill: `sis-sil-verification-reliability`
- Secondary shared skills: none
- Source purpose: Use the source to challenge SIS/SIF claims through lifecycle evidence, not labels.

## Source Navigation Hooks

- Cover
- Functional Safety: A Straightforward Guide to applying IEC 61508 and Related Standards
- Contents
- A Quick Overview
- Part A The Concept of Safety-Integrity
- 1 The meaning and context of Safety-Integrity targets
- 1.1 Risk and the need for safety targets
- 1.2 Quantitative and qualitative safety targets
- 1.3 The life-cycle approach
- 1.4 Basic steps in the assessment process
- 1.5 Costs
- 1.5.1 Costs of applying the Standard
- 1.5.2 Savings
- 1.5.3 Penalty costs
- 1.6 The seven parts of IEC 61508
- Part B The Basic Requirements of IEC 61508 and 61511
- 2 Meeting IEC 61508 Part 1
- 2.1 Functional safety management and competence

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 120 | 16 | incident_human, sis_sil, qra_risk, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 244 | 16 | sis_sil, reliability, qra_risk, relief_effluent, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 149 | 15 | sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 60 | 14 | sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 46 | 14 | sis_sil, qra_risk, lopa_ipl | Use as a source-navigation anchor; verify before numeric/design claims. |
| 23 | 13 | sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 68 | 13 | sis_sil, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 86 | 12 | sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 28 | 12 | sis_sil, reliability, qra_risk, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 50 | 12 | sis_sil, reliability, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 57 | 12 | sis_sil, psm_moc_docs, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 94 | 12 | sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- SIS/SIL: Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. Evidence pages: 2, 4, 6-8, 10-11, 14, 17-19, 21-33, 36, 38-102, 104, 107, 109, 111, 113, .... Treat these pages as navigation anchors, not final proof.
- Reliability data: Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. Evidence pages: 7, 10, 16-17, 21-22, 25, 28, 32, 34, 43-45, 50, 58, 63-64, 74, 92, .... Treat these pages as navigation anchors, not final proof.
- QRA/risk criteria: Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. Evidence pages: 17-18, 20, 28, 30, 33, 44-48, 50-51, 53, 64, 92, 107, 116-120, 123-124, 146, .... Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 7, 16-17, 26, 30, 40, 45, 61, 97, 120-124, 130, 158, 204, 207-208, 245, .... Treat these pages as navigation anchors, not final proof.
- PSM/MOC/documentation: Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. Evidence pages: 27, 38, 41, 56-57, 65, 69-70, 81, 87-89, 101, 164, 171, 193, 225-226, 228, .... Treat these pages as navigation anchors, not final proof.
- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 25, 27, 40, 65, 155, 176, 267, 275. Treat these pages as navigation anchors, not final proof.

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

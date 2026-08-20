# Field Manual - CCPS Process Equipment Reliability Data

This is the dense working reference for `book-ccps-process-equipment-reliability-data`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `ccps-process-equipment-reliability-data`
- Domain family: `reliability`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 312
- Usable text pages indexed: 311
- Indexed text characters: 449144
- Top evidence signals: Reliability data:457, QRA/risk criteria:31, Incident/human factors:26, Consequence analysis:14, PSM/MOC/documentation:12, HAZOP/PHA:9
- Primary shared skill: `reliability-data-selection`
- Secondary shared skills: none
- Source purpose: Use the source to challenge reliability and failure-rate assumptions for applicability and uncertainty.

## Source Navigation Hooks

- 04227_fm.pdf
- Acronyms
- 04227_toc.pdf
- 1. Introduction
- 2. Equipment Failure Rate Data
- 3. CCPS Taxonomy
- 4. Data Bases, Sources, and Studies
- 5. CCPS Generic Failure Rate Data Base
- 6. Collection and Conversion of Plant-Specific Data
- 7. Failure Rate Data Transfer
- 8. Supplemental References
- Appendices
- 04227_01.pdf
- 1.1 Background
- 1.2 Guidelines Purpose, Scope and Organization
- 1.3 Use of This Guidelines
- 04227_02.pdf
- 2.1 Sources and Types of Failure Rate Data

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 4 | 13 | reliability, qra_risk, hazop_pha, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 17 | 11 | reliability, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 11 | 11 | reliability, qra_risk, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 27 | 10 | reliability, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 16 | 10 | qra_risk, hazop_pha, consequence, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 12 | 10 | reliability, qra_risk, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 150 | 9 | reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 151 | 9 | reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 248 | 9 | reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 98 | 9 | reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 44 | 9 | reliability, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 246 | 9 | reliability | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- Reliability data: Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. Evidence pages: 1-2, 4-12, 14-24, 26-32, 35-36, 40-49, 51-55, 58, 62, 64, 68, 71-79, 84-85, 87-88, .... Treat these pages as navigation anchors, not final proof.
- QRA/risk criteria: Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. Evidence pages: 4, 7-9, 11-12, 16, 42, 52, 55, 64, 70-71, 73, 131, 134, 245, 249, .... Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 4, 9, 12-13, 17, 23, 44-45, 54, 79, 89, 96, 105, 107, 111, 113, .... Treat these pages as navigation anchors, not final proof.
- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 3, 16, 42, 64, 73, 143, 289, 295. Treat these pages as navigation anchors, not final proof.
- PSM/MOC/documentation: Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. Evidence pages: 48, 80, 112, 227, 229-230, 249. Treat these pages as navigation anchors, not final proof.
- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 4, 9, 11, 16, 27, 69, 131. Treat these pages as navigation anchors, not final proof.

## How To Attack A HAZOP Row

1. Match the row to the strongest topic signal above.
2. State whether this book is primary evidence, secondary support, or screening-only for the decision.
3. Rewrite the cause to name the failed item, failure mode, human/organizational condition, external event, or initiating event.
4. Rewrite the consequence as the unmitigated event path before safeguards.
5. Challenge every safeguard for independence, timing, effectiveness, auditability, and evidence.
6. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- What equipment boundary, failure mode, service, duty cycle, environment, and maintenance context does the data represent?
- Is the data being used for HAZOP screening, LOPA frequency, QRA model, SIS verification, or mechanical integrity?
- Are common-cause, proof-test, inspection interval, repair time, demand rate, and uncertainty visible?
- Does the source match the plant equipment class closely enough to use the value?

## Anti-Patterns To Kill

- Copying handbook values into calculations without applicability review.
- Mixing failure rate, demand probability, PFDavg, PFH, and unavailability as if interchangeable.
- Ignoring common cause or inspection/proof-test assumptions.

## Row Moves

- Name the failure mode before requesting or applying data.
- Classify data as screening, project-approved, vendor-specific, or blocked.
- Route SIS data assumptions to SIF verification when they affect SIL/PFD.

## Hard Decision Gates

- Whether the equipment class, service, duty cycle, environment, failure mode, and data source match.
- Whether data are being used for screening, LOPA/SIL verification, QRA, maintenance, or mechanical integrity.
- Whether uncertainty, confidence, common cause, and inspection/proof-test assumptions are visible.

## Missing-Basis Triggers

- Equipment taxonomy and failure mode
- Operating/service context
- Approved reliability data source
- Proof-test/inspection interval
- Uncertainty and common-cause basis
- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Specialist Handoff

- Hand off to `reliability-data-selection` when the row needs the primary shared workflow.
- No secondary shared skill is configured; use the primary shared skill or project SME handoff when needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

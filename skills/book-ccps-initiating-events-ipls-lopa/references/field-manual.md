# Field Manual - CCPS Initiating Events and IPLs in LOPA

This is the dense working reference for `book-ccps-initiating-events-ipls-lopa`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `ccps-initiating-events-ipls-lopa`
- Domain family: `lopa`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 381
- Usable text pages indexed: 366
- Indexed text characters: 714066
- Top evidence signals: LOPA/IPL:1326, SIS/SIL:336, Relief/effluent:336, Reliability data:309, Incident/human factors:250, QRA/risk criteria:136
- Primary shared skill: `lopa-iel-conditional-modifier`
- Secondary shared skills: `reliability-data-selection`
- Source purpose: Use the source to turn selected HAZOP rows into disciplined one-scenario LOPA checks.

## Source Navigation Hooks

- Cover
- Title Page
- Copyright Page
- CONTENTS
- List of Data Tables
- Acronyms and Abbreviations
- 1. Introduction
- 1.1 Audience
- 1.2 Scope
- 1.3 Key Changes Since the Initial LOPA Concept Book
- 1.4 Recap of LOPA
- 1.4.1 What Is LOPA?
- 1.4.2 Common Elements of LOPA
- 1.4.3 When to Use LOPA
- 1.4.4 Inherently Safer Processes and LOPA
- 1.4.5 Advanced LOPA Techniques
- 1.5 Disclaimer
- 1.6 Linkage to Other CCPS Publications

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 189 | 34 | sis_sil, lopa_ipl, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 62 | 33 | lopa_ipl, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 71 | 29 | reliability, lopa_ipl, qra_risk, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 302 | 27 | qra_risk, lopa_ipl, sis_sil, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 41 | 26 | lopa_ipl, sis_sil, incident_human, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 191 | 26 | sis_sil, lopa_ipl, psm_moc_docs, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 42 | 25 | lopa_ipl, qra_risk, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 44 | 24 | qra_risk, lopa_ipl, reliability, inherent_siting, hazop_pha, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 82 | 24 | lopa_ipl, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 38 | 24 | lopa_ipl, hazop_pha, qra_risk, incident_human, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 377 | 24 | lopa_ipl, incident_human, psm_moc_docs, reliability, qra_risk, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 37 | 23 | sis_sil, lopa_ipl, reliability, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- LOPA/IPL: Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. Evidence pages: 6, 9-14, 18, 22-24, 27-28, 31-64, 66-88, 90-92, 94, 96-108, 110, 112-122, 124, 126, .... Treat these pages as navigation anchors, not final proof.
- SIS/SIL: Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. Evidence pages: 14, 19, 21, 24-25, 28, 35, 37, 41, 47, 54, 59, 67, 71, 73, .... Treat these pages as navigation anchors, not final proof.
- Relief/effluent: Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. Evidence pages: 12-14, 19, 22, 36, 46, 52, 67-68, 72, 74, 76-77, 93, 127-129, 151, 155, .... Treat these pages as navigation anchors, not final proof.
- Reliability data: Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. Evidence pages: 10, 12, 18-19, 21-22, 36-38, 43-47, 51, 53-54, 56-59, 63-64, 68-72, 82-84, 91, 96-97, .... Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 10-11, 13, 18-19, 23-24, 38, 41, 44-45, 47-50, 52, 54-58, 63, 67, 69-70, 78-80, .... Treat these pages as navigation anchors, not final proof.
- QRA/risk criteria: Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. Evidence pages: 10-11, 17-19, 34-35, 38-39, 42, 44, 47, 52, 62-64, 71, 88, 90, 92, 119, .... Treat these pages as navigation anchors, not final proof.

## How To Attack A HAZOP Row

1. Match the row to the strongest topic signal above.
2. State whether this book is primary evidence, secondary support, or screening-only for the decision.
3. Rewrite the cause to name the failed item, failure mode, human/organizational condition, external event, or initiating event.
4. Rewrite the consequence as the unmitigated event path before safeguards.
5. Challenge every safeguard for independence, timing, effectiveness, auditability, and evidence.
6. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- Is this exactly one scenario with one initiating event and one defined consequence?
- Which enabling conditions and conditional modifiers are actually applicable, and are they independent of the initiating event?
- For each credited IPL, where is the evidence for independence, effectiveness, auditability, and response time?
- Has any BPCS, alarm, SIS, relief, procedure, or inspection credit been double counted?

## Anti-Patterns To Kill

- Using a HAZOP safeguard list as an IPL list.
- Reducing likelihood without approved initiating event frequency, PFD, proof-test, or risk criteria basis.
- Crediting operator action without alarm quality, diagnosis time, action time, training, and audit evidence.

## Row Moves

- Convert the row into scenario, initiating event, consequence, enabling conditions, conditional modifiers, IPLs, and residual risk.
- Classify safeguards as candidate IPL, non-IPL safeguard, mitigation, or missing evidence.
- Block final likelihood/risk ranking until project LOPA rules and approved data are supplied.

## Hard Decision Gates

- Whether the scenario has one initiating event, one consequence, and explicit enabling conditions/conditional modifiers.
- Whether a safeguard qualifies as an IPL with independence, effectiveness, auditability, and timing.
- Whether likelihood reduction is supported without double counting BPCS, alarms, SIS, relief, procedures, or inspection.

## Missing-Basis Triggers

- Project LOPA rules and tolerable risk criteria
- Approved initiating-event frequency source
- Conditional modifier/enabling-condition basis
- IPL independence, audit, response-time, and proof-test evidence
- Common-cause and double-counting review
- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Specialist Handoff

- Hand off to `lopa-iel-conditional-modifier` when the row needs the primary shared workflow.
- Hand off to `reliability-data-selection` when those secondary workflows are needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

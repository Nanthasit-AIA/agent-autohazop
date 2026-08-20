# Field Manual - CCPS Enabling Conditions and Conditional Modifiers in LOPA

This is the dense working reference for `book-ccps-enabling-conditions-conditional-modifiers-lopa`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `ccps-enabling-conditions-conditional-modifiers-lopa`
- Domain family: `lopa`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 136
- Usable text pages indexed: 124
- Indexed text characters: 264865
- Top evidence signals: LOPA/IPL:590, Consequence analysis:194, Fire/explosion:133, QRA/risk criteria:130, HAZOP/PHA:80, PSM/MOC/documentation:31
- Primary shared skill: `lopa-iel-conditional-modifier`
- Secondary shared skills: none
- Source purpose: Use the source to turn selected HAZOP rows into disciplined one-scenario LOPA checks.

## Source Navigation Hooks

- Cover
- Title Page
- Copyright Page
- Contents
- List of Tables
- List of Figures
- Abbreviations and Acronyms
- 1 CONTEXT
- 1.1 LOPA Overview
- 1.2 Pertinent LOPA Variations
- 1.3 When to Use Enabling Conditions and Conditional Modifiers
- 1.4 Risk Criteria Endpoints
- 2 LOPA ENABLING CONDITIONS
- 2.1 Definition and Defining Characteristics
- 2.2 Interrelationship with Initiating Event
- 2.3 Time-At-Risk Enabling Conditions
- 2.4 Campaign Enabling Conditions
- 2.5 Other Possible Enabling Conditions

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 32 | 27 | lopa_ipl, hazop_pha, qra_risk, psm_moc_docs, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 88 | 26 | consequence, fire_explosion, qra_risk, lopa_ipl, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 87 | 23 | lopa_ipl, consequence, fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 106 | 22 | hazop_pha, lopa_ipl, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 99 | 22 | lopa_ipl, psm_moc_docs, hazop_pha, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 35 | 22 | lopa_ipl, sis_sil, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 134 | 21 | lopa_ipl, qra_risk, fire_explosion, hazop_pha, consequence, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 57 | 20 | lopa_ipl, reliability, consequence, qra_risk, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 50 | 19 | consequence, qra_risk, lopa_ipl | Use as a source-navigation anchor; verify before numeric/design claims. |
| 49 | 19 | consequence, qra_risk, lopa_ipl | Use as a source-navigation anchor; verify before numeric/design claims. |
| 11 | 19 | lopa_ipl, fire_explosion, consequence, hazop_pha | Use as a source-navigation anchor; verify before numeric/design claims. |
| 34 | 18 | lopa_ipl, hazop_pha, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- LOPA/IPL: Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. Evidence pages: 6, 9-11, 13, 15, 17-18, 20-21, 27-29, 31-97, 99, 101-102, 105-109, 111, 114-115, 119-123, .... Treat these pages as navigation anchors, not final proof.
- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 11, 15, 18, 21, 23, 31, 33, 43, 45-52, 56-57, 62-63, 68, 71-85, 87-88, .... Treat these pages as navigation anchors, not final proof.
- Fire/explosion: Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. Evidence pages: 9, 11, 16-18, 21, 43, 45, 47-48, 52, 60, 66-67, 69-70, 72-75, 77-84, 87-88, .... Treat these pages as navigation anchors, not final proof.
- QRA/risk criteria: Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. Evidence pages: 9-10, 13, 15-19, 21-23, 28-29, 31-33, 37-38, 40-47, 49-50, 57, 67, 70, 74, 78-79, .... Treat these pages as navigation anchors, not final proof.
- HAZOP/PHA: Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. Evidence pages: 11, 15, 17-21, 23, 29, 31-34, 67, 99, 101, 105-109, 113-114, 119-120, 130, 134-135. Treat these pages as navigation anchors, not final proof.
- PSM/MOC/documentation: Convert technical gaps into PSI, MOC, PSSR, operating procedure, audit, training, and action-tracking requirements. Evidence pages: 21, 28-29, 32, 35, 65-66, 68, 71, 83, 86, 89, 99, 127, 134. Treat these pages as navigation anchors, not final proof.

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
- No secondary shared skill is configured; use the primary shared skill or project SME handoff when needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

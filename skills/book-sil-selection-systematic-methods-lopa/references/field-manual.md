# Field Manual - SIL Selection - Systematic Methods Including LOPA

This is the dense working reference for `book-sil-selection-systematic-methods-lopa`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `sil-selection-systematic-methods-lopa`
- Domain family: `lopa`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 264
- Usable text pages indexed: 264
- Indexed text characters: 592054
- Top evidence signals: SIS/SIL:955, LOPA/IPL:369, QRA/risk criteria:326, Consequence analysis:228, Fire/explosion:222, Reliability data:114
- Primary shared skill: `lopa-iel-conditional-modifier`
- Secondary shared skills: `sis-sil-verification-reliability`, `risk-criteria-qra`
- Source purpose: Use the source to turn selected HAZOP rows into disciplined one-scenario LOPA checks.

## Source Navigation Hooks

- 1. Selecting Safety Integrity Levels: Introduction
- 1.1 Safety Integrity Level
- 1.2 Safety Instrumented Functions
- 1.3 SIL Selection and Risk
- 1.3.1 Consequence
- 1.3.2 Likelihood
- 1.3.3 Tolerable Risk and SIL Assignment
- 1.4 Qualitative versus Quantitative SIL Selection
- 1.4.1 Problems with Qualitative Techniques
- 1.4.2 Improving Likelihood Estimation with Quantitative LOPA
- 1.4.3 Improving Consequence Estimation with Quantitative Modeling
- 1.5 Benefits of Systematic SIL Selection
- 1.6 Objectives of This Book
- Summary
- Exercises
- References
- 2. Safety Life Cycle Context for SIL Selection
- 2.1 Standards and the Safety Life Cycle

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 167 | 43 | sis_sil, reliability, lopa_ipl | Use as a source-navigation anchor; verify before numeric/design claims. |
| 184 | 32 | sis_sil, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 61 | 27 | hazop_pha, lopa_ipl, sis_sil, relief_effluent, psm_moc_docs | Use as a source-navigation anchor; verify before numeric/design claims. |
| 10 | 27 | sis_sil, lopa_ipl | Use as a source-navigation anchor; verify before numeric/design claims. |
| 185 | 26 | sis_sil, qra_risk, lopa_ipl | Use as a source-navigation anchor; verify before numeric/design claims. |
| 20 | 26 | lopa_ipl, qra_risk, sis_sil, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 165 | 25 | sis_sil, lopa_ipl, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 60 | 25 | sis_sil, hazop_pha, lopa_ipl, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 106 | 24 | fire_explosion, consequence, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 187 | 23 | sis_sil, qra_risk, lopa_ipl | Use as a source-navigation anchor; verify before numeric/design claims. |
| 144 | 23 | lopa_ipl, qra_risk, sis_sil | Use as a source-navigation anchor; verify before numeric/design claims. |
| 166 | 23 | sis_sil, reliability, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- SIS/SIL: Challenge SIF/SIS lifecycle evidence, SIL target basis, independence, proof testing, and SRS completeness. Evidence pages: 3-4, 6-14, 16-36, 45-46, 49-51, 54-65, 74, 80-81, 84, 86-87, 89, 93-95, 97, 100, .... Treat these pages as navigation anchors, not final proof.
- LOPA/IPL: Convert qualified HAZOP scenarios into LOPA candidates, challenge initiating event and IPL credit, and avoid double counting. Evidence pages: 1, 3, 5-6, 8, 10-12, 14, 16-18, 20-22, 24, 26, 28-30, 32, 34, 36, .... Treat these pages as navigation anchors, not final proof.
- QRA/risk criteria: Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. Evidence pages: 4-6, 13, 16, 19-20, 28, 35, 37, 39, 41-54, 66, 74-79, 89-90, 92-94, 97, .... Treat these pages as navigation anchors, not final proof.
- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 5, 12-13, 17, 28, 45, 53, 59, 64, 92-96, 98-106, 108-121, 136-137, 140-142, 147, .... Treat these pages as navigation anchors, not final proof.
- Fire/explosion: Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. Evidence pages: 46, 51, 94, 97-99, 101-109, 112, 115-116, 118-120, 122, 126, 140-143, 145, 148, 152, .... Treat these pages as navigation anchors, not final proof.
- Reliability data: Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. Evidence pages: 5, 68, 75-76, 78-87, 89-91, 123, 127, 132, 137, 155-156, 161-163, 166-167, 202, 216, .... Treat these pages as navigation anchors, not final proof.

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
- Hand off to `sis-sil-verification-reliability`, `risk-criteria-qra` when those secondary workflows are needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

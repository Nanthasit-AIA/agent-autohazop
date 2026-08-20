# Field Manual - CCPS Chemical Process Quantitative Risk Analysis

This is the dense working reference for `book-ccps-chemical-process-qra`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `ccps-chemical-process-qra`
- Domain family: `qra`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Pages: 632
- Usable text pages indexed: 625
- Indexed text characters: 1308581
- Top evidence signals: QRA/risk criteria:932, Consequence analysis:672, Fire/explosion:479, Reliability data:452, Incident/human factors:244, Relief/effluent:131
- Primary shared skill: `risk-criteria-qra`
- Secondary shared skills: `relief-effluent-fire-explosion-consequence`
- Source purpose: Use the source to discipline quantitative risk assumptions and risk-criteria decisions.

## Source Navigation Hooks

- No reliable outline hooks were available from the current extraction.

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| 256 | 30 | qra_risk, lopa_ipl, fire_explosion, consequence, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 151 | 26 | fire_explosion, consequence, relief_effluent | Use as a source-navigation anchor; verify before numeric/design claims. |
| 139 | 25 | consequence, fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 258 | 23 | qra_risk, lopa_ipl, fire_explosion, consequence, reliability | Use as a source-navigation anchor; verify before numeric/design claims. |
| 310 | 22 | qra_risk, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 46 | 20 | consequence, fire_explosion, lopa_ipl, relief_effluent, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 325 | 20 | qra_risk, consequence | Use as a source-navigation anchor; verify before numeric/design claims. |
| 260 | 20 | qra_risk, fire_explosion, lopa_ipl, relief_effluent, consequence, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |
| 222 | 19 | fire_explosion, consequence, qra_risk, relief_effluent, incident_human | Use as a source-navigation anchor; verify before numeric/design claims. |
| 308 | 19 | qra_risk, consequence, fire_explosion | Use as a source-navigation anchor; verify before numeric/design claims. |
| 281 | 19 | incident_human, consequence, qra_risk | Use as a source-navigation anchor; verify before numeric/design claims. |
| 206 | 19 | fire_explosion, relief_effluent, qra_risk, consequence, incident_human, inherent_siting | Use as a source-navigation anchor; verify before numeric/design claims. |

## Topic Capsules

- QRA/risk criteria: Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. Evidence pages: 1, 5-10, 12, 14, 16, 19, 21-24, 26, 28-38, 41, 43-47, 50-82, 84-89, 92-99, .... Treat these pages as navigation anchors, not final proof.
- Consequence analysis: Improve source-term, toxic, flammable, environmental, endpoint, and severity logic. Evidence pages: 6, 9-12, 15, 19, 23-35, 37-38, 45-47, 50, 52, 58-59, 65, 67-72, 74-75, 86, .... Treat these pages as navigation anchors, not final proof.
- Fire/explosion: Improve fire, flash fire, VCE, BLEVE, escalation, ignition, and emergency response logic. Evidence pages: 10, 25, 27-28, 30, 32-33, 35-36, 45-47, 50, 52, 59, 63, 65, 69, 71-72, .... Treat these pages as navigation anchors, not final proof.
- Reliability data: Challenge failure modes, generic data, uncertainty, common cause, inspection/test basis, and applicability of data sources. Evidence pages: 6, 10-11, 16, 19, 23, 25-27, 30-31, 33-37, 50, 67, 77, 79-80, 230, 232-233, .... Treat these pages as navigation anchors, not final proof.
- Incident/human factors: Use incident-learning and human-factor logic to avoid blame-only causes and weak administrative actions. Evidence pages: 25-27, 32-34, 38, 79, 96, 98, 148, 166, 206, 216, 221-223, 229, 231, 235-236, .... Treat these pages as navigation anchors, not final proof.
- Relief/effluent: Challenge overpressure scenarios, relief-device basis, flare/effluent handling, and disposal consequences. Evidence pages: 15, 33-34, 36, 46, 64, 106-109, 113-114, 145, 147, 149, 151-154, 156, 160-161, 164-165, .... Treat these pages as navigation anchors, not final proof.

## How To Attack A HAZOP Row

1. Match the row to the strongest topic signal above.
2. State whether this book is primary evidence, secondary support, or screening-only for the decision.
3. Rewrite the cause to name the failed item, failure mode, human/organizational condition, external event, or initiating event.
4. Rewrite the consequence as the unmitigated event path before safeguards.
5. Challenge every safeguard for independence, timing, effectiveness, auditability, and evidence.
6. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- What risk metric is being used: individual risk, societal risk, event frequency, consequence endpoint, or risk ranking?
- Are frequency, consequence, occupancy, ignition, vulnerability, and exposure assumptions explicit?
- Which project/company/regulatory risk criteria control the decision?
- Has uncertainty or sensitivity been shown for assumptions that drive the decision?

## Anti-Patterns To Kill

- Presenting qualitative ranking as quantitative risk.
- Using generic frequencies or vulnerability factors without applicability review.
- Comparing against an unstated or invented risk tolerance criterion.

## Row Moves

- Label the output as screening, calculation input request, or blocked quantitative decision.
- Break event-tree/fault-tree logic into explicit branch assumptions.
- Ask for project-approved criteria and modeling basis before accepting risk reduction.

## Hard Decision Gates

- Whether frequency, consequence, vulnerability, occupancy, and ignition/exposure assumptions are explicit.
- Whether the selected risk metric and tolerability criterion are project-approved.
- Whether uncertainty and sensitivity are visible enough for decision making.

## Missing-Basis Triggers

- Project risk criteria
- Frequency data source
- Consequence model/endpoints
- Occupancy, ignition, vulnerability, and exposure basis
- Sensitivity/uncertainty treatment
- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Specialist Handoff

- Hand off to `risk-criteria-qra` when the row needs the primary shared workflow.
- Hand off to `relief-effluent-fire-explosion-consequence` when those secondary workflows are needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

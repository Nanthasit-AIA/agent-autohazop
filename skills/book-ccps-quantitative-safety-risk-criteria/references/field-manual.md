# Field Manual - CCPS Quantitative Safety Risk Criteria

This is the dense working reference for `book-ccps-quantitative-safety-risk-criteria`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `ccps-quantitative-safety-risk-criteria`
- Domain family: `qra`
- Confidence tier: controlled-use - Use for qualitative review and conservative prompts; do not support detailed numeric, tabular, or chapter-specific claims.
- Pages: 245
- Usable text pages indexed: 1
- Indexed text characters: 873
- Top evidence signals: no indexed topic hits
- Primary shared skill: `risk-criteria-qra`
- Secondary shared skills: none
- Source purpose: Use the source to discipline quantitative risk assumptions and risk-criteria decisions.

## Source Navigation Hooks

- No reliable outline hooks were available from the current extraction.

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| none | 0 | none | No indexed page evidence; use only screening logic. |

## Topic Capsules

- No indexed topic capsule is available. Keep outputs at screening level and request source enrichment.

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
- No secondary shared skill is configured; use the primary shared skill or project SME handoff when needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

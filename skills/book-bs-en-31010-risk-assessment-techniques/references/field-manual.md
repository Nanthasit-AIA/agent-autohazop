# Field Manual - BS EN 31010 Risk Management - Risk Assessment Techniques

This is the dense working guide for `book-bs-en-31010-risk-assessment-techniques`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `bs-en-31010-risk-assessment-techniques`
- Domain family: `risk-assessment-methods`
- Pages: 94
- Source quality: pages: 94; outline/bookmark count: 115
- Primary shared skill: `risk-criteria-qra`
- Detailed reference: `autohazop-agent-pack/references/standards/bs-en-31010-risk-assessment-techniques.md`
- Source purpose: Support method selection and uncertainty review when a HAZOP row needs escalation to LOPA, FTA, ETA, QRA, bow-tie, or a different risk assessment technique.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Classify the decision: hazard identification, scenario screening, likelihood estimation, barrier analysis, consequence modeling, uncertainty, or risk acceptance.
- [ ] Select the technique that fits available data, uncertainty, complexity, and decision stakes.
- [ ] Do not use risk matrix outputs as quantitative proof where FTA/ETA/QRA is needed.

## Anti-Patterns To Kill

- Using HAZOP alone to justify final tolerability for high-consequence complex scenarios.
- Using LOPA multiplication when dependencies/common cause are unresolved.

## Row Moves

- Route scenario to HAZOP, LOPA, FTA, ETA, bow-tie, QRA, or FMEA based on decision need.
- Add uncertainty/missing-basis recommendation when method choice is blocked.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- Risk matrix
- Tolerability criteria
- Frequency data
- Consequence model
- Dependency/common-cause basis
- Uncertainty/sensitivity basis

## Specialist Handoff

- Hand off to `risk-criteria-qra` when the row needs the primary shared workflow.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision
- Source basis
- HAZOP impact
- Missing basis
- Confidence tier

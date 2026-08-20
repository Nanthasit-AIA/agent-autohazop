# Field Manual - Hazop and Hazan - Kletz

This is the dense working reference for `book-hazop-hazan-kletz`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `hazop-hazan-kletz`
- Domain family: `hazop`
- Confidence tier: screening-only - Use for routing, gap prompts, and missing-basis checks only until the source wiki is enriched from page-level reading.
- Pages: 220
- Usable text pages indexed: 0
- Indexed text characters: 0
- Top evidence signals: no indexed topic hits
- Primary shared skill: `hazop-hazan-study-leader`
- Secondary shared skills: none
- Source purpose: Use the source to improve HAZOP study discipline and worksheet quality.

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

- Is the node boundary tight enough to know what equipment, utilities, recycle, vent, drain, and relief paths are included?
- Does the deviation combine one guide word with one process parameter and one credible abnormal state?
- Does the cause name a failed item/failure mode instead of vague wording such as 'equipment failure'?
- Is the consequence written as the unmitigated path before safeguards are credited?

## Anti-Patterns To Kill

- Rows that mix several initiating events, safeguards, or consequences into one line.
- Recommendations that say 'review' without naming acceptance criteria or evidence to produce.
- Safeguards copied from design intent without checking effectiveness for the specific cause.

## Row Moves

- Rewrite generic causes into equipment + failure mode + condition.
- Separate normal control, alarms, trips, relief, procedures, passive design, and emergency response.
- Turn vague actions into basis requests: design basis, relief basis, alarm response time, procedure, inspection, or interlock logic.

## Hard Decision Gates

- Whether the node boundary and design intent are specific enough for the selected deviation.
- Whether each row has one initiating cause, one unmitigated consequence path, and correctly separated safeguards.
- Whether a recommendation closes a real gap instead of restating normal design intent.

## Missing-Basis Triggers

- Node boundary and design intent
- Normal operating envelope
- P&ID/process graph context
- Safeguard design basis
- Relief/alarm/interlock/procedure evidence
- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Specialist Handoff

- Hand off to `hazop-hazan-study-leader` when the row needs the primary shared workflow.
- No secondary shared skill is configured; use the primary shared skill or project SME handoff when needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

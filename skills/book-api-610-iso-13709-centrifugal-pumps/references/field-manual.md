# Field Manual - API 610 / ISO 13709 Centrifugal Pumps

This is the dense working guide for `book-api-610-iso-13709-centrifugal-pumps`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `api-610-iso-13709-centrifugal-pumps`
- Domain family: `pump-design`
- Pages: 194
- Source quality: pages: 194; outline/bookmark count: 157
- Primary shared skill: `hazop-hazan-study-leader`
- Detailed reference: `autohazop-agent-pack/references/standards/api-610-iso-13709-centrifugal-pumps.md`
- Source purpose: Improve pump and transfer-line HAZOP rows by forcing the model to reason through suction, discharge, minimum flow/recycle, seal system, driver, standby logic, and trip actions.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Identify pump service, suction source, discharge destination, normal flow, rated flow, minimum continuous flow, NPSH margin, recycle, seal system, driver, and standby arrangement.
- [ ] Check no/less flow causes against blocked suction/discharge, low suction head, vapor lock, cavitation, driver trip, control valve action, and minimum-flow failure.
- [ ] Keep pump trip or low-flow interlock as safeguard/cause only when the specific trip action independently creates the selected deviation.

## Anti-Patterns To Kill

- Using generic pump failure where no pump is on the selected node.
- Claiming cavitation, dry running, seal failure, or reverse flow without suction/discharge/NPSH/check-valve context.

## Row Moves

- Convert 'pump failure' into failed-to-start, failed-to-run, loss of suction, blocked discharge, seal failure, cavitation, driver trip, or standby failure.
- For dry-running consequence, check whether low-low level trip is a safeguard, not part of the unmitigated consequence.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- Pump datasheet
- Hydraulic curve
- NPSH basis
- Minimum-flow/recycle basis
- Seal/driver/trip cause-and-effect

## Specialist Handoff

- Hand off to `hazop-hazan-study-leader` when the row needs the primary shared workflow.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision
- Source basis
- HAZOP impact
- Missing basis
- Confidence tier

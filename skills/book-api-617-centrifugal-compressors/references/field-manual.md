# Field Manual - API 617 Axial and Centrifugal Compressors and Expander-Compressors

This is the dense working guide for `book-api-617-centrifugal-compressors`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `api-617-centrifugal-compressors`
- Domain family: `compressor-design`
- Pages: 0
- Source quality: metadata extraction warning: PdfStreamError('Stream has ended unexpectedly')
- Primary shared skill: `hazop-hazan-study-leader`
- Detailed reference: `none`
- Source purpose: Improve HAZOP rows for compressors by forcing anti-surge/recycle, suction/discharge, seals, driver, lube/seal oil, vibration, and protection logic into cause/consequence/safeguard quality.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Identify compressor type, service, suction/discharge conditions, driver, seal system, lube/seal oil, anti-surge/recycle path, vibration monitoring, trip logic, and relief/depressuring path.
- [ ] Separate process causes from protection trips and anti-surge safeguards.
- [ ] Check whether surge, overspeed, blocked discharge, high temperature, seal failure, or utility loss is credible for the selected node.

## Anti-Patterns To Kill

- Using generic compressor failure without failure mode or operating envelope.
- Crediting anti-surge/trip logic without sensor, controller, final element, setpoint/action, and test basis.

## Row Moves

- Convert 'compressor failure' into surge, trip, fail-to-start, seal failure, lube-oil failure, vibration, overspeed, or blocked discharge scenario.
- Route severe high-pressure rows to relief/depressuring review.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- Compressor datasheet
- Anti-surge/recycle control narrative
- Seal/lube-oil system basis
- Trip setpoints/actions
- Relief/depressuring basis
- Vibration/driver data

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

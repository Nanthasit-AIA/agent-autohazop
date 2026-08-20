# Field Manual - API 521 Pressure-Relieving and Depressuring Systems

This is the dense working guide for `book-api-521-pressure-relieving-depressuring-systems`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `api-521-pressure-relieving-depressuring-systems`
- Domain family: `relief-depressuring`
- Pages: 206
- Source quality: pages: 206; outline/bookmark count: 59
- Primary shared skill: `relief-effluent-fire-explosion-consequence`
- Detailed reference: `autohazop-agent-pack/references/standards/api-521-pressure-relieving-depressuring-systems.md`
- Source purpose: Improve HAZOP/LOPA rows where overpressure, relief, depressuring, flare/vent/effluent destination, fire exposure, thermal expansion, or tube rupture may drive consequence or safeguard adequacy.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Identify credible overpressure scenario, protected equipment, relief path, disposal system, blocked outlet/fire/utility/tube rupture/thermal expansion basis, and simultaneous scenario rules.
- [ ] Check whether relief discharge creates downstream flare, vent, scrubber, sewer, or occupied-area consequences.
- [ ] Do not use API 521 to invent relief capacity; request calculation/design basis.

## Anti-Patterns To Kill

- Crediting relief without naming the credible overpressure case.
- Mixing relief system failure into consequence text as a second failure without basis.

## Row Moves

- For high pressure rows, identify whether blocked outlet, external fire, control valve failure, utility failure, tube rupture, or thermal expansion is the scenario.
- Add recommendation to verify relief/depressuring design when HAZOP row exceeds design envelope.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- Relief-case list
- Protected equipment
- Relief sizing basis
- Flare/vent/disposal capacity
- Backpressure
- Fire/tube rupture/utility failure assumptions

## Specialist Handoff

- Hand off to `relief-effluent-fire-explosion-consequence` when the row needs the primary shared workflow.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision
- Source basis
- HAZOP impact
- Missing basis
- Confidence tier

# Field Manual - API 650 Welded Tanks for Oil Storage

This is the dense working guide for `book-api-650-welded-tanks-oil-storage`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `api-650-welded-tanks-oil-storage`
- Domain family: `tank-design`
- Pages: 514
- Source quality: pages: 514; outline/bookmark count: 313
- Primary shared skill: `inherently-safer-siting-layout`
- Detailed reference: `autohazop-agent-pack/references/standards/api-650-welded-tanks-oil-storage.md`
- Source purpose: Improve tank HAZOP rows involving overfill, low level, roof behavior, venting interaction, nozzle/overflow paths, anchorage, foundation, settlement, or design-metal-temperature gaps.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Define tank type, roof type, design liquid level, design specific gravity, design metal temperature, nozzle/overflow arrangement, foundation, and anchorage basis.
- [ ] Separate normal fill/withdrawal operation from design basis and emergency conditions.
- [ ] Check whether overfill, vacuum, roof, settlement, or nozzle consequences need API 2000, API 2350, or facility siting handoff.

## Anti-Patterns To Kill

- Treating tank inventory buffer as a safeguard without level/venting/overflow basis.
- Claiming roof, shell, or nozzle failure without design envelope or settlement evidence.

## Row Moves

- For overfill rows, identify inlet source, level detection, shutdown path, overflow/drain path, and release consequence.
- For low pressure/vacuum rows, hand off to API 2000 venting checks.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- Tank datasheet
- Roof type
- Design liquid level/specific gravity
- Nozzle/overflow arrangement
- Foundation/settlement basis

## Specialist Handoff

- Hand off to `inherently-safer-siting-layout` when the row needs the primary shared workflow.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision
- Source basis
- HAZOP impact
- Missing basis
- Confidence tier

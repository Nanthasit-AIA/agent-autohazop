# Field Manual - Piping and Instrumentation Diagram Development

This is the dense working guide for `book-moe-toghraei-pid-development`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `moe-toghraei-pid-development`
- Domain family: `pid-development`
- Pages: 472
- Source quality: pages: 472
- Primary shared skill: `hazop-hazan-study-leader`
- Detailed reference: `autohazop-agent-pack/references/standards/moe-toghraei-pid-development.md`
- Source purpose: Improve AutoHAZOP graph extraction and node definition by requiring P&ID topology, line service, equipment boundary, instrument role, and valve placement evidence.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Build node boundary from equipment, lines, valves, instruments, utilities, drains, vents, relief paths, and off-page connectors.
- [ ] Check line tags, flow direction, service, normal position, control loop action, and package boundary before HAZOP rows.
- [ ] Reject graph-derived causes when the failed item is not on or connected to the selected node.

## Anti-Patterns To Kill

- Using valve/instrument IDs as equipment nodes.
- Generating cross-node consequences without upstream/downstream path evidence.
- Ignoring off-page connectors, vents, drains, bypasses, or common headers.

## Row Moves

- Convert graph uncertainty into a P&ID extraction correction before HAZOP generation.
- Use line/equipment boundary evidence to reject irrelevant causes.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- P&ID revision
- Line list
- Equipment list
- Instrument index
- Valve list/normal position
- Off-page connector mapping

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

# Field Manual - BS EN 1861 Refrigerating Systems Flow Diagrams and P&ID Layout/Symbols

This is the dense working guide for `book-bs-en-1861-refrigerating-pid-layout-symbols`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `bs-en-1861-refrigerating-pid-layout-symbols`
- Domain family: `pid-symbols-refrigeration`
- Pages: 32
- Source quality: pages: 32
- Primary shared skill: `hazop-hazan-study-leader`
- Detailed reference: `autohazop-agent-pack/references/standards/bs-en-1861-refrigerating-pid-layout-symbols.md`
- Source purpose: Support P&ID parsing and graph validation where refrigeration or heat-pump diagrams, symbol conventions, flow direction, equipment boundaries, or layout conventions affect HAZOP context.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Confirm whether the drawing is process P&ID, refrigeration/heat-pump system diagram, flow diagram, or mixed schematic.
- [ ] Check symbols, flow direction, equipment boundaries, line functions, valves, instruments, and utilities before generating HAZOP nodes.
- [ ] Mark ambiguous symbols as missing basis instead of inventing equipment or safeguards.

## Anti-Patterns To Kill

- Treating every symbol as equipment instead of valve/instrument/line annotation.
- Generating HAZOP nodes from uncertain drawing symbols without confidence tags.

## Row Moves

- Convert ambiguous drawing elements into extraction questions before HAZOP generation.
- Use symbol/layout uncertainty as missing-basis recommendation when it changes node boundary or safeguard location.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- Drawing legend
- Symbol standard
- Flow direction
- Equipment boundary
- Line/service identification

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

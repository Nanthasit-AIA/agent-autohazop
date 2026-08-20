# Field Manual - ISA 5.1 Instrumentation Symbols and Identification

This is the dense working guide for `book-isa-5-1-instrumentation-symbols-identification`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `isa-5-1-instrumentation-symbols-identification`
- Domain family: `instrument-symbols`
- Pages: 293
- Source quality: pages: 293; outline/bookmark count: 175
- Primary shared skill: `hazop-hazan-study-leader`
- Detailed reference: `none`
- Source purpose: Support graph extraction and HAZOP rows where instrument tag meaning, loop function, signal type, control/alarm/interlock role, or symbol interpretation affects cause/safeguard logic.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Parse tag letters, loop numbers, shared functions, instrument location, signal type, and functional role before using an instrument in cause or safeguard text.
- [ ] Separate indication, alarm, control, shutdown, permissive, interlock, and SIS functions.
- [ ] Do not infer safety function or fail action from tag letters alone.

## Anti-Patterns To Kill

- Calling any instrument an interlock or IPL without cause-and-effect evidence.
- Using transmitter failure on a node where the instrument does not measure the selected parameter.

## Row Moves

- Map each instrument to measured variable and action before allowing it as cause or safeguard.
- Convert ambiguous tag interpretation into missing-basis request for legend, loop diagram, or control narrative.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- P&ID legend
- Instrument index
- Loop diagram
- Control narrative
- Cause-and-effect chart
- Signal/fail action

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

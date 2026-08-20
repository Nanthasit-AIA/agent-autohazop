# Field Manual - CCPS Guidelines for Safe Automation of Chemical Processes

This is the dense working guide for `book-ccps-safe-automation-chemical-processes`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `ccps-safe-automation-chemical-processes`
- Domain family: `automation-sis-bpcs`
- Pages: 441
- Source quality: pages: 441
- Primary shared skill: `sis-sil-verification-reliability`
- Detailed reference: `autohazop-agent-pack/references/standards/ccps-safe-automation-chemical-processes.md`
- Source purpose: Prevent HAZOP rows from misusing interlocks/alarms/SIS as generic causes or safeguards; force cause-and-effect, fail-safe action, bypass management, and independence evidence.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Classify each automation element as BPCS, alarm/operator action, interlock/trip, SIS/SIF, permissive, shutdown, or final element.
- [ ] Identify sensor, logic solver/controller, final element, setpoint, action, safe state, reset, bypass, diagnostics, and test/validation basis.
- [ ] Separate spurious trip as initiating event from failure-on-demand as IPL evidence; do not mix both in one HAZOP row.

## Anti-Patterns To Kill

- Using 'interlock fails' as a cause after another initiating event has already occurred.
- Crediting BPCS/alarm/interlock as IPL without independence, timing, audit, and proof-test evidence.
- Treating a valve fail position as known when the P&ID/process description does not state it.

## Row Moves

- Rewrite automation causes as false trip, failure to act on demand, loss of signal, sensor fault, logic fault, final-element fault, or bypassed state.
- Move protection-layer failure from consequence text into IPL missing-basis review.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- Cause-and-effect chart
- Control narrative
- Trip setpoint/action
- Fail-safe position
- Bypass/MOC record
- Proof-test/validation evidence
- BPCS/SIS independence

## Specialist Handoff

- Hand off to `sis-sil-verification-reliability` when the row needs the primary shared workflow.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision
- Source basis
- HAZOP impact
- Missing basis
- Confidence tier

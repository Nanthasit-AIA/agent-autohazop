# HAZOP Control Documentation QA

Use this reference before accepting instrument/control content in HAZOP, LOPA, IPL review, or GraphRecon outputs.

## Decision Gates

### Cause Credibility

An instrument/control cause is credible only when these are clear enough for the node:

- Tag or loop identity.
- Measured or manipulated variable.
- Failure mode or wrong action.
- Effect on the final element, signal, control output, or utility.
- Physical path from the control failure to the selected deviation.
- Operating mode in which the failure can occur.

Reject or revise causes like:

- `instrument failure`
- `control loop failure`
- `operator error`
- `alarm failure`
- `interlock failure`

until the tag, function, failure mode, and process effect are stated.

### Consequence Wording

Consequences must remain unmitigated. Do not include alarm, operator response, trip, shutdown, PSV, or other protection action in the consequence text. Put those in safeguards or IPL fields.

Good consequence structure:

`<control/documented failure> causes <deviation> at <node/tag>. This propagates through <local/downstream/upstream/utility path>. The unmitigated state is <overpressure/no flow/reverse flow/LOPC/off-spec/dry running>, leading to <safety/environment/asset/operability effect>.`

### Safeguard And IPL Evidence

Treat each item as follows:

- `ordinary safeguard`: tag or document indicates an alarm, indication, control, procedure, or device exists, but IPL criteria are not proven.
- `candidate IPL`: protection function appears relevant, but independence, effectiveness, auditability, timing, or design basis is missing.
- `credited IPL`: project evidence shows independence from initiating event, effectiveness for the scenario, auditability/testing, design basis, management basis, and accepted PFD/SIL credit.

## Required Evidence By Claim

| Claim | Minimum documentation to check |
| --- | --- |
| Control loop causes deviation | P&ID, tag/index entry, loop diagram, controller or control narrative, final element action |
| Alarm as safeguard | P&ID or alarm list, alarm setpoint/rationalization, operator response procedure, response time basis |
| Interlock/trip as safeguard | P&ID, cause-and-effect or logic diagram, process control description, final element action, bypass/override status |
| SIF/SIS as IPL | SRS/SIF definition, SIL target, sensor-logic-final element chain, proof test/maintenance basis, independence review |
| Manual action as safeguard | Procedure/checklist, alarm/check cue, available time, training, safe access, task complexity |
| Loop wiring/power/air dependency | Loop diagram, installation details, power/instrument-air source, junction/terminal data |

## Recommendation Quality

Recommendations should name the document and decision they close:

- Bad: `Review interlock.`
- Better: `Provide current cause-and-effect and loop diagram for XV-101 trip to verify safe action, independence from BPCS cause, and testable IPL basis.`

## Conflict Handling

If documents disagree, do not silently reconcile them. Mark the affected worksheet cell:

- cause credibility
- safeguard existence
- IPL credit
- likelihood reduction
- recommendation closure
- graph control relation

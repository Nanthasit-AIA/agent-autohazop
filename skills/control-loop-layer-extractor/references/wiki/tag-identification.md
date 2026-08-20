# Tag Identification Wiki

Use this wiki when parsing instrument tags, function letters, and loop numbers into candidate control-loop components.

## Core Principle

Instrument tags are strong routing hints but weak engineering proof. A tag can suggest what an item may do, but a tag alone does not prove:

- control action.
- fail action.
- safe state.
- process connection.
- alarm priority.
- operator response.
- interlock logic.
- SIS/SIF/IPL status.

## Tag Parsing Fields

Extract:

- `raw_tag`: exact text from source.
- `normalized_tag`: cleaned tag string.
- `prefix`: plant/unit/area prefix if present.
- `function_letters`: alphabetic function segment.
- `loop_number`: loop identifier.
- `suffix`: train, redundant channel, equipment suffix, or drawing suffix.
- `service_hint`: service from nearby text or index row.
- `location_hint`: field, panel, DCS, PLC, local, shared display, or unknown.
- `source_document`: P&ID, loop diagram, index, datasheet, narrative, or unknown.
- `attachment`: line, equipment, nozzle, panel, rack, or unknown.

## Function-Letter Reasoning

Use function letters as role hints:

- `F`: flow-related variable.
- `P`: pressure-related variable.
- `T`: temperature-related variable.
- `L`: level-related variable.
- `A`: analysis, alarm, or other project-specific usage depending on context.
- `I`: indication.
- `C`: control.
- `R`: recording or running depending on project convention.
- `S`: switch, speed, safety, or status depending on project convention.
- `V`: valve, vibration, or other project convention depending on context.
- `Y`: relay, computation, or converter depending on project convention.
- `Z`: position or other project convention depending on context.

Do not hard-code a universal meaning when the project legend says otherwise.

## Common Tag Families

Use these as candidates, not final facts:

- `FT`: flow transmitter or flow measurement source.
- `FIC`: flow indicating controller.
- `FCV`: flow control valve.
- `PT`: pressure transmitter.
- `PIC`: pressure indicating controller.
- `PCV`: pressure control valve.
- `LT`: level transmitter.
- `LIC`: level indicating controller.
- `LCV`: level control valve.
- `TT`: temperature transmitter.
- `TIC`: temperature indicating controller.
- `TCV`: temperature control valve.
- `AT` or analyzer tags: analyzer measurement source.
- `XV` or `MOV`: on-off valve candidate, not automatically control valve.
- `ESDV` or `SDV`: shutdown valve candidate, not normal BPCS final element unless project documents say so.

## Loop Number Grouping

Tags with the same loop number often belong together, but verify with:

- loop diagram.
- signal line.
- index row.
- control narrative.
- shared service description.
- physical process relation.

Example candidate grouping:

```json
{
  "loop_number": "101",
  "candidates": ["FT-101", "FIC-101", "FCV-101"],
  "candidate_relation": "FT measures flow, FIC controls, FCV manipulates flow",
  "required_basis": ["P&ID signal path", "instrument index", "loop diagram or control narrative"]
}
```

## Rejection Checks

Reject or downgrade the grouping when:

- same number appears in unrelated services.
- one tag is alarm-only or switch-only and no normal controller exists.
- final element is not on a process path that can manipulate the measured variable.
- controller is absent and only an indicator is present.
- P&ID suggests a local indicator only.
- loop number is a drawing convention rather than a control-loop relation.

## HAZOP Use

Good HAZOP cause wording from tag evidence:

```text
FIC-101 output drives FCV-101 closed due controller output fault, causing no/less flow through line L-101.
```

Weak wording to reject:

```text
Instrument failure causes no flow.
```

The good version names tag, role, failure mode, final element effect, and physical deviation path.

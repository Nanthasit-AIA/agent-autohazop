# Control Software And FRS Wiki

Use this wiki when a control relation depends on DCS/PLC logic, functional requirements, control narratives, permissives, sequences, or software commands.

## Why This Is Separate From P&ID Reading

A P&ID can show instruments and signals, but it often cannot prove:

- control mode.
- setpoint source.
- sequence state.
- permissive conditions.
- override selection.
- reset behavior.
- interlock action.
- bypass/override logic.
- manual/auto mode rules.

Those claims need control software documentation, functional requirements, control narratives, cause-and-effect, or operating procedures.

## Functional Requirement Fields To Extract

For each software-controlled relation, capture:

- `function_id`
- `function_name`
- `controlled_equipment`
- `input_tags`
- `output_tags`
- `mode`: auto, manual, cascade, remote, local, sequence, maintenance, unknown.
- `setpoint_source`
- `enable_conditions`
- `permissives`
- `interlocks`
- `operator_actions`
- `alarms`
- `commands`
- `reset_or_latch_behavior`
- `bypass_or_override`
- `failure_response`
- `source_document`
- `revision`
- `confidence`

## Classification

Separate:

- normal BPCS control.
- operator supervisory action.
- alarm-only function.
- permissive.
- interlock.
- trip/shutdown.
- SIS/SIF candidate.
- monitoring-only function.

Do not merge them into one "control loop" unless documents show the relation.

## Software Edge Patterns

Use:

- controller or function `uses_input` transmitter/switch/analyzer.
- function `has_setpoint` setpoint source.
- function `commands` final element.
- function `permits` start/open/close command.
- function `interlocks` equipment or valve.
- function `overrides` another controller output.
- function `depends_on` DCS/PLC/power/network.

## Missing Basis Patterns

Flag missing basis when:

- P&ID shows a signal but no control narrative proves action.
- a final element is commanded but action on fail or trip is unknown.
- a switch or alarm is assumed to trip equipment without cause-and-effect evidence.
- a software function is named but input/output tags are missing.
- mode handling is unclear.
- bypass or override state affects HAZOP consequence.

## HAZOP Use

Software evidence can support causes such as:

- wrong setpoint.
- controller in manual.
- output frozen.
- sequence step commands wrong valve.
- permissive prevents start.
- override selector holds output at constraint.
- communication loss between PLC and final element.

But HAZOP consequences should remain unmitigated. Do not write consequence text that assumes a protection layer also fails.

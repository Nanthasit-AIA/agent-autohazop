# Final Control Element Wiki

Use this wiki when mapping controller outputs to valves, actuators, drives, dampers, heaters, or other final elements.

## Final Element Types

Common final elements:

- control valve.
- on-off valve.
- shutdown valve.
- motor-operated valve.
- variable-speed drive.
- pump start/stop command.
- damper or louver.
- heater duty command.
- compressor guide vane.
- recycle valve.
- reagent or utility dosing valve.

## Required Fields

For each final element, extract:

- tag.
- final element type.
- controlled or manipulated stream.
- line/equipment attachment.
- actuator type if known.
- signal source.
- utility dependency.
- normal operating role.
- fail action if documented.
- evidence source.
- confidence.

## Manipulated Variable

A final element manipulates something:

- valve position manipulates flow or pressure drop.
- VFD manipulates speed.
- damper manipulates air/gas flow.
- heater command manipulates heat duty.
- pump command manipulates flow or pressure.
- recycle valve manipulates recycle rate.

If the manipulated variable is unclear, record `unknown` and a missing-basis note.

## Do Not Infer Fail Action

Do not infer fail-open, fail-closed, fail-last, spring action, air-to-open, or air-to-close from tag alone. Require:

- datasheet.
- actuator specification.
- loop diagram.
- valve schedule.
- cause-and-effect.
- project standard or explicit P&ID note.

## HAZOP Cause Families

Control-valve and final-element causes can include:

- stuck closed/open.
- output signal failed low/high.
- actuator air failure.
- positioner fault.
- wrong split-range setting.
- valve undersized or saturated.
- manual bypass or isolation left wrong.
- VFD speed command failure.
- motor fails to start or stop.

Each cause must connect physically to the selected deviation.

## Safeguard Boundary

A final element in a normal BPCS loop is not automatically an IPL. If a final element is claimed as protection, require:

- independence from initiating cause.
- designed protective function.
- proof/testing basis.
- response time basis.
- management and auditability basis.
- accepted risk credit or SIL/PFD basis if applicable.

Otherwise label it as ordinary safeguard or candidate basis needed.

# P&ID, Loop, And Logic Checklist

Use this checklist for GraphRecon extraction, HAZOP generation, and control documentation review.

## P&ID And Tag Interpretation

Check:

- Instrument symbol and tag are legible.
- Function letters are interpreted as role hints, not proof of action or safety function.
- Loop number groups related devices logically.
- Field, panel, shared display/control, and behind-panel locations are distinguished when symbols provide that information.
- Signal type and line symbols are captured when shown.
- Final control element, control valve, damper, louver, variable-speed drive, or other actuator is linked to the loop.
- Local instruments are not ignored, because they may be important for operation and maintenance.

Do not infer:

- fail-open/fail-closed action without project evidence.
- alarm priority or operator response from an alarm tag alone.
- SIS/SIF status from a symbol or tag alone.

## Control Loop Review

For each loop, identify:

- sensing element or transmitter.
- controller, shared control system, logic, or comparison function.
- setpoint or intended controlled variable when available.
- final control element and manipulated variable.
- signal path and power/utility dependencies.
- process connection and controlled equipment.
- abnormal effect if the signal, power, air, controller, or final element fails.

## Binary Logic And Interlocks

For on-off control, require enough documentation to answer:

- What condition starts the action?
- What permissive, interlock, or shutdown condition is required?
- What final element moves or what command is issued?
- What safe state is intended?
- Is the action implemented in PLC, DCS, relay, field device, or another system?
- Are bypasses, overrides, resets, and manual actions documented?
- Is the logic readable by operations, maintenance, and engineering reviewers?

Use logic diagrams, interlock notes, process control descriptions, operation descriptions, functional specifications, or cause-and-effect documents as the preferred evidence for logic behavior.

## Loop Diagram Review

Loop diagrams are useful when they show the information needed to install, checkout, and maintain a loop. Check for:

- process connection.
- instrument, controller/logic, final element, and other loop devices.
- pneumatic, electrical, digital, or mixed signal paths.
- power and service utility sources such as instrument air.
- junction boxes, terminal strips, panels, racks, local panels, or marshalling.
- wire/cable/conductor identifiers when required by the project.
- consistency with instrument index, specification forms, installation details, and location plans.

## Drawing Control

Check:

- drawing title and number.
- revision number and revision history.
- revision description specific enough to know what changed.
- drawing notes and interlock notes when used.
- reference table linking P&ID, loop diagram, installation details, location plan, or logic documents.
- current revision status before using the drawing as HAZOP evidence.

## GraphRecon Fields To Preserve

When extracting graph data, preserve:

- `tag`
- `loop_number`
- `function_letters`
- `location_class`
- `signal_type`
- `measured_variable`
- `manipulated_variable`
- `controller_or_logic`
- `final_element`
- `safe_state`
- `document_source`
- `revision`
- `confidence`
- `missing_basis`

# Extraction Workflow

Use this procedure to extract a ControlLoopLayer from P&ID, loop diagram, instrument index, control narrative, or GraphRecon data. The goal is not to "recognize tags" only. The goal is to produce evidence-grounded relations that say what is measured, what is controlled, what is manipulated, and where the control loop sits in the process graph.

## Pass 0: Evidence Intake

Collect and label all available evidence:

- P&ID drawing number, title, revision, page, and extracted tag text.
- loop diagram number, title, revision, page, and loop devices.
- instrument index rows with tag, service, location, I/O type, loop number, and drawing references.
- instrument datasheets for range, service, process connection, fail action, and actuator data.
- control narrative or functional requirements for setpoint, mode, logic, permissive, sequence, and command behavior.
- cause-and-effect chart for trips and interlocks.
- alarm list or alarm rationalization document for alarm-only claims.

If a source document is unavailable, create a missing-evidence item rather than inferring the claim.

## Pass 1: Tag Candidate Extraction

For each candidate tag, record:

- raw tag string.
- normalized tag.
- function letters.
- loop number.
- suffix or redundant-unit marker.
- service description.
- drawing/page/bbox if available.
- attached line, equipment, panel, or unknown.
- confidence and method.

Do not decide control logic at this stage.

## Pass 2: Loop Grouping

Group tags into loop candidates using strongest evidence first:

1. explicit loop diagram or loop number reference.
2. instrument index loop grouping.
3. signal line between sensor, controller, and final element.
4. control narrative naming controller and final element.
5. shared service description and loop number.
6. tag-name proximity only as low-confidence candidate.

Split loops when:

- tags share a loop number but serve different functions.
- one controller drives multiple final elements with split-range logic.
- cascade primary and secondary loops have distinct PV/MV relations.
- an alarm or interlock shares a number but is not part of normal BPCS control.

## Pass 3: Role Assignment

Assign roles only from evidence:

- `measured_variable`: the process variable sensed by transmitter/analyzer/switch.
- `controller`: DCS, PLC, panel controller, local controller, logic, or unknown.
- `setpoint_source`: local, remote, operator, cascade, recipe, ratio, schedule, or unknown.
- `final_element`: control valve, on-off valve, damper, VFD, motor command, heater duty, pump speed, or unknown.
- `manipulated_variable`: flow, valve position, speed, duty, pressure, purge rate, recycle rate, or unknown.
- `controlled_asset`: equipment, line, vessel, pump, exchanger, column, utility header, or process node.

Tag letters provide hints, not proof. A controller/final element relation needs signal, loop, index, narrative, or other document evidence.

## Pass 4: Control Pattern Classification

Classify the loop:

- `feedback`: one measured variable controls one manipulated variable.
- `cascade`: primary controller setpoint feeds secondary controller.
- `ratio`: one flow or variable is controlled in proportion to another.
- `feedforward`: disturbance or upstream variable adjusts control output.
- `override`: selector or constraint control overrides normal controller.
- `split_range`: one controller output drives multiple final elements by ranges.
- `on_off`: binary controller or logic commands open/close/start/stop.
- `sequence`: procedural or state-based command logic.
- `analyzer`: analyzer measurement affects control or monitoring.
- `monitoring_only`: indication/recording only.
- `alarm_only`: alarm function only, no normal control.
- `candidate`: plausible control loop with incomplete proof.
- `unknown`: evidence insufficient to classify.

## Pass 5: Attachment And Process Context

Attach every component:

- instruments to process taps, lines, vessels, equipment nozzles, or unknown.
- final elements to line segments, equipment utilities, drives, or unknown.
- controllers to control system, panel, local instrument, PLC, DCS, or unknown.
- controlled assets to the process node affected by the manipulated variable.

When an instrument measures a vessel variable but final element is on an inlet/outlet line, record both the measured asset and manipulated asset.

## Pass 6: Edge Construction

Create graph edges:

- sensor `measures` controlled asset or line variable.
- sensor `transmits_signal_to` controller.
- controller `commands` final element.
- final element `manipulates` process variable or line/equipment.
- loop `controls` controlled asset.
- loop `depends_on` instrument air, power, DCS/PLC, hydraulic power, or communication.
- evidence document `evidence_supports` node or edge.

For candidate edges, set:

```json
{
  "attributes": {
    "status": "candidate",
    "basis": "tag grouping only",
    "review_required": true
  }
}
```

## Pass 7: Missing Basis

Create missing-basis notes for:

- unverified final element action.
- missing process tap or attachment.
- missing controller or logic source.
- unknown setpoint source.
- unknown control direction.
- missing loop diagram or index reference.
- missing control narrative for sequences, interlocks, permissives, and trips.
- uncertain BPCS vs SIS boundary.

## Pass 8: HAZOP Readiness

A loop is HAZOP-ready when it has enough evidence to support:

- a credible control-related initiating cause.
- a credible ordinary safeguard or candidate safeguard statement.
- a missing-basis recommendation.
- a traceable relation to HAZOP node, parameter, and guide word.

The loop is not HAZOP-ready when the only evidence is a tag letter or unverified symbol.


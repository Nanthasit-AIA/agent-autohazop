# Loop Diagram Wiki

Use this wiki when loop diagrams, wiring, signal paths, instrument air, power, terminals, field panels, or loop checkout evidence matter.

## What A Loop Diagram Should Prove

A useful loop diagram may prove:

- process connection.
- sensing element or transmitter.
- controller, display, DCS/PLC point, or local panel.
- final element and actuator.
- signal type and direction.
- wiring, pneumatic tubing, digital communication, or mixed signal path.
- junction boxes, terminal strips, marshalling, panels, racks, and cabinets.
- power supply, instrument air, hydraulic supply, or other dependency.
- loop number and drawing references.
- revision and drawing status.

## Extraction Targets

Extract these fields:

- `loop_diagram_id`
- `loop_number`
- `device_tags`
- `process_connection`
- `controller_or_logic`
- `final_element`
- `signal_paths`
- `terminal_path`
- `panel_or_rack`
- `power_source`
- `air_or_hydraulic_source`
- `communication_path`
- `drawing_revision`
- `referenced_documents`
- `missing_basis`

## Signal Path Pattern

Represent each segment:

```json
{
  "source": "FT-101",
  "target": "FIC-101",
  "signal_type": "4-20mA | pneumatic | digital | discrete | unknown",
  "medium": "cable | tubing | network | internal DCS | unknown",
  "confidence": 0.86,
  "missing_basis": []
}
```

## Control Relation Evidence

Use the loop diagram to support:

- transmitter sends process measurement to controller or input card.
- controller output goes to final element positioner, solenoid, VFD, or actuator.
- utility loss such as instrument air or power can affect final element behavior.

Do not use the loop diagram alone to prove:

- process control objective.
- permissive or interlock logic.
- trip setpoint.
- SIL or IPL status.
- alarm priority.
- operator response time.

Those need control narrative, cause-and-effect, SRS, alarm rationalization, or procedure evidence.

## Attachment Logic

A loop diagram can show process connection, but P&ID or installation details may be needed to attach the instrument to:

- exact line number.
- exact vessel nozzle.
- upstream/downstream side of valve.
- pump suction/discharge.
- bypass or recycle line.
- local panel or field rack.

If exact attachment is unclear, record:

```json
{
  "attachment": "unknown",
  "missing_basis": ["Need P&ID or installation detail to confirm process tap location."]
}
```

## HAZOP Use

Loop diagrams strengthen HAZOP row generation by identifying:

- utility dependencies such as instrument air and power.
- final element affected by controller output.
- signal path components that can fail.
- missing evidence for cause specificity.

Example:

```text
Instrument air loss to FCV-101 actuator is a credible no/less flow cause only if the loop diagram or datasheet shows FCV-101 depends on instrument air and the fail position supports the deviation.
```

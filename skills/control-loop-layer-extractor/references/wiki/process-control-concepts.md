# Process Control Concepts Wiki

Use this wiki for chatbot answers and for classifying control-loop patterns in the ControlLoopLayer.

## Core Terms

- `PV`: process variable measured by an instrument.
- `SP`: setpoint or target value.
- `MV`: manipulated variable changed by the controller output.
- `CV`: controlled variable. Often same as PV, but not always.
- `disturbance`: process input that changes the controlled variable but is not directly controlled.
- `controller output`: signal or command sent to final element.
- `final element`: valve, drive, damper, heater, pump command, or actuator that changes the process.

## Feedback Loop

Pattern:

```text
PV measured -> controller compares PV to SP -> output changes final element -> MV affects process -> PV changes
```

Extraction fields:

- measured variable.
- controller.
- setpoint.
- final element.
- manipulated variable.
- controlled asset.

HAZOP cause families:

- transmitter drift or failure.
- wrong setpoint.
- controller output fault.
- final element stuck or saturated.
- loop in manual.
- utility loss to final element.

## Cascade Loop

Pattern:

```text
Primary controller output becomes secondary controller setpoint.
Secondary controller manipulates final element.
```

Extraction fields:

- primary PV.
- primary controller.
- secondary PV.
- secondary controller.
- secondary final element.
- cascade setpoint relation.

Hazard note:

- Do not collapse cascade into one loop if primary and secondary loops can fail differently.

## Ratio Loop

Pattern:

```text
controlled flow = ratio x wild flow
```

Extraction fields:

- wild variable.
- ratio setpoint.
- controlled variable.
- final element.
- material balance or quality objective.

HAZOP relevance:

- wrong ratio can cause composition, concentration, temperature, reaction rate, or quality deviations.

## Feedforward Loop

Pattern:

```text
measured disturbance adjusts output before controlled variable changes
```

Extraction fields:

- disturbance variable.
- compensation function.
- final element.
- affected controlled variable.

HAZOP relevance:

- bad feedforward signal or compensation can create over/under correction.

## Override Control

Pattern:

```text
selector chooses constraint controller output over normal controller output
```

Extraction fields:

- normal controller.
- constraint controller.
- selector logic.
- final element.
- selected output basis.

HAZOP relevance:

- override active at wrong time can starve flow, overpressure, overcool, or limit production.

## Split-Range Control

Pattern:

```text
one controller output drives two or more final elements over different output ranges
```

Extraction fields:

- controller.
- final element A and range.
- final element B and range.
- manipulated variables.
- interaction or deadband.

HAZOP relevance:

- wrong split range can open wrong valve, mix utilities, or lose control near transition.

## On-Off And Sequence Control

Pattern:

```text
condition or state -> command open/close/start/stop
```

Extraction fields:

- triggering condition.
- permissive.
- command.
- final element.
- reset/latch/bypass behavior.

HAZOP relevance:

- this often needs FRS or control narrative. P&ID symbols alone are not enough.

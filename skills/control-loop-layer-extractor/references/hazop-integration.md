# HAZOP Integration

Use this reference when passing ControlLoopLayer outputs into HAZOP generation.

## Purpose

The ControlLoopLayer should improve HAZOP generation by making control-related causes, safeguards, and recommendations specific and evidence-grounded.

It should prevent weak rows such as:

```text
Instrument failure causes no flow.
```

and support stronger rows such as:

```text
FIC-101 output drives FCV-101 closed due controller output fault, causing no or less flow through L-101.
```

## What HAZOP Can Use

HAZOP generation can use:

- loop id and tags.
- measured variable.
- controlled variable.
- manipulated variable.
- final element.
- controlled asset.
- signal or utility dependencies.
- documented operating mode.
- missing basis.
- confidence.
- source documents.

## Cause Generation

A control-related cause is credible when:

- the loop exists with enough evidence.
- the final element can physically change the selected parameter.
- the failure mode is specific.
- the operating mode supports the failure.
- the cause is not merely failure of a safeguard after another independent initiating event.

Good cause forms:

- `<controller tag> output fails high/low, driving <final element> <open/closed if documented>.`
- `<transmitter tag> fails low/high, causing controller to command <final element> in a way that creates <deviation>.`
- `Loss of instrument air to <final element> causes <documented fail action or unknown action with recommendation>.`
- `<loop> left in manual at wrong output during startup/shutdown, causing <deviation>.`

If fail action is unknown, do not claim the action. Write a recommendation:

```text
Verify fail action and loop diagram for FCV-101 before crediting actuator air-loss scenario.
```

## Safeguard And IPL Boundary

Control loops may be:

- ordinary safeguards.
- candidate safeguards.
- candidate IPLs requiring basis.
- unrelated to safeguard claims.

Do not reduce likelihood for a control loop unless the HAZOP/LOPA evidence supports IPL criteria.

## Recommendation Hooks

Common recommendation hooks:

- provide current loop diagram.
- provide instrument index row and service.
- verify control narrative and final element action.
- verify datasheet fail action.
- verify alarm rationalization and operator response basis.
- verify BPCS/SIS independence if IPL credit is desired.
- reconcile P&ID and loop diagram revision conflict.

## Output Traceability

Each HAZOP row influenced by the ControlLoopLayer should record:

- `ControlLoopID`
- relevant tags.
- evidence source.
- missing basis.
- confidence.

When the HAZOP export format cannot add columns, include concise trace in Recommendations or internal skill trace log.


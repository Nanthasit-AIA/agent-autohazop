# PID Algorithms And Loop Performance Wiki

Use this wiki only when the task requires PID or loop-performance reasoning. Do not load it for simple tag grouping.

## PID Terms

- proportional action responds to present error.
- integral action responds to accumulated error.
- derivative action responds to rate of error change.
- output limit prevents controller output from exceeding configured bounds.
- anti-reset windup limits integral accumulation when output saturates.
- dead time delays process response.
- process gain relates output change to process-variable change.
- loop mode may be automatic, manual, cascade, remote, tracking, or unknown.

## Extraction Fields

When PID behavior is relevant, capture:

- controller tag.
- loop mode.
- PV.
- SP.
- MV.
- output limits.
- cascade tracking relation.
- tuning or performance evidence if available.
- alarm or constraint relation if documented.
- source document and confidence.

## HAZOP Cause Families

PID-related causes can include:

- wrong setpoint.
- controller in manual.
- output saturated.
- poor tuning causing oscillation.
- integral windup after constraint.
- cascade mode broken.
- tracking failure.
- bad PV filtering or signal conditioning.

Only use these when the supplied context shows the loop and the cause can physically create the selected HAZOP deviation.

## Guardrails

- Do not invent tuning constants.
- Do not claim instability unless evidence shows oscillation, poor control, or project discussion.
- Do not infer cascade/override/split-range from tag letters only.
- Do not use PID algorithm concepts to overcomplicate a simple on-off or monitoring loop.

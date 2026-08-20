# Reference Roadmap

This roadmap explains which control references belong in this skill and how to use them safely. It is a planning map, not a substitute for licensed standards, books, project documents, or engineering review.

## Skill Core References

### ISA-5.1 Instrumentation Symbols And Identification

Role in this skill:

- Interpret function letters and tag families as hints.
- Normalize tag patterns and loop numbering.
- Distinguish measurement, indication, control, alarm, switching, and final control functions.

Use as:

- tag parsing wiki.
- symbol interpretation checklist.
- guardrail against overclaiming action from tag letters.

Do not use it to infer:

- fail action.
- safety function.
- SIL/PFD/IPL credit.
- control narrative.
- alarm priority or operator response.

### ISA-5.4 Instrument Loop Diagrams

Role in this skill:

- Define what loop diagrams should prove.
- Support sensor-controller-final-element grouping.
- Track signal path, terminals, panels, wiring, instrument air, power, and loop services.

Use as:

- loop-diagram evidence gate.
- signal-path and dependency wiki.
- field/panel/system boundary checklist.

This is the highest-priority missing reference for robust ControlLoopLayer extraction.

### Instrumentation And Control Systems Documentation

Role in this skill:

- Connect P&ID, index, datasheet, specification form, loop diagram, logic diagram, installation detail, location plan, and revision history.
- Decide which document should prove each claim.

Use as:

- evidence chain and missing-basis logic.
- HAZOP/LOPA documentation QA.
- conflict handling across drawings and tables.

### ISA-5.06 Functional Requirements Documentation For Control Software Applications

Role in this skill:

- Interpret control software, functional requirements, sequence behavior, permissives, state logic, and software-controlled actions.
- Separate normal BPCS behavior from interlock/SIS claims.

Use as:

- control narrative and DCS/PLC extraction wiki.
- required fields for software-based control relations.

## Wiki/Concept References

### Control Loop Foundation: Batch And Continuous Processes

Role:

- Explain PV, SP, MV, disturbance, feedback, cascade, ratio, feedforward, override, split-range, and batch/continuous operating modes.

Use as:

- concept wiki for chatbot answers.
- pattern library for loop classification.

Do not use as:

- project evidence that a specific loop exists.

### Fundamentals Of Process Control: Principles And Concepts

Role:

- Provide plain-language process-control concepts and common loop behavior.

Use as:

- general explanation wiki.
- context for HAZOP cause families involving controller tuning, sensor drift, actuator saturation, wrong setpoint, or loop in manual.

### Process Control Basics

Role:

- Short operational explanations for new users and chatbot answers.

Use as:

- quick wiki for non-specialist questions.

### Basic Math For Process Control

Role:

- Support units, signals, scaling, simple dynamic response, dead time, gain, and proportional/integral/derivative ideas.

Use as:

- optional wiki when the task involves scaling, percent output, range conversion, controller gain, or time response.

### Control Valve Primer

Role:

- Explain control valve roles, actuator relations, manipulated flow, valve sizing concepts, leakage, stiction, fail action evidence, and installation concerns.

Use as:

- final-control-element wiki.
- HAZOP cause family hints for stuck, saturated, mis-ranged, air-failed, or misapplied control valves.

Do not use to claim:

- actual fail-open/fail-closed behavior without datasheet or project evidence.

### ISA-TR5.9 PID Algorithms And Performance

Role:

- Explain PID loop pattern, tuning effects, loop mode, setpoint response, output limits, and performance terms.

Use as:

- PID pattern wiki when output requires algorithm-level reasoning.

## Related But Separate Skill References

Use a SIS/LOPA skill, not this skill alone, for:

- ISA-84 / IEC 61511.
- SIF definition.
- SIL target.
- proof test interval.
- IPL credit.
- independence from BPCS.
- safety lifecycle evidence.

## Copyright And Provenance Boundary

Some user-supplied filenames may identify public mirror sources. Do not extract, summarize, or reproduce copyrighted content from unverified or unauthorized copies. Build skill instructions as original operational guidance, and use only licensed project documents, legally available references, or user-owned notes as source evidence.


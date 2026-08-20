# Control Loop Wiki Index

This directory is the wiki library for the single `control-loop-layer-extractor` skill. These pages support chatbot answers, retrieval context, and detailed reasoning after `SKILL.md` has routed the task.

## Wiki Pages

| Wiki page | Use when |
| --- | --- |
| `tag-identification.md` | The task involves instrument tags, function letters, loop numbers, tag families, or tag grouping. |
| `loop-diagram.md` | The task involves loop diagrams, signal paths, wiring, terminals, field/panel boundaries, instrument air, or power. |
| `control-software-frs.md` | The task involves DCS/PLC logic, control narratives, functional requirements, permissives, sequences, or software commands. |
| `process-control-concepts.md` | The task needs PV/SP/MV, feedback, cascade, ratio, feedforward, override, split-range, or on-off control concepts. |
| `final-control-element.md` | The task involves FCV/PCV/LCV/TCV, on-off valves, actuators, VFDs, dampers, heaters, or manipulated variables. |
| `pid-algorithms.md` | The task specifically needs PID mode, tuning, output limits, windup, dead time, or performance reasoning. |

## Use Pattern

1. Start from `SKILL.md`.
2. Read only the wiki page needed for the current question.
3. Use project documents as evidence.
4. Use wiki guidance as reasoning support, not as proof that a project loop exists.

## Boundary

This wiki is not a separate skill collection. It does not create independent triggerable skills. It is a reference library loaded by the one `control-loop-layer-extractor` skill.


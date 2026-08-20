# Function Contract

## Agent Function

```text
Agent name: control-loop-layer-extractor
Function name: extract_control_loop_layer
Project method: Agentic Evidence-Grounded Multi-Pass Multimodal Graph Reconstruction
Project name: GraphRecon-HAZOP
Purpose: Convert process-control evidence into a traceable L4 Control And Safety Layer.
```

## Trigger Scope

Use this function when the user asks to:

- read loop control, control loop, loop diagram, or BPCS evidence.
- answer what controls a line, valve, pump, tank, vessel, compressor, exchanger, or node.
- map instrument tags into PV, controller, final element, manipulated variable, and controlled asset.
- build a graph layer for process control before HAZOP generation.
- verify whether a HAZOP control cause or safeguard has enough documentation basis.
- create or validate `ControlLoopLayer` JSON.

Do not use this function as the primary skill for:

- SIL verification, SIS lifecycle, or IPL credit. Use a SIS/LOPA skill.
- alarm rationalization as a standalone task. Use an alarm management skill.
- generic process-control tutoring with no extraction or evidence need. Use wiki-style answer only.

## Inputs

Accept any combination of:

- P&ID pages or extracted P&ID JSON.
- loop diagrams.
- instrument index or tag list.
- instrument specification forms.
- control narratives or operating descriptions.
- functional requirement specifications for DCS/PLC applications.
- cause-and-effect charts, interlock notes, permissive tables, alarm lists.
- GraphRecon L0-L3 evidence, entity, and connectivity layers.
- process description and HAZOP node definitions.

## Outputs

Primary output:

- `ControlLoopLayer` JSON following `references/control-loop-layer-schema.json`.

Secondary outputs:

- graph patch for GraphRecon L4 nodes and edges.
- evidence gap report.
- HAZOP integration notes.
- rejected or candidate control claims.

## Graph Layers Touched

Primary:

- L4 Control And Safety Layer.

Reads from:

- L0 Evidence Layer.
- L2 Entity Layer.
- L3 Connectivity Layer.
- L5 Semantic Process Layer when available.

Feeds:

- L5 Semantic Process Layer.
- L6 HAZOP Layer.

## Node Types

- `control_loop`
- `instrument`
- `sensor`
- `transmitter`
- `controller`
- `logic_solver`
- `final_element`
- `control_valve`
- `actuator`
- `drive`
- `controlled_asset`
- `signal_path`
- `utility_dependency`
- `control_document`
- `missing_basis`

## Edge Types

- `measures`
- `indicates`
- `transmits_signal_to`
- `controls`
- `commands`
- `manipulates`
- `mounted_on`
- `connected_to_process`
- `depends_on`
- `has_setpoint`
- `cascades_to`
- `overrides`
- `splits_to`
- `ratio_controls`
- `feedforward_to`
- `candidate_control`
- `evidence_supports`

## Evidence And Provenance Fields

Every node and edge should carry:

```json
{
  "source_file": "pid.pdf",
  "page": 1,
  "bbox": [0, 0, 0, 0],
  "document_type": "pid | loop_diagram | instrument_index | control_narrative | frs | cause_effect | datasheet | unknown",
  "method": ["ocr", "vision", "llm_verifier"],
  "agent": "control-loop-layer-extractor",
  "confidence": 0.0,
  "activity": "tag_detection | loop_grouping | role_assignment | edge_validation"
}
```

## Model Policy

- Prefer deterministic parsing for tag formats, JSON validation, and graph checks.
- Use LLM reasoning only to propose candidate role assignments, not to certify facts.
- Lower confidence when relation evidence comes only from tag naming or proximity.
- Mark uncertain facts as `unknown`, `candidate`, or `missing_basis`.

## Human Escalation

Escalate for human review when:

- fail action, trip action, control direction, safe state, or IPL credit is requested but not documented.
- P&ID, index, loop diagram, and control narrative disagree.
- the extracted loop affects high-severity HAZOP scenarios.
- missing evidence prevents deciding whether the loop is BPCS, alarm-only, interlock, SIS, or manual operation.


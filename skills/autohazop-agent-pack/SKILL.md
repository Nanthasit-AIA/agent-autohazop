---
name: autohazop-agent-pack
description: Build or review HAZOP/LOPA worksheets from PFDs, P&IDs, process descriptions, line lists, equipment datasheets, operating procedures, safeguards, alarms, interlocks, relief documents, and bundled engineering-standard references. Use when an agent needs one portable HAZOP skill that can trace equipment-line-valve-instrument context, derive operating and design envelopes, screen credible causes and consequences, assess severity, separate safeguards from IPLs, perform LOPA/risk-ranking logic with supplied company criteria, and flag missing process safety information without relying on other local skills.
---

# AutoHAZOP Agent Pack

## Core Rule

This is a portable single-skill HAZOP/LOPA pack. Do not assume any other local skill exists. Use only user-supplied project documents, this skill body, and the bundled references under `references/`.

Generate HAZOP content from engineering context, not from a fixed generic cause list. A generic checklist may be used as a prompt for completeness, but final rows must be credible for the node, operating mode, material, equipment arrangement, and safeguards.

## Mandatory Analysis Contract

When this skill is invoked, treat the bundled workflows and standards as the analysis foundation. Do not use them as optional background reading after rows are already drafted.

For HAZOP generation, first load `references/workflows/scgc-hazop-lopa-generation-method.md` and apply its seven generation passes as the controlling worksheet method. Other workflow and standard references then add node-specific technical detail.

Before producing HAZOP rows, the agent must build an internal `analysis_basis` with:

- Node boundary and design intent.
- Normal flow direction and connected upstream/downstream equipment.
- Operating mode, including startup, shutdown, maintenance, standby, abnormal, bypassed, isolated, or blocked-in states where relevant.
- Equipment-specific operating envelope, such as pump minimum flow/NPSH, tank level/venting limits, vessel MAWP/MDMT, PRD installation limits, piping class limits, or automation safe state.
- Design envelope, including design pressure, design temperature, material/class, corrosion allowance, rating, code, and mechanical limits when available.
- Control and protection layers: BPCS loops, alarms, interlocks, SIS/SIF, relief/depressuring, vents, overflow, check valves, procedures, and mechanical safeguards.
- Relevant standard references selected from `references/standards/`.
- Missing data that could change cause credibility, consequence severity, IPL credit, or risk ranking.

Only after this basis exists should the agent generate deviations, causes, consequences, safeguards, IPLs, and risk cells. If the basis is incomplete, produce useful partial rows but mark the exact missing basis instead of guessing.

## Foundation Behavior

Use the references as active reasoning rails:

- For a pump node, analyze suction, discharge, minimum flow, recycle, NPSH/cavitation, seals, driver, trips, and standby logic before writing pump causes.
- For a tank node, analyze level, overfill, venting, blanketing, roof type, drain/overflow, pressure/vacuum, product properties, foundation, and floating-roof modes before writing tank causes.
- For a pressure vessel, analyze design pressure/temperature, MAWP, MDMT, corrosion allowance, cyclic/fatigue context, testing basis, and overpressure protection before writing vessel causes.
- For relief or depressuring paths, analyze protected equipment, credible overpressure scenarios, inlet/outlet paths, isolation, discharge destination, backpressure, and relief system interactions before crediting relief safeguards.
- For instruments, alarms, interlocks, and SIS, analyze sensor, logic solver/controller, final element, trip action, safe state, bypass, independence, testing, and operator response before crediting protection.
- For procedures, analyze the actual operating mode, task step, temporary bypass/defeat, lineup, maintenance state, and safe operating limit before treating a procedure as a safeguard.

## Execution Flow

1. Load the SCGC HAZOP-LOPA generation method and use it as the row-generation gate.
2. Define the study scope, node boundary, design intent, operating mode, and available documents.
3. Read the PFD/P&ID as a process graph: equipment nodes, line edges, flow direction, valves, instruments, controls, utilities, relief/vent/drain paths, common headers, and package boundaries.
4. Select the relevant bundled standard references only when they match the node or document type.
5. Extract context needed for HAZOP: topology, operating envelope, design envelope, safeguards, alarms/interlocks/SIS, relief/venting, procedures, and missing information.
6. Generate deviations by pairing meaningful parameters and guide words for the node.
7. For each deviation, screen credible causes and trace unmitigated consequence paths before listing safeguards.
8. Assess safety, environmental, and asset/equipment severity separately; choose the governing severity.
9. Select initiating event likelihood from user/company basis when supplied; otherwise mark the basis missing.
10. Separate safeguards from credited IPLs. Credit IPLs only when independence, effectiveness, auditability, design basis, and management basis are established.
11. Perform initial and final risk ranking only with the supplied company matrix or rules.
12. Write recommendations that close a specific risk gap or missing basis.

## Workflow References

Load these references only as needed:

- Read `references/workflows/scgc-hazop-lopa-generation-method.md` first for graph-agent HAZOP generation, SCGC procedure gates, appendix-derived deviation prompts, IEL/PFD screening examples, IPL caveats, and final row QA.
- Read `references/workflows/end-to-end-hazop-lopa.md` for full HAZOP/LOPA worksheet drafting, review, and coordination.
- Read `references/workflows/methodology-guideline.md` for HAZOP/LOPA methodology, node definition, guide-word use, and worksheet rules.
- Read `references/workflows/pfd-pid-tracing.md` when reading PFD/P&ID topology, tracing upstream/downstream effects, recycle/common-header behavior, utilities, relief/vent/drain paths, and control-loop response.
- Read `references/workflows/cause-consequence.md` when deciding cause credibility, excluding weak or double-jeopardy causes, splitting rows, and writing unmitigated consequences.
- Read `references/workflows/severity-assessment.md` when assigning safety, environmental, and asset/equipment severity rationale.
- Read `references/workflows/lopa-ipl-assessment.md` when evaluating initiating event likelihood, safeguards, IPL qualification, PFD/credit, and mitigated likelihood.
- Read `references/workflows/risk-ranking.md` when combining governing severity and likelihood through the supplied risk matrix and checking recommendation triggers.

## Book-Wiki References

The existing project book-derived references remain useful after merging this pack. Load them only when the current node, deviation, or review question needs the topic:

- Read `references/per-book-skill-wiki-matrix.md` to map book-derived wiki topics to detailed local skills.
- Read `references/book-wiki/alarm-management.md` for alarm philosophy, rationalization, operator response, and alarm safeguard quality.
- Read `references/book-wiki/hazop-pha-security-review.md` for HAZOP/PHA quality, security review, and worksheet completeness.
- Read `references/book-wiki/incident-learning-and-human-factors.md` for incident learning, human error, and operator task credibility.
- Read `references/book-wiki/inherent-safety-siting-layout.md` for inherent safety, siting, layout, occupied building, and escalation context.
- Read `references/book-wiki/lopa-sil-sis.md` for LOPA, IPL, SIL, SIS/SIF, proof testing, and independence context.
- Read `references/book-wiki/loss-prevention-master-reference.md` for loss prevention, fire/explosion, toxic, and consequence escalation context.
- Read `references/book-wiki/psm-rbps-moc-documentation.md` for RBPS, PSM, MOC, procedure, audit, and documentation gaps.
- Read `references/book-wiki/reliability-data.md` for failure modes, reliability basis, and missing initiating-event data.
- Read `references/book-wiki/relief-fire-explosion-consequence.md` for relief, fire, explosion, BLEVE, VCE, flash fire, toxic release, and consequence analysis context.
- Read `references/book-wiki/risk-criteria-qra.md` for risk criteria, QRA, tolerability, and risk-ranking basis gaps.

## Standard Reference Selection

Load only the standard references relevant to the current node, document, or question:

- Read `references/standards/moe-toghraei-pid-development.md` for P&ID reading, topology, line tags, equipment arrangements, valves, instruments, PRDs, controls, utilities, and P&ID review quality.
- Read `references/standards/bs-en-1861-refrigerating-pid-layout-symbols.md` for refrigeration/heat-pump flow diagrams, refrigeration P&IDs, layout conventions, and symbols.
- Read `references/standards/dsf-spc-pip-020-piping-material.md` for piping material classes, pressure/temperature/material limits, branch connections, flange/gasket/bolting compatibility, and mechanical envelope checks.
- Read `references/standards/asme-bpvc-viii-2-pressure-vessel-design.md` for pressure vessel design envelopes, MAWP, MDMT, design pressure/temperature, corrosion allowance, testing, fatigue, cyclic service, and vessel overpressure protection context.
- Read `references/standards/api-610-iso-13709-centrifugal-pumps.md` for centrifugal pump operating envelopes, suction/discharge context, NPSH/cavitation, minimum flow, recycle, seal systems, driver trips, vibration/bearing monitoring, standby pumps, and pump safeguards.
- Read `references/standards/api-650-welded-tanks-oil-storage.md` for welded aboveground storage tank design basis, fixed/floating roofs, bottom/foundation, nozzles, overflow, overfill, pressure/vacuum, design metal temperature, specific gravity, anchorage, wind/seismic, and settlement context.
- Read `references/standards/api-2000-atmospheric-low-pressure-tank-venting.md` for atmospheric/low-pressure tank venting, PV valves, inbreathing/outbreathing, emergency vents, blanketing, flame arresters, vapor recovery, and vacuum/overpressure scenarios.
- Read `references/standards/api-520-part-ii-prd-installation.md` for PRD installation, inlet/outlet piping, isolation valves, rupture disks, bonnet/pilot vents, drains, chatter, stability, and installation quality flags.
- Read `references/standards/api-521-pressure-relieving-depressuring-systems.md` for overpressure scenarios, relief systems, depressuring, flare/vent disposal, blocked outlet, fire, utility failure, exchanger tube rupture, thermal expansion, and flare headers.
- Read `references/standards/ccps-operating-maintenance-procedures.md` for operating modes, startup, shutdown, maintenance, abnormal operation, procedural safeguards, safe operating limits, validation, and MOC.
- Read `references/standards/ccps-safe-automation-chemical-processes.md` for BPCS, alarms, interlocks, SIS/SIF, cause-and-effect, control narratives, bypasses, FAT/SAT, diagnostics, and automation-layer independence.
- Read `references/standards/ccps-hazard-evaluation-procedures.md` for PHA/HAZOP planning, hazard evaluation technique selection, safeguard adequacy, LOPA handoff, MOC reviews, revalidation, human factors, and action closure.
- Read `references/standards/bs-en-31010-risk-assessment-techniques.md` for risk assessment technique selection, HAZOP method quality, LOPA screening, bow-tie, FMEA/FMECA, FTA, ETA, SWIFT, risk matrix use, ALARP, uncertainty, and control effectiveness.
- Read `references/standards/hydrocarbon-processing-refining-processes.md` for refinery process block context, licensed unit purposes, feed/product/service clues, and HAZOP node orientation in refinery units.

## Context Extraction Schema

Use this shape internally before generating rows:

```yaml
source:
  documents: []
  drawing_or_sheet: null
  revision: null
  assumptions: []
  missing_information: []
node:
  id: null
  boundary: null
  design_intent: null
  operating_mode: normal | startup | shutdown | maintenance | abnormal | standby | unknown
topology:
  upstream: []
  downstream: []
  connected_equipment: []
  connected_lines: []
  valves: []
  instruments: []
  controls: []
  relief_vent_drain_paths: []
  utilities: []
operating_envelope:
  normal_pressure: null
  normal_temperature: null
  normal_flow: null
  normal_level: null
  safe_operating_limits: []
design_envelope:
  design_code: null
  design_pressure: null
  design_temperature: null
  material_or_class: null
  corrosion_allowance: null
  mechanical_limits: []
safeguards:
  mechanical: []
  control: []
  alarms: []
  interlocks: []
  sis_sif: []
  relief_depressuring: []
  procedures: []
hazop_basis:
  relevant_standards: []
  credible_deviations: []
  cause_prompts: []
  consequence_prompts: []
  missing_basis: []
```

## Worksheet Output

Use the user's worksheet columns when supplied. Otherwise use:

- Node
- Design intent
- Operating mode
- Parameter
- Guide word
- Deviation
- Cause
- Consequence
- Safety severity basis
- Environmental severity basis
- Asset/equipment severity basis
- Governing severity
- Initiating event likelihood basis
- Initial risk
- Existing safeguards
- Candidate IPLs
- Credited IPLs
- Final likelihood
- Final risk
- Recommendation/action
- Owner
- Missing basis / assumptions

## Quality Rules

- Keep normal operating values separate from design limits and safe operating limits.
- Mark missing fields as `missing`; mark inferred fields as `inferred` and state the basis.
- Do not invent design pressure, design temperature, material hazards, flow direction, valve fail position, relief destination, SIL level, IPL credit, or risk rank.
- Do not mix safeguards into unmitigated consequence wording.
- Do not credit a safeguard as an IPL unless the specific scenario has independence, effectiveness, auditability, design basis, and management basis.
- Do not assign final numeric risk without the user's severity scale, likelihood scale, risk matrix, and IPL criteria.
- Prefer fewer high-quality credible rows over many generic rows when the user asks for quality.
- Expand shorthand references such as `See No Flow` into a complete event path when producing final rows.
- Record conflicts between P&ID, datasheet, line list, procedure, and standard context instead of silently reconciling them.
- Run the SCGC final row QA before output: credible cause, unmitigated consequence, separated safeguards/IPLs, screening-only risk when criteria are missing, and recommendation tied to a specific gap.

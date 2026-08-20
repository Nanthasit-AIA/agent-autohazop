# CCPS Guidelines For Hazard Evaluation Procedures

Use this reference when planning, checking, facilitating, or extracting context for process hazard evaluations such as PHA, HAZOP, What-if, What-if/Checklist, FMEA, FTA, ETA, bow-tie, LOPA handoff, safety review, MOC hazard review, cyclic revalidation, procedure-based operation review, human factors review, chemical reactivity review, or facility siting review.

This is a derived working guide. It does not reproduce CCPS tables, forms, worked examples, checklists, or detailed method text. It does not replace the CCPS book, company PHA/LOPA procedures, regulatory requirements, project risk matrices, qualified facilitation, or discipline engineering review.

## Source Traceability

- Source book: CCPS / AIChE, "Guidelines for Hazard Evaluation Procedures", Third Edition.
- Part I covers hazard evaluation procedures.
- Chapter 1 covers hazard evaluation context, relation to risk management, incident anatomy, safeguards, lifecycle use, regulations, and limitations.
- Chapter 2 covers preparation: infrastructure, objectives, scope/boundaries, information requirements, software, personnel/skills, schedule, execution, and initial team review.
- Chapter 3 covers hazard identification: material properties, process conditions, experience, interaction matrices, hazard identification results, worst-case consequence screening, and inherent safety review.
- Chapter 4 covers non-scenario-based procedures: PHA, safety review, relative ranking, and checklist analysis.
- Chapter 5 covers scenario-based procedures: What-if, What-if/Checklist, HAZOP, FMEA, FTA, ETA, cause-consequence, bow-tie, and related techniques.
- Chapter 6 covers selection of hazard evaluation techniques, MOC hazard reviews, combined reviews, lifecycle stages, and integration of occupational safety, environmental, reliability, maintainability, quality, and security concerns.
- Chapter 7 covers risk-based determination of safeguard adequacy: scenario selection, severity, initiating cause frequency, safeguard effectiveness, risk matrix/direct calculation, and LOPA.
- Chapter 8 covers follow-up: recommendations, prioritization, documentation, management response, action resolution, communication of findings, and use over the plant lifetime.
- Chapter 9 covers special applications: procedure-based operations, programmable systems, chemical reactivity hazards, combinations of tools, human factors/HRA, and facility siting.
- Part II provides worked examples across lifecycle stages such as R&D, conceptual design, pilot plant, detailed engineering, construction/startup, routine operation, cyclic review, expansion, incident investigation, and decommissioning.

## Applies To

- PHA/HAZOP preparation, workshop facilitation, worksheet quality review, and action follow-up.
- Selecting hazard evaluation techniques for different maturity levels: R&D, conceptual design, pilot plant, detailed design, startup, operation, MOC, revalidation, incident investigation, expansion, and decommissioning.
- Translating P&ID context into scenario-based hazard evaluation rows.
- Deciding whether safeguards are adequate or need LOPA, SIL review, relief review, procedure improvement, or design change.
- Checking whether a hazard evaluation is complete enough to support HAZOP/LOPA work.

## Does Not Provide

- Company-specific risk criteria, LOPA probability values, SIL target rules, legal compliance determination, or final engineering acceptance.
- A substitute for a trained facilitator or multidisciplinary workshop.
- Final relief sizing, dispersion modelling, fire modelling, QRA, mechanical design, or functional safety lifecycle deliverables.

## Hazard Evaluation Planning Schema

Use this schema before producing HAZOP rows or recommendations.

```yaml
hazard_evaluation_plan:
  source:
    document:
    page_or_sheet:
    revision:
  study_definition:
    study_type:
    objective:
    decision_to_support:
    lifecycle_stage:
    facility_or_unit:
    nodes_or_scope:
    boundaries:
    interfaces:
    exclusions:
    assumptions:
  required_information:
    pfd:
    pid:
    heat_material_balance:
    equipment_datasheets:
    line_list:
    instrument_index:
    cause_and_effect:
    control_narrative:
    relief_summary:
    operating_procedures:
    maintenance_procedures:
    incident_history:
    chemical_hazard_data:
    layout_or_siting_data:
  team:
    facilitator:
    scribe:
    process_engineer:
    operations:
    maintenance:
    instrumentation_controls:
    mechanical_piping:
    process_safety:
    specialist_needed:
  method_selection:
    selected_method:
    selection_reason:
    scenario_based: null
    non_scenario_based: null
    combined_methods: []
  worksheet_controls:
    risk_matrix_source:
    safeguard_credit_rules:
    recommendation_rules:
    action_tracking_system:
    revalidation_basis:
  output:
    hazards_identified: []
    scenarios: []
    safeguards: []
    recommendations: []
    lopa_candidates: []
    missing_information: []
```

## Preparation Rules

- Define the objective first: hazard identification, design improvement, operability review, MOC screening, cyclic revalidation, incident follow-up, safeguard adequacy, or LOPA candidate selection.
- Define scope and boundaries explicitly. Include package boundaries, tie-ins, utilities, relief systems, control system interfaces, bypasses, startup/shutdown paths, maintenance isolation, and temporary operations.
- Gather current documents before the meeting. Stale P&IDs or missing operating procedures can turn a HAZOP into guesswork.
- Identify information gaps early and decide whether to defer the node, proceed with assumptions, or create a pre-work action.
- Use a multidisciplinary team. At minimum, include process/design knowledge and real operating/maintenance experience.
- Schedule enough time for scenario development and action quality, not only for filling rows.
- Run an initial team review to align on objective, method, guidewords/prompts, risk criteria, safeguard credit rules, action wording, and documentation style.

## Hazard Identification Inputs

Look beyond P&ID topology. Hazard evaluation should also consider:

- Material properties: toxicity, flammability, reactivity, instability, corrosivity, phase behavior, vapor pressure, dust explosibility, incompatibility, environmental harm, and decomposition potential.
- Process conditions: pressure, temperature, flow, inventory, residence time, concentration, level, heat input/removal, agitation, vacuum, and abnormal energy sources.
- Process experience: incidents, near misses, known failure modes, maintenance findings, alarm history, trip history, relief events, leaks, fouling, plugging, corrosion, operator workarounds, and nuisance shutdowns.
- Interaction matrices: chemical compatibility, utility/process cross-contamination, adjacent equipment effects, shared headers, common drains, relief/vapor recovery interactions, and simultaneous operations.
- Initial worst-case consequences: enough screening to recognize major accident potential and choose proper review depth.
- Inherent safety opportunities: eliminate, substitute, minimize, moderate, simplify, and make error-tolerant before adding protective layers.

## Technique Selection

Select the method based on lifecycle stage, available information, complexity, consequence potential, and decision need.

| Situation | Preferred Technique | Why |
| --- | --- | --- |
| Early concept with limited design detail | PHA, checklist, relative ranking, What-if | Finds major hazards without pretending detail exists |
| Mature P&ID/process design | HAZOP, What-if/Checklist, FMEA for equipment details | Systematic scenario development from design intent |
| MOC affecting a narrow system | Safety review, What-if/Checklist, focused HAZOP | Efficient review of changed hazards and interfaces |
| Need to understand one top event | FTA | Builds causal logic for a defined event |
| Need to understand outcomes after an initiating event | ETA | Shows consequence paths through safeguard success/failure |
| Need barrier communication | Bow-tie or cause-consequence | Shows threats, top event, prevention, mitigation, escalation factors |
| Need semi-quantitative safeguard adequacy | LOPA | Tests one cause-consequence scenario against tolerable risk |
| Need component failure review | FMEA/FMECA | Starts from function and failure modes |
| Need operating or maintenance task review | Procedure HAZOP, What-if/Checklist, HRA | Captures human actions, timing, and procedural weaknesses |
| Incident investigation support | RCA, FMEA, HRA, bow-tie update | Connects causes, failed safeguards, and corrective actions |
| Decommissioning or temporary operation | What-if/Checklist, PHA, procedure HAZOP | Handles nonroutine steps and changing boundaries |

Do not choose a complex method just to look rigorous. A simple method done well can outperform a complex method done poorly. Conversely, do not use a checklist alone for a high-hazard mature process when scenario interactions need systematic review.

## Non-Scenario-Based Procedures

Use these for screening, early lifecycle decisions, or completeness checks.

- PHA: early hazard screening when design detail is limited. Output should include hazards, possible causes, consequences, existing or needed controls, and recommendations for further study.
- Safety review: field or document review for compliance with known requirements, readiness, or change impact. Useful for pre-startup, MOC, construction/startup, and periodic reviews.
- Relative ranking: compare units, options, inventories, or operations to prioritize deeper review. Use only within a consistent basis.
- Checklist analysis: verify against known standards, company requirements, lessons learned, and recurring failure modes. Good for completeness, weak for novel hazards.

## Scenario-Based Procedures

Use these when the goal is to develop cause-consequence-safeguard scenarios.

- What-if: structured questions explore credible abnormal events. Useful when a full HAZOP is too heavy or design detail is moderate.
- What-if/Checklist: combines creativity with known hazard prompts. Good for MOC, batch/nonroutine operations, and smaller systems.
- HAZOP: systematic deviation review using guidewords and design intent. Best for mature P&IDs, procedures, control logic, and operating modes.
- FMEA: begins with component/function failure modes and asks what effects follow. Useful for equipment packages, controls, mechanical systems, and maintainability.
- FTA: starts from a top event and works backward to combinations of causes. Useful for proving causal logic and identifying common-cause contributors.
- ETA: starts from an initiating event and works forward through protective layer successes/failures. Useful for consequence-path analysis.
- Cause-consequence and bow-tie: combine cause-side and consequence-side logic. Useful for barrier mapping and communication.

## HAZOP Execution Rules

- Start each node with design intent, normal operating envelope, key safeguards, and operating modes.
- Apply guidewords to parameters that matter: flow, pressure, temperature, level, composition, phase, reaction, mixing, addition, utility, containment, isolation, startup, shutdown, maintenance, and human action.
- For each deviation, identify credible causes before consequences. Avoid writing vague causes such as "failure" without mechanism.
- Consequences should describe what can happen if safeguards fail or are absent, not only the immediate upset.
- Safeguards must be tied to the specific scenario path. Do not list unrelated alarms, procedures, or relief devices.
- Recommendations should address a real gap and be written so closure can be verified.
- If the team lacks information, record a data gap instead of inventing design assumptions.
- If a scenario is high consequence, complex, or safeguard adequacy is uncertain, mark it for LOPA, relief review, functional safety review, siting review, reactivity review, or specialist analysis.

## Worksheet Quality Schema

Use this compact structure when reviewing or generating HAZOP rows.

```yaml
hazard_evaluation_row:
  node:
  design_intent:
  operating_mode:
  guideword_or_prompt:
  deviation:
  cause:
  consequence:
  existing_safeguards:
    preventive: []
    mitigative: []
    detection_or_alarm: []
    procedural: []
    relief_or_depressuring: []
    sis_or_interlock: []
  risk_ranking:
    severity:
    likelihood:
    risk:
    criteria_source:
  recommendation:
    action:
    owner:
    due_date:
    closure_evidence_required:
  follow_up:
    lopa_required:
    specialist_review:
    missing_information:
```

## Safeguard Adequacy And LOPA Handoff

Use this section when deciding whether HAZOP safeguards are enough.

- Separate a safeguard from an IPL. A safeguard may reduce risk; an IPL must meet the governing independence, effectiveness, auditability, availability, and response-time requirements.
- Evaluate scenario severity, initiating cause frequency, and safeguard effectiveness before deciding adequacy.
- Risk matrix ranking is useful for screening, but use direct calculation or LOPA when high-consequence scenarios need a more defensible decision.
- LOPA should receive one initiating cause and one consequence at a time. Do not mix unrelated causes or consequences in one LOPA row.
- Check common-cause and dependency: shared sensors, shared logic solver, shared utility, same operator, same alarm display, same maintenance bypass, same plugged impulse line, or same relief header.
- A safeguard is weak evidence if it lacks proof test, inspection, maintenance, set point, alarm response time, operator training, procedure control, or bypass management.
- If a recommendation adds a safeguard, define the performance expectation: what it detects/prevents/mitigates, when it acts, how reliable it must be, and how it will be verified.

## Follow-Up And Closure

Hazard evaluation is incomplete until findings are resolved.

- Recommendations should be specific, assignable, technically meaningful, and verifiable.
- Prioritize actions using consequence, likelihood, uncertainty, safeguard weakness, regulatory exposure, and implementation urgency.
- Management response should accept, modify, or reject recommendations with documented rationale.
- Closure evidence should demonstrate that the hazard gap has been addressed, not merely that a document was edited.
- Communicate special findings to affected units, similar equipment, procedures, training, inspection programs, and future projects.
- Maintain study results over the plant lifetime so revalidation can start from known assumptions, open issues, incidents, MOCs, and changed safeguards.

## Special Applications

- Procedure-based operations: review step sequence, wrong action, skipped step, too early/late action, wrong lineup, temporary bypass, communication handoff, confirmation step, and recovery path.
- Programmable systems: review sensor failure, logic error, software change, override, bypass, permissive, trip, common cause with BPCS, HMI ambiguity, alarm overload, cybersecurity interface, and proof-test coverage.
- Chemical reactivity: review incompatibility, contamination, runaway, decomposition, polymerization, wrong addition order, heat removal failure, scale-up, hold time, and emergency relief basis.
- Human factors and HRA: review task complexity, workload, time pressure, visibility, accessibility, labeling, ergonomics, alarm clarity, training, procedure usability, and error recovery.
- Facility siting: review toxic, fire, explosion, occupancy, building vulnerability, control room location, occupied portable buildings, traffic, emergency response, and escalation effects.
- Combined tools: use HAZOP to identify scenarios, LOPA to test safeguard adequacy, bow-tie to communicate barriers, FTA/ETA for complex logic, and checklist to verify known requirements.

## Lifecycle Use

- R&D: What-if and hazard identification from material/reactivity data.
- Conceptual design: PHA, inherent safety review, relative ranking, and early consequence screening.
- Pilot plant: HAZOP and procedure review with strong attention to scale-up uncertainty.
- Detailed engineering: HAZOP, FMEA, FTA/ETA, LOPA, relief review, and functional safety review.
- Construction/startup: checklist, safety review, PSSR support, procedure HAZOP, and temporary operation review.
- Routine operation: cyclic HAZOP revalidation, MOC review, operating procedure review, alarm/interlock review, and incident learning.
- Expansion: compare new and existing hazards; use relative ranking plus HAZOP/LOPA for changed nodes.
- Incident investigation: connect root causes to failed or missing safeguards and update HAZOP/bow-tie/LOPA assumptions.
- Decommissioning: What-if/Checklist and procedure review for cleaning, isolation, draining, purging, demolition, and temporary utilities.

## Missing Information To Flag

- Study objective, scope, boundaries, or exclusions are unclear.
- P&IDs, procedures, cause-and-effect, relief basis, or operating data are missing or not current.
- Team lacks operations, maintenance, controls, process safety, or specialist participation required for the hazard.
- Risk matrix, safeguard credit rules, or LOPA criteria are not defined.
- Node design intent is missing.
- Operating modes such as startup, shutdown, maintenance, bypassed, isolated, standby, and emergency are not covered.
- Safeguards are listed without scenario-specific function or effectiveness evidence.
- High-consequence scenarios are closed with qualitative judgement despite major uncertainty.
- Recommendations lack owner, due date, priority, or closure evidence.
- MOC, incident history, action status, or previous revalidation findings are not available.
- Human factors, chemical reactivity, programmable systems, and facility siting are omitted despite being relevant.

## Output Rule

When using this reference, produce hazard evaluation guidance that is traceable to the study decision. State the selected technique, why it fits the lifecycle stage and information quality, what inputs are required, what output should be produced, and what limitations or follow-up analyses remain.

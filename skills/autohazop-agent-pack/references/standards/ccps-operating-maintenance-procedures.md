# CCPS Guidelines for Writing Effective Operating and Maintenance Procedures

Use this reference to extract practical operating, maintenance, abnormal, startup, shutdown, and emergency context from procedures for HAZOP/LOPA work. It is derived from the CCPS book on effective operating and maintenance procedures and focuses on what an agent should capture: procedure type, operating mode, prerequisites, safe operating limits, cautions, expected equipment response, corrective action, emergency entry/exit criteria, procedure control, training, validation, and MOC links.

This is a derived working guide. It does not reproduce the book's sample formats, checklists, or operating-limit tables and does not replace approved site procedures, PSM/RMP compliance programs, permit-to-work, lockout/tagout, equipment datasheets, alarm rationalization, SIS lifecycle documents, emergency response plans, or jurisdictional requirements.

## Source Traceability

- Source book: `Guidelines for Writing Effective Operating and Maintenance Procedures`, Center for Chemical Process Safety, AIChE, 1996.
- Process safety, environmental, quality, and regulatory procedure considerations: chapter 2.
- Procedure management system design, task selection, training, and continuous improvement: chapter 3.
- Operating and maintenance procedure writing, resources, human factors, format, precautions, prerequisites, steps, maintenance, and batch considerations: chapter 4.
- Procedure evaluation criteria and usability checks: chapter 5 and Appendix E.
- Emergency Operating Procedures (EOPs), initiating events, emergency recognition, human factors, decision aids, and links to the Emergency Response Plan: chapter 6.
- Procedure control, revisions, review, approval, in-use evaluation, electronic document control, and MOC interface: chapter 7.
- Task selection, performance evaluation, sample formats, and operating-limit table concepts: Appendices C, D, F, and G.

## Applies To

- Extracting operation-mode context from approved or draft procedures.
- Converting procedures into HAZOP/LOPA context for normal, startup, shutdown, abnormal, emergency, maintenance, batch, temporary, and nonroutine operation.
- Identifying procedural safeguards, operator actions, preconditions, verification steps, decision branches, hold points, and acceptance criteria.
- Checking whether a procedure gives enough information to keep the process inside safe operating limits or to reach a defined safe/stable state.
- Reviewing whether procedure changes, equipment changes, PHA findings, incidents, training gaps, or MOC records should trigger procedure revision.

## Does Not Provide

- Site-specific operating limits or emergency actions.
- A basis to credit a procedure as an IPL by itself.
- Proof that an operator response has enough time, independence, reliability, or training basis.
- Final approval that a procedure is compliant, current, or fit for use.
- Replacement for field validation, operator training, drills, or management approval.

## Procedure Context Schema

When reading a procedure, extract these fields. Preserve the source wording for tags, numbers, limits, and document IDs, but summarize instructions rather than copying long procedure text.

```yaml
procedure_context:
  source:
    document:
    procedure_id:
    title:
    revision:
    approval_date:
    effective_date:
    required_review_date:
    page_or_section:
  procedure_class:
    type:
    operating_mode:
    task_frequency:
    criticality:
    complexity:
    temporary_or_permanent:
  scope:
    purpose:
    unit_area:
    equipment_tags:
    line_or_pid_refs:
    applicable_conditions:
    excluded_conditions:
  prerequisites:
    plant_state:
    lineups:
    permits:
    isolation_loto:
    support_systems:
    personnel_notifications:
    tools_equipment_ppe:
    prior_quality_or_lab_approval:
  operating_limits:
    normal_range:
    alarms:
    interlocks:
    never_exceed_limits:
    safe_upper_limit:
    safe_lower_limit:
    consequence_of_deviation:
    required_action:
    monitoring_location:
  step_logic:
    steps:
      - step_id:
        action:
        equipment_or_instrument:
        expected_response:
        verification:
        caution_warning_note:
        decision_condition:
        branch_target:
        hold_point:
        corrective_action:
  safeguards:
    engineered_safeguards_referenced:
    alarms_operator_action:
    interlocks_or_sis:
    relief_or_mechanical:
    procedural_controls:
    communications:
  emergency_context:
    initiating_symptoms:
    automatic_system_actions:
    eop_entry_criteria:
    immediate_actions:
    safe_or_stable_state:
    eop_exit_criteria:
    emergency_response_plan_trigger:
    evacuation_or_shelter_action:
  maintenance_context:
    work_scope:
    isolation_boundary:
    depressurize_drain_vent_purge:
    inspection_test_acceptance_criteria:
    post_maintenance_test:
    return_to_service:
    records:
  governance:
    owner_or_sponsor:
    reviewers:
    approver:
    training_required:
    validation_method:
    moc_link:
    procedure_change_request:
    in_use_evaluation:
  hazop_use:
    credible_deviations:
    causes_revealed:
    consequences_revealed:
    safeguards_to_review:
    recommendations:
    missing_information:
```

## Procedure Types To Distinguish

Classify a procedure before extracting safeguards:

- Normal operating procedure.
- Startup procedure, including cold start, warm start, startup after maintenance, and startup after emergency shutdown.
- Normal shutdown procedure.
- Emergency shutdown or EOP.
- Abnormal operating procedure.
- Maintenance procedure.
- Inspection, test, and calibration procedure.
- Batch charging, reaction, transfer, cleaning, or changeover procedure.
- Temporary, nonroutine, or one-time procedure.
- Administrative procedure, including procedure control, MOC, training, or document control.

If a procedure mixes classes, split the extraction by mode. A startup step, maintenance isolation step, and emergency action should not be treated as the same operating condition.

## Operating Mode Extraction

For each step or section, assign one or more modes:

| Mode | Extraction focus |
|---|---|
| Normal | Intended lineup, operating range, routine checks, control response, alarm response, and normal transfer path. |
| Startup | Initial conditions, purge/inerting, warmup/cooldown, utility availability, permissives, first-feed conditions, ramp limits, and transition to steady operation. |
| Shutdown | Stop sequence, inventory control, depressuring, draining, purge, cooldown, isolation, and final safe state. |
| Maintenance | Permit, LOTO, isolation, de-energization, draining, venting, purging, blinding/spools, confined-space or line-break controls, testing, and return to service. |
| Abnormal | Symptoms, diagnosis, temporary controls, escalation criteria, corrective action, and monitoring frequency. |
| Emergency | EOP trigger, immediate action, safe/stable state, role assignment, evacuation/ERP trigger, and exit back to operating procedure. |
| Batch | Step sequence, charge quantities, hold points, QC release, completion criteria, abnormal branches, and cleanup/changeover. |
| Temporary/nonroutine | Temporary equipment, bypasses, defeat of safeguards, changed limits, extra monitoring, authorization, and expiration condition. |

Mark a mode as `missing` if the procedure title implies it but the body does not define initial state, final state, or limits.

## Safe Operating Limits

Appendix G emphasizes that operating-limit information should connect process variables, monitoring locations, limits, consequences, alarms/interlocks, and required actions. Extract limits as structured context:

```yaml
safe_operating_limit:
  variable:
  equipment_or_system:
  monitoring_location:
  normal_operating_range:
  alarm_setpoints:
  interlock_or_trip_setpoints:
  safe_lower_limit:
  safe_upper_limit:
  never_exceed_limit:
  consequence_if_outside_normal_range:
  consequence_if_outside_safe_limit:
  required_operator_action:
  referenced_procedure:
  investigation_or_reporting_trigger:
```

Rules:

- Keep normal operating range, alarm setpoint, trip setpoint, safe limit, never-exceed limit, design pressure/temperature, and MAWP separate.
- If the procedure only says "operate normally" without a numeric range, record the range as `missing`.
- If an action is given without a consequence, record consequence as `missing`; do not invent it.
- If the limit is in an external table, line list, datasheet, or DCS screen, reference that source and mark the value as `referenced`.
- For HAZOP, use safe operating limits to identify deviations and consequences, not to certify equipment design.

## Procedure Sections To Extract

Minimum useful sections:

- Purpose: task intent and final outcome.
- References: P&IDs, MSDS/SDS, equipment manuals, PHA findings, safe work practices, vendor manuals, operating-limit tables, task lists, and related procedures.
- Precautions: hazards, why they matter, consequence of ignoring them, and any required quality or environmental controls.
- Special tools/equipment: PPE, special tools, parts, spool pieces, blinds, test devices, chemicals, calibration equipment, and communication devices.
- Prerequisites: plant status, required lineup, support systems, qualifications, notifications, approvals, permits, LOTO, fire protection, lab/QC release, and initial process conditions.
- Steps: action, sequence, expected response, verification, decision branch, alarm/interlock reference, corrective action, and final state.
- Acceptance criteria: test limits, inspection criteria, leak-test criteria, calibration tolerance, cleanliness, torque, pressure hold, or quality release.
- Responsibilities: operator, control-room operator, field operator, maintenance craft, supervisor, engineer, manager, emergency response team, or contractor.
- Records: logs, forms, shift handover, inspection report, permit closure, calibration record, training record, or incident investigation trigger.

## Step-Level Extraction Rules

For each procedure step, ask:

- What physical action is required?
- Which tag, valve, switch, pump, instrument, line, or equipment item is involved?
- What sequence dependency exists?
- What should the process, instrument, or equipment do after the action?
- What value, position, alarm status, panel indication, sample result, or field condition confirms success?
- What safe operating limit or acceptance criterion governs the step?
- What should the user do if the expected response does not occur?
- Does the step require communication, approval, second-person verification, or hold point?
- Does the step introduce a temporary bypass, defeated safeguard, open drain/vent, manual mode, blind/spool change, or abnormal lineup?

Record missing expected response or verification as a quality gap. These are often important HAZOP findings because they hide loss of control or delayed recognition of a deviation.

## Procedural Safeguards And IPL Screening

Treat procedure-based controls conservatively.

A procedure step may be a procedural safeguard when it is specific, documented, available to the user, trained, and linked to a defined hazard or operating limit. Examples:

- Verify a valve lineup before introducing hazardous material.
- Stop feed when a temperature or pressure limit is approached.
- Increase monitoring frequency after an alarm or abnormal indication.
- Confirm isolation, depressurization, draining, and purging before maintenance.
- Follow an EOP to place the process in a safe or stable state.

Do not credit a procedure as an IPL unless the LOPA basis separately establishes:

- Independence from the initiating cause and other credited safeguards.
- Clear trigger or demand condition.
- Feasible operator response time.
- Reliable indication available where the operator acts.
- Trained and qualified personnel.
- Documented action, verification, and auditability.
- Human-factors suitability under the expected stress and workload.
- Periodic validation, drills, or performance evaluation.

If those elements are absent, list it as `procedural safeguard - credit not established`.

## Maintenance Procedure Context

For maintenance procedures, extract:

- Equipment tag, service, and protected/affected systems.
- Work boundary and whether upstream/downstream isolation is defined.
- LOTO and try/verify requirements.
- Depressurization, draining, venting, purging, washing, neutralization, or inerting steps.
- Blinding, spool removal, line breaking, confined-space, hot-work, excavation, or electrical permit links.
- Required tools, parts, PPE, lifting/rigging, and vendor instructions.
- Inspection, testing, calibration, and acceptance criteria.
- Post-maintenance leak test, functional test, trip/interlock proof test, alarm test, or rotation check.
- Return-to-service lineup and restoration of bypassed/defeated safeguards.
- Records, signoffs, and next inspection/test frequency.

Quality flags:

- Isolation boundary unclear.
- No verification that equipment is de-energized, depressurized, drained, vented, or purged.
- Return-to-service steps do not restore normal valve positions, auto/manual modes, interlocks, alarms, car seals, blinds, or bypasses.
- Acceptance criteria are absent for inspection, test, calibration, or leak check.
- Procedure does not say what to do when a test fails.

## Emergency Operating Procedure Context

An EOP should help the user recognize an emergency, act quickly, stabilize the process, and know when to invoke the Emergency Response Plan.

Extract:

```yaml
eop_context:
  event_or_symptom:
  initiating_conditions:
  automatic_system_actions:
  immediate_operator_actions:
  equipment_to_isolate_or_stop:
  valves_to_open_or_close:
  alternate_route_or_dump_path:
  monitoring_required:
  safe_or_stable_state:
  escalation_criteria:
  emergency_response_plan_trigger:
  roles:
  communication:
  evacuation_or_assembly:
  exit_to_normal_or_shutdown_procedure:
```

EOP quality checks:

- Entry criteria are explicit and observable.
- The first actions are short, direct, and feasible under stress.
- Roles are assigned when more than one person is involved.
- Decision aids use simple yes/no questions, tables, or flow logic.
- The EOP states how to reach a safe/stable condition or controlled shutdown.
- It distinguishes EOP actions from the broader Emergency Response Plan.
- It gives escalation criteria for alarms, releases, fire, fumes, concentration, loss of containment, or loss of critical utilities.
- It tells the user where to go after stabilization: normal operation, shutdown, maintenance, or ERP.

Flag an EOP if it requires the user to search through many documents, if trigger conditions are vague, if actions are inconsistent with alarms/interlocks, or if the procedure has no controlled accessible copy for emergency use.

## Procedure Management System

When reviewing a procedure library or procedure program, extract:

- How procedure needs are identified: task list, PHA, incident, audit, training needs, MOC, new equipment, changed materials, changed sequence, user feedback, or regulatory requirement.
- How procedures are prioritized: frequency, criticality, complexity, hazard potential, environmental impact, and quality impact.
- Who writes, reviews, approves, owns, distributes, and revises procedures.
- How users participate in writing and review.
- How obsolete versions are removed or blocked from use.
- How training is completed before implementation.
- How procedures are validated: simulation, dry run, field performance, water batch, actual use, drill, or performance evaluation.
- How current accuracy is periodically certified or reviewed.
- How electronic and hard-copy access is controlled, including backup for power/computer failure.

Procedure control should interface with MOC. A change in equipment, process technology, materials, control logic, operating sequence, auxiliary systems, limits, or operating method can require procedure revision before implementation. A requested procedure change can also trigger MOC when it changes the process or risk profile.

## Task Selection

Appendix C supports task-based selection of procedures. Use this logic when deciding whether a missing procedure is a gap:

```yaml
task_screen:
  job_or_area:
  task:
  starting_point:
  stopping_point:
  frequency:
  criticality:
  complexity:
  safety_impact:
  environmental_impact:
  quality_impact:
  regulatory_requirement:
  written_procedure_needed:
  basis:
```

Written procedures are especially important for tasks that are infrequent, complex, critical, hazardous, performed by multiple roles or shifts, required by regulation, or vulnerable to error during startup, shutdown, maintenance, emergency response, or batch transitions.

## Validation And Training Evidence

Extract training and validation context separately from procedure text:

- Required qualification or certification level.
- Training required before first use or after revision.
- Drill or simulation requirement for EOPs.
- Performance evaluation record.
- Whether a typical qualified user has performed or simulated the procedure as written.
- Open comments from users, supervisors, engineering, safety, environmental, quality, or maintenance reviewers.
- Date of last review and next required review.

If a procedure is technically detailed but unvalidated, flag `procedure accuracy not field-validated`. If a procedure credits operator response without training or drills, flag `operator action reliability not established`.

## HAZOP And LOPA Use

Use procedure context to strengthen these parts of a HAZOP/LOPA worksheet:

- Node design intent: normal lineup, operating range, batch state, startup/shutdown transition, or maintenance state.
- Deviations: high/low pressure, temperature, level, flow, composition, wrong material, reverse flow, no flow, contamination, utility loss, open to atmosphere, wrong sequence, failed isolation, bypass left in service, or return-to-service error.
- Causes: incorrect lineup, missed prerequisite, wrong valve, wrong mode, failed instrument, missing utility, poor communication, maintenance error, failed post-maintenance test, or uncontrolled procedure change.
- Consequences: exceed safe operating limit, release, runaway, overpressure, vacuum, equipment damage, off-spec product, exposure, fire/explosion, environmental release, or delayed emergency response.
- Existing safeguards: explicit interlocks, alarms, mechanical devices, operator checks, procedural verification, independent review, permits, LOTO, proof tests, and emergency actions.
- Recommendations: add or revise procedure limits, define expected response, add verification/hold point, clarify branch logic, add safe-state criteria, add MOC link, add training/drill, improve accessibility, or require field validation.

## Missing Information To Flag

- Procedure has no unique ID, title, revision, approval date, effective date, page control, or review date.
- Title or purpose does not match the task.
- Scope does not identify affected equipment, unit, system, or operating mode.
- References to P&IDs, SDS/MSDS, equipment manuals, safe work practices, PHA results, or operating-limit tables are missing.
- Preconditions are vague or do not include plant state, support systems, permits, LOTO, qualifications, notifications, or approvals.
- Precautions list hazards without consequences or actions.
- Steps do not identify tags, expected equipment response, verification method, or corrective action.
- Limits are not numeric where numeric control is needed.
- Normal operating range, alarm, interlock, safe limit, and design limit are mixed together.
- Branching or cross-references force the user to search through multiple documents during a critical task.
- No clear final state or restoration/return-to-service state.
- Emergency entry, escalation, ERP trigger, or EOP exit criteria are missing.
- Temporary procedures, bypasses, or nonroutine changes have no MOC or expiration control.
- Procedure has no training, validation, periodic review, or in-use feedback evidence.

## Output Rule

When using this reference, produce HAZOP-ready context. Do not summarize the procedure for readability only. The output should answer:

- What mode is the system in?
- What is the intended state and final safe/stable state?
- Which process variables and limits matter?
- What happens if a limit or expected response is not met?
- Which engineered and procedural safeguards are present?
- What evidence is missing before the safeguard can be credited?

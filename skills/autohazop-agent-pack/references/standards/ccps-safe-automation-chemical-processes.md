# CCPS Guidelines for Safe Automation of Chemical Processes

Use this reference to extract practical automation safety context for HAZOP/LOPA, P&ID review, cause-and-effect review, control narrative review, alarm review, SIS/SIF review, and management-of-change review. It is derived from the CCPS safe automation guideline and focuses on what an agent should capture: automation protection layers, BPCS functions, alarms/operator action, SIS functions, SRS fields, sensor/logic-solver/final-element paths, failure modes, independence, diagnostics, bypasses, testing, training, documentation, and audit evidence.

This is a derived working guide. It does not reproduce the book's figures, tables, circuit diagrams, checklists, or detailed matrices. It does not replace IEC 61511/ISA 84, project standards, approved SRS documents, cause-and-effect charts, alarm rationalization, proof-test procedures, functional safety assessments, vendor manuals, or jurisdictional requirements.

## Source Traceability

- Source book: `Guidelines for Safe Automation of Chemical Processes`, Center for Chemical Process Safety, AIChE, 1993.
- Scope, limits, and glossary for BPCS, SIS, PES, HMI, IPL, fail-safe, fail-to-danger, availability, PFD, separation, and software life cycle: front matter and chapter 1.
- Automation as part of process safety, layers of protection, IPL criteria, SRS, integrity levels, and design philosophy: chapter 2.
- Integrity evaluation methods, PHA/PHA-team role, HAZOP/FMEA/FTA/ETA/QRA/capability assessment, common-mode issues, and data-quality limits: chapter 3.
- BPCS technology, signals, sensors, final elements, controllers, HMI, alarms, communications, power, grounding, batch control, software, and administrative actions: chapter 4.
- SIS requirements analysis, technology selection, architecture, equipment selection, verification/validation, HMI, alarms, sequential interlocks, testing provisions, and documentation: chapter 5.
- Procedures, bypasses, online calibration, abnormal operation, batch recipes, turnover, MOC, security, maintenance, testing, training, documentation, audit, simulation, and staffing: chapter 6.
- Batch polymerization reactor example: chapter 7.
- Separation, watchdog timers, communications, sensor fail-safe examples, SIS equipment selection, PES failure modes, and FAT guidance: Appendices B-H.

## Applies To

- Control narratives, cause-and-effect charts, SRS documents, alarm lists, interlock lists, I/O lists, loop diagrams, logic diagrams, HMI graphics, network drawings, power/UPS drawings, cabinet drawings, test records, bypass logs, and automation MOC records.
- BPCS and SIS context extraction for HAZOP/LOPA.
- Deciding whether an alarm, interlock, operator action, BPCS function, or SIS function needs independence or further evidence before it can be credited.
- Reviewing startup, shutdown, batch, abnormal, maintenance, online test, bypassed, degraded, or loss-of-view operation.

## Does Not Provide

- Final SIS design approval, SIL verification, proof-test interval calculation, or certification.
- A modern replacement for IEC 61511/ISA 84 terminology.
- Vendor-specific failure rates or diagnostic coverage.
- Permission to credit BPCS, alarm, operator action, or SIS as an IPL without project evidence.
- Relief sizing, fire protection design, or non-automation mitigation design.

## Key Terms For Extraction

Use source terminology exactly when present:

| Term | Extraction use |
|---|---|
| `BPCS` | Basic process control system used for normal regulation, operator interface, routine alarms, and process transitions. |
| `SIS` | Safety interlock system used to take the process to a safe state or prevent an unsafe sequence. |
| `PES` | Programmable electronic system such as PLC, DCS controller, or computer-based control/protection device. |
| `HMI` | Operator interface for display, command entry, alarm viewing, diagnostics, and status. |
| `IPL` | Protection layer meeting specificity, independence, dependability, and auditability for an identified event. |
| `Fail-safe` | Failure direction moves the component or system toward a safer state. |
| `Fail-to-danger` | Fault prevents or delays reaching the safe operational state on demand. |
| `Separation` | Physical and functional isolation between BPCS/SIS or redundant SIS paths to reduce common-mode failure. |
| `Diversity` | Different technology, hardware, software, programming, sensing, or final elements used to reduce common-mode vulnerability. |
| `Diagnostics` | Active or passive detection of faults in sensors, logic solvers, outputs, communications, final elements, or software. |
| `Availability/PFD` | Probability context for whether a protection function will work on demand. Preserve project numbers if provided. |

This 1993 CCPS book uses `Integrity Level 1/2/3` for SIS classification. Do not automatically map those labels to modern `SIL` without an explicit project basis.

## Automation Context Schema

When reading automation documents, extract this structure:

```yaml
automation_context:
  source:
    document:
    page_or_sheet:
    revision:
    drawing_or_logic_id:
  scenario:
    node:
    hazardous_event:
    initiating_deviation:
    mode:
    operating_state:
  protection_layers:
    inherent_or_process_design:
    bpcs_control:
    alarm_operator_action:
    sis_or_interlock:
    relief_or_mechanical:
    procedure_or_administrative:
  bpcs:
    technology:
    controller_or_logic_solver:
    control_strategy:
    sensors:
    final_elements:
    alarms:
    hmi:
    communications:
    power_grounding:
    software_or_database:
    failure_modes:
  sis:
    function_id:
    safety_function:
    srs_reference:
    integrity_level_or_target:
    sensor_path:
    input_modules:
    logic_solver:
    output_modules:
    final_elements:
    trip_setpoints:
    prealarms:
    action_on_trip:
    safe_state:
    reset_or_restart_rules:
    manual_shutdown:
    separation:
    diversity:
    diagnostics:
    bypasses:
    proof_or_functional_test:
    documentation:
  administrative_controls:
    moc:
    access_security:
    training:
    procedures:
    bypass_authorization:
    maintenance:
    test_records:
    audit:
  hazop_use:
    deviations:
    causes:
    consequences:
    safeguards_to_review:
    independence_concerns:
    missing_information:
```

## Layer-Of-Protection Extraction

Separate the layers in this order:

1. Process design and inherent hazard reduction.
2. BPCS control and operator monitoring.
3. Alarm with operator corrective action.
4. SIS or safety interlock action.
5. Relief, containment, mitigation, emergency response, and administrative controls.

For each claimed protection layer, extract:

```yaml
protection_layer:
  claimed_layer:
  protected_event:
  trigger:
  action:
  protected_equipment:
  response_time_basis:
  independence_from_initiating_cause:
  independence_from_other_layers:
  dependability_or_test_basis:
  audit_or_record_basis:
  credited_as_ipl:
  evidence:
```

Rules:

- Do not count a BPCS function as independent from an initiating cause that is inside the same BPCS path.
- Do not count BPCS mirroring of SIS logic as an additional IPL.
- Diagnostics, alarms, event logs, and HMI indications are usually evidence or support functions; they are not automatically IPLs.
- If a shared sensor, shared valve, shared power supply, shared communication link, shared HMI, or shared software can defeat multiple layers, flag `common_mode_or_common_cause_concern`.
- If an operator action is credited, require trigger, indication, action, time available, training, accessibility, and audit basis.

## SRS And SIS Function Extraction

For each SIS/SIF or interlock, capture the SRS-level information:

```yaml
sis_function:
  function_id:
  hazard_or_deviation:
  process_variable_monitored:
  trip_setpoint:
  prealarm_setpoint:
  action_on_trip:
  final_safe_state:
  permissive_or_shutdown_logic:
  integrity_class_or_target_pfd:
  demand_mode:
  allowable_response_time:
  sensor_requirements:
  logic_solver_requirements:
  final_element_requirements:
  reset_restart_requirements:
  bypass_requirements:
  full_function_test_requirement:
  minimum_test_interval:
  environmental_limits:
  documentation_required:
```

Flag missing SRS data when the source does not identify setpoints, action, final element, safe state, required test interval, or integrity target.

## BPCS Context Extraction

For BPCS documents, extract:

- Technology: analog, pneumatic, DCS, PLC, single-loop controller, hybrid system, direct-wired logic, or PES-based system.
- Control objective: pressure, temperature, flow, level, composition, sequence, recipe, optimization, or supervisory control.
- Control strategy: feedback, cascade, ratio, feedforward, override, split-range, batch sequence, permissive, hold, startup, shutdown, or manual mode.
- Controller mode and transfer: auto/manual/cascade status, bumpless transfer, reset windup handling, derivative/setpoint behavior, and mode-change safeguards.
- Sensors: range, accuracy, response time, representative sampling, sensing-line design, material compatibility, serviceability, failure direction, signal conditioning, and hazardous-area suitability.
- Final elements: control valve, block valve, solenoid, motor starter, variable-speed drive, pump/compressor action, fail position, leakage class, fire-safe needs, position feedback, and maintenance access.
- Communications: fieldbus/network/data highway, remote I/O, read-only/read-write paths, diagnostics, time synchronization, event logging, and cyber/physical access limits.
- Power/grounding: UPS, restart time, power-source independence, grounding, shielding, EMI/RFI susceptibility, and power-loss state.
- HMI: display hierarchy, units, tag naming, colors/symbols, command-entry method, two-step confirmation, access security, engineering workstation access, and loss-of-view response.
- Software/database: application program, configuration database, alarm database, display database, recipe database, scan/execution rates, online changes, backups, master records, and change history.

HAZOP prompts:

- What happens on loss of BPCS view, loss of control, loss of communication, loss of power, frozen data, stale data, wrong range, wrong units, wrong display, wrong setpoint, or wrong mode?
- Can the operator still see SIS status if the BPCS HMI fails?
- Can a BPCS change alter or defeat a protection function?
- Are startup, shutdown, batch hold, restart, manual, maintenance, and abnormal modes covered?

## Alarm Context Extraction

For each alarm, extract:

```yaml
alarm_context:
  alarm_tag:
  variable:
  source_system:
  bpcs_or_sis:
  setpoint_or_condition:
  priority:
  message:
  current_value_shown:
  violated_limit_shown:
  operator_action:
  time_available:
  acknowledgement_required:
  return_to_normal_indication:
  first_out_required:
  suppression_or_inhibit_logic:
  event_log:
  display_location:
  independence_concern:
```

Rules:

- Separate BPCS alarms from SIS alarms where the SIS must remain visible during BPCS failure.
- Capture alarm priority, process state, grouping, message clarity, current value, violated limit, status, and event timestamps.
- First-out alarm logic is useful only where knowing the first cause changes diagnosis or action.
- Alarm suppression should reduce nuisance alarms without hiding critical out-of-limit conditions.
- Too many alarms during a disturbance can be a hazard; flag alarm flood, cycling alarms, nuisance alarms, and unclear priority.
- Do not credit an alarm/operator action unless the action is explicit, timely, trained, available, and auditable.

## SIS Architecture Extraction

Extract the full path from initiating condition to final action:

```yaml
sis_path:
  sensors:
    - tag:
      variable:
      technology:
      process_connection:
      range:
      failure_direction:
      diagnostics:
      redundancy:
      diversity:
  input_modules:
  logic_solver:
    technology:
    voting:
    watchdog:
    diagnostics:
    memory_or_program_protection:
    power_loss_action:
  output_modules:
  final_elements:
    - tag:
      type:
      fail_position:
      action_on_trip:
      position_feedback:
      leakage_or_shutoff_basis:
      solenoid_arrangement:
      power_or_air_dependency:
  communications:
  hmi_or_annunciation:
  manual_shutdown:
```

Checks:

- Sensors should be representative, timely, serviceable, and fail in the intended direction.
- Redundant sensors should avoid shared process taps where practical.
- Calculated or inferred variables used for SIS input need validation and testability.
- Logic solvers should fail safe on power loss or malfunction and should not automatically restart into unsafe operation.
- External watchdog timers may be needed for PES-based SIS where internal diagnostics are not enough.
- Final elements need position feedback or equivalent confirmation when required by risk.
- A BPCS control valve used as a SIS final element requires explicit approval and evidence; as the only final element it is usually a major review item.
- Double block and bleed arrangements need valve-position feedback and testability, including the bleed path.

## Separation, Diversity, And Diagnostics

Extract these fields:

```yaml
integrity_features:
  separation:
    physical:
    functional:
    sensors:
    final_elements:
    logic_solvers:
    i_o:
    power:
    hmi:
    communications:
    software:
  diversity:
    sensor_technology:
    logic_solver_vendor_or_type:
    software:
    application_programming:
    final_elements:
  diagnostics:
    passive:
    active:
    internal_watchdog:
    external_watchdog:
    input_output_checking:
    final_element_feedback:
    communication_diagnostics:
    program_compare_to_master:
```

Rules:

- Separation is required to reduce common-mode failure between BPCS and SIS and between redundant SIS paths.
- Read-only or safety-gateway communication is preferred when BPCS needs SIS status; read/write paths need stronger justification and controls.
- Diversity should reduce a real common-mode vulnerability. Diversity that adds unfamiliar, less reliable equipment can increase risk.
- Passive diagnostics detect faults on demand or during test. Active diagnostics periodically exercise or check the function before demand.
- Diagnostics can improve availability only if alarms, repair response, bypass control, and testing are managed.

## Bypass And Online Work

Bypasses and online maintenance/testing are high-value HAZOP context. Extract:

```yaml
bypass_context:
  function_bypassed:
  bypass_type:
  master_or_individual:
  reason:
  approval:
  start_time:
  expiry_time:
  visible_tag_or_annunciation:
  compensating_safeguards:
  monitoring_required:
  authorized_removal:
  log_record:
  return_to_normal_verification:
```

Rules:

- Master bypasses of multiple SIS trip initiators are a major concern.
- Individual bypasses require written approval, clear annunciation, time limit, tagging/logging, and return-to-normal verification.
- Output bypasses are a major concern unless specifically justified by approved procedure and risk review.
- Online calibration or test must define when it is allowed, what is bypassed, what remains in service, who performs it, expected results, and precautions.
- Test jumpers or temporary connections need identification, authorization, removal log, and independent verification.

## Testing And Validation Extraction

Capture testing evidence separately from design intent:

```yaml
test_context:
  test_type:
    factory_acceptance_test:
    offline_test:
    online_test:
    sis_functional_test:
    proof_test:
    post_maintenance_test:
    post_moc_test:
  procedure_id:
  scope:
  participants:
  expected_results:
  actual_results:
  exceptions_or_punch_list:
  signoff:
  test_interval_basis:
  failures_found:
  corrective_actions:
  next_test_due:
```

Rules:

- FAT should test integrated hardware and software before shipment where applicable.
- Functional testing should validate sensor inputs, logic, setpoints, alarms, final elements, fail-safe positions, displays, and feedback.
- SIS tests should be specific to each SIS and recorded with signoff.
- Multiple SISs on the same unit should not be tested simultaneously unless a risk review explicitly supports it.
- Test frequency should not be less frequent than the interval assumed in the PHA/risk assessment.
- Retesting is needed after modifications, major turnarounds, and maintenance that can affect the SIS.

## Administrative And Lifecycle Controls

Extract evidence for:

- Written procedures for BPCS/SIS operation, critical operations, SIS bypass, online calibration, abnormal operation, batch recipes, turnover, safety review, security, maintenance, and testing.
- Control-system MOC for changes to strategy, loops, algorithms, interlocks, ranges, final-element fail position, sensor type, operating system/software, third-party software, backup capability, or SIS hardware/software/final elements.
- Security for engineering workstations, passwords/key locks, remote diagnostics, program downloads, and authorized personnel.
- Maintenance planning for spares, revision levels, storage, vendor support, software compatibility, static/magnetic damage protection, and post-maintenance checks.
- Training for operators, maintenance, engineers, and contractors on BPCS/SIS use, abnormal response, diagnostics, startup/shutdown, bypass, and changes.
- Documentation: up-to-date P&IDs, logic diagrams, C&E, I/O termination, displays, reports, power diagrams, software master copies, change history, and official-copy control.
- Audit: review of changes, problems, documentation status, functional checks, operating understanding, proposed changes, and incident trends.

## Batch And Sequential Automation

For batch or sequence-controlled processes, extract:

- Recipe state, phase, equipment allocation, charge quantity, charge endpoint, two-stage shutoff, hold, normal shutdown, emergency shutdown, restart, and maintenance/idle state.
- Trigger events based on time, measurement, equipment status, operator confirmation, QC/lab release, or sequence completion.
- Permissives and reject-unsafe-command logic.
- Wrong sequence, wrong time, wrong duration, wrong material, wrong quantity, wrong equipment, or wrong destination scenarios.
- Whether the SIS remains separate from recipe/process-management levels and can reject unsafe actions.
- Whether recipe edits, downloads, scaling, and destination rules are controlled and documented.

## HAZOP/LOPA Use

Use this reference to add automation-specific context to worksheets:

- Deviations: no control, more control, less control, wrong control action, reverse action, delayed action, no alarm, alarm flood, wrong setpoint, wrong mode, wrong sequence, loss of view, frozen display, false signal, common-mode failure, bypass active, failed final element, loss of power, loss of air, loss of communication, software change, failed restart, failed ESD, or spurious trip causing another hazard.
- Causes: sensor failure, plugged impulse line, unrepresentative sample, EMI/RFI, range error, configuration error, application software bug, network failure, power/UPS failure, grounding issue, HMI confusion, unauthorized change, recipe error, maintenance error, failed proof test follow-up, bypass left in service, or uncontrolled vendor update.
- Consequences: delayed operator response, failure to shut down, shutdown to wrong state, release, overpressure, runaway, wrong material addition, equipment damage, exposure, environmental release, loss of containment, or unsafe restart.
- Safeguards to review: independent SIS, alarm/operator action, permissive, interlock, manual shutdown, final-element feedback, prealarm, first-out alarm, event log, proof test, diagnostics, independent HMI, written bypass procedure, MOC, and training.
- Recommendations: define SRS, separate BPCS/SIS, add final-element feedback, improve alarm priority/action, add first-out where useful, remove master bypass, add bypass log/time limit, add functional test procedure, validate startup/shutdown modes, control online changes, update documentation, or perform MOC.

## Missing Information To Flag

- No SRS or SRS lacks trip value, action, safe state, test interval, response time, or integrity target.
- BPCS and SIS independence not shown.
- Shared sensor, final element, HMI, power, network, or software not justified.
- Cause-and-effect chart does not show final element, reset, bypass, permissive, or safe state.
- Alarm list lacks priority, operator action, time available, current value, violated limit, or event logging.
- SIS alarm visibility depends only on the BPCS HMI.
- Bypass criteria, approval, time limit, tagging, and return-to-normal steps are absent.
- Online testing or calibration requires temporary defeats without compensating safeguards.
- Functional test records do not include final element action and fail-safe position.
- MOC does not cover software, configuration, range, alarm, setpoint, sequence, recipe, or vendor revision changes.
- Documentation copies conflict or are not controlled.
- Operators and maintenance personnel have no training or drill evidence for abnormal automation failures.

## Output Rule

When using this reference, output automation context that answers:

- What automation layer is being claimed?
- What event does it protect against?
- What sensor-to-final-element path performs the action?
- What setpoint, logic, and safe state are defined?
- What can fail in the same way across layers?
- What test, bypass, MOC, training, and documentation evidence exists?
- What evidence is missing before the layer can be credited in HAZOP/LOPA?

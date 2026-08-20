# BS EN 31010 Risk Assessment Techniques

Use this reference when selecting, checking, or documenting risk assessment techniques for HAZOP/LOPA work, PHA planning, safeguard review, risk ranking, bow-tie development, or escalation from qualitative to semi-quantitative or quantitative analysis.

This is a derived working guide. It does not reproduce BS EN 31010 tables, figures, guideword tables, examples, or method text. It does not replace BS EN 31010 / IEC/ISO 31010, ISO 31000, IEC 61882, IEC 61508, IEC 61511, project risk matrices, company HAZOP/LOPA procedures, or qualified facilitator judgement.

## Source Traceability

- Source standard: BS EN 31010:2010, UK implementation of EN 31010:2010, identical to IEC/ISO 31010:2009, "Risk management - Risk assessment techniques".
- Scope: guidance on selection and application of systematic risk assessment techniques supporting ISO 31000.
- Risk assessment concepts: clause 4.
- Risk assessment process: clause 5.
- Technique selection: clause 6.
- Applicability and attributes of techniques: Annex A.
- Technique descriptions: Annex B.
- HAZOP technique summary: Annex B.6.
- LOPA technique summary: Annex B.18.
- Bow-tie technique summary: Annex B.21.
- Consequence/probability matrix summary: Annex B.29.
- Cost/benefit and ALARP discussion: Annex B.30.

## Applies To

- Deciding which risk assessment technique to use at each lifecycle stage: concept, design, construction, operation, modification, incident review, decommissioning, or disposal.
- Reviewing whether a HAZOP, LOPA, risk matrix, bow-tie, FMEA, FTA, ETA, SWIFT, checklist, RCA, HRA, RCM, or quantitative method is suitable for the decision being made.
- Building traceable HAZOP/LOPA documentation: context, objectives, criteria, assumptions, controls, uncertainty, sensitivity, recommendations, and review triggers.
- Preventing overuse of a risk matrix where a more detailed scenario method or quantitative analysis is needed.

## Does Not Provide

- Company-specific risk tolerability criteria, severity/likelihood categories, risk ranking tables, SIL targets, IPL probability values, or initiating event frequencies.
- A mandatory technique for every situation. Technique choice depends on objectives, data quality, uncertainty, complexity, resources, and decision needs.
- Safety-only requirements. The standard is generic risk management guidance; use process-safety standards and company procedures for safety acceptance criteria.

## Risk Assessment Planning Schema

Use this schema before selecting a technique. Do not start with the method; start with the decision the assessment must support.

```yaml
risk_assessment_plan:
  source:
    document:
    page_or_sheet:
    revision:
  decision_need:
    objective:
    decision_to_support:
    lifecycle_stage:
    required_output:
    required_confidence:
  context:
    system_or_node:
    boundaries:
    operating_modes:
    stakeholders:
    external_constraints:
    internal_constraints:
    legal_or_project_requirements:
    risk_criteria_source:
  information_quality:
    drawings_available:
    procedures_available:
    operating_history:
    failure_data:
    consequence_data:
    uncertainty_level:
    assumptions:
  technique_selection:
    candidate_techniques: []
    selected_technique:
    selection_reason:
    rejected_techniques:
    reason_rejected:
  assessment:
    risk_identification_method:
    risk_analysis_method:
    risk_evaluation_method:
    controls_considered:
    control_effectiveness_evidence:
    uncertainty_and_sensitivity:
  output:
    risk_register_or_worksheet:
    recommendations:
    actions_owner:
    review_trigger:
    remaining_gaps:
```

## Core Risk Assessment Process

- Establish the context before analysis. Define scope, objectives, boundaries, stakeholders, risk criteria, decision rules, and reporting needs.
- Identify risks by finding what can happen, why it can happen, what existing controls are present, and what objectives can be affected.
- Analyse risk by considering causes, consequences, likelihood, existing controls, control effectiveness, uncertainty, and sensitivity.
- Evaluate risk by comparing analysed risk against predefined criteria. Do not invent acceptance criteria inside the worksheet.
- Treat risk by selecting actions that change likelihood, consequence, exposure, detectability, or recovery capability.
- Monitor and review because assumptions, controls, operating modes, and external context can change.

## Technique Selection Rules

Choose a technique using these factors:

- Objective of the study: screening, design improvement, operating procedure development, SIL allocation, maintenance planning, incident learning, or decision between options.
- Decision maker needs: quick ranking, traceable qualitative reasoning, scenario frequency estimate, barrier map, or quantitative risk result.
- Type and range of risks: process safety, reliability, environmental, financial, operational, human factors, organizational, or security.
- Consequence magnitude: high-consequence scenarios deserve more rigour even when frequency is uncertain.
- Available information: PFD only, mature P&ID, procedures, operating data, failure data, human reliability data, or validated models.
- Uncertainty: poor data and model uncertainty must be stated; apparent numerical precision must not exceed evidence quality.
- Complexity: interacting causes, common-cause failures, dependent barriers, and multiple consequences may need FTA, ETA, bow-tie, QRA, or specialist analysis.
- Resources and expertise: a simple method done well can be more useful than a complex method done poorly.
- Need for update: choose methods that can be maintained when design, operating data, or controls change.
- Regulatory or project requirements: use mandated methods when specified.

## Practical Technique Map

Use this derived map to choose a technique for process-safety work.

| Technique | Best Use In This Skill | Main Inputs | Useful Output | Caution |
| --- | --- | --- | --- | --- |
| Checklist | Quick completeness check against known requirements | Standards, prior incidents, procedures | Gap list | Can miss novel hazards |
| Brainstorming / interviews / Delphi | Capture expert knowledge and weak signals | Facilitator, experts, prompts | Candidate hazards and assumptions | Needs structure and challenge |
| PHA | Early lifecycle hazard screening | Concept design, material/service data | Preliminary hazard list and actions | Not detailed enough for final design acceptance |
| HAZOP | Systematic deviation study of process, procedure, or system | P&IDs, design intent, procedures, team | Deviations, causes, consequences, safeguards, actions | Depends heavily on scope, guidewords, and team knowledge |
| SWIFT / What-if | Fast structured review or management-of-change screening | System description, prompts, team | What-if scenarios and actions | Less systematic than full HAZOP |
| FMEA / FMECA | Component or function failure mode review | Equipment list, functions, failure modes | Failure effects, criticality, actions | Can miss system-level interactions |
| FTA | Analyse causes of a defined top event | Top event, logic structure, failure data | Cause combinations and top-event likelihood | Needs good logic and data |
| ETA | Analyse outcomes after an initiating event | Initiating event, barrier sequence, probabilities | Consequence pathways | Assumes sequence and barrier states are well defined |
| Cause-consequence analysis | Combine FTA and ETA thinking | Causes, event, safeguards, consequences | Scenario logic from causes to outcomes | Can become complex quickly |
| Bow-tie | Communicate threats, top event, barriers, and consequences | Hazard/top event, causes, consequences, barriers | Barrier map with prevention and mitigation controls | Can oversimplify dependent barriers |
| LOPA | Semi-quantitative check of one cause-consequence scenario | HAZOP/PHA scenario, initiating frequency, IPL PFD, tolerable risk | Required risk reduction or additional protection | One scenario at a time; common-cause and dependency risk can be missed |
| HRA | Analyse human error likelihood and performance shaping factors | Task, procedures, interface, training, time pressure | Human error contribution and improvements | Data uncertainty is often high |
| RCM | Maintenance strategy for equipment failures | Equipment functions, failure modes, consequences | Maintenance tasks and intervals | Not a substitute for HAZOP |
| Risk matrix | Screening and communication of qualitative risk ranking | Severity and likelihood criteria | Ranked list and treatment priority | Subjective; ordinal scores should not be treated as precise numbers |
| Cost/benefit or ALARP | Evaluate risk treatment options | Risk level, treatment options, cost, benefit | Treatment decision support | Do not use cost alone to justify intolerable safety risk |

## HAZOP Use

Use HAZOP when a mature design, process, procedure, or system description exists and the aim is to identify deviations from design intent.

Minimum HAZOP inputs:

- Current P&IDs, PFDs, line lists, datasheets, control narratives, cause-and-effect, plot/layout information, and operating/maintenance/emergency procedures.
- Design intent for each node or step.
- Operating modes: normal, startup, shutdown, abnormal, maintenance, isolated, bypassed, standby, emergency.
- Guidewords or prompts suitable for the system.
- Multidisciplinary team including design, operations, maintenance, control/instrument, process safety, and facilitator roles.

HAZOP output should include:

- Node or study point.
- Parameter and guideword.
- Deviation.
- Causes.
- Consequences.
- Existing safeguards.
- Risk ranking or need for further analysis if required by procedure.
- Recommendations/actions, owner, due date, and closure basis.

Quality flags:

- Study scope is unclear or excludes interfaces and package boundaries.
- Design intent is missing, so deviations become generic.
- Safeguards are listed without verifying whether they act on the scenario.
- Human and organizational factors are ignored.
- Recommendations solve minor design detail while fundamental assumptions are not challenged.
- The study is performed too late and actions become hard to implement.

## LOPA Use

Use LOPA after HAZOP/PHA when a scenario needs more rigour than qualitative ranking but does not require full QRA.

LOPA works on one cause-consequence pair at a time. Do not merge several initiating causes, multiple outcomes, or unrelated safeguards into one scenario unless the project method explicitly supports it.

Minimum LOPA inputs:

- Scenario from HAZOP/PHA with clear initiating cause and consequence.
- Initiating event frequency source.
- Consequence severity and tolerable risk target.
- Enabling conditions and conditional modifiers with basis.
- Existing and proposed protection layers.
- Evidence that each credited IPL is independent, effective, auditable, and capable of acting before the consequence.
- Probability of failure on demand or risk reduction factor for each IPL from an approved source.

LOPA quality rules:

- Not every safeguard is an IPL.
- Procedures and inspections are normally not IPLs in this standard's LOPA summary; use company LOPA rules if they allow tightly controlled exceptions.
- Common-cause, common-mode, dependency, bypass, maintenance defeat, and shared utility failures must be checked before crediting multiple layers.
- LOPA is weak for complex scenarios with many interacting causes, many consequences, or strong dependencies.
- If LOPA drives a SIL requirement, connect the output to IEC 61508 / IEC 61511 and the project SRS workflow.

## Bow-Tie Use

Use bow-tie analysis when the goal is to communicate the barrier picture around a top event.

Minimum bow-tie inputs:

- Hazard and top event.
- Threats/causes on the left side.
- Consequences on the right side.
- Prevention barriers between threats and top event.
- Mitigation and recovery barriers between top event and consequences.
- Escalation factors that weaken barriers.
- Escalation controls that protect barriers.
- Barrier owners, performance standards, inspection/test basis, and impairment/bypass controls.

Quality flags:

- Bow-tie is used as proof of risk tolerability without risk criteria.
- Barriers are shown but no performance standard or owner exists.
- Dependent barriers are presented as independent.
- Multiple simultaneous causes are oversimplified.
- Preventive and mitigative controls are mixed together.

## FMEA, FTA, ETA, And Cause-Consequence Use

- Use FMEA/FMECA when the study starts from component/function failure modes and asks what effects they create.
- Use FTA when a defined top event needs causal logic and, where data permit, probability estimation.
- Use ETA when an initiating event can lead through a sequence of barrier successes/failures to multiple outcomes.
- Use cause-consequence analysis when both cause logic and outcome paths matter.
- Use these methods to supplement HAZOP when safeguards interact, common-cause failures matter, or scenario logic needs clearer proof than a worksheet row provides.

## Risk Matrix Use

Risk matrices are useful for screening and communication, but they are not precision instruments.

- Use the project-approved consequence and likelihood criteria. Do not invent scale meanings.
- Probability must match the selected consequence, not the event as a whole if the event has several possible outcomes.
- Rank the most serious credible outcome when the decision is about major accident prevention; consider separate rows for frequent low-impact events and rare high-impact events.
- Do not aggregate ordinal scores or claim that several low risks equal one medium risk.
- Record uncertainty, assumptions, and basis for severity and likelihood.
- If risk matrix output drives expensive or safety-critical decisions, consider whether LOPA, bow-tie, FTA/ETA, QRA, or sensitivity analysis is needed.

## Control Assessment And Safeguard Evidence

Controls should be assessed for adequacy and effectiveness before being credited.

Ask:

- What control exists for this risk?
- What exact scenario step does it prevent, detect, mitigate, or recover from?
- Is it capable of working under the scenario conditions?
- Is it independent from the initiating cause and from other credited controls?
- Is it operating as intended in the field?
- What documentation, inspection, proof test, alarm response record, maintenance record, or procedure proves effectiveness?
- What can defeat it: bypass, isolation, common utility failure, human error, poor HMI, alarm flood, hidden failure, corrosion, fouling, wrong set point, or unavailable operator?

For HAZOP/LOPA output, classify safeguards by layer:

- Inherent/design feature.
- Passive mechanical protection.
- Basic process control.
- Alarm with operator action.
- Interlock or trip.
- SIS/SIF.
- Relief/depressuring.
- Physical mitigation.
- Procedure/training/inspection.
- Emergency response.

Only call a safeguard an IPL when the governing LOPA method supports it and independence/effectiveness/auditability/proof basis are stated.

## Documentation Requirements

Risk assessment documentation should be traceable enough to maintain over the lifecycle.

Capture:

- Objective and scope.
- System description and boundaries.
- External and internal context.
- Risk criteria and justification.
- Methodology and why selected.
- Team/roles and expertise.
- Data, assumptions, sources, and validation.
- Risk identification results.
- Risk analysis and evaluation results.
- Existing controls and effectiveness basis.
- Uncertainty and sensitivity.
- Recommendations and action tracking.
- Review triggers and assumptions to monitor.
- References to drawings, datasheets, procedures, calculations, and standards.

## Lifecycle Use

- Concept phase: use checklist, PHA, scenario analysis, and coarse risk ranking to decide whether to proceed and what design options are safer.
- Design phase: use HAZOP, FMEA, FTA/ETA, LOPA, bow-tie, and risk matrix to refine design and safeguards.
- Construction/commissioning: use checklists, procedure HAZOP, pre-startup risk review, and verification of controls.
- Operation: use HAZOP revalidation, MOC reviews, RCA, bow-tie barrier review, alarm/interlock review, and operating procedure risk review.
- Maintenance: use FMEA, RCM, human reliability review, and critical task analysis.
- Incident review: use RCA, cause-and-effect, FTA, bow-tie update, and control effectiveness review.
- Decommissioning: use PHA/HAZOP, procedure review, human reliability review, and emergency response planning.

## Missing Information To Flag

- Decision objective or risk criteria are missing.
- Method selected is not justified against objective, uncertainty, complexity, and available data.
- HAZOP lacks design intent, node boundaries, current P&IDs, procedures, or multidisciplinary participation.
- LOPA lacks a single cause-consequence pair, initiating frequency, IPL independence basis, PFD source, conditional modifier basis, or tolerable risk target.
- Risk matrix scales are undefined or not project-approved.
- Numerical risk values are shown without data source, uncertainty, or sensitivity.
- Safeguards are credited without proof that they are effective and available.
- Human and organizational factors are excluded without justification.
- Common-cause or dependency between safeguards is not checked.
- Recommendations lack owner, due date, or closure evidence.
- Review triggers are missing for assumptions likely to change.

## Output Rule

When using this reference, do not simply name a technique. State why the technique fits the decision, what inputs are required, what output it should produce, what it cannot prove, and what missing information must be obtained before relying on the result.

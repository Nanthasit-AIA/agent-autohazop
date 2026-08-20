---
name: hazop-lopa-guideline
description: Apply a HAZOP-LOPA methodology when Codex needs to support AI HAZOP studies, process hazard reviews, HAZOP worksheet drafting, node/design-intent definition, guide-word deviation generation, cause/consequence analysis, safeguard/IPL review, initial and final risk ranking, or recommendation drafting for process HAZOP/LOPA work.
---

# HAZOP-LOPA Guideline

## Source Scope

Use this skill as a working procedure derived from the user-provided HAZOP-LOPA procedure pages. The covered material includes HAZOP/LOPA definitions, the HAZOP study phases, process HAZOP workflow, node definition, design intent, deviation generation, cause/consequence rules, generic guide words, generic process parameters, and early LOPA handling.

If the task requires appendix-specific criteria, such as the risk matrix, initiating event likelihood table, IPL credit rules, HAZOP deviation matrix, SIL determination method, or final company risk acceptance criteria, ask for the relevant appendix or source file before assigning final numeric values.

Use companion skills when the task needs deeper execution:

- Use `hazop-pfd-pid-tracer` to read PFD/P&ID topology, node boundaries, upstream/downstream propagation, recycle/common-header effects, utility paths, and relief/vent/drain effects.
- Use `hazop-cause-consequence-assessor` to screen cause credibility, split cause-consequence paths, and write unmitigated consequences without safeguards.
- Use `hazop-severity-assessor` to assess safety, environmental, and asset/equipment severity separately, then select the most severe credible dimension.
- Use `hazop-lopa-ipl-assessor` to review IEL, safeguards, IPL qualification, PFD/credit, and mitigated likelihood.
- Use `hazop-risk-ranking-assessor` to perform initial/final risk lookup, category consistency checks, and recommendation triggers.

## Core Definitions

- `HAZOP`: Hazard and Operability Study.
- `LOPA`: Layer of Protection Analysis.
- `IPL`: Independent Protection Layer.
- `IEL`: Initial Event Likelihood.
- `LOPC`: Loss of Primary Containment.
- `PFD`: Process Flow Diagram.
- `P&IDs`: Piping and Instrument Diagrams.
- `H&MB`: Heat and Material Balance.
- `SDS`: Safety Datasheet.
- `CHHP`: Critical higher-hazard process.
- `HHP`: Higher-hazard process.
- `CSO`: Process Safety Management System Owner.
- `Double jeopardy`: occurrence of two independent initiating events at the same time. Do not use double jeopardy as a routine cause unless plant experience or the design case makes it credible.

## Core Approach

- Treat HAZOP as a systematic multidisciplinary review to identify credible deviations from design intent, their causes, consequences, safeguards, and required actions.
- Treat HAZOP-LOPA as a semi-quantitative workflow: use HAZOP to identify hazardous scenarios and LOPA to judge whether existing independent protection layers reduce risk to a tolerable level.
- Focus on safety, health, environmental, asset, and significant operability consequences.
- Avoid turning HAZOP into a general design review, layout review, fire and gas review, escalation review, or safety-distance review unless the user explicitly asks.
- Use conservative engineering judgment when data is missing. State assumptions clearly and do not invent plant-specific criteria.

## HAZOP Study Phases

1. Definition: select the team, define the scope, and define the objectives.
2. Preparation: plan the study, collect data, and arrange the schedule.
3. Examination: perform Process HAZOP and, when applicable, Procedure HAZOP.
4. Documentation: record the examination, sign off the documentation, follow up implemented recommendations, re-study modified or cancelled recommendations if necessary, and produce the final report.

## Process HAZOP Workflow

1. Divide the system into nodes.
2. Select one node and define its design intent.
3. Identify deviations by combining guide words with process parameters.
4. Identify causes and consequences.
5. Evaluate initial risk ranking from cause likelihood and consequence severity.
6. Identify safeguards and IPLs that mitigate the risk to a tolerable level.
7. Evaluate final risk ranking after credited IPLs.
8. Agree actions or recommendations for remaining risk gaps or useful clarifications.
9. Check whether all causes and consequences have been considered.
10. Check whether all guide words and selected parameters have been applied.
11. Check whether all nodes in scope have been applied.

## Nodes And Design Intent

- Divide complex systems into simpler nodes. Node boundaries normally end at valves or equipment such as control valves, isolation valves, separators, exchangers, coolers, pumps, or similar process boundaries.
- Ensure the node set covers every relevant line and item of equipment within the defined study scope.
- For each selected node, define design intent using available P&IDs, PFDs, H&MB, equipment datasheets, material specifications, operating procedures, or other user-provided basis documents.
- Include key parameters and normal or intended operating ranges when available.
- Cover normal operation and non-routine operation when in scope, including start-up, shutdown, emergency start-up or shutdown, commissioning, decommissioning, decoking, and special operating modes.
- Before writing a cause/consequence path, trace the node as a process graph: upstream sources, downstream users, recycle or bypass lines, relief/vent/drain paths, utility interfaces, common headers, and control loops.
- For failed equipment or valves, identify local effects, downstream effects, upstream/backpressure effects, recycle/common-header effects, and utility effects before selecting the ultimate consequence.

## Deviation Generation

Use a parameter-first approach: choose a process parameter, then apply relevant guide words. Keep only combinations that have physical meaning for the node.

Treat flow, pressure, and temperature as common starting parameters when they apply. Other process parameters can be tested case by case.

Common process parameters include:

- Flow
- Pressure
- Temperature
- Level
- Composition
- Phase
- Reaction
- Viscosity
- Speed
- pH
- Mixing
- Addition
- Separation
- Time
- Sequence
- Start/stop
- Signal
- Measure
- Maintain
- Monitoring
- Control
- Diagnostics
- Transfer
- Services
- Communication
- Aging

Use these guide words:

- `No`: none of the design intent is achieved, such as no flow.
- `More`: quantitative increase, such as high pressure or high temperature.
- `Less`: quantitative decrease, such as low flow or low level.
- `As well as`: qualitative increase or an additional adverse effect, such as contamination, impurities, or an extra activity.
- `Part of`: qualitative decrease where only part of the design intent is achieved, such as a change in component, concentration, or pH.
- `Reverse`: logical opposite of the design intent, such as reverse flow or reverse reaction.
- `Other than`: complete substitution where the original intent is not achieved and something different happens.

Include utility failures, such as instrument air failure, cooling water failure, or power failure, as common HAZOP scenarios when relevant.

## Cause Rules

- Identify each credible cause that can lead to the selected deviation.
- Treat distinct causes separately because similar causes can have different consequences, safeguards, and IPLs.
- Consider causes within the node under review. Consequences may affect equipment, instruments, or areas outside the node.
- Describe causes and consequences clearly enough to identify relevant equipment tags, instrument tags, and event paths.
- Do not assume safeguards while identifying the unmitigated consequence. First describe the event chain from deviation to immediate effects, LOPC when applicable, and ultimate consequence such as explosion, toxic release, environmental release, off-spec product, or asset damage.
- Stop progressing a scenario if there is no safety, health, environmental, asset, or significant operability consequence.
- Avoid double jeopardy unless plant experience or the design case makes it credible.
- Treat causes as unrelated only when there are no process, mechanical, or electrical linkages, or when enough time has elapsed between possible successive occurrences to make them unrelated. Use approximately one hour only as a guideline when the study basis supports it.

Do not normally consider these causes unless the user provides plant experience, a design case, or explicit scope:

- Simultaneous independent failures or double jeopardy.
- Natural events, such as storm, hurricane, earthquake, or flooding.
- External process impacts, such as dropped objects or sabotage.
- Incredible manual valve closure or opening due to operator error, especially valves not subject to normal operating mode, such as maintenance isolation valves, control-valve bypass valves, or tie-in valves.
- Single point failures such as piping or gasket deterioration, except for shell-and-tube heat exchanger tube rupture cases.

For shell-and-tube heat exchanger tube rupture:

- If the exchanger is designed under an accepted pressure-rule basis, note the inherent safer design basis.
- Otherwise, identify the need to review suitable pressure protection, such as PSV protection.

## Consequence Rules

- Analyze each cause to see whether it takes the system outside the intended operating range.
- Ignore all safeguards first so the ultimate unmitigated consequence is understood.
- Describe the consequence step by step from deviation to equipment or instrument impact, LOPC where relevant, and ultimate consequence.
- Use equipment or instrument tag numbers when available.
- Ensure potential consequences inside and outside the node have been considered.
- Consider immediate consequences outside the node until a detection point or protection system is reached.
- Avoid overly distant or long-duration consequence chains unless they remain credible within the study basis. For example, do not carry a chain to a remote tank farm off-spec impact unless the user specifically establishes that it is relevant.

## Risk And LOPA Handling

- Evaluate initial risk only after identifying the unmitigated consequence.
- Determine consequence severity using the company risk matrix when provided.
- Evaluate severity in three dimensions: safety/human health, environmental impact, and asset/equipment damage.
- Select the governing severity as the highest credible severity among the three dimensions; do not average them or let low equipment loss hide severe safety/environmental impact.
- For the money/equipment dimension, count direct equipment/property damage and direct restoration impact only unless the user supplies another company rule.
- Estimate initiating event likelihood using the applicable initiating event likelihood table when provided.
- If Appendix B or the IEL table is missing, do not invent frequencies. State that the initiating event likelihood basis is required.
- Adjust initiating event likelihood for non-normal operations such as start-up, shutdown, or special activities only when there is a clear operating-frequency basis.
- Treat detailed SIL determination as a separate study unless the user provides the required SIL methodology and asks for it.
- For batch operations or infrequent operator actions that can cause hazards, apply a peak-risk concept when the study basis requires it. Do not apply an initial-event frequency reduction below the allowed minimum without a provided rule.
- Credit safeguards as IPLs only when the required IPL criteria are available or can be justified from the user-provided basis.
- When IPL criteria are missing, list safeguards and candidate IPLs separately from credited IPLs.

## Worksheet Shape

When drafting or reviewing a HAZOP/LOPA worksheet, prefer these columns unless the user provides a template:

- Node
- Design intent
- Operating mode
- Parameter
- Guide word
- Deviation
- Cause
- Consequence
- Initial severity
- Initiating event likelihood
- Initial risk ranking
- Existing safeguards
- Candidate IPLs
- Credited IPLs
- Final likelihood
- Final risk ranking
- Recommendation or action
- Responsible owner
- Status or remark

For generated rows, do not use shorthand cross-references such as `See No/Less Flow...` as the final cause or consequence. Expand the referenced scenario into a complete path or mark that the reference needs expansion.

## Output Behavior

- If the user asks for worksheet rows, produce one row per distinct cause and consequence path.
- If the user provides a template, preserve the template columns and wording style.
- If a field cannot be completed from available information, write a clear placeholder such as `Need risk matrix`, `Need IEL table`, `Need IPL criteria`, or `Need operating range`.
- Keep recommendations specific to the remaining risk gap. Avoid vague actions such as "review system" when a more precise action is possible.
- Separate safeguards from IPLs unless the document gives enough evidence to credit them as IPLs.

## Quality Checks

Before finalizing, check that:

- Every node in scope has a defined design intent.
- Relevant parameters and guide words have been applied.
- Utility failures have been considered where applicable.
- Each meaningful deviation has at least one clear cause/consequence decision.
- Cause and consequence descriptions are not mixed with safeguards.
- Safeguards and IPLs are distinguished.
- Initial risk and final risk are not assigned without the required criteria.
- Recommendations close a specific remaining risk gap or document a specific required clarification.
- Missing appendices, risk criteria, or plant-specific data are called out instead of guessed.

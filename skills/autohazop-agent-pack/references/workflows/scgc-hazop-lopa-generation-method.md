# SCGC HAZOP-LOPA Generation Method

Use this reference whenever the agent generates or reviews HAZOP/LOPA rows for the graph-agent HAZOP generator. It is a derived working method from the user-provided `HAZOP_LOPA Procedure for AI HAZOP.pdf` copied into the project workspace under `inputs/procedure/`.

Treat this as methodology and screening guidance. It does not prove that a tag, safeguard, IPL, frequency, or risk criterion exists in the project. Project P&IDs, datasheets, procedures, risk matrix, and owner-approved criteria still control final acceptance.

## Mandatory Generation Passes

Run these passes internally before returning rows:

1. Node and design-intent pass: confirm node boundary, normal flow direction, intended operation, operating mode, key process parameters, and available drawings or datasheets.
2. Deviation pass: choose the parameter first, then apply only physically meaningful guide words. Do not force meaningless combinations.
3. Cause credibility pass: ask what can cause this exact deviation in this exact node. Reject process states, consequences, double jeopardy, random manual-valve mistakes, and unsupported external events.
4. Consequence pass: ignore safeguards first. Trace cause to deviation, local upset, upstream/downstream/recycle/utility effect, LOPC or other hazardous state, and ultimate credible consequence.
5. Initial risk pass: evaluate safety, environmental, and asset/equipment severity separately. Select the governing severity and choose initiating-event likelihood only from supplied or accepted basis.
6. Safeguard and IPL pass: list existing safeguards separately from credited IPLs. Credit IPLs only when independence, effectiveness, auditability, design basis, and management basis are established.
7. Recommendation and QA pass: write actions for remaining risk gaps or missing basis, then check coverage for all causes, consequences, guide words, parameters, and nodes in scope.

## Node And Design Intent Rules

- Divide complex systems into simpler nodes. Boundaries normally end at equipment or valves such as control valves, isolation valves, separators, exchangers, coolers, pumps, vessels, or tanks.
- Cover every relevant line and equipment item within the study scope.
- Define design intent from available P&IDs, PFDs, H&MB, datasheets, material specifications, operating procedures, or user-supplied basis.
- Include normal operating range, key design limits, materials, connected upstream/downstream systems, utility interfaces, relief/vent/drain paths, recycle paths, bypasses, and common headers when available.
- Include non-routine modes when in scope: startup, shutdown, emergency startup/shutdown, commissioning, decommissioning, decoking, maintenance lineup, standby, bypassed, isolated, blocked-in, and special operating modes.
- Do not turn HAZOP generation into a general design, layout, fire-and-gas, or safety-distance review unless the user asks for that scope.

## Parameter-First Deviation Rules

Generate deviations by selecting a parameter, then testing guide words. Keep only combinations with physical meaning for the node.

Common parameters:

- Flow, pressure, temperature, level, viscosity, reaction, composition, mixing, stirring, transfer, separation, time, aging, phase, speed, particle size.
- Addition, measure, monitoring, pH, sequence, signal, start/stop, operate, maintain, control, diagnostics, services, communication.

Guide words:

| Guide word | Generation meaning |
| --- | --- |
| No | None of the intended function occurs |
| More | Quantitative increase |
| Less | Quantitative decrease |
| As well as | Extra effect, contaminant, impurity, or extra activity |
| Part of | Partial achievement, missing component, weak concentration, or incomplete function |
| Reverse | Logical opposite, such as reverse flow or reverse reaction |
| Other than | Wrong material, wrong action, wrong destination, or substituted intent |

Include utility failures when relevant, such as instrument air, cooling water, steam, nitrogen, power, seal fluid, vent, drain, or service failure.

## Deviation Matrix Prompts

Use this matrix as a prompt for completeness, not as a row list to force blindly:

| Parameter | Common useful deviations |
| --- | --- |
| Flow | high flow, low flow, no flow, reverse flow, contamination, wrong concentration, wrong material |
| Pressure | high pressure, low pressure, vacuum |
| Temperature | high temperature, low temperature |
| Level | high level, low level, no level |
| Time | too long, too late, too short, too soon, wrong time |
| Reaction | fast reaction, runaway, slow reaction, no reaction, reverse reaction, incomplete reaction, side reaction, wrong reaction |
| Mixing | excessive mixing, poor mixing, no mixing, foaming |
| Draining or venting | too long, too short, none, wrong pressure condition |
| Sequence | step too late, step too early, no sequence, step backward, extra action, omitted action, wrong action |
| Inerting | high pressure, low pressure, none, contamination, wrong material |
| Vibration | too low, too high, none, wrong frequency |

## Cause Credibility Rules

Each row should have one distinct initiating cause and one distinct unmitigated consequence path. Similar causes may still need separate rows when they have different consequences, safeguards, IPLs, or risk ranking.

Use specific cause wording:

- Good: `<tag or equipment> <failure mode or wrong action> causing <immediate process effect>`.
- Weak: generic `equipment failure`, `operator error`, `instrument failure`, `utility failure`, or `human error` without a tag, task, failure mode, or scenario condition.

Do not normally generate these causes unless plant experience, design case, or explicit scope supports them:

- Simultaneous independent failures or double jeopardy.
- Natural events such as storm, hurricane, earthquake, or flooding.
- External impacts such as dropped objects or sabotage.
- Incredible manual valve closure/opening, especially valves not normally operated in the mode under study, such as maintenance isolation valves, control-valve bypass valves, and tie-in valves.
- Generic single-point piping or gasket deterioration, except recognized shell-and-tube exchanger tube rupture cases.

For shell-and-tube exchanger tube rupture:

- If the accepted pressure-rule design basis prevents overpressure or LOPC on the lower-pressure side, record that inherent safer design basis.
- If that basis is not established, identify the need to review pressure protection such as PSV coverage.

## Consequence Construction Rules

Write unmitigated consequence text before safeguards:

`<Cause> creates <deviation/local upset> at <node or tag>. This propagates <downstream/upstream/recycle/common-header/utility/relief path>. The unmitigated hazardous state is <LOPC/overpressure/vacuum/dry running/overheating/off-spec/etc.>, leading to <ultimate consequence>.`

Required consequence checks:

- Does the cause take the system outside the intended operating range?
- What happens locally at the failed item?
- What happens downstream in the normal flow direction?
- What happens upstream or by backpressure?
- Does a recycle, bypass, side draw, common header, utility, relief, vent, or drain path create another effect?
- Is there LOPC, fire, explosion, toxic/corrosive exposure, environmental release, equipment damage, off-spec product, or significant operability loss?

Do not include safeguards in consequence wording. Move alarms, trips, PSVs, rupture disks, operator response, procedures, containment, fire and gas detection, and emergency response to safeguard/IPL fields.

If there is no credible safety, health, environmental, asset, or significant operability consequence, record the no-hazard decision and stop the HAZOP/LOPA path.

Avoid overly remote or long-duration consequence chains unless the study basis supports them. For normal HAZOP worksheet generation, stop at the immediate credible consequence outside the node or at the detection/protection handoff point.

## Initial Risk And IEL Rules

Initial risk is based on unmitigated consequence severity and initiating-event likelihood before IPL credit.

- Evaluate severity in safety/human health, environment, and asset/equipment dimensions.
- Select the highest credible severity as governing severity.
- Do not average severity dimensions.
- Count asset/equipment severity from direct equipment/property damage and direct restoration or downtime basis only, unless project criteria say otherwise.
- Use the company risk matrix and initiating event likelihood table when supplied.
- If final company risk criteria are missing, keep risk values as screening only and recommend verification of risk-matrix, IEL, and IPL basis.
- For startup, shutdown, batch, or infrequent tasks, adjust frequency only when the operating-frequency basis is provided.

Screening IEL examples from the procedure appendix include:

| Initiating event family | Screening frequency |
| --- | --- |
| BPCS loop, instrument, regulator, valve, cooling-water failure, or redundant power loss | 1E-1 per year |
| Rotating equipment, pump seal, hose leak/rupture, compressor/pump overspeed | 1E-1 per year |
| Gasket/packing blowout, fixed equipment failure, exchanger tube failure, safety valve opens spuriously, PSV failure | 1E-2 per year |
| Turbine/diesel overspeed with casing breach | 1E-4 per year |
| Single check valve high-demand failure | 1E-1 per year |
| Double dissimilar check valves high-demand failure | 1E-2 per year |
| Routine operator task weekly or more often | 1 per year |
| Routine operator task monthly to weekly | 1E-1 per year |
| Non-routine operator task less than monthly | 1E-2 per year |
| LOTO checklist failure | 1E-3 per opportunity |

Use these values only when the scenario clearly matches and the project accepts this basis.

## IPL And PFD Rules

Existing safeguards are not automatically IPLs. A credited IPL must be:

- Independent from the initiating event and other credited IPLs.
- Effective for the specific consequence and fast enough for the scenario.
- Auditable, inspectable, testable, or procedurally verifiable.
- Designed for the scenario and service.
- Maintained and managed with an owner-approved basis.

Screening PFD examples from the procedure appendix include:

| IPL family | Screening PFD |
| --- | --- |
| Open vent with no valve | 1E-2 |
| Overflow line with no impediment | 1E-3 |
| Overflow line with passive fluid or rupture disk | 1E-2 |
| Overflow line that may freeze, foul, or be closed | 1E-1 |
| Permanent mechanical stop | 1E-2 |
| Inherent safer design | 1E-2 or consequence eliminated by team basis |
| Captive key or lock system | 1E-2 |
| Adjustable movement-limiting device | 1E-1 |
| Restriction orifice in clean noncorrosive nonerosive service | 1E-2 |
| Multiple mechanical pump seal with detection or indication | 1E-1 |
| Human response to alarm, check, sample, or verification | 1E-1 |
| BPCS loop or interlock | normally no more than 1E-1 credit without company/IEC basis |
| SIL 1 SIF | 1E-2 <= PFD < 1E-1 |
| SIL 2 SIF | 1E-3 <= PFD < 1E-2 |
| SIL 3 SIF | 1E-4 <= PFD < 1E-3 |
| Relief valve, rupture disk, or breather valve designed for scenario | 1E-2 |
| Single check valve, low-demand clean service | 1E-1 |
| Double dissimilar check valves, low-demand clean service | 1E-2 |
| Pressure regulator | 1E-1 |

Special IPL caveats:

- Do not credit a future recommendation as an existing IPL.
- Human response requires a clear alarm/check, written action, training, response time, low complexity, and safe working conditions.
- Relief devices get credit only when designed and sized for the scenario.
- If relief effectiveness depends on another device, treat the combination as one IPL using the weaker PFD.
- If isolation valves can defeat a relief device, use weaker credit unless valve-position management is established.
- Check valves alone are not sufficient IPLs for overpressure of low-pressure equipment due to reverse flow from a high-pressure system; review relief protection as well.
- Do not count BPCS as both initiating event and IPL without explicit multiple-loop independence basis.

## Existing 22-Column Generator Mapping

When the graph-agent generator must output its current 22 CSV fields, map the procedure logic as follows:

- `Node`: selected node boundary or source-to-destination pair.
- `Guide Word`, `Parameter`, `Deviation`: from parameter-first deviation generation.
- `Cause`: one credible initiating cause with tag/action/failure mode when available.
- `Consequence`: unmitigated event path with no safeguards embedded.
- `Unmitigated Risk Category`, `S Before Safeguards`, `L Before Safeguards`, `RR Before Safeguards`, `Overall Risk`: screening initial risk using the supplied matrix.
- `Safeguards`: existing safeguards plus candidate IPLs, clearly marking any missing IPL basis.
- `Mitigated Risk Category`, `S`, `L`, `RR`, `Overall Risk`: screening mitigated risk after only credited IPLs.
- `Recommendations`: specific action to close remaining risk gap or missing basis, such as risk-matrix confirmation, IEL verification, IPL independence/effectiveness/auditability proof, SIL classification, relief sizing check, procedure update, or instrument cause-and-effect verification.
- `S/L/RR After Recommendation`: expected screening state after recommendation. If the recommendation is only a study or verification, do not overclaim risk reduction.

## Final Row QA Checklist

Before returning rows, reject or revise any row where:

- The cause is a process state, consequence, or safeguard failure after another initiating event.
- The cause is unsupported double jeopardy, natural event, external impact, random manual-valve action, or generic piping/gasket deterioration.
- The consequence assumes an alarm, trip, PSV, operator response, or other protection layer also fails.
- The consequence stops at vague wording such as `equipment damage` without saying what changes physically.
- Safeguards and IPLs are mixed without qualification.
- Risk scores are presented as final acceptance when plant criteria are missing.
- The recommendation is generic and does not close a specific remaining gap.

---
name: hazop-lopa-assessor
description: Coordinate an end-to-end HAZOP/LOPA assessment using embedded SCG-style HAZOP/LOPA workflow plus project criteria supplied by the user. Use when Codex needs to review or draft HAZOP worksheet rows, read PFD/P&ID intent, trace upstream/downstream effects, compare safety/environment/asset severity, assign initiating-event likelihood, review safeguards/IPLs, calculate mitigated likelihood, and draft recommendations without inventing missing risk-matrix data.
---

# HAZOP-LOPA Assessor

## Use Boundary

Use the criteria embedded in this skill and any project-specific basis supplied by the user. Do not assume hidden files, private databases, or company matrices.

If the applicable company risk matrix is missing, do not invent final severity score, likelihood score, or risk rank. Complete the engineering logic and mark the exact missing basis.

Use the companion skills when available:

- `hazop-pfd-pid-tracer` for reading PFD/P&ID topology and tracing effects.
- `hazop-cause-consequence-assessor` for cause credibility, row splitting, unmitigated consequence chains, and no-hazard decisions.
- `hazop-severity-assessor` for safety, environmental, and asset/equipment severity comparison.
- `hazop-lopa-ipl-assessor` for initiating event likelihood, IPL credit, and mitigated likelihood.
- `hazop-risk-ranking-assessor` for initial/final risk lookup, category consistency, and recommendation triggers.

## Team Working Style

Work like a HAZOP team in a workshop, not as a single free-form brainstorm.

1. State the node and design intent.
2. Confirm normal operation, non-routine modes, and drawing boundaries.
3. Select one parameter and one guide word.
4. Generate one meaningful deviation.
5. Ask, "What can cause this deviation in this node?"
6. For each credible cause, trace the unmitigated event path.
7. Check consequence severity in the three dimensions: safety/human health, environment, and asset/equipment.
8. Select the governing severity as the most severe credible dimension.
9. Select initiating event likelihood from supplied IEL basis.
10. Look up initial risk from the supplied risk matrix.
11. Identify existing safeguards, then separate credited IPLs from non-credited safeguards.
12. Calculate mitigated likelihood only from credited IPLs.
13. Look up final risk from the supplied risk matrix.
14. Draft recommendations for remaining risk gaps, missing bases, or failed IPL criteria.
15. Record assumptions and missing data explicitly.

## SCGC Procedure Overlay For Generation

When drafting rows for the graph-agent generator, apply the user-provided SCGC HAZOP-LOPA procedure as a generation gate:

1. Confirm node boundary and design intent before drafting causes.
2. Use parameter-first deviation generation, then keep only meaningful guide-word combinations.
3. Screen each initiating cause for node-specific credibility.
4. Trace the unmitigated consequence before naming safeguards.
5. Evaluate safety, environmental, and asset/equipment severity separately and select the governing severity.
6. Separate existing safeguards from credited IPLs, and credit only IPLs with independence, effectiveness, auditability, design basis, and management basis.
7. Write a recommendation only for a real residual risk gap, missing basis, failed IPL criterion, or required verification.

Use the procedure appendix prompts as screening aids: standard deviation matrix prompts, initiating-event likelihood examples, IPL/PFD examples, and caveats for human response, BPCS, relief devices, check valves, and SIL/SIF claims. Do not treat those prompts as proof that project-specific criteria are accepted.

For the current 22-column generator schema, keep the risk numbers as screening values when final plant criteria are missing, and make the recommendation explicitly request risk-matrix, IEL, IPL, SIL, relief sizing, or operating-basis confirmation as applicable.

## Core Definitions

- HAZOP: Hazard and Operability Study.
- LOPA: Layer of Protection Analysis.
- IPL: Independent Protection Layer.
- IEL: Initial Event Likelihood.
- LOPC: Loss of Primary Containment.
- PFD: Probability of Failure on Demand.
- PFD drawing: Process Flow Diagram.
- P&ID: Piping and Instrument Diagram.
- SDS: Safety Datasheet.
- Double jeopardy: two independent initiating events occurring at the same time.

## Workflow

Follow the seven-step process HAZOP/LOPA flow:

1. Divide the system into nodes.
2. Select a node and define design intent.
3. Identify deviations using guide words and parameters.
4. Identify causes and consequences; evaluate initial risk from cause likelihood and consequence severity.
5. Identify safeguards/IPLs; evaluate final risk after credited IPLs.
6. Agree recommendations or actions for remaining risk gaps.
7. Repeat until all causes, consequences, guide words, parameters, and nodes are covered.

## PFD/P&ID Reading Requirements

Before writing causes or consequences, build a mental process graph:

- Equipment nodes: vessels, columns, exchangers, pumps, compressors, filters, reactors, tanks, packages.
- Line edges: source, destination, normal flow direction, recycles, vents, drains, bypasses, relief lines, utility lines.
- Control elements: control valves, manual valves, check valves, restrictions, regulators, interlocks, trips.
- Measurements: pressure, temperature, flow, level, composition, vibration, analyzer, permissive signals.
- Safeguards: alarms, trips, PSV/rupture disc, containment, drains, procedures, mechanical limits.
- Interfaces: upstream feed, downstream users, recycle loops, utilities, flare/vent/drain systems, common headers.

For any failed equipment or valve, trace:

1. Local effect at the failed item.
2. Downstream effect along normal flow.
3. Upstream or backpressure effect against the normal flow.
4. Recycle or side-draw effect, if applicable.
5. Utility effect, if utility supply or removal changes.
6. Control-loop response and possible control-loop failure mode.
7. Relief/vent/drain path and whether it creates another consequence.
8. Common-cause or common-header impact to parallel equipment.

Do not stop at "equipment damage." State what the damage changes: loss of containment, loss of flow, overpressure, reverse flow, overheating, dry running, contamination, off-spec product, environmental release, or personnel exposure.

## Parameters And Guide Words

Use a parameter-first approach. Keep only combinations with physical meaning for the node.

Common parameters:

- Flow, pressure, temperature, level, composition, phase, reaction, viscosity, speed, pH.
- Mixing, addition, separation, time, sequence, start/stop, signal, measurement, control.
- Transfer, services, utilities, communication, diagnostics, aging.

Guide words:

| Guide word | Meaning |
| --- | --- |
| No / none | None of the design intent is achieved |
| More | Quantitative increase |
| Less | Quantitative decrease |
| As well as | Additional adverse effect |
| Part of | Only part of the design intent is achieved |
| Reverse | Logical opposite of design intent |
| Other than | Complete substitution or wrong material/action |

Include utility failures such as instrument air, cooling water, steam, nitrogen, power, and drain/vent system failure when relevant.

## Cause Rules

Treat each distinct cause-consequence path as a separate row when it has different consequences, safeguards, IPLs, or final risk.

Do not normally use these causes unless plant experience, design case, or explicit scope supports them:

- Double jeopardy or simultaneous independent failures.
- Natural events such as storm, earthquake, hurricane, or flooding.
- External process impacts such as dropped objects or sabotage.
- Incredible manual operation of valves not normally operated.
- Generic single-point piping/gasket deterioration, except recognized exchanger tube rupture cases.

For shell-and-tube exchanger tube rupture:

- If pressure-rule design prevents LOPC on the lower design-pressure side, record inherent safer design basis.
- Otherwise review suitable overpressure protection, such as PSV.

## Consequence Rules

Ignore safeguards first. Write the unmitigated path from cause to deviation to process upset to ultimate consequence.

A good consequence includes:

- Immediate process effect.
- Equipment/instrument tag or affected item.
- Direction of propagation: downstream, upstream/backpressure, recycle, common header, utility, relief/vent/drain.
- Hazardous state: LOPC, overpressure, vacuum, dry running, overheating, toxic exposure, flammable cloud, fire/explosion, environmental release, off-spec product, or operability loss.
- Ultimate credible consequence.

Do not mix safeguards into the consequence text.

If no safety, health, environmental, asset/equipment, or significant operability consequence exists, mark no further HAZOP/LOPA evaluation for that path.

For deeper cause/consequence review, use `hazop-cause-consequence-assessor`.

## Severity Rule

Always evaluate three dimensions separately:

1. Safety / human health.
2. Environmental impact.
3. Asset / equipment damage and process interruption.

Then compare the three results and select the governing severity as the most severe credible dimension. Keep the non-governing dimensions in the rationale so reviewers can see why they were not selected.

For asset/equipment severity, count only direct equipment/property damage, repair/replacement, associated cleanup needed to restore the equipment area, and direct interruption/downtime if the project risk matrix uses downtime. Do not count business reputation, remote market loss, or unrelated commercial loss unless the user supplies a company rule.

## Initial And Final Risk

Initial risk:

- Use unmitigated consequence severity.
- Use initiating event likelihood before IPL credit.
- Look up risk rank in the supplied company risk matrix.

Final risk:

- Use the same severity unless a safeguard genuinely changes the consequence category, not merely its frequency.
- Reduce likelihood only by credited IPLs.
- Look up final risk in the same supplied risk matrix.

Never calculate risk rank by multiplying severity and likelihood unless the user-provided matrix explicitly defines that method.

For risk-rank lookup and consistency checks, use `hazop-risk-ranking-assessor`.

## IPL Handling

Separate safeguards from credited IPLs.

Credit an IPL only when it is:

- Independent from the initiating event and other credited IPLs.
- Effective for the scenario.
- Auditable, inspectable, testable, or procedurally verifiable.
- Designed for the scenario.
- Maintained and managed.

Do not credit a future recommendation as an existing IPL.

For alarm/operator response, require clear alarm/check, written response guidance, response time, trained operator, low-complexity action, and safe working conditions.

## Worksheet Output

Use the user's worksheet schema when supplied. Otherwise use:

- Node
- Design intent
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
- Safeguards
- Credited IPLs and PFD/credit
- Final likelihood
- Final risk
- Recommendation/action
- Owner
- Missing basis / assumptions

## Engineer Worksheet Style

When writing rows, emulate concise engineer worksheet style:

- Cause: tag/equipment + failure mode + immediate process effect.
- Consequence: process effect through affected equipment to ultimate effect.
- IPLs: numbered items with tags and credit only when justified.
- Recommendations: specific action tied to the missing basis or remaining risk gap, such as SIL classification for a credited interlock without SIL basis.
- Avoid final outputs that only say `See ...` another parameter/deviation. Expand the referenced path or mark it as needing expansion.

## Review Before Finalizing

Check:

- Node boundary and design intent are explicit.
- PFD/P&ID propagation was traced downstream, upstream, and through utility/recycle/relief paths.
- Cause is credible and not unqualified double jeopardy.
- Consequence is unmitigated and reaches an ultimate effect.
- Safety, environment, and asset severities were compared.
- Governing severity is the worst credible dimension.
- Initial likelihood is not reduced by safeguards.
- Safeguards and IPLs are separated.
- Recommendations close a specific risk gap.
- Missing risk matrix, IEL, IPL basis, SDS, P&ID, or operating range is called out.

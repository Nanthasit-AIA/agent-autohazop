---
name: hazop-cause-consequence-assessor
description: Analyze HAZOP causes and consequences as distinct engineering event paths. Use when Codex needs to decide cause credibility, exclude double jeopardy or weak causes, split worksheet rows, trace unmitigated consequence chains from deviation to ultimate effect, decide no-hazard cases, and ensure consequences are not mixed with safeguards.
---

# HAZOP Cause Consequence Assessor

## Purpose

Turn a deviation into credible cause-consequence paths that a HAZOP team can review one by one.

Do not start risk ranking until the cause and unmitigated consequence are technically clear.

## Workshop Sequence

For one node, one parameter, one guide word, and one deviation:

1. Restate the node boundary and design intent.
2. Restate the deviation in process terms.
3. Ask what can cause the deviation inside the node.
4. Screen each cause for credibility.
5. Trace the cause through the PFD/P&ID network before writing consequence text.
6. Write the unmitigated consequence while ignoring safeguards.
7. Identify the ultimate effect.
8. Split paths when one cause has multiple ultimate consequences or different safeguards/IPLs.
9. Stop the path when no safety, health, environmental, asset/equipment, or significant operability consequence exists.
10. Send the accepted consequence to severity and risk ranking.

## Cause Credibility

A cause is credible when:

- It can physically create the deviation.
- It fits the node, operating mode, material, and equipment arrangement.
- It is not already a consequence of another listed cause.
- It is specific enough for safeguards and recommendations to be assessed.
- It is supported by drawing information, operating experience, equipment failure mode, human task, utility failure, or explicit user input.

Weak cause wording to improve:

- `Equipment failure` -> name the equipment and failure mode.
- `Human error` -> name the task, wrong action, omitted action, or timing error.
- `Instrument failure` -> name signal, transmitter, controller, valve, or bad calibration effect.
- `Utility failure` -> name utility and what process function is lost.

## Exclusion Rules

Do not normally use these as causes unless user-supplied plant experience, design case, or explicit study scope supports them:

- Double jeopardy: two independent initiating events at the same time.
- Natural events such as storm, hurricane, earthquake, flooding, or lightning.
- External impacts such as dropped objects or sabotage.
- Incredible operation of valves not normally operated, such as maintenance isolation valves, control-valve bypass valves, or tie-in valves.
- Generic piping or gasket deterioration as a single-point failure, except recognized exchanger tube rupture cases.

For shell-and-tube exchanger tube rupture:

- If pressure-rule design prevents LOPC on the lower design-pressure side, record inherent safer design basis.
- Otherwise, review overpressure protection need, such as PSV.

## Cause Categories To Consider

Use these prompts without forcing them:

- Instrument/signal failure: transmitter, sensor, analyzer, controller, bad calibration, wrong setpoint.
- Final element failure: control valve stuck open/closed, actuator failure, regulator failure, damper failure.
- Mechanical failure: pump/compressor/fan failure, seal failure, bearing failure, tube rupture, blockage, fouling, erosion/corrosion where allowed.
- Utility failure: power, instrument air, nitrogen, steam, cooling water, hot oil, vacuum, seal fluid.
- Human task failure: wrong valve line-up, wrong sequence, late/early action, omitted step, LOTO failure, maintenance reinstatement error.
- Process/material cause: abnormal feed, contamination, wrong material, decomposition, runaway, phase change, solids formation.
- External interface: upstream pressure/flow/composition abnormality, downstream restriction, common header upset.

## Consequence Construction

Write consequence as an event chain:

`<Cause> creates <deviation/local process upset> at <tag/node>. This causes <downstream/upstream/recycle/utility effect>. The unmitigated hazardous state is <LOPC/overpressure/vacuum/dry running/overheating/etc.>, leading to <ultimate consequence>.`

The consequence should include:

- Immediate process effect.
- Affected equipment or instrument tag when known.
- Propagation direction.
- Hazardous state.
- Ultimate credible effect.

Engineer worksheet style to emulate:

- Write causes as `<tag/equipment> <failure mode> resulting in <immediate process effect>`.
- Name the affected equipment in both the cause and consequence when possible.
- Use direct process language: loss of feed, loss of suction, pump cavitation, tank underpressure, tank overpressure, roof damage, seal LOPC, pool fire, fire scenario.
- Keep the wording concise but complete enough that another engineer can follow the physical path.
- If the row depends on another deviation or parameter, do not leave it as `See ...` in the final answer. Expand the referenced scenario into a complete cause-consequence path, or mark it as a duplicate reference that needs expansion.

Ultimate effects include:

- Personnel exposure, injury, fatality, asphyxiation, burn, toxic/corrosive exposure.
- Fire, flash fire, pool fire, jet fire, explosion, pressure burst, projectile.
- Environmental release to soil, water, atmosphere, drain, sewer, marine, groundwater, or community.
- Asset/equipment damage, collapse, rupture, tube failure, seal failure, dry-running damage.
- Off-spec product or significant operability loss.

## Safeguard Separation

Do not include safeguards in consequence wording.

Move these to safeguards/IPLs:

- Alarms.
- Trips/interlocks/SIF.
- PSV/rupture disc/breather valve.
- Operator response.
- Procedures/checklists.
- Preventive maintenance.
- Secondary containment.
- Fire and gas detection.
- Emergency response.

Wrong pattern:

`High pressure causes PSV to open, preventing rupture.`

Better pattern:

`High pressure can exceed equipment design pressure, leading to LOPC and possible fire/explosion if containment fails.`

Then list `PSV` separately as a safeguard or IPL candidate.

## Row Splitting Rules

Split into separate rows when:

- One cause has multiple ultimate consequences with different severities.
- Consequences use different safeguards or IPLs.
- Consequences affect different receptors, such as personnel versus environment versus asset.
- One path is no hazard and another path is hazardous.
- Initial or final risk ranking would differ.

Do not split when the wording is merely a more detailed description of the same event path.

When a worksheet uses shorthand such as `See No/Less Flow...`, treat it as an internal cross-reference only. For generated output, write the full path or state `Referenced scenario needs expansion`.

## No-Hazard Decision

Mark no further HAZOP/LOPA evaluation when the unmitigated path has no credible:

- Safety or health effect.
- Environmental effect.
- Asset/equipment damage.
- Significant operability or product-quality effect.

Still record the reason, such as `No safety, health, environmental, asset, or significant operability consequence identified`.

## Output Format

For each path, output:

- Deviation.
- Cause.
- Cause credibility: accepted / rejected / needs basis.
- Rejection or uncertainty reason, if any.
- Unmitigated consequence chain.
- Ultimate consequence.
- Propagation path: local, downstream, upstream, recycle/common header, utility, relief/vent/drain.
- Row split decision.
- No-hazard decision, if applicable.
- Missing basis.

## Quality Check

Before passing to severity/risk:

- Cause is not a safeguard failure unless it is the initiating event under review.
- Cause is not double jeopardy without explicit basis.
- Consequence ignores safeguards.
- Consequence reaches an ultimate effect.
- Equipment tags and affected systems are named where available.
- The path can be understood by another engineer without hidden reasoning.

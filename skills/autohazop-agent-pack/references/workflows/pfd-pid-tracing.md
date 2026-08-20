---
name: hazop-pfd-pid-tracer
description: Read PFDs and P&IDs as process networks for HAZOP. Use when Codex needs to infer design intent, node boundaries, normal flow direction, upstream/downstream propagation, backpressure, recycle/common-header effects, utility effects, relief/vent/drain paths, control-loop behavior, and what equipment may be affected if an item fails.
---

# HAZOP PFD/P&ID Tracer

## Purpose

Convert drawing information into an engineering event-path map before generating HAZOP causes and consequences.

Do not assume hidden drawings. Use only tags, lines, valves, instruments, services, and narrative supplied by the user.

## Team Workflow

Work in the same order a HAZOP team would talk through a drawing:

1. Orient the node: equipment, line numbers, normal flow direction, operating mode.
2. Define boundaries: inlet isolation/control points, outlet isolation/control points, relief/vent/drain limits, utility interfaces.
3. Identify normal design intent: what should flow, at what phase/condition, at what pressure/temperature/level/quality target.
4. Build a process graph: equipment as nodes and lines as directed edges.
5. Mark control loops and protective devices on the graph.
6. For each failed item, trace effects downstream, upstream, sideways through recycle/common headers, and through utilities.
7. Stop propagation at a credible detection point, protection system, inventory break, or explicitly defined study boundary.
8. Record uncertainty where drawing detail is missing.

## Drawing Objects To Extract

- Equipment: pumps, compressors, exchangers, reactors, columns, vessels, tanks, filters, packages.
- Lines: process, recycle, bypass, vent, drain, relief, flare, sample, utility, chemical injection.
- Valves: manual, control, check, isolation, bypass, relief, regulator, fail-open/fail-closed if known.
- Instruments: PI/PT, TI/TT, FI/FT, LI/LT, analyzers, alarms, trips, interlocks, permissives.
- Utilities: cooling water, chilled water, steam, hot oil, instrument air, nitrogen, power, vacuum, seal fluid.
- Containment and disposal: bunds, closed drain, open drain, flare, scrubber, vent stack, sewer.

## Propagation Questions

For a failed equipment item or valve, answer these before writing the consequence:

- What changes immediately at the failed item?
- What downstream equipment receives too much, too little, wrong composition, wrong phase, wrong pressure, or wrong temperature?
- What upstream equipment sees backpressure, blocked outlet, no suction, reverse flow, deadhead, flooding, or vacuum?
- Does a recycle, bypass, or common header spread the upset to parallel equipment?
- Does a utility failure remove heat, add heat, remove pressure control, remove inerting, or remove motive force?
- Does a relief/vent/drain path send material to flare, atmosphere, closed drain, open drain, sewer, or containment?
- Does a control loop respond correctly, saturate, fail, or hide the condition?
- Can a check valve, isolation valve, or regulator create or prevent reverse flow?

## Failure Mode Patterns

- Pump fails stopped: downstream low/no flow; upstream level/pressure may rise; downstream equipment may starve; spare pump/common suction may be affected.
- Pump deadheaded or outlet blocked: pump heats, pressure rises, seal damage, possible leak/fire depending on service.
- Pump runs dry: seal/bearing damage, leak, ignition risk if flammable, no downstream flow.
- Pump suction lost from upstream tank low level or blocked inlet: cavitation, seal damage/LOPC, loss of downstream transfer, and possible fire if flammable service.
- Control valve fails closed: downstream low/no flow; upstream pressure/level rise; possible relief if blocked-in.
- Control valve fails open: downstream high flow/overfill/overpressure; upstream low level/pressure.
- Check valve fails open/leaks: reverse flow from high-pressure downstream to low-pressure upstream; possible contamination or overpressure.
- Exchanger tube rupture: high-pressure side can enter low-pressure side; possible overpressure, contamination, relief, or downstream release.
- Cooling loss: downstream high temperature, pressure rise, vaporization, reaction acceleration, product off-spec.
- Heating uncontrolled: high temperature, overpressure, decomposition, fire/explosion potential depending on material.
- Blocked vent/drain: pressure/vacuum control lost, slow depressurization/draining, possible overpressure/vacuum collapse.
- Nitrogen blanketing failure: tank underpressure/vacuum during outflow or cooldown, or overpressure if vent/blanketing control fails closed/open depending on arrangement.
- Tank overfill or high inflow: high level, possible overflow/vent release, roof or containment challenge, downstream consequences if transfer continues.
- Common header upset: one source failure or contamination can affect all users connected to the header.

## Consequence Wording

Write consequences as event paths:

`<Cause> causes <local process effect> at <tag>. This propagates <downstream/upstream/recycle/utility path> to <affected equipment>. The unmitigated result is <hazardous state> leading to <ultimate consequence>.`

Keep safeguards out of the consequence. Put alarms, trips, PSV, procedures, and operator actions in safeguards/IPLs.

## Stop Rules

Stop and ask for more data when:

- Normal flow direction is unknown.
- Node boundary is unclear.
- Equipment tags or line connections conflict.
- Fail position of a critical valve is required but not supplied.
- Relief/vent/drain destination is unknown and affects consequence severity.
- Material hazards from SDS are needed but not supplied.

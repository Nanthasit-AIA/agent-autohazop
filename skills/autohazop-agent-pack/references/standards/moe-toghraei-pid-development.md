# Moe Toghraei - Piping and Instrumentation Diagram Development

Use this reference to extract practical P&ID context for HAZOP/LOPA, process safety review, operability review, and P&ID quality checking. It is derived from Moe Toghraei's book on P&ID development and focuses on what an agent should actually capture: topology, operating intent, design envelope, equipment weaknesses, valves, instruments, alarms, SIS, relief, utilities, and maintenance provisions.

Do not use this as a substitute for project P&ID standards, company drafting rules, ISA/ISO symbol standards, equipment datasheets, relief calculations, alarm rationalization, SIS lifecycle documents, or jurisdictional codes. Use it to ask the right questions and structure extracted context.

## Source Traceability

- Source book: `Piping and Instrumentation Diagram Development`, Moe Toghraei, first edition, 2019.
- Fundamentals, sheet anatomy, visual rules, and P&ID development principles: chapters 1-5.
- Pipes, valves, maintenance provisions, containers, pumps/compressors, heat transfer units, and pressure relief devices: chapters 6-12.
- Instrumentation, control architecture, plant control, SIS/interlocks, alarms, and motor control: chapters 13-16.
- Utilities: chapter 17.
- Safety/environmental ancillary systems, sampling, corrosion monitoring, plant model effects, and design pressure/temperature: chapter 18.
- General P&ID development and checking procedure: chapter 19.

## Applies To

- Reading or developing P&IDs for process plants, utilities, packages, and auxiliary systems.
- Extracting what each equipment item is connected to: lines, valves, drains, vents, instruments, control loops, interlocks, relief, utilities, and package boundaries.
- Reviewing whether a P&ID supports normal, nonroutine, startup, shutdown, maintenance, bypassed, isolated, reduced-capacity, and abnormal operation.
- Building a HAZOP/LOPA context graph from P&IDs and related documents.

## Does Not Provide

- A universal company drafting standard.
- Final valve, pipe, relief, control-loop, or instrument sizing.
- Proof that an alarm is rationalized or that a SIF is valid as an IPL.
- Vendor-specific package requirements.
- Exact symbol interpretation where the project legend differs.

## P&ID Context Graph

When reading a P&ID, build a graph with these node and edge types:

```yaml
nodes:
  equipment:
    tag:
    type:
    duty:
    design_pressure_temperature:
    normal_operating_window:
    maintenance_strategy:
  line:
    line_number:
    size:
    commodity:
    piping_class:
    insulation_tracing:
    spec_breaks:
    flow_direction:
  valve:
    tag:
    type:
    function:
    normal_position:
    fail_position:
    car_seal_or_lock_status:
  instrument:
    tag:
    measured_or_manipulated_parameter:
    location_symbol:
    signal_type:
    control_or_monitoring_role:
  safeguard:
    type:
    trigger:
    action:
    protected_item:
edges:
  flows_to:
  isolated_by:
  bypasses:
  recirculates_to:
  drains_to:
  vents_to:
  relieves_to:
  measures:
  controls:
  trips:
  alarms:
  supplies_utility_to:
```

## Development Hierarchy

When rules conflict, rank evidence in this order:

1. Jurisdictional health, safety, and environmental requirements.
2. Owner/client requirements and project standards.
3. Designer/operator/maintenance requirements.
4. Approved company guidelines.
5. General industry practice.

Mark any item based only on general practice as `assumption`; do not treat it as a project requirement.

## Sheet and Symbol Context

Extract from each P&ID sheet:

- Sheet title, drawing number, revision, reference drawing block, ownership block, comments block, and off-page connector references.
- Main-body items: pipes/flow conductors, equipment, instruments, signals, utilities, boundaries, packages, and notes.
- Item identifiers: symbol, tag, name/service, and technical information/callout.
- Drawing type: legend, system P&ID, network P&ID, interarea P&ID, detail P&ID, package/vendor P&ID, or auxiliary P&ID.

Quality flags:

- Off-page connectors missing or not traceable.
- Symbols inconsistent with the legend.
- Line crossing, signal crossing, or visual congestion that obscures topology.
- Vendor/package boundaries not clear.
- Reference flags to details or auxiliary drawings missing.

## Operating Modes To Extract

A P&ID should support the plant through its life cycle. For each item, identify whether the P&ID covers:

- Normal operation.
- Reduced-capacity operation.
- Reduced-efficiency operation.
- Startup.
- Shutdown.
- Inspection and maintenance.
- Operation while one item is absent, bypassed, isolated, or failed.
- Future expansion or future tie-in.

If a mode is not addressed, list the missing hardware, utility, valve lineup, procedure, or control function.

## Parameter Level Model

For pressure, temperature, level, flow, and composition, separate these bands:

- Normal operating value or band.
- Low/high alarm or operator-action band.
- Low-low/high-high trip or SIS band.
- Low/high structural integrity boundary, also used as mechanical design context.

Use this mapping:

| Parameter band | Typical layer | HAZOP extraction use |
|---|---|---|
| Normal | Process operation and BPCS | Defines intended operation. |
| Low/high | Alarm and operator action | Defines abnormal operation and operator response. |
| Low-low/high-high | SIS/interlock or shutdown | Defines automatic protective action. |
| Structural integrity boundary | Mechanical design / relief / vacuum protection | Defines what the item can tolerate. |

Do not confuse operating values with design values. Design pressure and design temperature are structural integrity values; normal operation may be far inside that envelope.

## Pipes and Line Context

For each line, extract:

- Line tag, commodity/service, line size, piping class/material spec, sequential number, insulation/tracing, and any note such as intermittent, normally no flow, slope, minimum length, no pocket, or do not pocket.
- Whether the flow conductor is a pipe, tube, hose, duct, channel, or trench. Pipe tags usually belong to piping that needs pressure testing and line-list control.
- Off-page connectors and sheet continuation.
- Route intent: normal flow, bypass, recirculation, series units, parallel units, pressure equalization, diversion, distribution, gravity flow, self-draining, free-venting, no gas pocket, or no liquid pocket.
- Source and destination pressure/energy basis. A flow arrow shows intended normal direction, not a guarantee that reverse flow cannot occur.

Spec-break/border extraction:

- Battery limit.
- Area border.
- Package/vendor border.
- Work-division border.
- Aboveground/underground border.
- Piping spec/material/class break.

Spec breaks may require a flange, block valve, or block-valve/check-valve arrangement. Record the exact boundary side and which class covers the valve or border item.

## Valve Context

Classify each valve by function:

- Blocking/isolation.
- Throttling/manual adjustment.
- Control valve.
- Switching/on-off valve.
- Check valve/backflow prevention.
- Regulator.
- Safety-related valve.
- Multiport/diverting/mixing valve.
- Restriction orifice plus valve arrangement.

Extract these attributes:

- Tag and whether tagging is project-required for manual valves.
- Normal position: normally open, normally closed, locked open/closed, car sealed open/closed.
- Fail position for automatic valves: fail open, fail closed, fail last/locked, and whether this is power-loss or signal-loss behavior.
- Actuator energy: manual, pneumatic, hydraulic, electric motor, solenoid, or mixed pneumatic/electric arrangement.
- Bypass and isolation station around control valves.
- Drain/vent valves trapped between isolations.
- Reducer/enlarger type around reduced-body control valves.

Decision flags:

- Fail position chosen without safety, equipment protection, or process-smoothness basis.
- Control valve bypass present where manual pressure control could threaten downstream integrity.
- Switching valves in parallel for safety service without clear justification.
- Spec break downstream of a pressure-reducing valve/control valve not shown or not protected.
- Check valve absent where reverse flow could damage idle equipment or migrate pressure.

## Maintenance and Isolation

For each equipment item, ask:

1. Can the plant afford to operate without this item?
2. What isolation strength is required by fluid hazard, pressure, and human-entry risk?
3. Where should isolation be placed relative to the equipment?
4. How will pressure, temperature, level, flow, and composition be made safe?
5. How will fluids be drained, vented, washed, purged, or sampled?
6. Are removable spools needed to physically remove the item?

Isolation types to recognize:

- Block valve plus blind.
- Double block and bleed with blind.
- Block valve plus removable spool.

Extract maintenance provisions:

- Upstream and downstream isolation close to equipment.
- Blinds/spades/spectacle blinds and their normal state.
- Vents at high points and drains at low points.
- Drain/vent destination: atmosphere, safe location, open drain, closed drain, closed hydrocarbon drain, sump, flare, or process return.
- Washing, steam-out, purging, inerting, clean-in-place, and manual cleaning connections.
- Removable spools at pumps, exchangers, vessels, tanks, and flanged nozzles.

Do not credit maintenance isolation as an IPL unless the LOPA basis explicitly supports it.

## Containers, Tanks, and Vessels

For each container, extract:

- Type and duty: storage, surge, separation, reaction, buffer, mixing, sump, silo, open basin, or vessel.
- Material phase: flowable solid, nonvolatile liquid, volatile liquid, gas/vapor, two-phase.
- Nozzle duties: inlet, outlet, overflow, drain, vent, relief, blanketing, sample, instrument, manway, recirculation, utility, cleaning.
- Nozzle locations relative to liquid levels and operating modes.
- Level bands: normal, high, high-high, low, low-low, overflow, pump low suction risk.
- Breathing/venting, blanketing, vacuum protection, overflow, secondary containment, and drainage.

HAZOP prompts:

- Can inflow continue while outflow is blocked?
- Can outflow continue while inflow is stopped?
- Can gas/vapor breathing be blocked or overwhelmed?
- Is blanketing or inert gas loss hazardous?
- Can nozzle location create dead zones, siphon, overflow, or pump dry-running?

## Pumps, Compressors, and Fluid Movers

For each fluid mover, extract:

- Suction source, discharge destination, normal/standby/lead-lag role, and spare philosophy.
- Suction-side protection: NPSH/cavitation context, strainer, isolation, drain/vent, minimum straight run if relevant.
- Discharge-side protection: check valve, isolation, pressure gauge/transmitter, relief for positive displacement pumps, and downstream class break.
- Minimum-flow protection: recirculation line, control loop, on-off recycle, restriction orifice, automatic recirculation valve, or continuous spillback.
- Recirculation destination: pump suction, upstream vessel, suction drum, or other safe destination.
- Warm-up/cool-down bypass, seal system, flush, quench, drain, and vent.
- Parallel-pump reverse flow risk and check valves.
- Series/booster pump relationship and NPSH basis.
- Compressor/blower anti-surge recycle and shutdown functions.

Do not assume any loop around a pump is minimum-flow protection. Identify the purpose from notes, controls, destination, and equipment datasheet.

## Heat Transfer Units

For exchangers, air coolers, fired heaters, and boilers, extract:

- Hot/cold side, shell/tube side, process side, utility side, and phase-change service.
- Isolation valves, vents, drains, chemical cleaning connections, bypasses, and pressure safety devices.
- Temperature control strategy: direct control, bypass control, utility flow control, air cooler fan/louver control, fired heater fuel control, or back-pressure control.
- Series/parallel arrangement and whether one item can be removed without shutting down the process.
- Extreme temperature protection: freezing, overheating, thermal shock, tube rupture, blocked-in thermal expansion, and loss of utility.

## Pressure Relief Devices

For each PRD, extract:

- Protected equipment or enclosure and which side is protected.
- Overpressure/vacuum scenarios if stated.
- Device type: PSV, vacuum relief valve, rupture disk, pressure/vacuum safety valve, buckling pin, or combination.
- Set pressure or burst pressure.
- Governing case if shown.
- Inlet/outlet sizes, orifice designation if shown, and discharge destination.
- Isolation valves and car-seal/lock status.
- Single, spare, parallel, series, rupture-disk-plus-PSV, or changeover arrangement.
- Emergency release collection network: header slope, top tie-in, no-pocket requirement, drains, reaction-force notes, flare/vent/scrubber/pop tank/disposal system.

Flags:

- PRD can be isolated without administrative or mechanical control.
- Inlet/outlet line smaller, longer, more pocketed, or more restrictive than project rules allow.
- Relief destination unclear, unsafe, or incompatible with fluid phase/hazard.
- Low-pressure downstream equipment is not protected after pressure reduction.

## Instrumentation and Signals

For each instrument, extract:

- Process parameter: pressure, temperature, level, flow, composition/analyzer, vibration, torque, current, position, or other equipment parameter.
- Role: element/sensor, transmitter, indicator, controller, alarm, switch, final element, selector, math function, permissive/inhibitive logic, or interlock.
- Location/accessibility from symbol divider: field, control room, field panel/cabinet, accessible/inaccessible.
- Signal type: pneumatic, electrical, digital/data, hydraulic, capillary, instrument air tubing, or hardwired discrete.
- Additional notes clarifying function, carrier, tag, or range.

Sensor arrangement prompts:

- Temperature sensor in small pipe may need enlarged spool or bend location.
- Pressure service with dirty/corrosive/precipitating fluid may need diaphragm seal, flush ring, or purge.
- Level is for containers/open channels/silos, not gas-filled lines.
- Flowmeter may need straight run, clean service, strainer, reduced line size, bypass, or online/offline maintenance plan.
- Analyzer often needs sampling, conditioning, return/waste, and utility support.

## BPCS and Control Architecture

For each loop, identify:

- Controlled parameter.
- Manipulated stream/final element.
- Setpoint source.
- Sensor location relative to valve/equipment.
- Final control element and fail behavior.
- Loop type: feedback, feedforward, cascade, ratio, selective, override, limit, split-range, parallel control, discrete control, or manual fallback.

Use these distinctions:

- Feedback reacts to measured deviation.
- Feedforward acts from a measured disturbance before it reaches the controlled variable.
- Cascade uses a primary controller to set a secondary controller setpoint.
- Ratio control sets one stream from another stream's measurement.
- Selective control chooses one of multiple sensor signals.
- Override control temporarily lets another loop protect a process/equipment constraint.
- Limit control constrains a control output or signal near a boundary.
- Discrete control is process on/off logic, not a safety interlock.

If a parameter has a control loop or SIF, expect control-room monitoring. If it has control-room monitoring, field monitoring may also be needed depending on operation and maintenance.

## SIS, Interlocks, and Alarms

For each protective function, extract:

- Initiating sensor or switch and setpoint type: high, high-high, low, low-low.
- Logic solver or interlock reference.
- Final element: switching valve, control/switching combined valve, motor trip/start, louver, damper, or other on/off final element.
- Trip action and safe state.
- Shutdown tier: equipment, system, unit, or plant.
- Cause-and-effect reference or shutdown key number.

Representation rules:

- P&IDs may show only an interlock tag or diamond instead of all logic lines. Use cause-and-effect documents for exact actions.
- Do not infer action from a line alone when a shutdown key exists.
- SIS is for safety; discrete BPCS is for process sequencing. Keep them separate.
- Alarms warn operators; alarms may exist without SIS, but a high-consequence or high-probability scenario needs explicit justification if no SIS exists.
- Field alarms are relevant when field operator evacuation or simple local action is required.
- Fire and gas systems may appear on auxiliary P&IDs; extract detector type, alarm levels, locations, and action if connected to shutdown.

## Utilities

For utility systems, extract:

- Users and priority users.
- Distribution and collection topology: header, subheader, ring, branch, return, condensate, drain, sewer, flare, vapor collection, instrument air, utility air, steam, cooling water, fuel gas, inert gas, firewater, or sampling utility.
- Root valves and area isolation.
- Tie-in details between utility and process.
- Cross-references between utility P&IDs and process P&IDs.
- Whether utility loss affects BPCS, SIS final elements, purging, blanketing, cooling, heating, or seal systems.

## Design Pressure and Temperature Checks

Extract design pressure and design temperature as a coincident pair when possible. Do not report `design pressure` without its associated `design temperature`.

Check:

- Normal, high, high-high, and structural integrity pressure/temperature levels.
- Rebel pressure or rebel temperature scenarios that can exceed normal operation.
- MAWP/design pressure source for vessels, tanks, pipe spools, flanges, instruments, and packaged equipment.
- Connected equipment with different design pressures.
- Pressure-reducing valves, regulators, control valves, or orifices that separate high-pressure and low-pressure systems.
- PSV or other limiting device downstream of pressure reduction.
- Check valves that prevent high pressure from migrating into a lower-rated upstream or branch system.
- Instrument/equipment connection ratings, especially sensors connected to higher-pressure equipment.

If connected items have different design pressures, flag whether the project uses inherent equalization to the higher rating or a limiting/protective design such as regulator plus PSV/check valve.

## P&ID Review Checklist

Use four levels of checking:

1. Format check: clarity, readability, naming, drawing consistency.
2. Demonstration-rules check: symbols, line styles, title/revision/reference blocks, off-page connectors, legend compliance.
3. Technical check: whether each item supports normal, nonroutine, maintenance, absence/bypass, and safety requirements.
4. Design check: whether the P&ID matches PFDs, line lists, datasheets, equipment lists, cause-and-effect charts, utility drawings, previous markups, and project basis documents.

Technical checks to run:

- Every relevant pipe has tag, size, commodity, spec, arrows, notes, spec breaks, reducers/enlargers, branch-table compatibility, slope/no-pocket comments, and insulation/tracing when needed.
- Every equipment item has required isolation, drain, vent, utility, sample, relief, control, monitoring, and maintenance provisions.
- Every valve has correct type, normal/fail position, accessibility/operator arrangement, and bypass/isolation context.
- Every PRD has protected item, set/burst pressure, destination, isolation control, and collection/disposal path.
- Every loop has sensor, controller/logic, signal, final element, fail state, and safe/manual fallback where needed.
- Every interlock has cause, effect, final action, and reference to cause-and-effect logic.

## HAZOP Extraction Prompts

For each node, ask:

- What is the intended duty and normal operating envelope?
- What lines and utilities feed it and what lines leave it?
- What can isolate it, bypass it, recirculate around it, drain it, vent it, or relieve it?
- What measurements tell operators/control systems the node is healthy?
- What control loop manipulates the node?
- What alarm warns before a trip or relief action?
- What interlock or SIS acts automatically?
- What PRD or mechanical protection remains if control and SIS fail?
- How is the node made safe for maintenance?
- Can operation continue while the node is absent?
- Are connected items rated for the same pressure/temperature, or is a class/design break protected?


# API 610 / ISO 13709 Centrifugal Pumps

Use this reference when a HAZOP, LOPA, P&ID review, or equipment-context extraction task involves centrifugal pumps in petroleum, petrochemical, or natural gas service. It converts API 610 / ISO 13709 pump expectations into practical data fields and review prompts.

## Source Traceability

- Source document: API Standard 610, 11th edition, September 2010, identical to ISO 13709:2009, for centrifugal pumps in petroleum, petrochemical, and natural gas industries.
- Use this as derived operational guidance only. Do not quote or reproduce API tables, figures, acceptance criteria, or vendor datasheet forms.
- The uploaded PDF text layer was not extractable as reliable words because of character mapping issues; this reference is intentionally conservative and based on the identified standard scope and common API 610 pump review practice.

## Applies To

- Process centrifugal pumps and their immediate P&ID context.
- Pump datasheets, operating envelopes, and equipment design context.
- Suction and discharge piping, valves, strainers, reducers, vents, drains, check valves, warm-up lines, and recycle lines.
- Minimum flow protection, automatic recirculation, and low-flow alarms or trips.
- Mechanical seals, seal support systems, seal leakage collection, cooling, quench, buffer or barrier systems, and related utilities.
- Drivers, couplings, lube oil, bearing monitoring, vibration monitoring, and package auxiliaries.
- Standby pump arrangements, auto-start logic, common headers, common utilities, and maintenance isolation.

## Does Not Provide

- Pump sizing, hydraulic calculation, or performance-curve generation.
- Exact NPSH margin, acceptance-test criteria, nozzle-load criteria, or vibration limits.
- Detailed API 682 seal-plan design. If seal-plan adequacy is important, request the seal plan, vendor drawing, and API 682 context.
- Credit as an IPL by itself. Protection credit still needs independence, effectiveness, reliability, management system, and proof-test evidence.

## Pump Context Schema

Capture pump context in this shape when extracting from a P&ID, datasheet, cause-and-effect chart, or operating procedure:

```yaml
source:
  documents: []
  drawing_numbers: []
  revision: null
  assumptions: []
  missing_information: []

pump:
  tag: null
  service: null
  duty: normal | startup | standby | emergency | intermittent | spare | unknown
  arrangement: single | parallel | series | duty_standby | unknown
  api_610_type: OH | BB | VS | unknown
  stages: null
  driver_type: electric_motor | steam_turbine | gas_turbine | engine | unknown
  speed_control: fixed_speed | vfd | turbine_governor | unknown

fluid_context:
  fluid_name: null
  phase: liquid | mixed | flashing | unknown
  hazardous_properties: []
  density: null
  viscosity: null
  vapor_pressure: null
  solids_or_fouling: null
  normal_temperature: null
  normal_pressure: null

operating_envelope:
  normal_flow: null
  rated_flow: null
  minimum_continuous_stable_flow: null
  thermal_minimum_flow: null
  maximum_allowable_flow_or_runout_limit: null
  normal_head: null
  rated_head: null
  shutoff_head_pressure: null
  preferred_operating_region: null
  allowable_operating_region: null
  npshr: null
  npsha: null
  npsh_margin_basis: null

design_envelope:
  casing_design_pressure: null
  casing_design_temperature: null
  mawp_or_pressure_limit: null
  hydrotest_pressure: null
  nozzle_rating: null
  material_class: null
  corrosion_erosion_allowance: null
  seal_chamber_limits: null

suction_system:
  upstream_source: null
  source_pressure_level: null
  suction_line_number: null
  suction_block_valve: null
  suction_strainer: null
  reducer_or_eccentric_reducer: null
  low_point_drain: null
  high_point_vent: null
  warmup_or_bypass_line: null
  npsh_risks: []

discharge_system:
  discharge_line_number: null
  check_valve: null
  discharge_block_valve: null
  downstream_control_valve: null
  downstream_destination: null
  relief_or_thermal_relief: null
  common_header: null
  reverse_flow_risks: []
  deadhead_risks: []

minimum_flow_recycle:
  required: true | false | unknown
  protection_type: manual_bypass | control_valve | automatic_recirculation_valve | restriction_orifice | trip_only | unknown
  flow_measurement: null
  recycle_destination: suction_vessel | source_vessel | pump_suction | cooler | flare_or_closed_system | unknown
  valve_fail_position: null
  credible_failure_modes: []

seal_system:
  seal_type: single | dual | tandem | cartridge | packed | unknown
  seal_plan: null
  flush_source: null
  buffer_or_barrier_fluid: null
  seal_pot_or_reservoir: null
  cooling_or_quench: null
  leakage_detection: null
  leakage_destination: null
  dry_run_or_loss_flush_risks: []

auxiliaries:
  lube_oil_system: null
  cooling_water: null
  seal_support_utilities: []
  instrument_air: null
  power_supply: null
  local_panel_or_package_controls: null

instrumentation_controls:
  pressure_indication: []
  flow_indication: []
  temperature_indication: []
  vibration_monitoring: []
  bearing_temperature_monitoring: []
  seal_leak_monitoring: []
  motor_current_or_power_monitoring: []
  speed_control_loop: null

protection:
  alarms: []
  trips: []
  interlocks: []
  permissives: []
  emergency_shutdown_actions: []
  safe_state: stopped | running | isolated | depressurized | unknown
  credited_safeguards: []

hazop_context:
  design_intent: null
  deviations: []
  causes: []
  consequences: []
  safeguards: []
  recommendations: []
```

## What To Extract First

Start with the fields below because they usually change the HAZOP result:

- Pump tag, service, normal duty, standby duty, and whether pumps are in parallel or series.
- Upstream source, downstream destination, suction pressure, discharge pressure, fluid vapor pressure, and normal operating temperature.
- Normal flow, rated flow, minimum continuous stable flow, thermal minimum flow, maximum operating or runout limit, and whether the P&ID shows a minimum-flow recycle path.
- NPSHA, NPSHR, NPSH margin basis, suction strainer details, and any line-up that can reduce suction head.
- Seal type, seal plan if available, flush source, cooling or quench, leakage destination, and leakage detection.
- Driver type, speed control, power supply, lube oil, cooling water, instrument air, and other common utilities.
- Alarms, trips, permissives, ESD actions, valve fail positions, and whether the safe state is pump stop, isolation, recycle-open, or another defined action.

## Operating Envelope

Treat the pump operating envelope as a system boundary, not only a vendor datasheet value.

- Separate normal flow, rated flow, minimum continuous stable flow, thermal minimum flow, and maximum allowable flow. These are not interchangeable.
- Low flow can cause internal recirculation, overheating, vibration, seal damage, or deadhead consequences.
- High flow or runout can overload the driver, reduce discharge pressure, increase NPSH demand, or destabilize downstream operation.
- Operation far from best efficiency can increase vibration, heat, bearing load, seal stress, and maintenance risk.
- A pump operating envelope is incomplete if the datasheet gives flow and head but not fluid vapor pressure, density, viscosity, NPSHA/NPSHR basis, or minimum-flow basis.

## Suction System Review

For each pump, trace the complete suction path from source to pump nozzle.

- Identify the source vessel or header, liquid level basis, suction pressure, line size, line class, suction block valve, strainer, reducer, vents, drains, and temporary start-up strainers.
- Flag any missing NPSHA/NPSHR comparison, especially for hot, flashing, near-boiling, high-vapor-pressure, or volatile fluids.
- A plugged suction strainer, closed suction valve, low upstream level, vapor breakout, wrong reducer orientation, or excessive pressure drop can create low suction pressure and cavitation.
- Vertical pumps need source level, submergence, vortex, and sump or can geometry context.
- Hot-service pumps may need warm-up or equalizing lines to avoid thermal shock, seizure, or casing distortion.

## Discharge System Review

Trace the full discharge path to the destination and pressure boundary.

- Identify discharge check valve, discharge block valve, control valve, downstream destination, common header, pressure indication, relief/thermal relief, and isolation logic.
- Check whether pump shutoff pressure plus suction pressure can exceed downstream equipment, piping, seal chamber, exchanger, filter, or hose limits.
- A failed or missing check valve can allow reverse flow, reverse rotation, backspin, or unexpected pressurization from a common header.
- A closed discharge valve, blocked downstream path, or failed control valve can cause deadhead. Deadhead can heat the liquid and damage seals even if pressure does not immediately exceed design.
- For parallel pumps, check whether one pump can drive reverse flow through another pump, and whether common suction/discharge headers create common-cause failures.

## Minimum Flow And Recycle

Minimum-flow protection is often the key HAZOP context for centrifugal pumps.

- Identify whether minimum flow is protected by an automatic recirculation valve, control valve, restriction orifice, manual bypass, low-flow trip, or procedural action.
- Capture the recycle destination. Recycle to the pump suction line can still heat the pump if there is no heat sink; recycle to the source vessel or another volume usually changes the heat-buildup scenario.
- Do not treat a manual bypass as a strong safeguard unless procedures, line-up verification, and operator response are credible for the scenario timing.
- Do not credit a low-flow alarm or trip as an IPL unless it is independent of the initiating cause and has suitable reliability, response time, and proof-test evidence.
- Flag a missing minimum-flow value, missing recycle destination, unclear valve fail position, or no shown flow measurement.

## Seal And Seal Support Review

Seal context is essential when the pumped fluid is flammable, toxic, hot, corrosive, volatile, or environmentally sensitive.

- Extract seal type, seal plan, seal flush source, seal pot or reservoir, buffer/barrier fluid, quench, cooling, drains, vents, and leakage destination.
- Identify whether seal leakage goes to atmosphere, closed drain, oily water, flare, containment, or detection system.
- Loss of seal flush, loss of cooling, dry running, reverse rotation, contaminated buffer fluid, or wrong valve line-up can create rapid seal failure.
- Dual seals or seal support packages need utility availability and alarm/trip context. A seal pot level or pressure alarm is not the same as an automatic trip.
- If the P&ID only says "mechanical seal" without plan or utility detail, mark the seal protection basis incomplete.

## Driver, Lube, And Utilities

Extract the driver and auxiliary systems because they often create common-cause failures.

- Driver: motor, turbine, engine, variable-speed drive, rated power, speed, start permissives, and trip path.
- Electrical: power source, MCC, VFD, motor overload, restart logic, auto-start standby logic, and emergency power if credited.
- Mechanical: coupling, coupling guard, baseplate, bearing type, bearing temperature monitoring, and vibration monitoring.
- Utilities: lube oil, cooling water, seal flush, buffer/barrier fluid, instrument air, nitrogen, steam, condensate, and package controls.
- For standby pumps, check whether standby readiness depends on the same suction source, discharge header, power source, cooling water, seal system, or logic solver.

## Instrumentation And Protection

Classify each signal as indication, alarm, control, permissive, trip, or ESD action.

- Typical pump signals include suction pressure, discharge pressure, flow, casing or bearing temperature, vibration, seal leakage, seal pot pressure/level, motor current, speed, and run status.
- Typical protective functions include low suction pressure trip, low flow trip, high discharge pressure trip, high vibration trip, high bearing temperature trip, motor overload trip, and ESD stop.
- Capture final elements: motor stop, turbine trip valve, suction/discharge isolation valves, recycle valve open, control valve position, and depressuring or drain action if any.
- A pump stop can be safe for some cases and unsafe for others. For example, stopping a cooling-water pump may worsen a high-temperature scenario.
- Verify whether the protection action creates a secondary hazard, such as blocked-in thermal expansion, reverse flow, or loss of circulation.

## HAZOP Deviations To Consider

Use these deviations when the node includes a centrifugal pump:

- No flow: stopped pump, loss of power, closed suction/discharge valve, tripped driver, failed coupling, no liquid source, vapor lock, blocked strainer.
- Low flow: plugged suction strainer, low upstream level, control valve closed, recycle blocked, wrong line-up, excessive downstream pressure, worn impeller.
- High flow: downstream valve failed open, low system resistance, runout, incorrect speed, parallel pump interaction, failed control loop.
- Reverse flow: failed check valve, common discharge header backflow, shutdown pump exposed to running pump discharge, reverse rotation.
- Low suction pressure or cavitation: low level, high temperature, high vapor pressure, excessive suction losses, flashing, blocked strainer, inadequate NPSH margin.
- High discharge pressure: blocked outlet, closed valve, downstream isolation, high static head, control valve failure, deadhead.
- High temperature: deadhead, low flow, blocked cooling, hot recycle, loss of seal flush, bearing failure, inadequate warm-up.
- Seal leak or rupture: loss of flush, dry running, high vibration, high temperature, wrong seal plan line-up, contaminated barrier fluid, overpressure.
- High vibration: cavitation, operation outside envelope, misalignment, bearing damage, two-phase flow, foundation/baseplate issue, impeller damage.
- Standby unavailable: maintenance isolation, common power loss, common suction issue, failed auto-start, wrong valve position, unavailable utilities.

## Safeguard Review Rules

- A check valve may prevent reverse flow, but it should not be credited as highly reliable without inspection, maintenance, and failure-mode context.
- A minimum-flow line is a safeguard only when it is open or automatic for the scenario being reviewed and has adequate capacity and destination.
- An alarm is not protection unless operator response time is credible before consequence escalation.
- A trip can be a safeguard, but LOPA/IPL credit needs independence from the initiating cause and proof of reliability.
- A standby pump is not a safeguard for scenarios caused by common suction loss, common utility loss, common control failure, or common downstream blockage.
- Relief devices for pump blocked-discharge or thermal expansion scenarios should be tied back to API 520/API 521 context where applicable.

## Missing Information To Flag

Flag these gaps explicitly in the output:

- Pump curve, rated point, shutoff pressure, NPSHR, or operating region not available.
- NPSHA basis missing or inconsistent with suction source level and pressure.
- Minimum continuous stable flow or thermal minimum flow not stated.
- Recycle line missing, manual-only, or destination unclear.
- Seal plan, seal support utilities, or leakage routing not shown.
- Check valve location or failure consequence unclear.
- Driver trip, restart, auto-start, and permissive logic not shown.
- Valve fail positions not shown for recycle, discharge control, suction isolation, or ESD valves.
- Standby pump readiness or common-cause dependencies not shown.
- Casing/nozzle design pressure and temperature not available for blocked-discharge or hot-service review.

## Output Rule

When using this reference, produce only the pump context needed for the task. Prefer short extracted fields, explicit assumptions, and HAZOP-relevant gaps over broad pump-design commentary.

# API 521 / ISO 23251 Pressure-Relieving and Depressuring Systems

Use this reference to extract practical pressure-relief, vapour-depressuring, flare, vent, and disposal-system context for HAZOP/LOPA and process-safety documentation. It is derived from API Standard 521 / ISO 23251 and focuses on what an agent should capture: credible overpressure or vacuum causes, protected equipment, relieving conditions, required relief-load basis, disposal path, back pressure, flare/vent hazards, depressuring intent, and whether HIPS/HIPPS or administrative controls have enough evidence to be considered.

This is a derived working guide. It does not reproduce API 521 tables, equations, example calculations, figures, or data sheets and does not replace API 520, API 521, API 537, API 2000, ASME BPVC, IEC 61511/ISA 84, project relief calculations, flare-network simulations, vendor data, jurisdictional requirements, or review by a qualified relief-system engineer.

## Source Traceability

- Source standard: `ANSI/API Standard 521`, fifth edition, January 2007, including June 2007 errata and May 2008 addendum; identical to `ISO 23251`.
- Scope, referenced standards, terms, and definitions: clauses 1-3.
- Causes and potentials for overpressure, protection philosophy, vacuum protection, minimum relief-system design content, and flare-header documentation: clause 4.
- Determination of individual relieving rates and scenario-specific guidance: clause 5.
- Selection of disposal systems, including atmospheric discharge, flaring, closed systems, and special fluid hazards: clause 6.
- Disposal-system design, flare headers, laterals, knockout drums, liquid seals, vent stacks, noise/radiation concerns, and flare gas recovery: clause 7.
- Fire-relief background: Annex A.
- Special system design considerations: Annex B.
- Flare stack sizing example material: Annex C.
- Typical details and sketches: Annex D.
- High Integrity Protection Systems (HIPS/HIPPS): Annex E.

## Applies To

- P&IDs, PFDs, relief summaries, PSV/PRV datasheets, rupture-disk datasheets, relief-load calculations, flare-network studies, depressuring studies, HIPS/HIPPS documents, cause-and-effect charts, operating procedures, and process-safety information.
- HAZOP/LOPA review of pressure vessels, columns, heat exchangers, reactors, pumps, compressors, fired heaters, separators, piping, blocked-in liquid sections, tanks/process vessels, flare systems, vent systems, and disposal systems.
- Extracting why a relief device exists, what it protects, which scenario controls, what discharge path is used, and what assumptions need verification.

## Does Not Provide

- Final relief sizing, relief area, or flare-stack design.
- Permission to omit a pressure-relief device based only on a summarized HIPS or administrative control.
- A substitute for project calculations, process simulation, dynamic analysis, fire modelling, dispersion/radiation/noise modelling, or jurisdictional acceptance.
- A universal list of all possible overpressure causes. API 521 emphasizes scenario-specific judgement.

## Key Terms For Extraction

| Term | Extraction use |
|---|---|
| `MAWP` | Basis for pressure-relief device setting for a vessel when established. Keep separate from design pressure. |
| `design pressure` | Mechanical design basis with coincident design temperature; not automatically equal to MAWP. |
| `operating pressure` | Normal pressure including normal variation. Do not use as relief limit. |
| `relieving conditions` | Inlet pressure and temperature at the relief device during the overpressure case. |
| `back pressure` | Outlet pressure on a relief device; split into superimposed and built-up where possible. |
| `blowdown/depressuring` | Reduction of pressure in plant/equipment, not the valve reseat pressure differential. |
| `closed disposal system` | Disposal system that contains pressure different from atmosphere, such as flare header. |
| `atmospheric discharge` | Direct release to atmosphere; requires dispersion, flammability, toxicity, noise, and exposure review. |
| `knockout drum` | Vessel in the disposal system used to remove/store liquids before vent/flare. |
| `HIPS/HIPPS` | Instrumented overpressure protection using sensors, logic solver, and final elements; requires SIL/availability, testing, MOC, and jurisdictional review. |

## Relief Scenario Schema

For each relief or depressuring case, extract:

```yaml
relief_scenario:
  source:
    document:
    page_or_sheet:
    revision:
    calculation_or_case_id:
  protected_item:
    tag:
    type:
    service:
    design_code:
    design_pressure:
    design_temperature:
    mawp:
    corrected_hydrotest_pressure:
    normal_operating_pressure:
    normal_operating_temperature:
  scenario:
    initiating_event:
    overpressure_cause:
    operating_mode:
    blocked_in_or_flowing:
    single_or_common_cause:
    simultaneous_cases_assumed:
    assumptions:
    excluded_cases:
  relieving_basis:
    required_relief_rate:
    controlling_phase:
    relieving_pressure:
    relieving_temperature:
    fluid_composition:
    fluid_properties:
    two_phase_or_flashing:
    reaction_or_runaway:
    fire_case:
    depressuring_case:
  device:
    tag:
    type:
    set_pressure_or_burst_pressure:
    rated_capacity:
    cold_differential_test_pressure:
    inlet_pressure_drop:
    superimposed_back_pressure:
    built_up_back_pressure:
    back_pressure_limit_or_correction:
    discharge_to:
  disposal:
    closed_or_atmospheric:
    header_or_lateral:
    flare_or_vent:
    knockout_drum:
    liquid_seal:
    treatment_or_recovery:
    radiation_dispersion_noise_review:
    environmental_or_toxic_review:
  safeguards:
    bpcs_credit:
    alarm_operator_action:
    sis_or_hips_credit:
    check_valve_credit:
    administrative_control:
    mechanical_relief:
  hazop_use:
    credible_deviation:
    consequence:
    safeguards_to_review:
    missing_information:
```

## Overpressure Scenario Checklist

Screen each node for these credible causes. Preserve the source case name if the project uses a different label.

- Closed outlet, blocked discharge, or blocked outlet on a vessel, pump, compressor, column, exchanger, or piping segment.
- Inadvertent valve closure or opening, including remotely operated valves and control valves.
- Check-valve leakage or latent check-valve failure causing reverse flow from a higher-pressure system to a lower-pressure system.
- Utility failure: electric power, cooling water/medium, instrument air, steam, heating medium, fuel, inert gas, refrigeration, vacuum, quench, reflux, or boiler feed.
- Electrical or mechanical failure of equipment that provides cooling, condensation, pumping, compression, or control.
- Loss of fans on air coolers or cooling towers.
- Loss of heat in linked fractionation systems where light ends move downstream.
- Accumulation of non-condensables.
- Entrance of volatile material into a hot system, including water into hot oil or light hydrocarbons into hot oil.
- Failure of process stream automatic controls, including fail-open/fail-closed/fail-in-place final elements.
- Abnormal heat input, including reboiler/heater control failure or blocked heat removal.
- Heat exchanger tube rupture or inter-stream leakage from high-pressure to low-pressure side.
- Transient pressure surges such as water hammer or steam hammer.
- External fire and heat input to wetted/unwetted surfaces.
- Process change, chemical reaction, decomposition, polymerization, runaway reaction, or reactive mixing in relief/disposal system.
- Thermal expansion of blocked-in liquids.
- Vacuum caused by pump-out, condensation, cooling, steam-out, draining, siphoning, or compressor/pump suction.
- Overfilling, especially where liquid carryover can affect vent, flare, knockout drum, or atmospheric release.

For HAZOP, treat this checklist as prompts, not a complete list. Any site-specific hazard that can create pressure, vacuum, temperature, or inventory imbalance should be considered.

## Relief Basis Extraction Rules

- Keep the initiating event separate from intermediate consequences. Example structure: `loss of power -> loss of cooling -> condenser duty lost -> column pressure rise -> relief`.
- Separate required relieving rate from rated device capacity. Both may matter for different parts of the disposal system.
- Keep normal operating pressure, design pressure, MAWP, set pressure, relieving pressure, hydrotest pressure, and corrected hydrotest pressure separate.
- Record whether favourable response of conventional control instrumentation was assumed. Do not assume it for individual equipment relief sizing unless the source explicitly justifies it.
- Record whether manual or operator action is time-dependent. Flag it if used as the only protection against overpressure.
- Record whether check valves, administrative controls, or HIPS/HIPPS are credited and what inspection, testing, or reliability basis is given.
- Record whether the case is steady-state, dynamic, transient, fire, two-phase, reactive, or depressuring. Do not collapse them into one generic "PSV case".
- If the source says a scenario is excluded or reduced, capture the exact basis and the risk-analysis evidence.

## Relief-System Design Content To Extract

For a complete pressure-relief basis package, look for:

- Equipment design and operating data.
- Applicable pressure-design code and jurisdictional constraints.
- PFD/P&ID references and revision numbers.
- Heat and material balance basis.
- All considered overpressure causes and controlling scenario.
- Operating and relieving fluid composition, phase, hazards, pressure, temperature, and properties.
- Device type and configuration: pressure-relief valve, rupture disk, pilot-operated valve, balanced bellows valve, buckling-pin device, combinations, or other device.
- Set pressure, burst pressure, manufacturing range, cold differential test pressure, and rated capacity.
- Required relief area/capacity basis and correction factors from the applicable code/API 520 calculation package.
- Inlet-line pressure drop and outlet/back-pressure basis.
- Discharge requirement: flare, vent, closed system, recovery, treatment, atmospheric release, bellows/pilot vent, or safe location.
- Relief installation details: drainage, heat tracing, pipe stress, reaction forces, drains/bleeds, maintenance access, and bonnet/pilot vent routing.
- Vacuum-protection criteria where applicable.

If these items are missing from a relief summary, mark them as `missing`; do not infer from PSV tag alone.

## Fire Relief And Depressuring Context

For fire exposure, extract:

```yaml
fire_relief_context:
  fire_zone_or_source:
  equipment_exposed:
  wetted_area_basis:
  insulation_or_fireproofing_credit:
  liquid_inventory:
  vapour_generation_basis:
  isolation_assumption:
  alternate_relief_paths:
  metal_temperature_or_stress_rupture_concern:
  passive_fire_protection:
  active_depressuring:
  flare_capacity_interaction:
```

Rules:

- Do not assume lines remain open during fire unless the source justifies it. Operators or emergency shutdown logic can isolate equipment.
- If insulation/fireproofing is credited, record whether removal or damage would invalidate the relief basis.
- Fire can threaten equipment by metal temperature and stress rupture even if pressure does not exceed maximum allowable accumulation.

For depressuring, extract:

```yaml
depressuring_context:
  protected_equipment:
  purpose:
    fire_stress_reduction:
    leak_consequence_reduction:
    inventory_reduction:
    emergency_shutdown:
  initiation:
    manual:
    automatic:
    remote:
  blowdown_valves:
  target_pressure:
  target_time:
  low_temperature_limit:
  hydrate_or_solid_formation:
  valve_fail_position:
  actuator_signal_fire_survivability:
  simultaneous_depressuring_cases:
  flare_or_vent_capacity_basis:
```

Depressuring can chill light hydrocarbons and create low-temperature embrittlement risk. Capture minimum metal temperature, material limits, hydrate/solid formation, and downstream disposal capacity whenever present.

## Heat Exchanger Tube Rupture

Extract tube-rupture context as its own scenario:

```yaml
tube_rupture_context:
  exchanger_tag:
  high_pressure_side:
  low_pressure_side:
  pressure_ratio_or_delta:
  connected_equipment_protected:
  full_bore_or_dynamic_basis:
  phase_change_or_flashing:
  reactive_mixing_concern:
  relief_device_location:
  transient_overpressure_concern:
  low_pressure_side_design_basis:
  inspection_or_mechanical_layer:
```

Quality flags:

- Relief device is remote from a liquid-full low-pressure side.
- Reactive mixing between shell-side and tube-side fluids is not evaluated.
- Connected upstream/downstream low-pressure equipment and piping are ignored.
- Tube rupture is treated as simple steady-state flow where a dynamic/transient analysis is needed.

## Thermal Expansion And Vacuum

Thermal expansion context:

- Identify blocked-in liquid sections in piping, exchangers, pumps, filters, sample systems, and equipment jackets.
- Capture heat source: solar, ambient warmup, heat tracing, exchanger duty, steam, fire, or adjacent hot equipment.
- Record whether the section can remain liquid-full or has an adequate non-condensable vapour pocket.
- Record procedure/permit reliance for draining after isolation.
- Flag flashing or solid-forming fluids through the thermal relief device.

Vacuum context:

- Identify vacuum causes: pump-out, draining, siphoning, condensation, cooling, steam-out, compressor suction, blocked inflow, or phase change.
- Capture whether the equipment is designed for full vacuum or needs vacuum relief/repressuring.
- Record the gas admitted: air, nitrogen, fuel gas, or other gas, and any flammability/reactivity/asphyxiation concern.
- Flag reliance on procedure alone for maintenance draining, steaming, or hydrotesting where mechanical vacuum protection may be needed.

## Disposal System And Flare Context

For flare-header and disposal-system studies, extract:

```yaml
disposal_system_context:
  system_id:
  relief_sources:
  design_scenarios:
    - initiating_event:
      simultaneous_sources:
      required_rates:
      rated_capacities:
      fluid_properties:
      pressure_profile:
      controlling_component:
  laterals:
  headers:
  allowable_back_pressure:
  calculated_back_pressure:
  knockout_drums:
  liquid_handling:
  liquid_seals:
  flare_or_vent_stack:
  purge_or_assist_gas:
  flame_arresting_or_flashback_controls:
  radiation:
  dispersion:
  noise:
  smokeless_or_environmental_requirement:
  flare_gas_recovery:
```

Rules:

- A disposal-system design basis is not necessarily the largest mass rate; fluid molecular weight, temperature, phase, pressure drop, and component-specific duties can control.
- Evaluate individual initiating events and resultant effects. Do not combine unrelated contingencies unless a common cause or project basis requires it.
- Partial utility failure can govern over total utility failure; capture bus, header, train, or utility-zone assumptions.
- For relief headers, record back pressure at each source for each analyzed case.
- For atmospheric discharge, record flammability, toxicity, mist/spray, autoignition, radiation, noise, pollution, and personnel exposure basis.
- For flare gas recovery, emergency flow path to flare must remain available; the recovery system should not become the main emergency path.
- For knockout drums and liquid seals, capture high-level alarms, low/minimum level requirements, field verification, dirty-service maintenance, freeze/solidification risk, carryover, and seal-water management.

## HIPS/HIPPS As Overpressure Protection

Treat HIPS/HIPPS cautiously. Extract:

```yaml
hips_context:
  protected_equipment:
  overpressure_scenario_removed_or_reduced:
  sensors:
  logic_solver:
  final_elements:
  action:
  safe_state:
  sil_or_availability_target:
  demand_rate_basis:
  spurious_trip_consequence:
  proof_test_interval:
  reliability_calculation:
  independence_from_bpcs:
  common_cause_failure_controls:
  maintenance_testing_inspection:
  moc:
  jurisdictional_acceptance:
  backup_relief_device:
```

Rules:

- HIPS can be used to remove the source of overpressure or reduce a contingency frequency, but only with rigorous design, testing, inspection, MOC, and authority acceptance where required.
- If no owner risk tolerance is given for omitting a relief device, flag that local regulations and a high integrity basis are required.
- Do not credit HIPS/HIPPS from a C&E line alone. Require SRS, SIL/availability target, proof-test interval, reliability calculation, independence, and lifecycle evidence.
- A HIPS used together with a relief device should be recorded as layered protection, with the relief device role clear.

## HAZOP And LOPA Use

Use API 521 context to strengthen worksheets:

- Deviations: high pressure, low pressure/vacuum, high temperature, low temperature, no flow, reverse flow, blocked outlet, more feed, no cooling, no reflux, no heat removal, wrong valve position, tube rupture, fire exposure, thermal expansion, overfill, reaction/runaway, and relief/disposal blocked.
- Causes: valve closure/opening, utility loss, control failure, check-valve leakage, pump/compressor trip, fan failure, exchanger failure, tube rupture, water/volatile entry, fire, blocked-in liquid heating, operator isolation, SIS failure, or flare path impairment.
- Consequences: vessel/piping rupture, relief to flare/atmosphere, toxic/flammable release, vapour cloud, radiation, noise exposure, liquid carryover, flare-header overpressure, back-pressure reducing PSV capacity, low-temperature brittle failure, or vacuum collapse.
- Safeguards: PRV/PSV, rupture disk, thermal relief valve, depressuring valve, HIPS/HIPPS, vacuum relief, check valve, alarm/operator action, BPCS control, SIS, flare, knockout drum, liquid seal, fireproofing, insulation, emergency response, and procedure.
- Recommendations: add missing relief-case study, verify PSV sizing basis, add thermal relief, evaluate tube rupture dynamically, check back pressure, update flare model, verify disposal path, define HIPS SRS, add bypass/MOC controls, validate depressuring low-temperature limits, or improve knockout/liquid-seal monitoring.

## Missing Information To Flag

- Protected equipment, MAWP/design pressure/design temperature, or pressure-design code missing.
- Relief-device tag exists on P&ID but no scenario, set pressure, discharge destination, or protected item is identified.
- Controlling overpressure case not stated.
- Required relief rate, relieving pressure/temperature, phase, composition, or fluid properties missing.
- Two-phase, flashing, reactive, or runaway behavior not addressed where credible.
- Utility failure analysis does not identify affected equipment or cascade effects.
- Fire case credits open paths, insulation, or operator action without basis.
- Tube rupture ignores connected low-pressure equipment/piping or relief-device response/location.
- Thermal relief omitted from blocked-in liquid section without a documented basis.
- Vacuum protection missing for equipment vulnerable to pump-out, condensation, steam-out, draining, or cooling.
- Disposal-system design lacks flare-header pressure profile, back-pressure basis, or simultaneous-source assumptions.
- Atmospheric vent lacks dispersion, flammability, toxicity, mist/spray, noise, radiation, and exposure review.
- Knockout drum, liquid seal, or flare gas recovery controls are shown but no level, freeze, carryover, or emergency-path basis is given.
- HIPS/HIPPS is credited without SRS, SIL/availability, proof-test interval, reliability calculation, lifecycle controls, or jurisdictional review.

## Output Rule

When using this reference, output HAZOP-ready relief context. The answer should identify:

- What item is protected?
- What overpressure/vacuum scenario is credible?
- What normal, design, MAWP, set, and relieving pressures apply?
- What relief/depressuring rate basis is used?
- Where does the discharge go?
- What back-pressure, liquid, flare, vent, radiation, dispersion, noise, or environmental issue is relevant?
- Which safeguards are mechanical, instrumented, procedural, or disposal-system safeguards?
- What evidence is missing before the relief or HIPS claim can be accepted?

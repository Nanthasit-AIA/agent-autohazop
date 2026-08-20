# API 520 Part II Pressure-Relief Device Installation

Use this reference to extract practical installation context for pressure-relief devices (PRDs) from P&IDs, isometrics, relief-device datasheets, inspection records, maintenance records, and relief-system design packages. It is derived from API Standard 520 Part II and focuses on what an agent should capture: PRD location, inlet piping, outlet/discharge piping, stability risks, isolation valves, spare relief capacity, rupture-disk combinations, bonnet/pilot vents, drains, handling, installation, inspection, and maintenance.

This is a derived working guide. It does not reproduce API 520 figures, tables, formulae, annex details, or installation sketches. It does not replace API 520 Part I sizing/selection, API 521 relief-load and disposal-system design, API 576 inspection/repair practices, manufacturer installation instructions, project specifications, jurisdictional requirements, or review by a qualified relief-system engineer.

## Source Traceability

- Source standard: `API Standard 520`, `Sizing, Selection, and Installation of Pressure-relieving Devices`, `Part II - Installation`, sixth edition, March 2015.
- Scope and terminology: clauses 1-3.
- PRD location, proximity to protected equipment, pressure fluctuations, vibration, environment, free drainage, and maintainability: clause 4.
- Inlet piping requirements, minimum diameter, layout, process laterals, inlet pressure loss, static loads, and reaction forces: clause 5.
- Discharge piping, safe disposal, back pressure, pilot-operated PRV concerns, and auto-refrigeration: clause 6.
- PRV stability, cycling, flutter, chatter, inlet losses, built-up back pressure, acoustic interaction, retrograde condensation, trim selection, thermal relief valves, and remote sensing: clause 7 and Annex C.
- Isolation valves, spare relieving capacity, three-way changeover valves, flare-header block valves, and administrative controls: clause 8.
- Rupture disk installations, PRV/RD combinations, and rupture disks in series: clause 9 and Annex A.
- Bonnet and pilot vent piping: clause 10.
- Drain piping: clause 11.
- Pre-installation handling, storage, cleaning, hydrotest protection, installation, inspection, maintenance, lifting levers, heat tracing, and insulation: clauses 12-13 and Annexes A-B.

## Applies To

- PRVs, safety relief valves, relief valves, rupture disk devices, and pin-actuated non-reclosing PRDs.
- Equipment with MAWP of 15 psig or greater when API 520 Part II is the applicable installation reference.
- Gas, vapour, steam, two-phase, and incompressible-liquid service.
- HAZOP/LOPA review where the question is whether the installed relief path can actually work as intended.

## Does Not Provide

- Relief-load determination or overpressure scenario selection.
- PRV or rupture-disk sizing calculations.
- Final disposal-system design, flare radiation/noise/dispersion modelling, or flare-network simulation.
- Acceptance of unusual installations without manufacturer/project engineering review.
- Proof that a relief device is an IPL if installation, maintenance, and inspection evidence is missing.

## PRD Installation Context Schema

When reading a P&ID, isometric, relief datasheet, or inspection record, extract:

```yaml
prd_installation_context:
  source:
    document:
    page_or_sheet:
    revision:
  protected_item:
    tag:
    type:
    service:
    mawp_or_design_pressure:
    design_temperature:
  device:
    tag:
    device_type:
    service_phase:
    set_pressure_or_burst_pressure:
    rated_capacity:
    required_relief_rate:
    trim_or_certification:
    discharge_destination:
  location:
    mounted_on:
    distance_from_protected_equipment:
    pressure_fluctuation_sources:
    vibration_sources:
    operating_environment:
    access_for_maintenance:
  inlet_piping:
    nominal_size:
    common_inlet_area:
    inlet_loss_basis:
    static_liquid_head:
    process_laterals:
    free_draining:
    pockets_or_deadlegs:
    inlet_isolation_valve:
    rupture_disk_upstream:
    remote_sensing_line:
    supports_and_loads:
  discharge_piping:
    open_or_closed:
    nominal_size:
    self_draining:
    low_point_drains:
    built_up_back_pressure:
    superimposed_back_pressure:
    auto_refrigeration_min_temperature:
    reaction_force_support:
    disposal_hazard:
  stability:
    cycling_risk:
    flutter_risk:
    chatter_risk:
    inlet_loss_concern:
    back_pressure_concern:
    acoustic_interaction:
    retrograde_condensation:
    oversized_or_trim_mismatch:
  isolation_and_spare_capacity:
    inlet_isolation:
    outlet_isolation:
    lock_or_car_seal:
    required_position:
    mechanical_interlock:
    administrative_control:
    spare_relief_device:
    changeover_valve:
    bleed_valve:
  rupture_disk:
    location:
    nonfragmenting_required:
    holder_compatibility:
    flow_direction:
    interspace_vent_or_telltale:
    pressure_gauge_or_alarm:
    torque_or_installation_record:
  bonnet_pilot_vents:
    valve_type:
    vent_destination:
    back_pressure_free:
    free_draining:
    bug_screen_or_weather_protection:
    leak_detection:
    hazardous_fluid_handling:
  maintenance:
    pre_install_cleaning:
    hydrotest_isolation:
    set_pressure_test:
    inspection_record:
    chatter_history:
    heat_tracing:
    insulation:
  hazop_use:
    credible_installation_failures:
    consequences:
    safeguards_to_review:
    missing_information:
```

## PRD Location Checks

Extract and flag:

- Whether the PRD is close enough to the protected equipment to avoid excessive inlet loss and delayed sensing.
- Nearby pressure-fluctuation sources: control valves, reducers, short-radius elbows, pump/compressor discharge, or other turbulent/unstable flow sources.
- Whether the PRD branch is smooth and well-rounded where it joins a flowing process line.
- Vibration sources that can cause PRV leakage, premature opening, fatigue, rupture disk burst-pressure shift, or shortened disk life.
- Whether the PRD is placed in a cleaner/cooler process region where feasible.
- Whether inlet and outlet piping are free-draining away from the PRD.
- Whether the device is accessible for inspection, removal, testing, lifting lever checks, and maintenance.

Quality flags:

- PRD at the end of a long normally stagnant horizontal inlet pipe.
- PRD near a pressure-pulsation or unstable-flow source with no analysis.
- Device inaccessible for maintenance or blocked by structure.
- Vibration history, leakage history, or chatter history not reviewed.

## Inlet Piping Extraction

For every PRV inlet path, capture:

- Inlet pipe and fitting nominal size versus PRV inlet connection.
- For multiple PRVs on a common inlet, common inlet flow area versus combined PRV inlet areas.
- Nonrecoverable inlet pressure loss basis, including entrance loss, pipe/fitting friction, stop/changeover valves, and any rupture disk device.
- Whether the commonly used inlet pressure loss target is met or whether a documented engineering analysis justifies a higher value.
- Static liquid head between protected equipment and PRV, and whether the PRV set pressure was adjusted if needed.
- Whether a common PRV protects multiple interconnected equipment items and whether pressure profile/turndown effects are considered.
- Whether a PRV is mounted on a flowing process line and includes both the normally nonflowing PRV inlet loss and incremental process-line pressure loss during relief.
- Whether process laterals connect into PRV inlet piping and whether simultaneous flow has been analyzed.
- Whether the inlet line can collect liquid, rust, scale, solids, wax, polymer, hydrate, or other foreign matter.

Rules:

- Do not infer inlet pressure loss from line size alone. Require calculation, datasheet, isometric, or relief package evidence.
- The 3 percent set-pressure criterion is a screening rule, not a complete stability proof.
- If an installation with higher inlet loss is accepted, the engineering analysis must be documented.
- Engineering analysis should not be used to accept an installation that has already experienced chatter without further review.

## Discharge Piping Extraction

For every PRD discharge path, capture:

- Open atmospheric discharge or closed discharge system.
- Discharge destination: vent stack, flare header, closed drain, recovery/treatment system, safe location, or local discharge.
- Built-up and superimposed back pressure basis.
- Whether the discharge system is self-draining or has low-point drains.
- Whether rainwater, condensate, process liquid, solids, or corrosive fluids can accumulate downstream.
- Whether discharge piping is independently supported, aligned, and flexible enough to avoid transferring loads to the PRD.
- Whether reaction forces for open discharge or sudden expansions in closed systems were considered.
- Whether auto-refrigeration/Joule-Thomson cooling can make the outlet/discharge piping brittle.
- Whether two-phase or liquid discharge to atmosphere creates unacceptable hazard.

Quality flags:

- Outlet piping drains toward the PRD or has pockets.
- Discharge piping supported by the PRD.
- Back pressure not checked for the selected valve type.
- Pilot-operated PRV connected to a common discharge header without reverse-flow/backpressure review.
- Low-temperature discharge case not compared with discharge-piping material limits.

## PRV Stability

Classify instability concerns:

| Phenomenon | Extraction cue |
|---|---|
| `cycling` | Low-frequency open/close behavior, often when required relief rate is small compared with valve capacity. |
| `flutter` | Rapid partial motion of the disk without full closing. |
| `chatter` | Rapid opening/closing with seat contact; can damage valve and piping. |

Potential causes to flag:

- Excessive inlet pressure loss relative to blowdown and overpressure.
- Excessive built-up back pressure for the valve type.
- Oversized PRV or relief capacity poorly matched to required rate.
- Acoustic interaction between PRV motion and inlet piping.
- Retrograde condensation or supercritical-to-two-phase transition near the inlet.
- Vapor-certified trim used for liquid relief, or trim not suited to all credible relief scenarios.
- Full-bore PRV with inlet line that makes pressure loss difficult to control.
- Long inlet line, many fittings, sharp entry, or small branch connection.

Possible mitigation context to look for:

- Larger/shorter inlet piping.
- Fewer or lower-loss fittings.
- Rounded inlet entry.
- Multiple smaller PRVs with staggered settings.
- Restricted-lift PRV or different PRV type.
- Pilot-operated PRV with remote sensing where suitable.
- Manufacturer review of trim, blowdown, modulating behavior, and installation.

## Thermal Relief Valves

Treat thermal relief valves separately:

- For simple liquid hydraulic expansion due to ambient/solar heating, inlet and outlet losses often do not control because required flow can be far below rated capacity.
- For long pipelines, large liquid-full vessels, process heating, refrigerated liquids, LPG, LNG, or cases where ambient heating can lead to vaporization, inlet/outlet pressure drop can matter.
- Do not misclassify vaporization overpressure as simple liquid thermal expansion.
- Capture whether the discharge destination can handle flashing, cold liquid, solids, or two-phase flow.

## Isolation Valves And Spare Relief Capacity

Extract:

```yaml
isolation_context:
  inlet_valve:
    type:
    full_area:
    locked_or_car_sealed:
    normal_position:
    bleed_for_depressuring:
  outlet_valve:
    type:
    flow_area:
    locked_or_car_sealed:
    normal_position:
    back_pressure_effect:
  spare_capacity:
    installed_spare:
    stored_spare:
    capacity_available_during_maintenance:
    mechanical_interlock:
    administrative_control:
    changeover_valve:
    active_device_indication:
```

Rules:

- Isolation valves must not compromise required relief capacity.
- Check valves should not be installed in PRD inlet or outlet lines.
- Butterfly or globe valves are normally poor PRD isolation choices; any use needs specific engineering basis.
- Isolation valves need locking/car-sealing in the required position and periodic position verification.
- Spare relief arrangements need mechanical interlocks or administrative controls so the protected equipment is never left without required capacity.
- Changeover valves should prevent both PRDs from being isolated during switching and should clearly indicate the active device.
- A bleed between an isolated PRD and its inlet isolation valve is needed for safe depressuring before maintenance.
- Keep a controlled list of relief-system isolation valves, required positions, and reasons for locks/seals.

## Rupture Disk Installation

Extract:

- Whether the rupture disk is the sole PRD, upstream of a PRV, downstream of a PRV, or in series with another disk.
- Disk type and whether nonfragmenting design is required upstream of a PRV.
- Holder compatibility, flange rating, flow direction, tag, gasket, bolting, torque pattern, and manufacturer instructions.
- Whether the space between rupture disk and PRV is vented or provided with a suitable telltale indicator.
- Whether series rupture disks have an interspace vent, pressure gauge, trycock, or suitable telltale to prevent trapped pressure.
- Whether a pressure gauge alone is backed by administrative controls or alarms.
- Whether damaged/dented disks, dull knife blades, reused disks, or incompatible holders are present.
- Whether personnel are trained and protected from hazardous contamination during removal.

Quality flags:

- Captive pressure between disk and PRV or between series disks.
- Fragmenting disk installed upstream of PRV.
- Flow-direction arrows not visible or contradicted by installation.
- Disk reused after clamping force is released without manufacturer basis.
- Disk/holder style mismatch.

## Bonnet And Pilot Vent Piping

For balanced bellows, balanced piston, and pilot-operated valves, extract:

- Bonnet/pilot vent destination: local atmosphere, safe remote location, discharge piping, or separate vent system.
- Whether the vent must remain free of back pressure.
- Whether the vent line is free-draining away from the bonnet and has no pockets.
- Weather protection or bug screen for nonhazardous vapour vents.
- Hazardous vapour/liquid routing to a safe location.
- Flashing liquid handling, such as separation pot or safe drain/vent arrangement.
- Test port or inspection method for bellows leakage or plugged vent line.
- Whether insulation covers any discharge or vent port.

Flags:

- Plugged/open bonnet vent where venting is required.
- Hazardous bonnet/pilot vent routed to personnel area.
- Remote vent line pocketed, rainwater-prone, or backpressure-prone.
- Pilot vent backpressure not considered unless balanced design is confirmed.

## Drain Piping

Extract:

- Whether closed discharge piping self-drains to a liquid disposal point.
- Whether non-self-draining discharge piping has drain piping, body drain, low-point drain, or weep hole.
- Where drain/weep discharge goes relative to personnel, structural steel, hot surfaces, drains, and operating areas.
- Whether drain piping can plug, freeze, corrode, accumulate liquids, or create slug flow.
- Whether flammable, toxic, or corrosive drains are routed to a safe location.
- Whether drain piping has purge or heat tracing and whether tracing reliability is maintained.

Rules:

- Drain piping is part of the discharge system and must not impair PRD performance.
- Conventional PRVs and rupture disks are differential-pressure devices; downstream liquid accumulation can change activation behavior.

## Pre-Installation, Inspection, And Maintenance

Extract:

- Storage: indoor/clean storage, flange protection, shock avoidance, rupture disks kept in shipping container.
- Pre-install cleaning: inlet/outlet flanges clean, vessel/nozzle/piping cleaned of weld beads, scale, and foreign objects.
- Hydrotest/pneumatic-test protection: PRDs removed or isolated, with safeguards against pressure leaking into PRDs.
- Mounting: PRVs and rupture pin valves vertical upright unless manufacturer approves otherwise; rupture disks may be vertical or horizontal if properly supported and aligned.
- Gaskets and bolting: correct size, service suitability, no intrusion into flow path, manufacturer torque for rupture disk devices.
- Set-pressure testing before installation.
- Inspection/maintenance record review for chatter, leakage, damage, corrosion, plugging, or service problems.
- Lifting lever or pilot test provisions where required.
- Heat tracing and insulation on inlet, outlet, and pilot sensing lines where viscosity, corrosion on cooling, solidification, or plugging is credible.

Quality flags:

- PRD installed after construction without line cleaning.
- Evidence of chatter but no PRV system design review.
- PRV mounted non-vertical without manufacturer approval.
- Heat tracing absent or unreliable for viscous/solidifying/corrosive-on-cooling service.
- Vent ports or drains covered by insulation.

## HAZOP And LOPA Use

Use API 520 Part II context to strengthen worksheets:

- Deviations: relief path blocked, relief path restricted, high inlet pressure loss, high back pressure, PRV chatter, PRV leaks, PRV opens late, rupture disk fails to burst, rupture disk bursts early, discharge liquid accumulation, pilot sensing blocked, bonnet vent blocked, drain plugged, isolation valve closed, wrong spare PRD active, wrong trim, wrong mounting, low-temperature brittle failure in discharge.
- Causes: wrong valve position, missing car seal, poor changeover procedure, process lateral on PRV inlet, inlet deadleg fouling, solids/rust/scale, vibration, pressure pulsation, common discharge header backpressure, rainwater in vent stack, plugged drain, blocked pilot sensing line, wrong rupture disk orientation, wrong gasket/torque, incompatible disk/holder, poor storage/handling, heat tracing failure.
- Consequences: loss of overpressure protection, loss of containment, PRV damage, repeated leakage, relief to unsafe location, liquid spray, toxic/flammable exposure, flare/header upset, equipment overpressure, or unsafe maintenance.
- Safeguards: properly sized inlet/discharge piping, documented inlet loss analysis, backpressure check, free-draining layout, independent support, car-sealed isolation valves, mechanical interlock, bypass/spare procedure, rupture disk telltale, bonnet vent to safe location, drains to safe location, inspection/maintenance program, set-pressure test, line cleaning, and heat tracing.
- Recommendations: verify inlet loss, remove inlet lateral, shorten/enlarge inlet line, add drains, reroute bonnet vent, add telltale indicator, lock/car-seal isolation valves, add mechanical interlock, update isolation valve list, review chatter history, confirm trim, add support/reaction-force analysis, or update inspection/maintenance procedure.

## Missing Information To Flag

- PRD tag exists but protected equipment, set pressure, discharge destination, or device type is missing.
- Inlet pipe size, inlet pressure loss basis, or common inlet area not shown.
- Process laterals connect to PRV inlet without simultaneous-flow analysis.
- Discharge piping/backpressure basis absent.
- Closed discharge path has pockets or no drain basis.
- Atmospheric discharge lacks safe disposal review.
- Reaction forces/supports not shown for open discharge or sudden expansion.
- Isolation valves shown without lock/car seal, required position, bleed, interlock, or administrative control.
- Spare PRD/changeover arrangement does not clearly maintain 100 percent required relieving capacity.
- Rupture disk interspace has no vent/telltale indicator.
- Bonnet/pilot vent route not shown or can see back pressure.
- Heat tracing/insulation missing where process can plug, solidify, or corrode on cooling.
- Inspection records show chatter, leakage, or damage without design review.

## Output Rule

When using this reference, output installation-ready relief context. The answer should identify:

- Which PRD protects which equipment?
- Whether the inlet path, outlet path, drains, vents, and isolation valves support proper device operation.
- What stability risks are visible.
- What installation evidence is missing from the P&ID/isometric/datasheet.
- What should be reviewed before the PRD can be treated as a reliable safeguard in HAZOP/LOPA.

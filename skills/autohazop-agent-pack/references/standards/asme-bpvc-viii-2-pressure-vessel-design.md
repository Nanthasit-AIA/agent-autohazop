# ASME BPVC Section VIII Division 2 Pressure Vessel Design

Use this reference when extracting pressure-vessel mechanical design envelope and process-safety context from vessel datasheets, nameplates, Manufacturer's Data Reports, User's Design Specifications, Manufacturer's Design Reports, P&IDs, relief summaries, inspection records, or HAZOP/LOPA worksheets.

This is a derived working guide. It does not reproduce ASME BPVC formulas, stress tables, material tables, figures, fatigue curves, examination tables, pressure-test formulas, or certification text. It does not replace ASME BPVC Section VIII Division 2, ASME Section II, ASME Section V, ASME Section IX, ASME Section XIII, jurisdictional rules, owner specifications, vendor calculations, or review by a qualified pressure-vessel engineer.

## Source Traceability

- Source code: ASME BPVC.VIII.2-2023, Section VIII, Division 2, "Alternative Rules", Rules for Construction of Pressure Vessels, 2023 Edition, issued July 1, 2023.
- Part 1 covers general requirements, scope, geometric scope, exclusions, units, tolerances, and overpressure protection interface.
- Part 2 covers responsibilities and duties, including user responsibilities, User's Design Specification, Manufacturer's Design Report, Manufacturer's Data Report, construction records, quality control, inspection, and stamping.
- Part 3 covers material requirements, permitted materials, traceability, toughness, allowable stresses, strength parameters, physical properties, fatigue curves, and low-temperature design values.
- Part 4 covers design-by-rule requirements for shells, heads, external pressure, openings/nozzles, flanges, quick-opening closures, jackets, supports, heat exchangers, bellows, expansion joints, and related vessel components.
- Part 5 covers design-by-analysis requirements, including loading conditions, protection against plastic collapse, local failure, buckling, cyclic loading, ratcheting, and fatigue assessment.
- Part 6 covers fabrication requirements, welding, forming, heat treatment, clad/overlay/lining, forged fabrication, layered vessels, expansion joints, and PMI practice.
- Part 7 covers inspection and examination requirements, NDE responsibilities, examination groups, weld examination, cyclic-service supplemental examination, leak testing, and acoustic emission.
- Part 8 covers pressure testing requirements, pressure-test method selection, preparation, test fluid, test procedure, acceptance, alternative pressure testing, leak tightness testing, and documentation.
- Part 9 covers pressure-vessel overpressure protection, responsibilities, pressure-relieving requirements, overpressure limits, permitted methods, pressure settings, performance, and installation.

## Applies To

- Pressure vessels specified or stamped to ASME Section VIII Division 2.
- Vessels where HAZOP needs design-envelope context: reactors, drums, separators, columns, filters, heat exchangers, shell-and-tube exchangers, jackets, autoclaves, high-pressure vessels, layered vessels, forged vessels, and vessels with quick-opening closures.
- Review of datasheet fields that define what the vessel can tolerate: design pressure, design temperature, MAWP, MDMT, external pressure/full vacuum, corrosion allowance, material, cladding/lining, fatigue, cyclic service, NDE, pressure test, and overpressure protection.

## Does Not Provide

- Thickness calculation, stress classification, finite element analysis, fatigue calculation, buckling calculation, heat exchanger tubesheet design, nozzle reinforcement calculation, or pressure-test calculation.
- Fitness-for-service assessment for an in-service damaged vessel. Use the applicable inspection and FFS standards.
- Relief device sizing. Use API 520/API 521, ASME Section XIII, project relief calculations, and vendor data.
- Permission to change operating limits. Use approved engineering review, MOC, and jurisdictional requirements.

## Pressure Vessel Context Schema

Extract only fields that are visible, stated, or reasonably inferable from the provided documents. Mark assumptions and missing values.

```yaml
pressure_vessel_design_context:
  source:
    document:
    page_or_sheet:
    revision:
  vessel:
    tag:
    service:
    vessel_type:
    code:
    code_edition:
    division:
    certification_or_stamp:
    manufacturer:
    serial_number:
    year_built:
  design_envelope:
    design_pressure_internal:
    design_pressure_external_or_vacuum:
    mawp_internal:
    mawp_external:
    coincident_design_temperature:
    mdmt:
    corrosion_allowance:
    erosion_allowance:
    nominal_thickness:
    required_thickness:
    test_pressure:
    test_method:
    normal_operating_pressure:
    normal_operating_temperature:
    startup_shutdown_conditions:
    upset_conditions:
  design_basis_documents:
    user_design_specification:
    manufacturer_design_report:
    manufacturer_data_report:
    construction_records:
    nameplate_or_marking:
  materials:
    pressure_part_materials:
    attachment_materials:
    bolting_materials:
    welding_materials:
    material_traceability:
    impact_test_or_exemption:
    toughness_basis:
    pwht:
    cladding_lining_overlay:
    pmi_required:
  geometry_and_connections:
    shell_head_configuration:
    nozzles:
    manways:
    quick_opening_closure:
    supports:
    lifting_lugs:
    internal_attachments:
    jacket_or_half_pipe:
    heat_exchanger_tubesheet:
    expansion_joint_or_bellows:
  loading_and_analysis:
    design_by_rule:
    design_by_analysis:
    local_loads:
    wind_seismic:
    thermal_gradient:
    piping_reaction_loads:
    cyclic_service:
    fatigue_analysis_required:
    buckling_or_external_pressure_basis:
    ratcheting_or_shakedown_basis:
  inspection_examination_testing:
    examination_group:
    weld_joint_efficiency:
    nde_methods:
    cyclic_service_supplemental_exam:
    leak_test:
    hydro_or_pneumatic_test:
    final_inspection:
    inspection_opening:
  overpressure_protection:
    pressure_relief_device_tags:
    open_flow_path:
    system_design_basis:
    relief_design_basis_document:
    set_pressure:
    accumulation_or_overpressure_basis:
    protected_volume:
    relief_nozzle:
    isolation_valves:
  hazop_use:
    credible_deviations:
    consequences_enabled_by_context:
    safeguards_to_credit_or_review:
    missing_information:
```

## Design Envelope Extraction

- Treat the design envelope as the vessel tolerance boundary, not the normal operating condition.
- Extract internal MAWP and external MAWP or full-vacuum rating separately. External pressure/vacuum is often missed in HAZOP but can control collapse risk.
- Extract coincident pressure and temperature pairs. Do not mix MAWP from one temperature with another operating case unless the source explicitly supports it.
- Extract MDMT and impact-test or exemption basis. Low-temperature operation, autorefrigeration, blowdown, startup, depressuring, and cold feed can make MDMT relevant to HAZOP consequences.
- Extract corrosion allowance, erosion allowance, lining/cladding/overlay, and material of construction. These define whether the vessel remains within its design basis over time.
- Extract pressure-test method and test pressure as construction/acceptance evidence, not as allowable operating pressure.
- Extract whether the vessel was designed by rule, by analysis, or with a combination. Design-by-analysis signals that local stresses, cyclic service, or special geometries may matter.

## Required Design Documents

For Division 2 vessels, do not rely only on a P&ID tag.

- User's Design Specification: should define design conditions, service, loads, operating cases, corrosion allowance, cyclic data if applicable, and special requirements.
- Manufacturer's Design Report: should document how the vessel design satisfies the User's Design Specification and code requirements.
- Manufacturer's Data Report: should capture final certified construction data such as MAWP, MDMT, materials, test, and marking basis.
- Construction records: should support material traceability, welding qualifications, NDE, heat treatment, test records, and as-built condition.
- Nameplate/marking: useful for field verification of MAWP, MDMT, code edition, serial number, year built, construction type, and certification basis.

Flag any HAZOP or MOC where these documents are missing, inconsistent, or not aligned with P&ID and relief data.

## Materials And Toughness

- Extract material specifications for pressure parts, attachments, bolting, weld metal, cladding, lining, and overlay.
- Check material traceability and whether nonstandard or substitute material is identified.
- Extract toughness basis: impact testing, exemption, MDMT, governing thickness, PWHT condition, and low-temperature service assumptions.
- For low-temperature or depressuring scenarios, compare possible minimum metal temperature with MDMT rather than only normal operating temperature.
- For sour, hydrogen, caustic, chloride, amine, wet H2S, high-temperature hydrogen, or other damage mechanisms, flag the need for corrosion/materials review beyond the construction code.
- If cladding, lining, weld overlay, or nonmetallic lining protects the base metal, capture failure consequences: under-lining corrosion, permeation, blistering, loss of corrosion barrier, or hidden damage.

## Design By Rule And Design By Analysis Flags

Use Division 2 design method context to decide when HAZOP should ask for specialist mechanical review.

- Design-by-rule context includes shells, heads, external pressure, openings, nozzles, flanges, quick-opening closures, jackets, supports, heat exchangers, bellows, and expansion joints.
- Design-by-analysis context can involve plastic collapse, local failure, buckling, cyclic loading, ratcheting, and fatigue.
- Flag cyclic service, thermal cycling, pressure cycling, batch operation, frequent startup/shutdown, blowdown, quench, vibration, reciprocating equipment, or repeated PSV lifting as possible fatigue-relevant conditions.
- Flag local load cases from piping reactions, supports, lifting lugs, platforms, agitators, internals, seismic, wind, thermal gradients, nozzle loads, and differential expansion.
- Flag external pressure or vacuum scenarios from steamout, condensation, pump-out, blocked vent, rapid cooldown, vacuum system, or vapor recovery.
- Flag quick-opening closures for interlock, residual pressure, operator exposure, maintenance procedure, and wrong-opening hazards.

## Heat Exchanger And Special Component Context

For shell-and-tube exchangers and special vessels, extract both process sides and mechanical interfaces.

- Tube side and shell side design pressures and temperatures.
- Differential pressure design basis, if specified.
- Tube rupture scenario basis and protected side.
- Tubesheet type and whether thermal or pressure loading cases are special.
- Expansion joint or bellows presence.
- Channel, floating head, U-tube, fixed tubesheet, jacket, or half-pipe construction.
- Relief and isolation philosophy for each pressure chamber.

Do not assume the shell side protects the tube side or vice versa. HAZOP should track each pressure boundary and credible cross-leak path.

## Fabrication, Examination, And Testing Context

- Extract weld categories only when shown; otherwise record required NDE methods and examination group from design documents.
- Capture PWHT, preheat, heat treatment after forming, repair weld requirements, and whether repairs can affect original toughness or corrosion assumptions.
- Capture NDE methods: visual, RT, UT, MT, PT, ET, leak testing, acoustic emission, and any supplemental cyclic-service examination.
- Pressure test confirms construction integrity at test conditions. It does not prove acceptability for new operating modes, corrosion loss, fatigue damage, or changed service.
- For pneumatic or alternative testing, flag stored-energy risk and need for approved procedure.
- For old vessels, missing construction records or nameplate data should trigger mechanical integrity review before crediting design limits.

## Overpressure Protection Interface

Use this section together with API 520, API 521, and project relief calculations.

- Division 2 Part 9 addresses overpressure protection methods and responsibilities, including pressure relief devices, open flow paths, and overpressure protection by system design.
- Extract the protected volume, relief device tag, relief nozzle, set pressure, relief basis, discharge path, isolation valves, and any open-flow-path or system-design claim.
- Do not infer relief adequacy from vessel code stamp. Relief scenarios, capacity, backpressure, installation, and disposal system adequacy require separate relief documentation.
- If operating pressure, design pressure, or MAWP changes, flag relief device set pressure and capacity review.
- If the vessel has multiple chambers, jackets, coils, tubes, or heat exchanger sides, identify which pressure boundary each relief device protects.
- For blocked-in liquid, thermal expansion, tube rupture, fire exposure, utility failure, control failure, or runaway reaction, route scenario analysis to API 521 or project relief basis.

## HAZOP And LOPA Use

Use ASME VIII-2 context to improve consequence definition and safeguard review.

- Deviation: high pressure.
  - Causes: blocked outlet, utility failure, control valve failure, fire, tube rupture, runaway reaction, thermal expansion, wrong lineup, relief isolation.
  - Consequences: vessel overstress, relief lifting, loss of containment, brittle fracture if cold, escalation to connected systems.
  - Safeguards to verify: relief device, HIPS/HIPPS if applicable, high pressure trip, design pressure margin, relief documentation, open flow path, operator response.
- Deviation: vacuum or external pressure.
  - Causes: steam condensation, rapid cooldown, pump-out, blocked vent, vapor recovery, vacuum system, draining without venting.
  - Consequences: shell/head buckling or collapse, nozzle damage, inward leakage, air ingress, contamination.
  - Safeguards to verify: vacuum breaker, vent, procedure, external pressure rating, low pressure trip, nitrogen padding, mechanical review.
- Deviation: low metal temperature.
  - Causes: autorefrigeration, blowdown, cold feed, cryogenic contamination, Joule-Thomson cooling, startup/shutdown.
  - Consequences: brittle fracture risk if below MDMT or toughness basis.
  - Safeguards to verify: MDMT, impact test basis, depressuring study, material review, low-temperature alarm/interlock.
- Deviation: cyclic loading or fatigue.
  - Causes: frequent pressure/temperature cycles, vibration, thermal shock, batch operation, PSV chatter, compressor pulsation.
  - Consequences: crack initiation, leak, rupture, weld or nozzle failure.
  - Safeguards to verify: fatigue analysis, cyclic-service inspection, vibration control, operating envelope, startup/shutdown limits.
- Deviation: loss of corrosion barrier.
  - Causes: lining failure, wrong material, chemical contamination, erosion, under-deposit corrosion, damaged cladding.
  - Consequences: wall thinning, leak, relief load change, toxic/flammable release.
  - Safeguards to verify: corrosion allowance, inspection interval, corrosion monitoring, material compatibility, lining inspection.

## Missing Information To Flag

- Code edition, Division, stamp/certification basis, or vessel serial/year data is missing.
- MAWP, external pressure rating, MDMT, design temperature, corrosion allowance, or coincident pressure-temperature basis is missing.
- User's Design Specification, Manufacturer's Design Report, Manufacturer's Data Report, or nameplate is unavailable.
- Operating pressure or temperature exceeds, approaches, or is inconsistent with the stated design envelope.
- External pressure/full vacuum is not stated but vacuum scenarios are credible.
- Relief device is shown but protected volume, set pressure, relief basis, or isolation status is missing.
- Heat exchanger has multiple pressure chambers but only one relief basis is documented.
- Cyclic, thermal shock, vibration, or repeated startup/shutdown service exists but fatigue basis is not shown.
- Low-temperature scenarios are credible but MDMT/toughness basis is not shown.
- Corrosion/erosion/damage mechanism is credible but material and inspection basis are missing.
- Pressure test is shown but test method, test pressure, test fluid, or final inspection evidence is missing.

## Output Rule

When using this reference, separate mechanical design facts from process operating assumptions. State what the vessel is designed for, what it normally sees, what credible HAZOP deviations can challenge the design envelope, and what documents are needed before accepting a safeguard or operating-limit claim.

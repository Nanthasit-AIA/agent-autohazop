# API 650 Welded Tanks for Oil Storage

Use this reference when a HAZOP, LOPA, P&ID review, tank datasheet review, or process-safety information extraction task involves aboveground welded storage tanks built or specified to API 650.

## Source Traceability

- Source document: API Standard 650, Welded Tanks for Oil Storage, 13th edition, March 2020.
- The uploaded PDF text layer was readable. The skill reference intentionally converts the standard into practical extraction fields and HAZOP review prompts instead of reproducing API text, tables, figures, formulas, or acceptance criteria.
- API 650 is primarily a tank design, fabrication, erection, and inspection standard. Use it to identify the tank mechanical design envelope and appurtenance context; do not use this reference as a tank design calculation or code-compliance certification.

## Applies To

- Vertical, cylindrical, aboveground, welded storage tanks.
- Open-top, fixed-roof, internal floating-roof, and external floating-roof tank contexts when API 650 is specified.
- Tank datasheets, nameplate data, general arrangement drawings, nozzle schedules, foundation drawings, P&IDs, vent/overflow drawings, and inspection/test records.
- Storage of petroleum, petroleum products, and other liquid products where API 650 is the selected design basis.
- HAZOP review of tank fill, emptying, heating, mixing, blanketing, venting interfaces, overfill, drain, water draw, roof drain, sampling, product change, and maintenance isolation scenarios.

## Does Not Provide

- Final tank shell, roof, bottom, anchor, nozzle, seismic, wind, or settlement calculations.
- Tank vent sizing or emergency vent sizing. Use the API 2000 reference for venting atmospheric and low-pressure tanks.
- Pressure-vessel design. API 650 tanks are not ASME pressure vessels unless a separate pressure-vessel boundary is specified.
- Refrigerated storage tank design unless a separate applicable tank standard or annex basis is provided.
- Product compatibility, corrosion-rate selection, coating selection, fire protection design, or overfill prevention design by itself.

## Tank Context Schema

Extract tank information in this shape when reviewing a datasheet, P&ID, tank GA drawing, or operating procedure:

```yaml
source:
  documents: []
  drawing_numbers: []
  revision: null
  page_or_sheet: null
  assumptions: []
  missing_information: []

tank:
  tag: null
  service: null
  stored_liquid: null
  design_standard: API_650
  edition_or_project_spec: null
  tank_type: fixed_roof | open_top | internal_floating_roof | external_floating_roof | unknown
  roof_type: cone | dome | umbrella | self_supported | supported | floating | unknown
  bottom_type: flat | cone_up | cone_down | sloped | unknown
  foundation_type: ringwall | slab | earth | pile_supported | unknown
  capacity:
    nominal: null
    working: null
    overflow: null
    heel_or_unpumpable: null

geometry:
  diameter: null
  shell_height: null
  shell_courses: []
  bottom_slope: null
  annular_plate: null
  anchorage: self_anchored | mechanically_anchored | unknown

design_envelope:
  design_pressure: null
  design_vacuum: null
  maximum_design_temperature: null
  design_metal_temperature: null
  design_specific_gravity: null
  corrosion_allowance: null
  materials: []
  lining_or_coating: null
  wind_basis: null
  seismic_basis: null
  snow_or_roof_live_load_basis: null
  external_loads: []
  settlement_basis: null

operating_envelope:
  normal_level: null
  high_level_alarm: null
  high_high_level_trip_or_shutdown: null
  overflow_level: null
  low_level_alarm: null
  low_low_level_trip: null
  normal_temperature: null
  maximum_operating_temperature: null
  normal_pressure_or_blanketing_pressure: null
  maximum_fill_rate: null
  maximum_emptying_rate: null
  product_change_basis: null

connections:
  inlet_nozzles: []
  outlet_nozzles: []
  drains: []
  water_draws: []
  vents: []
  emergency_vents: []
  overflow: null
  manways: []
  gauge_hatches: []
  sampling_points: []
  mixers_or_agitators: []
  heating_coils_or_heaters: []
  roof_drains: []
  foam_or_fire_protection: []
  floating_suction_or_swing_line: null

instrumentation_controls:
  level_measurement: []
  temperature_measurement: []
  pressure_or_vacuum_measurement: []
  blanketing_control: null
  vent_control_or_vapor_recovery: null
  overfill_prevention: []
  alarms: []
  trips_or_interlocks: []

protection_layers:
  normal_vents: []
  emergency_vents: []
  weak_roof_or_frangible_roof_basis: null
  overflow_protection: null
  bund_or_dike: null
  fire_protection: null
  grounding_bonding: null
  corrosion_protection: null
  inspection_testing: []
  operating_procedures: []

hazop_context:
  design_intent: null
  deviations: []
  credible_causes: []
  consequences: []
  safeguards: []
  recommendations: []
```

## What To Extract First

Start with the fields that most often change the HAZOP result:

- Tank tag, service, stored liquid, product hazards, tank type, roof type, capacity, and design standard edition or project specification.
- Design pressure, design vacuum, maximum design temperature, design metal temperature, design specific gravity, corrosion allowance, materials, lining/coating, wind, seismic, and anchorage basis.
- Normal level, high level alarm, high-high level shutdown or transfer stop, overflow level, low level, maximum fill rate, and maximum emptying rate.
- Vent, emergency vent, blanketing, vapor recovery, flame arrester, overflow, drain, water draw, roof drain, and fire-protection connections.
- Inlet and outlet nozzle locations because they define overfill, pump suction loss, water draw, line-up, contamination, and reverse-flow scenarios.
- Operating modes: normal fill, normal emptying, simultaneous fill/empty, product change, water draw, tank cleaning, maintenance entry, heating, mixing, roof drain operation, and emergency isolation.

## Mechanical Envelope Rules

Use API 650 context to define what the tank can mechanically tolerate.

- Treat an API 650 tank as an atmospheric or low-pressure storage tank unless the datasheet clearly states a higher internal pressure basis and the applicable annex/project basis.
- Keep design pressure, design vacuum, normal blanketing pressure, vent set pressure, and emergency vent pressure separate.
- Maximum operating temperature is not automatically the design temperature; capture both when available.
- Design metal temperature matters for brittle-fracture screening and material selection. If the project location, lowest one-day mean temperature basis, or material toughness basis is missing, flag the design-temperature basis as incomplete.
- Design specific gravity controls shell and bottom loading. If the tank can store multiple products, capture the governing product and the product-change basis.
- Corrosion allowance, lining/coating, internal corrosion risk, bottom-side corrosion protection, and inspection basis should be captured separately.
- Foundation, anchorage, wind, seismic, settlement, and external loads affect overfill, sloshing, nozzle strain, roof damage, and loss-of-containment scenarios.

## Roof And Venting Interface

Use API 650 to identify roof type and mechanical roof assumptions; use API 2000 to review venting adequacy.

- Fixed-roof tanks need normal venting, emergency venting, blanketing/vapor recovery interface, and vacuum protection context.
- Floating-roof tanks need roof type, seal system, roof drain, roof leg, anti-rotation, guide pole, gauge well, rim vent, deck drain, and product-specific floatation/compatibility context.
- Internal floating-roof tanks need both fixed-roof vapor-space context and floating-roof seal/drain/access context.
- Weak roof-to-shell or frangible roof assumptions must be explicitly documented before being treated as overpressure mitigation.
- Flame arresters, conservation vents, blanketing regulators, vapor recovery valves, or vent headers can plug, freeze, corrode, foul, or be isolated. Capture isolation valves and bypasses.
- Do not infer vent capacity from API 650 alone. Route vent sizing questions to the API 2000 reference.

## Nozzles And Appurtenances

Tank nozzles and appurtenances define many HAZOP causes and safeguards.

- Extract nozzle tag, size, rating/class, elevation, service, connected line, internal projection, reinforcement, isolation valve, and blind/spade status where available.
- Separate inlet, outlet, recirculation, drain, water draw, overflow, vent, vapor return, foam, sample, gauge, roof drain, mixer, heater, and manway connections.
- Low nozzles can create full-tank drainage, siphoning, reverse flow, or leakage consequences.
- High fill nozzles can create static, splashing, foaming, vapor generation, or floating-roof impact concerns depending on product and inlet design.
- Heating coils, steam coils, hot-oil coils, and mixers add leak, overheating, cross-contamination, and ignition-source scenarios.
- Floating suction or swing-line assemblies add wrong-position, stuck, loss-of-prime, water pickup, and unavailable-suction scenarios.

## Level, Overfill, And Inventory Control

For tank HAZOP, level context is usually more important than tank wall thickness.

- Capture normal operating level, maximum working level, high level alarm, high-high level trip, overflow elevation, roof landing level, low-low pump trip, and tank heel.
- Identify whether overfill protection stops incoming transfer, closes an inlet valve, trips a pump, diverts flow, alarms the operator, or depends on manual action.
- A bund/dike limits spread after release; it does not prevent tank overfill.
- Overflow lines are safeguards only when capacity, routing, destination, isolation status, freezing/fouling risk, and consequence of discharge are understood.
- Product transfer into the wrong tank can exceed design specific gravity, temperature, compatibility, vapor pressure, or roof/seal assumptions even if level remains below overflow.

## Pressure And Vacuum Scenarios

Use these prompts when a tank node includes filling, emptying, heating, cooling, blanketing, vapor recovery, or vent headers.

- Overpressure causes: overfill, blocked vent, fire exposure, high fill rate, vapor generation, nitrogen regulator failure, vapor recovery blockage, wrong connection, steam coil leak, chemical reaction, inerting error.
- Vacuum causes: pump-out with blocked vent, rapid cooling, steam-out condensation, vapor recovery malfunction, nitrogen failure, blocked flame arrester, closed vent isolation, liquid withdrawal under sealed conditions.
- Pressure or vacuum consequences: roof damage, shell-to-roof damage, bottom uplift, tank buckling, seal damage, loss of containment, vapor release, air ingress, flammable atmosphere, pump cavitation, or structural instability.
- Interface with API 2000 for normal inbreathing/outbreathing, emergency venting, and vacuum-protection adequacy.

## Floating Roof Review

If the tank has an internal or external floating roof, capture roof-specific operating states.

- Roof floating, roof landed, filling from landed condition, draining, cleaning, maintenance entry, and roof support-leg setting are distinct operating modes.
- Extract deck drain, emergency drain, seal type, rim space, guide pole, anti-rotation device, gauge well, sample well, and roof access details when available.
- Low-level operation can land the roof and create vapor-space changes, seal damage, leg damage, or restart restrictions.
- Roof drains can fail open or closed and can introduce water/product cross-contamination or release routes.
- Floating roof operation is sensitive to product specific gravity, wax/solid formation, fouling, snow/rain load, and uneven settlement.

## Bottom, Foundation, And Settlement

Extract bottom and foundation context because leaks often start outside the P&ID boundary.

- Capture bottom type, annular plate, bottom slope, sump, under-bottom connection, leak detection, cathodic protection, liner, foundation type, and settlement monitoring.
- Bottom drains and water draws can release product if left open, plugged, frozen, or connected to the wrong destination.
- Settlement can strain nozzles, distort floating roofs, affect roof drains, and change tank calibration/level accuracy.
- Foundation or anchorage limits can be critical for wind, seismic, flooding, external loads, and empty-tank uplift.

## HAZOP Deviations To Consider

Use these deviations when the node includes an API 650 tank:

- High level or overfill: transfer pump not stopped, wrong tank lined up, level instrument failure, alarm ignored, valve failed open, manual gauging error, high fill rate.
- Low level: pump-out continues, outlet vortexing, pump cavitation, floating roof landed, heater coil exposed, mixer operation below minimum level.
- High pressure: blocked vent, failed blanketing regulator, fire exposure, vapor recovery blockage, emergency vent unavailable, hot product, reaction, steam leak.
- Vacuum: pump-out with blocked vent, rapid cooling, nitrogen failure, vapor recovery malfunction, steam-out condensation.
- High temperature: hot transfer, failed heater control, steam coil leak, external fire, product stratification, mixer failure.
- Low temperature: brittle-fracture risk, wax/solid formation, vent freezing, seal stiffening, contraction vacuum.
- Wrong composition: wrong product, water ingress, incompatible product, high vapor pressure liquid, corrosive contaminant, off-spec density/specific gravity.
- Loss of containment: bottom leak, shell leak, nozzle leak, roof drain leak, overfill, drain left open, manway gasket failure, settlement-induced nozzle strain.
- Floating roof abnormal: roof stuck, roof sunk, seal failure, roof drain blocked, roof landed unexpectedly, guide pole leakage, foam dam or seal fire scenario.
- Maintenance hazard: confined space, pyrophoric deposits, residual hydrocarbons, nitrogen/inerting hazard, open drains, blinds/spades incorrect.

## Safeguard Review Rules

- Do not credit API 650 design itself as an IPL unless the scenario is purely mechanical capacity and the design basis directly addresses it.
- Treat level alarms, HH trips, transfer pump stops, inlet valve closures, and diversion valves as separate safeguards only if their sensors, logic, final elements, and response are independent enough for the intended credit.
- Treat vents, flame arresters, blanketing valves, vapor recovery valves, and emergency vents as safeguards only after checking isolation, plugging/fouling, freezing, corrosion, and maintenance bypass status.
- A floating roof reduces vapor space in normal service but can create separate hazards during landed-roof, drain, seal, and maintenance modes.
- A dike/bund is consequence mitigation, not prevention of tank failure or overfill.
- Use API 2000 for venting adequacy; use API 521 for connected relief/flare/depressuring systems when tank vapors discharge into a relief or flare network.

## Missing Information To Flag

Flag these gaps explicitly:

- API 650 edition, project tank specification, or purchaser options not shown.
- Tank type, roof type, design pressure, design vacuum, maximum design temperature, or design metal temperature missing.
- Design specific gravity, corrosion allowance, material, lining/coating, or stored-product range missing.
- Normal level, high alarm, high-high trip, overflow elevation, low-level limit, maximum fill rate, or maximum emptying rate missing.
- Vent, emergency vent, blanketing, vapor recovery, flame arrester, or overflow sizing basis missing.
- Nozzle schedule, nozzle elevations, internal piping, drains, water draw, roof drain, or mixer/heater details missing.
- Floating roof seal, roof drain, roof landing level, support-leg setting, or product-specific floating basis missing.
- Foundation, anchorage, wind, seismic, settlement, cathodic protection, or leak-detection basis missing.
- Inspection/testing records, hydrotest/pneumatic test basis, settlement records, or nameplate data missing.

## Output Rule

When using this reference, output only HAZOP-relevant tank context, operating/design limits, safeguards, and missing information. Keep API 650 mechanical design assumptions separate from API 2000 venting assumptions and from normal operating values.

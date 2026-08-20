# BS EN 1861:1998 Refrigerating Systems and Heat Pumps P&ID Layout and Symbols

Use this reference when extracting or checking context from system flow diagrams and piping and instrument diagrams for refrigerating systems and heat pumps. It is most useful for deciding what minimum information should appear on refrigeration/heat-pump diagrams, how to separate a system flow diagram from a P&ID, what symbol categories to expect, and how to decode common instrument function letters.

This is a derived working guide for HAZOP/LOPA and P&ID context extraction. It does not reproduce the graphical symbol tables and does not replace the standard, project drawing legend, ISO 3511, ISO 10628, refrigeration safety standards, or project/company drafting rules.

## Source Traceability

- Source standard: `BS EN 1861:1998`, English version of `EN 1861:1998`.
- Title: `Refrigerating systems and heat pumps - System flow diagrams and piping and instrument diagrams - Layout and symbols`.
- Scope and exclusions: clause 1.
- Normative references: clause 2, including ISO 3511 parts, ISO 4196, ISO 5457, ISO 7200, and ISO 10628.
- Definition and classification of diagram types: clauses 3 and 4.
- Layout rules: clause 5.
- Graphical-symbol selection: clause 6 and Table 1.
- Example diagrams: Annex A.
- Instrument letter code and example measurement/control symbols: Annex B.

## Applies To

- Refrigerating systems and heat pumps.
- System flow diagrams that show configuration/function at a higher level.
- P&IDs that show technical realization with equipment, machinery, piping, measurement/control functions, and safety equipment.
- Diagrams used through design, construction, installation, commissioning, operation, maintenance, and decommissioning.

## Does Not Apply To

- Refrigeration systems where heat is extracted by an electrical circuit such as Peltier-effect systems.
- General process P&IDs outside refrigeration/heat-pump scope unless the project adopts the same drawing rules.
- Detailed instrument interconnection diagrams or loop drawings.
- Final refrigeration safety design, pressure equipment compliance, or relief sizing.

## Diagram Type Decision

Use this split:

| Diagram type | Purpose | Minimum extraction target |
|---|---|---|
| System flow diagram | Shows configuration and function using symbols connected by flow lines. | Main equipment/machinery, in/out products, refrigerant, heat-transfer medium, absorbent/adsorbent, and characteristic operating conditions. |
| P&ID | Shows technical realization based on the system flow diagram. | Refrigerant/medium designations, operating conditions, components, standby equipment, piping size/rating/material/type, insulation, measurement/control functions, and safety equipment. |

Do not treat a system flow diagram as sufficient for HAZOP node detail. Use it for orientation, then request or inspect the P&ID for valves, fittings, instruments, safety devices, piping class, and insulation.

## Minimum Context To Extract From Refrigeration P&IDs

Capture these fields:

```yaml
refrigeration_pid_context:
  diagram_type:
  refrigerant:
  heat_transfer_medium:
  absorbent_or_adsorbent:
  characteristic_operating_conditions:
  refrigerant_charge:
  mass_flows:
  equipment_and_machinery:
  standby_equipment:
  piping:
    size:
    pressure_rating:
    material:
    type_or_class:
    identification_number:
    insulation:
  valves_and_fittings:
  measurement_control_functions:
  safety_equipment:
  flow_routes:
  flow_directions:
  construction_data_references:
  separate_lists_or_tables:
```

If any of the minimum P&ID fields are absent, mark them `missing` instead of inferring from symbol appearance alone.

## Symbol Category Checklist

Table 1 organizes graphical symbols for equipment, machinery, and piping. For context extraction, expect symbols from these subject groups:

- Piping.
- Shut-off valves.
- Check valves.
- Regulating valves.
- Valves/fittings with safety function.
- Valve actuators.
- Pipe fittings.
- Vessels and tanks.
- Vessels/columns/reactors with internals.
- Heating or cooling facilities.
- Heat exchangers and steam generators.
- Filters, liquid filters, gas filters, and filter-driers.
- Separators.
- Agitators.
- Liquid pumps.
- Compressors, vacuum pumps, and fans.
- Lifting, conveying, and transport.
- Scales.
- Distribution facilities.
- Motors, engines, and drives.

Use the project legend or the standard's graphical tables to confirm the exact symbol. This reference only tells you which categories to look for and what context to extract.

## Layout Rules To Check

- Use standardized drawing sheets and title blocks consistent with the referenced ISO drawing standards.
- Highlight main flow lines or main piping more strongly than auxiliary lines.
- Keep line spacing clear enough to preserve readability.
- Show flow direction with arrows; treat arrows as diagram intent, not proof that reverse flow is impossible.
- Use SI units.
- Put equipment identification close to the symbol but do not rely on the symbol alone for details.
- Put flow-line or piping designations along the line in a clear orientation.
- Put valve/fitting designations next to the symbol and aligned with the flow direction.
- Use reference boxes or separate tables for flow rates, operating conditions, and thermophysical properties.

For HAZOP, flag any crowded diagram, missing title/revision context, unclear line direction, unclear continuation, missing table reference, or inconsistent symbol use.

## Instrument Function Letter Code

Annex B follows ISO 3511-style function-letter logic. Decode tags by reading the first letter as the measured/initiating variable and succeeding letters as modifiers or output/display functions.

Common first-letter variables:

| Letter | Meaning |
|---|---|
| `A` | Alarm or analysis context, depending on position/function. |
| `D` | Density when first; difference when modifier. |
| `E` | Electrical variable. |
| `F` | Flow rate. |
| `G` | Gauging, position, or length. |
| `H` | Hand or manually initiated. |
| `K` | Time or time programme. |
| `L` | Level. |
| `M` | Moisture or humidity. |
| `P` | Pressure or vacuum. |
| `Q` | Quality, analysis, concentration, conductivity, or totalizing context depending on position. |
| `R` | Nuclear radiation when first; recording when succeeding. |
| `S` | Speed/frequency when first; switching when succeeding. |
| `T` | Temperature; transmitting when succeeding. |
| `U` | Multivariable. |
| `V` | Viscosity. |
| `W` | Weight or force. |
| `X` | Unclassified variable. |
| `Z` | Emergency or safety acting. |

Common succeeding-letter functions:

- `A`: alarm.
- `C`: controlling.
- `I`: indicating.
- `R`: recording.
- `S`: switching.
- `T`: transmitting.
- `H` / `L`: high/max or low/min context when used with setpoint/alarm symbols.

User-choice letters must be defined by the project. Do not infer a custom meaning without a legend.

## Tag Interpretation Examples

Use these examples as decoding patterns, not as a full symbol library:

| Tag/function pattern | Interpret as |
|---|---|
| `FI` | Flow indication. |
| `FSL` | Flow switch or safety-related low-flow switching context, depending on symbol/legend. |
| `LI` | Level indication. |
| `LSH` / `LSL` | Level switch high/low or alarm setpoint context. |
| `LT` | Level transmitter. |
| `PG` | Pressure gauge. |
| `PDG` | Differential pressure gauge. |
| `PS` | Pressure switch. |
| `PT` | Pressure transmitter. |
| `PI` | Pressure indication. |
| `PC` | Pressure control. |
| `PZH` / `PZL` | Safety/emergency high or low pressure acting context, confirm with project legend. |
| `QI` / `QA` | Quality/analysis indication or alarm, such as gas concentration. |
| `TI` | Temperature indication. |
| `TT` | Temperature transmitter. |
| `TSH` / `TSL` | Temperature switch high/low or alarm setpoint context. |

For tags with two measured/initiating variables, put the prime function first when extracting context and preserve the full tag from the drawing.

## Refrigeration/Heat-Pump HAZOP Prompts

For each refrigeration node, ask:

- What refrigerant, heat-transfer medium, absorbent, or adsorbent is present?
- What are the characteristic operating pressures, temperatures, phases, and flow rates?
- Which equipment is installed, and which equipment is standby?
- Are compressors, pumps, fans, heat exchangers, filters/filter-driers, separators, receivers/vessels, safety devices, and actuators shown?
- Are piping size, pressure rating, material/type/class, and thermal insulation identified or referenced?
- Are flow directions and route continuations clear?
- Where can liquid refrigerant accumulate, migrate, or be trapped?
- Where can overpressure occur due to isolation, heating, blocked discharge, thermal expansion, or compressor operation?
- Where can low temperature, freezing, brittle failure, or ice formation affect equipment/piping/instruments?
- Are relief/safety devices and pressure cut-outs shown and connected to protected items?
- Are high/low pressure, temperature, level, flow, and gas concentration instruments shown with their alarms/trips?
- Is NH3 or another hazardous refrigerant indicated, and are detection/ventilation/alarm functions represented or referenced?
- Are maintenance/decommissioning requirements visible: isolation, draining, venting, pump-out, recovery, purge, or safe disposal?

## Missing Information To Flag

- Diagram type unclear: system flow diagram presented as if it were a P&ID.
- Refrigerant or heat-transfer medium not designated.
- Characteristic operating conditions missing.
- Refrigerant charge or mass flow absent where needed for safety review.
- Standby equipment not identified.
- Piping pressure rating/material/class/type missing.
- Thermal insulation not shown where cold surfaces, condensation, freezing, or heat gain matter.
- Safety equipment missing or unclear.
- Instrument letters not defined by project legend when user-choice or ambiguous letters are used.
- Flow direction or sheet continuation unclear.
- Separate equipment/piping/thermophysical property lists referenced but unavailable.


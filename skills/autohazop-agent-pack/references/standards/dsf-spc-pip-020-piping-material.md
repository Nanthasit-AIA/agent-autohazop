# DSF-SPC-PIP-020 Piping Material

Use this reference for DESFA high-pressure transmission station piping material context. It supports HAZOP/LOPA extraction from P&IDs, line lists, piping class tables, and station design documents by mapping line class codes to mechanical design envelopes and material constraints.

Do not use this reference as a replacement for the source specification for procurement, wall-thickness design, detailed branch-table lookup, or code compliance certification. For HAZOP/LOPA, use it to identify what the piping system is designed to tolerate and where missing or conflicting information must be resolved.

## Source Traceability

- Source document: `DSF-SPC-PIP-020`, Rev. 1, June 2021, 53 pages.
- Scope and exclusions: section 1, page 4.
- Reference standards and linked DESFA specifications: section 2, pages 5-8.
- Class code logic and design-condition basis: section 4, pages 10-12.
- Piping class index: section 5, pages 13-14.
- Detailed material specifications, branch schedules, flanges, gaskets, bolting, and notes: section 6, pages 15-53.

## Applies To

- Above-ground and underground piping inside valve stations, scraper stations, metering/pressure-reduction stations, and compressor stations.
- Main-line piping within station battery limits.
- Natural gas, nitrogen, utilities, hot water, and condensate services covered by the listed piping classes.

## Does Not Apply To

- Cross-country pipelines outside the covered station scope.
- Exact relief sizing, PSV set-pressure selection, depressuring calculations, or flare design.
- Equipment design limits unless the equipment datasheet explicitly ties the equipment to the same class envelope.
- Instrument loop logic, alarm setpoints, SIF proof-test basis, or IPL credit.

## Extract These Fields

From a P&ID, line list, or material table, capture:

- `line_number`, `line_size_dn`, `piping_class`, `service`, `fluid`, `location` (`AGI` or `UGI`), and connected equipment.
- `design_code`, `pressure_class`, `design_pressure_barg`, `design_temperature_c`, `design_factor`, `corrosion_allowance_mm`, `material_family`, and `covered_size_range_dn`.
- Boundary items: reducers, branch connections, vents, drains, isolation valves, spectacle blinds/spades/spacers, line blinds, flanges, gaskets, and bolting.
- Connection restrictions: threaded, socket weld, butt weld, weld neck, blind, raised face, and first-isolation-valve position.
- Special mechanical notes: impact-test temperature, PWHT avoidance, vibration/pulsation restrictions, branch minimum size, and surface-finish/gasket contact notes.

## Piping Class Code

Interpret the class code as:

- First digit: pressure/rating family.
  - `1`: CL150 / PN20; nominal design pressure family 19 barg.
  - `3`: CL300 / PN50; nominal design pressure family 50 barg.
  - `6`: CL600 / PN100; nominal design pressure family 80 barg.
  - `9`: CL900 / PN150; nominal design pressure family 140 barg.
- Second letter: material family.
  - `A`: carbon steel, including normal-temperature and low-temperature carbon steel variants.
  - `B`: stainless steel.
  - `C`: HDPE.
- Third digit: sequential variant within the same pressure/material family.

Do not infer a complete piping class from pressure class alone. The location, design factor, service, corrosion allowance, temperature range, and material family are also required.

## Class Envelope Table

Use the table below for HAZOP screening and context extraction. Where source sections conflict, keep the conflict visible and request verification.

| Class | Design code | Pressure class | Location | Design factor | Design pressure | Design temperature | CA | Material | DN range | Service | HAZOP note |
|---|---|---:|---|---:|---:|---:|---:|---|---:|---|---|
| 1A1 | EN 1594 | CL150 / PN20 | UGI | 0.5 | 19 barg | -20/+50 C | 0 mm | Carbon steel | 15-600 | Natural gas | Underground natural gas class. |
| 1A2 | EN 1594 | CL150 / PN20 | UGI | 0.4 | 19 barg | -20/+50 C | 0 mm | Carbon steel | 15-600 | Natural gas | Lower design factor variant. |
| 1A3 | EN 1594 | CL150 / PN20 | AGI | 0.5 | 19 barg | -20/+80 C | 0.5 mm | Carbon steel | 15-600 | Natural gas | Above-ground natural gas class. |
| 1A4 | EN 1594 | CL150 / PN20 | AGI | 0.4 | 19 barg | -20/+80 C | 0.5 mm | Carbon steel | 15-600 | Natural gas | Lower design factor variant. |
| 3A1 | EN 1594 | CL300 / PN50 | UGI | 0.5 | 50/48 barg | -20/+50 C | 0 mm | Carbon steel | 15-600 | Natural gas | Index and material-spec header conflict on pressure; verify. |
| 3A2 | EN 1594 | CL300 / PN50 | UGI | 0.4 | 50/48 barg | -20/+50 C | 0 mm | Carbon steel | 15-600 | Natural gas | Index and material-spec header conflict on pressure; verify. |
| 3A3 | EN 1594 | CL300 / PN50 | AGI | 0.5 | 50/48 barg | -20/+80 C | 0.5 mm | Carbon steel | 15-600 | Natural gas | Index and material-spec header conflict on pressure; verify. |
| 3A4 | EN 1594 | CL300 / PN50 | AGI | 0.4 | 50/48 barg | -20/+80 C | 0.5 mm | Carbon steel | 15-600 | Natural gas | Index and material-spec header conflict on pressure; verify. |
| 6A1 | EN 1594 | CL600 / PN100 | UGI | 0.5 | 80 barg | -20/+50 C | 0 mm | Carbon steel | 15-1050 | Natural gas | Underground high-pressure natural gas class. |
| 6A2 | EN 1594 | CL600 / PN100 | UGI | 0.4 | 80 barg | -20/+50 C | 0 mm | Carbon steel | 15-1050 | Natural gas | Lower design factor variant. |
| 6A3 | EN 1594 | CL600 / PN100 | AGI | 0.5 | 80 barg | -20/+80 C | 0.5 mm | Carbon steel | 15-1050 | Natural gas | Above-ground high-pressure natural gas class. |
| 6A4 | EN 1594 | CL600 / PN100 | AGI | 0.4 | 80 barg | -20/+80 C | 0.5 mm | Carbon steel | 15-1050 | Natural gas | Lower design factor variant. |
| 1A5 | EN 13480 | CL150 / PN20 | AGI | N/A | 19 barg | -48/+80 C | 0.5 mm | Low-temp carbon steel | 15-750 | Natural gas / nitrogen | Low-temperature service; verify impact-test basis. |
| 6A5 | EN 13480 | CL600 / PN100 | AGI | N/A | 80 barg | -48/+80 C | 0.5 mm | Low-temp carbon steel | 15-750 | Natural gas / nitrogen | Low-temperature high-pressure service. |
| 1A6 | EN 13480 | CL150 / PN20 | AGI | N/A | 19 barg | -20/+90 C | 1.5 mm | Carbon steel | 15-1050 | Utilities / hot water / nitrogen / condensates | Utility/condensate class; not natural gas-only. |
| 3A6 | EN 13480 | CL300 / PN50 | AGI | N/A | 50 barg | -20/+90 C | 1.5 mm | Carbon steel | 15-1050 | Utilities / hot water / nitrogen / condensates | Source index OCR shows CL600/PN100 in one place; class code/spec header indicate CL300/PN50. Verify. |
| 6A6 | EN 13480 | CL600 / PN100 | AGI | N/A | 80 barg | -20/+90 C | 1.5 mm | Carbon steel | 15-1050 | Utilities / hot water / nitrogen / condensates | One material-spec header shows +80 C while index/next header show +90 C; verify. |
| 3B1 | EN 13480 | CL300 / PN50 | AGI | N/A | 48/50 barg | -40/+80 C | 0 mm | Stainless steel | 15-250 | Natural gas / utilities | Index and material-spec header conflict on pressure; verify. |
| 6B1 | EN 13480 | CL600 / PN100 | AGI | N/A | 80 barg | -40/+80 C | 0 mm | Stainless steel | 15-250 | Natural gas / utilities | Stainless high-pressure class. |

For screening, use the more conservative value when a conflict exists, but do not close an action or accept a design until the original source is checked.

## Material Families

- EN 1594 natural-gas carbon steel classes use EN ISO 3183 line-pipe grades in the L245 family for many listed pipe/fitting cases.
- EN 13480 carbon steel utility/condensate classes use EN 10216/EN 10217 pipe families and EN 10253/EN 10222 fittings/forgings.
- Low-temperature carbon steel classes use low-temperature grades and low-temperature bolting; treat them as a distinct material envelope from normal carbon steel.
- Stainless classes use X5CrNi18-10 families for pipe, fittings, flanges, blinds, and bolting context.
- Do not mix class material families across a class break without identifying the boundary and asking for material compatibility confirmation.

## Branch and Connection Rules

Branch schedule symbols:

| Symbol | Meaning |
|---|---|
| `STE` | Socket weld tee, equal |
| `STR` | Socket weld tee, reducing |
| `SOL` | Sockolet |
| `WTE` | Weld tee, equal |
| `WTR` | Weld tee, reducing |
| `WOL` | Weldolet |

Use the original branch schedule table when exact run/branch DN pairing matters. For HAZOP screening, always capture the branch connection type because it can affect leakage, vibration, isolation, inspection, and mechanical integrity discussion.

Minimum branch size is DN25 in the listed branch schedules.

## Mechanical Rules To Carry Into HAZOP

- Select piping material specification based on fluid/gas characteristics, design pressure, design temperature, design factor, and corrosion allowance.
- Treat class pressure/temperature as a design envelope, not a normal operating value.
- For vibrating or pulsating service, flag any piping smaller than DN50 or socket-welded construction for review; the specification expects fully butt-welded construction in that service.
- All threaded connections, where allowed, are NPT.
- Screwed fittings are only allowed after the first isolation valve in the listed small-bore fitting notes. If a P&ID shows a threaded connection upstream of first isolation, flag it.
- Tees at DN80 and below may be die-forged; seamless caps are expected.
- Fittings require Charpy impact testing according to the applicable material standard and project/specification temperature.
- EN 1594 does not call for PWHT in this document; high-strength materials should avoid a PWHT need unless purchaser approval exists.
- Blind flanges should have a vent screw; capture blind locations during isolation/depressuring reviews.
- Branch welding surfaces require NDT attention in the source context; for HAZOP, flag branch-heavy or modified piping as mechanical integrity context rather than as an IPL.

## Flanges, Gaskets, Blinds, and Bolting

- Many carbon-steel classes use EN 1759-1 for small-bore flanges and EN 14870-3 for larger weld-neck/blind flanges. Verify the class table before applying the split.
- Carbon-steel classes commonly use spiral-wound gaskets with inner/outer rings and non-asbestos filler to EN 12560-2.
- Stainless classes use compressed non-metallic, non-asbestos flat ring gaskets to EN 12560-1 in the extracted tables.
- Carbon-steel bolting context uses EN 1515-3; stainless bolting context uses EN 1515-1.
- Gasket contact surfaces use stock finish context. Capture gasket type and flange face when reviewing leak, fire, maintenance, or wrong-gasket scenarios.

## Impact-Test Context

Use impact-test temperature as a fragility/brittle-fracture screening clue, not as a standalone acceptance decision.

| Class group | Extracted impact-test context |
|---|---|
| EN 1594 carbon steel natural-gas classes | -20 C noted in class notes. |
| 1A5 low-temperature carbon steel | -48 C noted in class notes. |
| 6A5 low-temperature carbon steel | -50 C noted in class notes. |
| EN 13480 carbon steel utility/condensate classes | -25 C noted in class notes. |
| Stainless classes | No comparable Charpy note was extracted; verify if low-temperature service is relevant. |

## HAZOP Use

When a P&ID line class is available:

1. Map the line class to the class envelope table.
2. Compare service, AGI/UGI location, DN range, pressure, and temperature against the line list and equipment datasheets.
3. Identify class breaks at equipment nozzles, reducers, branches, tie-ins, package boundaries, and material changes.
4. List possible deviations enabled by mechanical context: overpressure above design, low temperature below material class, wrong material/gasket/bolting, corrosion allowance mismatch, vibration/pulsation fatigue, leakage at branch/flange/threaded fittings, blocked-in thermal expansion, and isolation/depressuring difficulty.
5. Separate safeguards: material class and design code are inherent/mechanical design context; they are not IPLs by themselves.

When line class is missing:

- Do not infer acceptability from pressure class or service alone.
- Request line class, line list, design pressure/temperature, service, DN, AGI/UGI location, corrosion allowance, and connected equipment design data.
- If only a P&ID is available, record topology and mark mechanical envelope as `missing`.

## Missing Or Ambiguous Information To Flag

- Conflict between class index and detailed material-spec header.
- Missing line class or class break at equipment/package boundary.
- Operating pressure/temperature absent; design envelope alone is not enough for normal-operation HAZOP.
- AGI/UGI location unclear.
- Service/fluid inconsistent with class service.
- DN outside listed class size range.
- Threaded/socket-welded fittings in vibration/pulsation service.
- Screwed fitting location relative to first isolation valve unclear.
- Low-temperature operation below class minimum or without impact-test confirmation.
- Gasket/bolting material mismatch at flange pairs.
- Branch connection type absent where branch size/run size matters.

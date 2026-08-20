# API 610 / ISO 13709 Centrifugal Pumps - Book Wiki

## Source Card

- Source slug: `api-610-iso-13709-centrifugal-pumps`
- Domain: `pump-design`
- Tags: `api-610`, `centrifugal-pump`, `minimum-flow`, `npsh`, `seal`, `driver`
- Primary procedural skill: `hazop-hazan-study-leader`
- Topic wiki: `pump-design-operation`
- Detailed standard reference: `autohazop-agent-pack/references/standards/api-610-iso-13709-centrifugal-pumps.md`
- Working quality: controlled-use qualitative guidance; verify numeric, tabular, and clause-level decisions from project/source basis.
- Source quality: pages: 194; outline/bookmark count: 157
- Source file: `G:\.shortcut-targets-by-id\1B9dVATZu7Jx-iYIRt0KSwjnMzhv4w10U\2026_Thananchanai_Nin\SCGC\Lrarning Data\3.Standards, Codes & Methodology\Equipment Design Standards\api_std_610_centrifugal_pumps.pdf`

## Alternate Source PDFs

- `G:\.shortcut-targets-by-id\1B9dVATZu7Jx-iYIRt0KSwjnMzhv4w10U\2026_Thananchanai_Nin\SCGC\Lrarning Data\API STD 610 - 2010-09 Centrifugal Pumps for Petroleum, Petrochemical and Natural Gas Industries, 11th Ed.(ISO 137092009 Identic (Rayan Paya) (z-library.sk, 1lib.sk, z-lib.sk).pdf`

## What This Source Contributes

Improve pump and transfer-line HAZOP rows by forcing the model to reason through suction, discharge, minimum flow/recycle, seal system, driver, standby logic, and trip actions.

## Decision Lens

Use pump operating/design envelope to challenge no/less/more/reverse flow causes, minimum flow, NPSH, cavitation, seals, trips, standby, and recycle assumptions.

## Source-Derived Checks

- Identify pump service, suction source, discharge destination, normal flow, rated flow, minimum continuous flow, NPSH margin, recycle, seal system, driver, and standby arrangement.
- Check no/less flow causes against blocked suction/discharge, low suction head, vapor lock, cavitation, driver trip, control valve action, and minimum-flow failure.
- Keep pump trip or low-flow interlock as safeguard/cause only when the specific trip action independently creates the selected deviation.

## HAZOP Injection Pattern

1. Identify whether the current node/deviation touches this source's domain.
2. Improve cause wording so it names the failed item, failure mode, human task, operating phase, or design-envelope exceedance.
3. Improve consequence wording so it describes the unmitigated event path before safeguards.
4. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
5. Convert missing source/project data into a precise recommendation.
6. Do not reduce risk or claim IPL credit unless the specific project basis is supplied.

## Sharp Questions

- [ ] Identify pump service, suction source, discharge destination, normal flow, rated flow, minimum continuous flow, NPSH margin, recycle, seal system, driver, and standby arrangement.
- [ ] Check no/less flow causes against blocked suction/discharge, low suction head, vapor lock, cavitation, driver trip, control valve action, and minimum-flow failure.
- [ ] Keep pump trip or low-flow interlock as safeguard/cause only when the specific trip action independently creates the selected deviation.
- [ ] Pump datasheet
- [ ] Hydraulic curve
- [ ] NPSH basis
- [ ] Minimum-flow/recycle basis
- [ ] Seal/driver/trip cause-and-effect

## Anti-Patterns To Kill

- Using generic pump failure where no pump is on the selected node.
- Claiming cavitation, dry running, seal failure, or reverse flow without suction/discharge/NPSH/check-valve context.

## Row Moves

- Convert 'pump failure' into failed-to-start, failed-to-run, loss of suction, blocked discharge, seal failure, cavitation, driver trip, or standby failure.
- For dry-running consequence, check whether low-low level trip is a safeguard, not part of the unmitigated consequence.

## Recommendation Logic

- Verify minimum-flow/recycle and NPSH basis for no/less flow scenarios.
- Request pump cause-and-effect and standby logic before crediting trips or auto-starts.

## Missing-Basis Checklist

- [ ] Pump datasheet
- [ ] Hydraulic curve
- [ ] NPSH basis
- [ ] Minimum-flow/recycle basis
- [ ] Seal/driver/trip cause-and-effect
- [ ] Use the P&ID/process graph and supplied project data as controlling evidence.
- [ ] Keep normal operation, design limits, safe operating limits, and protection layers separate.
- [ ] Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- [ ] Do not treat a standard/book statement as proof that a safeguard exists in the project.
- [ ] Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- [ ] Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Source Navigation Preview

COVER | SPECIAL NOTES | API FOREWORD | CONTENTS | FOREWORD | INTRODUCTION | 1 Scope | 2 Normative references | 3 Terms and definitions | 4 Classification and designation | 4.1 General | 4.2 Pump designations | 4.3 Units and governing requirements | 5 Basic design | 5.1 General | 5.2 Pump types | 5.3 Pressure casings | 5.4 Nozzles and pressure casing connections | 5.5 External nozzle forces and moments | 5.6 Rotors | 5.7 Wear rings and running clearances | 5.8 Mechanical shaft seals | 5.9 Dynamics | 5.10 Bearings and bearing housings | 5.11 Lubrication | 5.12 Materials | 5.13 Nameplates and rotation arrows | 6 Accessories | 6.1 Drivers | 6.2 Couplings and guards | 6.3 Baseplates | 6.4 Instrumentation | 6.5 Piping and appurtenances | 6.6 Special tools | 7 Inspection, testing, and preparation for shipment | 7.1 General | 7.2 Inspection | 7.3 Testing | 7.4 Preparation for shipment | 8 Specific pump types | 8.1 Single-stage overhung pumps | 8.2 Between-bearings pumps (types BB1, BB2, BB3 and BB5) | 8.3 Vertically suspended pumps (types VS1 through VS7) | 9 Vendor's data | 9.1 General | 9.2 Proposals | 9.3 Contract data | Annex A (informative) Specific speed and suction-specific speed | Annex B (normative) Cooling water and lubrication system schematics | Annex C (normative) Hydraulic power recovery turbines | Annex D (normative) Standard baseplates | Annex E (informative) Inspector's checklist | Annex F (normative) Criteria for piping design | Annex G (informative) Materials class selection guidance | Annex H (normative) Materials and material specifications for pump parts | Annex I (normative) Lateral analysis | Annex J (normative) Determination of residual unbalance | Annex K (normative) Seal chamber runout illustrations | Annex L (informative) Vendor drawing and data requirements | Annex M (informative) Test data summary

## Retrieval Queries

- `api-610-iso-13709-centrifugal-pumps api-610 centrifugal-pump minimum-flow npsh seal driver HAZOP cause consequence safeguard recommendation`
- `api-610-iso-13709-centrifugal-pumps pump-design missing basis project data assumptions`
- `api-610-iso-13709-centrifugal-pumps AutoHAZOP graph node deviation quality gate`
- `api-610-iso-13709-centrifugal-pumps safeguard IPL independence auditability effectiveness`

## Working Boundaries

- This wiki is a derived working artifact, not a reproduction of the source.
- Use it to improve AutoHAZOP generation, review, and missing-basis detection.
- Do not quote long source passages or invent standard requirements not encoded here.
- Use exact PDF/source/project review for clause-level compliance, sizing, calculations, and acceptance criteria.

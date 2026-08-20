# API 617 Axial and Centrifugal Compressors and Expander-Compressors - Book Wiki

## Source Card

- Source slug: `api-617-centrifugal-compressors`
- Domain: `compressor-design`
- Tags: `api-617`, `compressor`, `surge`, `seal`, `driver`, `vibration`, `lube-oil`
- Primary procedural skill: `hazop-hazan-study-leader`
- Topic wiki: `compressor-design-operation`
- Detailed standard reference: `none`
- Working quality: controlled-use qualitative guidance; verify numeric, tabular, and clause-level decisions from project/source basis.
- Source quality: metadata extraction warning: PdfStreamError('Stream has ended unexpectedly')
- Source file: `G:\.shortcut-targets-by-id\1B9dVATZu7Jx-iYIRt0KSwjnMzhv4w10U\2026_Thananchanai_Nin\SCGC\Lrarning Data\3.Standards, Codes & Methodology\Equipment Design Standards\API-617-2022.pdf`

## Alternate Source PDFs

- none

## What This Source Contributes

Improve HAZOP rows for compressors by forcing anti-surge/recycle, suction/discharge, seals, driver, lube/seal oil, vibration, and protection logic into cause/consequence/safeguard quality.

## Decision Lens

Use compressor operating/design envelope to challenge surge, overspeed, high discharge pressure, seal failure, lube-oil failure, vibration, recycle/anti-surge, and trip logic.

## Source-Derived Checks

- Identify compressor type, service, suction/discharge conditions, driver, seal system, lube/seal oil, anti-surge/recycle path, vibration monitoring, trip logic, and relief/depressuring path.
- Separate process causes from protection trips and anti-surge safeguards.
- Check whether surge, overspeed, blocked discharge, high temperature, seal failure, or utility loss is credible for the selected node.

## HAZOP Injection Pattern

1. Identify whether the current node/deviation touches this source's domain.
2. Improve cause wording so it names the failed item, failure mode, human task, operating phase, or design-envelope exceedance.
3. Improve consequence wording so it describes the unmitigated event path before safeguards.
4. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
5. Convert missing source/project data into a precise recommendation.
6. Do not reduce risk or claim IPL credit unless the specific project basis is supplied.

## Sharp Questions

- [ ] Identify compressor type, service, suction/discharge conditions, driver, seal system, lube/seal oil, anti-surge/recycle path, vibration monitoring, trip logic, and relief/depressuring path.
- [ ] Separate process causes from protection trips and anti-surge safeguards.
- [ ] Check whether surge, overspeed, blocked discharge, high temperature, seal failure, or utility loss is credible for the selected node.
- [ ] Compressor datasheet
- [ ] Anti-surge/recycle control narrative
- [ ] Seal/lube-oil system basis
- [ ] Trip setpoints/actions
- [ ] Relief/depressuring basis
- [ ] Vibration/driver data

## Anti-Patterns To Kill

- Using generic compressor failure without failure mode or operating envelope.
- Crediting anti-surge/trip logic without sensor, controller, final element, setpoint/action, and test basis.

## Row Moves

- Convert 'compressor failure' into surge, trip, fail-to-start, seal failure, lube-oil failure, vibration, overspeed, or blocked discharge scenario.
- Route severe high-pressure rows to relief/depressuring review.

## Recommendation Logic

- Verify anti-surge/recycle and trip logic before crediting compressor safeguards.
- Request compressor datasheet and control narrative for compressor-node HAZOP rows.

## Missing-Basis Checklist

- [ ] Compressor datasheet
- [ ] Anti-surge/recycle control narrative
- [ ] Seal/lube-oil system basis
- [ ] Trip setpoints/actions
- [ ] Relief/depressuring basis
- [ ] Vibration/driver data
- [ ] Use the P&ID/process graph and supplied project data as controlling evidence.
- [ ] Keep normal operation, design limits, safe operating limits, and protection layers separate.
- [ ] Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- [ ] Do not treat a standard/book statement as proof that a safeguard exists in the project.
- [ ] Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- [ ] Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Source Navigation Preview

No usable outline/bookmark preview extracted; use this wiki as a derived working guide and verify detailed clauses/tables from the PDF or project basis.

## Retrieval Queries

- `api-617-centrifugal-compressors api-617 compressor surge seal driver vibration lube-oil HAZOP cause consequence safeguard recommendation`
- `api-617-centrifugal-compressors compressor-design missing basis project data assumptions`
- `api-617-centrifugal-compressors AutoHAZOP graph node deviation quality gate`
- `api-617-centrifugal-compressors safeguard IPL independence auditability effectiveness`

## Working Boundaries

- This wiki is a derived working artifact, not a reproduction of the source.
- Use it to improve AutoHAZOP generation, review, and missing-basis detection.
- Do not quote long source passages or invent standard requirements not encoded here.
- Use exact PDF/source/project review for clause-level compliance, sizing, calculations, and acceptance criteria.

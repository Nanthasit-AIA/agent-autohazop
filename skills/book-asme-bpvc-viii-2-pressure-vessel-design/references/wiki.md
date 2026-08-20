# ASME BPVC Section VIII Division 2 Pressure Vessel Design - Book Wiki

## Source Card

- Source slug: `asme-bpvc-viii-2-pressure-vessel-design`
- Domain: `pressure-vessel`
- Tags: `asme-viii-2`, `pressure-vessel`, `mawp`, `mdmt`, `fatigue`, `test-pressure`
- Primary procedural skill: `relief-effluent-fire-explosion-consequence`
- Topic wiki: `pressure-vessel-design`
- Detailed standard reference: `autohazop-agent-pack/references/standards/asme-bpvc-viii-2-pressure-vessel-design.md`
- Working quality: controlled-use qualitative guidance; verify numeric, tabular, and clause-level decisions from project/source basis.
- Source quality: metadata extraction warning: PdfStreamError('Stream has ended unexpectedly')
- Source file: `G:\.shortcut-targets-by-id\1B9dVATZu7Jx-iYIRt0KSwjnMzhv4w10U\2026_Thananchanai_Nin\SCGC\Lrarning Data\ASME BPVC VIII-2 ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf`

## Alternate Source PDFs

- none

## What This Source Contributes

Support vessel HAZOP rows where the consequence depends on MAWP/MDMT/design temperature, cyclic service, overpressure protection, testing, fatigue, or mechanical integrity basis.

## Decision Lens

Use pressure vessel design envelope to challenge overpressure, vacuum, temperature, brittle fracture, fatigue, corrosion allowance, and testing assumptions.

## Source-Derived Checks

- Identify vessel code basis, MAWP, design pressure/temperature, MDMT, corrosion allowance, relief basis, cyclic/fatigue service, and test/inspection evidence.
- Separate normal operating pressure from design pressure and relief set pressure.
- Route overpressure rows to API 520/521 or relief/consequence review before crediting relief protection.

## HAZOP Injection Pattern

1. Identify whether the current node/deviation touches this source's domain.
2. Improve cause wording so it names the failed item, failure mode, human task, operating phase, or design-envelope exceedance.
3. Improve consequence wording so it describes the unmitigated event path before safeguards.
4. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
5. Convert missing source/project data into a precise recommendation.
6. Do not reduce risk or claim IPL credit unless the specific project basis is supplied.

## Sharp Questions

- [ ] Identify vessel code basis, MAWP, design pressure/temperature, MDMT, corrosion allowance, relief basis, cyclic/fatigue service, and test/inspection evidence.
- [ ] Separate normal operating pressure from design pressure and relief set pressure.
- [ ] Route overpressure rows to API 520/521 or relief/consequence review before crediting relief protection.
- [ ] Vessel datasheet
- [ ] MAWP/design pressure
- [ ] Design temperature/MDMT
- [ ] Corrosion allowance
- [ ] Relief/design code basis
- [ ] Inspection/test records

## Anti-Patterns To Kill

- Writing vessel rupture without pressure/temperature/design-envelope basis.
- Using PSV as proof of adequate protection without protected equipment and relief-case evidence.

## Row Moves

- Convert 'high pressure damages vessel' into explicit exceedance of MAWP, relief demand, brittle fracture, fatigue, or LOPC path.
- Flag missing vessel datasheet when severity depends on design envelope.

## Recommendation Logic

- Request vessel mechanical design basis before finalizing overpressure/vacuum severity.
- Verify relief protection and inspection/test basis for credible pressure excursions.

## Missing-Basis Checklist

- [ ] Vessel datasheet
- [ ] MAWP/design pressure
- [ ] Design temperature/MDMT
- [ ] Corrosion allowance
- [ ] Relief/design code basis
- [ ] Inspection/test records
- [ ] Use the P&ID/process graph and supplied project data as controlling evidence.
- [ ] Keep normal operation, design limits, safe operating limits, and protection layers separate.
- [ ] Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- [ ] Do not treat a standard/book statement as proof that a safeguard exists in the project.
- [ ] Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- [ ] Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Source Navigation Preview

No usable outline/bookmark preview extracted; use this wiki as a derived working guide and verify detailed clauses/tables from the PDF or project basis.

## Retrieval Queries

- `asme-bpvc-viii-2-pressure-vessel-design asme-viii-2 pressure-vessel mawp mdmt fatigue test-pressure HAZOP cause consequence safeguard recommendation`
- `asme-bpvc-viii-2-pressure-vessel-design pressure-vessel missing basis project data assumptions`
- `asme-bpvc-viii-2-pressure-vessel-design AutoHAZOP graph node deviation quality gate`
- `asme-bpvc-viii-2-pressure-vessel-design safeguard IPL independence auditability effectiveness`

## Working Boundaries

- This wiki is a derived working artifact, not a reproduction of the source.
- Use it to improve AutoHAZOP generation, review, and missing-basis detection.
- Do not quote long source passages or invent standard requirements not encoded here.
- Use exact PDF/source/project review for clause-level compliance, sizing, calculations, and acceptance criteria.

# API 521 Pressure-Relieving and Depressuring Systems - Book Wiki

## Source Card

- Source slug: `api-521-pressure-relieving-depressuring-systems`
- Domain: `relief-depressuring`
- Tags: `api-521`, `overpressure`, `depressuring`, `flare`, `blocked-outlet`, `fire-case`
- Primary procedural skill: `relief-effluent-fire-explosion-consequence`
- Topic wiki: `relief-depressuring-systems`
- Detailed standard reference: `autohazop-agent-pack/references/standards/api-521-pressure-relieving-depressuring-systems.md`
- Working quality: controlled-use qualitative guidance; verify numeric, tabular, and clause-level decisions from project/source basis.
- Source quality: pages: 206; outline/bookmark count: 59
- Source file: `G:\.shortcut-targets-by-id\1B9dVATZu7Jx-iYIRt0KSwjnMzhv4w10U\2026_Thananchanai_Nin\SCGC\Lrarning Data\ANSIAPI Standard 521 Pressure-relieving and Depressuring Systems (5th ed.) (American Petroleum Institute) (z-library.sk, 1lib.sk, z-lib.sk).pdf`

## Alternate Source PDFs

- none

## What This Source Contributes

Improve HAZOP/LOPA rows where overpressure, relief, depressuring, flare/vent/effluent destination, fire exposure, thermal expansion, or tube rupture may drive consequence or safeguard adequacy.

## Decision Lens

Use API 521 relief-system context to challenge credible overpressure scenarios, depressuring, flare/vent disposal, fire case, blocked outlet, utility failure, and exchanger tube rupture.

## Source-Derived Checks

- Identify credible overpressure scenario, protected equipment, relief path, disposal system, blocked outlet/fire/utility/tube rupture/thermal expansion basis, and simultaneous scenario rules.
- Check whether relief discharge creates downstream flare, vent, scrubber, sewer, or occupied-area consequences.
- Do not use API 521 to invent relief capacity; request calculation/design basis.

## HAZOP Injection Pattern

1. Identify whether the current node/deviation touches this source's domain.
2. Improve cause wording so it names the failed item, failure mode, human task, operating phase, or design-envelope exceedance.
3. Improve consequence wording so it describes the unmitigated event path before safeguards.
4. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
5. Convert missing source/project data into a precise recommendation.
6. Do not reduce risk or claim IPL credit unless the specific project basis is supplied.

## Sharp Questions

- [ ] Identify credible overpressure scenario, protected equipment, relief path, disposal system, blocked outlet/fire/utility/tube rupture/thermal expansion basis, and simultaneous scenario rules.
- [ ] Check whether relief discharge creates downstream flare, vent, scrubber, sewer, or occupied-area consequences.
- [ ] Do not use API 521 to invent relief capacity; request calculation/design basis.
- [ ] Relief-case list
- [ ] Protected equipment
- [ ] Relief sizing basis
- [ ] Flare/vent/disposal capacity
- [ ] Backpressure
- [ ] Fire/tube rupture/utility failure assumptions

## Anti-Patterns To Kill

- Crediting relief without naming the credible overpressure case.
- Mixing relief system failure into consequence text as a second failure without basis.

## Row Moves

- For high pressure rows, identify whether blocked outlet, external fire, control valve failure, utility failure, tube rupture, or thermal expansion is the scenario.
- Add recommendation to verify relief/depressuring design when HAZOP row exceeds design envelope.

## Recommendation Logic

- Request API 521 relief-case verification for each credible overpressure row.
- Verify discharge destination and downstream consequence before crediting relief safeguards.

## Missing-Basis Checklist

- [ ] Relief-case list
- [ ] Protected equipment
- [ ] Relief sizing basis
- [ ] Flare/vent/disposal capacity
- [ ] Backpressure
- [ ] Fire/tube rupture/utility failure assumptions
- [ ] Use the P&ID/process graph and supplied project data as controlling evidence.
- [ ] Keep normal operation, design limits, safe operating limits, and protection layers separate.
- [ ] Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- [ ] Do not treat a standard/book statement as proof that a safeguard exists in the project.
- [ ] Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- [ ] Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Source Navigation Preview

Cover | Special Notes | API Foreword | Contents | Foreword | Introduction | 1 Scope | 2 Normative references | 3 Terms and definitions | 4 Causes of overpressure | 4.1 General | 4.2 Overpressure protection philosophy | 4.3 Potentials for overpressure | 4.4 Recommended minimum relief system design content | 4.5 List of items required in flare-header calculation documentation | 4.6 Guidance on vacuum relief | 5 Determination of individual relieving rates | 5.1 Principal sources of overpressure | 5.2 Sources of overpressure | 5.3 Effects of pressure, temperature, and composition | 5.4 Effect of operator response | 5.5 Closed outlets | 5.6 Cooling or reflux failure | 5.7 Absorbent flow failure | 5.8 Accumulation of non condensables | 5.9 Entrance of volatile material into the system | 5.10 Failure of process stream automatic controls | 5.11 Abnormal process heat input | 5.12 Internal explosion (excluding detonation) | 5.13 Chemical reaction | 5.14 Hydraulic expansion | 5.15 External pool fires | 5.16 Jet fires | 5.17 Opening manual valves | 5.18 Electric power failure | 5.19 Heat-transfer equipment failure | 5.20 Vapour depressuring | 5.21 Special considerations for individual pressure-relief devices | 5.22 Dynamic simulation | 5.23 Overfilling process or surge vessel | 6 Selection of disposal systems | 6.1 General | 6.2 Fluid properties that influence design | 6.3 Atmospheric discharge | 6.4 Disposal by flaring | 6.5 Disposal to a lower-pressure system | 6.6 Disposal of liquids and condensable vapours | 6.7 Disposal through common vent stack | 7 Disposal systems | 7.1 Definition of system design load | 7.2 System arrangement | 7.3 Design of disposal system components | 7.4 Flare gas recovery systems | Annex A (informative) Determination of fire relief requirements | Annex B (informative) Special system design considerations | Annex C (informative) Sample calculations for sizing a subsonic flare stack | Annex D (informative) Typical details and sketches | Annex E (informative) High integrity protection systems (HIPS) | Bibliography

## Retrieval Queries

- `api-521-pressure-relieving-depressuring-systems api-521 overpressure depressuring flare blocked-outlet fire-case HAZOP cause consequence safeguard recommendation`
- `api-521-pressure-relieving-depressuring-systems relief-depressuring missing basis project data assumptions`
- `api-521-pressure-relieving-depressuring-systems AutoHAZOP graph node deviation quality gate`
- `api-521-pressure-relieving-depressuring-systems safeguard IPL independence auditability effectiveness`

## Working Boundaries

- This wiki is a derived working artifact, not a reproduction of the source.
- Use it to improve AutoHAZOP generation, review, and missing-basis detection.
- Do not quote long source passages or invent standard requirements not encoded here.
- Use exact PDF/source/project review for clause-level compliance, sizing, calculations, and acceptance criteria.

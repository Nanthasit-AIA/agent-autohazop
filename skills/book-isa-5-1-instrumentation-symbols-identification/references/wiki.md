# ISA 5.1 Instrumentation Symbols and Identification - Book Wiki

## Source Card

- Source slug: `isa-5-1-instrumentation-symbols-identification`
- Domain: `instrument-symbols`
- Tags: `isa-5-1`, `instrument-tag`, `loop`, `p&id-symbol`, `signal`, `control`
- Primary procedural skill: `hazop-hazan-study-leader`
- Topic wiki: `instrument-symbols-identification`
- Detailed standard reference: `none`
- Working quality: controlled-use qualitative guidance; verify numeric, tabular, and clause-level decisions from project/source basis.
- Source quality: pages: 293; outline/bookmark count: 175
- Source file: `G:\.shortcut-targets-by-id\1B9dVATZu7Jx-iYIRt0KSwjnMzhv4w10U\2026_Thananchanai_Nin\SCGC\Lrarning Data\Instrumentation Symbols and Identification (Instrument Society Of America) (z-library.sk, 1lib.sk, z-lib.sk).pdf`

## Alternate Source PDFs

- none

## What This Source Contributes

Support graph extraction and HAZOP rows where instrument tag meaning, loop function, signal type, control/alarm/interlock role, or symbol interpretation affects cause/safeguard logic.

## Decision Lens

Use ISA instrument tag/symbol conventions to improve P&ID extraction, instrument function classification, and loop/control/safeguard interpretation.

## Source-Derived Checks

- Parse tag letters, loop numbers, shared functions, instrument location, signal type, and functional role before using an instrument in cause or safeguard text.
- Separate indication, alarm, control, shutdown, permissive, interlock, and SIS functions.
- Do not infer safety function or fail action from tag letters alone.

## HAZOP Injection Pattern

1. Identify whether the current node/deviation touches this source's domain.
2. Improve cause wording so it names the failed item, failure mode, human task, operating phase, or design-envelope exceedance.
3. Improve consequence wording so it describes the unmitigated event path before safeguards.
4. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
5. Convert missing source/project data into a precise recommendation.
6. Do not reduce risk or claim IPL credit unless the specific project basis is supplied.

## Sharp Questions

- [ ] Parse tag letters, loop numbers, shared functions, instrument location, signal type, and functional role before using an instrument in cause or safeguard text.
- [ ] Separate indication, alarm, control, shutdown, permissive, interlock, and SIS functions.
- [ ] Do not infer safety function or fail action from tag letters alone.
- [ ] P&ID legend
- [ ] Instrument index
- [ ] Loop diagram
- [ ] Control narrative
- [ ] Cause-and-effect chart
- [ ] Signal/fail action

## Anti-Patterns To Kill

- Calling any instrument an interlock or IPL without cause-and-effect evidence.
- Using transmitter failure on a node where the instrument does not measure the selected parameter.

## Row Moves

- Map each instrument to measured variable and action before allowing it as cause or safeguard.
- Convert ambiguous tag interpretation into missing-basis request for legend, loop diagram, or control narrative.

## Recommendation Logic

- Request instrument index/loop diagram for unclear instrument roles.
- Verify tag function before crediting alarms, trips, or control actions.

## Missing-Basis Checklist

- [ ] P&ID legend
- [ ] Instrument index
- [ ] Loop diagram
- [ ] Control narrative
- [ ] Cause-and-effect chart
- [ ] Signal/fail action
- [ ] Use the P&ID/process graph and supplied project data as controlling evidence.
- [ ] Keep normal operation, design limits, safe operating limits, and protection layers separate.
- [ ] Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- [ ] Do not treat a standard/book statement as proof that a safeguard exists in the project.
- [ ] Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- [ ] Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Source Navigation Preview

Refining Processes Home | Refining Processes Index | Company Index | Equipment and Services providers | Processes index | Alkylation | Alkylation | Alkylation | Alkylation | Alkylation | Alkylation | Alkylation, catalytic | Alkylation, sulfuric acid | Alkylation—feed preparation | Alkylation—HF | Aromatics | Aromatics extractive distillation | Aromatics recovery | Asphalt—oxidation | Benzene reduction | Catalytic cracking (MSCC) | Catalytic dewaxing | Catalytic reforming | Catalytic reforming | Catalytic reforming | Coking | Coking | Coking, flexi | Coking, fluid | Crude distillation | Crude distillation | Crude distillation | Crude topping units | Deasphalting | Deasphalting | Deep catalytic cracking | Deep thermal conversion | Desulfurization | Desulfurization | Dewaxing | Dewaxing | Dewaxing/wax deoiling | Diesel upgrading | Diesel—ultra-low-sulfur diesel (ULSD) | Electrical desalting | Ethers | Ethers | Ethers—ETBE | Ethers—MTBE | Fluid catalytic cracking | Fluid catalytic cracking | Fluid catalytic cracking | Fluid catalytic cracking | Fluid catalytic cracking | Fluid catalytic cracking | Fluid catalytic cracking—pretreatment | Gas treating—H2S removal | Gasification | Gasification | Gasification

## Retrieval Queries

- `isa-5-1-instrumentation-symbols-identification isa-5-1 instrument-tag loop p&id-symbol signal control HAZOP cause consequence safeguard recommendation`
- `isa-5-1-instrumentation-symbols-identification instrument-symbols missing basis project data assumptions`
- `isa-5-1-instrumentation-symbols-identification AutoHAZOP graph node deviation quality gate`
- `isa-5-1-instrumentation-symbols-identification safeguard IPL independence auditability effectiveness`

## Working Boundaries

- This wiki is a derived working artifact, not a reproduction of the source.
- Use it to improve AutoHAZOP generation, review, and missing-basis detection.
- Do not quote long source passages or invent standard requirements not encoded here.
- Use exact PDF/source/project review for clause-level compliance, sizing, calculations, and acceptance criteria.

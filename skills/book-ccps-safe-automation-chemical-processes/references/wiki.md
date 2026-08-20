# CCPS Guidelines for Safe Automation of Chemical Processes - Book Wiki

## Source Card

- Source slug: `ccps-safe-automation-chemical-processes`
- Domain: `automation-sis-bpcs`
- Tags: `safe-automation`, `bpcs`, `alarm`, `interlock`, `sis`, `cause-and-effect`, `bypass`
- Primary procedural skill: `sis-sil-verification-reliability`
- Topic wiki: `safe-automation`
- Detailed standard reference: `autohazop-agent-pack/references/standards/ccps-safe-automation-chemical-processes.md`
- Working quality: controlled-use qualitative guidance; verify numeric, tabular, and clause-level decisions from project/source basis.
- Source quality: pages: 441
- Source file: `G:\.shortcut-targets-by-id\1B9dVATZu7Jx-iYIRt0KSwjnMzhv4w10U\2026_Thananchanai_Nin\SCGC\Lrarning Data\Guidelines for Safe Automation of Chemical Processes (Center for Chemical Process Safety (CCPS) (z-library.sk, 1lib.sk, z-lib.sk).pdf`

## Alternate Source PDFs

- none

## What This Source Contributes

Prevent HAZOP rows from misusing interlocks/alarms/SIS as generic causes or safeguards; force cause-and-effect, fail-safe action, bypass management, and independence evidence.

## Decision Lens

Use safe automation lifecycle logic to classify BPCS, alarms, interlocks, SIS/SIF, cause-and-effect, bypass, diagnostics, FAT/SAT, and independence assumptions.

## Source-Derived Checks

- Classify each automation element as BPCS, alarm/operator action, interlock/trip, SIS/SIF, permissive, shutdown, or final element.
- Identify sensor, logic solver/controller, final element, setpoint, action, safe state, reset, bypass, diagnostics, and test/validation basis.
- Separate spurious trip as initiating event from failure-on-demand as IPL evidence; do not mix both in one HAZOP row.

## HAZOP Injection Pattern

1. Identify whether the current node/deviation touches this source's domain.
2. Improve cause wording so it names the failed item, failure mode, human task, operating phase, or design-envelope exceedance.
3. Improve consequence wording so it describes the unmitigated event path before safeguards.
4. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
5. Convert missing source/project data into a precise recommendation.
6. Do not reduce risk or claim IPL credit unless the specific project basis is supplied.

## Sharp Questions

- [ ] Classify each automation element as BPCS, alarm/operator action, interlock/trip, SIS/SIF, permissive, shutdown, or final element.
- [ ] Identify sensor, logic solver/controller, final element, setpoint, action, safe state, reset, bypass, diagnostics, and test/validation basis.
- [ ] Separate spurious trip as initiating event from failure-on-demand as IPL evidence; do not mix both in one HAZOP row.
- [ ] Cause-and-effect chart
- [ ] Control narrative
- [ ] Trip setpoint/action
- [ ] Fail-safe position
- [ ] Bypass/MOC record
- [ ] Proof-test/validation evidence
- [ ] BPCS/SIS independence

## Anti-Patterns To Kill

- Using 'interlock fails' as a cause after another initiating event has already occurred.
- Crediting BPCS/alarm/interlock as IPL without independence, timing, audit, and proof-test evidence.
- Treating a valve fail position as known when the P&ID/process description does not state it.

## Row Moves

- Rewrite automation causes as false trip, failure to act on demand, loss of signal, sensor fault, logic fault, final-element fault, or bypassed state.
- Move protection-layer failure from consequence text into IPL missing-basis review.

## Recommendation Logic

- Request cause-and-effect and control narrative for all credited trips/interlocks.
- Create SIF/SIS verification action when the row relies on safety automation as IPL.

## Missing-Basis Checklist

- [ ] Cause-and-effect chart
- [ ] Control narrative
- [ ] Trip setpoint/action
- [ ] Fail-safe position
- [ ] Bypass/MOC record
- [ ] Proof-test/validation evidence
- [ ] BPCS/SIS independence
- [ ] Use the P&ID/process graph and supplied project data as controlling evidence.
- [ ] Keep normal operation, design limits, safe operating limits, and protection layers separate.
- [ ] Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- [ ] Do not treat a standard/book statement as proof that a safeguard exists in the project.
- [ ] Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- [ ] Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Source Navigation Preview

No usable outline/bookmark preview extracted; use this wiki as a derived working guide and verify detailed clauses/tables from the PDF or project basis.

## Retrieval Queries

- `ccps-safe-automation-chemical-processes safe-automation bpcs alarm interlock sis cause-and-effect bypass HAZOP cause consequence safeguard recommendation`
- `ccps-safe-automation-chemical-processes automation-sis-bpcs missing basis project data assumptions`
- `ccps-safe-automation-chemical-processes AutoHAZOP graph node deviation quality gate`
- `ccps-safe-automation-chemical-processes safeguard IPL independence auditability effectiveness`

## Working Boundaries

- This wiki is a derived working artifact, not a reproduction of the source.
- Use it to improve AutoHAZOP generation, review, and missing-basis detection.
- Do not quote long source passages or invent standard requirements not encoded here.
- Use exact PDF/source/project review for clause-level compliance, sizing, calculations, and acceptance criteria.

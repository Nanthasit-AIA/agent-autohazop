# CCPS Layer of Protection Analysis - Simplified Process Risk Assessment - Book Wiki

## Source Card

- Source slug: `ccps-layer-of-protection-analysis-simplified`
- Domain: `lopa-core`
- Tags: `lopa`, `simplified-risk-assessment`, `initiating-event`, `ipl`, `pfd`, `risk-tolerance`
- Primary procedural skill: `lopa-iel-conditional-modifier`
- Topic wiki: `lopa-core-simplified-risk-assessment`
- Detailed standard reference: `none`
- Working quality: controlled-use qualitative guidance; verify numeric, tabular, and clause-level decisions from project/source basis.
- Source quality: pages: 280
- Source file: `G:\.shortcut-targets-by-id\1B9dVATZu7Jx-iYIRt0KSwjnMzhv4w10U\2026_Thananchanai_Nin\SCGC\Lrarning Data\3.Standards, Codes & Methodology\Safety Instrumented System Standards\Layer_of_Protection_Analysis.pdf`

## Alternate Source PDFs

- none

## What This Source Contributes

Make LOPA discipline explicit in AutoHAZOP so safeguards, IPLs, initiating event frequencies, conditional modifiers, and final risk are not mixed or guessed.

## Decision Lens

Use the core LOPA method to normalize HAZOP rows into one initiating event, one consequence, enabling conditions, conditional modifiers, safeguards, candidate IPLs, credited IPLs, and residual risk.

## Source-Derived Checks

- Normalize one scenario: initiating event, consequence, enabling conditions, conditional modifiers, safeguards, candidate IPLs, credited IPLs, and risk criterion.
- Credit IPLs only when independent, effective, auditable, and supported by PFD/credit basis.
- Do not reduce likelihood using safeguards that are dependent on the initiating event or each other.

## HAZOP Injection Pattern

1. Identify whether the current node/deviation touches this source's domain.
2. Improve cause wording so it names the failed item, failure mode, human task, operating phase, or design-envelope exceedance.
3. Improve consequence wording so it describes the unmitigated event path before safeguards.
4. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
5. Convert missing source/project data into a precise recommendation.
6. Do not reduce risk or claim IPL credit unless the specific project basis is supplied.

## Sharp Questions

- [ ] Normalize one scenario: initiating event, consequence, enabling conditions, conditional modifiers, safeguards, candidate IPLs, credited IPLs, and risk criterion.
- [ ] Credit IPLs only when independent, effective, auditable, and supported by PFD/credit basis.
- [ ] Do not reduce likelihood using safeguards that are dependent on the initiating event or each other.
- [ ] Project LOPA procedure
- [ ] Risk tolerance criteria
- [ ] Initiating event frequency
- [ ] Conditional modifier basis
- [ ] IPL PFD/credit
- [ ] Independence/auditability evidence

## Anti-Patterns To Kill

- Using HAZOP safeguards as credited IPLs by default.
- Putting 'if interlock fails' in the unmitigated consequence.
- Assigning final likelihood without IEL, conditional modifier, and IPL PFD basis.

## Row Moves

- Convert HAZOP row into LOPA scenario table before final risk reduction.
- Classify each safeguard as non-IPL safeguard, candidate IPL, credited IPL, or missing evidence.
- Block final risk where project risk tolerance or PFD data is missing.

## Recommendation Logic

- Add LOPA readiness review for high-risk HAZOP rows.
- Document why each safeguard is or is not a credited IPL.

## Missing-Basis Checklist

- [ ] Project LOPA procedure
- [ ] Risk tolerance criteria
- [ ] Initiating event frequency
- [ ] Conditional modifier basis
- [ ] IPL PFD/credit
- [ ] Independence/auditability evidence
- [ ] Use the P&ID/process graph and supplied project data as controlling evidence.
- [ ] Keep normal operation, design limits, safe operating limits, and protection layers separate.
- [ ] Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- [ ] Do not treat a standard/book statement as proof that a safeguard exists in the project.
- [ ] Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- [ ] Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Source Navigation Preview

No usable outline/bookmark preview extracted; use this wiki as a derived working guide and verify detailed clauses/tables from the PDF or project basis.

## Retrieval Queries

- `ccps-layer-of-protection-analysis-simplified lopa simplified-risk-assessment initiating-event ipl pfd risk-tolerance HAZOP cause consequence safeguard recommendation`
- `ccps-layer-of-protection-analysis-simplified lopa-core missing basis project data assumptions`
- `ccps-layer-of-protection-analysis-simplified AutoHAZOP graph node deviation quality gate`
- `ccps-layer-of-protection-analysis-simplified safeguard IPL independence auditability effectiveness`

## Working Boundaries

- This wiki is a derived working artifact, not a reproduction of the source.
- Use it to improve AutoHAZOP generation, review, and missing-basis detection.
- Do not quote long source passages or invent standard requirements not encoded here.
- Use exact PDF/source/project review for clause-level compliance, sizing, calculations, and acceptance criteria.

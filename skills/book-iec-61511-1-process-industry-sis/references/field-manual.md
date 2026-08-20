# Field Manual - IEC 61511-1 Functional Safety - SIS for the Process Industry Sector

This is the dense working guide for `book-iec-61511-1-process-industry-sis`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `iec-61511-1-process-industry-sis`
- Domain family: `sis-lifecycle`
- Pages: 81
- Source quality: pages: 81; outline/bookmark count: 109
- Primary shared skill: `sis-sil-verification-reliability`
- Detailed reference: `none`
- Source purpose: Review whether a safety instrumented function can be credited in LOPA or HAZOP based on lifecycle evidence rather than an interlock label.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Define SIF, safe state, demand mode, process safety time, sensors, logic solver, final elements, target SIL/PFD, proof-test interval, diagnostics, bypass, and reset philosophy.
- [ ] Separate SIL target selection from SIL verification and validation evidence.
- [ ] Check independence from BPCS and other credited IPLs.

## Anti-Patterns To Kill

- Calling an interlock a SIS/SIF without SRS, target SIL, verification, validation, and proof-test basis.
- Using the same sensor/final element in BPCS initiating event and credited SIF without dependency review.

## Row Moves

- Move unsupported SIS credit into candidate IPL with missing lifecycle evidence.
- Convert automation recommendation into a defined SIF/SRS action when risk reduction is required.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- SIF list
- SRS
- Target SIL/PFD
- Proof-test interval/procedure
- Validation record
- Bypass/MOC record
- BPCS/SIS independence

## Specialist Handoff

- Hand off to `sis-sil-verification-reliability` when the row needs the primary shared workflow.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision
- Source basis
- HAZOP impact
- Missing basis
- Confidence tier

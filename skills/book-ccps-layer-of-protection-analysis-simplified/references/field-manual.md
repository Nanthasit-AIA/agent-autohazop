# Field Manual - CCPS Layer of Protection Analysis - Simplified Process Risk Assessment

This is the dense working guide for `book-ccps-layer-of-protection-analysis-simplified`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `ccps-layer-of-protection-analysis-simplified`
- Domain family: `lopa-core`
- Pages: 280
- Source quality: pages: 280
- Primary shared skill: `lopa-iel-conditional-modifier`
- Detailed reference: `none`
- Source purpose: Make LOPA discipline explicit in AutoHAZOP so safeguards, IPLs, initiating event frequencies, conditional modifiers, and final risk are not mixed or guessed.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Normalize one scenario: initiating event, consequence, enabling conditions, conditional modifiers, safeguards, candidate IPLs, credited IPLs, and risk criterion.
- [ ] Credit IPLs only when independent, effective, auditable, and supported by PFD/credit basis.
- [ ] Do not reduce likelihood using safeguards that are dependent on the initiating event or each other.

## Anti-Patterns To Kill

- Using HAZOP safeguards as credited IPLs by default.
- Putting 'if interlock fails' in the unmitigated consequence.
- Assigning final likelihood without IEL, conditional modifier, and IPL PFD basis.

## Row Moves

- Convert HAZOP row into LOPA scenario table before final risk reduction.
- Classify each safeguard as non-IPL safeguard, candidate IPL, credited IPL, or missing evidence.
- Block final risk where project risk tolerance or PFD data is missing.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- Project LOPA procedure
- Risk tolerance criteria
- Initiating event frequency
- Conditional modifier basis
- IPL PFD/credit
- Independence/auditability evidence

## Specialist Handoff

- Hand off to `lopa-iel-conditional-modifier` when the row needs the primary shared workflow.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision
- Source basis
- HAZOP impact
- Missing basis
- Confidence tier

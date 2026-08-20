# Field Manual - OREDA Offshore Reliability Data Handbook

This is the dense working reference for `book-oreda-offshore-reliability-data-handbook`. It is a derived guide for AutoHAZOP use, not a reproduction of the source. Use it to ask sharper questions, reject weak worksheet logic, and produce evidence-aware recommendations.

## Source Status

- Source slug: `oreda-offshore-reliability-data-handbook`
- Domain family: `reliability`
- Confidence tier: screening-only - Use for routing, gap prompts, and missing-basis checks only until the source wiki is enriched from page-level reading.
- Pages: 835
- Usable text pages indexed: 0
- Indexed text characters: 0
- Top evidence signals: no indexed topic hits
- Primary shared skill: `reliability-data-selection`
- Secondary shared skills: none
- Source purpose: Use the source to challenge reliability and failure-rate assumptions for applicability and uncertainty.

## Source Navigation Hooks

- oreda0409.pdf
- oreda0410.pdf
- oreda0411.pdf
- oreda0412.pdf
- oreda0413.pdf
- oreda0414.pdf
- oreda0415.pdf
- oreda0416.pdf
- oreda0417.pdf
- oreda0418.pdf
- oreda0419.pdf
- oreda0420.pdf
- oreda0421.pdf
- oreda0422.pdf
- oreda0423.pdf
- oreda0424.pdf
- oreda0425.pdf
- Binder2.pdf

## High-Signal Page Anchors

| Page | Hits | Topics | Use |
|---:|---:|---|---|
| none | 0 | none | No indexed page evidence; use only screening logic. |

## Topic Capsules

- No indexed topic capsule is available. Keep outputs at screening level and request source enrichment.

## How To Attack A HAZOP Row

1. Match the row to the strongest topic signal above.
2. State whether this book is primary evidence, secondary support, or screening-only for the decision.
3. Rewrite the cause to name the failed item, failure mode, human/organizational condition, external event, or initiating event.
4. Rewrite the consequence as the unmitigated event path before safeguards.
5. Challenge every safeguard for independence, timing, effectiveness, auditability, and evidence.
6. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- What equipment boundary, failure mode, service, duty cycle, environment, and maintenance context does the data represent?
- Is the data being used for HAZOP screening, LOPA frequency, QRA model, SIS verification, or mechanical integrity?
- Are common-cause, proof-test, inspection interval, repair time, demand rate, and uncertainty visible?
- Does the source match the plant equipment class closely enough to use the value?

## Anti-Patterns To Kill

- Copying handbook values into calculations without applicability review.
- Mixing failure rate, demand probability, PFDavg, PFH, and unavailability as if interchangeable.
- Ignoring common cause or inspection/proof-test assumptions.

## Row Moves

- Name the failure mode before requesting or applying data.
- Classify data as screening, project-approved, vendor-specific, or blocked.
- Route SIS data assumptions to SIF verification when they affect SIL/PFD.

## Hard Decision Gates

- Whether the equipment class, service, duty cycle, environment, failure mode, and data source match.
- Whether data are being used for screening, LOPA/SIL verification, QRA, maintenance, or mechanical integrity.
- Whether uncertainty, confidence, common cause, and inspection/proof-test assumptions are visible.

## Missing-Basis Triggers

- Equipment taxonomy and failure mode
- Operating/service context
- Approved reliability data source
- Proof-test/inspection interval
- Uncertainty and common-cause basis
- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Specialist Handoff

- Hand off to `reliability-data-selection` when the row needs the primary shared workflow.
- No secondary shared skill is configured; use the primary shared skill or project SME handoff when needed.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision: accept, challenge, downgrade credit, request basis, or block.
- Evidence: book slug, topic signal, page-anchor range, and confidence tier.
- Worksheet impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: exact data or record needed.
- Next action: engineering calculation, project-basis request, skill handoff, field verification, or worksheet rewrite.

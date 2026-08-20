# Field Manual - ASME BPVC Section VIII Division 2 Pressure Vessel Design

This is the dense working guide for `book-asme-bpvc-viii-2-pressure-vessel-design`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `asme-bpvc-viii-2-pressure-vessel-design`
- Domain family: `pressure-vessel`
- Pages: 0
- Source quality: metadata extraction warning: PdfStreamError('Stream has ended unexpectedly')
- Primary shared skill: `relief-effluent-fire-explosion-consequence`
- Detailed reference: `autohazop-agent-pack/references/standards/asme-bpvc-viii-2-pressure-vessel-design.md`
- Source purpose: Support vessel HAZOP rows where the consequence depends on MAWP/MDMT/design temperature, cyclic service, overpressure protection, testing, fatigue, or mechanical integrity basis.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Identify vessel code basis, MAWP, design pressure/temperature, MDMT, corrosion allowance, relief basis, cyclic/fatigue service, and test/inspection evidence.
- [ ] Separate normal operating pressure from design pressure and relief set pressure.
- [ ] Route overpressure rows to API 520/521 or relief/consequence review before crediting relief protection.

## Anti-Patterns To Kill

- Writing vessel rupture without pressure/temperature/design-envelope basis.
- Using PSV as proof of adequate protection without protected equipment and relief-case evidence.

## Row Moves

- Convert 'high pressure damages vessel' into explicit exceedance of MAWP, relief demand, brittle fracture, fatigue, or LOPC path.
- Flag missing vessel datasheet when severity depends on design envelope.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- Vessel datasheet
- MAWP/design pressure
- Design temperature/MDMT
- Corrosion allowance
- Relief/design code basis
- Inspection/test records

## Specialist Handoff

- Hand off to `relief-effluent-fire-explosion-consequence` when the row needs the primary shared workflow.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision
- Source basis
- HAZOP impact
- Missing basis
- Confidence tier

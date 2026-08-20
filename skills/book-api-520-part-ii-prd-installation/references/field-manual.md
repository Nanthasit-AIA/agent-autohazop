# Field Manual - API 520 Part II Pressure-Relieving Device Installation

This is the dense working guide for `book-api-520-part-ii-prd-installation`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `api-520-part-ii-prd-installation`
- Domain family: `pressure-relief`
- Pages: 66
- Source quality: pages: 66; outline/bookmark count: 105
- Primary shared skill: `relief-effluent-fire-explosion-consequence`
- Detailed reference: `autohazop-agent-pack/references/standards/api-520-part-ii-prd-installation.md`
- Source purpose: Improve HAZOP rows where PSV/PRD is claimed as safeguard, where relief path could be isolated/blocked, or where installation details affect effectiveness.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Identify protected equipment, PRD type, set pressure, inlet/outlet piping, isolation valves, rupture disk, bonnet/pilot vent, drains, discharge destination, and backpressure basis.
- [ ] Check whether PRD installation can create chatter, excessive inlet pressure loss, outlet restriction, blocked drain, or unsafe discharge.
- [ ] Do not credit a PRD without protected-equipment and installation-basis evidence.

## Anti-Patterns To Kill

- Listing PSV as a generic safeguard without set pressure, protected equipment, relief path, and installation basis.
- Ignoring isolation valves, spectacle blinds, car seals, outlet backpressure, or fouling in relief path.

## Row Moves

- Split overpressure cause from PRD installation weakness; do not use PRD failure as the initiating event unless the deviation is relief system malfunction.
- Convert weak safeguard text into candidate IPL with missing installation/proof/inspection basis.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- PRD datasheet
- Set pressure
- Inlet/outlet piping
- Isolation/car-seal status
- Backpressure basis
- Discharge destination
- Inspection/test basis

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

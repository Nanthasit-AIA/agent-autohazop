# Field Manual - API 2000 Atmospheric and Low-Pressure Tank Venting

This is the dense working guide for `book-api-2000-atmospheric-low-pressure-tank-venting`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `api-2000-atmospheric-low-pressure-tank-venting`
- Domain family: `tank-venting`
- Pages: 88
- Source quality: pages: 88; outline/bookmark count: 64
- Primary shared skill: `relief-effluent-fire-explosion-consequence`
- Detailed reference: `autohazop-agent-pack/references/standards/api-2000-atmospheric-low-pressure-tank-venting.md`
- Source purpose: Improve atmospheric/low-pressure tank HAZOP rows involving nitrogen blanketing, PV valves, emergency vents, pump-out, thermal inbreathing, fire case, vapor recovery, and blocked vent paths.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Identify tank pressure/vacuum limits, inbreathing/outbreathing cases, liquid movement rates, thermal cases, blanketing, PV valve, emergency vent, flame arrester, and vapor recovery path.
- [ ] Check whether no/less flow, high level, low pressure, high pressure, or blocked vent scenarios exceed tank venting capacity.
- [ ] Treat PV valves and vents as safeguards only with service, sizing, inspection, and isolation/bypass basis.

## Anti-Patterns To Kill

- Claiming nitrogen blanketing prevents vacuum without inbreathing capacity basis.
- Crediting PVV/emergency vent without vent path, sizing, fouling, isolation, or fire-case basis.

## Row Moves

- For pump-out/no inlet flow rows, add missing-basis action to verify inbreathing capacity.
- For overfill/high pressure rows, separate normal outbreathing, vapor recovery, emergency venting, and relief discharge consequence.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- Tank pressure/vacuum design limits
- Fill/withdrawal rates
- Thermal venting basis
- PVV/emergency vent sizing
- Blanketing/vapor recovery basis
- Inspection/isolation status

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

# Field Manual - CCPS Guidelines for Writing Effective Operating and Maintenance Procedures

This is the dense working guide for `book-ccps-operating-maintenance-procedures`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `ccps-operating-maintenance-procedures`
- Domain family: `procedures-human-factors`
- Pages: 160
- Source quality: pages: 160; outline/bookmark count: 163
- Primary shared skill: `process-safety-management-rbps-moc-docs`
- Detailed reference: `autohazop-agent-pack/references/standards/ccps-operating-maintenance-procedures.md`
- Source purpose: Improve HAZOP rows involving startup, shutdown, maintenance isolation, valve lineup, bypass, reinstatement, sampling, draining, handover, and procedure-based safeguards.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Identify operating mode, task step, responsible role, preconditions, safe operating limits, hold points, verification, communication, and abnormal response.
- [ ] Treat procedures/training as weak safeguards unless they include a specific auditable action that interrupts the scenario.
- [ ] Manual valve causes need a real task path: lineup, isolation, reinstatement, startup, shutdown, sampling, draining, or maintenance.

## Anti-Patterns To Kill

- Generic 'operator error' or 'manual valve failure' with no task, phase, or tag.
- Recommendation only says retrain/update SOP without fixing verification, design, or procedure usability.

## Row Moves

- Rewrite human causes as wrong valve lineup, isolation not restored, bypass left open, wrong sequence, omitted verification, or handover failure.
- Move weak procedure safeguards into missing-basis recommendations for checklist/independent verification.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- Operating mode
- Procedure revision
- Task step
- Valve lineup/isolation plan
- Permit/LOTO basis
- Independent verification
- Training/competency record

## Specialist Handoff

- Hand off to `process-safety-management-rbps-moc-docs` when the row needs the primary shared workflow.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision
- Source basis
- HAZOP impact
- Missing basis
- Confidence tier

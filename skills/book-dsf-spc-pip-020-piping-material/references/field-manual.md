# Field Manual - DSF-SPC-PIP-020 Piping Material Specification

This is the dense working guide for `book-dsf-spc-pip-020-piping-material`. It is designed to make AutoHAZOP sharper, not to reproduce the source.

## Source Status

- Source slug: `dsf-spc-pip-020-piping-material`
- Domain family: `piping-material`
- Pages: 53
- Source quality: pages: 53
- Primary shared skill: `hazop-hazan-study-leader`
- Detailed reference: `autohazop-agent-pack/references/standards/dsf-spc-pip-020-piping-material.md`
- Source purpose: Review whether a HAZOP cause or recommendation depends on piping class, metallurgy, gasket/bolting compatibility, branch design, corrosion allowance, or pressure-temperature envelope.

## How To Attack A HAZOP Row

1. Match the row to this source's domain and tags.
2. State whether the source is primary evidence, secondary support, or routing-only.
3. Check whether the failed item exists on the selected node or connected process path.
4. Rewrite the cause as a specific initiating event, failure mode, task error, design-envelope exceedance, or missing basis.
5. Rewrite the consequence as the unmitigated event path before safeguards.
6. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
7. Convert the weakest assumption into a missing-basis recommendation.

## Sharp Questions

- [ ] Identify line class, material, rating, flange type, gasket, bolting, branch connection, corrosion/erosion service, and design envelope before accepting mechanical causes.
- [ ] Check whether the selected deviation can exceed the applicable pressure-temperature or material limit.
- [ ] Keep piping material/design basis separate from operating safeguards and IPLs.

## Anti-Patterns To Kill

- Calling corrosion, gasket failure, or piping rupture credible without service/material basis.
- Recommending material upgrade without naming the failed compatibility or design-envelope issue.

## Row Moves

- Turn vague 'pipe failure' into a specific material, rating, corrosion, erosion, gasket, bolting, branch, or thermal expansion basis.
- Route unresolved line-class questions to mechanical/piping verification instead of guessing severity or likelihood.

## Hard Decision Gates

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Missing-Basis Triggers

- Line class/spec revision
- Design pressure/temperature
- Material compatibility
- Corrosion/erosion basis
- Branch/flange/gasket/bolting detail

## Specialist Handoff

- Hand off to `hazop-hazan-study-leader` when the row needs the primary shared workflow.
- Hand off to project SMEs when the decision depends on plant-specific criteria, vendor data, inspection/proof-test records, operating procedures, relief/consequence calculations, or approved risk criteria.

## Output Standard

Return concise but traceable results:

- Decision
- Source basis
- HAZOP impact
- Missing basis
- Confidence tier

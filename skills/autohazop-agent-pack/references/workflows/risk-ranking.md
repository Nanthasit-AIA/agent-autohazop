---
name: hazop-risk-ranking-assessor
description: Perform HAZOP/LOPA initial and final risk ranking using supplied company severity, likelihood, and risk matrix criteria. Use when Codex needs to combine governing severity with initiating-event likelihood, look up initial risk, apply mitigated likelihood after credited IPLs, look up final risk, check category consistency, and decide whether recommendations are required without inventing matrix values.
---

# HAZOP Risk Ranking Assessor

## Boundary

Use the user's company risk matrix and acceptance criteria when supplied. If the matrix is missing, do not invent numeric risk rank or category.

Risk ranking is a lookup or company-defined mapping step, not a place to create new severity or frequency rules.

## Required Inputs

Initial risk needs:

- Governing unmitigated severity from safety/environment/asset comparison.
- Initiating event likelihood before IPL credit.
- Company risk matrix or company risk ranking rule.

Final risk needs:

- Governing severity, usually unchanged from unmitigated consequence.
- Mitigated likelihood after credited IPLs.
- Same company risk matrix or ranking rule.

Recommendation risk needs:

- Current final risk.
- Risk acceptance/tolerability rule.
- Proposed recommendation effect, if user asks for post-recommendation estimate.

## Ranking Sequence

1. Confirm the cause-consequence path is final.
2. Confirm governing severity is selected from the worst credible safety, environmental, and asset/equipment dimension.
3. Confirm initiating event likelihood is before IPL credit.
4. Look up initial risk in the supplied matrix.
5. Confirm safeguards and credited IPLs are separated.
6. Confirm mitigated likelihood calculation uses only credited IPLs.
7. Look up final risk in the same supplied matrix.
8. Check category labels match risk rank.
9. Decide whether recommendation/action is required by the supplied acceptance rule.
10. Record missing inputs instead of forcing values.

## Rules

- Do not multiply severity and likelihood unless the user-provided matrix explicitly says to.
- Do not reduce severity because a safeguard exists unless the safeguard changes the consequence category itself.
- Do not reduce likelihood for safeguards that are not credited IPLs.
- Do not count future recommendations as current IPLs.
- Do not assign final risk when IPL credit basis is missing.
- Do not assign numeric severity, likelihood, or risk rank when the required company scale is missing.

## Initial Risk

Use this form:

`Initial risk = matrix lookup(governing severity, initiating event likelihood before IPL credit)`

Initial risk answers: how bad and how likely is the scenario before safeguards/IPLs are credited?

## Final Risk

Use this form:

`Mitigated likelihood = initiating event frequency x credited IPL PFDs`

Then:

`Final risk = matrix lookup(governing severity, mitigated likelihood)`

Final risk answers: what risk remains after existing qualified IPLs?

## Post-Recommendation Risk

Post-recommendation risk is not current risk.

Use it only when:

- The user asks for expected post-action risk.
- The recommendation is specific enough to identify severity or likelihood change.
- The proposed safeguard/IPL has a defined design and credit basis.

Label clearly as `expected after recommendation`, `not credited until implemented`.

## Category Consistency

When the user provides category mapping, verify:

- Risk rank and category agree.
- Initial category comes from initial risk.
- Final category comes from final risk.
- Post-recommendation category is not used as current final category.

If category mapping is missing, output rank only if rank lookup is possible; otherwise mark missing mapping.

## Engineer Worksheet Style

When reviewing or producing worksheet risk cells:

- Keep initial `S/L/R` separate from final `S/L/R`.
- Initial `L` is the initiating-event likelihood before IPL credit.
- Final `L` is the mitigated likelihood after credited IPLs.
- Keep severity the same before and after safeguards unless the user provides a basis that the consequence category changes.
- If a worksheet has blank or shorthand rows that point to another parameter/deviation, do not reuse the risk cells blindly. Reconstruct the scenario or mark the risk basis as needing expansion.

## Recommendation Trigger

Use the user's company tolerability rule first.

If no rule is provided, do not invent mandatory action thresholds. Instead state:

- `Need risk acceptance criterion to decide whether recommendation is mandatory.`
- Recommend action only as an engineering suggestion tied to a specific remaining risk gap or missing basis.

Good recommendation triggers:

- Final risk is not tolerable by supplied criteria.
- Risk rank cannot be justified because severity, likelihood, or IPL basis is missing.
- Claimed IPL fails independence/effectiveness/auditability.
- Consequence severity depends on unverified design or material data.
- PFD/P&ID tracing shows an unprotected upstream/downstream propagation path.

## Output Format

For each scenario, output:

- Governing severity and basis.
- Initiating likelihood and basis.
- Initial risk lookup result or missing matrix.
- Credited IPLs and likelihood reduction basis.
- Mitigated likelihood.
- Final risk lookup result or missing matrix.
- Category consistency check.
- Recommendation trigger.
- Missing basis.

## Review Checks

Before finalizing:

- Governing severity came from three-dimension comparison.
- IEL is not reduced by safeguards.
- IPL credits came from qualified IPLs only.
- Same matrix is used for initial and final risk unless user supplies another rule.
- No numeric value is guessed from generic wording.

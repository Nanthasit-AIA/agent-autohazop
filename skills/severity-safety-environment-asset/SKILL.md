---
name: severity-safety-environment-asset
description: Assess and validate HAZOP consequence severity for safety, environmental, and asset/equipment damage using deterministic rule guidance. Use when generating or reviewing HAZOP/LOPA rows that need severity S1-S5, governing severity selection, release/fire/explosion/toxic/spill/cleanup/direct-damage reasoning, or missing-basis recommendations. Production loss, downtime loss, lost revenue, business interruption, opportunity cost, and flowrate multiplied by product price are excluded.
---

# Severity Safety Environment Asset

Use this skill to assign or review consequence severity before risk ranking. Assess Safety, Environment, and Asset separately, then use the governing severity for risk matrix lookup when the project basis supports it.

## Core Rules

- Do not assign severity from a generic word like "damage" or "release" alone.
- Trace the consequence path from initiating upset to release/exposure/fire/explosion/toxic effect/spill/cleanup/direct equipment damage.
- Use project SDS, material hazard, pressure, temperature, inventory, phase, release route, occupied area, drain path, containment, and isolation time when available.
- Mark severity as `N/A` when the required basis is missing and write the missing basis in Recommendations.
- Exclude production loss, downtime loss, lost revenue, business interruption, opportunity cost, and flowrate multiplied by product price from severity.
- Evaluate safeguards separately; do not reduce unmitigated severity unless the scenario definition itself changes.

## References

- Read `references/severity-rules.md` for searchable safety, environmental, and asset severity rules converted from the JSONL rule pack.
- Use `references/raw/*.jsonl` as the raw source rules if exact JSON fields are needed for deterministic parsing or future tooling.

## Review Flow

1. Identify the credible consequence endpoint: no release, loss of containment, fire, explosion, toxic exposure, environmental spill/release, cleanup/remediation, or direct asset damage.
2. Select the matching severity dimension rules from `references/severity-rules.md`.
3. Check applicability and `not_applicable_if` before using a rule.
4. Collect required inputs. If inputs are absent, mark the missing basis instead of guessing.
5. Determine Safety, Environment, and Asset severity independently.
6. Select the governing severity only after all relevant dimensions are considered.

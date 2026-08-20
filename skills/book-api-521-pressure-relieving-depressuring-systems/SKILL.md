---
name: book-api-521-pressure-relieving-depressuring-systems
description: Use source-specific working knowledge from API 521 Pressure-Relieving and Depressuring Systems for AutoHAZOP, HAZOP/PHA, LOPA, SIS, relief/consequence, reliability, PSM, operations, maintenance, P&ID/graph extraction, or process-safety review when a node, deviation, cause, safeguard, recommendation, or user question matches these tags: api-521, overpressure, depressuring, flare, blocked-outlet, fire-case. Use to sharpen cause credibility, consequence paths, safeguard/IPL classification, missing-basis detection, and verifiable recommendations. Read references/wiki.md, references/field-manual.md, and references/evidence-map.md before substantive use.
---

# API 521 Pressure-Relieving and Depressuring Systems Book Skill

Use this skill as a controlled AutoHAZOP working method for `api-521-pressure-relieving-depressuring-systems`. This is intentionally fail-closed: if a value, table, equation, clause, acceptance criterion, inspection interval, proof-test basis, or project fact is not encoded in the wiki/evidence map or supplied by project data, mark it as missing basis instead of guessing.

## Load Order

1. Read `references/wiki.md` for the source-specific decision playbook.
2. Read `references/field-manual.md` for sharp questions, anti-patterns, row moves, and hard decision gates.
3. Read `references/evidence-map.md` for source identity, source quality, alternate PDFs, and routing.
4. If detailed standard-derived context is needed and available, read `autohazop-agent-pack/references/standards/api-521-pressure-relieving-depressuring-systems.md`.
5. Use project P&IDs, datasheets, line lists, procedures, cause-and-effect, relief calculations, and risk criteria as controlling evidence.

## Source Role

- Source slug: `api-521-pressure-relieving-depressuring-systems`
- Domain: `relief-depressuring`
- Primary topic wiki: `relief-depressuring-systems`
- Primary shared skill: `relief-effluent-fire-explosion-consequence`
- Secondary shared skills: none
- Detailed standard reference: `autohazop-agent-pack/references/standards/api-521-pressure-relieving-depressuring-systems.md`
- Confidence tier: controlled-use - strong qualitative decision rail; project data controls all final engineering decisions.
- Source quality: pages: 206; outline/bookmark count: 59
- Core decision lens: Use API 521 relief-system context to challenge credible overpressure scenarios, depressuring, flare/vent disposal, fire case, blocked outlet, utility failure, and exchanger tube rupture.

## Alternate Source PDFs

- none

## Required Workflow

1. Match the HAZOP row or user question to this source's domain, tags, and decision lens.
2. State whether this source is primary, secondary, or only a routing aid for the decision.
3. Identify the exact decision type: graph/P&ID extraction, node boundary, cause credibility, consequence path, safeguard, IPL, severity, likelihood, recommendation, documentation, or missing basis.
4. Apply `references/wiki.md` and `references/field-manual.md`; keep source-derived guidance separate from project facts.
5. Challenge weak rows using the anti-patterns and hard gates.
6. If the decision depends on missing project data or exact standard clauses/tables, return a missing-basis recommendation.

## Source-Derived Decision Checks

- Identify credible overpressure scenario, protected equipment, relief path, disposal system, blocked outlet/fire/utility/tube rupture/thermal expansion basis, and simultaneous scenario rules.
- Check whether relief discharge creates downstream flare, vent, scrubber, sewer, or occupied-area consequences.
- Do not use API 521 to invent relief capacity; request calculation/design basis.

## Guardrails

- Use the P&ID/process graph and supplied project data as controlling evidence.
- Keep normal operation, design limits, safe operating limits, and protection layers separate.
- Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- Do not treat a standard/book statement as proof that a safeguard exists in the project.
- Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Output Pattern

When this skill materially supports an answer, structure the result as:

- Decision: recommended engineering status or next action.
- Basis: `api-521-pressure-relieving-depressuring-systems`, matched tag/domain, source role, and confidence tier.
- HAZOP impact: affected graph extraction, node, cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation.
- Missing basis: exact project/source data required before accepting the decision.
- Confidence: `usable`, `controlled-use`, `screening-only`, or `blocked`.

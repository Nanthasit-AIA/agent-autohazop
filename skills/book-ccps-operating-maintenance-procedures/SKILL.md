---
name: book-ccps-operating-maintenance-procedures
description: Use source-specific working knowledge from CCPS Guidelines for Writing Effective Operating and Maintenance Procedures for AutoHAZOP, HAZOP/PHA, LOPA, SIS, relief/consequence, reliability, PSM, operations, maintenance, P&ID/graph extraction, or process-safety review when a node, deviation, cause, safeguard, recommendation, or user question matches these tags: operating-procedure, maintenance-procedure, startup, shutdown, lineup, permit. Use to sharpen cause credibility, consequence paths, safeguard/IPL classification, missing-basis detection, and verifiable recommendations. Read references/wiki.md, references/field-manual.md, and references/evidence-map.md before substantive use.
---

# CCPS Guidelines for Writing Effective Operating and Maintenance Procedures Book Skill

Use this skill as a controlled AutoHAZOP working method for `ccps-operating-maintenance-procedures`. This is intentionally fail-closed: if a value, table, equation, clause, acceptance criterion, inspection interval, proof-test basis, or project fact is not encoded in the wiki/evidence map or supplied by project data, mark it as missing basis instead of guessing.

## Load Order

1. Read `references/wiki.md` for the source-specific decision playbook.
2. Read `references/field-manual.md` for sharp questions, anti-patterns, row moves, and hard decision gates.
3. Read `references/evidence-map.md` for source identity, source quality, alternate PDFs, and routing.
4. If detailed standard-derived context is needed and available, read `autohazop-agent-pack/references/standards/ccps-operating-maintenance-procedures.md`.
5. Use project P&IDs, datasheets, line lists, procedures, cause-and-effect, relief calculations, and risk criteria as controlling evidence.

## Source Role

- Source slug: `ccps-operating-maintenance-procedures`
- Domain: `procedures-human-factors`
- Primary topic wiki: `operating-maintenance-procedures`
- Primary shared skill: `process-safety-management-rbps-moc-docs`
- Secondary shared skills: none
- Detailed standard reference: `autohazop-agent-pack/references/standards/ccps-operating-maintenance-procedures.md`
- Confidence tier: controlled-use - strong qualitative decision rail; project data controls all final engineering decisions.
- Source quality: pages: 160; outline/bookmark count: 163
- Core decision lens: Use procedure quality logic to decide when operator/manual-valve/maintenance-lineup causes are credible and when procedures can or cannot be safeguards.

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

- Identify operating mode, task step, responsible role, preconditions, safe operating limits, hold points, verification, communication, and abnormal response.
- Treat procedures/training as weak safeguards unless they include a specific auditable action that interrupts the scenario.
- Manual valve causes need a real task path: lineup, isolation, reinstatement, startup, shutdown, sampling, draining, or maintenance.

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
- Basis: `ccps-operating-maintenance-procedures`, matched tag/domain, source role, and confidence tier.
- HAZOP impact: affected graph extraction, node, cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation.
- Missing basis: exact project/source data required before accepting the decision.
- Confidence: `usable`, `controlled-use`, `screening-only`, or `blocked`.

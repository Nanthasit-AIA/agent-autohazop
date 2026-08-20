---
name: book-ccps-safe-automation-chemical-processes
description: Use source-specific working knowledge from CCPS Guidelines for Safe Automation of Chemical Processes for AutoHAZOP, HAZOP/PHA, LOPA, SIS, relief/consequence, reliability, PSM, operations, maintenance, P&ID/graph extraction, or process-safety review when a node, deviation, cause, safeguard, recommendation, or user question matches these tags: safe-automation, bpcs, alarm, interlock, sis, cause-and-effect, bypass. Use to sharpen cause credibility, consequence paths, safeguard/IPL classification, missing-basis detection, and verifiable recommendations. Read references/wiki.md, references/field-manual.md, and references/evidence-map.md before substantive use.
---

# CCPS Guidelines for Safe Automation of Chemical Processes Book Skill

Use this skill as a controlled AutoHAZOP working method for `ccps-safe-automation-chemical-processes`. This is intentionally fail-closed: if a value, table, equation, clause, acceptance criterion, inspection interval, proof-test basis, or project fact is not encoded in the wiki/evidence map or supplied by project data, mark it as missing basis instead of guessing.

## Load Order

1. Read `references/wiki.md` for the source-specific decision playbook.
2. Read `references/field-manual.md` for sharp questions, anti-patterns, row moves, and hard decision gates.
3. Read `references/evidence-map.md` for source identity, source quality, alternate PDFs, and routing.
4. If detailed standard-derived context is needed and available, read `autohazop-agent-pack/references/standards/ccps-safe-automation-chemical-processes.md`.
5. Use project P&IDs, datasheets, line lists, procedures, cause-and-effect, relief calculations, and risk criteria as controlling evidence.

## Source Role

- Source slug: `ccps-safe-automation-chemical-processes`
- Domain: `automation-sis-bpcs`
- Primary topic wiki: `safe-automation`
- Primary shared skill: `sis-sil-verification-reliability`
- Secondary shared skills: none
- Detailed standard reference: `autohazop-agent-pack/references/standards/ccps-safe-automation-chemical-processes.md`
- Confidence tier: controlled-use - strong qualitative decision rail; project data controls all final engineering decisions.
- Source quality: pages: 441
- Core decision lens: Use safe automation lifecycle logic to classify BPCS, alarms, interlocks, SIS/SIF, cause-and-effect, bypass, diagnostics, FAT/SAT, and independence assumptions.

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

- Classify each automation element as BPCS, alarm/operator action, interlock/trip, SIS/SIF, permissive, shutdown, or final element.
- Identify sensor, logic solver/controller, final element, setpoint, action, safe state, reset, bypass, diagnostics, and test/validation basis.
- Separate spurious trip as initiating event from failure-on-demand as IPL evidence; do not mix both in one HAZOP row.

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
- Basis: `ccps-safe-automation-chemical-processes`, matched tag/domain, source role, and confidence tier.
- HAZOP impact: affected graph extraction, node, cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation.
- Missing basis: exact project/source data required before accepting the decision.
- Confidence: `usable`, `controlled-use`, `screening-only`, or `blocked`.

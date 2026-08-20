---
name: book-oreda-offshore-reliability-data-handbook
description: Use source-specific working knowledge from OREDA Offshore Reliability Data Handbook for AutoHAZOP, HAZOP/PHA, LOPA, SIS, QRA, relief/consequence, reliability, PSM, incident-learning, alarm, or process-safety review when a node, deviation, safeguard, recommendation, or user question matches these tags: oreda, offshore, failure-rate, equipment-class, reliability-data. Use to improve scenario framing, missing-basis detection, evidence-traceable recommendations, and specialist handoff. Read references/wiki.md, references/field-manual.md, and references/evidence-map.md before substantive use.
---

# OREDA Offshore Reliability Data Handbook Book Skill

Use this skill to apply the `oreda-offshore-reliability-data-handbook` book wiki as a controlled AutoHAZOP working method. This skill is intentionally fail-closed: if a value, table, criterion, equation, example, or plant-specific fact is not encoded in the wiki/evidence map or supplied by project data, mark it as missing basis instead of guessing.

## Load Order

1. Read `references/wiki.md` for the source-specific decision playbook.
2. Read `references/field-manual.md` for sharp questions, anti-patterns, row moves, and high-signal source anchors.
3. Read `references/evidence-map.md` when you need source quality, topic signals, page evidence, or confidence limits.
4. Use the project P&ID/process graph, design basis, procedures, and risk criteria as controlling context.
5. Route to shared skill `reliability-data-selection` when the decision needs a specialist workflow.

## Source Role

- Source slug: `oreda-offshore-reliability-data-handbook`
- Domain: `reliability_data`
- Primary topic wiki: `reliability-data`
- Primary shared skill: `reliability-data-selection`
- Secondary shared skills: none
- Confidence tier: screening-only - Use for routing, gap prompts, and missing-basis checks only until the source wiki is enriched from page-level reading.
- Top evidence signals: no indexed topic hits
- Core decision lens: Use the source to challenge reliability and failure-rate assumptions for applicability and uncertainty.

## Required Workflow

1. Match the user request or HAZOP row to the source tags, domain, and evidence signals.
2. State whether the source is primary, secondary, or only a screening/routing aid for this decision.
3. Identify the exact decision type: node definition, cause, consequence, safeguard, IPL, likelihood, severity, recommendation, documentation, or missing basis.
4. Apply the playbook from `references/wiki.md`; keep source-derived guidance separate from project facts.
5. Challenge every safeguard or risk reduction claim for independence, timing, effectiveness, auditability, and evidence.
6. Return a decision, basis, HAZOP impact, missing basis, and confidence tier.

## Source-Derived Decision Checks

- Whether the equipment class, service, duty cycle, environment, failure mode, and data source match.
- Whether data are being used for screening, LOPA/SIL verification, QRA, maintenance, or mechanical integrity.
- Whether uncertainty, confidence, common cause, and inspection/proof-test assumptions are visible.

## Playbook

- Name the equipment boundary and failure mode before applying any rate or probability.
- Treat handbook values as inputs needing applicability review, not universal plant facts.
- Route safety-instrumented data to SIS/SIL verification when it affects PFD/PFH or SIL target acceptance.

## Missing-Basis Triggers

- Equipment taxonomy and failure mode
- Operating/service context
- Approved reliability data source
- Proof-test/inspection interval
- Uncertainty and common-cause basis

## Guardrails

- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Pattern

When this skill materially supports an answer, structure the result as:

- Decision: recommended engineering status or next action.
- Basis: `oreda-offshore-reliability-data-handbook`, matched evidence signal, source role, and confidence tier.
- HAZOP impact: affected cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation.
- Missing basis: exact project/source data required before accepting the decision.
- Confidence: `usable`, `controlled-use`, `screening-only`, or `blocked`.

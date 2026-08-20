---
name: book-ccps-consequence-analysis-chemical-releases
description: Use source-specific working knowledge from CCPS Consequence Analysis of Chemical Releases for AutoHAZOP, HAZOP/PHA, LOPA, SIS, QRA, relief/consequence, reliability, PSM, incident-learning, alarm, or process-safety review when a node, deviation, safeguard, recommendation, or user question matches these tags: consequence-analysis, release, dispersion, toxic, flammable, source-term. Use to improve scenario framing, missing-basis detection, evidence-traceable recommendations, and specialist handoff. Read references/wiki.md, references/field-manual.md, and references/evidence-map.md before substantive use.
---

# CCPS Consequence Analysis of Chemical Releases Book Skill

Use this skill to apply the `ccps-consequence-analysis-chemical-releases` book wiki as a controlled AutoHAZOP working method. This skill is intentionally fail-closed: if a value, table, criterion, equation, example, or plant-specific fact is not encoded in the wiki/evidence map or supplied by project data, mark it as missing basis instead of guessing.

## Load Order

1. Read `references/wiki.md` for the source-specific decision playbook.
2. Read `references/field-manual.md` for sharp questions, anti-patterns, row moves, and high-signal source anchors.
3. Read `references/evidence-map.md` when you need source quality, topic signals, page evidence, or confidence limits.
4. Use the project P&ID/process graph, design basis, procedures, and risk criteria as controlling context.
5. Route to shared skill `relief-effluent-fire-explosion-consequence` when the decision needs a specialist workflow.

## Source Role

- Source slug: `ccps-consequence-analysis-chemical-releases`
- Domain: `consequence_analysis`
- Primary topic wiki: `relief-fire-explosion-consequence`
- Primary shared skill: `relief-effluent-fire-explosion-consequence`
- Secondary shared skills: none
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Top evidence signals: Consequence analysis:553, Fire/explosion:501, Relief/effluent:200, QRA/risk criteria:46
- Core decision lens: Use the source to strengthen release, relief, fire/explosion, and consequence-screening logic.

## Required Workflow

1. Match the user request or HAZOP row to the source tags, domain, and evidence signals.
2. State whether the source is primary, secondary, or only a screening/routing aid for this decision.
3. Identify the exact decision type: node definition, cause, consequence, safeguard, IPL, likelihood, severity, recommendation, documentation, or missing basis.
4. Apply the playbook from `references/wiki.md`; keep source-derived guidance separate from project facts.
5. Challenge every safeguard or risk reduction claim for independence, timing, effectiveness, auditability, and evidence.
6. Return a decision, basis, HAZOP impact, missing basis, and confidence tier.

## Source-Derived Decision Checks

- Whether the source term, material state, inventory, pressure/temperature, and release path are defined.
- Whether relief, flare/effluent, dispersion, fire, explosion, toxic, or environmental consequence assumptions are supported.
- Whether escalation and emergency response claims are engineering controls, safeguards, or only mitigations.

## Playbook

- Start with material, inventory, phase, isolation, release size, duration, and destination.
- Challenge relief/consequence recommendations for calculation basis, design assumptions, and endpoint criteria.
- Use missing-basis actions for sizing, capacity, dispersion, radiation, overpressure, toxic endpoint, or flare/effluent limits.

## Missing-Basis Triggers

- Material properties and inventory
- Relief/design basis and capacity calculation
- Release scenario/source-term basis
- Dispersion/fire/explosion/toxic endpoint criteria
- Flare/effluent/disposal system basis

## Guardrails

- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Pattern

When this skill materially supports an answer, structure the result as:

- Decision: recommended engineering status or next action.
- Basis: `ccps-consequence-analysis-chemical-releases`, matched evidence signal, source role, and confidence tier.
- HAZOP impact: affected cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation.
- Missing basis: exact project/source data required before accepting the decision.
- Confidence: `usable`, `controlled-use`, `screening-only`, or `blocked`.

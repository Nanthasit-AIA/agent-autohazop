---
name: book-ccps-facility-siting-layout
description: Use source-specific working knowledge from CCPS Facility Siting and Layout for AutoHAZOP, HAZOP/PHA, LOPA, SIS, QRA, relief/consequence, reliability, PSM, incident-learning, alarm, or process-safety review when a node, deviation, safeguard, recommendation, or user question matches these tags: facility-siting, layout, occupied-building, spacing, congestion, vulnerability. Use to improve scenario framing, missing-basis detection, evidence-traceable recommendations, and specialist handoff. Read references/wiki.md, references/field-manual.md, and references/evidence-map.md before substantive use.
---

# CCPS Facility Siting and Layout Book Skill

Use this skill to apply the `ccps-facility-siting-layout` book wiki as a controlled AutoHAZOP working method. This skill is intentionally fail-closed: if a value, table, criterion, equation, example, or plant-specific fact is not encoded in the wiki/evidence map or supplied by project data, mark it as missing basis instead of guessing.

## Load Order

1. Read `references/wiki.md` for the source-specific decision playbook.
2. Read `references/field-manual.md` for sharp questions, anti-patterns, row moves, and high-signal source anchors.
3. Read `references/evidence-map.md` when you need source quality, topic signals, page evidence, or confidence limits.
4. Use the project P&ID/process graph, design basis, procedures, and risk criteria as controlling context.
5. Route to shared skill `inherently-safer-siting-layout` when the decision needs a specialist workflow.

## Source Role

- Source slug: `ccps-facility-siting-layout`
- Domain: `siting_layout`
- Primary topic wiki: `inherent-safety-siting-layout`
- Primary shared skill: `inherently-safer-siting-layout`
- Secondary shared skills: none
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Top evidence signals: Inherent safety/siting:612, Fire/explosion:135, Consequence analysis:118, Relief/effluent:49
- Core decision lens: Use the source to prefer inherent safety and layout/siting risk reduction before add-on protection.

## Required Workflow

1. Match the user request or HAZOP row to the source tags, domain, and evidence signals.
2. State whether the source is primary, secondary, or only a screening/routing aid for this decision.
3. Identify the exact decision type: node definition, cause, consequence, safeguard, IPL, likelihood, severity, recommendation, documentation, or missing basis.
4. Apply the playbook from `references/wiki.md`; keep source-derived guidance separate from project facts.
5. Challenge every safeguard or risk reduction claim for independence, timing, effectiveness, auditability, and evidence.
6. Return a decision, basis, HAZOP impact, missing basis, and confidence tier.

## Source-Derived Decision Checks

- Whether hazard can be eliminated, substituted, minimized, moderated, simplified, segregated, or relocated.
- Whether occupied building, congestion, drainage, escalation, access/egress, or emergency response exposure is relevant.
- Whether a safeguard is compensating for a design/layout issue that should be challenged earlier.

## Playbook

- Ask whether the inventory, pressure, temperature, material, location, or operating complexity can be reduced.
- Challenge siting/layout recommendations for exposure path, occupancy, separation, drainage, and escalation basis.
- Prefer durable design changes before administrative controls when the scenario permits.

## Missing-Basis Triggers

- Inventory and layout basis
- Occupied building/siting criteria
- Escalation and drainage path
- Access/egress and emergency response assumptions
- Inherent safety option comparison

## Guardrails

- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Pattern

When this skill materially supports an answer, structure the result as:

- Decision: recommended engineering status or next action.
- Basis: `ccps-facility-siting-layout`, matched evidence signal, source role, and confidence tier.
- HAZOP impact: affected cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation.
- Missing basis: exact project/source data required before accepting the decision.
- Confidence: `usable`, `controlled-use`, `screening-only`, or `blocked`.

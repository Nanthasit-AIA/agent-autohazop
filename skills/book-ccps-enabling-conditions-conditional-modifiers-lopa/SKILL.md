---
name: book-ccps-enabling-conditions-conditional-modifiers-lopa
description: Use source-specific working knowledge from CCPS Enabling Conditions and Conditional Modifiers in LOPA for AutoHAZOP, HAZOP/PHA, LOPA, SIS, QRA, relief/consequence, reliability, PSM, incident-learning, alarm, or process-safety review when a node, deviation, safeguard, recommendation, or user question matches these tags: lopa, enabling-condition, conditional-modifier, occupancy, ignition, vulnerability. Use to improve scenario framing, missing-basis detection, evidence-traceable recommendations, and specialist handoff. Read references/wiki.md, references/field-manual.md, and references/evidence-map.md before substantive use.
---

# CCPS Enabling Conditions and Conditional Modifiers in LOPA Book Skill

Use this skill to apply the `ccps-enabling-conditions-conditional-modifiers-lopa` book wiki as a controlled AutoHAZOP working method. This skill is intentionally fail-closed: if a value, table, criterion, equation, example, or plant-specific fact is not encoded in the wiki/evidence map or supplied by project data, mark it as missing basis instead of guessing.

## Load Order

1. Read `references/wiki.md` for the source-specific decision playbook.
2. Read `references/field-manual.md` for sharp questions, anti-patterns, row moves, and high-signal source anchors.
3. Read `references/evidence-map.md` when you need source quality, topic signals, page evidence, or confidence limits.
4. Use the project P&ID/process graph, design basis, procedures, and risk criteria as controlling context.
5. Route to shared skill `lopa-iel-conditional-modifier` when the decision needs a specialist workflow.

## Source Role

- Source slug: `ccps-enabling-conditions-conditional-modifiers-lopa`
- Domain: `lopa`
- Primary topic wiki: `lopa-sil-sis`
- Primary shared skill: `lopa-iel-conditional-modifier`
- Secondary shared skills: none
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Top evidence signals: LOPA/IPL:590, Consequence analysis:194, Fire/explosion:133, QRA/risk criteria:130
- Core decision lens: Use the source to turn selected HAZOP rows into disciplined one-scenario LOPA checks.

## Required Workflow

1. Match the user request or HAZOP row to the source tags, domain, and evidence signals.
2. State whether the source is primary, secondary, or only a screening/routing aid for this decision.
3. Identify the exact decision type: node definition, cause, consequence, safeguard, IPL, likelihood, severity, recommendation, documentation, or missing basis.
4. Apply the playbook from `references/wiki.md`; keep source-derived guidance separate from project facts.
5. Challenge every safeguard or risk reduction claim for independence, timing, effectiveness, auditability, and evidence.
6. Return a decision, basis, HAZOP impact, missing basis, and confidence tier.

## Source-Derived Decision Checks

- Whether the scenario has one initiating event, one consequence, and explicit enabling conditions/conditional modifiers.
- Whether a safeguard qualifies as an IPL with independence, effectiveness, auditability, and timing.
- Whether likelihood reduction is supported without double counting BPCS, alarms, SIS, relief, procedures, or inspection.

## Playbook

- State the initiating event family before assigning or requesting frequency data.
- Separate safeguards from credited IPLs and state why each credited IPL is independent of the cause.
- Fail closed when risk criteria, frequency data, conditional modifiers, or IPL PFD/test basis are absent.

## Missing-Basis Triggers

- Project LOPA rules and tolerable risk criteria
- Approved initiating-event frequency source
- Conditional modifier/enabling-condition basis
- IPL independence, audit, response-time, and proof-test evidence
- Common-cause and double-counting review

## Guardrails

- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Pattern

When this skill materially supports an answer, structure the result as:

- Decision: recommended engineering status or next action.
- Basis: `ccps-enabling-conditions-conditional-modifiers-lopa`, matched evidence signal, source role, and confidence tier.
- HAZOP impact: affected cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation.
- Missing basis: exact project/source data required before accepting the decision.
- Confidence: `usable`, `controlled-use`, `screening-only`, or `blocked`.

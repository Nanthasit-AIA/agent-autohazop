---
name: book-engineers-view-human-error
description: Use source-specific working knowledge from An Engineer's View of Human Error for AutoHAZOP, HAZOP/PHA, LOPA, SIS, QRA, relief/consequence, reliability, PSM, incident-learning, alarm, or process-safety review when a node, deviation, safeguard, recommendation, or user question matches these tags: human-error, human-factors, design-for-error, procedure, maintenance. Use to improve scenario framing, missing-basis detection, evidence-traceable recommendations, and specialist handoff. Read references/wiki.md, references/field-manual.md, and references/evidence-map.md before substantive use.
---

# An Engineer's View of Human Error Book Skill

Use this skill to apply the `engineers-view-human-error` book wiki as a controlled AutoHAZOP working method. This skill is intentionally fail-closed: if a value, table, criterion, equation, example, or plant-specific fact is not encoded in the wiki/evidence map or supplied by project data, mark it as missing basis instead of guessing.

## Load Order

1. Read `references/wiki.md` for the source-specific decision playbook.
2. Read `references/field-manual.md` for sharp questions, anti-patterns, row moves, and high-signal source anchors.
3. Read `references/evidence-map.md` when you need source quality, topic signals, page evidence, or confidence limits.
4. Use the project P&ID/process graph, design basis, procedures, and risk criteria as controlling context.
5. Route to shared skill `incident-learning-root-cause-human-error` when the decision needs a specialist workflow.

## Source Role

- Source slug: `engineers-view-human-error`
- Domain: `human_factors`
- Primary topic wiki: `incident-learning-and-human-factors`
- Primary shared skill: `incident-learning-root-cause-human-error`
- Secondary shared skills: none
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Top evidence signals: Incident/human factors:418, Fire/explosion:43, Inherent safety/siting:32, HAZOP/PHA:28
- Core decision lens: Use the source to improve causal reasoning, human factors, and learning from prior incidents.

## Required Workflow

1. Match the user request or HAZOP row to the source tags, domain, and evidence signals.
2. State whether the source is primary, secondary, or only a screening/routing aid for this decision.
3. Identify the exact decision type: node definition, cause, consequence, safeguard, IPL, likelihood, severity, recommendation, documentation, or missing basis.
4. Apply the playbook from `references/wiki.md`; keep source-derived guidance separate from project facts.
5. Challenge every safeguard or risk reduction claim for independence, timing, effectiveness, auditability, and evidence.
6. Return a decision, basis, HAZOP impact, missing basis, and confidence tier.

## Source-Derived Decision Checks

- Whether a cause is a direct technical failure, human action, latent organizational weakness, or degraded barrier.
- Whether a recommendation changes the system rather than only reminding people to be careful.
- Whether repeat-event learning, design-for-error, maintenance, procedure, or supervision gaps are visible.

## Playbook

- Challenge blame-only wording and look for design, procedure, interface, maintenance, training, workload, and management-system contributors.
- Convert lessons into engineered, procedural, and audit-backed actions.
- Use incident patterns to ask better questions, not to assert plant-specific facts without evidence.

## Missing-Basis Triggers

- Incident evidence and timeline
- Barrier failure analysis
- Human factors/task analysis
- Management-system causal evidence
- Action effectiveness verification

## Guardrails

- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Pattern

When this skill materially supports an answer, structure the result as:

- Decision: recommended engineering status or next action.
- Basis: `engineers-view-human-error`, matched evidence signal, source role, and confidence tier.
- HAZOP impact: affected cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation.
- Missing basis: exact project/source data required before accepting the decision.
- Confidence: `usable`, `controlled-use`, `screening-only`, or `blocked`.

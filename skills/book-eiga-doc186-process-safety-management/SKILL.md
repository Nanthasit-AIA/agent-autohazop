---
name: book-eiga-doc186-process-safety-management
description: Use source-specific working knowledge from EIGA Doc 186 - Process Safety Management for AutoHAZOP, HAZOP/PHA, LOPA, SIS, QRA, relief/consequence, reliability, PSM, incident-learning, alarm, or process-safety review when a node, deviation, safeguard, recommendation, or user question matches these tags: psm, hazard-identification, risk-management, moc, audit. Use to improve scenario framing, missing-basis detection, evidence-traceable recommendations, and specialist handoff. Read references/wiki.md, references/field-manual.md, and references/evidence-map.md before substantive use.
---

# EIGA Doc 186 - Process Safety Management Book Skill

Use this skill to apply the `eiga-doc186-process-safety-management` book wiki as a controlled AutoHAZOP working method. This skill is intentionally fail-closed: if a value, table, criterion, equation, example, or plant-specific fact is not encoded in the wiki/evidence map or supplied by project data, mark it as missing basis instead of guessing.

## Load Order

1. Read `references/wiki.md` for the source-specific decision playbook.
2. Read `references/field-manual.md` for sharp questions, anti-patterns, row moves, and high-signal source anchors.
3. Read `references/evidence-map.md` when you need source quality, topic signals, page evidence, or confidence limits.
4. Use the project P&ID/process graph, design basis, procedures, and risk criteria as controlling context.
5. Route to shared skill `process-safety-management-rbps-moc-docs` when the decision needs a specialist workflow.

## Source Role

- Source slug: `eiga-doc186-process-safety-management`
- Domain: `psm`
- Primary topic wiki: `psm-rbps-moc-documentation`
- Primary shared skill: `process-safety-management-rbps-moc-docs`
- Secondary shared skills: none
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Top evidence signals: PSM/MOC/documentation:91, Incident/human factors:18, HAZOP/PHA:3, Inherent safety/siting:2
- Core decision lens: Use the source to turn technical gaps into auditable process-safety management actions.

## Required Workflow

1. Match the user request or HAZOP row to the source tags, domain, and evidence signals.
2. State whether the source is primary, secondary, or only a screening/routing aid for this decision.
3. Identify the exact decision type: node definition, cause, consequence, safeguard, IPL, likelihood, severity, recommendation, documentation, or missing basis.
4. Apply the playbook from `references/wiki.md`; keep source-derived guidance separate from project facts.
5. Challenge every safeguard or risk reduction claim for independence, timing, effectiveness, auditability, and evidence.
6. Return a decision, basis, HAZOP impact, missing basis, and confidence tier.

## Source-Derived Decision Checks

- Whether the gap is PSI, procedure, training, MOC, PSSR, mechanical integrity, emergency management, audit, or action tracking.
- Whether a recommendation names an accountable management-system deliverable.
- Whether documentation is sufficient to support later HAZOP/LOPA/SIS decisions.

## Playbook

- Translate vague 'review/update' actions into specific records, owners, acceptance criteria, and verification evidence.
- Flag MOC/PSSR needs when design, procedure, alarm, interlock, relief, operating envelope, or equipment service changes.
- Keep technical and management-system recommendations linked to the scenario that created the need.

## Missing-Basis Triggers

- Process safety information
- Operating procedure/training record
- MOC/PSSR evidence
- Inspection/test/maintenance record
- Audit/action-tracking closure evidence

## Guardrails

- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Pattern

When this skill materially supports an answer, structure the result as:

- Decision: recommended engineering status or next action.
- Basis: `eiga-doc186-process-safety-management`, matched evidence signal, source role, and confidence tier.
- HAZOP impact: affected cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation.
- Missing basis: exact project/source data required before accepting the decision.
- Confidence: `usable`, `controlled-use`, `screening-only`, or `blocked`.

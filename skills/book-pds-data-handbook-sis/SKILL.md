---
name: book-pds-data-handbook-sis
description: Use source-specific working knowledge from PDS Data Handbook for SIS for AutoHAZOP, HAZOP/PHA, LOPA, SIS, QRA, relief/consequence, reliability, PSM, incident-learning, alarm, or process-safety review when a node, deviation, safeguard, recommendation, or user question matches these tags: pds, sis, failure-rate, reliability-data, proof-test, pfd. Use to improve scenario framing, missing-basis detection, evidence-traceable recommendations, and specialist handoff. Read references/wiki.md, references/field-manual.md, and references/evidence-map.md before substantive use.
---

# PDS Data Handbook for SIS Book Skill

Use this skill to apply the `pds-data-handbook-sis` book wiki as a controlled AutoHAZOP working method. This skill is intentionally fail-closed: if a value, table, criterion, equation, example, or plant-specific fact is not encoded in the wiki/evidence map or supplied by project data, mark it as missing basis instead of guessing.

## Load Order

1. Read `references/wiki.md` for the source-specific decision playbook.
2. Read `references/field-manual.md` for sharp questions, anti-patterns, row moves, and high-signal source anchors.
3. Read `references/evidence-map.md` when you need source quality, topic signals, page evidence, or confidence limits.
4. Use the project P&ID/process graph, design basis, procedures, and risk criteria as controlling context.
5. Route to shared skill `reliability-data-selection` and secondary skills `sis-sil-verification-reliability` when the decision needs a specialist workflow.

## Source Role

- Source slug: `pds-data-handbook-sis`
- Domain: `sis_reliability`
- Primary topic wiki: `reliability-data`
- Primary shared skill: `reliability-data-selection`
- Secondary shared skills: `sis-sil-verification-reliability`
- Confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.
- Top evidence signals: Reliability data:734, SIS/SIL:149, Relief/effluent:8, Consequence analysis:4
- Core decision lens: Use the source to challenge SIS/SIF claims through lifecycle evidence, not labels.

## Required Workflow

1. Match the user request or HAZOP row to the source tags, domain, and evidence signals.
2. State whether the source is primary, secondary, or only a screening/routing aid for this decision.
3. Identify the exact decision type: node definition, cause, consequence, safeguard, IPL, likelihood, severity, recommendation, documentation, or missing basis.
4. Apply the playbook from `references/wiki.md`; keep source-derived guidance separate from project facts.
5. Challenge every safeguard or risk reduction claim for independence, timing, effectiveness, auditability, and evidence.
6. Return a decision, basis, HAZOP impact, missing basis, and confidence tier.

## Source-Derived Decision Checks

- Whether a claimed SIF has a defined hazardous event, safe state, sensor-logic-final element chain, and demand mode.
- Whether SIL target, PFD/PFH, proof-test interval, bypass controls, and independence from BPCS are supported.
- Whether the evidence belongs in HAZOP, LOPA, SRS, SIL verification, validation, or operations/maintenance.

## Playbook

- Map every claimed SIF to cause, consequence, safe state, response time, and equipment architecture.
- Challenge generic SIL statements unless the lifecycle and verification basis are present.
- Route reliability-data assumptions to approved plant/project sources before accepting PFD/PFH.

## Missing-Basis Triggers

- SIL target allocation basis
- SRS/SIF definition
- PFD/PFH calculation and proof-test interval
- Independence from BPCS and common-cause review
- Validation, bypass, maintenance, and proof-test records

## Guardrails

- Separate source-derived guidance from project facts and assumptions.
- Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- Treat the book artifact as decision support, not as a substitute for competent engineering review.
- If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Pattern

When this skill materially supports an answer, structure the result as:

- Decision: recommended engineering status or next action.
- Basis: `pds-data-handbook-sis`, matched evidence signal, source role, and confidence tier.
- HAZOP impact: affected cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation.
- Missing basis: exact project/source data required before accepting the decision.
- Confidence: `usable`, `controlled-use`, `screening-only`, or `blocked`.

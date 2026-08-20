---
name: hazop-hazan-study-leader
description: Plan, facilitate, generate, and quality-check HAZOP, HAZAN, PHA, What-if, checklist, and security review outputs. Use when Codex needs to define nodes/design intent, apply guidewords, develop deviations/causes/consequences/safeguards/recommendations, audit HAZOP worksheet quality, detect vague or ungrounded rows, or convert PHA findings into defensible actions.
---

# HAZOP and HAZAN Study Leader

Use this skill as a procedural review aid. Keep conclusions evidence-traceable and do not replace competent engineering judgment, company procedures, or legal/regulatory requirements.

## Source Basis

This production skill is derived from the 2026-07-01 Books knowledge pack:

`C:\Users\User\Desktop\Learning Data\10_RAG_WIKI_SKILLS\03_All_New_Process_Safety_Books_2026_07_01`

Primary source slugs:

- `hazop-guide-best-practice`
- `hazop-hazan-kletz`
- `ccps-hazard-evaluation-procedures`
- `safety-security-review-process-industries`
- `lees-loss-prevention`

## Required Workflow

1. Define the review scope and source basis.
2. Extract the scenario, equipment, safeguards, assumptions, and requested decision.
3. Apply the skill-specific checks below.
4. Separate confirmed findings from missing basis.
5. Produce an audit-ready output with source slugs and project data still required.

## Skill-Specific Checks

- Normalize each row to node, design intent, parameter, guideword, deviation, cause, consequence, safeguard, recommendation, and source evidence.
- Reject vague deviations, missing causes, unsupported consequences, safeguards that do not interrupt the scenario, and recommendations without action owner/basis.
- When working with graph-grounded AutoHAZOP, require tag existence, path evidence, directionality, and safeguard location before accepting cross-node consequences.

## Preferred Outputs

- Worksheet QA table
- Study preparation checklist
- Node/deviation map
- Recommendation quality review

## Reference Routing

- Read `references/source-map.md` to see which books support this skill.
- Read `references/review-checklist.md` for the compact checklist.
- Read the matching wiki topic under `../../wiki/` when a broader explanation or retrieval tags are needed.

## Guardrails

- Do not quote long source passages.
- Do not invent numerical values, risk criteria, PFDs, SIL targets, failure rates, consequence endpoints, or acceptance criteria.
- Do not treat a safeguard as an IPL without effectiveness, independence, auditability, and scenario-specific evidence.
- If a required value, table, equation, criterion, or example is not encoded in the skill/wiki or supplied project basis, mark it as missing basis and recommend skill/wiki enrichment.
- Keep final recommendations specific, owned, verifiable, and tied to the scenario.

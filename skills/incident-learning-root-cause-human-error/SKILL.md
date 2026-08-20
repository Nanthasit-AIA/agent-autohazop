---
name: incident-learning-root-cause-human-error
description: Analyze process incident cases, human error, root causes, organizational learning, and corrective actions. Use when Codex needs to convert accidents or near misses into HAZOP prompts, identify barrier failures, challenge blame-focused explanations, or draft incident-learning recommendations.
---

# Incident Learning and Human Error Review

Use this skill as a procedural review aid. Keep conclusions evidence-traceable and do not replace competent engineering judgment, company procedures, or legal/regulatory requirements.

## Source Basis

This production skill is derived from the 2026-07-01 Books knowledge pack:

`C:\Users\User\Desktop\Learning Data\10_RAG_WIKI_SKILLS\03_All_New_Process_Safety_Books_2026_07_01`

Primary source slugs:

- `what-went-wrong-case-histories`
- `lessons-from-disaster`
- `engineers-view-human-error`
- `ccps-investigating-chemical-process-incidents`

## Required Workflow

1. Define the review scope and source basis.
2. Extract the scenario, equipment, safeguards, assumptions, and requested decision.
3. Apply the skill-specific checks below.
4. Separate confirmed findings from missing basis.
5. Produce an audit-ready output with source slugs and project data still required.

## Skill-Specific Checks

- Build a timeline, separate immediate technical causes from underlying and management-system causes, and identify failed/missing barriers.
- Treat human error as a symptom; propose design, interface, procedure, training, workload, supervision, and management-system changes.
- Check that corrective actions are specific, owned, verifiable, and capable of preventing recurrence.

## Preferred Outputs

- Incident learning summary
- Root-cause/barrier table
- HAZOP prompt extraction
- Corrective action QA

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

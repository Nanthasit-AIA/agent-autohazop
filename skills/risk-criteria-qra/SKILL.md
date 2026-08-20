---
name: risk-criteria-qra
description: Review quantitative risk assessment, risk criteria, tolerability, ALARP/ALAP decisions, event trees, fault trees, frequency/consequence integration, and escalation beyond HAZOP/LOPA. Use when Codex needs to check risk criteria, QRA inputs, scenario frequency, uncertainty, or individual/societal risk arguments.
---

# Risk Criteria and QRA Review

Use this skill as a procedural review aid. Keep conclusions evidence-traceable and do not replace competent engineering judgment, company procedures, or legal/regulatory requirements.

## Source Basis

This production skill is derived from the 2026-07-01 Books knowledge pack:

`C:\Users\User\Desktop\Learning Data\10_RAG_WIKI_SKILLS\03_All_New_Process_Safety_Books_2026_07_01`

Primary source slugs:

- `ccps-chemical-process-qra`
- `ccps-quantitative-safety-risk-criteria`
- `ccps-consequence-analysis-chemical-releases`
- `thermal-process-risk-food-manufacture`
- `sil-selection-systematic-methods-lopa`

## Required Workflow

1. Define the review scope and source basis.
2. Extract the scenario, equipment, safeguards, assumptions, and requested decision.
3. Apply the skill-specific checks below.
4. Separate confirmed findings from missing basis.
5. Produce an audit-ready output with source slugs and project data still required.

## Skill-Specific Checks

- Separate scenario risk, individual risk, societal risk, corporate criteria, regulatory criteria, and cost-benefit/ALARP logic.
- Escalate from HAZOP/LOPA to QRA when cumulative risk, complex dependencies, facility siting, major consequence modeling, or high-stakes mitigation decisions matter.
- Require transparent source terms, event/fault tree logic, consequence models, frequency basis, uncertainty, sensitivity, and acceptance criteria.

## Preferred Outputs

- Risk criteria review
- QRA readiness checklist
- Escalation recommendation
- Uncertainty/sensitivity gap list

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

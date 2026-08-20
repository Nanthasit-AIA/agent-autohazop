---
name: reliability-data-selection
description: Select and challenge reliability, failure-rate, demand-rate, PFD, and equipment failure data for HAZOP, LOPA, QRA, SIS, and mechanical integrity assumptions. Use when Codex needs to match handbook data to equipment classes, identify data-quality issues, or prevent double counting in frequency calculations.
---

# Reliability Data Selection

Use this skill as a procedural review aid. Keep conclusions evidence-traceable and do not replace competent engineering judgment, company procedures, or legal/regulatory requirements.

## Source Basis

This production skill is derived from the 2026-07-01 Books knowledge pack:

`C:\Users\User\Desktop\Learning Data\10_RAG_WIKI_SKILLS\03_All_New_Process_Safety_Books_2026_07_01`

Primary source slugs:

- `ccps-process-equipment-reliability-data`
- `pds-data-handbook-sis`
- `oreda-offshore-reliability-data-handbook`
- `control-systems-safety-evaluation-reliability`

## Required Workflow

1. Define the review scope and source basis.
2. Extract the scenario, equipment, safeguards, assumptions, and requested decision.
3. Apply the skill-specific checks below.
4. Separate confirmed findings from missing basis.
5. Produce an audit-ready output with source slugs and project data still required.

## Skill-Specific Checks

- Match equipment class, service, boundary, duty, environment, failure mode, operating context, repair policy, and data source before using a number.
- Keep uncertainty visible; handbook values are inputs to judgment, not universal truth.
- Trace each data item to its role: initiating event, equipment failure, IPL PFD, SIF verification, event tree, fault tree, or maintenance decision.

## Preferred Outputs

- Reliability data selection note
- Frequency/PFD assumption register
- Data-quality challenge list

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

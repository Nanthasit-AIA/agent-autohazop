---
name: alarm-management-rationalization
description: Review alarm philosophy, rationalization, alarm lifecycle, alarm performance, operator response, and alarm-as-safeguard claims. Use when Codex needs to decide whether an alarm is a credible safeguard/IPL candidate, identify alarm flood/standing/nuisance alarm risks, or draft alarm rationalization outputs.
---

# Alarm Management Rationalization

Use this skill as a procedural review aid. Keep conclusions evidence-traceable and do not replace competent engineering judgment, company procedures, or legal/regulatory requirements.

## Source Basis

This production skill is derived from the 2026-07-01 Books knowledge pack:

`C:\Users\User\Desktop\Learning Data\10_RAG_WIKI_SKILLS\03_All_New_Process_Safety_Books_2026_07_01`

Primary source slugs:

- `alarm-management-handbook`

## Required Workflow

1. Define the review scope and source basis.
2. Extract the scenario, equipment, safeguards, assumptions, and requested decision.
3. Apply the skill-specific checks below.
4. Separate confirmed findings from missing basis.
5. Produce an audit-ready output with source slugs and project data still required.

## Skill-Specific Checks

- Confirm alarm purpose, consequence of no response, operator action, response time, priority, setpoint, deadband, shelving/suppression rules, and documentation.
- Treat an alarm as weak until independence, rationalization, training, response time, and performance evidence are available.
- Flag alarm floods, nuisance alarms, standing alarms, stale priorities, ambiguous messages, and action wording that does not tell the operator what to do.

## Preferred Outputs

- Alarm rationalization table
- Alarm safeguard/IPL screening
- Alarm KPI gap list

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

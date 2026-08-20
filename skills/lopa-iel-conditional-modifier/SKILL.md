---
name: lopa-iel-conditional-modifier
description: Review LOPA scenario structure, initiating events, independent protection layers, enabling conditions, conditional modifiers, and SIL-selection inputs. Use when Codex needs to convert HAZOP rows to LOPA scenarios, qualify IPLs, check independence/effectiveness/auditability, avoid double counting, review initiating event frequency basis, or flag missing LOPA/SIL evidence.
---

# LOPA IE/IPL and Conditional Modifier Review

Use this skill as a procedural review aid. Keep conclusions evidence-traceable and do not replace competent engineering judgment, company procedures, or legal/regulatory requirements.

## Source Basis

This production skill is derived from the 2026-07-01 Books knowledge pack:

`C:\Users\User\Desktop\Learning Data\10_RAG_WIKI_SKILLS\03_All_New_Process_Safety_Books_2026_07_01`

Primary source slugs:

- `ccps-initiating-events-ipls-lopa`
- `ccps-enabling-conditions-conditional-modifiers-lopa`
- `sil-selection-systematic-methods-lopa`

## Required Workflow

1. Define the review scope and source basis.
2. Extract the scenario, equipment, safeguards, assumptions, and requested decision.
3. Apply the skill-specific checks below.
4. Separate confirmed findings from missing basis.
5. Produce an audit-ready output with source slugs and project data still required.

## Skill-Specific Checks

- Use one initiating event and one consequence per scenario; separate enabling conditions and conditional modifiers.
- Credit IPLs only when effective, independent, and auditable, with project-approved PFD/credit basis.
- Do not invent initiating event frequencies, conditional probabilities, PFDs, or risk criteria; list missing basis instead.

## Preferred Outputs

- LOPA readiness audit
- IEL/IPL review table
- Conditional modifier decision
- Missing basis list

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

---
name: sis-sil-verification-reliability
description: Review SIS/SIF functional safety evidence, SIL selection basis, SIF definition, PFDavg/PFH verification, proof testing, architecture, reliability data, and BPCS/SIS independence. Use when Codex needs to assess whether a SIF can support LOPA IPL credit, check SIS verification inputs, or identify lifecycle and calculation gaps.
---

# SIS, SIL and SIF Verification

Use this skill as a procedural review aid. Keep conclusions evidence-traceable and do not replace competent engineering judgment, company procedures, or legal/regulatory requirements.

## Source Basis

This production skill is derived from the 2026-07-01 Books knowledge pack:

`C:\Users\User\Desktop\Learning Data\10_RAG_WIKI_SKILLS\03_All_New_Process_Safety_Books_2026_07_01`

Primary source slugs:

- `sis-verification-probabilistic-calculation`
- `functional-safety-straightforward-guide`
- `control-systems-safety-evaluation-reliability`
- `pds-data-handbook-sis`
- `sil-selection-systematic-methods-lopa`

## Required Workflow

1. Define the review scope and source basis.
2. Extract the scenario, equipment, safeguards, assumptions, and requested decision.
3. Apply the skill-specific checks below.
4. Separate confirmed findings from missing basis.
5. Produce an audit-ready output with source slugs and project data still required.

## Skill-Specific Checks

- Start with SIF definition, safe state, demand mode, response time, target SIL/PFD, and proof-test basis.
- Check architecture, dangerous failure assumptions, common cause, beta factors, diagnostics, proof-test coverage, bypasses, and repair assumptions.
- Separate SIL selection from SIL verification; do not claim achieved SIL without both target and verification evidence.

## Preferred Outputs

- SIF evidence review
- SIL verification gap list
- PFD/PFH assumption register
- BPCS/SIS dependency review

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

---
name: hazop-lopa-ipl-assessor
description: Evaluate initiating event likelihood, safeguards, IPL qualification, PFD/credit, and mitigated likelihood for HAZOP/LOPA scenarios. Use when Codex needs to separate safeguards from credited IPLs, check independence/effectiveness/auditability, reject weak IPL claims, apply IEL/PFD tables supplied by the user or embedded defaults, and calculate final likelihood before risk-matrix lookup.
---

# HAZOP LOPA IPL Assessor

## Boundary

Use user-provided company IEL and IPL criteria when available. If absent, use the embedded SCG-style values as screening defaults and state that final project acceptance requires the company basis.

Do not credit safeguards as IPLs just because they are listed in the worksheet.

## Team Workflow

1. Define the initiating event and unmitigated consequence.
2. Select initiating event frequency before any IPL credit.
3. List all existing safeguards.
4. For each safeguard, test IPL qualification.
5. Record credited IPLs separately from non-credited safeguards.
6. Apply PFD/credit only to qualified IPLs.
7. Multiply initiating event frequency by credited IPL PFDs to get mitigated frequency.
8. Convert mitigated frequency to likelihood using the supplied likelihood scale.
9. Look up final risk in the supplied risk matrix.
10. Recommend actions for missing or failed IPL criteria.

## Initiating Event Likelihood Defaults

Use these only when the scenario clearly matches and no better project-specific data is provided:

| Initiating event | Suggested frequency |
| --- | --- |
| BPCS instrument loop failure | 1E-1 per year |
| Instrument failure | 1E-1 per year |
| Regulator failure | 1E-1 per year |
| Valve failure | 1E-1 per year |
| Cooling water failure | 1E-1 per year |
| Loss of power with redundant power supplies | 1E-1 per year |
| Unloading/loading hose failure with annual inspection/replacement | 1E-1 per year |
| Turbine/diesel engine overspeed with casing breach | 1E-4 per year |
| Compressor / pump overspeed | 1E-1 per year |
| Rotating equipment failure | 1E-1 per year |
| Pump seal failure | 1E-1 per year |
| Hose leak/rupture | 1E-1 per year |
| Gasket/packing blowout | 1E-2 per year |
| Fixed equipment failure, such as exchanger tube failure | 1E-2 per year |
| Safety valve opens spuriously | 1E-2 per year |
| PSV failure | 1E-2 per year |
| Single check valve failure in high-demand mode | 1E-1 per year |
| Double dissimilar check valves in high-demand mode | 1E-2 per year |
| Routine operator task once per week or more | 1 per year |
| Routine operator task between monthly and weekly | 1E-1 per year |
| Non-routine operator task less than monthly | 1E-2 per year |
| LOTO checklist failure | 1E-3 per opportunity |

Do not reduce initiating event likelihood for safeguards. IPL credit is applied later.

For startup, shutdown, batch, or special activities, reduce frequency only when the user provides operating frequency or SIL determination basis. Do not reduce below a stated minimum without a supplied rule.

## IPL Qualification

Credit an IPL only when all are true:

- Independence: not the initiating event and not dependent on another credited IPL.
- Effectiveness: prevents or mitigates the specific consequence in time.
- Auditability: can be inspected, tested, maintained, or procedurally verified.
- Design basis: designed for the scenario and service.
- Management basis: inspection, testing, preventive maintenance, training, or procedure exists.

If any criterion is missing, list as safeguard or candidate IPL with zero credit.

## PFD / Credit Defaults

Use company PFD values first. Screening defaults:

| IPL | Suggested PFD |
| --- | --- |
| Open vent with no valve | 1E-2 |
| End-of-line deflagration arrester | 1E-2 |
| In-line deflagration arrester | 1E-1 to 1E-2 |
| In-line stable detonation arrester | 1E-1 to 1E-2 |
| In-line unstable detonation arrester | 1E-2 to 1E-3 |
| Overflow line with no impediment | 1E-3 |
| Overflow line with passive fluid or rupture disk | 1E-2 |
| Overflow line with freeze/foul/closed-valve potential | 1E-1 |
| Permanent mechanical stop | 1E-2 |
| Inherent safe design | 1E-2 or eliminate consequence by team decision |
| Continuous pilot | 1E-1 |
| Captive key / lock system | 1E-2 |
| Adjustable movement-limiting device | 1E-1 |
| Restriction orifice in clean, noncorrosive, nonerosive service | 1E-2 |
| Multiple mechanical pump seal with detection/indication | 1E-1 |
| Human response to alarm/check/sample | 1E-1 |
| BPCS loop or interlock | not greater than 1E-1 credit unless IEC/company basis supports more |
| SIL 1 SIF | 1E-2 <= PFD < 1E-1 |
| SIL 2 SIF | 1E-3 <= PFD < 1E-2 |
| SIL 3 SIF | 1E-4 <= PFD < 1E-3 |
| Relief valve designed for scenario | 1E-2 |
| Rupture disc | 1E-2 |
| Breather valve | 1E-2 |
| Single check valve, low-demand clean service | 1E-1 |
| Double dissimilar check valves, low-demand clean service | 1E-2 |
| Secondary pressure regulator | 1E-1 |

## Special Rejection Rules

- Do not credit proposed recommendations as current IPLs.
- Do not credit alarm/operator response without clear alarm/check, written action, training, response time, low complexity, and safe working condition.
- Do not credit relief devices unless sized/designed for the scenario.
- If relief valve effectiveness depends on another device, treat them as one IPL using the weaker PFD.
- If an isolation valve can defeat a relief device, use weaker credit unless valve-position management is established.
- Do not use check valve(s) as sole IPL for overpressure of low-pressure equipment from high-pressure reverse flow; relief protection is also required.
- Do not count multiple BPCS IPLs or BPCS as both initiating event and IPL without explicit company/IEC/CCPS multiple-loop basis.

## Output Format

For each scenario, output:

- Initiating event and frequency basis.
- Existing safeguards.
- Candidate IPLs.
- Credited IPLs with PFD/credit.
- Rejected IPLs and rejection reason.
- Mitigated frequency calculation.
- Final likelihood basis.
- Missing data.
- Recommendations for failed or missing IPL criteria.

## Engineer Worksheet Style

When writing IPLs and recommendations, follow concise engineer worksheet style:

- Number each IPL or safeguard when there are multiple items.
- Include equipment or instrument tags when supplied.
- Show credit beside the IPL, such as `(-1)` or `(-2)`, only when the credit basis is established.
- Record Independent / Effective / Auditable as separate yes/no checks when reviewing IPL quality.
- For interlocks or trips claimed as IPLs, recommend SIL classification or verification when the SIL basis is missing.
- For alarm/operator response, recommend procedure, response basis, or training only when those are the missing IPL criteria.

Do not copy shorthand cross-references from example worksheets as final IPL basis. Expand the IPL basis or mark it as needing expansion.

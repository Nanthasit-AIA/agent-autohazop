---
name: hazop-severity-assessor
description: Assess HAZOP/LOPA consequence severity by evaluating safety/human health, environmental impact, and asset/equipment damage separately, then selecting the most severe credible dimension. Use when Codex needs severity rationale, non-money severity logic, injury/environment evidence, equipment-only financial damage logic, or source-backed severity screening before risk ranking.
---

# HAZOP Severity Assessor

## Core Rule

Assess three dimensions independently:

1. Safety / human health.
2. Environmental impact.
3. Asset / equipment damage.

Then compare them and select the governing severity as the highest credible severity among the three. Do not average them. Do not let a low equipment loss hide a high human or environmental consequence.

Use the user's company risk matrix when it is supplied. If no company matrix is supplied, provide qualitative severity bands and the evidence needed for final scoring.

## Evidence Sources

Use these source-backed principles:

- OSHA recordability distinguishes death, days away from work, restricted work/job transfer, medical treatment beyond first aid, loss of consciousness, and significant diagnosed injury/illness.
- EPA human health risk assessment considers hazard identification, dose-response, exposure assessment, and risk characterization.
- EPA ecological risk assessment considers stressor, exposed ecological receptors, exposure magnitude, effects, and uncertainty.
- EPA RMP offsite consequence endpoints use toxic endpoints, 1 psi explosion overpressure, 5 kW/m2 radiant heat for 40 seconds, and lower flammability limit for flammables.
- CCPS Process Safety Metrics severity weighting uses safety/human health, direct cost, material release outside secondary containment, community impact, and off-site environmental impact categories. It distinguishes injury beyond first aid, days-away injury, fatality, third-party hospitalization/fatality, evacuation/shelter-in-place duration, and acute environmental cost or wildlife impact.

These are screening anchors, not a substitute for the user's company risk matrix.

Public source anchors:

- AIChE CCPS Process Safety Metrics Guide for Leading and Lagging Indicators, v4.1.
- OSHA 29 CFR 1904.7 general recording criteria for occupational injuries and illnesses.
- EPA human health risk assessment overview.
- EPA ecological risk assessment overview.
- EPA RMP offsite consequence analysis parameters in 40 CFR 68.22.

## Safety / Human Health Severity

Evaluate credible exposure before safeguards.

Extract:

- Event type: toxic release, asphyxiant release, corrosive exposure, hot liquid/steam, fire, explosion, pressure burst, projectile, rotating equipment failure.
- Material hazard from SDS: toxicity, flammability, corrosivity, temperature, pressure, oxygen displacement.
- Exposure route: inhalation, dermal, eye, ingestion, thermal radiation, blast overpressure, projectile.
- Exposed people: operators, maintenance workers, contractors, public/third party, occupied buildings.
- Exposure conditions: inventory, release rate, duration, ventilation, congestion/confinement, ignition probability, proximity, occupancy.
- Health outcome: first aid only, medical treatment beyond first aid, restricted work, days away, hospital admission, permanent disability, single fatality, multiple fatalities.

Qualitative scale:

| Band | Safety / human health basis |
| --- | --- |
| Catastrophic | Multiple fatalities, public fatality, or major accident exposure credible |
| Major | Single worker fatality, third-party hospital admission, permanent disability, irreversible serious health effect |
| Serious | Days-away injury, hospital treatment, serious burn/toxic/corrosive exposure, significant diagnosed illness |
| Moderate | Medical treatment beyond first aid, restricted work, reversible injury |
| Minor | First aid or negligible credible exposure |

Use EPA RMP endpoints as red flags for potentially serious offsite/public exposure: toxic endpoint reached, 1 psi explosion overpressure, 5 kW/m2 radiant heat for 40 seconds, or flammable cloud to LFL.

## Environmental Severity

Assess the credible unmitigated environmental impact, not merely that a leak occurred.

Extract:

- Material: hydrocarbon, toxic, corrosive, persistent, bioaccumulative, wastewater, contaminated firewater, gas/VOC, solid.
- Quantity/rate/duration and phase.
- Containment: inside equipment, secondary containment, closed drain, open drain, soil, waterway, atmosphere.
- Receptors: soil, groundwater, surface water, marine environment, protected area, public/community, wildlife.
- Effects: acute toxicity, oxygen depletion, fish kill/wildlife injury, long-term contamination, cleanup/remediation, regulatory reporting, offsite impact.
- Uncertainty: missing quantity, missing receptor, missing containment, missing SDS/ecotoxicity.

Qualitative scale:

| Band | Environmental basis |
| --- | --- |
| Catastrophic | Large offsite impact, major water/groundwater/marine impact, long-term remediation, large-scale wildlife injury/death |
| Major | Significant offsite or community environmental impact, medium-scale wildlife injury/death, major cleanup/remediation |
| Serious | Reportable area impact, release outside secondary containment with credible receptor exposure, moderate cleanup |
| Moderate | Local contained release, limited cleanup, no major receptor impact |
| Minor | Negligible release, no credible environmental pathway, fully contained with minimal cleanup |

Use environmental cost only when the user's matrix uses cost. Otherwise judge by receptor, quantity, duration, toxicity/persistence, containment, and remediation burden.

## Asset / Equipment Severity

For the money/equipment part, count only direct equipment/property damage and direct restoration impact.

Include:

- Damaged equipment repair or replacement.
- Instrument, piping, valve, insulation, electrical, structural, containment, or local cleanup needed to restore the equipment area.
- Direct production interruption/downtime only if the user's risk matrix includes downtime.

Do not include unless the user provides a rule:

- Reputation.
- Market share.
- Contract penalty.
- Corporate opportunity loss.
- Remote business interruption unrelated to the damaged equipment.

Extract:

- Equipment class and tag.
- Damage mode: rupture, leak, collapse, dry running, seal failure, overspeed, overheating, fire exposure, corrosion/erosion, tube rupture.
- Repair scope: minor repair, major overhaul, replacement, crane/lift, shutdown requirement, spare availability.
- Escalation: LOPC, fire/explosion, damage to adjacent equipment.
- Downtime: none, hours, days, weeks, months if matrix requires it.

Qualitative scale:

| Band | Asset/equipment basis |
| --- | --- |
| Catastrophic | Multiple major equipment losses, structural collapse, prolonged unit outage, or very high direct repair/replacement cost per matrix |
| Major | Major equipment replacement/large repair, significant outage, adjacent equipment damage |
| Serious | Equipment failure requiring repair/overhaul and planned/unplanned downtime |
| Moderate | Local equipment abnormality or repair with limited downtime |
| Minor | No meaningful equipment damage or minor repair only |

## Governing Severity Selection

Use this calculation pattern:

1. Assign `Safety severity`.
2. Assign `Environmental severity`.
3. Assign `Asset/equipment severity`.
4. Compare them using the company severity scale or qualitative order.
5. Select `Governing severity = highest credible of the three`.
6. Explain why the other two dimensions do not govern.

Example wording:

`Safety: Serious due to credible operator exposure requiring medical treatment. Environmental: Moderate because release remains in closed drain with limited cleanup. Asset: Minor because only seal replacement is expected. Governing severity: Serious (safety controls the risk ranking).`

## Missing Data Stop Points

Mark severity as incomplete when any governing basis is missing:

- SDS or material hazard.
- Inventory/release quantity/rate/duration.
- Occupancy/exposure basis.
- Containment and receptor pathway.
- Equipment repair/replacement/downtime basis.
- Company severity scale or risk matrix for numeric scoring.

Do not force a numeric severity from generic words such as `equipment damage`, `pollution`, `fire`, or `toxic release` without enough consequence evidence.

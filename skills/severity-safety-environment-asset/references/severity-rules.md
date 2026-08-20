# Severity Safety Environment Asset Rules

Converted from the source JSONL rule pack. Use these rules for HAZOP severity assessment across Safety, Environment, and Asset dimensions. Production loss, downtime loss, lost revenue, business interruption, opportunity cost, and flowrate multiplied by product price are excluded.

# Source: 01_safety_severity_rag.jsonl

## Schema - AutoHAZOP Severity RAG v1.0
- **Scope:** Severity evaluation only. Production loss is explicitly excluded.
- **Dimensions:** Safety, Environment, Asset

## SAFE-SRC-001 - loss of containment of flammable or toxic material
- **severity dimension:** Safety
- **rule group:** release_source
- **applicability:** Use when a deviation can create a hole, rupture, leak, relief discharge, vent discharge, seal leak, or open path to atmosphere.
- **not applicable if:** No credible material release outside normal containment; Closed-system upset with no exposure route
- **required inputs:** material hazard class; phase at release; pressure; temperature; inventory; line size/hole size; isolation time; release location
- **engineering logic:** Start safety severity from the release source. Estimate release rate, total quantity or duration, and phase/state before selecting fire, explosion, toxic, or exposure outcome.
- **severity indicators:** quantity released; release duration; phase: liquid/vapor/two-phase; operator proximity; ignition likelihood; toxic concentration potential
- **severity hint:** S1-S5 depending on outcome model and exposed people
- **increase severity if:** large inventory; delayed isolation; pressurized release; indoor/congested release; near occupied area
- **decrease severity if:** small inventory; rapid isolation; remote/open-air release; release captured by closed system
- **safeguards to check:** ESD; isolation valves; gas/fire detection; relief/vent system; dike/drainage; emergency response
- **retrieval keywords:** loss of containment; source model; release rate; release duration; total quantity released; release phase
- **source refs:** CCPS Consequence Analysis: source model logic, release rate/quantity/phase; CCPS HEP: initiating event and consequence chain

## SAFE-FLAM-001 - flammable liquid release
- **severity dimension:** Safety
- **rule group:** flammable_release
- **applicability:** Use for naphtha, hydrocarbon, solvent, LPG, or other flammable service where liquid release can form a pool, vapor cloud, or spray/jet.
- **not applicable if:** Material is nonflammable and cannot generate flammable vapor under scenario conditions
- **required inputs:** flash point; boiling point; operating temperature; vapor pressure; release pressure; pool area; ignition sources
- **engineering logic:** For flammable liquid, first decide whether release forms a liquid pool, vapor cloud, aerosol, or jet. Then branch to no ignition, immediate ignition, delayed ignition, pool fire, jet fire, flash fire, or VCE.
- **severity indicators:** flammable mass; pool size; vapor cloud size; ignition timing; distance to people
- **severity hint:** S2-S5
- **increase severity if:** release above flash point; large pool; congested area; ignition source present; operators nearby
- **decrease severity if:** below flash point with limited vapor generation; small contained spill; no ignition sources; remote area
- **safeguards to check:** hazardous area classification; ignition control; gas detector; fire detector; foam; dike; isolation
- **retrieval keywords:** flammable liquid release; pool formation; vaporization; delayed ignition; immediate ignition; naphtha
- **source refs:** CCPS Consequence Analysis: fire/explosion outcome logic; Lees: process plant fire and flash fire hazard

## SAFE-FIRE-001 - flammable liquid pool with immediate or delayed ignition
- **severity dimension:** Safety
- **rule group:** pool_fire
- **applicability:** Use when a liquid spill can accumulate on ground, inside bund, sump, trench, or low area and ignite.
- **not applicable if:** No liquid pool can form; Release is gas-only jet with no rainout/pool
- **required inputs:** pool diameter/area; burning duration; thermal radiation distance; people at exposed locations; escape route
- **engineering logic:** Pool fire severity is driven by thermal radiation, exposure duration, flame impingement, and exposed people. Localized pool fire without personnel exposure can be lower safety severity than pool fire impinging equipment or occupied areas.
- **severity indicators:** thermal radiation to workers; burn injury potential; fatality potential; blocked escape; fire escalation
- **severity hint:** S2-S5
- **increase severity if:** large pool; long duration; impinges equipment; near operators or control room; escape route blocked
- **decrease severity if:** small pool; short duration; remote/unoccupied area; fixed foam/water system effective
- **safeguards to check:** dike; foam system; firewater; fire/gas detection; ESD; remote isolation; fireproofing
- **retrieval keywords:** pool fire; thermal radiation; liquid pool; burn injury; fire duration
- **source refs:** CCPS Consequence Analysis: thermal radiation models for pool fires; Lees: pool fires and effects of fire injury

## SAFE-FIRE-002 - pressurized flammable release with immediate ignition
- **severity dimension:** Safety
- **rule group:** jet_fire
- **applicability:** Use for pressurized gas, two-phase, or liquid releases that produce a directional jet and ignite at or near release point.
- **not applicable if:** Release is nonpressurized pool only; No credible immediate ignition
- **required inputs:** release pressure; hole size; jet direction; impingement target; duration; people in jet/radiation zone
- **engineering logic:** Jet fire severity is high when the flame is directional, sustained, and impinges personnel, escape routes, pressure vessels, piping, or structural supports.
- **severity indicators:** direct flame contact; thermal radiation; impingement on occupied equipment area; duration until isolation
- **severity hint:** S3-S5
- **increase severity if:** high pressure; large hole; horizontal jet toward walkway/equipment; delayed isolation; impingement on vessel/tank
- **decrease severity if:** small leak; vertical/upward direction away from people; rapid ESD/isolation
- **safeguards to check:** ESD; remote-operated isolation; fire/gas detection; deluge; fireproofing; minimum manning
- **retrieval keywords:** jet fire; pressurized release; immediate ignition; thermal radiation; flame impingement
- **source refs:** CCPS Consequence Analysis: jet fire model category; Lees: jet flames and fire protection

## SAFE-FIRE-003 - flammable vapor cloud ignites without significant overpressure
- **severity dimension:** Safety
- **rule group:** flash_fire
- **applicability:** Use when delayed ignition of a dispersed flammable cloud can cause flame propagation through the cloud.
- **not applicable if:** Cloud diluted below LFL before ignition; No flammable vapor cloud forms
- **required inputs:** flammable cloud extent to LFL; UFL/LFL range; occupied locations inside cloud; escape/shelter possibility
- **engineering logic:** Flash fire severity depends primarily on whether people are inside the flammable cloud footprint and whether escape is possible before ignition. Direct flame contact and thermal radiation dominate; oxygen depletion may also matter.
- **severity indicators:** people within cloud footprint; fatal burn potential; cloud reaches occupied area; ignition timing
- **severity hint:** S3-S5
- **increase severity if:** cloud reaches operators/control room/maintenance area; night/limited visibility; no warning; high occupancy
- **decrease severity if:** remote cloud path; gas detection and evacuation before ignition; small cloud
- **safeguards to check:** gas detection; alarms; ESD; ignition source control; site layout separation; evacuation procedure
- **retrieval keywords:** flash fire; vapor cloud fire; LFL distance; direct flame contact; fatal burns
- **source refs:** CCPS Consequence Analysis: flash fire vs VCE outcome; Lees: vapor cloud/flash fire lethal thermal radiation

## SAFE-EXPL-001 - flammable vapor cloud with delayed ignition in congested or confined area
- **severity dimension:** Safety
- **rule group:** vapor_cloud_explosion
- **applicability:** Use when a large flammable vapor cloud can form and ignite before dilution below LFL, especially in congested process areas or buildings.
- **not applicable if:** No flammable vapor cloud; Cloud is remote/open without congestion and expected to burn as flash fire only
- **required inputs:** flammable mass; congestion/confinement; cloud volume; ignition source; occupied buildings; distance to receptors
- **engineering logic:** VCE severity is driven by blast overpressure, projectiles, structural damage, and number of people exposed. Congestion and confinement increase explosion potential.
- **severity indicators:** overpressure at occupied area; building damage; glass/projectile injury; fatality potential; off-site impact
- **severity hint:** S4-S5 for credible occupied exposure; S3-S4 for unoccupied local damage
- **increase severity if:** large cloud; congested area; near occupied building; delayed ignition; multiple people exposed
- **decrease severity if:** small cloud; open area; low occupancy; effective gas detection/isolation
- **safeguards to check:** gas detection; ESD; layout separation; blast-resistant control room; ignition control; ventilation
- **retrieval keywords:** vapor cloud explosion; VCE; overpressure; blast wave; congestion; occupied building
- **source refs:** CCPS Consequence Analysis: VCE main consequence overpressure; Lees: explosion hazards and vapor cloud fires/explosions

## SAFE-EXPL-002 - blast overpressure reaches personnel or occupied building
- **severity dimension:** Safety
- **rule group:** explosion_overpressure
- **applicability:** Use for VCE, confined explosion, physical explosion, BLEVE, or vessel rupture generating blast wave/projectiles.
- **not applicable if:** No credible explosion mechanism
- **required inputs:** peak side-on overpressure; distance to people/buildings; building type; projectile potential
- **engineering logic:** Safety severity increases from glass injury and minor structural effects to building collapse/fatality as overpressure and projectile effects increase.
- **severity indicators:** window breakage; structural damage; building collapse; projectiles; fatality potential
- **severity hint:** S2-S5
- **increase severity if:** people indoors behind glass; non-blast-rated building; projectiles from vessel rupture; occupied control room within endpoint
- **decrease severity if:** blast-resistant building; remote explosion; no occupancy
- **safeguards to check:** blast-resistant design; layout spacing; explosion venting; relief design; inerting; gas detection
- **retrieval keywords:** explosion overpressure; blast wave; projectile; building damage; fatality
- **source refs:** CCPS Consequence Analysis: explosion effects and damage tables; Lees: explosion injury/damage sections

## SAFE-TOX-001 - toxic gas/vapor/aerosol release or toxic combustion products
- **severity dimension:** Safety
- **rule group:** toxic_exposure
- **applicability:** Use when material has acute toxicity, decomposition products, combustion products, or asphyxiant effects that can expose people.
- **not applicable if:** Released material has no acute toxicity/asphyxiation concern and concentration cannot reach harmful level
- **required inputs:** SDS toxicity endpoints; IDLH/ERPG/AEGL/TLV if available; release rate; dispersion; exposure duration; people location
- **engineering logic:** Toxic exposure severity is based on concentration at receptor, exposure duration, dose-response, and ability to escape or shelter.
- **severity indicators:** IDLH exceedance; ERPG/AEGL exceedance; LC50/probit fatality potential; worker/public exposure
- **severity hint:** S2-S5
- **increase severity if:** high toxicity; indoors/confined accumulation; poor ventilation; near public/occupied building; no warning
- **decrease severity if:** low toxicity; small release; rapid dilution; effective detection/evacuation/shelter
- **safeguards to check:** toxic gas detection; ventilation; scrubber/absorber; respiratory PPE; emergency response; shelter/evacuation
- **retrieval keywords:** toxic exposure; toxic gas effects; dose response; probit; IDLH; ERPG; AEGL; dispersion
- **source refs:** CCPS Consequence Analysis: toxic effects and dispersion/effect models; Lees: toxic release and gas toxicity sections

## SAFE-OCC-001 - hazard endpoint reaches operator area, maintenance area, control room, road, or off-site public
- **severity dimension:** Safety
- **rule group:** occupied_area
- **applicability:** Use for fire, explosion, toxic, or asphyxiant endpoint intersecting an occupied location.
- **not applicable if:** Endpoint does not reach any occupied area and area is normally unmanned
- **required inputs:** occupied locations; headcount; work pattern; distance to endpoint; escape/shelter availability; time to warning
- **engineering logic:** Safety severity must reflect exposed population, not only physical event type. A smaller event in an occupied area can outrank a larger event in a remote unmanned area.
- **severity indicators:** single worker injury; multiple injuries; public exposure; control room exposure; fatality potential
- **severity hint:** S2-S5
- **increase severity if:** multiple workers; public/off-site people; night shift sleeping quarters; control room not blast/toxic protected
- **decrease severity if:** remote area; low occupancy; effective warning and evacuation; shelter-in-place available
- **safeguards to check:** site layout; muster/evacuation; alarms; shelter-in-place; blast/toxic-rated control room; permit to work control
- **retrieval keywords:** occupied area exposure; fatality potential; people exposed; escape; shelter in place; control room
- **source refs:** CCPS Consequence Analysis: effect models on people and mitigation factors; CCPS TRA: people exposed/injured as consequence measures

## SAFE-MIT-001 - credible safeguard or mitigation reduces exposure after release
- **severity dimension:** Safety
- **rule group:** mitigation
- **applicability:** Use after identifying unmitigated outcome to adjust mitigated severity only if safeguards are independent, reliable, and applicable.
- **not applicable if:** Safeguard is not present, not independent, not maintained, or not valid for the scenario
- **required inputs:** safeguard type; normal status; independence; response time; coverage; proof/testing evidence
- **engineering logic:** Safeguards may reduce likelihood or mitigated severity, but cannot erase the unmitigated consequence. Treat PPE and emergency response as weaker mitigation than engineered isolation/detection where exposure is fast.
- **severity indicators:** reduced duration; reduced people exposed; reduced release quantity; reduced radiation/overpressure/dose endpoint
- **severity hint:** Use for mitigated severity only
- **increase severity if:** safeguard unavailable; manual response too slow; single safeguard only; normal state unknown
- **decrease severity if:** automatic ESD; rapid isolation; effective detection; passive protection; verified evacuation/shelter
- **safeguards to check:** detectors; alarms; interlocks; remote isolation; dike; foam/deluge; PPE; emergency response
- **retrieval keywords:** mitigation factors; emergency response; shelter in place; containment dikes; ESD; isolation
- **source refs:** CCPS Consequence Analysis: mitigation factors in overall consequence logic; CCPS HEP: safeguards and layers of protection

## SAFE-SCALE-001 - map safety consequence to S1-S5
- **severity dimension:** Safety
- **rule group:** severity_scale
- **applicability:** Use as default qualitative scale when company matrix is unavailable.
- **not applicable if:** Company risk matrix provides stricter definitions
- **required inputs:** injury severity; number of people exposed; fatality potential; public/off-site exposure
- **engineering logic:** S1=no injury or first-aid only; S2=minor recordable injury; S3=serious injury or one person potentially hospitalized; S4=single fatality potential or multiple serious injuries; S5=multiple fatalities or public fatality potential.
- **severity indicators:** first aid; recordable injury; serious injury; single fatality; multiple fatalities; public exposure
- **severity hint:** S1-S5
- **increase severity if:** off-site public exposure; occupied building affected; fast-onset event with no escape; multiple people exposed
- **decrease severity if:** unmanned area; warning time; shelter/escape effective
- **safeguards to check:** company risk matrix; occupied area register; emergency response plan
- **retrieval keywords:** safety severity; fatality; serious injury; people exposed; risk matrix
- **source refs:** CCPS/Lees qualitative severity concepts; must be calibrated to Company Risk Matrix

# Source: 02_environment_severity_rag.jsonl

## Schema - AutoHAZOP Severity RAG v1.0
- **Scope:** Severity evaluation only. Production loss is explicitly excluded.
- **Dimensions:** Safety, Environment, Asset

## ENV-LOC-001 - no loss of containment
- **severity dimension:** Environment
- **rule group:** loss_of_containment
- **applicability:** Use when deviation causes process upset but no material leaves closed equipment, pipe, tank, drain, or designed vent/treatment path.
- **not applicable if:** external leak; spill; vent to atmosphere; relief to open system; drain to environment
- **required inputs:** containment boundary; normal vent/drain routing; leak path; relief destination
- **engineering logic:** If there is no environmental release, environmental severity normally remains S1 even if safety or asset severity is higher.
- **severity indicators:** no spill; no emission; no drain release; no cleanup
- **severity hint:** S1
- **increase severity if:** hidden release path exists; relief/vent discharges to atmosphere; drain bypasses treatment
- **decrease severity if:** confirmed closed system; closed drain/treatment available
- **safeguards to check:** closed drain; relief routing; secondary containment; leak detection
- **retrieval keywords:** no release; no loss of containment; closed system; environmental severity S1
- **source refs:** CCPS Consequence Analysis: accidents usually begin with loss of containment; environmental impact is separate from safety/property

## ENV-SPILL-001 - contained spill
- **severity dimension:** Environment
- **rule group:** contained_spill
- **applicability:** Use when liquid release is captured within bund, dike, drip tray, sump, paved process area, or closed drain without soil/water impact.
- **not applicable if:** spill escapes containment; storm drain/soil/water affected
- **required inputs:** spill quantity; bund/dike capacity; surface type; drain routing; cleanup method
- **engineering logic:** Contained spill affects environment mainly through cleanup waste and VOC emission. Severity is lower if contained and recovered locally.
- **severity indicators:** local cleanup; waste absorbent disposal; no off-site receptor; no soil/water contact
- **severity hint:** S2-S3
- **increase severity if:** large quantity; toxic/persistent material; VOC emission significant; formal cleanup contractor needed
- **decrease severity if:** minor drip; fully recovered; closed drain to treatment; no reportable threshold
- **safeguards to check:** bund/dike; closed drain; spill kit; isolation; operator response
- **retrieval keywords:** contained spill; bund; dike; closed drain; local cleanup
- **source refs:** Lees: bunds and containment; CCPS Consequence Analysis: containment dikes as mitigation

## ENV-SPILL-002 - uncontained liquid spill
- **severity dimension:** Environment
- **rule group:** uncontained_spill
- **applicability:** Use when release escapes process containment and can spread over ground, pavement, soil, stormwater, or off-site.
- **not applicable if:** release remains fully inside adequate secondary containment
- **required inputs:** release quantity; slope/grade; surface type; distance to drains/soil/water; isolation time
- **engineering logic:** Uncontained spills increase severity because material can migrate to environmental receptors and require larger cleanup/remediation.
- **severity indicators:** uncontrolled spreading; cleanup area; soil/drain exposure; off-site migration potential
- **severity hint:** S3-S5
- **increase severity if:** large inventory; storm drain nearby; rainfall; permeable soil; sensitive receptor
- **decrease severity if:** rapid isolation; temporary containment deployed; impermeable paved area with recovery
- **safeguards to check:** emergency isolation; spill response; temporary diking; drain isolation; site grading
- **retrieval keywords:** uncontained spill; spill migration; cleanup; environmental receptor
- **source refs:** CCPS TRA: environmental risks from spills and contaminated area; Lees: leaks and spillages

## ENV-DRAIN-001 - release to drain or sewer
- **severity dimension:** Environment
- **rule group:** release_to_drain
- **applicability:** Use when liquid or contaminated firewater can enter floor drain, oily-water sewer, wastewater system, or stormwater drain.
- **not applicable if:** drain is isolated/closed and contents are fully recovered
- **required inputs:** drain type; drain destination; treatment capacity; material compatibility; isolation valves
- **engineering logic:** Severity depends on drain destination. Closed oily-water/treatment systems reduce severity; storm drains or uncontrolled drains increase severity.
- **severity indicators:** closed drain vs storm drain; treatment overload; reportable discharge; off-site water path
- **severity hint:** S2-S5
- **increase severity if:** storm drain; uncontrolled sewer; WWT overload; flammable/toxic material; firewater runoff
- **decrease severity if:** closed drain to designed treatment; drain isolation; small quantity
- **safeguards to check:** drain isolation valve; oily-water sewer; WWT capacity; spill berms; firewater retention
- **retrieval keywords:** release to drain; storm drain; closed drain; wastewater treatment; firewater runoff
- **source refs:** CCPS TRA: environmental receptors and impacted areas; Lees: drainage and effluents

## ENV-SOIL-001 - chemical reaches soil
- **severity dimension:** Environment
- **rule group:** release_to_soil
- **applicability:** Use when spill contacts unpaved ground, permeable surface, damaged bund floor, or contaminated soil.
- **not applicable if:** impermeable surface with full recovery before soil contact
- **required inputs:** chemical mobility; soil type; quantity; duration; excavation/remediation need; groundwater depth
- **engineering logic:** Soil contact raises severity because remediation, contaminated waste disposal, and possible groundwater migration become credible.
- **severity indicators:** soil excavation; contaminated soil volume; groundwater pathway; long-term monitoring
- **severity hint:** S3-S5
- **increase severity if:** high mobility; persistent/toxic material; large quantity; near groundwater; rainfall
- **decrease severity if:** low quantity; low mobility; quick excavation; impermeable liner
- **safeguards to check:** impermeable paving; bund floor integrity; spill response; groundwater monitoring
- **retrieval keywords:** release to soil; soil contamination; groundwater pathway; remediation
- **source refs:** CCPS TRA: soil and groundwater receptors; environmental property behavior

## ENV-WATER-001 - release reaches surface water
- **severity dimension:** Environment
- **rule group:** surface_water
- **applicability:** Use when spill enters river, canal, pond, sea, stormwater outfall, or drainage leading to surface water.
- **not applicable if:** water pathway isolated before contact
- **required inputs:** quantity reaching water; material floats/sinks/dissolves; aquatic toxicity; flow/current; sensitive habitat
- **engineering logic:** Surface water impact normally produces high environmental severity due to rapid spread, ecological exposure, public visibility, cleanup complexity, and regulatory attention.
- **severity indicators:** water body contaminated; aquatic toxicity; boom/skimmer cleanup; public report; habitat impact
- **severity hint:** S4-S5
- **increase severity if:** large quantity; toxic or persistent material; drinking water intake; sensitive habitat; off-site spread
- **decrease severity if:** very small contained quantity; rapid boom/recovery; nonpersistent low-toxicity material
- **safeguards to check:** storm drain isolation; retention pond; oil boom; emergency response; spill barriers
- **retrieval keywords:** release to surface water; river contamination; oil spill; aquatic toxicity; habitat restoration
- **source refs:** CCPS TRA: surface water/drinking water receptors and oil spill/habitat restoration

## ENV-GW-001 - release can reach groundwater or drinking water source
- **severity dimension:** Environment
- **rule group:** groundwater
- **applicability:** Use when chemical can infiltrate soil or reach groundwater/drinking water due to mobility, solubility, persistence, or site geology.
- **not applicable if:** impermeable containment prevents infiltration
- **required inputs:** solubility; specific gravity; partition coefficient; adsorption coefficient; soil permeability; groundwater depth
- **engineering logic:** Groundwater or drinking water impact should be treated as severe because remediation and monitoring can be long-term.
- **severity indicators:** groundwater monitoring; drinking water concern; long-term remediation; public/regulatory impact
- **severity hint:** S5
- **increase severity if:** high solubility; persistent pollutant; DNAPL/LNAPL behavior; near well/drinking water
- **decrease severity if:** confirmed no pathway; rapid recovery; impermeable secondary containment
- **safeguards to check:** secondary containment; groundwater monitoring wells; drain isolation; spill response
- **retrieval keywords:** groundwater contamination; drinking water source; solubility; adsorption coefficient; octanol water partition coefficient
- **source refs:** CCPS TRA: solubility, specific gravity, adsorption and partitioning for water/soil interaction

## ENV-VOC-001 - VOC or hydrocarbon vapor release to atmosphere
- **severity dimension:** Environment
- **rule group:** VOC_release
- **applicability:** Use when volatile liquid/gas release creates atmospheric emission but not necessarily soil/water contamination.
- **not applicable if:** material is nonvolatile and no aerosol/vapor emission
- **required inputs:** vapor pressure; release duration; mass emitted; toxicity; odor threshold; regulatory emission concern
- **engineering logic:** VOC environmental severity depends on emitted mass, toxicity/persistence, duration, and regulatory/reportable emission threshold. Short releases may be lower environment severity than liquid spill to water/soil.
- **severity indicators:** VOC emission; odor complaint; reportable release; off-site plume
- **severity hint:** S2-S4
- **increase severity if:** large vapor mass; toxic VOC; off-site odor/exposure; long duration
- **decrease severity if:** small transient emission; rapid isolation; vapor recovery/scrubber
- **safeguards to check:** vapor recovery; activated carbon; scrubber; gas detection; closed vent
- **retrieval keywords:** VOC release; vapor emission; atmospheric release; hydrocarbon vapor; odor
- **source refs:** CCPS Consequence Analysis: atmospheric dispersion; Lees: emissions and fugitive emissions

## ENV-HC-001 - hydrocarbon/naphtha spill
- **severity dimension:** Environment
- **rule group:** hydrocarbon_contamination
- **applicability:** Use for naphtha, gasoline-like hydrocarbons, petroleum liquids, solvent hydrocarbons, and oily materials.
- **not applicable if:** nonhydrocarbon non-oily material; use SDS-specific environmental rules instead
- **required inputs:** spill quantity; vapor pressure; water solubility; floating/sinking behavior; soil contact; drain/water contact
- **engineering logic:** Hydrocarbon contamination severity is low to moderate if fully contained and recovered, but high if it reaches soil, stormwater, surface water, groundwater, or sensitive habitat.
- **severity indicators:** oil sheen; contaminated soil; flammable vapor; VOC emission; cleanup waste
- **severity hint:** S2-S5
- **increase severity if:** uncontained; reaches water; large surface area; near storm drain; persistent fraction
- **decrease severity if:** inside bund; oil-water separator designed; rapid recovery; small quantity
- **safeguards to check:** bund; oil-water separator; storm drain block; foam/vapor suppression; spill kit
- **retrieval keywords:** hydrocarbon contamination; naphtha spill; oil spill; VOC; soil water contamination
- **source refs:** CCPS TRA: oil spill and environmental risk; Lees: petroleum storage, bunds, spillages

## ENV-CLEAN-001 - cleanup/remediation required
- **severity dimension:** Environment
- **rule group:** cleanup_requirement
- **applicability:** Use once environmental release outcome is identified.
- **not applicable if:** no release or fully internal process upset
- **required inputs:** cleanup scope; waste disposal type; third-party contractor needed; soil/water remediation; monitoring duration
- **engineering logic:** Cleanup burden maps environmental consequence to severity. Local housekeeping cleanup is minor; specialist cleanup/reportable spill is moderate; remediation/habitat restoration/long-term monitoring is severe.
- **severity indicators:** local cleanup; specialist cleanup; remediation; habitat restoration; monitoring
- **severity hint:** S2-S5
- **increase severity if:** hazardous waste disposal; off-site cleanup; habitat restoration; long-term monitoring
- **decrease severity if:** local absorbent cleanup only; no contaminated media; no reportable threshold
- **safeguards to check:** spill response plan; waste management procedure; contractor response; containment
- **retrieval keywords:** cleanup requirement; remediation; contaminated waste; habitat restoration; spill cleanup
- **source refs:** CCPS TRA: cleanup cost and habitat restoration concepts; Lees: pollution/spill loss prevention

## ENV-REG-001 - reportable environmental incident
- **severity dimension:** Environment
- **rule group:** reportable_incident
- **applicability:** Use when release may exceed legal/company reporting thresholds or affect public/off-site receptors.
- **not applicable if:** release below threshold and fully contained with no environmental media affected
- **required inputs:** local reporting threshold; material classification; quantity released; off-site impact; water/soil contact
- **engineering logic:** Reportability is a severity escalator but not the only criterion. A reportable contained release may be S3, while off-site or water/groundwater impact may be S4-S5.
- **severity indicators:** agency notification; public complaint; reportable spill; permit exceedance
- **severity hint:** S3-S5
- **increase severity if:** off-site impact; water body; drinking water; sensitive habitat; regulatory investigation
- **decrease severity if:** internal notification only; contained small quantity; no media impact
- **safeguards to check:** environmental reporting procedure; spill threshold list; SDS; permit limits
- **retrieval keywords:** reportable environmental incident; regulatory notification; spill threshold; permit exceedance
- **source refs:** CCPS Consequence Analysis: regulated release scenarios; CCPS TRA: environmental risk development

## ENV-SCALE-001 - map environmental consequence to S1-S5
- **severity dimension:** Environment
- **rule group:** severity_scale
- **applicability:** Use as default qualitative scale when company environmental matrix is unavailable.
- **not applicable if:** Company environmental risk matrix gives stricter definitions
- **required inputs:** release status; containment; affected receptor; cleanup/remediation; reportability
- **engineering logic:** S1=no release; S2=minor contained cleanup; S3=contained/significant on-site cleanup or reportable spill; S4=uncontained soil/drain/surface water impact or major on-site remediation; S5=groundwater/drinking water/sensitive habitat/off-site or long-term damage.
- **severity indicators:** contained vs uncontained; soil/water/groundwater; cleanup level; regulatory impact
- **severity hint:** S1-S5
- **increase severity if:** sensitive receptor; persistence; large release; off-site migration
- **decrease severity if:** full containment; rapid recovery; no media contact
- **safeguards to check:** company environmental risk matrix; SDS; site drainage map; spill response plan
- **retrieval keywords:** environment severity scale; contained spill; uncontained spill; soil water groundwater; cleanup
- **source refs:** Lees severity categories and environmental damage; CCPS TRA environmental risk concepts

# Source: 03_asset_damage_severity_rag.jsonl

## Schema - AutoHAZOP Severity RAG v1.0
- **Scope:** Severity evaluation only. Production loss is explicitly excluded.
- **Dimensions:** Safety, Environment, Asset

## AST-NODMG-001 - no physical damage
- **severity dimension:** Asset
- **rule group:** direct_damage
- **applicability:** Use when deviation affects operation but equipment remains within mechanical/design limits and no repair/replacement is required.
- **not applicable if:** overpressure; vacuum collapse; fire exposure; explosion damage; pump damage; pipe rupture; seal failure
- **required inputs:** design pressure/temperature; operating excursion; safeguard action; inspection result
- **engineering logic:** Asset severity should be S1 if consequence is operational only and does not require physical repair, replacement, or inspection beyond routine checks.
- **severity indicators:** no repair; no replacement; no mechanical overstress; no damage
- **severity hint:** S1
- **increase severity if:** inspection required due to suspected overstress; safety device lifted with damage; thermal/mechanical excursion
- **decrease severity if:** within design limit; safeguard prevented damage
- **safeguards to check:** design margin; alarm/trip; PSV/PVV; operating procedure
- **retrieval keywords:** no physical damage; within design pressure; asset severity S1
- **source refs:** CCPS HEP/Consequence Analysis: property damage as distinct consequence

## AST-INST-001 - instrument, gauge, transmitter, sensor, analyzer, switch, or cubicle damaged
- **severity dimension:** Asset
- **rule group:** instrument_damage
- **applicability:** Use when incident physically damages instrumentation or requires direct instrument replacement.
- **not applicable if:** instrument reading failure only without physical damage; treat as cause not asset consequence
- **required inputs:** instrument type; damage mode; replacement cost band; location; fire/blast exposure
- **engineering logic:** Instrument damage is usually low to moderate asset severity unless it causes broader equipment damage, shutdown is excluded, or safety function impairment leads to escalation.
- **severity indicators:** single instrument replacement; multiple instruments/cabinet damage; controls damaged
- **severity hint:** S1-S3
- **increase severity if:** multiple instruments; control/safety cabinet damaged; blast/fire exposure; hard-to-access critical instrument
- **decrease severity if:** single low-cost field instrument; spare available; no physical process damage
- **safeguards to check:** instrument protection; blast/fireproof cabinet; redundant sensor; spares
- **retrieval keywords:** instrument damage; gauge broken; controls damaged; instrument cubicle
- **source refs:** CCPS Consequence Analysis: overpressure equipment damage table includes instruments/controls

## AST-VALVE-001 - valve, actuator, valve packing, or emergency isolation valve physically damaged
- **severity dimension:** Asset
- **rule group:** valve_damage
- **applicability:** Use when valve repair/replacement is a consequence, not merely initiating failure.
- **not applicable if:** valve stuck/fails as initiating cause but no additional physical damage occurs
- **required inputs:** valve size/class; service; failure mode; leakage/rupture; fire/blast exposure
- **engineering logic:** Valve damage ranges from minor packing repair to valve replacement. Severity increases with large-bore/high-pressure/hazardous service or if valve damage causes sustained release.
- **severity indicators:** packing repair; actuator replacement; full valve replacement; leak/rupture
- **severity hint:** S1-S3 normally; S4 if major hazardous release/fire damage accompanies valve loss
- **increase severity if:** large bore; high pressure; flammable/toxic service; fire exposure; cannot isolate
- **decrease severity if:** small valve; replaceable actuator; spare available
- **safeguards to check:** bypass isolation; double block; fire-safe valve; inspection/maintenance
- **retrieval keywords:** valve damage; actuator damage; packing leak; valve replacement
- **source refs:** Lees: pipework/valves and loss prevention; CCPS source model initiating releases

## AST-PUMP-001 - pump dry running
- **severity dimension:** Asset
- **rule group:** pump_damage
- **applicability:** Use when low/no suction, loss of liquid, closed suction, or tank low level allows pump to run without adequate liquid.
- **not applicable if:** pump is stopped before dry running or has dry-run-rated design
- **required inputs:** pump type; duration; seal type; bearing lubrication; low level trip; minimum flow
- **engineering logic:** Dry running can damage seals, bearings, impeller, and casing. Severity depends on duration, pump size, and whether damage is limited to seal or becomes catastrophic.
- **severity indicators:** seal failure; bearing damage; impeller damage; casing damage; release at seal
- **severity hint:** S2-S4
- **increase severity if:** large API pump; flammable service; no low-low level trip; long duration; seal leak creates LOC
- **decrease severity if:** rapid trip; seal-less design; short duration; spare pump available (for asset consequence do not count production loss)
- **safeguards to check:** low-low level trip; low flow trip; seal monitoring; minimum flow recycle; operator alarm
- **retrieval keywords:** pump dry running; seal failure; bearing damage; impeller damage; pump casing
- **source refs:** Lees: centrifugal pump maloperation damage includes dry running

## AST-PUMP-002 - pump cavitation
- **severity dimension:** Asset
- **rule group:** pump_damage
- **applicability:** Use when inadequate NPSH, blocked suction, low suction level, hot liquid, or flashing causes cavitation.
- **not applicable if:** NPSH adequate and no cavitation symptoms credible
- **required inputs:** NPSH available/required; temperature; vapor pressure; suction line losses; flow condition
- **engineering logic:** Cavitation causes bubble collapse on impeller, pitting, vibration, and progressive impeller damage. Severity rises with duration and pump criticality/size.
- **severity indicators:** impeller pitting; vibration; bearing damage; seal damage; pump replacement
- **severity hint:** S2-S4
- **increase severity if:** long operation while cavitating; large/high head pump; flammable seal leak; low flow unstable operation
- **decrease severity if:** early detection; adequate NPSH margin; automatic trip; short exposure
- **safeguards to check:** NPSH design margin; low suction pressure alarm; vibration monitoring; minimum flow recycle
- **retrieval keywords:** pump cavitation; NPSH; impeller pitting; pump vibration; low suction pressure
- **source refs:** Lees: cavitation pitting and destructive impeller damage

## AST-PUMP-003 - pump deadheading or blocked discharge
- **severity dimension:** Asset
- **rule group:** pump_damage
- **applicability:** Use when pump operates against closed outlet, blocked discharge, closed downstream valve, or failed control valve closed.
- **not applicable if:** minimum flow bypass opens and limits temperature/pressure
- **required inputs:** pump curve; shutoff head; blocked duration; temperature rise; relief/bypass; casing pressure rating
- **engineering logic:** Deadheading can generate heat and pressure leading to seal damage, casing damage, rupture, or hazardous reaction in pump depending on fluid.
- **severity indicators:** temperature rise; pressure rise; seal failure; casing rupture; pump replacement
- **severity hint:** S2-S4
- **increase severity if:** no bypass; hazardous/reactive fluid; high horsepower pump; long duration
- **decrease severity if:** automatic minimum flow; thermal/pressure trip; rapid operator response
- **safeguards to check:** minimum flow recycle; kickback line; pump high temperature trip; pump discharge pressure trip; PSV
- **retrieval keywords:** pump deadheading; blocked discharge; minimum flow bypass; kickback line; pump rupture
- **source refs:** Lees: deadheading heat/pressure and rupture; bypass/kickback countermeasure

## AST-PIPE-001 - pipe rupture, gasket failure, flange leak, or line break
- **severity dimension:** Asset
- **rule group:** piping_damage
- **applicability:** Use when pressure, corrosion, erosion, vibration, thermal stress, or external force causes physical piping damage.
- **not applicable if:** small controllable leak with no repair beyond gasket tightening; use lower severity
- **required inputs:** pipe size; pressure class; material; damage extent; isolation valves; hazardous service
- **engineering logic:** Piping damage severity depends on repair scope and whether the failure causes LOC/fire/explosion. Direct asset damage excludes production loss but includes pipe replacement and associated damaged supports/insulation.
- **severity indicators:** gasket repair; pipe spool replacement; support damage; line rupture; secondary equipment damage
- **severity hint:** S2-S4
- **increase severity if:** large diameter; high pressure; flammable/toxic service; fire/explosion damage; multiple spools
- **decrease severity if:** small bore; isolatable; minor gasket repair
- **safeguards to check:** pressure relief; inspection/corrosion monitoring; supports; vibration control; isolation valves
- **retrieval keywords:** pipe rupture; line break; gasket failure; piping replacement; flange leak
- **source refs:** CCPS Consequence Analysis: releases from pipes/tanks/vessels; Lees: pressure systems and pipework

## AST-TANK-001 - tank overpressure
- **severity dimension:** Asset
- **rule group:** tank_damage
- **applicability:** Use when blocked vent, excess inflow, fire heating, vapor generation, or nitrogen blanketing/control failure can exceed tank design pressure.
- **not applicable if:** PVV/venting capacity confirmed adequate and pressure remains within design limits
- **required inputs:** tank design pressure; operating pressure; PVV capacity/status; inbreathing/outbreathing path; fire case; inlet flow
- **engineering logic:** Tank overpressure can damage roof, shell, seams, floating roof, vents, or cause rupture. Severity depends on pressure excursion and tank size/inventory.
- **severity indicators:** PVV lift only; roof damage; shell deformation; tank rupture; LOC
- **severity hint:** S2-S5
- **increase severity if:** blocked PVV/vent; fire exposure; large atmospheric tank; flammable inventory; no emergency vent
- **decrease severity if:** adequate PVV/emergency vent; alarm/interlock stops inflow; pressure within design
- **safeguards to check:** PVV; emergency vent; high pressure alarm; inlet shutdown; fire relief case; blanketing control
- **retrieval keywords:** tank overpressure; PVV; vent blockage; roof damage; tank rupture; outbreathing
- **source refs:** CCPS/Lees: tank relief/overpressure concepts; CCPS TRA: relief systems prevent rupture

## AST-TANK-002 - tank vacuum collapse
- **severity dimension:** Asset
- **rule group:** tank_damage
- **applicability:** Use when pump-out, cooling, blocked inbreathing, nitrogen blanketing failure, or vent blockage can create excessive vacuum in atmospheric tank.
- **not applicable if:** vacuum relief/inbreathing capacity adequate and vacuum remains within design
- **required inputs:** tank vacuum design; pump-out rate; inbreathing capacity; PVV status; blanketing PCV status; temperature change
- **engineering logic:** Vacuum can collapse or deform atmospheric tanks, roofs, and shells. Direct asset severity can be high even without fire if tank shell/roof repair or replacement is needed.
- **severity indicators:** roof deformation; shell buckling; floating roof damage; tank collapse
- **severity hint:** S3-S5
- **increase severity if:** blocked vent; high pump-out rate; weak atmospheric tank; large tank; no vacuum breaker
- **decrease severity if:** adequate PVV/vacuum breaker; pump trip; low pressure alarm
- **safeguards to check:** PVV/vacuum breaker; nitrogen inbreathing PCV; low pressure alarm/trip; pump shutdown
- **retrieval keywords:** tank vacuum collapse; blocked inbreathing; vacuum breaker; tank shell buckling; PVV
- **source refs:** CCPS/Lees: pressure/vacuum relief to prevent tank rupture or collapse

## AST-FIRE-001 - fire exposure to process equipment
- **severity dimension:** Asset
- **rule group:** fire_damage
- **applicability:** Use when pool fire, jet fire, flash fire, fireball, or engulfing fire exposes equipment, structures, cables, instruments, or tanks.
- **not applicable if:** fire endpoint does not reach equipment and no heat damage credible
- **required inputs:** fire type; duration; thermal radiation/impingement; equipment fireproofing; firewater/deluge; equipment type
- **engineering logic:** Fire damage severity depends on direct flame impingement, thermal radiation, duration, and equipment vulnerability. Fire can damage instruments/cables, deform steel, weaken vessels, and escalate to rupture.
- **severity indicators:** cable/instrument damage; paint/insulation damage; steel deformation; vessel weakening; equipment replacement
- **severity hint:** S2-S5
- **increase severity if:** jet fire impingement; long pool fire; no fireproofing; pressure vessel/tank exposed; firewater unavailable
- **decrease severity if:** short exposure; passive fire protection; effective deluge/foam; remote equipment
- **safeguards to check:** fireproofing; deluge; foam; firewater; equipment spacing; fire/gas detection
- **retrieval keywords:** fire damage to equipment; thermal radiation damage; flame impingement; fireproofing
- **source refs:** CCPS Consequence Analysis: thermal effects/damage assessment; Lees: effects of fire damage and fire protection

## AST-EXPL-001 - explosion overpressure affects process equipment or buildings
- **severity dimension:** Asset
- **rule group:** explosion_damage
- **applicability:** Use when VCE, confined explosion, physical explosion, BLEVE, or vessel rupture produces blast overpressure/projectiles.
- **not applicable if:** no credible blast/projectile effect at equipment
- **required inputs:** peak overpressure; distance; equipment type; building type; projectile potential
- **engineering logic:** Overpressure can break gauges/windows at low levels, damage instruments/controls, break piping, move equipment, rupture storage tanks, or destroy buildings at high levels.
- **severity indicators:** instrument/control damage; piping breaks; unit moves; tank rupture; building collapse; total equipment loss
- **severity hint:** S2-S5
- **increase severity if:** high overpressure; projectiles; nearby occupied/control building; multiple equipment affected
- **decrease severity if:** blast-rated design; remote endpoint; minor glass/instrument damage only
- **safeguards to check:** layout spacing; blast-resistant design; explosion venting; inerting; gas detection
- **retrieval keywords:** explosion damage; overpressure damage; process equipment damage; piping breaks; tank rupture
- **source refs:** CCPS Consequence Analysis: overpressure damage estimates for process equipment

## AST-SCALE-001 - map direct equipment damage to S1-S5
- **severity dimension:** Asset
- **rule group:** severity_scale
- **applicability:** Use as default direct asset severity scale when company asset matrix/cost bands are unavailable.
- **not applicable if:** Company asset severity matrix provides cost thresholds
- **required inputs:** equipment affected; damage mechanism; repair scope; replacement scope; direct repair/replacement cost band
- **engineering logic:** S1=no damage/routine reset; S2=minor component repair or single small instrument; S3=repair/replacement of valve, instrument cabinet, pump seal/impeller, small piping; S4=major pump/piping/tank/vessel repair or localized fire/blast damage; S5=major vessel/tank/column/reactor loss, building collapse, or multiple equipment total loss. Do not include production loss.
- **severity indicators:** repair scope; replacement scope; direct equipment cost; equipment class
- **severity hint:** S1-S5
- **increase severity if:** large equipment; pressure vessel/tank damage; fire/explosion spread; multiple equipment damaged
- **decrease severity if:** small replaceable component; spare available (only for repair scope, not production loss); minor repair
- **safeguards to check:** company cost matrix; equipment list; inspection records; API/Perry/Turton/Peters cost data
- **retrieval keywords:** asset severity; direct equipment damage; repair cost; replacement cost; property damage
- **source refs:** Lees severity categories/property damage; CCPS damage assessment


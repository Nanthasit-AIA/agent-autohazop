# Hydrocarbon Processing Refining Processes Context

Use this reference to extract refinery process-unit context from the uploaded PDF named like an instrumentation-symbols document but whose extracted content is actually a Hydrocarbon Processing refining-process handbook/catalog plus related sulfur/liquid-redox process material.

This reference is not ISA-5.1 and must not be used to interpret instrument tag letters or P&ID instrument symbols. It is useful for HAZOP/P&ID orientation when a refinery process unit name, licensed technology, catalyst service, feed/product slate, or process block appears in project documents.

## Source Traceability

- Source content identified from extracted pages: `Hydrocarbon Processing` refining process handbook/index and process entries.
- Pages 1-5: refining process handbook overview, process index, company index, equipment/service provider index.
- Pages 6 onward: process entries using a repeated structure such as application, products, description, yields/economics, utilities, installations, references, and licensor.
- Later pages include detailed sulfur treating/liquid redox material such as LO-CAT/Stretford-style context, operating conditions, reliability, sampling, and spent-caustic/treating discussion.

## Applies To

- Refinery process context extraction.
- Early HAZOP node orientation when only a process name or licensor block is known.
- PFD/P&ID review where the agent needs to recognize typical feeds, products, utilities, catalysts, side streams, recycle streams, waste streams, and high-level unit boundaries.
- Building a checklist of process-specific questions before reading detailed P&IDs, line lists, datasheets, procedures, relief documents, or cause-and-effect charts.

## Does Not Apply To

- ISA instrument tag interpretation.
- Final process design, equipment sizing, catalyst design, licensed-process guarantee review, economics validation, or code compliance.
- Treating vendor process descriptions as the as-built project design.
- Crediting a technology feature as a safeguard or IPL without project-specific verification.

## Extraction Fields

For each process entry, capture:

```yaml
process_context:
  process_name:
  licensor_or_vendor:
  application:
  feed_streams:
  product_streams:
  byproducts_or_waste:
  main_process_sections:
  main_equipment_clues:
  catalyst_or_chemical_system:
  recycle_streams:
  utility_requirements:
  operating_severity_clues:
  installation_or_scale_clues:
hazop_orientation:
  likely_nodes:
  likely_deviations:
  likely_safeguards_to_verify:
  likely_documents_needed:
  assumptions_not_to_make:
```

## Process Families In The File

Use the process index as a navigation aid. The file includes refinery technology families such as:

- Alkylation and alkylation-feed preparation.
- Aromatics extraction/recovery and benzene reduction.
- Catalytic cracking, deep catalytic cracking, catalytic reforming, catalytic dewaxing.
- Coking and deep thermal conversion.
- Crude/vacuum distillation and crude topping.
- Deasphalting, visbreaking, asphalt oxidation.
- Diesel upgrading and ultra-low-sulfur diesel.
- Electrical desalting.
- Ether/ETBE/MTBE technologies.
- Fluid catalytic cracking and pretreatment.
- Gas treating and H2S removal.
- Gasification and hydrogen production/recovery.
- Hydrocracking, hydrodesulfurization, hydrotreating, hydrofinishing, hydroprocessing.
- Isomerization, isooctane/isooctene, oligomerization, olefins recovery.
- NOx/SOx abatement.
- Sour gas treatment, sulfur recovery, sulfur degassing, spent acid regeneration.
- Sweetening and treating of gases, gasoline, jet fuel, kerosene, light liquids, reformer products, spent caustic, and phenolic caustic.
- White oil, wax, lube extraction, lube treating, and dewaxing.

Do not infer that a project has every section listed in a generic process entry. Use the entry only as a prompt for what to look for.

## How To Use For P&ID/HAZOP Context

When a refinery unit or process name appears:

1. Identify the process family and intended conversion/removal/separation duty.
2. Extract likely feeds and products from the project documents first; use this reference only to recognize typical streams.
3. Identify typical process sections: feed preparation, reactor/contacting, separation/fractionation, recycle, regeneration, product treating, waste handling, and utility systems.
4. Map P&ID nodes around major functions rather than licensor marketing names.
5. Look for catalysts, acids, caustic, hydrogen, air/oxygen, amine, water wash, solvents, sulfur species, or other chemicals that change hazard context.
6. Look for recycle and regeneration streams because they often drive HAZOP deviations and abnormal operating cases.
7. Look for waste or disposal paths such as spent acid, spent caustic, sulfur, sour water, flare, offgas, acid gas, phenolic/naphthenic waste, or slop streams.
8. Verify utilities that are critical to safe operation: cooling water, steam, fuel gas, hydrogen, instrument air, nitrogen/inert gas, wash water, electricity, and heat tracing.

## HAZOP Prompts By Refinery Context

Use these prompts to orient the review:

- **Alkylation:** acid/catalyst inventory, hydrocarbon/acid separation, reactor cooling, isobutane recycle, acid regeneration, propane/butane/alkylate fractionation, acid leak or aerosol mitigation, and spent-acid/caustic handling.
- **Catalytic cracking/FCC/DCC:** feed preheat, riser/reactor, regenerator, catalyst circulation, high-temperature hydrocarbon, flue gas, wet gas compressor, fractionation, and catalyst fines.
- **Hydrotreating/hydrocracking/hydroprocessing:** hydrogen feed and recycle, high pressure, high temperature, reactor exotherm, H2S/ammonia formation, separator pressure control, sour water, amine treating, and depressuring.
- **Distillation/crude/vacuum:** heat input, column pressure, reflux, pumparounds, overhead condensation, sour water, vacuum system, furnace, and blocked-in thermal expansion.
- **Gas treating/H2S removal:** acid gas, amine/solvent circulation, absorber/regenerator, foaming, rich/lean solvent, reboiler, sulfur plant tie-in, and toxic gas detection.
- **Sulfur recovery/liquid redox:** H2S feed, air/oxygen, sulfur handling, catalyst/redox solution, filtration, pH/redox control, sampling, plugging, and offgas quality.
- **Sweetening/spent caustic:** caustic circulation, mercaptan oxidation, air injection, disulfide formation, spent caustic segregation, phenolic/naphthenic/sulfidic caustic compatibility, and waste treatment.
- **Isomerization/reforming/aromatics:** hydrogen, chloride/acid catalyst if applicable, reactor temperature, recycle gas, stabilizer/fractionation, benzene/aromatics toxicity, and product quality control.

## Safeguards To Verify, Not Assume

For any process entry, verify these in project-specific P&IDs and documents:

- Relief/depressuring devices and protected equipment.
- High-high temperature/pressure trips and reactor shutdown logic.
- Analyzer reliability and sample-system conditioning.
- Acid gas, flammable gas, toxic gas, and fire detection coverage.
- Catalyst/chemical isolation, drains, vents, and spill containment.
- Utility failure response, especially cooling, hydrogen, instrument air, nitrogen, and power loss.
- Startup/shutdown/regeneration modes.
- Manual bypasses and temporary lineups.
- Waste disposal routing and environmental constraints.

## Missing Information To Flag

- Process entry is generic and not tied to the project design basis.
- Feed composition, contaminants, or product quality targets are missing.
- Catalyst/chemical identity or concentration is missing.
- Reactor/separator/column operating pressure and temperature are missing.
- Recycle, regeneration, waste, or relief destination is unclear.
- Licensed package boundary and owner interface points are unclear.
- Utility users and critical utility failure response are missing.
- No P&ID, cause-and-effect chart, operating procedure, relief basis, or datasheet is available to verify the process-context assumption.


# OREDA Offshore Reliability Data Handbook - Book Wiki

## Source Card

- Source slug: `oreda-offshore-reliability-data-handbook`
- Domain: `reliability_data`
- Primary topic wiki: `reliability-data`
- Primary procedural skill: `reliability-data-selection`
- Secondary skills: none
- Tags: `oreda`, `offshore`, `failure-rate`, `equipment-class`, `reliability-data`
- Pages: 835
- Usable text pages in current extraction: 0
- Indexed topic hits: 0
- Top signals: no indexed topic hits
- Source quality: outline/bookmark count: 835; text layer weak; limited working coverage; Text layer is weak; keep as data-source routing with manual table lookup from PDF.
- AI confidence tier: screening-only - Use for routing, gap prompts, and missing-basis checks only until the source wiki is enriched from page-level reading.

## Role In AUTO HAZOP

Use this wiki as screening guidance with explicit missing-basis controls for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-oreda-offshore-reliability-data-handbook/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source to challenge reliability and failure-rate assumptions for applicability and uncertainty.

## Decisions This Source Can Support

- Whether the equipment class, service, duty cycle, environment, failure mode, and data source match.
- Whether data are being used for screening, LOPA/SIL verification, QRA, maintenance, or mechanical integrity.
- Whether uncertainty, confidence, common cause, and inspection/proof-test assumptions are visible.

## Source-Derived Playbook

- Name the equipment boundary and failure mode before applying any rate or probability.
- Treat handbook values as inputs needing applicability review, not universal plant facts.
- Route safety-instrumented data to SIS/SIL verification when it affects PFD/PFH or SIL target acceptance.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| none | 0 | none | Use only domain checklist and mark detailed claims as missing basis. |

## HAZOP Injection Pattern

When this wiki is selected for a HAZOP row:

1. State the matched source signal and confidence tier.
2. Restate the node/deviation/design-intent context from project data.
3. Improve the cause so it names the failed item, failure mode, human/organizational condition, external event, or initiating event.
4. Improve the consequence as an unmitigated event path before safeguards.
5. Test safeguards for independence, timing, auditability, and effectiveness before giving credit.
6. Recommend action only for a real gap: missing design basis, calculation, weak safeguard, missing procedure, missing inspection/test, missing MOC, missing training, or missing documentation.
7. Mark blocked decisions explicitly when project-specific criteria or data are absent.

## Missing-Basis Checklist

- [ ] Equipment taxonomy and failure mode
- [ ] Operating/service context
- [ ] Approved reliability data source
- [ ] Proof-test/inspection interval
- [ ] Uncertainty and common-cause basis
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `oreda-offshore-reliability-data-handbook`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `oreda-offshore-reliability-data-handbook oreda offshore failure-rate equipment-class reliability-data HAZOP cause consequence safeguard recommendation`
- `oreda-offshore-reliability-data-handbook reliability_data missing basis project criteria data assumptions`
- `oreda-offshore-reliability-data-handbook AutoHAZOP node deviation scenario review quality gate`
- `oreda-offshore-reliability-data-handbook evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `reliability-data-selection` and secondary skills none when the decision requires a specialist workflow.

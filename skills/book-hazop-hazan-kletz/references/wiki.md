# Hazop and Hazan - Kletz - Book Wiki

## Source Card

- Source slug: `hazop-hazan-kletz`
- Domain: `hazop`
- Primary topic wiki: `hazop-pha-security-review`
- Primary procedural skill: `hazop-hazan-study-leader`
- Secondary skills: none
- Tags: `hazop`, `hazan`, `hazard-assessment`, `risk-ranking`, `kletz`
- Pages: 220
- Usable text pages in current extraction: 0
- Indexed topic hits: 0
- Top signals: no indexed topic hits
- Source quality: text layer weak; limited working coverage; Text layer is very weak; profile is title/metadata driven and requires wiki enrichment before detailed use for detailed passages.
- AI confidence tier: screening-only - Use for routing, gap prompts, and missing-basis checks only until the source wiki is enriched from page-level reading.

## Role In AUTO HAZOP

Use this wiki as screening guidance with explicit missing-basis controls for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-hazop-hazan-kletz/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source to improve HAZOP study discipline and worksheet quality.

## Decisions This Source Can Support

- Whether the node boundary and design intent are specific enough for the selected deviation.
- Whether each row has one initiating cause, one unmitigated consequence path, and correctly separated safeguards.
- Whether a recommendation closes a real gap instead of restating normal design intent.

## Source-Derived Playbook

- Start from node intent, process parameter, guide word, normal envelope, and credible abnormal state.
- Rewrite vague causes so they name the failed equipment, failure mode, human/organizational condition, or external event.
- Write consequences as unmitigated event paths before safeguards, then test safeguards for effectiveness and independence.

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

- [ ] Node boundary and design intent
- [ ] Normal operating envelope
- [ ] P&ID/process graph context
- [ ] Safeguard design basis
- [ ] Relief/alarm/interlock/procedure evidence
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `hazop-hazan-kletz`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `hazop-hazan-kletz hazop hazan hazard-assessment risk-ranking kletz HAZOP cause consequence safeguard recommendation`
- `hazop-hazan-kletz hazop missing basis project criteria data assumptions`
- `hazop-hazan-kletz AutoHAZOP node deviation scenario review quality gate`
- `hazop-hazan-kletz evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `hazop-hazan-study-leader` and secondary skills none when the decision requires a specialist workflow.

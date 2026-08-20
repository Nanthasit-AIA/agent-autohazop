# Risk Assessment for Thermal Processes in Food Manufacture - Book Wiki

## Source Card

- Source slug: `thermal-process-risk-food-manufacture`
- Domain: `specialized_risk`
- Primary topic wiki: `risk-criteria-qra`
- Primary procedural skill: `risk-criteria-qra`
- Secondary skills: none
- Tags: `food-safety`, `thermal-process`, `risk-assessment`, `microbiology`, `specialized`
- Pages: 44
- Usable text pages in current extraction: 44
- Indexed topic hits: 3
- Top signals: HAZOP/PHA:2, QRA/risk criteria:1
- Source quality: text layer usable
- AI confidence tier: usable - Use for source-derived review guidance, with project data controlling all final engineering decisions.

## Role In AUTO HAZOP

Use this wiki as source-backed working guidance for AutoHAZOP generation, worksheet review, assistant answers, and recommendation challenge. It is strongest when the current node, deviation, safeguard, or question matches the tags and evidence signals above. It must not override project data, approved company criteria, vendor information, plant procedures, or competent engineering review.

For substantive row work, read `book-skills/book-thermal-process-risk-food-manufacture/references/field-manual.md`; it contains the sharper questions, anti-patterns, row moves, and high-signal page anchors for this source.

## Decision Lens

Use the source to discipline quantitative risk assumptions and risk-criteria decisions.

## Decisions This Source Can Support

- Whether frequency, consequence, vulnerability, occupancy, and ignition/exposure assumptions are explicit.
- Whether the selected risk metric and tolerability criterion are project-approved.
- Whether uncertainty and sensitivity are visible enough for decision making.

## Source-Derived Playbook

- Separate qualitative screening from quantitative claims and identify the missing numeric basis.
- Challenge event-tree/fault-tree branches for dependence, enabling conditions, and double counting.
- State whether the output is a screening recommendation, a calculation input request, or a blocked decision.

## Evidence Map

| Signal | Hits | Page evidence | Use |
|---|---:|---|---|
| HAZOP/PHA | 2 | 29 | Improve node intent, guide-word deviation quality, cause/consequence wording, safeguards, and recommendation discipline. |
| QRA/risk criteria | 1 | 12 | Challenge frequency, consequence, risk criteria, event-tree/fault-tree assumptions, and uncertainty treatment. |

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

- [ ] Project risk criteria
- [ ] Frequency data source
- [ ] Consequence model/endpoints
- [ ] Occupancy, ignition, vulnerability, and exposure basis
- [ ] Sensitivity/uncertainty treatment
- [ ] Separate source-derived guidance from project facts and assumptions.
- [ ] Do not invent site risk criteria, failure rates, SIL targets, PFD/PFH, proof-test intervals, occupancy data, consequence endpoints, or relief capacity.
- [ ] Use the P&ID/process graph and supplied project basis as controlling context when they conflict with generic book guidance.
- [ ] Treat the book artifact as decision support, not as a substitute for competent engineering review.
- [ ] If the required value, table, equation, criterion, or example is not encoded here or supplied by the project, mark it as missing basis.

## Output Contract

When this wiki materially supports an answer, include:

- Decision: the engineering status or next action.
- Basis: `thermal-process-risk-food-manufacture`, matched evidence signal, and confidence tier.
- HAZOP impact: cause, consequence, safeguard, IPL, likelihood, severity, recommendation, or documentation effect.
- Missing basis: data, calculation, standard, procedure, inspection/test, proof-test, risk criteria, or site decision still needed.
- Confidence: usable, controlled-use, screening-only, or blocked pending source/project verification.

## High-Value Retrieval Queries

- `thermal-process-risk-food-manufacture food-safety thermal-process risk-assessment microbiology specialized HAZOP cause consequence safeguard recommendation`
- `thermal-process-risk-food-manufacture HAZOP/PHA QRA/risk criteria missing basis project criteria data assumptions`
- `thermal-process-risk-food-manufacture AutoHAZOP node deviation scenario review quality gate`
- `thermal-process-risk-food-manufacture evidence map page ranges confidence limitations`

## Boundaries

- Keep guidance derived and concise; do not reproduce source chapters or long passages.
- Do not invent numerical values, tables, criteria, equations, examples, or plant-specific facts.
- Use page evidence as a pointer for targeted enrichment, not as final proof for calculations.
- Escalate to the primary shared skill `risk-criteria-qra` and secondary skills none when the decision requires a specialist workflow.

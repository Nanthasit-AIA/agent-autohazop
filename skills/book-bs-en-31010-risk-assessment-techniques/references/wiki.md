# BS EN 31010 Risk Management - Risk Assessment Techniques - Book Wiki

## Source Card

- Source slug: `bs-en-31010-risk-assessment-techniques`
- Domain: `risk-assessment-methods`
- Tags: `bs-en-31010`, `risk-assessment`, `hazop`, `lopa`, `fta`, `eta`, `uncertainty`
- Primary procedural skill: `risk-criteria-qra`
- Topic wiki: `risk-assessment-techniques`
- Detailed standard reference: `autohazop-agent-pack/references/standards/bs-en-31010-risk-assessment-techniques.md`
- Working quality: controlled-use qualitative guidance; verify numeric, tabular, and clause-level decisions from project/source basis.
- Source quality: pages: 94; outline/bookmark count: 115
- Source file: `G:\.shortcut-targets-by-id\1B9dVATZu7Jx-iYIRt0KSwjnMzhv4w10U\2026_Thananchanai_Nin\SCGC\Lrarning Data\3.Standards, Codes & Methodology\HAZOP Methodology Standards\BN SE\BS EN 310102010 Risk Management - Risk Assessment Techniques (The Britsh Standards Institution) (z-library.sk, 1lib.sk, z-lib.sk) (1).pdf`

## Alternate Source PDFs

- none

## What This Source Contributes

Support method selection and uncertainty review when a HAZOP row needs escalation to LOPA, FTA, ETA, QRA, bow-tie, or a different risk assessment technique.

## Decision Lens

Use risk assessment technique selection to decide whether HAZOP, What-if, FMEA, LOPA, FTA, ETA, bow-tie, QRA, or risk matrix is appropriate.

## Source-Derived Checks

- Classify the decision: hazard identification, scenario screening, likelihood estimation, barrier analysis, consequence modeling, uncertainty, or risk acceptance.
- Select the technique that fits available data, uncertainty, complexity, and decision stakes.
- Do not use risk matrix outputs as quantitative proof where FTA/ETA/QRA is needed.

## HAZOP Injection Pattern

1. Identify whether the current node/deviation touches this source's domain.
2. Improve cause wording so it names the failed item, failure mode, human task, operating phase, or design-envelope exceedance.
3. Improve consequence wording so it describes the unmitigated event path before safeguards.
4. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
5. Convert missing source/project data into a precise recommendation.
6. Do not reduce risk or claim IPL credit unless the specific project basis is supplied.

## Sharp Questions

- [ ] Classify the decision: hazard identification, scenario screening, likelihood estimation, barrier analysis, consequence modeling, uncertainty, or risk acceptance.
- [ ] Select the technique that fits available data, uncertainty, complexity, and decision stakes.
- [ ] Do not use risk matrix outputs as quantitative proof where FTA/ETA/QRA is needed.
- [ ] Risk matrix
- [ ] Tolerability criteria
- [ ] Frequency data
- [ ] Consequence model
- [ ] Dependency/common-cause basis
- [ ] Uncertainty/sensitivity basis

## Anti-Patterns To Kill

- Using HAZOP alone to justify final tolerability for high-consequence complex scenarios.
- Using LOPA multiplication when dependencies/common cause are unresolved.

## Row Moves

- Route scenario to HAZOP, LOPA, FTA, ETA, bow-tie, QRA, or FMEA based on decision need.
- Add uncertainty/missing-basis recommendation when method choice is blocked.

## Recommendation Logic

- Escalate to LOPA/FTA/ETA/QRA when qualitative HAZOP cannot support the decision.
- Document uncertainty and method limits in the recommendation.

## Missing-Basis Checklist

- [ ] Risk matrix
- [ ] Tolerability criteria
- [ ] Frequency data
- [ ] Consequence model
- [ ] Dependency/common-cause basis
- [ ] Uncertainty/sensitivity basis
- [ ] Use the P&ID/process graph and supplied project data as controlling evidence.
- [ ] Keep normal operation, design limits, safe operating limits, and protection layers separate.
- [ ] Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- [ ] Do not treat a standard/book statement as proof that a safeguard exists in the project.
- [ ] Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- [ ] Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Source Navigation Preview

ieciso31010{ed1.0}b.pdf | English | CONTENTS | FOREWORD | INTRODUCTION | 1 Scope | 2 Normative references | 3 Terms and definitions | 4 Risk assessment concepts | 4.1 Purpose and benefits | 4.2 Risk assessment and the risk management framework | 4.3 Risk assessment and the risk management process | 5 Risk assessment process | 5.1 Overview | 5.2 Risk identification | 5.3 Risk analysis | 5.4 Risk evaluation | 5.5 Documentation | 5.6 Monitoring and reviewing risk assessment | 5.7 Application of risk assessment during life cycle phases | 6 Selection of risk assessment techniques | 6.1 General | 6.2 Selection of techniques | 6.3 Application of risk assessment during life cycle phases | 6.4 Types of risk assessment techniques | Annex A (informative) Comparison of risk assessment techniques | Annex B (informative) Risk assessment techniques | Bibliography | Figures | Figure 1 – Contribution of risk assessment to the risk management process | Figure B.1 – Dose-response curve | Figure B.2 – Example of an FTA from IEC 60300-3-9 | Figure B.3 – Example of an event tree | Figure B.4 – Example of cause-consequence analysis | Figure B.5 – Example of Ishikawa or Fishbone diagram | Figure B.6 – Example of tree formulation of cause-and-effect analysis | Figure B.7 – Example of human reliability assessment | Figure B.8 – Example bow tie diagram for unwanted consequences | Figure B.9 – Example of system Markov diagram | Figure B.10 – Example of state transition diagram | Figure B.11 – Sample Bayes’ net | Figure B.12 – The ALARP concept | Figure B.13 – Part example of a consequence criteria table | Figure B.14 – Part example of a risk ranking matrix | Figure B.15 – Part example of a probability criteria matrix | Tables | Table A.1 – Applicability of tools used for risk assessment | Table A.2 – Attributes of a selection of risk assessment tools | Table B.1 – Example of possible HAZOP guidewords | Table B.2 – Markov matrix | Table B.3 – Final Markov matrix | Table B.4 – Example of Monte Carlo simulation | Table B.5 – Bayes’ table data | Table B.6 – Prior probabilities for nodes A and B | Table B.7 – Conditional probabilities for node C with node A and node B defined | Table B.8 – Conditional probabilities for node D with node A and node C defined | Table B.9 – Posterior probability for nodes A and B with node D and node C defined | Table B.10 – Posterior probability for node A with node D and node C defined | Français | SOMMAIRE

## Retrieval Queries

- `bs-en-31010-risk-assessment-techniques bs-en-31010 risk-assessment hazop lopa fta eta uncertainty HAZOP cause consequence safeguard recommendation`
- `bs-en-31010-risk-assessment-techniques risk-assessment-methods missing basis project data assumptions`
- `bs-en-31010-risk-assessment-techniques AutoHAZOP graph node deviation quality gate`
- `bs-en-31010-risk-assessment-techniques safeguard IPL independence auditability effectiveness`

## Working Boundaries

- This wiki is a derived working artifact, not a reproduction of the source.
- Use it to improve AutoHAZOP generation, review, and missing-basis detection.
- Do not quote long source passages or invent standard requirements not encoded here.
- Use exact PDF/source/project review for clause-level compliance, sizing, calculations, and acceptance criteria.

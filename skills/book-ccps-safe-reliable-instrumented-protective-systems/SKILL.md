---
name: book-ccps-safe-reliable-instrumented-protective-systems
description: Use source-specific working knowledge from CCPS Guidelines for Safe and Reliable Instrumented Protective Systems for AutoHAZOP, HAZOP/PHA, LOPA, SIS, IPS, interlock, alarm/operator-response, BPCS independence, IPL credit, SRS/STR evidence, bypass/defeat management, proof testing, validation, operations, maintenance, and lifecycle review. Use when a row or user question involves instrumented protective functions, safety instrumented functions, trips, shutdowns, alarms with response, permissives, interlocks, final elements, logic solvers, common-cause failure, independence, reliability, auditability, maintainability, or management of change. Read references/wiki.md, references/field-manual.md, and references/evidence-map.md before substantive use.
---

# CCPS Safe And Reliable Instrumented Protective Systems Book Skill

Use this skill as a controlled AutoHAZOP working method for instrumented protective systems (IPS), including safety instrumented systems (SIS), interlocks, alarms with operator response, permissives, shutdowns, and instrumented prevention/mitigation functions.

This skill is intentionally fail-closed: if SRS, cause-and-effect, trip setpoint, response time, final element action, proof-test interval, bypass status, independence basis, common-cause assessment, PFD/STR basis, or lifecycle evidence is not supplied, mark it as missing basis instead of granting IPL credit.

## Load Order

1. Read `references/wiki.md` for the IPS lifecycle and HAZOP/LOPA decision playbook.
2. Read `references/field-manual.md` for sharp row-review questions, anti-patterns, and hard decision gates.
3. Read `references/evidence-map.md` for source identity, merged-PDF status, coverage, and known source caveats.
4. If the row requires SIL/PFD verification, also use `sis-sil-verification-reliability`.
5. If the row requires LOPA scenario normalization, also use `lopa-iel-conditional-modifier` and `book-ccps-initiating-events-ipls-lopa`.
6. If the row requires IEC 61511 lifecycle evidence, also use `book-iec-61511-1-process-industry-sis`.

## Source Role

- Source slug: `ccps-safe-reliable-instrumented-protective-systems`
- Domain: `instrumented-protective-systems`
- Primary procedural skill: `sis-sil-verification-reliability`
- Secondary procedural skills: `lopa-iel-conditional-modifier`, `alarm-management-rationalization`, `process-safety-management-rbps-moc-docs`
- Confidence tier: controlled-use qualitative/lifecycle guidance; project data controls all final engineering decisions.
- Core decision lens: Treat IPS as a lifecycle-controlled protective function, not as a generic safeguard label.

## Required Workflow

1. Identify the claimed protective function: detection, logic, final action, process effect, timing, and reset/bypass behavior.
2. Classify it before credit: control function, alarm/operator response, permissive, interlock, SIS/SIF, mechanical mitigation, response action, or non-creditable process indication.
3. Separate initiating event, consequence, enabling conditions, and protection layers. Do not make failure of the IPS the initiating event unless the hazard is specifically loss/spurious operation of that IPS function.
4. Check independence from the initiating cause, BPCS, utilities, sensors, final elements, human task, and other credited layers.
5. Check lifecycle evidence: risk assessment/allocation, process requirements, SRS/STR, design basis, FAT/SAT/validation, proof-test/inspection, bypass management, OMI procedures, MOC, and performance monitoring.
6. Grant IPL/SIF credit only when independence, effectiveness, response time, reliability/PFD or STR basis, auditability, and maintainability evidence are all present.
7. If evidence is missing, keep the safeguard as non-creditable or candidate IPL and write a missing-basis recommendation.

## Guardrails

- Do not credit an interlock, trip, shutdown, alarm, or operator response from its tag name alone.
- Do not reduce likelihood using an IPS that shares the failed sensor, logic solver, final element, utility, human task, or maintenance practice with the initiating event.
- Do not write consequences that already assume "if the trip/interlock/SIS fails" after a separate initiating event; that is a second-layer failure and belongs in LOPA sensitivity or recommendation basis.
- Do not invent SIL, PFDavg, spurious trip rate, proof-test interval, diagnostic coverage, beta factor, response time, or final element closure time.
- Treat bypassed, defeated, inhibited, out-of-service, untested, undocumented, or manually reset functions as missing-basis until project evidence proves availability and management controls.
- Separate safe failure, dangerous detected failure, dangerous undetected failure, systematic failure, common-cause failure, and spurious operation.

## Output Pattern

When this skill materially supports an answer, structure the result as:

- Decision: IPS classification and whether it is creditable, candidate, non-creditable, or blocked.
- Basis: matched lifecycle stage, protective-function attributes, and source role.
- HAZOP impact: corrected cause, consequence, safeguard/IPL classification, likelihood, severity, recommendation, or documentation gap.
- Missing basis: exact project evidence required before credit or acceptance.
- Confidence: `usable`, `controlled-use`, `screening-only`, or `blocked`.

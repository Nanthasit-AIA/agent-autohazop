# Field Manual - CCPS Safe And Reliable Instrumented Protective Systems

## Fast Triage

Use this manual when a HAZOP row contains any of these words: `interlock`, `trip`, `shutdown`, `SIS`, `SIF`, `IPS`, `permissive`, `alarm`, `operator response`, `ESD`, `logic solver`, `final element`, `bypass`, `defeat`, `inhibit`, `proof test`, `validation`, `spurious trip`, or `common cause`.

## Five-Minute Row Review

1. Name the process initiating event without relying on protection-layer failure.
2. Write the unmitigated consequence before safeguards act.
3. Expand the instrumented function into sensor, logic, final element, action, timing, reset, bypass, and proof-test basis.
4. Classify the function: BPCS, alarm/operator response, permissive, interlock, SIS/SIF, mitigation, barrier, or response.
5. Decide the credit status: non-creditable safeguard, candidate IPL, credited IPL, or blocked pending missing basis.

## Hard Gates

- No SRS/STR or equivalent requirement basis: do not grant SIS/SIF credit.
- No setpoint/action/response-time/final-element definition: do not grant function credit.
- Shared sensor, logic, final element, utility, software, maintenance, bypass, or human task with the initiating event: do not claim independence.
- Alarm without rationalized priority, cue, diagnosis, procedure, response time, training, and audit basis: do not grant IPL credit.
- Bypassed, defeated, inhibited, out-of-service, or untested function: treat as unavailable unless compensating measures are documented.
- Missing proof-test interval, coverage, architecture, diagnostics, or PFD/STR basis: block quantitative risk reduction.

## Sharp Questions

- What abnormal condition is detected?
- Which tag detects it, and is that tag independent from BPCS control?
- Which logic solver acts, and is its software/configuration lifecycle controlled?
- Which final element changes state, what is the fail position, and how fast must it act?
- Does the function prevent the event, mitigate the consequence, supervise operator response, or only support diagnosis?
- Is the function available during startup, shutdown, maintenance, bypass, manual mode, and abnormal operations?
- What proof test demonstrates the entire loop, including sensor, logic, final element, and response time?
- What records show FAT/SAT/validation and post-MOC revalidation?
- What common-cause or systematic failure can defeat multiple claimed layers?
- What demand/failure/spurious-trip history changes confidence in the function?

## IPL Credit Decision

| Status | Use when |
|---|---|
| Credited IPL | Independent, effective, timely, auditable, maintained, validated, available, and supported by PFD/STR basis. |
| Candidate IPL | Function exists but one or more credit-basis documents are missing. |
| Non-IPL safeguard | Helpful control/indication/procedure exists but does not meet independence, reliability, auditability, or timing tests. |
| Blocked | Function, action, lifecycle status, or project risk criteria are too unclear to classify. |

## Common Corrections

- Change `High pressure due to high pressure trip failure` to `Blocked outlet / control valve failure / external fire / thermal expansion causes high pressure; high-pressure trip is candidate protection`.
- Change `Operator closes manual valve` to `Alarm plus operator response; require cue, time available, access, procedure, training, and human reliability basis`.
- Change `SIS protects vessel` to `SIF: sensor detects high pressure, logic solver trips feed pump and closes XV, final action must occur within required response time; credit pending SRS/SIL/proof-test/validation`.
- Change `Interlock is IPL` to `candidate IPL pending independence from initiating cause, final element availability, bypass management, and proof-test basis`.

## Recommendation Templates

- Verify and document SRS/STR for `<function>` including cause, consequence, setpoint, action, response time, final element, reset, bypass, and required risk reduction.
- Confirm `<function>` independence from BPCS, initiating cause, utilities, final elements, software, and maintenance practices before IPL credit.
- Add proof-test/validation basis for the full loop `<sensor> -> <logic> -> <final element>` and record test interval, coverage, and acceptance criteria.
- Review bypass/defeat/inhibit management and compensating measures for `<function>` before accepting availability in LOPA.
- Reclassify `<alarm/operator action>` as non-IPL until alarm rationalization, operator response time, procedure, training, and human reliability basis are documented.

## Failure Modes To Keep Separate

- Safe failure versus dangerous failure
- Detected versus undetected dangerous failure
- Random hardware failure versus systematic design/configuration/procedure failure
- Common-cause failure versus independent failure
- Spurious operation versus failure to act on demand
- Demand frequency versus probability of failure on demand

## Stop Conditions

Return `blocked` or `missing basis` when the row lacks project risk criteria, initiating event frequency, unmitigated consequence, SRS/STR, setpoint/action basis, response time, proof-test/PFD basis, validation, bypass status, or independence evidence.

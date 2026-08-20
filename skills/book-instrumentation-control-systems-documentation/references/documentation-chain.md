# Documentation Chain

Use this reference to decide which instrument/control document should support a HAZOP or LOPA claim. The guidance is derived as a copyright-safe working summary from a user-supplied copy of *Instrumentation and Control Systems Documentation* by Frederick A. Meier and Clifford A. Meier.

## Source Role

This source is useful for documentation completeness and traceability. It is not a design code, risk matrix, SIL standard, or proof that a control or safeguard exists in the project.

## Typical Development Sequence

1. `PFD`: establishes the process concept, major equipment, major streams, material quantities, and important operating conditions such as pressure, temperature, and flow.
2. `P&ID`: adds instrument symbols, tag numbers, control loops, local instruments, equipment/line context, and process connections needed by design disciplines.
3. `Instrument index or database`: tracks tag-numbered devices, functions, status, configuration, ranges, and cross-document links.
4. `Specification forms or instrument data sheets`: define each tag-numbered device well enough for procurement, configuration, installation, and maintenance.
5. `Binary logic / control descriptions`: document on-off control, permissives, interlocks, shutdowns, and functional behavior that is too detailed for a P&ID note alone.
6. `Location plans`: show where instruments and associated hardware are installed for construction, operations, and maintenance.
7. `Installation details`: define mounting, process connection, tubing, supports, materials, and construction details.
8. `Loop diagrams`: consolidate loop interconnections, process connections, signals, power, utilities, terminals, junction boxes, panels, and checkout information once enough design detail is available.
9. `Drawing title blocks, revisions, notes, and references`: keep ownership, document identity, revision history, and cross-document basis traceable.

## HAZOP Use

- Use the PFD and P&ID for node context, process intent, normal flow direction, and instrument presence.
- Use the instrument index/database to confirm tag identity, service, range, status, and document links.
- Use specification forms to support device service, range, materials, signal type, fail action, and procurement basis when available.
- Use process control descriptions, interlock notes, logic diagrams, or cause-and-effect documents to support on-off logic and trip action.
- Use loop diagrams to confirm wiring, signal path, power, instrument air, termination, final element, and checkout evidence.
- Use revision records to avoid relying on stale control logic, tag data, or loop wiring.

## Anti-Patterns

- Claiming a safeguard from a P&ID symbol without checking tag function, loop action, and document status.
- Treating an instrument index row as proof that logic exists or is tested.
- Treating a loop diagram as proof of SIL, IPL independence, or response time.
- Using an old drawing revision when the P&ID, logic diagram, or loop diagram disagree.
- Writing `instrument failure` as a HAZOP cause without the tag, measured variable, failure mode, and effect on the final element or process.

## Missing-Basis Recommendations

Use targeted recommendations such as:

- `Verify tag service, range, and loop membership in the instrument index/database.`
- `Provide current loop diagram showing sensor, controller/logic, final element, power, signal path, and termination details.`
- `Provide process control description, interlock note, logic diagram, or cause-and-effect for claimed trip action.`
- `Resolve revision conflict between P&ID, loop diagram, instrument index, and logic document before crediting safeguard.`

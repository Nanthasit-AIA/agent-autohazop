# Piping and Instrumentation Diagram Development - Book Wiki

## Source Card

- Source slug: `moe-toghraei-pid-development`
- Domain: `pid-development`
- Tags: `p&id`, `pid-development`, `line-tag`, `equipment`, `valve`, `instrument`, `review`
- Primary procedural skill: `hazop-hazan-study-leader`
- Topic wiki: `pid-development-tracing`
- Detailed standard reference: `autohazop-agent-pack/references/standards/moe-toghraei-pid-development.md`
- Working quality: controlled-use qualitative guidance; verify numeric, tabular, and clause-level decisions from project/source basis.
- Source quality: pages: 472
- Source file: `G:\.shortcut-targets-by-id\1B9dVATZu7Jx-iYIRt0KSwjnMzhv4w10U\2026_Thananchanai_Nin\SCGC\Lrarning Data\Piping and Instrumentation Diagram Development (Moe Toghraei) (z-library.sk, 1lib.sk, z-lib.sk).pdf`

## Alternate Source PDFs

- none

## What This Source Contributes

Improve AutoHAZOP graph extraction and node definition by requiring P&ID topology, line service, equipment boundary, instrument role, and valve placement evidence.

## Decision Lens

Use P&ID development practice to validate graph topology, equipment-line-valve-instrument extraction, line tags, utilities, drains, vents, relief, and control loops.

## Source-Derived Checks

- Build node boundary from equipment, lines, valves, instruments, utilities, drains, vents, relief paths, and off-page connectors.
- Check line tags, flow direction, service, normal position, control loop action, and package boundary before HAZOP rows.
- Reject graph-derived causes when the failed item is not on or connected to the selected node.

## HAZOP Injection Pattern

1. Identify whether the current node/deviation touches this source's domain.
2. Improve cause wording so it names the failed item, failure mode, human task, operating phase, or design-envelope exceedance.
3. Improve consequence wording so it describes the unmitigated event path before safeguards.
4. Challenge safeguards for independence, timing, effectiveness, auditability, and project evidence.
5. Convert missing source/project data into a precise recommendation.
6. Do not reduce risk or claim IPL credit unless the specific project basis is supplied.

## Sharp Questions

- [ ] Build node boundary from equipment, lines, valves, instruments, utilities, drains, vents, relief paths, and off-page connectors.
- [ ] Check line tags, flow direction, service, normal position, control loop action, and package boundary before HAZOP rows.
- [ ] Reject graph-derived causes when the failed item is not on or connected to the selected node.
- [ ] P&ID revision
- [ ] Line list
- [ ] Equipment list
- [ ] Instrument index
- [ ] Valve list/normal position
- [ ] Off-page connector mapping

## Anti-Patterns To Kill

- Using valve/instrument IDs as equipment nodes.
- Generating cross-node consequences without upstream/downstream path evidence.
- Ignoring off-page connectors, vents, drains, bypasses, or common headers.

## Row Moves

- Convert graph uncertainty into a P&ID extraction correction before HAZOP generation.
- Use line/equipment boundary evidence to reject irrelevant causes.

## Recommendation Logic

- Verify graph extraction against P&ID legend and line/equipment lists.
- Add missing valve/instrument normal position before relying on safeguard or cause logic.

## Missing-Basis Checklist

- [ ] P&ID revision
- [ ] Line list
- [ ] Equipment list
- [ ] Instrument index
- [ ] Valve list/normal position
- [ ] Off-page connector mapping
- [ ] Use the P&ID/process graph and supplied project data as controlling evidence.
- [ ] Keep normal operation, design limits, safe operating limits, and protection layers separate.
- [ ] Do not invent design pressure, design temperature, material class, relief capacity, SIL/PFD, failure rate, proof-test interval, or risk criteria.
- [ ] Do not treat a standard/book statement as proof that a safeguard exists in the project.
- [ ] Mark detailed numeric, tabular, or code-compliance decisions as missing basis unless the exact project value and source clause/table are supplied.
- [ ] Write recommendations that are specific, owned, testable, and tied to the row's remaining risk gap or missing basis.

## Source Navigation Preview

No usable outline/bookmark preview extracted; use this wiki as a derived working guide and verify detailed clauses/tables from the PDF or project basis.

## Retrieval Queries

- `moe-toghraei-pid-development p&id pid-development line-tag equipment valve instrument review HAZOP cause consequence safeguard recommendation`
- `moe-toghraei-pid-development pid-development missing basis project data assumptions`
- `moe-toghraei-pid-development AutoHAZOP graph node deviation quality gate`
- `moe-toghraei-pid-development safeguard IPL independence auditability effectiveness`

## Working Boundaries

- This wiki is a derived working artifact, not a reproduction of the source.
- Use it to improve AutoHAZOP generation, review, and missing-basis detection.
- Do not quote long source passages or invent standard requirements not encoded here.
- Use exact PDF/source/project review for clause-level compliance, sizing, calculations, and acceptance criteria.

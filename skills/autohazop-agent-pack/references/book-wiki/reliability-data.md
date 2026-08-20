# Reliability Data Wiki

## Purpose

Support selection and challenge of failure-rate/PFD data for equipment, control systems, SIS, LOPA, QRA, and mechanical integrity assumptions.

## Retrieval Tags

`reliability-data`, `failure-rate`, `pfd`, `pds`, `oreda`, `equipment-class`

## Source Books

| Source | Slug | Pages | Artifact | Tags |
|---|---:|---:|---|---|
| CCPS Process Equipment Reliability Data | `ccps-process-equipment-reliability-data` | 312 | wiki_and_skill | `failure-rate`, `reliability-data`, `equipment`, `data-quality`, `mechanical-integrity` |
| OREDA Offshore Reliability Data Handbook | `oreda-offshore-reliability-data-handbook` | 835 | wiki_and_skill | `oreda`, `offshore`, `failure-rate`, `equipment-class`, `reliability-data` |
| PDS Data Handbook for SIS | `pds-data-handbook-sis` | 112 | wiki_and_multiple_skills | `pds`, `sis`, `failure-rate`, `reliability-data`, `proof-test`, `pfd` |

## Data selection

Match equipment class, service, duty, environment, failure mode, boundary definition, repair policy, and data population before importing a value.

## Uncertainty

Keep confidence ranges, source quality, age, operating context, and expert judgment visible. Do not overstate precision from handbook values.

## Safety use

Trace values to initiating event frequency, equipment failure probability, IPL PFD, SIF verification, or QRA frequency model; avoid double counting proof testing or safeguards.

## Answer Pattern

When using this wiki, answer with:

- `Decision`: the best current engineering decision or review status.
- `Basis`: source slug(s), page count/source note, and assumptions.
- `Missing data`: project criteria, tags, drawings, calculations, inspection/proof-test evidence, or data tables needed.
- `Cautions`: dependency, uncertainty, applicability, or OCR/manual-lookup limitations.
- `Next action`: specific review, calculation, field check, or documentation update.

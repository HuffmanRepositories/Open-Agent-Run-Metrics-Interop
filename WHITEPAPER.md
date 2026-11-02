# Open Agent Run Metrics Interop: Accounting Without False Precision

**Author:** Robert Huffman  
**Status:** Research whitepaper, version 0.1

## Abstract

OARMI explores how agent systems can represent run usage and accounting in ways that remain understandable across providers and frameworks. It focuses on test vectors, accounting invariants, and loss-aware interchange—not on billing or budget enforcement.

## Problem statement

An agent run may involve multiple model calls, tool invocations, delegated work, streaming updates, partial reports, cached usage, estimated costs, and provider-reported amounts. Systems can double-count, omit, or conflate these values. A number without units, source, time, and measurement status can create false precision.

## Approach

OARMI records synthetic examples and makes assumptions explicit. It distinguishes estimated, observed, provider-reported, and derived values; identifies units and accounting scope; tracks partial and incremental updates; and documents unknown pricing or incomplete usage. Delegated work must be accounted for without accidental duplication.

## How to use OARMI

Read [START-HERE.md](START-HERE.md), [docs/source-baselines.md](docs/source-baselines.md), and [docs/accounting-invariants.md](docs/accounting-invariants.md). Add a synthetic case using the documented fixture format. Run python3 scripts/validate_fixtures.py and python3 -m unittest discover -s tests -v.

## Boundaries

OARMI is not a billing engine, pricing catalog, invoice validator, budget manager, agent protocol, or financial compliance system. A passing validator checks selected fixture structure; it does not prove that provider usage or invoices are correct.

## Outlook

Prioritize explicit units, provenance, partial-state semantics, delegation accounting, and versioned source comparisons. Do not collapse uncertainty into a single apparently authoritative total.

— Robert Huffman
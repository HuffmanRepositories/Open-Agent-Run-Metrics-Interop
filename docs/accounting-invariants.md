# Accounting invariants and open questions

These are review prompts and conservative design assumptions—not a universal accounting specification.

## Draft invariants

1. **Identity:** Every invocation/event intended to be deduplicated should have a stable identifier within its declared scope.
2. **Scope:** A run, child run, model invocation, and tool invocation are distinct scopes unless a source explicitly defines otherwise.
3. **No accidental double count:** Parent aggregates and child details must not be summed together unless the aggregation rule says to do so.
4. **Snapshots versus deltas:** Reports must declare whether counters are cumulative snapshots or incremental deltas.
5. **Finality:** A final report should be distinguishable from an interim snapshot.
6. **Unknown is not zero:** Missing, unknown, unsupported, and zero are distinct states.
7. **Estimates versus observed values:** Estimated usage/cost must be labeled and must not silently replace reported usage.
8. **Cost provenance:** Currency, price source/version, calculation basis, and estimation status should be explicit when cost is present.
9. **Failure does not imply no usage:** Failed or cancelled calls may still have metered usage.
10. **Non-model actions:** Tool calls may exist without model token usage.
11. **Cache accounting:** Cache reads/writes and ordinary input/output tokens may have distinct semantics; do not assume they are additive without source support.
12. **Nonnegative counters:** Negative token/call counts are invalid unless a source explicitly defines signed corrections or adjustments.

## Open questions

- What is the correct treatment of retries and provider-side deduplication?
- How should partial streaming usage be reconciled with final totals?
- Should cost totals be represented as integer minor units, decimal strings, or source-native values?
- How are refunds, corrections, and late-arriving usage represented?
- How should delegated/child runs expose attribution without double counting?
- Which fields can safely be mapped across SDKs without semantic loss?

## Non-goal

This document does not establish financial accounting rules, legal compliance, or authoritative billing semantics.

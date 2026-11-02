# Open Agent Run Metrics Interop (OARMI)

[Start here](START-HERE.md) · [Whitepaper](WHITEPAPER.md) · [AI agent guidance](AGENTS.md)


**Status:** Early research / draft fixtures. Not a standard, certification, billing system, or production accounting implementation.

OARMI is a neutral, open-source project for documenting interoperability questions and maintaining test vectors around agent-run usage and accounting. It aims to help implementers compare how systems represent model usage, tool activity, delegation, partial reports, and estimated versus observed costs.

## Scope

- Test vectors and validation for usage/accounting interoperability.
- Explicit accounting invariants and ambiguity notes.
- Comparisons across published conventions and implementation reports.
- Loss-aware mapping notes, with evidence and version/source pinning.

## Non-goals

- Defining a new agent protocol or canonical wire format.
- Replacing OpenTelemetry, FOCUS, provider SDKs, or existing agent frameworks.
- Providing a pricing catalog, billing service, cost gateway, or budget enforcer.
- Claiming financial correctness, compliance, or certification.
- Treating estimates as invoices or provider-reported facts.

## Current maturity

- Fixtures are illustrative and should be treated as draft.
- The Agent Run Metrics Internet-Draft is an individual draft, not an IETF standard.
- A passing local fixture validator only checks this repository's fixture structure and selected invariants; it does not establish semantic correctness or provider conformance.
- No live provider/runtime integration or independent review is implied.

## Repository layout

- `docs/source-baselines.md`: source inventory and caveats.
- `docs/accounting-invariants.md`: explicit assumptions and open questions.
- `docs/fixture-format.md`: fixture conventions.
- `fixtures/valid/`: draft cases intended to be structurally valid.
- `fixtures/invalid/`: negative cases.
- `scripts/validate_fixtures.py`: dependency-free structural validator.

## Quick start

```bash
python3 scripts/validate_fixtures.py
python3 -m unittest discover -s tests -v
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), and the [review checklist](docs/review-checklist.md).

## License

MIT. See [LICENSE](LICENSE).

## Ecosystem directory

This project is part of the [HuffmanRepositories public ecosystem](https://github.com/HuffmanRepositories/Huffman-Ecosystem-Root). Use the directory for project routing, human and AI onboarding, shared terminology, governance, and related workstreams. This repository's own README and specifications remain authoritative for its scope, maturity, and validation status.

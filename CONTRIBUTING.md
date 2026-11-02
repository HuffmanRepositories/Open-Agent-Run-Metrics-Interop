# Contributing

OARMI prioritizes careful scope, transparent evidence, and reproducible test vectors.

## Before proposing changes

1. Read the README, source baselines, and accounting invariants.
2. Identify whether the change is a fixture, observation, mapping, or proposal.
3. Cite a stable source/version for claims about external systems.
4. Mark assumptions and unresolved behavior explicitly.
5. Avoid implying a provider or standards-body endorsement.

## Fixture requirements

- Use unique stable fixture IDs.
- Keep fixtures synthetic; do not include credentials, customer data, or real billing records.
- State the expected behavior and rationale.
- Distinguish source-reported values from estimates and derived values.
- Include a negative case when an invariant can be violated.
- Do not silently normalize away meaningful differences.

## Validation

Run:

```bash
python3 scripts/validate_fixtures.py
python3 -m unittest discover -s tests -v
```

Validation is structural and limited; reviewers must still inspect semantic assumptions.

## Pull requests

Explain the motivation, source/version, behavior changed, known limitations, and test evidence. If no test was run, say so.

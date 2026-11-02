# Fixture format (draft)

Fixtures are synthetic JSON documents. Format is intentionally small and repository-local; it is not presented as an official schema.

## Common fields

- `fixture_id`: stable unique identifier.
- `title`: concise case name.
- `status`: `draft`.
- `category`: test category.
- `input`: illustrative event/report payload.
- `expected`: expected result or validation observation.
- `notes`: caveats and assumptions.

The validator checks basic JSON structure, required keys, and unique IDs. It does not prove semantic correctness, provider compatibility, or standards conformance.

## Expected result conventions

Use descriptive outcomes (e.g. `accept`, `reject`, `review_required`, `no_double_count`) and explain why. Do not imply a fixture is a normative requirement unless the cited source supports it.

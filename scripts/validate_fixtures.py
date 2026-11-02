#!/usr/bin/env python3
"""Small dependency-free validator for OARMI draft fixture envelopes."""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIRS = (ROOT / "fixtures" / "valid", ROOT / "fixtures" / "invalid")
REQUIRED = {"fixture_id", "title", "status", "category", "input", "expected", "notes"}

def validate() -> list[str]:
    errors: list[str] = []
    seen: dict[str, Path] = {}
    count = 0
    for directory in FIXTURE_DIRS:
        if not directory.exists():
            errors.append(f"missing fixture directory: {directory.relative_to(ROOT)}")
            continue
        for path in sorted(directory.glob("*.json")):
            count += 1
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
                continue
            if not isinstance(data, dict):
                errors.append(f"{path.relative_to(ROOT)}: top-level value must be an object")
                continue
            missing = REQUIRED - data.keys()
            if missing:
                errors.append(f"{path.relative_to(ROOT)}: missing keys: {', '.join(sorted(missing))}")
            for key in ("fixture_id", "title", "status", "category", "notes"):
                if key in data and (not isinstance(data[key], str) or not data[key].strip()):
                    errors.append(f"{path.relative_to(ROOT)}: {key} must be a non-empty string")
            if data.get("status") != "draft":
                errors.append(f"{path.relative_to(ROOT)}: status must currently be 'draft'")
            for key in ("input", "expected"):
                if key in data and not isinstance(data[key], dict):
                    errors.append(f"{path.relative_to(ROOT)}: {key} must be an object")
            fixture_id = data.get("fixture_id")
            if isinstance(fixture_id, str):
                if fixture_id in seen:
                    errors.append(f"duplicate fixture_id {fixture_id!r}: {seen[fixture_id]} and {path.relative_to(ROOT)}")
                else:
                    seen[fixture_id] = path.relative_to(ROOT)
    if count == 0:
        errors.append("no fixture JSON files found")
    return errors

if __name__ == "__main__":
    issues = validate()
    if issues:
        print("Fixture validation FAILED:")
        for issue in issues:
            print(f"- {issue}")
        sys.exit(1)
    print(f"Fixture envelope validation passed ({len(list(FIXTURE_DIRS[0].glob('*.json'))) + len(list(FIXTURE_DIRS[1].glob('*.json')))} fixtures).")
    print("Note: this checks structure only, not semantic correctness or conformance.")

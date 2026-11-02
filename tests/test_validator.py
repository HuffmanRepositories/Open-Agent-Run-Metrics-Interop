import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_fixtures.py"
spec = importlib.util.spec_from_file_location("oarmi_validator", SCRIPT)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)

class FixtureValidatorTests(unittest.TestCase):
    def test_repository_fixtures_have_valid_envelopes(self):
        self.assertEqual(validator.validate(), [])

    def test_required_keys_are_declared(self):
        self.assertIn("fixture_id", validator.REQUIRED)
        self.assertIn("expected", validator.REQUIRED)

if __name__ == "__main__":
    unittest.main()

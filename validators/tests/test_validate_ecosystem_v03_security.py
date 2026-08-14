from __future__ import annotations
import json,unittest
from pathlib import Path
from validators.validate_ecosystem_v03_security import SecurityValidationError,validate_record

ROOT=Path(__file__).resolve().parents[2]
POS=ROOT/"fixtures/ecosystem-v03/security/positive"
NEG=ROOT/"fixtures/ecosystem-v03/security/negative"

class EcosystemV03SecurityTests(unittest.TestCase):
 def test_all_positive_grants(self):
  paths=sorted(POS.glob("*.json"));self.assertEqual(len(paths),5)
  for path in paths:
   with self.subTest(path=path.name):validate_record(json.loads(path.read_text(encoding="utf-8")))

 def test_all_negative_blockers(self):
  paths=sorted(NEG.glob("*.json"));self.assertEqual(len(paths),9)
  for path in paths:
   case=json.loads(path.read_text(encoding="utf-8"))
   with self.subTest(path=path.name):
    with self.assertRaises(SecurityValidationError) as caught:validate_record(case["record"])
    self.assertEqual(caught.exception.code,case["expected_blocker"])

 def test_schema_is_closed_fixture_contract(self):
  schema=json.loads((ROOT/"schemas/ecosystem-v03-security-grant.schema.json").read_text(encoding="utf-8"))
  self.assertEqual(schema["properties"]["record_kind"]["const"],"ECOSYSTEM_V03_SECURITY_GRANT")
  self.assertFalse(schema["additionalProperties"])

if __name__=="__main__":unittest.main()

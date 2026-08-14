from __future__ import annotations
import json,unittest
from pathlib import Path
from validators.validate_ecosystem_v03_ownership import OwnershipValidationError,validate_record

ROOT=Path(__file__).resolve().parents[2];POS=ROOT/"fixtures/ecosystem-v03/ownership/positive";NEG=ROOT/"fixtures/ecosystem-v03/ownership/negative"

class EcosystemV03OwnershipTests(unittest.TestCase):
 def test_all_positive_scenarios(self):
  paths=sorted(POS.glob("*.json"));self.assertEqual(len(paths),6)
  for path in paths:
   with self.subTest(path=path.name):validate_record(json.loads(path.read_text(encoding="utf-8")))

 def test_all_negative_blockers(self):
  paths=sorted(NEG.glob("*.json"));self.assertEqual(len(paths),10)
  for path in paths:
   case=json.loads(path.read_text(encoding="utf-8"))
   with self.subTest(path=path.name):
    with self.assertRaises(OwnershipValidationError) as caught:validate_record(case["record"])
    self.assertEqual(caught.exception.code,case["expected_blocker"])

 def test_schema_is_closed_fixture_contract(self):
  schema=json.loads((ROOT/"schemas/ecosystem-v03-ownership-claim.schema.json").read_text(encoding="utf-8"))
  self.assertEqual(schema["properties"]["record_kind"]["const"],"ECOSYSTEM_V03_OWNERSHIP_CLAIM")
  self.assertFalse(schema["additionalProperties"])

if __name__=="__main__":unittest.main()

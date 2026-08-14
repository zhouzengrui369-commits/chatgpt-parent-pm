from __future__ import annotations
import hashlib, json, unittest
from pathlib import Path
from validators.validate_ecosystem_v03_adoption import AdoptionValidationError, validate_record, validate_transition

ROOT=Path(__file__).resolve().parents[2]
POS=ROOT/"fixtures/ecosystem-v03/positive"
NEG=ROOT/"fixtures/ecosystem-v03/negative"
ECO="e46c4be501c465884486a4417adca2e158a58ccc"
SOURCE="ded00acf02d7714d36c4bcb73b132cb3defdaf09"
MANIFEST="15b989f37028682ca7e1a07e6061f7ebf03eff30c1c5d7a5c4bec90c5326056a"
SCHEMA="0e21d3e9f8c07586f4ee896376885ccc27bc7250cb2351f3ab5bec3b87e05324"

class EcosystemV03AdoptionTests(unittest.TestCase):
 def validate(self,data):
  validate_record(data,expected_ecosystem_sha=ECO,expected_contract_source=SOURCE,expected_contract_manifest_sha256=MANIFEST,expected_contract_schema_sha256=SCHEMA)

 def test_all_positive_role_fixtures(self):
  paths=sorted(POS.glob("*.json"));self.assertEqual(len(paths),5)
  for path in paths:
   with self.subTest(path=path.name):self.validate(json.loads(path.read_text(encoding="utf-8")))

 def test_all_negative_blockers(self):
  paths=sorted(NEG.glob("*.json"));self.assertEqual(len(paths),5)
  for path in paths:
   case=json.loads(path.read_text(encoding="utf-8"))
   with self.subTest(path=path.name):
    with self.assertRaises(AdoptionValidationError) as caught:self.validate(case["record"])
    self.assertEqual(caught.exception.code,case["expected_blocker"])

 def test_valid_transition(self):
  validate_transition("QUEUED","ACTIVATED");validate_transition("IMPLEMENTING","CANDIDATE");validate_transition("CANDIDATE","ACCEPTED")

 def test_rejects_invalid_transition(self):
  with self.assertRaises(AdoptionValidationError) as caught:validate_transition("QUEUED","ACCEPTED")
  self.assertEqual(caught.exception.code,"BLOCKED_MIGRATION_TRANSITION_INVALID")

 def test_lock_manifest_hash_matches_fixtures(self):
  lock_path=ROOT/"contracts/ecosystem-v03/shared-knowledge-v0.3.0.lock.json"
  self.assertEqual(hashlib.sha256(lock_path.read_bytes()).hexdigest(),MANIFEST)
  for path in sorted(POS.glob("*.json")):
   record=json.loads(path.read_text(encoding="utf-8"))
   self.assertEqual(record["shared_knowledge_engine"]["contract"]["contract_manifest_sha256"],MANIFEST)

 def test_schema_declares_additive_record(self):
  schema=json.loads((ROOT/"schemas/ecosystem-v03-adoption.schema.json").read_text(encoding="utf-8"))
  self.assertEqual(schema["properties"]["record_kind"]["const"],"ECOSYSTEM_V03_ADOPTION")
  self.assertFalse(schema["additionalProperties"])

if __name__=="__main__":unittest.main()

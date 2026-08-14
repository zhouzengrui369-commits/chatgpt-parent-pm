from __future__ import annotations
import copy,json,unittest
from pathlib import Path
from validators.validate_ecosystem_v03_regression import EXPECTED_COUNTS,RegressionValidationError,git_blob_sha,validate_release_candidate

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/"releases/v0.3.0-rc.1/MANIFEST.json"

class EcosystemV03RegressionTests(unittest.TestCase):
 def test_release_candidate_regression(self):self.assertEqual(validate_release_candidate(MANIFEST),EXPECTED_COUNTS)

 def test_manifest_is_not_release_claim(self):
  data=json.loads(MANIFEST.read_text(encoding="utf-8"));self.assertEqual(data["state"],"CANDIDATE_NOT_RELEASED");self.assertIn("NOT_RELEASED",data["claim_ceiling"])

 def test_git_blob_function_matches_manifest(self):
  data=json.loads(MANIFEST.read_text(encoding="utf-8"))
  for entry in data["sources"]:
   with self.subTest(path=entry["path"]):self.assertEqual(git_blob_sha(ROOT/entry["path"]),entry["git_blob_sha"])

if __name__=="__main__":unittest.main()

from __future__ import annotations
import unittest
from pathlib import Path
from validators.validate_ecosystem_v03_starter_kit import StarterKitValidationError,validate_manifest,validate_template_text

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/"starter-kit/ecosystem-v03/template-manifest.json"

class EcosystemV03StarterKitTests(unittest.TestCase):
 def test_complete_kit(self):validate_manifest(MANIFEST)

 def test_missing_placeholder_blocks(self):
  with self.assertRaises(StarterKitValidationError) as caught:validate_template_text("x","{{A}}",["{{A}}","{{B}}"])
  self.assertEqual(caught.exception.code,"BLOCKED_STARTER_TEMPLATE_PLACEHOLDER_MISSING")

 def test_moving_ref_blocks(self):
  with self.assertRaises(StarterKitValidationError) as caught:validate_template_text("x","{{A}} latest",["{{A}}"])
  self.assertEqual(caught.exception.code,"BLOCKED_MOVING_REF_FORBIDDEN")

 def test_local_path_blocks(self):
  with self.assertRaises(StarterKitValidationError) as caught:validate_template_text("x","{{A}} /Users/example",["{{A}}"])
  self.assertEqual(caught.exception.code,"BLOCKED_STARTER_TEMPLATE_UNSAFE_CONTENT")

if __name__=="__main__":unittest.main()

import json
import tempfile
import unittest
from pathlib import Path

from validators.validate_install import validate


class ValidateInstallTests(unittest.TestCase):
    def make_project(self, root: Path, commit: str = "1" * 40) -> None:
        required = {
            "AGENTS.md": "# agents\n",
            "PROJECT_STATUS.md": "# status\n",
            ".github/skills/chatgpt-parent-pm/SKILL.md": "# skill\n",
            ".github/skills/chatgpt-parent-pm/PROJECT_PROFILE.yaml": """
project_id: demo
project_type: web-app
repository: owner/demo
default_branch: main
roles: {}
commands: {}
policies:
  direct_main_write: false
  automatic_merge: false
  automatic_release: false
owner_only_actions: []
""",
            ".github/skills/chatgpt-parent-pm/GOVERNANCE_LOCK.json": json.dumps({
                "framework": "chatgpt-parent-pm",
                "core_commit": commit,
                "policies": {
                    "direct_main_write": False,
                    "automatic_merge": False,
                    "automatic_release": False,
                },
            }),
        }
        for rel, content in required.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    def test_valid_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_project(root)
            self.assertEqual(validate(root), [])

    def test_placeholder_lock_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_project(root, "0" * 40)
            self.assertIn("governance lock still uses the placeholder core_commit", validate(root))

    def test_unsafe_policy_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_project(root)
            profile = root / ".github/skills/chatgpt-parent-pm/PROJECT_PROFILE.yaml"
            profile.write_text(profile.read_text().replace("automatic_merge: false", "automatic_merge: true"))
            self.assertTrue(any("unsafe project policy" in error for error in validate(root)))


if __name__ == "__main__":
    unittest.main()

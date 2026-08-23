import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "starter-kit/.github/workflows/private-runner-technical-gate.yml.template"
POLICY = ROOT / "core/PRIVATE_REPO_EXECUTION_POLICY.md"
AUTHORITY = ROOT / "core/PRIVATE_RUNNER_FRAMEWORK_AUTHORITY.json"
PROFILE = ROOT / "starter-kit/.github/skills/chatgpt-parent-pm/PROJECT_PROFILE.yaml"


class PrivateRepoExecutionPolicyTests(unittest.TestCase):
    def test_private_starter_uses_only_self_hosted_compute(self):
        text = TEMPLATE.read_text(encoding="utf-8")
        self.assertIn(
            "runs-on: [self-hosted, macOS, ARM64, __PROJECT_RUNNER_LABEL__]", text
        )
        self.assertNotIn("runs-on: ubuntu-", text)
        self.assertNotIn("runs-on: windows-", text)
        self.assertNotIn("runs-on: macos-", text)
        self.assertNotIn("actions/upload-artifact@", text)
        self.assertIn("EVIDENCE_TRANSPORT=LOCAL_DURABLE_PLUS_LOG_DIGEST", text)

    def test_checkout_is_full_sha_pinned_and_tree_is_required(self):
        text = TEMPLATE.read_text(encoding="utf-8")
        self.assertIn(
            "actions/checkout@11d5960a326750d5838078e36cf38b85af677262", text
        )
        self.assertNotIn("actions/checkout@v4", text)
        self.assertIn("candidate_tree:", text)
        candidate_tree = text.split("candidate_tree:", 1)[1].split("permissions:", 1)[0]
        self.assertIn("required: true", candidate_tree)
        self.assertIn('test "$ACTUAL_TREE" = "$CANDIDATE_TREE"', text)

    def test_framework_authority_is_exact_and_self_hosted_only(self):
        authority = json.loads(AUTHORITY.read_text(encoding="utf-8"))
        self.assertEqual(authority["core_version"], "0.1.2-alpha")
        self.assertEqual(
            authority["framework_sha"],
            "ea051b03bdf7bbccb3de447ccd36f8e17bd2d0f7",
        )
        self.assertEqual(
            authority["predecessor_framework_sha"],
            "69b1515c137a6389a8afdccd07114b00e9eb8f1f",
        )
        self.assertEqual(authority["policy"], "PRIVATE_REPO_SELF_HOSTED_ONLY_R2")
        self.assertFalse(authority["github_hosted_runner_required"])
        self.assertFalse(authority["billing_dependency_allowed"])
        self.assertFalse(authority["artifact_storage_required"])
        self.assertEqual(
            authority["local_agent_fallback"], "OUT_OF_BAND_DIAGNOSTIC_ONLY"
        )
        self.assertEqual(
            authority["consumer_rule"], "PIN_EXACT_FRAMEWORK_SHA_NO_AUTO_MIGRATION"
        )

    def test_policy_and_profile_reject_billing_dependency_by_default(self):
        policy = POLICY.read_text(encoding="utf-8")
        profile = PROFILE.read_text(encoding="utf-8")
        self.assertIn("PRIVATE_RUNNER_FRAMEWORK_AUTHORITY.json", policy)
        self.assertIn("Billing-dependent hosted execution is forbidden by default", policy)
        self.assertIn("github_hosted_runner_required: false", profile)
        self.assertIn("billing_dependency_allowed: false", profile)
        self.assertIn("silent_local_agent_fallback: false", profile)


if __name__ == "__main__":
    unittest.main()

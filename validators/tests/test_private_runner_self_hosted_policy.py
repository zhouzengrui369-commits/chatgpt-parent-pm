import tempfile
import unittest
from pathlib import Path

from validators.validate_private_runner import validate_receipt, validate_workflow


class PrivateRunnerSelfHostedPolicyTests(unittest.TestCase):
    def template(self) -> Path:
        return (
            Path(__file__).resolve().parents[2]
            / "starter-kit/private-runner/private-runner-technical-gate.yml.template"
        )

    def test_template_has_no_metered_github_execution_or_artifact_dependency(self):
        text = self.template().read_text(encoding="utf-8")
        self.assertNotIn("runs-on: ubuntu-", text)
        self.assertNotIn("runs-on: windows-", text)
        self.assertNotIn("runs-on: macos-", text)
        self.assertNotIn("actions/upload-artifact@", text)
        self.assertIn(
            "runs-on: [self-hosted, macOS, ARM64, __REPOSITORY_LABEL__]", text
        )
        self.assertIn("EVIDENCE_TRANSPORT=LOCAL_DURABLE_PLUS_LOG_DIGEST", text)
        self.assertEqual(validate_workflow(self.template()), [])

    def test_github_hosted_runner_is_fail_closed(self):
        text = self.template().read_text(encoding="utf-8").replace(
            "runs-on: [self-hosted, macOS, ARM64, __REPOSITORY_LABEL__]",
            "runs-on: ubuntu-latest",
            1,
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "workflow.yml"
            path.write_text(text, encoding="utf-8")
            errors = validate_workflow(path)
        self.assertIn("BLOCKED_PRIVATE_RUNNER_GITHUB_HOSTED_DEPENDENCY", errors)

    def test_github_artifact_storage_dependency_is_fail_closed(self):
        text = self.template().read_text(encoding="utf-8") + "\nuses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02\n"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "workflow.yml"
            path.write_text(text, encoding="utf-8")
            errors = validate_workflow(path)
        self.assertIn(
            "BLOCKED_PRIVATE_RUNNER_GITHUB_ARTIFACT_STORAGE_DEPENDENCY", errors
        )

    @staticmethod
    def request():
        return {
            "request_id": "r",
            "attempt_id": "a",
            "repository": "o/r",
            "candidate_sha": "1" * 40,
            "candidate_tree": "2" * 40,
            "runner_profile_sha256": "3" * 64,
        }

    def test_pre_source_block_does_not_become_false_source_dirty(self):
        request = self.request()
        receipt = {
            "schema_version": "parent-pm.runner-execution-receipt.v1",
            **request,
            "verdict": "BLOCKED",
            "first_blocker": "RUNNER_DEFECT",
            "source_clean": {"pre": False, "post": False},
            "gate_results": {"exact_source_transport": "UNPROVEN"},
            "mutation_counters": {},
            "artifacts": [],
        }
        self.assertEqual(validate_receipt(receipt, request), [])

    def test_source_transport_pass_still_requires_clean_source(self):
        request = self.request()
        receipt = {
            "schema_version": "parent-pm.runner-execution-receipt.v1",
            **request,
            "verdict": "FAIL",
            "first_blocker": "RUNTIME_DEFECT",
            "source_clean": {"pre": True, "post": False},
            "gate_results": {"exact_source_transport": "PASS"},
            "mutation_counters": {},
            "artifacts": [],
        }
        self.assertIn("BLOCKED_RUNNER_SOURCE_DIRTY", validate_receipt(receipt, request))


if __name__ == "__main__":
    unittest.main()

import tempfile
import unittest
from pathlib import Path

from validators.validate_private_runner import validate_workflow


class PrivateRunnerSelfHostedPolicyTests(unittest.TestCase):
    def template(self) -> Path:
        return (
            Path(__file__).resolve().parents[2]
            / "starter-kit/private-runner/private-runner-technical-gate.yml.template"
        )

    def test_template_has_no_github_hosted_compute_dependency(self):
        text = self.template().read_text(encoding="utf-8")
        self.assertNotIn("runs-on: ubuntu-", text)
        self.assertNotIn("runs-on: windows-", text)
        self.assertNotIn("runs-on: macos-", text)
        self.assertIn(
            "runs-on: [self-hosted, macOS, ARM64, __REPOSITORY_LABEL__]", text
        )
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


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from validators.validate_v03_g0_snapshot import SnapshotValidationError, validate_snapshot

ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT = ROOT / "work/tasks/2026-08-14-parent-pm-v03-g0-activation" / "CURRENT_TRUTH_SNAPSHOT.json"
MAIN_SHA = "99e88020789603f17de715775b455e91e4e20b17"
PROTECTED_HEAD = "93356868f656384c5023bd9db666c73a8524d224"


class V03G0SnapshotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid = json.loads(SNAPSHOT.read_text(encoding="utf-8"))

    def assert_blocked(self, payload, code: str) -> None:
        with self.assertRaises(SnapshotValidationError) as caught:
            validate_snapshot(payload, expected_main_sha=MAIN_SHA, expected_protected_head=PROTECTED_HEAD)
        self.assertEqual(caught.exception.code, code)

    def test_valid_snapshot(self) -> None:
        validate_snapshot(self.valid, expected_main_sha=MAIN_SHA, expected_protected_head=PROTECTED_HEAD)

    def test_rejects_stale_main(self) -> None:
        payload = copy.deepcopy(self.valid)
        payload["framework"]["main_sha"] = "0" * 40
        self.assert_blocked(payload, "E_MAIN_SHA_MISMATCH")

    def test_rejects_protected_head_drift(self) -> None:
        payload = copy.deepcopy(self.valid)
        payload["protected_lane"]["head_sha"] = "1" * 40
        self.assert_blocked(payload, "E_PROTECTED_HEAD_MISMATCH")

    def test_rejects_queued_state(self) -> None:
        payload = copy.deepcopy(self.valid)
        payload["migration_state"] = "QUEUED"
        self.assert_blocked(payload, "E_MIGRATION_STATE")

    def test_rejects_consumer_change(self) -> None:
        payload = copy.deepcopy(self.valid)
        payload["consumer_boundary"]["consumer_product_change"] = True
        self.assert_blocked(payload, "E_CONSUMER_BOUNDARY")

    def test_rejects_breaking_compatibility(self) -> None:
        payload = copy.deepcopy(self.valid)
        payload["compatibility"]["mode"] = "REPLACE"
        self.assert_blocked(payload, "E_COMPATIBILITY_MODE")

    def test_rejects_machine_contract_source_drift(self) -> None:
        payload = copy.deepcopy(self.valid)
        payload["ecosystem"]["machine_contract"]["exact_tested_source_sha"] = "2" * 40
        self.assert_blocked(payload, "E_MACHINE_CONTRACT_SOURCE")


if __name__ == "__main__":
    unittest.main()

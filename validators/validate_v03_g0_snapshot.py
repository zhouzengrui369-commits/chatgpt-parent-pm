#!/usr/bin/env python3
"""Validate the exact, fail-closed Parent PM v0.3 G0 truth snapshot."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
REQUIRED_CEILINGS = {
    "G0_GOVERNANCE_MAPPING_ONLY",
    "NO_CONSUMER_PRODUCT_CHANGE",
    "NO_PRODUCT_RUNTIME_PROOF",
    "NO_MERGE",
    "NO_RELEASE",
}


class SnapshotValidationError(ValueError):
    def __init__(self, code: str, path: str):
        super().__init__(f"{code}:{path}")
        self.code = code
        self.path = path


def require(condition: bool, code: str, path: str) -> None:
    if not condition:
        raise SnapshotValidationError(code, path)


def at(data: dict[str, Any], *path: str) -> Any:
    current: Any = data
    for part in path:
        require(isinstance(current, dict) and part in current, "E_REQUIRED_FIELD", ".".join(path))
        current = current[part]
    return current


def validate_snapshot(
    data: dict[str, Any],
    *,
    expected_main_sha: str | None = None,
    expected_protected_head: str | None = None,
) -> None:
    require(data.get("schema_version") == "1.0.0", "E_SCHEMA_VERSION", "schema_version")
    require(data.get("program_id") == "PARENT-PM-ECOSYSTEM-V03-R1", "E_PROGRAM_ID", "program_id")
    require(data.get("migration_state") == "ACTIVATED_G0", "E_MIGRATION_STATE", "migration_state")
    require(at(data, "activation", "current_goal") == "G0_CURRENT_FRAMEWORK_MAPPING", "E_ACTIVE_GOAL", "activation.current_goal")
    require(at(data, "activation", "scope") == "GOVERNANCE_ONLY", "E_SCOPE", "activation.scope")

    main_sha = at(data, "framework", "main_sha")
    require(isinstance(main_sha, str) and HEX40.fullmatch(main_sha) is not None, "E_MAIN_SHA", "framework.main_sha")
    if expected_main_sha is not None:
        require(main_sha == expected_main_sha, "E_MAIN_SHA_MISMATCH", "framework.main_sha")
    require(at(data, "framework", "repository") == "zhouzengrui369-commits/chatgpt-parent-pm", "E_FRAMEWORK_REPO", "framework.repository")
    require(at(data, "framework", "version") == "0.1.0-alpha", "E_FRAMEWORK_VERSION", "framework.version")
    for name in ("governance_lock", "local_receipt"):
        blob = at(data, "framework", "existing_schema_blobs", name)
        require(isinstance(blob, str) and HEX40.fullmatch(blob) is not None, "E_SCHEMA_BLOB", f"framework.existing_schema_blobs.{name}")

    require(at(data, "protected_lane", "pull_request") == 3, "E_PROTECTED_PR", "protected_lane.pull_request")
    require(at(data, "protected_lane", "state") == "OPEN_DRAFT", "E_PROTECTED_STATE", "protected_lane.state")
    require(at(data, "protected_lane", "base_ref") == "main", "E_PROTECTED_BASE", "protected_lane.base_ref")
    require(at(data, "protected_lane", "head_ref") == "chatgpt/shared-capability-adoption-r1", "E_PROTECTED_REF", "protected_lane.head_ref")
    protected_head = at(data, "protected_lane", "head_sha")
    require(isinstance(protected_head, str) and HEX40.fullmatch(protected_head) is not None, "E_PROTECTED_HEAD", "protected_lane.head_sha")
    if expected_protected_head is not None:
        require(protected_head == expected_protected_head, "E_PROTECTED_HEAD_MISMATCH", "protected_lane.head_sha")
    geo_hash = at(data, "protected_lane", "geo_context", "schema_sha256")
    require(isinstance(geo_hash, str) and HEX64.fullmatch(geo_hash) is not None, "E_GEO_SCHEMA_HASH", "protected_lane.geo_context.schema_sha256")

    require(at(data, "g0_pull_request", "pull_request") == 4, "E_G0_PR", "g0_pull_request.pull_request")
    require(at(data, "g0_pull_request", "state") == "OPEN_DRAFT", "E_G0_PR_STATE", "g0_pull_request.state")
    require(at(data, "g0_pull_request", "base_ref") == "chatgpt/shared-capability-adoption-r1", "E_G0_STACK_BASE", "g0_pull_request.base_ref")

    require(at(data, "ecosystem", "repository") == "zhouzengrui369-commits/knowme-ecosystem", "E_ECOSYSTEM_REPO", "ecosystem.repository")
    for path in (("ecosystem", "candidate_sha"), ("ecosystem", "machine_contract", "branch_head_sha"), ("ecosystem", "machine_contract", "exact_tested_source_sha")):
        value = at(data, *path)
        require(isinstance(value, str) and HEX40.fullmatch(value) is not None, "E_ECOSYSTEM_SHA", ".".join(path))
    require(at(data, "ecosystem", "machine_contract", "exact_tested_source_sha") == "ded00acf02d7714d36c4bcb73b132cb3defdaf09", "E_MACHINE_CONTRACT_SOURCE", "ecosystem.machine_contract.exact_tested_source_sha")

    require(at(data, "compatibility", "mode") == "ADDITIVE_ONLY", "E_COMPATIBILITY_MODE", "compatibility.mode")
    for field in ("existing_schemas_unchanged", "geo_context_regression_boundary_preserved", "unknown_capabilities_fail_closed"):
        require(at(data, "compatibility", field) is True, "E_COMPATIBILITY_GUARD", f"compatibility.{field}")
    for field in ("consumer_product_change", "product_runtime_tested", "merge_release_authorized"):
        require(at(data, "consumer_boundary", field) is False, "E_CONSUMER_BOUNDARY", f"consumer_boundary.{field}")

    require(at(data, "consumers", "lingxi", "migration_state") == "QUEUED", "E_LINGXI_STATE", "consumers.lingxi.migration_state")
    require(at(data, "consumers", "lingxi", "runtime_gate") == "NOT_PASS", "E_LINGXI_RUNTIME_CLAIM", "consumers.lingxi.runtime_gate")
    require(at(data, "consumers", "lingxi", "mvp_gate") == "NO-GO", "E_LINGXI_MVP_CLAIM", "consumers.lingxi.mvp_gate")
    ceilings = data.get("claim_ceiling")
    require(isinstance(ceilings, list) and REQUIRED_CEILINGS.issubset(set(ceilings)), "E_CLAIM_CEILING", "claim_ceiling")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--expected-main-sha")
    parser.add_argument("--expected-protected-head")
    args = parser.parse_args()
    try:
        payload = json.loads(args.snapshot.read_text(encoding="utf-8"))
        require(isinstance(payload, dict), "E_ROOT_TYPE", "$")
        validate_snapshot(payload, expected_main_sha=args.expected_main_sha, expected_protected_head=args.expected_protected_head)
    except (OSError, json.JSONDecodeError, SnapshotValidationError) as exc:
        if isinstance(exc, SnapshotValidationError):
            result = {"status": "FAIL", "code": exc.code, "path": exc.path}
        else:
            result = {"status": "FAIL", "code": type(exc).__name__, "detail": str(exc)}
        print(json.dumps(result, sort_keys=True))
        return 1
    print(json.dumps({"status": "PASS", "program_id": payload["program_id"], "migration_state": payload["migration_state"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

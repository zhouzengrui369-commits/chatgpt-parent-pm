#!/usr/bin/env python3
"""Validate a ChatGPT Parent PM project installation using only stdlib."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED = [
    "AGENTS.md",
    "PROJECT_STATUS.md",
    ".github/skills/chatgpt-parent-pm/SKILL.md",
    ".github/skills/chatgpt-parent-pm/PROJECT_PROFILE.yaml",
    ".github/skills/chatgpt-parent-pm/GOVERNANCE_LOCK.json",
]

PROFILE_KEYS = [
    "project_id:",
    "project_type:",
    "repository:",
    "default_branch:",
    "roles:",
    "commands:",
    "policies:",
    "owner_only_actions:",
]

PRIVATE_PROFILE_TOKENS = [
    "primary_local_executor: github-self-hosted-runner",
    "github_hosted_runner_required: false",
    "billing_dependency_allowed: false",
    "silent_local_agent_fallback: false",
    "artifact_storage_required: false",
    "evidence_transport: local-durable-plus-log-digest",
    "fail_closed: true",
    "product_attempt_requires_preflight_pass: true",
]

SHA40 = re.compile(r"^[0-9a-f]{40}$")
PINNED_CHECKOUT = re.compile(r"actions/checkout@[0-9a-f]{40}\b")
GITHUB_HOSTED_RUNS_ON = re.compile(
    r"runs-on:\s*(?:\[[^\]]*)?(?:ubuntu|windows|macos)-", re.IGNORECASE
)


def validate_private_execution(root: Path, profile_text: str) -> list[str]:
    errors: list[str] = []
    for token in PRIVATE_PROFILE_TOKENS:
        if token not in profile_text:
            errors.append(f"private project execution policy missing/unsafe: {token}")

    candidates = [
        root / ".github/workflows/private-runner-technical-gate.yml",
        root / ".github/workflows/private-runner-technical-gate.yml.template",
    ]
    gate = next((path for path in candidates if path.is_file()), None)
    if gate is None:
        errors.append("private project missing self-hosted technical gate workflow/template")
        return errors

    workflow = gate.read_text(encoding="utf-8")
    if "runs-on: [self-hosted," not in workflow:
        errors.append("private technical gate must run on self-hosted runner")
    if GITHUB_HOSTED_RUNS_ON.search(workflow):
        errors.append("private technical gate must not require GitHub-hosted compute")
    if "actions/upload-artifact@" in workflow:
        errors.append("private technical gate must not require GitHub artifact storage")
    if "actions/checkout@" in workflow and not PINNED_CHECKOUT.search(workflow):
        errors.append("private technical gate checkout action must use a full 40-hex pin")
    if "candidate_tree:" not in workflow or "required: true" not in workflow.split(
        "candidate_tree:", 1
    )[1].split("permissions:", 1)[0]:
        errors.append("private technical gate must require exact candidate tree")
    if "EVIDENCE_TRANSPORT=LOCAL_DURABLE_PLUS_LOG_DIGEST" not in workflow:
        errors.append("private technical gate must expose local durable evidence digest transport")
    return errors


def validate(root: Path, allow_placeholder_lock: bool = False) -> list[str]:
    errors: list[str] = []

    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")

    profile = root / ".github/skills/chatgpt-parent-pm/PROJECT_PROFILE.yaml"
    if profile.is_file():
        text = profile.read_text(encoding="utf-8")
        for key in PROFILE_KEYS:
            if key not in text:
                errors.append(f"project profile missing key: {key}")
        for unsafe in (
            "direct_main_write: true",
            "automatic_merge: true",
            "automatic_release: true",
        ):
            if unsafe in text:
                errors.append(f"unsafe project policy: {unsafe}")
        if "repository_visibility: private" in text:
            errors.extend(validate_private_execution(root, text))

    lock_path = root / ".github/skills/chatgpt-parent-pm/GOVERNANCE_LOCK.json"
    if lock_path.is_file():
        try:
            lock = json.loads(lock_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid governance lock JSON: {exc}")
        else:
            if lock.get("framework") != "chatgpt-parent-pm":
                errors.append("governance lock framework must be chatgpt-parent-pm")
            commit = lock.get("core_commit", "")
            if not SHA40.fullmatch(commit):
                errors.append("governance lock core_commit must be a lowercase 40-hex SHA")
            elif commit == "0" * 40 and not allow_placeholder_lock:
                errors.append("governance lock still uses the placeholder core_commit")
            policies = lock.get("policies", {})
            for key in ("direct_main_write", "automatic_merge", "automatic_release"):
                if policies.get(key) is not False:
                    errors.append(f"governance lock policy {key} must be false")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--allow-placeholder-lock", action="store_true")
    args = parser.parse_args()

    errors = validate(Path(args.root).resolve(), args.allow_placeholder_lock)
    if errors:
        print("GOVERNANCE_INSTALL: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("GOVERNANCE_INSTALL: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

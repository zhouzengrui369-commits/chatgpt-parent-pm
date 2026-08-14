#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

MODES = {"RUNTIME_PRIMARY", "PLATFORM_CONSUMER", "OUTPUT_CONSUMER", "GOVERNANCE", "REVIEW", "PLAN_ONLY", "OPTIONAL"}
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("lock", type=Path)
    parser.add_argument("--allow-placeholder", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.lock.read_text(encoding="utf-8"))
    required = ["schema_version", "capability_id", "capability_version", "authority_repository", "authority_commit_sha", "contract_path", "contract_sha256", "adoption_mode", "upstream_code_included"]
    missing = [key for key in required if key not in data]
    if missing:
        raise SystemExit("missing fields: " + ",".join(missing))
    if data["adoption_mode"] not in MODES:
        raise SystemExit("invalid adoption_mode")
    sha = str(data["authority_commit_sha"])
    digest = str(data["contract_sha256"])
    placeholder = set(sha) == {"0"} and set(digest) == {"0"}
    if placeholder and args.allow_placeholder:
        print("PASS placeholder capability lock")
        return 0
    if not HEX40.fullmatch(sha):
        raise SystemExit("authority_commit_sha must be exact 40-hex")
    if not HEX64.fullmatch(digest):
        raise SystemExit("contract_sha256 must be 64-hex")
    if data["upstream_code_included"] not in (True, False):
        raise SystemExit("upstream_code_included must be boolean")
    print(f"PASS capability={data['capability_id']} version={data['capability_version']} mode={data['adoption_mode']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

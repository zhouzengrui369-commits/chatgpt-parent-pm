#!/usr/bin/env bash
set -euo pipefail
PROFILE="${RUNNER_PROFILE_PATH:-.github/parent-pm-runner/RUNNER_PROFILE.json}"
MODE="${1:-}"
LOCK_PATH="$(python - "$PROFILE" <<'PY'
import json,sys
print(json.load(open(sys.argv[1],encoding='utf-8'))['global_mutex']['path'])
PY
)"
OWNER_TOKEN="${GITHUB_REPOSITORY:-unknown}:${GITHUB_RUN_ID:-manual}:${GITHUB_RUN_ATTEMPT:-0}"
OWNER_FILE="$LOCK_PATH/owner"

acquire() {
  if mkdir "$LOCK_PATH" 2>/dev/null; then
    printf '%s\n' "$OWNER_TOKEN" > "$OWNER_FILE"
    echo GLOBAL_MAC_MUTEX=ACQUIRED
    return 0
  fi
  echo BLOCKED_GLOBAL_MAC_MUTEX_BUSY
  [ -f "$OWNER_FILE" ] && { printf 'LOCK_OWNER='; cat "$OWNER_FILE"; }
  echo 'Stale locks are never auto-deleted; Parent PM/host owner must adjudicate.'
  return 73
}
release() {
  [ -d "$LOCK_PATH" ] || { echo GLOBAL_MAC_MUTEX=ALREADY_ABSENT; return 0; }
  current="$(cat "$OWNER_FILE" 2>/dev/null || true)"
  [ "$current" = "$OWNER_TOKEN" ] || { echo BLOCKED_GLOBAL_MAC_MUTEX_NOT_OWNER; return 74; }
  rm -f "$OWNER_FILE" && rmdir "$LOCK_PATH"
  echo GLOBAL_MAC_MUTEX=RELEASED
}
case "$MODE" in acquire) acquire;; release) release;; *) echo "usage: $0 acquire|release"; exit 64;; esac

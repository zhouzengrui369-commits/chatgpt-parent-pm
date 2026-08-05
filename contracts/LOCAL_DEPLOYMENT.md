# Local Deployment Contract

- Goal ID:
- Repository:
- Branch:
- Exact candidate SHA:
- Local target:
- Expected clean/dirty-state policy:

## Allowed actions

- identity verification
- exact-SHA checkout or authorized fast-forward
- dependency installation
- build/start/deploy
- smoke testing
- sanitized log collection

## Forbidden actions

- source or test modification
- package/lockfile modification
- commit, amend, rebase, merge, force-push
- PR state changes
- secret publication

## Receipt

- Observed local SHA:
- Build command/result:
- Start command/result:
- Runtime endpoint/path:
- Smoke result:
- Logs/artifacts:
- What was not tested:
- Verdict: PASS / PARTIAL PASS / BLOCKED / FAIL

# Local Deployment Contract

Executor: `OWNER_AUTHORIZED_LOCAL_AGENT` only.

```text
GITHUB=CONTROL_PLANE_ONLY
GITHUB_HOSTED_RUNNER=FORBIDDEN
SELF_HOSTED_RUNNER=FORBIDDEN
LOCAL_DEPLOYMENT=OWNER_AUTHORIZED_LOCAL_AGENT_ONLY
```

- Goal ID:
- Repository:
- Branch:
- Exact candidate SHA:
- Local target:
- Expected clean/dirty-state policy:
- Engineering Delivery contract/ref:

## Allowed Local Agent actions

- identity verification
- exact-SHA checkout or authorized fast-forward
- dependency installation
- local build/start/deploy
- prescribed technical tests
- prescribed runtime/device/data/browser smoke
- Owner-machine credential injection through authorized local mechanisms
- sanitized log/observation collection

## Forbidden actions

- GitHub-hosted Runner execution
- self-hosted Runner execution
- silent executor fallback
- source or test modification
- package/lockfile modification
- commit, amend, rebase, merge, force-push
- PR state changes
- self-repair or scope expansion
- secret publication
- `ENGINEERING_READY` declaration
- Candidate Admission / Product Experience / Human Owner Acceptance

## Receipt

- Executor identity: OWNER_AUTHORIZED_LOCAL_AGENT
- Observed local SHA:
- Observed tree/parent:
- Build command/result:
- Test command/result:
- Start/deploy command/result:
- Runtime endpoint/path:
- Smoke result:
- Clean state before/after:
- Zero prohibited writes:
- Logs/artifacts:
- What was not tested:
- Verdict: PASS / PARTIAL PASS / BLOCKED / FAIL

The Local Agent receipt is observation-only. The role owning the applicable evidence bucket adjudicates the receipt.

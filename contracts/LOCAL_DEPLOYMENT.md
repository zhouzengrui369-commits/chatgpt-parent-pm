# Local Deployment Contract

Executor: `LOCAL_AGENT` only.

```text
GITHUB=CONTROL_PLANE_ONLY
GITHUB_HOSTED_RUNNER=FORBIDDEN
SELF_HOSTED_RUNNER=FORBIDDEN
LOCAL_DEPLOYMENT=LOCAL_AGENT_ONLY
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
- local runtime configuration and credential injection/generation required by the Engineering Delivery contract
- sanitized log/observation collection

A local runtime-only technical secret may be generated/stored locally when required by the Engineering Delivery contract if it does not grant new external-account authority, authorize payment/production/irreversible action, and is never printed/exported/committed/uploaded/returned in the receipt.

## Forbidden actions

- GitHub-hosted Runner execution
- self-hosted Runner execution
- silent executor fallback
- source or test modification
- package/lockfile modification
- commit, amend, rebase, merge, force-push
- PR state changes
- self-repair or scope expansion
- secret publication/export
- external account/provider authorization not already granted
- payment/billing/production authorization
- `ENGINEERING_READY` declaration
- Candidate Admission / Product Experience / Human Owner Acceptance

## Receipt

- Executor identity: LOCAL_AGENT
- Observed local SHA:
- Observed tree/parent:
- Build command/result:
- Test command/result:
- Start/deploy command/result:
- Runtime endpoint/path:
- Smoke result:
- Local runtime secret status (non-secret metadata only):
- Clean state before/after:
- Zero prohibited writes:
- Secret value exported: false
- Logs/artifacts:
- What was not tested:
- Verdict: PASS / PARTIAL PASS / BLOCKED / FAIL

The Local Agent receipt is observation-only. The role owning the applicable evidence bucket adjudicates the receipt.

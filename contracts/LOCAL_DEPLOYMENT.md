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
- exact-SHA materialization
- dependency installation
- local build/start/deploy
- prescribed technical tests
- prescribed runtime/device/data/browser smoke
- local runtime configuration and local runtime-only technical secret generation/storage required by Engineering Delivery contract
- sanitized log/observation collection

A local runtime-only secret is technical configuration, not a Human Owner gate, when it grants no new external-account permission, billing/payment authority, production authority or irreversible capability and is never printed/exported/committed/uploaded/returned in the receipt.

## Forbidden actions

- GitHub-hosted Runner execution
- self-hosted Runner execution
- silent executor fallback
- source/test/workflow/lockfile modification
- commit, amend, rebase, merge, force-push
- PR state changes
- self-repair or scope expansion
- secret publication/export
- unauthorized external account/provider changes
- payment/billing/production authorization
- `ENGINEERING_READY` declaration
- Candidate Admission / Product Experience / Human Owner Acceptance

## Receipt

- Executor identity: LOCAL_AGENT
- Observed local SHA/tree/parent:
- Build/test/start results:
- Runtime endpoint/path:
- Runtime configuration compliance:
- Local runtime secret present/requirements match (non-secret metadata only):
- Secret value exported: false
- Clean state before/after:
- Zero prohibited writes:
- Logs/artifacts:
- What was not tested:
- Verdict: PASS / PARTIAL PASS / BLOCKED / FAIL

The Local Agent receipt is observation-only. The role owning the applicable evidence bucket adjudicates the receipt.

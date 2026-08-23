# GitHub Self-hosted Runner Adapter

Use this adapter as the primary local execution channel for private repositories.

## Contract

The Parent PM writes immutable candidate identity and task scope into GitHub. GitHub Actions triggers a repository/project-owned self-hosted runner. The runner executes preflight, exact-SHA validation, build/test/runtime/browser gates, and emits machine-readable evidence back through the workflow.

Recommended labels:

```text
self-hosted
macOS
ARM64
<project-specific-runner-label>
```

The workflow SHOULD also assert `RUNNER_NAME` against the project profile so a generic label match cannot silently substitute a different machine.

## Fail-closed order

1. validate task inputs;
2. validate runner name / OS / architecture;
3. checkout and verify exact SHA/tree;
4. validate governance/static preflight;
5. only then set `PRODUCT_ATTEMPT_STARTED=true` and run product commands;
6. emit receipt/evidence even on failure.

A queued workflow is not execution evidence. A repository may advertise this adapter only after the runner has been registered and a health/gate job has actually run on the expected machine.

## Fallback

If the runner is offline, unregistered, or the GitHub Actions control plane cannot dispatch the job, use a local agent only for diagnostics/bootstrap unless the Goal explicitly authorizes another execution route. Preserve the same exact-SHA and evidence requirements.

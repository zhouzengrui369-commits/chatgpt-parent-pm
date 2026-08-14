# TASK — G0 current-framework mapping

## Objective

Turn the queued v0.3 plan into an active, fail-closed governance Goal without altering the protected Shared Capability Adoption lane.

## In scope

- this task root;
- `docs/plans/ECOSYSTEM_V03_GOVERNANCE_ADOPTION.md` state annotation;
- `validators/validate_v03_g0_snapshot.py`;
- its unit tests;
- one path-scoped GitHub Actions workflow.

## Prohibited

- modifying PR #3 files, existing schemas, Geo Context identities, consumer repositories or product runtime;
- merge, release, paid calls, secrets, local deployment, or claim uplift.

## Required validation

```bash
python validators/validate_v03_g0_snapshot.py work/tasks/2026-08-14-parent-pm-v03-g0-activation/CURRENT_TRUTH_SNAPSHOT.json \
  --expected-main-sha 99e88020789603f17de715775b455e91e4e20b17 \
  --expected-protected-head 93356868f656384c5023bd9db666c73a8524d224
python -m unittest validators.tests.test_validate_v03_g0_snapshot -v
git diff --check <PR-base>...HEAD
```

## Acceptance

All commands pass on the exact PR head; PR #4 remains Draft and stacked on PR #3; no consumer/product gate changes.

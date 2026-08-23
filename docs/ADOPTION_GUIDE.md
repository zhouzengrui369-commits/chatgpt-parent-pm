# Adoption Guide

## Existing project

1. Recover current project truth before adding governance.
2. Preserve existing working project skills; do not reinstall or replace them blindly.
3. Compare existing rules with the public core.
4. Add a thin adapter and exact governance lock.
5. Record migration exceptions in the project profile.
6. Validate through an isolated governance PR.

For an existing **private** repository, also migrate execution explicitly:

- register or confirm a project-owned Self-hosted Runner;
- assign a project-specific runner name/label;
- set `primary_local_executor: github-self-hosted-runner`;
- set `github_hosted_runner_required: false`;
- move static preflight, exact-SHA/tree validation, test/build/runtime/browser gates and receipts onto the self-hosted execution chain;
- keep local agents as fallback diagnostics rather than the default product executor;
- do not claim migration complete until a real health/gate job executes on the expected runner.

## New project

Install the starter kit before the first product Goal and set product completion to `0%`.

For a private repository, fill the starter profile's runner name/labels and materialize `private-runner-technical-gate.yml.template` into a project workflow before the first local acceptance gate.

## Upgrades

Core upgrades should arrive as separate PRs. Never auto-overwrite the project profile or project status. Review changed invariants, update the exact core commit, run the validator, and preserve project-specific rules.

When adopting `0.1.1-alpha` from an older core, remove any migration exception that says Self-hosted Runner capability is unavailable only after the project has installed the new adapter/workflow and produced an actual expected-runner receipt.

## Role customization

Local executors are capability-based. A GitHub Self-hosted Runner is the default private-repository execution plane. Codex, MiniMax Code, OpenClaw, Claude Code, another local agent, or a human may implement a fallback local role if they obey the same exact-SHA and evidence contract.

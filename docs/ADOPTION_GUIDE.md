# Adoption Guide

## Existing project

1. Recover current project truth before adding governance.
2. Preserve existing working project skills; do not reinstall or replace them blindly.
3. Compare existing rules with the public core.
4. Add a thin adapter and exact governance lock.
5. Record migration exceptions in the project profile.
6. Validate through an isolated governance PR.

## New project

Install the starter kit before the first product Goal and set product completion to `0%`.

## Upgrades

Core upgrades should arrive as separate PRs. Never auto-overwrite the project profile or project status. Review changed invariants, update the exact core commit, run the validator, and preserve project-specific rules.

## Role customization

Local executors are capability-based. Codex, MiniMax Code, OpenClaw, Claude Code, a CI runner, or a human can implement a local role if they obey the same contract.

# Changelog

## 0.1.2-alpha — 2026-08-23

- Pin the canonical private Runner R2 framework authority to exact SHA `ea051b03bdf7bbccb3de447ccd36f8e17bd2d0f7`.
- Harden the private starter workflow to require exact SHA + tree, full-SHA-pinned checkout, project Self-hosted Runner identity, fail-closed preflight, and local durable evidence plus log digests.
- Add regression tests that reject GitHub-hosted compute, GitHub artifact-storage dependency, unpinned checkout, billing dependency, and silent local-agent fallback in the default private execution path.
- Make historical consumer authority immutable: newer framework adoption requires a successor project authority/task instead of rewriting accepted receipts.

## 0.1.1-alpha — 2026-08-23

- Make GitHub Self-hosted Runner the default execution plane for private product repositories.
- Keep GitHub as the control plane for immutable task identity, exact SHA/tree, workflow dispatch, receipts, and evidence.
- Make GitHub-hosted runners non-required for private-repository Parent PM gates unless the Human Owner explicitly opts in.
- Add a fail-closed private runner technical-gate template covering runner identity, exact candidate identity, preflight, product attempt, and receipt emission.
- Add the `github-self-hosted-runner` adapter and retain `generic-local-agent` as the fallback diagnostic executor.

## 0.1.0-alpha — 2026-08-05

- Bootstrap public Parent PM governance core.
- Define remote ChatGPT coding ownership and local execution roles.
- Add exact-SHA deployment, testing, review, and delivery receipts.
- Add starter kit, governance lock, project profile, validator, CI, adapters, and reference project.
- Add related-project landscape research.

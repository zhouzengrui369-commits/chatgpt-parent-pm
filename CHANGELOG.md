# Changelog

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

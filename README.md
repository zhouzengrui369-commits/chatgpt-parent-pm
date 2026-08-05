# ChatGPT Parent PM

[简体中文](README.zh-CN.md)

**An open, repository-native governance framework for AI-assisted software delivery.**

ChatGPT acts as the remote **Parent PM + Coding Agent**. Local agents such as Codex, MiniMax Code, or other computer-capable agents act as **exact-SHA deployment, runtime testing, and acceptance executors**.

> Community project. Not an official OpenAI, Codex, MiniMax, or GitHub project.

## Why this exists

AI coding workflows often mix planning, code ownership, local deployment, testing, and approval inside one long agent session. That creates hidden local state, unverifiable claims, repeated handoffs, and unclear accountability.

This framework separates the delivery system into explicit roles:

| Role | Default executor | Authority |
|---|---|---|
| Remote Parent PM + Coding Agent | ChatGPT with GitHub access | Requirements, goal contracts, source changes, tests, commits, PRs, CI triage, fixes |
| Local Deployment Agent | Codex, MiniMax Code, or another local agent | Checkout an exact SHA, install, build, start, deploy, collect logs |
| Local Test Agent | Codex, MiniMax Code, browser/computer-use agent, or human | Real browser/desktop/device testing, screenshots, annotations, focused retest |
| Owner | Human project owner | Product decisions, sensitive permissions, release, final customer-value acceptance |

GitHub is the single source of truth. Local agents do not own unpublished product source changes.

## Delivery loop

```text
Owner confirms outcome
  -> ChatGPT commits a Goal contract
  -> ChatGPT implements code and tests on GitHub
  -> CI and code gates pass
  -> Candidate SHA is frozen
  -> Local deployment agent deploys that exact SHA
  -> Local test agent performs real-operation acceptance
  -> Findings are recorded against the candidate SHA
  -> ChatGPT fixes and submits a new SHA
  -> Focused redeploy and retest
  -> Owner accepts customer value
  -> Final delivery SHA is frozen
```

## Core invariants

1. **GitHub First** — no product truth exists only in chat or a local worktree.
2. **Exact-SHA handoff** — deploy and test receipts identify the exact commit.
3. **Remote coding ownership** — ChatGPT is the default integration writer.
4. **Local execution separation** — local agents deploy and test; they do not silently become source owners.
5. **Evidence before claims** — code, runtime, product experience, customer value, and delivery identity are separate gates.
6. **No direct main writes** — use branches and pull requests by default.
7. **No automatic merge or release** — owner approval remains explicit.
8. **Fail closed on identity drift** — branch, SHA, dirty state, or scope mismatch returns `BLOCKED`.

## Quick start

```bash
# Copy the starter kit into an existing repository.
cp -R starter-kit/. your-project/

cd your-project
python3 validators/validate_install.py .
```

Then customize:

- `.github/skills/chatgpt-parent-pm/PROJECT_PROFILE.yaml`
- `.github/skills/chatgpt-parent-pm/GOVERNANCE_LOCK.json`
- `PROJECT_STATUS.md`
- the active Goal contract

See [Quick Start](docs/QUICKSTART.md) and [Adoption Guide](docs/ADOPTION_GUIDE.md).

## What v0.1.0-alpha includes

- Parent PM role and authority model
- Goal-driven development contracts
- exact-SHA deployment and test receipts
- project profile and governance lock templates
- repository installation validator
- GitHub Actions governance check
- generic, Codex, and MiniMax Code local-agent adapters
- reference project
- comparative research on related open-source projects

## What it does not do

- run an autonomous agent cloud
- store model credentials
- merge PRs automatically
- deploy production automatically
- replace project-specific architecture or product decisions
- claim that documentation success proves runtime success

## Project status

`v0.1.0-alpha` — bootstrap candidate. The framework should be validated on at least one external project before `v1.0.0`.

## Related work

See [Related Projects Research](research/RELATED_PROJECTS_2026-08-05.md). The closest public projects focus on specification-driven development, local multi-agent orchestration, or autonomous coding runtimes. This repository's narrower contribution is the **remote coding authority / local deployment-and-acceptance separation**, backed by exact-SHA receipts and explicit owner gates.

## License

Apache License 2.0. See [LICENSE](LICENSE).

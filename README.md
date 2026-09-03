# ChatGPT Parent PM — Product Governance

[简体中文](README.zh-CN.md)

A GitHub-native governance framework for separating product authority from engineering implementation in AI-assisted delivery.

Starting with `0.2.0-alpha`:

- **Parent PM / Product Governance** owns Product Baseline, one-Goal/one-Milestone contracts, prioritization, change control, candidate admission, independent review orchestration, release recommendation, and milestone closure. It does not author product source or tests.
- **Engineering Delivery** owns technical design, source, technical tests, code review, commits, pushes, pull requests, CI remediation, exact-SHA candidates, Candidate Manifests, and Technical Receipts. It cannot redefine product meaning or declare product acceptance.
- **Local Execution** deploys an authorized exact SHA, injects local credentials, executes environment-bound tests, and returns sanitized evidence without modifying source/tests.
- **Independent Product Experience Review** operates the real product against the frozen baseline and milestone contract without inspecting code.
- **Human Owner** owns sensitive permissions, major tradeoffs, production authorization, and final Owner Acceptance.

## Invariants

1. One Goal equals one Milestone; they close together.
2. Product Governance and Engineering Delivery use isolated contexts.
3. The same role cannot author and accept the same exact candidate.
4. Technical PASS does not imply Product Experience PASS.
5. Material product changes require an approved Change Request.
6. Only a frozen exact candidate enters independent review or the Human Owner Gate.
7. GitHub is the source of truth.
8. Security is risk-tiered by users, exposure, sensitivity, reversibility, and external authority.

## Delivery loop

```text
Product Baseline
-> Goal/Milestone Contract
-> Engineering Delivery
-> ENGINEERING_READY
-> exact candidate + manifest/receipt
-> Product Governance admission
-> Independent Product Experience Review
-> Human Owner Gate
-> Release Authorization
-> Goal/Milestone Close
```

The bootstrap source for the standalone Engineering Delivery skill is under `engineering-delivery-skill/`. See `docs/ROLE_SEPARATION_MIGRATION.md`.

> Community project. Not an official OpenAI, Codex, GitHub, or other vendor project.

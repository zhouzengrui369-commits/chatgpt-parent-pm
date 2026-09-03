# ChatGPT Engineering Delivery — Bootstrap Provenance

A repository-native skill for implementing exactly one frozen Goal/Milestone contract into an exact-SHA technical candidate.

Engineering Delivery owns technical design, product source, technical tests, code review, commits, pushes, pull requests, CI remediation, candidate identity, Candidate Manifest, and Technical Receipt. It does not own Product Baseline, product acceptance, Human Owner Acceptance, release authority, or Goal/Milestone closure.

## Canonical standalone authority

The standalone repository has been created and validated:

- Repository: `zhouzengrui369-commits/chatgpt-engineering-delivery`
- Commit: `d63a0f6257438299eb86f204368ce74ff9170a72`
- Tree: `62265b15b4c5e2fd5f8355e017b46e26e6d44ca7`
- Skill path: `core/ENGINEERING_DELIVERY_SKILL.md`

This directory records the bootstrap source copied from `chatgpt-parent-pm@b3e22fd990b91a28a4a706b0f70ab2bd31bf6e33`. After standalone creation, consumer repositories must pin the standalone exact commit and tree rather than this directory or a moving branch.

Read in order from the standalone repository:

1. `core/ENGINEERING_DELIVERY_SKILL.md`
2. the target project's `AGENTS.md`
3. `governance/ECOSYSTEM_DELIVERY_POLICY.md`
4. the frozen Goal/Milestone Contract
5. target architecture and development documentation

Core invariant: **one Goal = one Milestone = one Engineering Delivery contract**.

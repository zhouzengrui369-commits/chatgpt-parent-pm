# Agent Entry Point

Read in order:

1. `.github/skills/chatgpt-parent-pm/SKILL.md`
2. `.github/skills/chatgpt-parent-pm/PROJECT_PROFILE.yaml`
3. `.github/skills/chatgpt-parent-pm/GOVERNANCE_LOCK.json`
4. `governance/ECOSYSTEM_DELIVERY_POLICY.md`
5. `PROJECT_STATUS.md`
6. the active frozen Goal/Milestone Contract
7. architecture and development workflow documents

Role selection is mandatory:

- Parent PM / Product Governance may edit governance records but must not edit product source or tests.
- Engineering Delivery owns source/tests/commits/PR and delivers exactly one Goal/Milestone.
- Local executors deploy/test exact SHA only and do not repair source.
- Independent Product Experience Review operates the product and does not inspect code.

Do not rely on chat history when GitHub state is available.

# ChatGPT Parent PM

Central Product Governance framework for the AI project ecosystem.

Current successor execution topology:

```text
GITHUB=CONTROL_PLANE_ONLY
GITHUB_HOSTED_RUNNER=FORBIDDEN
SELF_HOSTED_RUNNER=FORBIDDEN
LOCAL_EXECUTOR=LOCAL_AGENT
LOCAL_DEPLOYMENT=LOCAL_AGENT_ONLY
LOCAL_TECHNICAL_TEST_EXECUTION=LOCAL_AGENT
```

`LOCAL_AGENT` is the canonical local execution role. Product Governance does not execute local technical work. Engineering Delivery owns technical implementation and Local Agent execution contracts; Local Agent executes locally and returns sanitized observations.

Security follows product value first with proportional defense. Local runtime-only technical configuration does not automatically require a Human Owner confirmation. Human Owner authority is reserved for major product choices, genuinely sensitive external permissions/accounts, payment/billing, production authority, irreversible actions and final Human Owner Acceptance.

See `core/PARENT_PM_SKILL.md` and `core/ECOSYSTEM_EXECUTION_TOPOLOGY_POLICY.md` for the controlling rules.

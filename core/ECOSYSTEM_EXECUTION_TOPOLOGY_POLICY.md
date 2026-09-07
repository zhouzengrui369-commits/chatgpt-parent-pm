# Ecosystem Execution Topology Policy — Local Agent Only

Status: OWNER-AUTHORIZED SUCCESSOR POLICY
Protocol: `DELIVERY-LIFECYCLE-1.0`

## Governing decision

The AI project ecosystem uses GitHub as the durable control plane and **does not use any Runner as a project execution surface**.

```text
GITHUB=CONTROL_PLANE_ONLY
GITHUB_HOSTED_RUNNER=FORBIDDEN
SELF_HOSTED_RUNNER=FORBIDDEN
ANY_GITHUB_ACTIONS_RUNNER_AS_PROJECT_EXECUTOR=FORBIDDEN
LOCAL_EXECUTOR=OWNER_AUTHORIZED_LOCAL_AGENT
LOCAL_DEPLOYMENT=OWNER_AUTHORIZED_LOCAL_AGENT_ONLY
LOCAL_TECHNICAL_TEST_EXECUTION=OWNER_AUTHORIZED_LOCAL_AGENT
SILENT_FALLBACK=FORBIDDEN
```

This is an ecosystem-level Human Owner execution-topology decision. It supersedes any prospective framework/project clause that treats GitHub-hosted Runner or self-hosted Runner as an allowed CI, deployment, runtime, browser, or local-execution substitute.

Historical Runner receipts remain immutable evidence for their original context but have no prospective execution authority.

## Role boundary

### Product Governance

Product Governance defines the Goal/Milestone contract, technical evidence outcomes and evidence ownership. It does not run local commands or mutate product source/tests/workflows.

### Engineering Delivery

Engineering Delivery owns technical design, source/tests, commit/push/PR, technical remediation, exact candidate identity, Candidate Manifest and Technical Receipt. Where an `engineering_required` gate requires execution, Engineering Delivery issues a bounded Local Agent execution contract and adjudicates the returned sanitized observation.

Engineering Delivery must not require GitHub-hosted or self-hosted Runner execution as a prerequisite unless a future explicit Human Owner successor policy changes this rule.

### Local Agent

The Owner-authorized Local Agent is the ecosystem execution surface for:

- exact-SHA materialization;
- dependency installation;
- local build and technical test execution;
- local runtime start/deployment;
- real-device/data/browser checks when contracted;
- local credential injection through Owner-authorized mechanisms;
- sanitized observation receipts.

The Local Agent remains observation/execution only. It must not modify source/tests, commit/push, self-repair, expand scope, declare `ENGINEERING_READY`, admit a candidate, issue Product Experience, grant Human Owner Acceptance, merge or release.

## CI semantics

`CI` means the contracted repeatable technical gate set, not specifically GitHub Actions.

For ecosystem projects under this policy:

```text
REQUIRED_TECHNICAL_GATE_EXECUTOR=OWNER_AUTHORIZED_LOCAL_AGENT
GITHUB_ACTIONS_SUCCESS=NOT_A_UNIVERSAL_REQUIRED_GATE
RUNNER_MINUTES_OR_BILLING=NOT_A_PRODUCT_OR_ENGINEERING_PREREQUISITE
```

A project contract may require exact command suites, test coverage, build identity, logs and receipts. Those requirements remain binding. Only the execution surface changes from Runner-based execution to Local-Agent execution.

GitHub may store contracts, commits, PRs, issues, checks metadata and sanitized receipts. GitHub is not the execution plane.

## Deployment semantics

All local development/review deployment is executed by the Owner-authorized Local Agent from an authorized exact SHA. Product Governance/Engineering may specify the expected identity and acceptance commands; the Local Agent performs the deployment and returns a receipt.

Production deployment remains separately governed by each project contract and Human Owner production authority. This policy does not grant production release authority.

## Change control

Any project contract, governance lock, profile, workflow expectation or Engineering handoff that requires a Runner must be prospectively reconciled with this policy.

If changing the execution surface changes a frozen Goal/Milestone evidence requirement, Product Governance must issue a Change Request and successor contract. Technical workflow/script cleanup belongs to a separate Engineering Delivery context.

## Security proportionality

This topology supports `PRODUCT_VALUE_FIRST_WITH_PROPORTIONATE_DEFENSE`: protected secrets remain local, GitHub stores no Owner credentials, and core product validation is not blocked by hosted-runner billing or unrelated enterprise infrastructure.

FORBIDDEN_CLAIMS_ACKNOWLEDGED=YES

# Ecosystem Execution Topology Policy — Local Agent Only

Status: HUMAN-OWNER SUCCESSOR POLICY
Protocol: `DELIVERY-LIFECYCLE-1.0`

## Governing decision

The AI project ecosystem uses GitHub as the durable control plane and **does not use any Runner as a project execution surface**.

```text
GITHUB=CONTROL_PLANE_ONLY
GITHUB_HOSTED_RUNNER=FORBIDDEN
SELF_HOSTED_RUNNER=FORBIDDEN
ANY_GITHUB_ACTIONS_RUNNER_AS_PROJECT_EXECUTOR=FORBIDDEN
LOCAL_EXECUTOR=LOCAL_AGENT
LOCAL_DEPLOYMENT=LOCAL_AGENT_ONLY
LOCAL_TECHNICAL_TEST_EXECUTION=LOCAL_AGENT
SILENT_FALLBACK=FORBIDDEN
```

`LOCAL_AGENT` is a project execution role. There is no separate `OWNER_AUTHORIZED_LOCAL_AGENT` lifecycle role. Historical records using that phrase remain immutable historical evidence, but the phrase has no prospective role-model authority.

This is an ecosystem-level execution-topology decision. It supersedes any prospective framework/project clause that treats GitHub-hosted Runner or self-hosted Runner as an allowed CI, deployment, runtime, browser, or local-execution substitute.

Historical Runner receipts remain immutable evidence for their original context but have no prospective execution authority.

## Role boundary

### Product Governance

Product Governance defines the Goal/Milestone contract, product baseline, acceptance outcomes, evidence requirements and evidence ownership. It does not run local commands or mutate product source/tests/workflows.

### Engineering Delivery

Engineering Delivery owns technical design, source/tests, commit/push/PR, technical remediation, exact candidate identity, Candidate Manifest and Technical Receipt. Where an `engineering_required` or review-preparation gate requires execution, Engineering Delivery issues a bounded Local Agent execution contract and adjudicates the returned sanitized observation.

Engineering Delivery must not require GitHub-hosted or self-hosted Runner execution as a prerequisite unless a future explicit Human Owner successor policy changes this rule.

### Local Agent

The Local Agent is the ecosystem execution surface for:

- exact-SHA materialization;
- dependency installation;
- local build and technical test execution;
- local runtime start/deployment;
- real-device/data/browser checks when contracted;
- local runtime configuration and local credential injection/generation when required by an Engineering Delivery contract;
- sanitized observation receipts.

The Local Agent remains execution/observation only. It must not modify source/tests, commit/push, self-repair, expand scope, declare `ENGINEERING_READY`, admit a candidate, issue Product Experience, grant Human Owner Acceptance, merge or release.

## Runtime credential proportionality

Security follows `PRODUCT_VALUE_FIRST_WITH_PROPORTIONATE_DEFENSE`.

A local runtime-only technical secret that is generated on the local machine solely to satisfy the admitted candidate's runtime configuration (for example a random non-default JWT signing secret) is **technical runtime configuration**, not a separate Human Owner approval gate, provided it:

- does not grant access to an external account or provider;
- does not authorize payment, purchase, production release or irreversible action;
- is generated/stored locally under the Engineering Delivery contract;
- is never printed, exported, committed, uploaded to GitHub or returned in a receipt.

Engineering Delivery may specify the required technical properties; Local Agent may generate/store the local value and report only non-secret status/evidence.

Human Owner authority remains required for genuinely sensitive authority changes such as:

- external account/provider authorization or new external credential access;
- payment, billing or purchasing decisions;
- production credentials or production release/deployment authorization;
- destructive/irreversible operations;
- final Human Owner Acceptance and major product trade-offs.

Do not elevate ordinary local runtime configuration into a Human Owner confirmation gate merely because it contains a secret value.

## CI semantics

`CI` means the contracted repeatable technical gate set, not specifically GitHub Actions.

For ecosystem projects under this policy:

```text
REQUIRED_TECHNICAL_GATE_EXECUTOR=LOCAL_AGENT
GITHUB_ACTIONS_SUCCESS=NOT_A_UNIVERSAL_REQUIRED_GATE
RUNNER_MINUTES_OR_BILLING=NOT_A_PRODUCT_OR_ENGINEERING_PREREQUISITE
```

A project contract may require exact command suites, test coverage, build identity, logs and receipts. Those requirements remain binding. Only the execution surface changes from Runner-based execution to Local-Agent execution.

GitHub may store contracts, commits, PRs, issues, checks metadata and sanitized receipts. GitHub is not the execution plane.

## Deployment semantics

All local development/review deployment is executed by the Local Agent from the exact SHA specified by Engineering Delivery. Product Governance defines required outcomes; Engineering Delivery owns local execution mechanics and contract; Local Agent performs deployment and returns a receipt.

Production deployment remains separately governed by each project contract and Human Owner production authority. This policy does not grant production release authority.

## Change control

Any project contract, governance lock, profile, workflow expectation or Engineering handoff that requires a Runner must be prospectively reconciled with this policy.

If changing the execution surface changes a frozen Goal/Milestone evidence requirement, Product Governance must issue a Change Request and successor contract. Technical workflow/script cleanup belongs to a separate Engineering Delivery context.

A terminology/role-boundary correction from `OWNER_AUTHORIZED_LOCAL_AGENT` to the canonical `LOCAL_AGENT`, without changing product scope, evidence ownership, acceptance thresholds or technical gates, is a governance role-model correction and does not by itself invalidate an admitted candidate.

## Security proportionality

This topology protects actual secrets while keeping them local. Core product validation must not be blocked by hosted-runner billing, redundant Owner confirmations, or unrelated enterprise controls. Security strength scales with user count, exposure, data sensitivity, reversibility and automation authority.

FORBIDDEN_CLAIMS_ACKNOWLEDGED=YES

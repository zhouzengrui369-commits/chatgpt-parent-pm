# Separated Product Delivery Loop

Protocol: `DELIVERY-LIFECYCLE-1.0`

## Ecosystem execution topology

The ecosystem-wide execution policy is `core/ECOSYSTEM_EXECUTION_TOPOLOGY_POLICY.md`.

```text
GITHUB=CONTROL_PLANE_ONLY
GITHUB_HOSTED_RUNNER=FORBIDDEN
SELF_HOSTED_RUNNER=FORBIDDEN
LOCAL_EXECUTOR=OWNER_AUTHORIZED_LOCAL_AGENT
LOCAL_DEPLOYMENT=OWNER_AUTHORIZED_LOCAL_AGENT_ONLY
LOCAL_TECHNICAL_TEST_EXECUTION=OWNER_AUTHORIZED_LOCAL_AGENT
```

GitHub stores durable control-plane state: contracts, commits, PRs, Issues and sanitized receipts. It is not the execution plane. Runner availability, Runner minutes and GitHub Actions billing are not universal delivery prerequisites.

## A — Product Baseline

Product Governance freezes product positioning, target user, problem, value, boundary and risk tier.

## B — Goal/Milestone Contract

Product Governance selects exactly one Goal and one Milestone, freezes the product contract, and classifies every required evidence item as:

```text
engineering_required
admission_required
review_required
product_experience
human_owner
```

Unclassified evidence blocks handoff.

## C — Engineering Delivery

A separate Engineering Delivery context implements source/tests, manages the engineering branch/PR, obtains all engineering-required evidence, freezes one exact candidate, emits Candidate Manifest and Technical Receipt, and returns one terminal state.

When technical execution is required, Engineering Delivery issues a bounded Local Agent execution contract. The Owner-authorized Local Agent materializes the exact SHA, installs dependencies, runs the contracted build/test/runtime/browser steps, and returns sanitized observations. Engineering Delivery adjudicates those observations.

`CI` means the repeatable contracted technical gate set; it does not require GitHub Actions. No GitHub-hosted or self-hosted Runner may be substituted for the Local Agent.

`ENGINEERING_READY` is atomic. Engineering Delivery stops after handback.

## D — Candidate Admission

Product Governance receives the immutable package. It verifies identity, contract coverage, admission evidence, Change Requests, defects/limitations and independence without modifying the candidate.

Outcome:

```text
CANDIDATE_ADMITTED
CANDIDATE_REJECTED
CANDIDATE_ADMISSION_BLOCKED
```

## E — Product Review eligibility

Only after admission, Product Governance separately verifies review runtime/artifact identity, review evidence and reviewer independence, then creates the exact Product Review referral.

Outcome:

```text
PRODUCT_REVIEW_ELIGIBLE
PRODUCT_REVIEW_NOT_ELIGIBLE
PRODUCT_REVIEW_ELIGIBILITY_BLOCKED
```

## F — Independent Product Experience

An independent, code-blind reviewer operates the exact product and issues Product Experience findings/verdict. It does not repair the candidate.

## G — Remediation

Product Governance reconciles the verdict. Any source/test change returns to a separate Engineering Delivery context under the same frozen Goal or an approved Change Request. Candidate identity change invalidates all downstream states.

## H — Human Owner and closure

The Human Owner grants any required final acceptance/sensitive authority. The contract-defined release authority acts separately. Product Governance closes Goal and Milestone together only when every required gate is closed.

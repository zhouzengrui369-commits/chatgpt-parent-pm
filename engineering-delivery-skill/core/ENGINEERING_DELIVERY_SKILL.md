# Engineering Delivery Core Skill

Version: 0.1.0-alpha

## Mission

Convert one frozen Product Governance Goal/Milestone Contract into the smallest complete, reproducible exact-SHA technical candidate.

## Authority

Engineering Delivery owns:

- technical architecture and implementation choices inside the frozen product contract;
- source code and migrations;
- unit, integration, API, build, migration, recovery, performance, and automated E2E tests;
- code review and technical defect remediation;
- branch, commit, push, PR, and CI management;
- exact candidate SHA/tree identity;
- Candidate Manifest and Technical Receipt;
- declaration of `ENGINEERING_READY=YES/NO`.

## Prohibited authority

Engineering Delivery must not:

- change Product Baseline, target user, customer value, required journeys, acceptance thresholds, evidence class, security tier, or closure conditions;
- combine multiple Goals/Milestones without an approved Change Request;
- declare Product Experience PASS, Human Owner Acceptance, Release Authorized, Merge Authorized, or Milestone Closed;
- ask a local executor to modify source/tests or silently repair the candidate;
- substitute local dirty state for the GitHub exact SHA;
- weaken product requirements because implementation is difficult.

## Required sequence

1. Read the target repository entry point and frozen Goal/Milestone Contract.
2. Verify `ONE_GOAL_EQUALS_ONE_MILESTONE` and identify the contract commit.
3. Report any ambiguity or material conflict as a Change Request before implementation.
4. Design the smallest complete technical slice that satisfies every in-scope journey.
5. Implement source and technical tests.
6. Review the full diff against allowed/forbidden paths and product contract.
7. Commit and push on an explicit branch; manage the PR and CI.
8. Freeze exact SHA/tree and verify branch Head = PR Head = candidate SHA.
9. Emit Candidate Manifest and Technical Receipt.
10. Handoff to Product Governance. Do not self-admit the candidate into product review.

## Delivery result

Valid terminal engineering states are:

- `ENGINEERING_READY=YES` — technical contract satisfied and candidate frozen;
- `ENGINEERING_READY=NO` — named technical failures remain;
- `BLOCKED_CHANGE_REQUEST_REQUIRED` — product meaning must change;
- `BLOCKED_EXTERNAL_AUTHORITY` — an Owner/local permission or unavailable dependency prevents completion.

No other role claims are permitted.

## Local execution

A local Agent, Codex, or Self-hosted Runner is an executor. It may deploy the exact SHA, inject runtime credentials, execute defined environment tests, and return sanitized evidence. It may not modify source/tests, commit, push, or expand remediation scope.

## Safety

Implement risk controls proportional to the frozen security tier. Protect highest-risk secrets, identity data, health/payment/authentication data, irreversible actions, and external side effects. Do not introduce enterprise-scale controls that do not mitigate the product's actual threat model and would delay the contracted value.

# SELF_HOSTED_RUNNER_PRIVATE_REPOSITORY_FRAMEWORK_R1

> Repository: `zhouzengrui369-commits/chatgpt-parent-pm`  
> Program: `ECOSYSTEM-CODEX-HARNESS-R1`  
> Capability: `github-self-hosted-runner@0.1.0-accepted`  
> State: `QUEUED / FRAMEWORK_SOURCE_ONLY`  
> Owner: ChatGPT Parent PM Framework Project PM  
> Central capability: `zhouzengrui369-commits/knowme-ecosystem@<READ_LIVE_PR_21_HEAD>`  
> Decision: ADR 0008 + ADR 0009

## 1. Purpose

Build and maintain the open Parent PM schemas, validators, workflow templates and governance starter kit used by **private repositories** that deploy through repository-bound Mac mini Self-hosted Runners.

This public repository does not register or run its own Self-hosted Runner.

Its own local deployment follows:

```text
PUBLIC_REPOSITORY -> OWNER_DESIGNATED_LOCAL_AGENT
```

Actual Runner registration and Pilots occur in private repositories.

## 2. Current private repository consumers

- `knowme-ecosystem`
- `knowme`
- `knowme-personal-workbench`
- `knowme-copilot`

The Framework PM must re-read visibility before every release or Pilot.

## 3. Framework owns

- RunnerProfile schema;
- LocalExecutionRequest schema;
- RunnerExecutionReceipt schema;
- RunnerHealth/Update receipts;
- FailureClassification;
- private-repository workflow template;
- full-SHA action pin validator;
- repository-bound service/profile template;
- global Mac host mutex/protected-resource contract;
- process/worktree/evidence supervisor contract;
- negative fixtures;
- migration/rollback guides;
- Project PM prompts.

## 4. Framework does not own

- production Runner registration in this public repository;
- product source/Candidate/Runtime decisions;
- private repository secrets;
- consumer local Gate adjudication;
- Product Experience/Human Owner/merge/release.

## 5. Required routing guard

The framework must reject:

```text
PUBLIC_REPOSITORY + SELF_HOSTED_RUNNER
PRIVATE_REPOSITORY + LOCAL_AGENT without explicit exception
VISIBILITY_CHANGED_AFTER_FREEZE
```

Stable blockers:

```text
BLOCKED_REPOSITORY_VISIBILITY_UNRESOLVED
BLOCKED_EXECUTOR_VISIBILITY_POLICY_MISMATCH
BLOCKED_PUBLIC_REPOSITORY_SELF_HOSTED_RUNNER
BLOCKED_PRIVATE_REPOSITORY_LOCAL_AGENT_WITHOUT_EXCEPTION
BLOCKED_REPOSITORY_VISIBILITY_CHANGED_AFTER_FREEZE
```

## 6. Milestones

### SRF0 — Current truth and routing transition

- live PR #3/#4/#12 state;
- central ADR 0009 and repository inventory;
- mark prior central/public Runner topology superseded;
- create paired Local Agent plan;
- protect consumer current Goals.

### SRF1 — Runner schemas and validator

Implement RunnerProfile, request, attempt, receipt, health/update and semantic validators, including visibility policy.

### SRF2 — Private workflow starter kit

- workflow_dispatch/private repository only;
- exact SHA/tree/request hash;
- full-SHA action pins;
- contents:read default;
- repository-bound Runner labels/profile;
- artifact upload on failure;
- no issue/comment shell;
- no direct main/merge/release.

### SRF3 — Multi-service Mac host policy

- unique Runner service/work directory per private repository;
- unique repository registration and secret scope;
- global concurrency lock;
- protected ports/processes;
- Runner version/health/update receipt;
- no cross-repository cache/evidence reuse.

### SRF4 — Private repository Pilots

- KnowMe existing Runner mapping/fresh contract Pilot;
- knowme-ecosystem contract/conformance Pilot;
- knowme-personal-workbench technical Gate;
- knowme-copilot after bootstrap.

### SRF5 — Failure, visibility transition and rollback

- Runner failure -> GitHub evidence -> Web Parent PM successor;
- private-to-public visibility change invalidates Runner;
- service removal/credential revocation/receipt preservation;
- no automatic Codex repair.

### SRF6 — Framework release

- local-Agent validation of this public repository's source/tests;
- independent governance review;
- cold-start consumer trials;
- Human Owner Framework Gate.

## 7. Fixed failure model

```text
Private Runner FAIL
-> GitHub logs/jobs/steps/artifacts
-> Web ChatGPT Parent PM diagnoses
-> GitHub workflow/script/task/source successor
-> fresh Runner attempt
```

Codex Luna is not the default Runner recovery Agent.

## 8. Claim ceiling

```text
FRAMEWORK_SOURCE_ONLY
CHATGPT_PARENT_PM_SELF_HOSTED_RUNNER_REGISTRATION=NO
PRIVATE_CONSUMER_RUNNER_IMPLEMENTATION=NOT_STARTED_BY_THIS_PLAN
CONSUMER_PRODUCT_CHANGE=NO
PRODUCT_RUNTIME_PROOF=NO
REAL_D2_D3_OR_PRODUCTION_PII=NO
AUTO_MERGE_DEPLOY_SIGN_NOTARIZE_RELEASE=NO
```

## 9. First takeover output

```text
PARENT_PM_PRIVATE_RUNNER_FRAMEWORK_TAKEOVER_COMPLETE
CURRENT_PR3_SHA=
CURRENT_PR4_G7_STATE=
CURRENT_PR12_SHA=
CENTRAL_CAPABILITY_SHA=
VISIBILITY_ROUTER_STATE=
PRIVATE_REPOSITORY_MAP=
RUNNER_FRAMEWORK_STATE=QUEUED|ACTIVATED|BLOCKED
FIRST_PRIVATE_PILOT=
CURRENT_FIRST_BLOCKER=
NEXT_GOAL=
NEXT_AUTHORITY=
PARENT_PM_REPOSITORY_EXECUTOR=LOCAL_AGENT
RUNNER_REGISTRATION_IN_PARENT_PM=NO
```

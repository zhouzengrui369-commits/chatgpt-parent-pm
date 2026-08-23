# SELF_HOSTED_RUNNER_PRIVATE_REPOSITORY_FRAMEWORK_R1

> Repository: `zhouzengrui369-commits/chatgpt-parent-pm`
> Program: `ECOSYSTEM-CODEX-HARNESS-R1`
> Capability: `github-self-hosted-runner@0.1.0-accepted`
> State: `SRF1_SRF3_SOURCE_PASS_PENDING_CONSUMER_PILOT`
> Owner: ChatGPT Parent PM Framework Project PM
> Decision: ADR 0008 + ADR 0009

## 1. Current accepted source pin

```text
FRAMEWORK_SOURCE_SHA=676fb82b614ec4d94a4889a372f0b474d902aa8b
FRAMEWORK_CI_RUN=32546264415
FRAMEWORK_CI=PASS
PRIVATE_RUNNER_FRAMEWORK_CI_RUN=32546264436
PRIVATE_RUNNER_FRAMEWORK_CI=PASS
```

This document change follows that accepted source pin and does not replace it for consumer contracts. A consumer must explicitly pin `676fb82b614ec4d94a4889a372f0b474d902aa8b` until Parent PM publishes and revalidates a later framework source.

## 2. Boundary

This public repository provides open contracts and starter tooling for **private consumer repositories**. It does not register or operate a production Self-hosted Runner for itself.

```text
PRIVATE_REPOSITORY -> MAC_MINI_SELF_HOSTED_RUNNER
PUBLIC_REPOSITORY  -> OWNER_DESIGNATED_LOCAL_AGENT
```

## 3. SRF1 — contracts and semantic validator: PASS source gate

Implemented and CI-validated on the accepted pin:

- `schemas/runner-profile.schema.json`;
- `schemas/local-execution-request.schema.json`;
- `schemas/runner-attempt.schema.json`;
- `schemas/runner-execution-receipt.schema.json`;
- `schemas/runner-health-receipt.schema.json`;
- `schemas/runner-update-receipt.schema.json`;
- `validators/validate_private_runner.py`;
- deterministic positive/negative `unittest` coverage.

The semantic validator fails closed on visibility/executor mismatch, non-repository registration scope, missing repository label, non-unique service/work roots, non-repository secret scope, D2/D3/raw-PII defaults, Local Agent fallback, source/local repair, prohibited writes, predecessor reuse, broad process kill, invalid profile/request/receipt binding, `strongest`, and PASS receipts with prohibited mutations.

## 4. SRF2 — private workflow starter kit: PASS source gate

`starter-kit/private-runner/private-runner-technical-gate.yml.template` requires:

- `workflow_dispatch` control;
- `contents: read` default permission;
- full-SHA action pins;
- exact candidate SHA/tree proof;
- repository-specific self-hosted labels;
- validated tracked request/profile;
- exact task script under `work/tasks/`;
- sanitized evidence artifact upload on terminal outcomes;
- no issue/comment shell, direct main write, merge, cloud deploy or release authority.

## 5. SRF3 — multi-service Mac host policy: PASS source gate

```text
REGISTRATION_SCOPE=repository
UNIQUE_RUNNER_SERVICE=YES
UNIQUE_WORK_DIR=YES
UNIQUE_TASK_ROOT=YES
UNIQUE_EVIDENCE_ROOT=YES
REPOSITORY_SPECIFIC_SECRETS=YES
MAX_LOCAL_CONCURRENCY=1
GLOBAL_MAC_MUTEX=YES
STALE_LOCK=AUTO_DELETE_FORBIDDEN
PROTECTED_RESOURCE_REGISTRY=REQUIRED
```

`host_mutex.sh` writes a run/repository ownership token and will not delete a busy/stale lock. `runner_health.sh` creates only sanitized service/platform/version/path/label evidence. `runner_update.sh` records version/update state without secrets or product data.

## 6. Fixed data/write/process policy

```text
DATA=D0_SYNTHETIC_OR_D1_SANITIZED
RAW_PRODUCTION_PII=NO
D2_DEFAULT_ACCESS=NO
D3_ACCESS=NO
NETWORK=DENY_BY_DEFAULT_OR_EXACT_ALLOWLIST
SOURCE_MUTATION_DURING_DEPLOYMENT=NO
LOCAL_REPAIR=NO
OWNER_SOURCE_WRITE=NO
MANUAL_STATUS_OVERRIDE=NO
PRODUCTION_DB_WRITE=NO
CLOUD_WRITE=NO
PREDECESSOR_REUSE=NO
BROAD_PROCESS_KILL=NO
RUNNER_AUTO_REPAIR_BY_CODEX=NO
AUTO_MERGE_DEPLOY_RELEASE=NO
```

## 7. Codex profile

```text
ENGINEERING_OR_SRE=Luna/xhigh
PRODUCT_EXPERIENCE=Sol/xhigh
SILENT_FALLBACK=NO
strongest=FORBIDDEN_AS_CONTRACT_VALUE
```

Harness authority must remain a subset of the outer Runner request.

## 8. Failure model

```text
Runner FAIL
-> GitHub Actions logs/jobs/steps/artifacts
-> Web ChatGPT Parent PM classifies FIRST_BLOCKER
-> GitHub source/workflow/script/task successor
-> NEW_ATTEMPT_ID + fresh worktree/release/task/evidence/runtime
```

Failure classifications:

```text
TASK_CONTRACT_DEFECT
SOURCE_DEFECT
WORKFLOW_DEFECT
RUNNER_DEFECT
TOOLCHAIN_DEFECT
DATA_POLICY_DEFECT
PII_DEFECT
IMPORT_FIDELITY_DEFECT
RUNTIME_DEFECT
EVIDENCE_INCOMPLETE
```

## 9. Evidence boundary / next milestone

Framework source PASS does **not** prove any consumer Runner is registered, online, healthy or authorized for product data. The next milestone is SRF4 private consumer health Pilot. A private consumer must pin the accepted framework SHA, create and validate a repository-specific RunnerProfile, register a repository-scoped service, produce fresh health/update receipts, then execute a fresh exact-SHA task.

## 10. Claim ceiling

```text
FRAMEWORK_SRF1_SRF3_SOURCE_GATE=PASS
CONSUMER_RUNNER_REGISTRATION=NOT_PROVEN_BY_FRAMEWORK
CONSUMER_RUNNER_HEALTH=NOT_PROVEN_BY_FRAMEWORK
CHATGPT_PARENT_PM_SELF_HOSTED_RUNNER_REGISTRATION=NO
CONSUMER_PRODUCT_CHANGE=NO
REAL_D2_D3_OR_PRODUCTION_PII=NO
AUTO_MERGE_DEPLOY_SIGN_NOTARIZE_RELEASE=NO
```

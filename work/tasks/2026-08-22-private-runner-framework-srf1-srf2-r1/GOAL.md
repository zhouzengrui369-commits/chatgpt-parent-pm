# GOAL — Private Runner Framework SRF1/SRF2 R1

```text
PROGRAM_ID=ECOSYSTEM-CODEX-HARNESS-R1
FRAMEWORK_REPOSITORY=zhouzengrui369-commits/chatgpt-parent-pm
FRAMEWORK_REPOSITORY_VISIBILITY=public
FRAMEWORK_BASE_SHA=a6968f771ab0274f042142d100ec446c0f641cf4
CENTRAL_CAPABILITY_PR=zhouzengrui369-commits/knowme-ecosystem#21
CENTRAL_CAPABILITY_SHA=193acc0cd2437393f25641eba92085d75fffb063
ADR_0008=ACCEPTED
ADR_0009=ACCEPTED
CONSUMER_BLOCKER=zhouzengrui369-commits/lingxi-presentation#90
CONSUMER_ACTIVATION_PR=zhouzengrui369-commits/lingxi-presentation#94
GOAL_CLASS=FRAMEWORK_SOURCE_ONLY
PARENT_PM_SELF_HOSTED_RUNNER_REGISTRATION=NO
CONSUMER_PRODUCT_MUTATION=NO
MERGE_RELEASE_AUTHORIZED=NO
```

## Goal

Implement the minimum reusable private-repository Self-hosted Runner framework required to let consumer Project PMs create deterministic repository-bound Runner activation records without inventing local schemas or fabricating receipts.

## SRF1 — Schemas and semantic validator

Implement versioned public-safe contracts for:

- RepositoryVisibilityReceipt;
- RunnerProfile;
- LocalExecutionRequest;
- ExecutionAttempt;
- RunnerHealthReceipt;
- RunnerUpdateReceipt;
- RunnerExecutionReceipt;
- ProtectedResourceRegistry;
- MaterialManifest.

The validator must fail closed on visibility/executor mismatch, repository/profile mismatch, missing repo-bound service/workdir/secret scope, concurrency/mutex violations, source/request identity mismatch, source mutation/local repair/push/merge/provider authority, wildcard network authority, predecessor reuse, broad process killing, stale/unhealthy Runner receipts, nonterminal process/port evidence and claim escalation.

## SRF2 — Private workflow starter kit

Implement a reusable private-repository workflow template that is safe by construction:

- `workflow_dispatch` only;
- repository-bound runner labels;
- exact source SHA/tree/request/profile inputs;
- `contents: read` default GitHub token permission;
- full-SHA-pinned third-party actions;
- no issue/comment text as shell;
- no direct main write/merge/tag/release;
- validate authority before local commands;
- preserve logs/evidence and fail closed.

The template is framework source only. This public repository does not register or execute a Self-hosted Runner.

## Consumer requirement frozen by Lingxi

Lingxi is currently private and blocked before its first Fix19 Runner attempt. The framework must be usable for a repository-bound profile with:

```text
registration_scope=repository
repository=zhouzengrui369-commits/lingxi-presentation
max_concurrent_local_execution=1
global_mac_mutex_required=true
source_mutation=false
local_repair=false
push=false
merge=false
provider_change=false
predecessor_reuse=false
network_default=deny
broad_process_kill=false
```

No private paths, tokens, fixture bytes or product source are copied into this public framework repository.

## Acceptance

Remote framework code Gate must prove:

1. every schema JSON parses;
2. positive private-runner fixture validates;
3. negative fixtures return stable expected blockers;
4. unit tests pass;
5. Python compile pass;
6. workflow starter kit uses only full-SHA action pins and `contents: read`;
7. workflow has no public PR/fork/comment trigger;
8. no consumer product source changes;
9. no Self-hosted Runner registration in `chatgpt-parent-pm`.

## Claim ceiling

```text
SRF1_SOURCE_IMPLEMENTATION_ONLY
SRF2_SOURCE_IMPLEMENTATION_ONLY
PRIVATE_CONSUMER_RUNNER_REGISTRATION=NOT_PROVEN
RUNNER_HEALTH=NOT_PROVEN
CONSUMER_RUNTIME=NOT_PROVEN
PRODUCT_EXPERIENCE_PASS=NO
HUMAN_OWNER_FRAMEWORK_GATE=NOT_YET
AUTO_MERGE_DEPLOY_SIGN_NOTARIZE_RELEASE=NO
```

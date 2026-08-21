# SELF_HOSTED_RUNNER_LOCAL_EXECUTION_PLANE_R1

> Repository: `zhouzengrui369-commits/chatgpt-parent-pm`  
> Program: `ECOSYSTEM-CODEX-HARNESS-R1`  
> Capability: `github-self-hosted-runner@0.1.0-proposed`  
> State: `QUEUED / PLANNING_ONLY`  
> Owner: ChatGPT Parent PM Framework Project PM  
> Central capability: `zhouzengrui369-commits/knowme-ecosystem@fd01ef7619a31b7ffca5dd2205a2e31a96fac834`  
> Central PR: `knowme-ecosystem#21`  
> Central tracker: `knowme-ecosystem#23`

## 1. Goal

Build the ecosystem's unique GitHub Self-hosted Runner Local Execution Plane:

```text
Product Parent PM exact-SHA request
→ Parent PM secure dispatcher
→ GitHub Self-hosted Runner / Owner Mac mini
→ fresh worktree/task/evidence roots
→ authorized local build/Runtime/evidence
→ ExecutionReceipt
→ Product Parent PM adjudication
```

The control plane may invoke Codex Harness as an optional worker, but Runner and Harness remain separate versioned capabilities.

## 2. Current protected framework lane

The Framework PM must read live GitHub truth before activation.

Protected at plan creation:

```text
SHARED_CAPABILITY_ADOPTION_PR=3
ECOSYSTEM_V03_RC_PR=4
PR4_G0_G6=PASS
PR4_G7=PENDING_OR_BLOCKED_READ_LIVE
CODEX_HARNESS_GATEWAY_PR=12
CODEX_HARNESS_GATEWAY_STATE=QUEUED
CONSUMER_PRODUCT_CHANGE=NO
```

No current PR #3/#4/#12 evidence may be overwritten or relabelled.

## 3. Security topology Gate

`chatgpt-parent-pm` is public. This plan does not change repository visibility.

Before production Runner registration, the Framework PM must record one exact topology:

```text
PRIVATE_PARENT_PM_EXECUTION_CONTROL_REPOSITORY
ORGANIZATION_RESTRICTED_RUNNER_GROUP
HUMAN_OWNER_PUBLIC_CONTROL_REPOSITORY_EXCEPTION
```

Until then:

```text
LOCAL_EXECUTION_PLANE_STATE=BLOCKED_RUNNER_CONTROL_REPOSITORY_NOT_SECURE
RUNNER_REGISTRATION_AUTHORIZED=NO
```

A public exception must prove no PR/fork execution, full-SHA action pins, read-only defaults, source validation before secret injection and explicit Human Owner acceptance.

## 4. Reference architecture ownership

This repository owns:

- RunnerProfile schema and registry;
- LocalExecutionRequest schema;
- ExecutionAttempt and ExecutionReceipt schemas;
- RunnerHealthReceipt and update receipt;
- FailureClassification schema;
- secure dispatch workflow;
- least-privilege cross-repository auth;
- local execution supervisor;
- process/port/worktree/cache policy;
- redaction and artifact manifest;
- product adapter starter kit;
- health/update monitoring;
- failure recovery and rollback guide;
- framework release and conformance.

This repository does not own product source, product Candidate, product Runtime verdict, Product Experience verdict, merge or release.

## 5. Existing KnowMe pilot

KnowMe PR #15 is the first repository-bound Runner implementation and current proof source.

At plan creation its live PR body reported:

```text
PRODUCT_PR=10
PRODUCT_SHA=bb9c095a2031ed918245c34a3d88667221c5e92d
RUNNER_LABELS=self-hosted,macOS,ARM64,knowme-local-runtime
RUNTIME_GATE_VERSION=v3
RUNTIME_GATE_RUN=32488557543
RUNTIME_GATE_JOB=96790658376
RUNTIME_GATE=PASS
RUNTIME_URL=http://127.0.0.1:38905
```

The Framework PM must fetch PR #15 live at activation. These values are discovery anchors, not moving authority.

PR #15 remains protected predecessor/reference evidence. Its runner name, local paths and process details must not be copied into public central receipts beyond sanitized logical IDs/hashes.

## 6. Milestones

## SR0 — Current truth and activation

Deliver:

- live PR #3/#4/#12 state;
- live central PR #21 and Issue #23;
- live KnowMe PR #15 mapping;
- registration topology decision;
- exact protected paths/branches/receipts;
- new repository-local GOAL/TASK/PLAN/RESULT/EVIDENCE/commands.log;
- first synthetic Pilot and rollback.

Exit:

```text
LOCAL_EXECUTION_PLANE_STATE=ACTIVATED
```

or factual blocker.

## SR1 — Schemas and validator

Implement:

- `RunnerProfile.schema.json`;
- `LocalExecutionRequest.schema.json`;
- `ExecutionReceipt.schema.json`;
- `RunnerHealthReceipt.schema.json`;
- `FailureClassification.schema.json`;
- semantic validator;
- positive and negative fixtures;
- stable blocker catalogue.

Negative fixtures include public PR/fork, stale SHA/tree, altered request, unpinned action, unauthorized command/path/network/secret, D2/D3, predecessor reuse, protected process/port and claim escalation.

## SR2 — Secure dispatcher

Implement:

- workflow_dispatch and validated repository_dispatch only;
- request identity payload only;
- source request fetched by exact repository/SHA/path/hash;
- product Parent PM ownership and current Goal check;
- full-SHA action pins;
- default `contents: read`;
- GitHub App or equally narrow approved cross-repo token;
- no arbitrary issue/comment shell;
- global/per-project concurrency;
- one attempt identity;
- artifact upload on failure.

## SR3 — Runner registration/profile/health

After topology authority:

- install/register official `actions/runner`;
- profile `owner-mac-mini-arm64-r1`;
- labels `self-hosted,macOS,ARM64,parent-pm-local-executor,owner-mac-mini`;
- capture observed runner version and update status;
- auto-update enabled by default;
- service/supervisor health;
- intended host/toolchain probe;
- runner name hidden in public evidence;
- no product source checkout in health-only Gate.

## SR4 — Local execution supervisor

Implement:

- fresh exact-SHA worktree;
- fresh task/evidence roots;
- request-declared cache only;
- isolated home/CODEX_HOME where applicable;
- durable command journal;
- process group and timeout;
- TERM→KILL owned processes only;
- protected ports/processes;
- no killall/pkill -f;
- source pre/post clean;
- artifact SHA-256 manifest;
- redaction/network/process receipts;
- single terminal ExecutionReceipt.

## SR5 — Synthetic Pilot

Run:

- Runner health;
- read-only source mapping;
- bounded test/build;
- one denied write;
- timeout/process leak negative;
- secret redaction negative;
- public trigger negative;
- rollback/removal/re-registration dry run.

No consumer product repository changes.

## SR6 — Codex Harness integration

Consume the accepted Codex Gateway under Runner authority:

```text
CODING=Luna/xhigh
PRODUCT_EXPERIENCE=Sol/xhigh
SILENT_FALLBACK=FORBIDDEN
APP_SERVER=stdio-jsonl
PRODUCTION_WEBSOCKET=FORBIDDEN
RUNNER_AUTO_REPAIR_BY_CODEX=FORBIDDEN
```

Prove:

- pinned Codex binary/schema;
- isolated CODEX_HOME;
- Runner request scope cannot be widened;
- nested Harness receipt included;
- Harness failure returns through Runner receipt;
- Runner failure does not auto-launch Codex repair.

## SR7 — KnowMe migration Pilot

- product Parent PM activates a new low-risk exact task;
- central request/profile/receipt used;
- current GOAL-003 Runtime/process protected;
- fresh attempt only;
- compare central receipt to PR #15 predecessor evidence;
- inject one Runner failure;
- Web ChatGPT Parent PM creates GitHub recovery successor;
- no product Gate is promoted automatically.

## SR8 — Additional product adapters

At least two accepted adapters:

- Copilot Electron/native/database/offline;
- Lingxi native import/STOP/export;
- AOG sanitized release/RAG/PII/FTS5.

Each remains owned by its product Parent PM.

## SR9 — Framework acceptance

- multi-repository cold-start;
- concurrency and isolation;
- stale runner/update handling;
- public trigger rejection;
- secret/data redaction;
- failure recovery;
- rollback;
- independent governance review;
- Human Owner Framework Gate.

## 7. Fixed failure ownership

```text
Runner FAIL
→ upload GitHub logs/jobs/steps/artifacts
→ Web ChatGPT Parent PM reads evidence
→ FIRST_BLOCKER classification
→ GitHub workflow/script/task/source successor
→ new attempt ID and fresh execution
```

Codex Luna is not the default Runtime executor or Runner recovery path. Only explicit Owner authorization may create a separate Luna recovery task.

## 8. Required blockers

```text
BLOCKED_RUNNER_CONTROL_REPOSITORY_NOT_SECURE
BLOCKED_RUNNER_PROFILE_NOT_PINNED
BLOCKED_RUNNER_OFFLINE
BLOCKED_RUNNER_LABEL_OR_CAPABILITY_MISMATCH
BLOCKED_RUNNER_VERSION_STALE
BLOCKED_LOCAL_EXECUTION_REQUEST_INVALID
BLOCKED_LOCAL_EXECUTION_SOURCE_IDENTITY_MISMATCH
BLOCKED_LOCAL_EXECUTION_PRODUCT_PM_NOT_AUTHORIZED
BLOCKED_LOCAL_EXECUTION_CURRENT_GOAL_NOT_PROTECTED
BLOCKED_LOCAL_EXECUTION_PUBLIC_PR_TRIGGER
BLOCKED_LOCAL_EXECUTION_UNPINNED_ACTION
BLOCKED_LOCAL_EXECUTION_SECRET_SCOPE
BLOCKED_LOCAL_EXECUTION_D2_D3_NOT_AUTHORIZED
BLOCKED_LOCAL_EXECUTION_PROTECTED_PATH
BLOCKED_LOCAL_EXECUTION_PROTECTED_PROCESS_OR_PORT
BLOCKED_LOCAL_EXECUTION_PREDECESSOR_REUSE
BLOCKED_LOCAL_EXECUTION_WORKTREE_NOT_FRESH
BLOCKED_LOCAL_EXECUTION_SOURCE_MUTATION
BLOCKED_LOCAL_EXECUTION_PROCESS_NOT_TERMINAL
BLOCKED_LOCAL_EXECUTION_EVIDENCE_INCOMPLETE
BLOCKED_LOCAL_EXECUTION_CLAIM_ESCALATION
BLOCKED_RUNNER_SELF_REPAIR_NOT_AUTHORIZED
```

## 9. Claim ceiling

```text
PLANNING_ONLY
RUNNER_REGISTRATION=NOT_AUTHORIZED_UNTIL_TOPOLOGY_GATE
REFERENCE_IMPLEMENTATION=NOT_STARTED
CONSUMER_PRODUCT_CHANGE=NO
PRODUCT_RUNTIME_PROOF=NO
REAL_D2_D3_OR_PRODUCTION_PII=NO
AUTO_MERGE_DEPLOY_SIGN_NOTARIZE_RELEASE=NO
```

## 10. First takeover output

```text
PARENT_PM_LOCAL_EXECUTION_PLANE_TAKEOVER_COMPLETE
CURRENT_PR3_SHA=
CURRENT_PR4_G7_STATE=
CURRENT_PR12_GATEWAY_STATE=
CENTRAL_CAPABILITY_SHA=
KNOWME_PR15_HEAD=
KNOWME_RUNNER_REFERENCE_STATE=
REGISTRATION_TOPOLOGY=
CONTROL_REPOSITORY_SECURITY_STATE=
RUNNER_PROFILE_STATE=
LOCAL_EXECUTION_PLANE_STATE=QUEUED|ACTIVATED|BLOCKED
FIRST_PILOT=
CURRENT_FIRST_BLOCKER=
NEXT_GOAL=
NEXT_AUTHORITY=
CONSUMER_PRODUCT_CHANGE=NO
AUTO_MERGE_DEPLOY_RELEASE=NO
```

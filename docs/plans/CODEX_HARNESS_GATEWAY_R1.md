# CODEX_HARNESS_GATEWAY_R1

> Repository：`zhouzengrui369-commits/chatgpt-parent-pm`  
> Program：`ECOSYSTEM-CODEX-HARNESS-R1`  
> State：`QUEUED / PLANNING_ONLY`  
> Execution owner：ChatGPT Parent PM Framework Project PM  
> Central capability：`zhouzengrui369-commits/knowme-ecosystem@8ccb543804a7881fd37b31e1ce35085ca7285a76`  
> Central Draft PR：`knowme-ecosystem#21`  
> Upstream research anchor：`openai/codex@93c54bca38996b56d344a2ca65f01627b1953b27`

## 1. Goal

Build the one ecosystem reference implementation for the official open-source Codex harness:

```text
Codex Harness Gateway
+ exact Binary/Protocol Lock
+ Task Envelope
+ Approval Broker
+ Model Profile enforcement
+ Session Binding
+ Event/Evidence Ledger
+ Process Supervisor
+ GitHub Self-hosted Runner Adapter
```

The Gateway converts a repository Project PM's GitHub-authorized task into a reproducible Codex worker session. It does not create product Goals, decide product scope, merge, deploy or issue Human Owner product decisions.

## 2. Current protected lane

The Project PM must read live GitHub truth before activation. At plan creation, the protected lane was:

```text
SHARED_CAPABILITY_ADOPTION_PR=3
ECOSYSTEM_V03_RC_PR=4
PR4_HEAD=6bee33442f1aec4995ae54d999989f939af8d772
PR4_RELEASE_CANDIDATE=0.3.0-rc.1
G0_G6=PASS
G7=BLOCKED_PENDING_INDEPENDENT_REVIEW_COLD_START_OWNER_GATE
```

This plan does not change or relabel PR #3/#4, their exact evidence, Geo Context or any consumer product.

Activation requires an explicit Project PM transition from the current G7 lane or a separately approved non-conflicting successor lane.

## 3. Architecture boundary

### This repository owns

- stable Codex release selection process;
- platform binary and protocol Schema locks;
- App Server stdio client;
- Codex Exec adapter;
- Task Envelope and policy validation;
- approval broker;
- session/thread lifecycle binding;
- model-profile discovery and enforcement;
- process timeout/cancellation;
- event/evidence normalization;
- secret/private-data redaction;
- Self-hosted Runner adapter;
- conformance fixtures and starter kit;
- Gateway release and migration guide.

### This repository does not own

- consumer product source or Runtime;
- product data and knowledge truth;
- product local deployment assignment;
- product experience repair;
- product candidate/Owner Gate;
- main merge, cloud deploy, signing, notarization or release in consumer repositories.

## 4. Model and execution policy

Owner defaults:

```text
CODING_PROFILE=Luna/xhigh
PRODUCT_EXPERIENCE_PROFILE=Sol/xhigh
SILENT_MODEL_OR_PROVIDER_FALLBACK=FORBIDDEN
EXECUTION_CONTRACT_LABEL_strongest=FORBIDDEN
```

The Gateway must discover exact model/profile support before starting a session. If unavailable, return a blocker; do not silently substitute another model, reasoning level or provider.

Initial transport:

```text
APP_SERVER_TRANSPORT=stdio-jsonl
PRODUCTION_WEBSOCKET=FORBIDDEN
```

## 5. Milestones

### HG0 — Current truth, transition and task authority

Deliverables:

- live PR #3/#4/G7 snapshot;
- explicit activation decision;
- exact central capability pin;
- protected current files/evidence;
- new repository-local `GOAL/TASK/PLAN/RESULT/EVIDENCE/commands.log`;
- claim ceiling and rollback.

Exit:

```text
CURRENT_G7_TRUTH=RESTORED
ACTIVATION=EXPLICIT
CONSUMER_PRODUCT_CHANGE=0
```

### HG1 — Stable upstream Binary and Protocol Lock

Deliverables:

- select official stable Codex release, not `main` or `latest`;
- exact release/tag/source commit where available;
- official distribution source;
- macOS ARM64 binary SHA-256;
- any supported Runner platform hashes;
- `codex --version` receipt;
- version-matched `generate-ts` and `generate-json-schema` output;
- protocol Schema SHA-256;
- Apache-2.0 / NOTICE record;
- lock JSON Schema and validator;
- upgrade compatibility report from the research anchor.

Exit:

```text
BINARY_LOCK=PASS
PROTOCOL_SCHEMA_LOCK=PASS
FLOATING_REFERENCE=0
```

### HG2 — Gateway core and process supervisor

Deliverables:

- stdio/JSONL process launch;
- initialize/initialized handshake;
- thread start/resume/fork/read/list/interrupt subset used by R1;
- turn start and event stream;
- Codex Exec one-shot adapter;
- process group/session;
- init/turn/command/idle/wall-clock timeouts;
- TERM then KILL grace;
- no surviving children;
- unsupported API/transport rejection.

Exit:

- deterministic protocol fixtures pass;
- cancellation and timeout receipts are durable;
- no global Codex/Git/shell/proxy configuration changed.

### HG3 — Task, approval and model profiles

Deliverables:

- `HarnessBinaryLock`;
- `CodexTaskEnvelope`;
- `CodexModelProfile`;
- `ApprovalEnvelope`;
- `SessionBinding`;
- A0–A5 approval classes;
- exact path/command/network scope;
- protected path hashing;
- Luna/xhigh and Sol/xhigh capability validation;
- no silent fallback.

Exit:

- positive/negative validation fixtures;
- predecessor approvals are rejected;
- wrong repository/source/model/path/network is rejected.

### HG4 — Event, evidence and redaction

Deliverables:

- normalized event journal;
- `EvidenceReceipt`;
- source/final SHA and diff hash;
- commands/checks/artifact identities;
- approval/network/token/time summaries;
- first blocker and next authority;
- secret/cookie/token/private path/data redaction;
- evidence claim layer.

Exit:

```text
TERMINAL_RECEIPT_RATE=100_PERCENT
UNREDACTED_SECRET_HITS=0
CLAIM_LAYER_ESCALATION=0
```

### HG5 — Security negative conformance

Must fail closed for:

- binary/schema mismatch;
- unavailable model or silent fallback;
- stale source/wrong repository;
- protected path/direct main write;
- wildcard/unapproved network;
- secret exposure;
- unauthorized D2/D3 or production data;
- predecessor worktree/approval/evidence reuse;
- unsupported WebSocket production config;
- timeout with surviving process;
- budget exhaustion;
- incomplete receipt;
- Harness evidence presented as Runtime/Product/Owner PASS;
- ecosystem/capability PM product takeover;
- Runner automatic self-repair.

### HG6 — Synthetic Pilot

Pilot ID：`PARENT-PM-HARNESS-PILOT-001`

Scenario:

1. fresh synthetic repository/worktree;
2. read-only mapping;
3. one approved bounded file write;
4. one denied write/network request;
5. test command;
6. diff/evidence;
7. interrupt/resume/fork;
8. timeout/cancel cleanup;
9. zero push/merge/private data;
10. terminal receipt.

### HG7 — GitHub Self-hosted Runner Pilot

Prove on intended Owner Mac mini:

- correct runner/machine identity;
- exact Binary/Schema Lock;
- isolated task `CODEX_HOME` and worktree;
- Luna/xhigh discovery;
- receipt/artifact upload;
- no interference with existing product Runtime/processes;
- injected Runner failure uploads evidence and launches no automatic Codex repair;
- Web ChatGPT Parent PM must create a new GitHub workflow/script/task successor.

### HG8 — Cross-repository cold-start and Human Owner Gate

Trials:

- KnowMe low-risk engineering Pilot;
- at least one of Copilot/Lingxi/AOG;
- Product Experience Reviewer read-only support Pilot.

Required:

- exact central/local pins;
- Project PM ownership preserved;
- no product claim escalation;
- uninstall/rollback;
- cost/observability report;
- independent governance review;
- Human Owner framework decision.

## 6. Required stable blockers

```text
BLOCKED_CODEX_BINARY_NOT_PINNED
BLOCKED_CODEX_BINARY_HASH_MISMATCH
BLOCKED_CODEX_PROTOCOL_SCHEMA_MISMATCH
BLOCKED_CODEX_MODEL_PROFILE_UNAVAILABLE
BLOCKED_CODEX_SILENT_FALLBACK_DETECTED
BLOCKED_CODEX_TASK_ENVELOPE_INVALID
BLOCKED_CODEX_SOURCE_IDENTITY_MISMATCH
BLOCKED_CODEX_PROTECTED_PATH_CHANGE
BLOCKED_CODEX_NETWORK_AUTHORITY_MISSING
BLOCKED_CODEX_SECRET_EXPOSURE
BLOCKED_CODEX_D2_D3_CONTEXT_NOT_AUTHORIZED
BLOCKED_CODEX_APPROVAL_SCOPE_MISMATCH
BLOCKED_CODEX_SESSION_BINDING_STALE
BLOCKED_CODEX_EVENT_RECEIPT_INCOMPLETE
BLOCKED_CODEX_PROCESS_NOT_TERMINAL
BLOCKED_CODEX_COST_OR_TIME_BUDGET
BLOCKED_CODEX_HARNESS_PRESENTED_AS_PRODUCT_PASS
BLOCKED_CODEX_PRODUCT_PM_OWNERSHIP_MISMATCH
BLOCKED_CODEX_RUNNER_SELF_REPAIR_NOT_AUTHORIZED
```

## 7. Acceptance layers

```text
SOURCE_GATE
PROTOCOL_CONFORMANCE_GATE
SECURITY_GATE
SYNTHETIC_RUNTIME_GATE
SELF_HOSTED_RUNNER_GATE
MULTI_REPO_COLD_START_GATE
HUMAN_OWNER_FRAMEWORK_GATE
```

A green source/protocol/security Gate does not prove product Runtime or customer value.

## 8. Claim ceiling

```text
PLANNING_ONLY
CURRENT_PR3_PR4_GATE_CHANGE=NO
REFERENCE_GATEWAY_IMPLEMENTATION=NOT_STARTED_BY_THIS_PLAN
CONSUMER_PRODUCT_CHANGE=NO
REAL_SECRET_OR_PRIVATE_DATA=NO
SELF_HOSTED_RUNNER_PILOT=NOT_STARTED
AUTO_MERGE_DEPLOY_RELEASE=NO
HUMAN_OWNER_FRAMEWORK_GATE=REQUIRED
```

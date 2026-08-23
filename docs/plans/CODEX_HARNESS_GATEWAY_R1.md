# CODEX_HARNESS_GATEWAY_R1

> Repository: `zhouzengrui369-commits/chatgpt-parent-pm`  
> Visibility: `public`  
> Program: `ECOSYSTEM-CODEX-HARNESS-R1`  
> State: `QUEUED / PLANNING_ONLY`  
> Owner: ChatGPT Parent PM Framework Project PM  
> Self-deployment plan: [`PARENT_PM_LOCAL_AGENT_DEPLOYMENT_R1.md`](./PARENT_PM_LOCAL_AGENT_DEPLOYMENT_R1.md)  
> Visibility router: [`VISIBILITY_ROUTED_EXECUTION_ROUTER_R1.md`](./VISIBILITY_ROUTED_EXECUTION_ROUTER_R1.md)

## 1. Goal

Build the open Codex Harness Gateway reference implementation:

- stable Codex binary/protocol locks;
- App Server stdio and Codex Exec adapters;
- Task/Approval/Model/Session contracts;
- event/evidence/redaction;
- process supervision and conformance;
- integration with visibility-routed local executors.

## 2. Executor routing

```text
private consumer repository -> repository-bound Mac mini Runner
public consumer repository  -> Owner-designated Local Agent
```

`chatgpt-parent-pm` is public. Its own source/test/build/App Server synthetic validation uses a Local Agent. No Self-hosted Runner is registered to this repository.

The Gateway may execute inside either authorized executor adapter, but it cannot choose or widen the executor request.

## 3. Protected lane

Read live before activation:

- PR #3 Shared Capability Adoption;
- PR #4 G0-G7 current state;
- PR #12 and Issues #13/#14/#15;
- central ADR 0007/0008/0009;
- all consumer current Candidates and ownership.

## 4. Model/transport policy

```text
CODING_OR_DEPLOYMENT=Luna/xhigh
PRODUCT_EXPERIENCE=Sol/xhigh
SILENT_MODEL_OR_PROVIDER_FALLBACK=FORBIDDEN
CONTRACT_LABEL_strongest=FORBIDDEN
APP_SERVER_TRANSPORT=stdio-jsonl
PRODUCTION_WEBSOCKET=FORBIDDEN
```

## 5. Milestones

### HG0 — Current truth and transition

Restore current framework/G7/visibility-router truth, freeze the central capability and protect consumers.

### HG1 — Binary and Protocol Lock

Select an official stable Codex release, exact binary hashes, generated protocol Schema hash, license/NOTICE and upgrade validator.

### HG2 — Gateway core

Implement stdio handshake, thread/turn/item subset, Exec adapter, inner process groups/timeouts/cancellation and unsupported transport rejection.

### HG3 — Task, approval and model profiles

Implement Task/Model/Approval/Session envelopes and verify they are a subset of the selected executor request.

### HG4 — Event, evidence and redaction

Normalize event journal and nested Harness receipt, bind it to Local Agent or Runner outer receipt and remove secrets/private paths/data.

### HG5 — Security negatives

Reject binary/schema/model mismatch, silent fallback, stale source, protected paths, wildcard network, secret/D2/D3, predecessor reuse, nonterminal process, claim escalation, visibility/executor mismatch and automatic Runner repair.

### HG6 — Public Local Agent synthetic Pilot

Validate this public repository through an exact Local Agent task: read-only map, one bounded source/test task, one denied action, failure handback and no source repair during deployment.

### HG7 — Private Runner integration Pilot

Consume the Gateway inside a private repository Runner task, initially KnowMe or knowme-ecosystem. This repository itself does not register the Runner.

### HG8 — Multi-repository cold-start and Owner Gate

Trial at least one private Runner consumer, two public Local Agent consumers and Reviewer support; prove rollback, failure ownership and Human Owner framework acceptance.

## 6. Required blockers

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
BLOCKED_CODEX_EXECUTOR_REQUEST_MISSING
BLOCKED_CODEX_SCOPE_WIDER_THAN_EXECUTOR_REQUEST
BLOCKED_EXECUTOR_VISIBILITY_POLICY_MISMATCH
```

## 7. Failure ownership

```text
Harness or executor FAIL
→ durable evidence
→ Web ChatGPT Parent PM diagnosis
→ GitHub source/task/framework successor
→ fresh executor attempt
```

No automatic local repair or Runner recovery by Codex.

## 8. Claim ceiling

```text
PLANNING_ONLY
CURRENT_PR3_PR4_GATE_CHANGE=NO
GATEWAY_IMPLEMENTATION=NOT_STARTED
PARENT_PM_SELF_EXECUTOR=LOCAL_AGENT
PARENT_PM_SELF_HOSTED_RUNNER_REGISTRATION=NO
CONSUMER_PRODUCT_CHANGE=NO
REAL_SECRET_OR_PRIVATE_DATA=NO
AUTO_MERGE_DEPLOY_RELEASE=NO
HUMAN_OWNER_FRAMEWORK_GATE=REQUIRED
```

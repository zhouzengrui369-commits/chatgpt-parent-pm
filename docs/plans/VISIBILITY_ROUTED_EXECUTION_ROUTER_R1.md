# VISIBILITY_ROUTED_EXECUTION_ROUTER_R1

> Repository: `zhouzengrui369-commits/chatgpt-parent-pm`  
> Program: `ECOSYSTEM-CODEX-HARNESS-R1`  
> State: `QUEUED / PLANNING_ONLY`  
> Owner: ChatGPT Parent PM Framework Project PM  
> Decision: `knowme-ecosystem` ADR 0009

## 1. Goal

Build the Parent PM framework router that selects the local executor from the repository's live GitHub visibility:

```text
private -> Mac mini Self-hosted Runner adapter
public  -> Owner-designated Local Agent adapter
```

The router governs identity and evidence. It does not execute product work by itself or own product Gate decisions.

## 2. Current repository map

Read live at activation. Acceptance-time discovery:

### Private

- knowme-ecosystem
- knowme
- knowme-personal-workbench
- knowme-copilot

### Public

- chatgpt-parent-pm
- copilot-app
- lingxi-presentation
- aog-knowledge-base
- product-experience-reviewer-skill
- ebook-miniapp

## 3. Core contracts

Implement:

- `RepositoryVisibilityReceipt`;
- `ExecutorRoutingDecision`;
- `CommonExecutionRequest`;
- `CommonExecutionReceipt`;
- `VisibilityTransitionReceipt`;
- executor-specific request/receipt references;
- stable visibility and executor blockers.

## 4. Router logic

```text
fetch repository metadata
-> record repository id/full name/visibility/timestamp
-> compare to frozen Project Profile/plan
-> select exactly one executor
-> validate executor adapter available
-> emit routing receipt
-> re-check visibility before final adjudication
```

## 5. Required blockers

```text
BLOCKED_REPOSITORY_VISIBILITY_UNRESOLVED
BLOCKED_EXECUTOR_VISIBILITY_POLICY_MISMATCH
BLOCKED_PUBLIC_REPOSITORY_SELF_HOSTED_RUNNER
BLOCKED_PRIVATE_REPOSITORY_LOCAL_AGENT_WITHOUT_EXCEPTION
BLOCKED_REPOSITORY_VISIBILITY_CHANGED_AFTER_FREEZE
BLOCKED_EXECUTOR_ADAPTER_NOT_AVAILABLE
BLOCKED_EXECUTOR_PROFILE_NOT_PINNED
```

## 6. Parent PM repository self-execution

`chatgpt-parent-pm` is public. Therefore its own source/test/build/deployment validation uses the Local Agent adapter.

No production Self-hosted Runner is registered to this repository.

## 7. Milestones

### VR0 — Current truth and accepted policy

- live PR #3/#4/#12 and central ADR 0009;
- exact visibility inventory;
- prior public Runner plans marked superseded;
- current product Goals protected.

### VR1 — Common schemas and validator

- deterministic schema/semantic tests;
- visibility mismatch negatives;
- current visibility recheck;
- no network/secret/product mutation.

### VR2 — Private Runner adapter binding

Bind the open Runner framework contracts to private repository plans, without registering a Runner in this public repo.

### VR3 — Public Local Agent adapter binding

Bind LocalAgentProfile/Request/Receipt and no-source-mutation deployment mode to public repository plans.

### VR4 — Transition and fallback policy

- private->public invalidates Runner;
- public->private invalidates Local Agent plan;
- no silent executor fallback;
- private local-Agent exception requires exact Human Owner/Project PM authority.

### VR5 — Multi-repository trials

- private: KnowMe;
- private: knowme-ecosystem or personal-workbench;
- public: Parent PM local-Agent self-validation;
- public: at least two product local-Agent deployments;
- failure handback and rollback.

### VR6 — Framework acceptance

- cold-start routing;
- visibility changes;
- evidence/claim separation;
- independent governance review;
- Human Owner Framework Gate.

## 8. Claim ceiling

```text
PLANNING_ONLY
ROUTER_IMPLEMENTATION=NOT_STARTED
PARENT_PM_SELF_EXECUTOR=LOCAL_AGENT
PARENT_PM_RUNNER_REGISTRATION=NO
CONSUMER_PRODUCT_CHANGE=NO
AUTO_MERGE_DEPLOY_RELEASE=NO
```

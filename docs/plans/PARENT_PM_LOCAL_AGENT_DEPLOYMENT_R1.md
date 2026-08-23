# PARENT_PM_LOCAL_AGENT_DEPLOYMENT_R1

> Repository: `zhouzengrui369-commits/chatgpt-parent-pm`  
> Visibility: `public`  
> Executor: `OWNER_DESIGNATED_LOCAL_AGENT`  
> Program: `ECOSYSTEM-CODEX-HARNESS-R1`  
> State: `QUEUED / PLANNING_ONLY`

## 1. Goal

Use an Owner-designated local Agent to validate and deploy the public Parent PM framework at an exact SHA without registering the Owner Mac mini as a Self-hosted Runner for this repository.

## 2. Allowed tasks

- framework source/static review;
- schema/validator/unit/integration tests;
- starter-kit generation checks;
- local package/build/CLI smoke;
- synthetic Codex Gateway/App Server tests;
- visibility router tests;
- public-safe documentation and release-candidate artifact checks.

## 3. Forbidden tasks

- Self-hosted Runner registration in this public repository;
- direct public PR/fork execution on the Mac mini;
- real consumer product mutation;
- real D2/D3/production PII;
- silent source repair during deployment;
- direct main/merge/tag/release;
- Product Experience or Human Owner claim from technical evidence.

## 4. Agent policy

The Project PM names the local Agent per task.

When Codex is used:

```text
ENGINEERING_OR_DEPLOYMENT=Luna/xhigh
PRODUCT_EXPERIENCE=Sol/xhigh
SILENT_FALLBACK=FORBIDDEN
```

Default deployment mode:

```text
SOURCE_MUTATION=NO
LOCAL_REPAIR=NO
PUSH=NO
MERGE=NO
```

## 5. Activation prerequisites

- [ ] live PR #3/#4/#12 truth restored;
- [ ] central ADR 0009 and visibility receipt pinned;
- [ ] repository-local Goal/TASK/PLAN/RESULT/EVIDENCE/commands.log;
- [ ] exact source SHA/tree;
- [ ] LocalAgentProfile and request;
- [ ] synthetic/public-safe data only;
- [ ] exact commands/checks/artifacts;
- [ ] protected paths/processes/ports;
- [ ] fresh local checkout/worktree/task/evidence roots;
- [ ] rollback.

## 6. Milestones

### PLA0 — Current truth and activation

Restore framework/Gateway/router state, choose first bounded use case and exact Agent profile.

### PLA1 — Read-only/source test Pilot

Fresh exact-SHA checkout, source/schema/fixture validation, no source change and terminal receipt.

### PLA2 — Bounded build/runtime Pilot

Run public-safe framework build/CLI/App Server synthetic smoke with no consumer data or product process interference.

### PLA3 — Failure handback

Inject a bounded test/toolchain failure. Agent returns evidence; Web ChatGPT Parent PM creates GitHub successor; no local repair.

### PLA4 — Framework release evidence

Produce public-safe artifact/hash/compatibility receipt. Independent governance and Human Owner framework decisions remain separate.

## 7. First output

```text
PARENT_PM_LOCAL_AGENT_TAKEOVER_COMPLETE
CURRENT_PR3_SHA=
CURRENT_PR4_G7_STATE=
CURRENT_PR12_SHA=
REPOSITORY_VISIBILITY=public
EXECUTOR=LOCAL_AGENT
LOCAL_AGENT_PROFILE=
VISIBILITY_ROUTER_STATE=
FIRST_USE_CASE=
LOCAL_AGENT_STATE=QUEUED|ACTIVATED|BLOCKED
CURRENT_FIRST_BLOCKER=
NEXT_GOAL=
NEXT_AUTHORITY=
SELF_HOSTED_RUNNER_REGISTRATION=NO
CONSUMER_PRODUCT_CHANGE=NO
AUTO_MERGE_RELEASE=NO
```

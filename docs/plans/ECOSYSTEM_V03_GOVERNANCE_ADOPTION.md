# Parent PM v0.3 Ecosystem Governance Adoption Plan

> **Plan ID**: `PARENT-PM-ECOSYSTEM-V03-R1`
> **State**: `ACTIVATED_G5 / G5_PASS`
> **Execution owner**: ChatGPT Parent PM framework Project PM
> **Ecosystem authority**: `zhouzengrui369-commits/knowme-ecosystem@e46c4be501c465884486a4417adca2e158a58ccc`
> **Ecosystem PR**: `knowme-ecosystem#17`
> **Date**: 2026-08-11
> **G0 activation**: 2026-08-14, stacked on protected Draft PR #3

---

## 1. Purpose

Extend the Parent PM governance Core so repository-local Project PMs can adopt ecosystem v0.3 and Shared Knowledge Engine capabilities through exact, fail-closed contracts while preserving current candidates, evidence and PM ownership.

The framework must make it difficult to:

- silently create a second canonical knowledge truth;
- claim Shared Knowledge Engine compatibility without a pinned contract and conformance evidence;
- expose physical database tables as an unversioned ecosystem API;
- treat broad collection permission as cloud/write/execution permission;
- overwrite active product candidates during a strategic migration;
- let a central ecosystem/capability PM take over consumer product delivery;
- promote planning, fixtures or source CI into product/runtime/release truth.

---

## 2. Protected current truth

Before activation, the Parent PM framework PM must read:

- repository governance/skill entry and current framework version/status;
- open Shared Capability Adoption Draft PR #3 and its exact contract/tests;
- current schema/validator/CI and capability-ownership behavior;
- all current product-project integration assumptions;
- any later merged or successor governance change.

Hard protection:

- v0.3 planning does not change or relabel PR #3;
- Geo Context remains its own capability identity and evidence chain;
- no consumer product source, candidate, deployment, review or release is changed from this repository;
- G0 is activated by the framework PM on a branch stacked on protected Draft PR #3; this transition does not authorize consumer implementation, merge or release;
- no central governance code may silently execute consumer product implementation.

---

## 3. Required governance model

### 3.1 Ecosystem baseline identity

Every v0.3 adoption record must pin:

```yaml
ecosystem:
  repository: zhouzengrui369-commits/knowme-ecosystem
  commit: full-40-character-sha
  version: semver
  blueprint_path: docs/blueprint/ecosystem-blueprint-v0.3.md
  blueprint_sha256: 64-hex
```

No `latest`, tag-only or moving branch authority.

### 3.2 Shared contract identity

```yaml
shared_knowledge_engine:
  contract_version: semver
  contract_commit: full-sha
  contract_manifest_sha256: 64-hex
  supported_capabilities: []
  required_conformance_receipts: []
  implementation_provider: optional-id
  implementation_artifact: optional-exact-identity
```

A product may pin a subset, but unsupported capabilities remain explicit and cannot be claimed.

### 3.3 Product ownership identity

```yaml
product:
  repository: owner/name
  project_pm: role-or-identity
  current_protected_goal: string
  current_candidate_sha: optional-full-sha
  migration_state: queued | activated | implementing | candidate | accepted | blocked
  local_goal_id: optional
  deviations: []
```

### 3.4 Authority split

- Ecosystem PM: baseline, shared contracts, compatibility and program tracking.
- Capability/reference PM: implementation of the reusable capability in its owning repository.
- Consumer Project PM: product adapter, UX, candidate, deployment, review and Human Owner delivery.
- MiniMax/Mavis/Codex/other workers: only under repository-local Goal and exact authority.
- Human Owner: product-role baseline, D2/D3, E3+, merge, release and final value decisions.

---

## 4. Required lifecycle

```text
PROPOSED_ECOSYSTEM_BASELINE
→ HUMAN_OWNER_BASELINE_ACCEPTED
→ EXACT_BASELINE_PINNED
→ SHARED_CONTRACT_CANDIDATE
→ CONTRACT_CONFORMANCE_SOURCE_PASS
→ REFERENCE_IMPLEMENTATION_CANDIDATE
→ REFERENCE_IMPLEMENTATION_RUNTIME_ACCEPTED
→ CONSUMER_PLAN_QUEUED
→ CONSUMER_PROJECT_PM_ACTIVATED
→ CONSUMER_SOURCE_CANDIDATE
→ CONSUMER_RUNTIME_ACCEPTED
→ INDEPENDENT_PRODUCT_EXPERIENCE_ACCEPTED
→ HUMAN_OWNER_PRODUCT_GATE
```

Not every consumer needs every capability. A consumer may stay `QUEUED_OPTIONAL` or close as `NOT_ACTIVATED_NO_CUSTOMER_VALUE`.

---

## 5. New fail-closed blockers

### Baseline and contract

```text
BLOCKED_ECOSYSTEM_BASELINE_IDENTITY_MISSING
BLOCKED_ECOSYSTEM_BASELINE_SHA_INVALID
BLOCKED_ECOSYSTEM_BASELINE_NOT_ACCEPTED
BLOCKED_SHARED_CONTRACT_NOT_PINNED
BLOCKED_SHARED_CONTRACT_HASH_MISMATCH
BLOCKED_SHARED_CAPABILITY_NOT_SUPPORTED
BLOCKED_CONFORMANCE_RECEIPT_MISSING
BLOCKED_REFERENCE_IMPLEMENTATION_IDENTITY_MISSING
```

### Product boundary

```text
BLOCKED_PRODUCT_ROLE_MISMATCH
BLOCKED_DUPLICATE_TRUTH_LAYER_WITHOUT_ADR
BLOCKED_PHYSICAL_SCHEMA_EXPOSED_AS_CONTRACT
BLOCKED_PRODUCT_SPECIFIC_POLICY_LEAKED_INTO_SHARED_CONTRACT
BLOCKED_DOMAIN_EXTENSION_COLLIDES_WITH_CORE_SCHEMA
BLOCKED_CURRENT_PROTECTED_GOAL_NOT_DECLARED
BLOCKED_CURRENT_CANDIDATE_MUTATION
```

### Permission, privacy and execution

```text
BLOCKED_PERMISSION_SCOPE_UNPROVEN
BLOCKED_COLLECTION_REUSED_FOR_UNDECLARED_PURPOSE
BLOCKED_CLOUD_EGRESS_AUTHORITY_MISSING
BLOCKED_AGENT_WRITE_AUTHORITY_MISSING
BLOCKED_D2_D3_PRODUCT_GATE_MISSING
BLOCKED_D3_ORDINARY_INDEX_OR_LOG_PATH
BLOCKED_E3_PLUS_OWNER_AUTHORITY_MISSING
BLOCKED_DELETION_LIFECYCLE_UNBOUND
```

### PM ownership and claims

```text
BLOCKED_CAPABILITY_PM_OWNERSHIP_MISMATCH
BLOCKED_ECOSYSTEM_PM_PRODUCT_TAKEOVER
BLOCKED_PROJECT_PM_ACTIVATION_MISSING
BLOCKED_PLANNING_ONLY_CLAIM_ESCALATION
BLOCKED_SOURCE_TEST_PRESENTED_AS_RUNTIME
BLOCKED_FIXTURE_PRESENTED_AS_REAL_DATA
BLOCKED_PRODUCT_EXPERIENCE_RECEIPT_MISSING
BLOCKED_HUMAN_OWNER_GATE_MISSING
```

Every blocker must include the first factual failing field, expected authority and allowed next owner. Do not auto-repair across repositories.

---

## 6. Duplicate truth-layer detection

The governance system should inspect repository plans/diffs for new long-term implementations of:

- canonical knowledge objects/relations;
- provenance/source ledger;
- generic review/conflict/expiry;
- full-text/vector/graph/Wiki truth;
- generic Agent permission/access;
- backup/export/import/migration/deletion;
- personal identity/value/relationship models outside KnowMe;
- unrestricted direct database integration.

Detection is not an automatic rejection. The Project PM may supply an accepted deviation ADR with:

- why the shared contract/reference cannot satisfy the case;
- exact scope;
- interoperability and migration plan;
- security consequences;
- owner and review/expiry date.

Without that record, fail closed.

---

## 7. Planning-only to active Goal transition

A planning PR/issue may contain architecture, milestones and PM handoff. It must not:

- modify product Runtime;
- advance release state;
- open D2/D3 or E3+ permissions;
- assign local deployment to a worker before Project PM activation;
- claim a candidate or customer value.

Activation requires:

```yaml
activation:
  project_pm_acceptance: receipt/ref
  current_truth_snapshot: ref
  protected_goal_transition: ref
  ecosystem_baseline_pin: full-sha
  contract_pin: version+hash-or-explicit-not-yet-needed
  local_goal_id: string
  task_root: repository-path
  worker_assignments: []
  scope_and_non_goals: []
  acceptance_and_evidence: []
  rollback: string
```

---

## 8. Cross-project dependency management

The framework must distinguish:

- **contract dependency**: consumer can implement against schemas/fixtures;
- **reference implementation dependency**: consumer needs a Copilot artifact/service/library;
- **product dependency**: user journey requires another product Runtime;
- **optional enrichment**: integration adds value but does not block base product;
- **governance dependency**: exact baseline or reviewer extension required.

A consumer may activate a thin contract-compatible slice before the full reference implementation only when the supported subset, substitute implementation and claim ceiling are explicit.

---

## 9. Evidence manifest

Recommended machine-readable record:

```yaml
schema_version: 1.0.0
program_id: ECOSYSTEM-V03-DIGITAL-TWIN-R1
repository: owner/name
project_pm: role
migration_state: queued
current_protected_goal:
  id: string
  candidate_sha: optional
  gate: string
ecosystem:
  commit: full-sha
  blueprint_sha256: 64-hex
shared_contract:
  version: optional
  manifest_sha256: optional
  supported_capabilities: []
local_goal:
  id: optional
  branch: optional
  source_sha: optional
implementation:
  provider: optional
  artifact_sha256: optional
  runtime_id: optional
receipts:
  source_gate: optional
  conformance: optional
  local_runtime: optional
  product_experience: optional
human_owner_gate: not_started
deviations: []
claim_ceiling: []
```

The framework validates identity and allowed state transitions but does not invent missing product evidence.

---

## 10. Milestone plan

### G0 — Activation and current-framework mapping

- read PR #3 and current framework truth;
- create repository-local Goal/TASK/PLAN/RESULT/EVIDENCE/commands.log;
- pin ecosystem v0.3 candidate/accepted commit;
- map existing shared capability schema and ownership checks;
- identify backward-compatible extensions vs breaking changes;
- preserve Geo Context fixtures and results.

### G1 — v0.3 adoption schema

- implement baseline/contract/product/activation/evidence fields;
- positive/negative fixtures for KnowMe, Copilot, Lingxi, AOG and optional ebook;
- migration state transition validator;
- exact SHA/hash and no-`latest` rules.

### G2 — architecture boundary validator

- duplicate truth detection inputs;
- physical-schema contract blocker;
- product-role and core/domain extension checks;
- deviation ADR schema and expiry.

### G3 — permission/security validator

- D0-D3 grant dimensions;
- cloud/Agent write/execution separation;
- D3 ordinary-index/log blocker;
- deletion/export lifecycle fields;
- D2/D3 and E3+ Human Owner authority checks.

### G4 — PM ownership and claim validator

- protected Goal declaration;
- Project PM activation receipt;
- central/capability PM takeover blocker;
- planning/source/fixture/runtime/product/release claim ceilings;
- independent reviewer and Human Owner receipt checks.

### G5 — repository starter kit

Provide:

- `ECOSYSTEM_V03_ADOPTION.yaml` template;
- `CURRENT_TRUTH_SNAPSHOT.md` template;
- planning PR template;
- active Goal template;
- conformance/evidence manifest template;
- deviation ADR template;
- cross-project tracker updater.

### G6 — CI and regression

- preserve existing Parent PM/shared capability behavior;
- run deterministic positive and blocker fixtures;
- reject ownership escalation and candidate mutation;
- validate example plans from all consumer repositories;
- publish versioned governance release and migration guide.

### G7 — framework review and adoption

- independent governance review;
- trial cold-start takeover in at least two repositories;
- confirm no need for conversation-memory context;
- Human Owner accepts the governance release before product PMs claim it as authority.

---

## 11. Non-goals

This repository does not:

- implement Shared Knowledge Engine Runtime;
- implement KnowMe digital twin;
- edit product source or local data;
- run product local deployment;
- perform product experience review;
- merge/release consumer PRs;
- decide customer value for a product.

---

## 12. Project PM first action

Return:

```text
PARENT_PM_CURRENT_ACTIVE_GOAL=
CURRENT_FRAMEWORK_SHA=
PR_3_STATE=
CURRENT_GATE=
CURRENT_BLOCKER=
V03_MIGRATION_STATE=QUEUED|ACTIVATED|BLOCKED
ACTIVATION_PREREQUISITE=
PINNED_ECOSYSTEM_SHA=e46c4be501c465884486a4417adca2e158a58ccc
NEXT_REPOSITORY_LOCAL_GOAL=
BACKWARD_COMPATIBILITY_PLAN=
```

Do not implement until this snapshot matches current repository and PR #3 truth.

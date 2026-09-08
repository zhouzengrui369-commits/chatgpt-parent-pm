# Repository Local Execution Policy

Version: 0.2.0-alpha
Protocol: DELIVERY-LIFECYCLE-1.0

## Authority

This policy implements the Human Owner ecosystem execution-topology decision recorded in `zhouzengrui369-commits/knowme-ecosystem#32`.

## Canonical topology

```text
GITHUB=SINGLE_AUTHORITATIVE_FACT_SOURCE_AND_REMOTE_CONTROL_PLANE
LOCAL_EXECUTOR=OWNER_DESIGNATED_LOCAL_AGENT
LOCAL_EXECUTION_ROUTE=LOCAL_AGENT_ONLY
SILENT_EXECUTOR_FALLBACK=FORBIDDEN
```

The same local-execution rule applies to private and public repositories. Repository visibility does not select a different local executor.

## GitHub boundary

GitHub remains authoritative for:

- repository `AGENTS.md`, governance locks and project profiles;
- Product Baselines and frozen Goal/Milestone Contracts;
- Change Requests and Engineering Delivery handoffs;
- branches, PRs, exact SHA/tree/parent identities and candidate artifacts;
- durable lifecycle receipts and historical evidence;
- normal repository CI when the project contract permits it.

Normal CI is engineering evidence only. It cannot substitute for a contracted Local Agent observation when real Owner-machine, device, data, browser, credential, local database, native runtime or deployment evidence is required.

## Local Agent boundary

A Local Agent acts only under an exact bounded request issued by the role that owns the required evidence bucket. The request must bind at minimum:

```text
REPOSITORY
GOAL_ID
MILESTONE_ID
REQUESTING_ROLE
EVIDENCE_BUCKET
CANDIDATE_SHA
CANDIDATE_TREE
PRESCRIBED_STEPS
ALLOWED_DATA
FORBIDDEN_DATA
SOURCE_MUTATION=FORBIDDEN
TEST_MUTATION=FORBIDDEN
COMMIT_PUSH=FORBIDDEN
SELF_REPAIR=FORBIDDEN
SCOPE_EXPANSION=FORBIDDEN
```

The Local Agent may:

- materialize the authorized exact candidate;
- inject Owner-machine credentials without committing or exposing them;
- execute prescribed local build/runtime/device/data/browser/deployment observations;
- return sanitized observations and evidence references.

The Local Agent must not:

- change source, tests, locks, workflows or build/deploy scripts;
- commit, push, merge, tag or release;
- repair the candidate or expand scope;
- declare `ENGINEERING_READY`;
- admit a candidate or declare review eligibility;
- issue the independent Product Experience verdict;
- grant Human Owner Acceptance.

## Engineering Delivery boundary

Engineering Delivery does not operate the Owner machine as part of its role. When an `engineering_required` item needs local execution, Engineering Delivery issues an exact Local Agent request, receives the sanitized observation receipt, adjudicates it against the technical contract and records the result in the Technical Receipt.

A missing required Local Agent receipt produces the Engineering Delivery blocker required by the frozen contract; it is not permission for Engineering Delivery to perform the local steps itself.

## Product Governance boundary

Product Governance may define and freeze which evidence bucket requires Local Agent execution, verify exact identity, and adjudicate only the buckets it owns. Product Governance does not execute local steps, repair candidates, or substitute CI output for required Local Agent observations.

## Historical evidence

Historical receipts from predecessor executor topologies remain immutable evidence for their original exact SHA and gate. They do not provide prospective execution authority and must not be reused as PASS for a new candidate.

## Migration rule

Any active Goal/Milestone contract, project profile, governance lock, workflow, script, adapter or execution task that requires a different local executor must be superseded before the next local attempt. Governance-only wording may be changed by Product Governance; technical workflow/script/configuration removal belongs to a separate Engineering Delivery context.

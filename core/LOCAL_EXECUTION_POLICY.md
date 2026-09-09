# Repository Local Execution Policy

Version: 0.2.0-alpha
Protocol: DELIVERY-LIFECYCLE-1.0

## Authority

This policy implements the Human Owner ecosystem execution decisions recorded in:

- `zhouzengrui369-commits/knowme-ecosystem#32` — Owner-designated Local Agent as the only local executor;
- `zhouzengrui369-commits/knowme-ecosystem#37` — mandatory post-deployment operational/browser verification.

## Canonical topology

```text
GITHUB=SINGLE_AUTHORITATIVE_FACT_SOURCE_AND_REMOTE_CONTROL_PLANE
LOCAL_EXECUTOR=OWNER_DESIGNATED_LOCAL_AGENT
LOCAL_EXECUTION_ROUTE=LOCAL_AGENT_ONLY
SILENT_EXECUTOR_FALLBACK=FORBIDDEN
POST_DEPLOYMENT_OPERATIONAL_VERIFICATION=REQUIRED
DEPLOYMENT_SUCCESS_ALONE=INSUFFICIENT
BROWSER_VERIFICATION=REQUIRED_WHEN_BROWSER_OPERABLE_OR_BROWSER_JOURNEY_APPLIES
VERIFICATION_METHOD=TOOL_AGNOSTIC
LOCAL_AGENT_OWN_BROWSER_CAPABILITY=PREFERRED
OWNER_FOREGROUND_BROWSER_OR_DESKTOP=LAST_RESORT
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

Normal CI is engineering evidence only. It cannot substitute for a contracted Local Agent observation when real Owner-machine, device, data, browser, credential, local database, native runtime, deployment or post-deployment operational evidence is required.

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
- after deployment or runtime launch, perform the required post-deployment operational verification;
- return sanitized observations and evidence references.

The Local Agent must not:

- change source, tests, locks, workflows or build/deploy scripts;
- commit, push, merge, tag or release;
- repair the candidate or expand scope;
- declare `ENGINEERING_READY`;
- admit a candidate or declare review eligibility;
- issue the independent Product Experience verdict;
- grant Human Owner Acceptance.

## Mandatory post-deployment operational verification

When the bounded Local Agent request includes deployment, installation, runtime launch, or materialization of a runnable candidate, successful deployment/start/process/port/health evidence alone is not a complete Local Agent result.

After deployment/launch the Local Agent must verify, where applicable:

- deployed/runtime identity remains bound to the authorized exact candidate SHA/tree or contract-defined deployment identity;
- the runtime/application is reachable and not merely process-started;
- the primary deployed surface opens/renders successfully;
- the prescribed deployment smoke or critical journey can be operated, not only fetched statically;
- blocking runtime errors, broken routing, fatal loading states, bootstrap/authentication failures or unusable first interaction are surfaced;
- sanitized evidence is returned to the requesting role.

For browser-accessible products or a contract containing a browser-operable journey, browser operation is the default verification route.

The method is tool-agnostic. No browser vendor, engine, automation framework or vendor-specific Browser Use implementation is required. Preference order is:

1. Local Agent built-in/program-provided browser-operation capability or isolated browser surface;
2. Local Agent-controlled headless/isolated browser or isolated browser profile/session;
3. another non-disruptive automated browser route that does not seize the Human Owner's foreground mouse, keyboard, browser window or desktop;
4. Human Owner foreground browser/desktop automation only when the required observation cannot be proven otherwise and the frozen contract permits it.

```text
NON_DISRUPTIVE_BROWSER_FIRST=REQUIRED
FOREGROUND_TAKEOVER_FOR_CONVENIENCE=FORBIDDEN
OWNER_FOREGROUND_INTERACTION=LAST_RESORT
```

If the product has no browser-operable surface, the frozen contract may mark browser verification `NOT_APPLICABLE`. Equivalent post-deployment operational verification remains mandatory using the Local Agent's own least-disruptive permitted runtime/UI/device capability.

If deployment succeeds but required post-deployment verification fails or cannot be completed:

```text
LOCAL_EXECUTION_RESULT=FAIL_OR_BLOCKED
DEPLOYMENT_ONLY_PASS_PROMOTION=FORBIDDEN
SELF_REPAIR=FORBIDDEN
```

The Local Agent returns the blocker and evidence. It does not repair candidate bytes or weaken the frozen contract.

```text
LOCAL_AGENT_POST_DEPLOYMENT_PASS
!= TECHNICAL_PASS
!= ENGINEERING_READY
!= CANDIDATE_ADMITTED
!= PRODUCT_REVIEW_ELIGIBLE
!= PRODUCT_EXPERIENCE_PASS
!= HUMAN_OWNER_ACCEPTED
!= RELEASE_AUTHORIZED
!= GOAL_MILESTONE_CLOSED
```

## Engineering Delivery boundary

Engineering Delivery does not operate the Owner machine as part of its role. When an `engineering_required` item needs local execution, Engineering Delivery issues an exact Local Agent request, receives the sanitized observation receipt, adjudicates it against the technical contract and records the result in the Technical Receipt.

When the Engineering Delivery request includes deployment/runtime materialization, the Local Agent instruction must include the applicable post-deployment operational verification. A missing required Local Agent receipt or missing required post-deployment observation produces the Engineering Delivery blocker required by the frozen contract; it is not permission for Engineering Delivery to perform the local steps itself.

## Product Governance boundary

Product Governance may define and freeze which evidence bucket requires Local Agent execution, which deployment smoke/user-visible journey is applicable, whether browser operation is applicable, verify exact identity, and adjudicate only the buckets it owns. Product Governance does not execute local steps, repair candidates, or substitute CI output for required Local Agent observations.

Product Governance must not turn Local Agent post-deployment PASS into Product Experience PASS or Human Owner Acceptance.

## Historical evidence

Historical receipts from predecessor executor topologies or predecessor Local Agent contracts remain immutable evidence for their original exact SHA and gate. They do not provide prospective execution authority and must not be reused as PASS for a new candidate. Historical receipts are not retroactively invalidated solely because post-deployment verification became mandatory on 2026-09-09.

## Migration rule

Any active Goal/Milestone contract, project profile, governance lock, workflow, script, adapter or execution task that requires a different local executor must be superseded before the next local attempt. Any current Local Agent handoff that includes deployment/runtime materialization must include the post-deployment operational verification requirement before the next such local attempt.

Governance-only wording may be changed by Product Governance; technical workflow/script/configuration enforcement belongs to a separate Engineering Delivery context.

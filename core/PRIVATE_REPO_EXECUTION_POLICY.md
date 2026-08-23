# Private Repository Execution Policy

Version: 0.1.2-alpha

## Policy

For private product repositories governed by ChatGPT Parent PM:

- `GitHub` remains the control plane for branches, pull requests, workflow triggers, exact-SHA identity, receipts, and evidence.
- `GitHub Self-hosted Runner` on the project-owned machine is the primary execution plane.
- `GitHub-hosted Runner` is not a required dependency for private-repository Parent PM gates and must not be inserted as a mandatory preflight hop by default.
- `Local Agent` is an explicit out-of-band diagnostic executor for runner/bootstrap/control-plane failures or one-off diagnostics; it is not the default product execution plane and there is no silent fallback.
- Billing-dependent hosted execution is forbidden by default for private-repository acceptance gates unless the Human Owner explicitly opts in.
- GitHub Actions artifact storage is not a required dependency of the authoritative private execution gate; durable evidence stays under the project-owned local evidence root and validated receipt/evidence digests are surfaced in GitHub logs.

## Canonical private-runner framework authority

The Core publishes the exact executable framework authority in:

`core/PRIVATE_RUNNER_FRAMEWORK_AUTHORITY.json`

Consumers MUST pin the exact `framework_sha` from that authority file. A moving branch name or open PR head is not sufficient consumer authority. Existing consumer authority refs and receipts remain immutable; migration to a newer framework SHA requires a successor project authority/task rather than rewriting history.

For `0.1.2-alpha`, the canonical R2 framework authority is:

```text
FRAMEWORK_PR=12
FRAMEWORK_BRANCH=chatgpt/codex-harness-gateway-r1
FRAMEWORK_SHA=ea051b03bdf7bbccb3de447ccd36f8e17bd2d0f7
POLICY=PRIVATE_REPO_SELF_HOSTED_ONLY_R2
```

## Required execution chain

A private-repository technical gate SHOULD use one fail-closed self-hosted job in this order:

1. immutable task / workflow input validation;
2. expected runner identity and health validation;
3. exact candidate SHA and tree validation;
4. governance/static preflight;
5. dependency installation;
6. build and tests;
7. runtime/browser/product gate when required;
8. machine-readable terminal receipt and evidence manifest/digests.

Product execution MUST NOT start before steps 1–4 pass.

```text
FAIL_CLOSED=true
PRODUCT_ATTEMPT_STARTED=false until preflight PASS
```

## Private vs public repositories

- Private repository: self-hosted runner first; hosted runner is optional only by explicit Human Owner/project policy.
- Public repository: project policy may use GitHub-hosted runners, self-hosted runners, or local-agent execution as appropriate.

## Evidence rules

A self-hosted receipt must identify at minimum:

- repository;
- candidate SHA;
- candidate tree;
- workflow/run/job identity;
- `RUNNER_NAME`;
- expected runner labels;
- operating system and architecture;
- preflight result;
- product-attempt-started flag;
- test/runtime results;
- evidence paths or hashes;
- evidence transport mode.

Do not infer runner execution merely because a workflow exists. A project may claim self-hosted execution capability only after an accepted adapter/workflow exists and an actual job has executed on the expected runner.

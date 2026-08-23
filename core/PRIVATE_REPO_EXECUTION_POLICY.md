# Private Repository Execution Policy

Version: 0.1.1-alpha

## Policy

For private product repositories governed by ChatGPT Parent PM:

- `GitHub` remains the control plane for branches, pull requests, workflow triggers, exact-SHA identity, receipts, and evidence.
- `GitHub Self-hosted Runner` on the project-owned machine is the primary execution plane.
- `GitHub-hosted Runner` is not a required dependency for private-repository Parent PM gates and must not be inserted as a mandatory preflight hop by default.
- `Local Agent` is a fallback diagnostic executor for runner/bootstrap/control-plane failures or one-off diagnostics; it is not the default product execution plane.
- Billing-dependent hosted execution is forbidden by default for private-repository acceptance gates unless the Human Owner explicitly opts in.

## Required execution chain

A private-repository technical gate SHOULD use one fail-closed self-hosted job in this order:

1. immutable task / workflow input validation;
2. expected runner identity and health validation;
3. exact candidate SHA and optional tree validation;
4. governance/static preflight;
5. dependency installation;
6. build and tests;
7. runtime/browser/product gate when required;
8. machine-readable receipt and evidence manifest.

Product execution MUST NOT start before steps 1–4 pass.

```text
FAIL_CLOSED=true
PRODUCT_ATTEMPT_STARTED=false until preflight PASS
```

## Private vs public repositories

- Private repository: self-hosted runner first; hosted runner is optional only by explicit project policy.
- Public repository: project policy may use GitHub-hosted runners, self-hosted runners, or local-agent execution as appropriate.

## Evidence rules

A self-hosted receipt must identify at minimum:

- repository;
- candidate SHA;
- candidate tree when required;
- workflow/run/job identity;
- `RUNNER_NAME`;
- expected runner labels;
- operating system and architecture;
- preflight result;
- product-attempt-started flag;
- test/runtime results;
- evidence paths or hashes.

Do not infer runner execution merely because a workflow exists. A project may claim self-hosted execution capability only after an accepted adapter/workflow exists and an actual job has executed on the expected runner.

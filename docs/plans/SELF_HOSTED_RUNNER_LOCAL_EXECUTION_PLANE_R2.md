# Self-hosted Runner Local Execution Plane R2

Status: successor candidate to R1 for private consumer repositories.

## Decision

For private consumer repositories, GitHub remains the control plane and the repository-scoped Mac mini GitHub Actions Self-hosted Runner is the primary and required execution plane.

The private-runner technical gate MUST NOT require GitHub-hosted compute (`ubuntu-*`, `windows-*`, or GitHub-hosted `macos-*`) for preflight, validation, build, test, runtime, evidence generation, or receipt validation.

The private-runner technical gate also MUST NOT require GitHub Actions artifact storage. Durable task evidence remains under the repository-scoped local `evidence_root`; the workflow exposes the validated `RunnerExecutionReceipt` verdict plus receipt/terminal-manifest SHA-256 values in the GitHub job log. Artifact upload may be handled only by a separately authorized optional transport layer and is not part of the standard private execution Gate.

The fail-closed preflight and the authorized local technical task execute on the same repository-scoped self-hosted Runner lane. A task MUST NOT begin until contract, exact candidate identity, Runner scope, and health validation have passed.

## Control-plane / execution-plane split

GitHub provides:
- immutable refs, pull requests, issues, workflow orchestration, and logs;
- read-only repository token scope by default;
- dispatch/trigger identity and auditable run/job identifiers;
- terminal receipt verdict and evidence digests in job logs.

The dedicated Mac mini Self-hosted Runner provides:
- contract preflight;
- exact-SHA/tree verification;
- repository-specific local build/test/runtime execution;
- durable local evidence and RunnerExecutionReceipt generation;
- deterministic cleanup under the task contract.

GitHub-hosted compute and GitHub artifact storage are not required dependencies of the private consumer execution path.

## Local Agent fallback boundary

`RUNNER_PROFILE.authority.local_agent_fallback` remains `false` and the semantic validator MUST continue rejecting `true`.

A local Agent is not an automatic substitute for an unavailable or failed Runner job. It may be used only as an explicit out-of-band diagnostic/fallback lane under a new task and explicit authority. There is no silent fallback, no inheritance of a Runner execution request, and no conversion of Agent output into Runner PASS evidence.

## Fail-closed ordering

The standard private technical gate order is:

1. start on the exact repository-scoped Self-hosted Runner labels;
2. materialize/checkout the exact authorized candidate or immutable control inputs;
3. prove exact SHA/tree and clean source state;
4. validate RunnerProfile and LocalExecutionRequest;
5. acquire the host-global mutex;
6. emit and validate Runner health;
7. execute the tracked authorized task only after all preceding controls PASS;
8. validate the terminal local RunnerExecutionReceipt and emit its SHA-256/evidence-manifest digest into the GitHub job log;
9. release the host-global mutex in an `always()` path.

Any blocker before step 7 means the product/local task did not start. For a terminal BLOCKED receipt generated before exact source materialization, `source_clean=false/false` records that source clean evidence was not entered and MUST NOT be reclassified as a source-dirty defect. Once exact source transport has passed, clean pre/post evidence remains mandatory even for later failures.

## Version and isolation invariants

R2 does not relax any R1 isolation, data, network, Runner-version, or mutation constraints. Repository-specific Runner identity, work directory, task/evidence roots, secret scope, protected-resource registry, global mutex, and fail-closed authority remain mandatory.

Known-bad Runner versions remain project/framework-controlled and cannot be adopted through automatic self-update.

## Migration rule

Existing private consumer workflows that use a GitHub-hosted preflight should migrate by moving that preflight onto their repository-scoped Self-hosted Runner before the authorized task. Existing workflows that require `actions/upload-artifact` should migrate their authoritative evidence to the local `evidence_root` and expose validated receipt/evidence digests in logs. Historical frozen authority refs and receipts are immutable; a consumer whose frozen validator encodes an older topology or evidence transport must create a new successor authority instead of rewriting history.

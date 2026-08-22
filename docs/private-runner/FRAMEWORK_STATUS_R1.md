# Private Runner Framework status R1

The milestone plan remains `docs/plans/SELF_HOSTED_RUNNER_LOCAL_EXECUTION_PLANE_R1.md`. SRF1 and SRF2 now have remotely validated implementation source in Draft PR #16; consumer Runner registration and framework release remain separate future Gates.

Implemented source provides visibility/profile/request/attempt/health/update/protected-resource/material/failure/execution-receipt contracts, semantic fail-closed validation, negative fixtures and a private-repository workflow starter kit.

A pre-freeze review detected and corrected self-referential authority hashes. The current contract uses byte-level SHA-256 values computed outside the authority documents. The consumer workflow recomputes the exact `RunnerProfile`, `LocalExecutionRequest`, `MaterialManifest` and `ProtectedResourceRegistry` file hashes before local execution.

Consumer Project PMs may pin only the exact externally published validated framework SHA/ref. They still must produce repository-specific service/workdir/secret scope, fresh health/update, host mutex/protected-resource receipt, material authority, execution request/attempt and final Runner receipt.

`chatgpt-parent-pm` remains public and does not register a production Self-hosted Runner. Hosted CI success is framework-source evidence only.

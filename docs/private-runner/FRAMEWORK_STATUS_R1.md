# Private Runner Framework status R1

The planning document `docs/plans/SELF_HOSTED_RUNNER_LOCAL_EXECUTION_PLANE_R1.md` remains the milestone map. SRF1 and SRF2 now have validated implementation source in the dedicated successor Draft PR created from PR #12.

Implemented source includes Runner visibility/profile/request/attempt/health/update/resource/material/failure/execution-receipt contracts, semantic fail-closed validation, negative fixtures and a private repository workflow starter kit.

This is not the framework release and is not proof of any consumer Runner. Consumer Project PMs may pin only the exact externally published validated framework SHA/ref and must still produce repository-specific RunnerProfile, service/workdir/secret scope, fresh health/update, host mutex/protected-resource, material manifest, request/attempt and execution receipts.

`chatgpt-parent-pm` remains public and must not register a production Self-hosted Runner.

# PLAN — Private Runner Framework SRF1/SRF2 R1

1. Freeze live PR #12 / central PR #21 / ADR 0008+0009 / Lingxi consumer blocker.
2. Implement RunnerProfile, visibility, request, attempt, health/update, protected-resource, material, failure and execution-receipt contracts.
3. Implement semantic fail-closed validator and fixtures.
4. Implement private workflow starter with workflow_dispatch, repository labels, exact hashes, contents:read, full-SHA actions and evidence upload.
5. Add repository service, global mutex/protected-resource and rollback/revocation documentation.
6. Run hosted CI; do not use a Self-hosted Runner in this public repository.
7. Harden freshness, command, attempt/receipt and claim semantics.
8. Freeze exact validated framework source for consumer Project PM pinning.
9. Return consumer activation to Lingxi; actual Runner service/health remains consumer-local evidence.

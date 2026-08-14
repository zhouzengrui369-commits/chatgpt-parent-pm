# TASK — G2 architecture-boundary validator

## In scope

Architecture-boundary schema, three synthetic positive fixtures, six negative blockers, deviation ADR identity/expiry, validator/tests, CI and receipts.

## Prohibited

Consumer source/runtime changes, database migration, permissions/security Gate work, merge, release and product acceptance.

## Acceptance

Exact PR head passes G2 workflow, repository CI and G0/G1 regressions; every negative fixture returns its declared first blocker.

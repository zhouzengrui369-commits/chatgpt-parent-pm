# TASK — G1 v0.3 adoption schema

## In scope

- one versioned adoption JSON Schema;
- one exact shared-contract lock manifest;
- five synthetic product-role fixtures;
- five negative blocker fixtures;
- zero-dependency validator and transition checks;
- path-scoped CI and evidence.

## Prohibited

Consumer repository writes, private data, product runtime, deployment, credentials, merge, release and Human Owner claim uplift.

## Acceptance

Exact PR head passes validator CLI for every positive fixture, all negative blocker tests, repository test discovery and PR-base whitespace check. Existing PR #3 and G0 behavior remain green.

# Development Loop

## Phase A — Contract

Create a bounded Goal with user outcome, scope, exclusions, input identity, acceptance criteria, evidence requirements, and owner-locked decisions.

## Phase B — Remote implementation

ChatGPT modifies source and tests through GitHub, records verification, and freezes a candidate SHA.

## Phase C — Local deployment

A local agent reconstructs the candidate without source modification and returns build/start/runtime evidence.

## Phase D — Real-operation acceptance

A local test agent executes actual user tasks and failure paths on the deployed candidate.

## Phase E — Remediation

ChatGPT converts findings into focused source changes and a new candidate SHA. Completed gates are not rerun unless affected.

## Phase F — Owner acceptance

The owner decides customer value and any owner-locked action. Final acceptance binds to the exact final SHA.

# Separated Product Delivery Loop

## Phase A — Product Baseline

Product Governance confirms the authoritative product positioning, target user, core user problem, product boundaries, and risk tier.

## Phase B — Goal/Milestone Contract

Product Governance creates exactly one Goal for exactly one Milestone and freezes customer value, scope, required journeys, evidence, limitations, and closure conditions.

## Phase C — Engineering Delivery

A separate Engineering Delivery context implements source and tests, performs code review, commits and pushes, manages the PR, and emits an exact-SHA Candidate Manifest plus Technical Receipt. It may declare only `ENGINEERING_READY`.

## Phase D — Candidate Admission

Product Governance verifies exact identity, contract coverage, unapproved deviations, evidence completeness, and unresolved blockers. It declares `PRODUCT_REVIEW_ELIGIBLE=YES/NO` without changing source.

## Phase E — Local and Independent Review

The local execution layer deploys the authorized exact SHA and returns sanitized environment evidence. The Independent Product Experience Reviewer operates the real product against the frozen contract and publishes an independent verdict.

## Phase F — Remediation

Product Governance converts valid findings into the existing Goal's focused engineering remediation contract, unless an approved Change Request creates a successor Goal. Engineering Delivery authors the successor candidate. Completed unaffected gates need not be repeated.

## Phase G — Owner and Closure

The Human Owner grants any required acceptance/release authorization. Product Governance closes the Goal and Milestone together only after all required gates close.

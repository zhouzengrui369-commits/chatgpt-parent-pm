# Product Governance / Engineering Delivery Migration

## Decision

Starting with framework `0.2.0-alpha`, ChatGPT Parent PM becomes Product Governance. Source development, technical tests, commits, pushes, PRs, and candidate construction move to a separate Engineering Delivery skill and context.

## Mandatory invariants

1. One Goal equals one Milestone.
2. Product Governance does not author product source or test candidates.
3. Engineering Delivery does not rewrite Product Baseline or Goal/Milestone acceptance.
4. The same role cannot author and accept the same exact candidate.
5. Technical PASS never becomes Product Experience PASS by implication.
6. Material scope or acceptance changes require an approved Change Request.
7. Only a frozen exact candidate enters independent review or Human Owner Gate.

## Existing work

An in-flight candidate may remain technically valid, but its current author cannot independently product-accept it. Product Governance must first recover the authoritative baseline, map the work to one Goal/one Milestone, record any deviations, and decide whether the exact SHA is eligible for independent review.

Do not rewrite historic receipts. Apply the new model prospectively through a successor governance commit or Goal contract.

## Repository migration

Add a repository-level `AGENTS.md`, `governance/ECOSYSTEM_DELIVERY_POLICY.md`, Goal/Milestone and Change Request templates, and `delivery/CANDIDATE_MANIFEST_TEMPLATE.md`. Existing project baselines remain authoritative unless Product Governance explicitly supersedes them.

## New Engineering Delivery repository

The standalone target is `zhouzengrui369-commits/chatgpt-engineering-delivery`. Until the repository shell exists, the complete bootstrap source is maintained under `engineering-delivery-skill/` in this repository. Copy it without changing semantics, then pin its exact commit in each consumer repository.

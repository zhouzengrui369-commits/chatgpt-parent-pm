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

## Canonical Engineering Delivery authority

The standalone Engineering Delivery repository is established and validated:

```text
REPOSITORY=zhouzengrui369-commits/chatgpt-engineering-delivery
COMMIT=d63a0f6257438299eb86f204368ce74ff9170a72
TREE=62265b15b4c5e2fd5f8355e017b46e26e6d44ca7
SKILL_PATH=core/ENGINEERING_DELIVERY_SKILL.md
VALIDATION=PASS
```

The original bootstrap provenance is:

```text
SOURCE_REPOSITORY=zhouzengrui369-commits/chatgpt-parent-pm
SOURCE_COMMIT=b3e22fd990b91a28a4a706b0f70ab2bd31bf6e33
SOURCE_PATH=engineering-delivery-skill/
```

Each consumer repository must replace any provisional bootstrap reference with the standalone repository, exact commit, exact tree, and skill path. Moving branch references are forbidden. Pinning the skill does not authorize engineering: Product Governance must first reconcile and freeze the Product Baseline and exactly one Goal/Milestone Contract.

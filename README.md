# ChatGPT Product Governance

[简体中文](README.zh-CN.md)

A repository-native governance framework that separates Product Governance, Engineering Delivery, Local Execution, Independent Product Experience Review, and Human Owner authority.

## Canonical lifecycle

```text
Product Governance freezes one Goal/Milestone Contract
→ separate Engineering Delivery
→ ENGINEERING_READY + exact SHA + Candidate Manifest + Technical Receipt
→ Product Governance Candidate Admission
→ Product Governance PRODUCT_REVIEW_ELIGIBLE
→ Independent Product Experience Review
→ Human Owner Gate
→ contract-defined release
→ Product Governance Goal/Milestone closure
```

Every state has one decision owner. No role may emit another role's state.

## Non-equivalence

```text
TECHNICAL_PASS
!= ENGINEERING_READY
!= CANDIDATE_ADMITTED
!= PRODUCT_REVIEW_ELIGIBLE
!= PRODUCT_EXPERIENCE_PASS
!= HUMAN_OWNER_ACCEPTED
!= RELEASE_AUTHORIZED
!= GOAL_MILESTONE_CLOSED
```

## Core authority

- Product Governance: `core/PARENT_PM_SKILL.md`
- Machine state model: `core/DELIVERY_STATE_MACHINE.json`
- Engineering Delivery exact authority: `core/ENGINEERING_DELIVERY_AUTHORITY.json`
- Candidate Admission: `contracts/CANDIDATE_ADMISSION.md`
- Product Review referral: `contracts/PRODUCT_REVIEW_REFERRAL.md`

Version: `0.3.0-alpha`.

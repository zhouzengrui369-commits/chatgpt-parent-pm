# Changelog

## 0.4.0-alpha — 2026-09-21

- Make Human Owner Acceptance a contract-defined conditional gate.
- Default pre-1.0 development Goals to Independent Product Experience validation without routine Human Owner acceptance.
- Require explicit Human Owner acceptance for the exact 1.0 final candidate.
- Add a narrow governance-only gate-policy Change Request class that can preserve exact-candidate Engineering/Candidate/PX states when product meaning and bytes are unchanged.
- Add durable preservation-receipt requirements and forbid synthesizing Human Owner acceptance.

## 0.3.0-alpha — 2026-09-04

- Introduce machine-readable `DELIVERY-LIFECYCLE-1.0`.
- Make `ENGINEERING_READY` an Engineering Delivery-owned atomic exact-candidate package.
- Separate Candidate Admission from Product Review eligibility.
- Assign every evidence item to a single role-owned gate.
- Define Local Executor output as observation-only.
- Add fail-closed invalidation for candidate, contract and role/context drift.
- Add Candidate Admission, Product Review referral, Engineering Delivery handoff and state-transition receipts.
- Upgrade the canonical Engineering Delivery authority to `0.2.0-alpha`.
- Forbid ambiguous cross-gate aliases such as milestone-ready, product-ready, delivery-complete and release-ready.

## 0.2.0-alpha — 2026-09-03

- Split Product Governance from standalone Engineering Delivery.
- Enforce one Goal equals one Milestone.

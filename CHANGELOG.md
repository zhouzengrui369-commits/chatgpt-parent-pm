# Changelog

## 0.3.1-alpha — 2026-09-07

- Establish ecosystem-wide `GITHUB=CONTROL_PLANE_ONLY` execution topology.
- Forbid GitHub-hosted Runner and self-hosted Runner as project CI/deployment/runtime execution surfaces.
- Make the Owner-authorized Local Agent the sole local execution/deployment surface.
- Clarify that `CI` means the repeatable contracted technical gate set, not GitHub Actions specifically.
- Remove Runner billing/minutes as a universal product or engineering prerequisite.
- Deprecate the self-hosted Runner adapter prospectively while preserving historical receipts.

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

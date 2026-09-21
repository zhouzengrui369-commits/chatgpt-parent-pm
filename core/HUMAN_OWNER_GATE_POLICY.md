# Human Owner Gate Policy

Version: 1.0
Applies to: DELIVERY-LIFECYCLE-1.0

## Purpose

Protect Human Owner time for product-direction decisions and final product acceptance, while keeping development-stage product validation owned by Engineering Delivery and Independent Product Experience Review.

## Version-horizon rule

```text
PRE_1_0_DEVELOPMENT
→ HUMAN_OWNER_ACCEPTANCE_REQUIRED=NO by default

1_0_FINAL_PRODUCT_CANDIDATE
→ HUMAN_OWNER_ACCEPTANCE_REQUIRED=YES

POST_1_0_MAJOR_OWNER_DECISION
→ contract-defined
```

For pre-1.0 Goals/Milestones, Product Experience Review is the normal product-experience gate. The Human Owner may still intervene for a major product tradeoff, sensitive/irreversible authority, or an explicitly escalated Owner decision, but the Owner is not the routine development tester.

A 1.0 final candidate must not close without explicit Human Owner acceptance bound to that exact candidate.

## Intermediate development closure

A pre-1.0 Goal/Milestone may close after all contract-required gates are satisfied when:

- Candidate Admission is complete;
- Product Review eligibility is complete;
- Independent Product Experience has issued PRODUCT_EXPERIENCE_PASS;
- no contract-required Engineering/Product Experience blocker remains;
- Human Owner acceptance is not required by the contract;
- release authorization is either not required or separately satisfied.

Closure does not imply final product acceptance, release readiness, real-device validation, or production authority.

## Owner exploratory feedback

Human Owner exploratory use before 1.0 is optional and must not be scheduled as routine milestone testing.

If the Human Owner voluntarily observes a product defect or product-direction problem before 1.0:

- preserve the observation as Owner product input;
- Product Governance classifies it against the frozen baseline/contract;
- Engineering/Product Experience own correction and revalidation;
- do not require the Human Owner to repeatedly retest development candidates unless the Owner explicitly requests it.

## Governance-only gate-policy correction

A frozen contract normally invalidates downstream states when changed. A narrow exception is allowed for a governance-only gate-policy correction when **all** of the following are true:

1. the exact product candidate SHA/tree is unchanged;
2. target user, user problem, customer value, product boundary, required journeys, acceptance outcomes/thresholds, evidence ownership, security tier and allowed limitations are unchanged;
3. no product source/test/build/runtime mutation is required;
4. the only change is required-gate/closure metadata implementing an explicit Human Owner governance directive;
5. Product Governance records an approved Change Request;
6. Product Governance records a preservation receipt enumerating each preserved exact-candidate state/evidence reference;
7. no preserved state is relabeled or upgraded beyond its original authority.

When these conditions hold:

```text
ENGINEERING_READY
CANDIDATE_ADMITTED
PRODUCT_REVIEW_ELIGIBLE
PRODUCT_EXPERIENCE_PASS
```

may remain valid for the same exact candidate.

Human Owner Acceptance cannot be synthesized or preserved if it never occurred.

## Contract requirements

Every Goal/Milestone Contract must declare:

```yaml
version_horizon: PRE_1_0 | FINAL_1_0 | POST_1_0
owner_acceptance_policy:
  mode: DELEGATED_TO_PRODUCT_EXPERIENCE | HUMAN_OWNER_FINAL_REQUIRED | EXPLICIT_OWNER_GATE
required_gates:
  human_owner_acceptance: true | false
```

Rules:

- `FINAL_1_0` requires `HUMAN_OWNER_FINAL_REQUIRED` and `human_owner_acceptance: true`.
- `PRE_1_0` defaults to `DELEGATED_TO_PRODUCT_EXPERIENCE` and `human_owner_acceptance: false`.
- Product Governance may not downgrade a 1.0 final Owner gate to save time or bypass a failed Owner decision.

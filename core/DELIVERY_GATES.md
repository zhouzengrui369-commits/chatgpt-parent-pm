# Delivery Gates

One Goal equals one Milestone. Gate ownership is separated so no implementation author can self-accept the product candidate.

| State / Gate | Authority | Minimum proof |
|---|---|---|
| `BASELINE_FROZEN` | Product Governance | Versioned Product Baseline and Project Profile |
| `MILESTONE_CONTRACT_FROZEN` | Product Governance | One Goal/Milestone contract with value, scope, journeys, evidence and closure conditions |
| `ENGINEERING_READY` | Engineering Delivery | Technical tests/checks and declared implementation scope |
| `CANDIDATE_FROZEN` | Engineering Delivery submits; Product Governance verifies identity | Exact SHA/tree, PR head, Candidate Manifest, Technical Receipt |
| `PRODUCT_REVIEW_ELIGIBLE` | Product Governance | Contract coverage, no unapproved baseline deviation, complete required evidence |
| `PRODUCT_EXPERIENCE_PASS` | Independent Product Experience Reviewer | Real-product user-task verdict bound to exact SHA |
| `HUMAN_OWNER_ACCEPTED` | Human Owner | Explicit Owner acceptance bound to exact SHA and contract |
| `RELEASE_AUTHORIZED` | Human Owner or explicitly delegated release authority | Explicit authorization and target environment |
| `MILESTONE_CLOSED` | Product Governance | Every required gate closed; Goal and Milestone close together |

`TECHNICAL_PASS`, `PRODUCT_EXPERIENCE_PASS`, `HUMAN_OWNER_ACCEPTED`, and `RELEASE_AUTHORIZED` are distinct states. No single green gate implies another.

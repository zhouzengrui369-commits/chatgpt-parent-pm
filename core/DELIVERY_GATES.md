# Delivery Gates — Role-Owned State Machine

Protocol: `DELIVERY-LIFECYCLE-1.0`

One Goal equals one Milestone. Every gate has exactly one decision owner.

| State / decision | Sole authority | Required proof | Explicitly does not prove |
|---|---|---|---|
| `BASELINE_FROZEN` | Product Governance | Exact Product Baseline reference | Engineering or product acceptance |
| `GOAL_MILESTONE_CONTRACT_FROZEN` | Product Governance | Exact contract commit/tree/path and evidence-ownership matrix | Candidate readiness |
| `ENGINEERING_READY` | Engineering Delivery | Atomic exact SHA/tree/parent + Candidate Manifest + Technical Receipt + complete engineering-required evidence | Candidate Admission, Product Review eligibility, Product Experience |
| `CANDIDATE_ADMITTED` | Product Governance | Admission record bound to exact candidate/contract, admission evidence complete, no unapproved deviation | Product Review eligibility or Product Experience |
| `PRODUCT_REVIEW_ELIGIBLE` | Product Governance | Candidate admitted, review runtime/artifact identity, review evidence complete, reviewer independence, referral | Product Experience PASS |
| `PRODUCT_EXPERIENCE_PASS/FAIL/BLOCKED` | Independent Product Experience Reviewer | Code-blind real-product verdict bound to exact candidate/runtime | Human Owner Acceptance or release |
| `HUMAN_OWNER_ACCEPTED/BLOCKED` | Human Owner | Explicit Owner decision bound to exact candidate/contract | Release unless contract says so |
| `RELEASE_AUTHORIZED` | Contract-defined release authority | Explicit target/environment authorization | Goal close by itself |
| `GOAL_MILESTONE_CLOSED` | Product Governance | Every contract-required gate closed | — |

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

## Fail-closed rules

- Missing required fields or evidence means the current transition is blocked.
- Candidate identity change invalidates all states from Engineering Ready onward.
- Contract change invalidates the Engineering Delivery handoff and all downstream states.
- One role cannot emit another role's state.
- The candidate author cannot admit or independently review the same candidate.
- Local Executor output is observation evidence, not a technical or product verdict.

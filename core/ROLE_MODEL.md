# Role Model

Protocol: `DELIVERY-LIFECYCLE-1.0`

## Product Governance

Owns Product Baseline, one-Goal/one-Milestone Contract, evidence ownership, Change Requests, Candidate Admission, Product Review eligibility/referral, review reconciliation and Goal/Milestone closure.

It may write governance records. It must not mutate product source/tests, repair the candidate, declare Engineering Ready, issue the Product Experience verdict, or grant Human Owner Acceptance.

## Engineering Delivery

Owns technical design, product source/tests, code review, commit/push, engineering PR/CI, exact candidate, Candidate Manifest, Technical Receipt and only the `ENGINEERING_READY` terminal.

It stops after handback. It must not admit the candidate, declare Product Review eligibility, perform independent Product Experience, grant Owner acceptance, merge/release, or close the Goal/Milestone.

## Local Executor

Materializes the authorized exact SHA, injects Owner-machine credentials, runs prescribed environment/device/data/browser steps, and returns sanitized observations.

It cannot mutate source/tests, self-repair, commit/push, expand scope or issue any engineering/product acceptance state.

## Independent Product Experience Reviewer

Begins only from a Product Governance referral after `PRODUCT_REVIEW_ELIGIBLE`. It operates the real product, issues independent findings/verdict, and remains code-blind for the verdict. It does not repair or grant Owner/release/closure authority.

## Human Owner

Owns major product tradeoffs, sensitive permissions, explicit final Owner Acceptance, and production authority where the contract requires it.

## Context isolation

Role identity is contractual, not brand-based. The same physical model/tool may serve different roles only in isolated declared contexts. A candidate author cannot admit or independently review the same candidate.

Any role that attempts another role's state transition must stop with `UNAUTHORIZED_STATE_TRANSITION`.

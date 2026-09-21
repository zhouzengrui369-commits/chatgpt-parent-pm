# Goal / Milestone Contract

> One Goal equals one Milestone. Product Governance owns and freezes this contract. Engineering Delivery implements it without changing product meaning.

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
goal_id: GOAL-XXX
milestone_id: MILESTONE-GOAL-XXX
relationship: ONE_GOAL_EQUALS_ONE_MILESTONE
status: DRAFT | FROZEN | SUPERSEDED | CLOSED
version_horizon: PRE_1_0 | FINAL_1_0 | POST_1_0

owner_acceptance_policy:
  mode: DELEGATED_TO_PRODUCT_EXPERIENCE | HUMAN_OWNER_FINAL_REQUIRED | EXPLICIT_OWNER_GATE

product_baseline:
  version: ""
  ref: ""

product_governance:
  role: PRODUCT_GOVERNANCE
  context_id: ""

target_user: ""
user_problem: ""
customer_value: ""
in_scope: []
out_of_scope: []
required_user_journeys: []
acceptance_outcomes: []
allowed_known_limitations: []

evidence_ownership:
  engineering_required: []
  admission_required: []
  review_required: []
  product_experience: []
  human_owner: []

security_tier:
  users: SINGLE_USER | LIMITED_GROUP | MULTI_USER_PUBLIC
  exposure: LOCAL | PRIVATE_NETWORK | INTERNET
  data: LOW | PERSONAL | SENSITIVE | HIGHEST
  reversibility: REVERSIBLE | PARTLY_REVERSIBLE | IRREVERSIBLE
  automation_authority: OBSERVE | SUGGEST | OWNER_CONFIRMED_WRITE | AUTONOMOUS_WRITE

owner_locked_decisions: []
engineering_allowed_paths: []
engineering_forbidden_paths: []

required_gates:
  candidate_admission: true
  product_review_eligibility: true
  product_experience: true
  human_owner_acceptance: false
  release_authorization: false

closure_conditions: []
change_request_required_for:
  - target_user
  - customer_value
  - product_boundary
  - required_user_journey
  - acceptance_outcome_or_threshold
  - evidence_bucket_or_class
  - security_tier
  - allowed_limitation
  - closure_condition

frozen_at: ""
frozen_commit: ""
frozen_tree: ""
contract_path: ""
```

Every required evidence item must appear in exactly one evidence bucket. Missing or duplicate ownership is a blocking contract defect.

Human Owner gate rules:
- `PRE_1_0` defaults to `DELEGATED_TO_PRODUCT_EXPERIENCE` and `human_owner_acceptance: false`.
- `FINAL_1_0` must use `HUMAN_OWNER_FINAL_REQUIRED` and `human_owner_acceptance: true`.
- An intermediate Owner gate may be added only when the frozen contract explicitly requires it for a major tradeoff or sensitive authority.

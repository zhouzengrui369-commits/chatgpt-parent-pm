# Goal / Milestone Contract

> One Goal equals one Milestone. Product Governance owns and freezes this contract. Engineering Delivery implements it without changing its product meaning.

```yaml
goal_id: GOAL-XXX
milestone_id: MILESTONE-GOAL-XXX
relationship: ONE_GOAL_EQUALS_ONE_MILESTONE
status: DRAFT | FROZEN | SUPERSEDED | CLOSED
baseline_version: ""
product_governor: ""
engineering_delivery_handoff: ""
target_user: ""
user_problem: ""
customer_value: ""
in_scope: []
out_of_scope: []
required_user_journeys: []
acceptance_outcomes: []
required_product_evidence: []
required_technical_evidence: []
allowed_known_limitations: []
security_tier:
  users: SINGLE_USER | LIMITED_GROUP | MULTI_USER_PUBLIC
  exposure: LOCAL | PRIVATE_NETWORK | INTERNET
  data: LOW | PERSONAL | SENSITIVE | HIGHEST
  reversibility: REVERSIBLE | PARTLY_REVERSIBLE | IRREVERSIBLE
owner_locked_decisions: []
engineering_allowed_paths: []
engineering_forbidden_paths: []
required_gates:
  product_experience: true
  human_owner_acceptance: true
  release_authorization: false
closure_conditions: []
change_request_required_for:
  - target_user
  - customer_value
  - product_boundary
  - required_user_journey
  - acceptance_threshold
  - evidence_class
  - security_tier
  - closure_condition
frozen_at: ""
frozen_commit: ""
```

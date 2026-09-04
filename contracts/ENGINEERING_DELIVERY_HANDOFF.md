# Engineering Delivery Handoff

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
actor_role: PRODUCT_GOVERNANCE
actor_context_id: ""

product_baseline_ref: ""
goal_id: ""
milestone_id: ""
relationship: ONE_GOAL_EQUALS_ONE_MILESTONE

product_contract:
  commit: ""
  tree: ""
  path: ""

engineering_delivery_authority:
  repository: zhouzengrui369-commits/chatgpt-engineering-delivery
  commit: ""
  tree: ""
  skill_path: core/ENGINEERING_DELIVERY_SKILL.md

engineering_delivery_context_id: ""
engineering_delivery_contract_ref: ""

preimage:
  repository: ""
  branch: ""
  sha: ""
  tree: ""
  parent: ""

allowed_paths: []
forbidden_paths: []
approved_change_requests: []

evidence_ownership:
  engineering_required: []
  admission_required: []
  review_required: []
  product_experience: []
  human_owner: []

required_return:
  - engineering_terminal
  - candidate_manifest
  - technical_receipt

forbidden_engineering_claims:
  - CANDIDATE_ADMITTED
  - PRODUCT_REVIEW_ELIGIBLE
  - PRODUCT_EXPERIENCE_PASS
  - HUMAN_OWNER_ACCEPTED
  - MERGE_AUTHORIZED
  - RELEASE_AUTHORIZED
  - GOAL_MILESTONE_CLOSED
```

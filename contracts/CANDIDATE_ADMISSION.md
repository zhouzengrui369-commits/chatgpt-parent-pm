# Product Governance Candidate Admission Record

Candidate Admission is separate from Engineering Ready and Product Review eligibility.

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
actor_role: PRODUCT_GOVERNANCE
actor_context_id: ""

goal_id: ""
milestone_id: ""
input_state: ENGINEERING_READY
output_state: CANDIDATE_ADMITTED | CANDIDATE_REJECTED | CANDIDATE_ADMISSION_BLOCKED

product_contract:
  commit: ""
  tree: ""
  path: ""

candidate:
  repository: ""
  pr: ""
  branch: ""
  sha: ""
  tree: ""
  parent: ""
  branch_head_match: false
  pr_head_match: false

engineering_ready_terminal_ref: ""
candidate_manifest_ref: ""
technical_receipt_ref: ""

checks:
  exact_identity_verified: false
  contract_coverage_verified: false
  engineering_required_evidence_complete: false
  admission_required_evidence_complete: false
  approved_change_requests_complete: false
  unapproved_product_deviations: []
  known_defects_within_contract: false
  author_acceptor_independence: false

decision_reason: ""
first_blocker: ""
candidate_mutated_by_product_governance: false
product_experience_claimed: false
human_owner_acceptance_claimed: false
issued_at: ""
```

Product Governance must not repair or complete the candidate during admission.

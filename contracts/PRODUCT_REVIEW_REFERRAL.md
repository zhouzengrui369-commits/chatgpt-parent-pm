# Product Review Eligibility and Referral

This record is created only after Candidate Admission.

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
actor_role: PRODUCT_GOVERNANCE
actor_context_id: ""

goal_id: ""
milestone_id: ""
input_state: CANDIDATE_ADMITTED
output_state: PRODUCT_REVIEW_ELIGIBLE | PRODUCT_REVIEW_NOT_ELIGIBLE | PRODUCT_REVIEW_ELIGIBILITY_BLOCKED

product_contract:
  commit: ""
  tree: ""
  path: ""

candidate_sha: ""
candidate_tree: ""
candidate_admission_ref: ""

review_runtime_or_artifact:
  identity: ""
  exact_candidate_match: false
  reachable: false

review_required_evidence:
  status: COMPLETE | INCOMPLETE
  refs: []

independent_reviewer:
  role: INDEPENDENT_PRODUCT_EXPERIENCE_REVIEWER
  context_id: ""
  did_not_author_candidate: false
  did_not_technically_gate_candidate: false
  did_not_admit_candidate: false
  code_blind_for_verdict: false

review_baseline_refs: []
required_product_journeys: []
known_open_findings: []
claim_ceiling:
  human_owner_acceptance: false
  merge_release: false
  goal_milestone_close: false

first_blocker: ""
issued_at: ""
```

The referral supplies product authority and exact identity. It must not pre-write or constrain the independent verdict.

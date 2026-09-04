# State Transition Receipt

Every lifecycle transition must use a durable receipt.

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
goal_id: ""
milestone_id: ""
actor_role: PRODUCT_GOVERNANCE | ENGINEERING_DELIVERY | LOCAL_EXECUTOR | INDEPENDENT_PRODUCT_EXPERIENCE_REVIEWER | HUMAN_OWNER | CONTRACT_DEFINED_RELEASE_AUTHORITY
actor_context_id: ""
input_state: ""
output_state: ""
product_contract_commit: ""
candidate_sha: ""
candidate_tree: ""
evidence_refs: []
forbidden_claims_acknowledged: true
issued_at: ""
```

A receipt is invalid when the actor does not own `output_state`, exact identities are missing or moving, required evidence is incomplete, or author/acceptor independence is violated.

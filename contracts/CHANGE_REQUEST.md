# Change Request

```yaml
change_request_id: CR-XXX
goal_id: GOAL-XXX
milestone_id: MILESTONE-GOAL-XXX
requester_role: PRODUCT_GOVERNANCE | ENGINEERING_DELIVERY | REVIEWER | OWNER
change_class: PRODUCT_MEANING_CHANGE | GOVERNANCE_ONLY_GATE_POLICY_CHANGE
current_contract_commit: ""
reason: ""
proposed_change: ""
product_value_impact: ""
required_journey_impact: ""
risk_and_security_impact: ""
schedule_impact: ""
alternatives_considered: []
product_governance_decision: PENDING | APPROVED | REJECTED
decision_reason: ""
decision_commit: ""
preserve_existing_candidate_states: false
preservation_criteria_refs: []
```

Engineering difficulty, architecture preference, or test failure does not itself amend the contract. Until Product Governance approves this record, the frozen Goal/Milestone Contract remains authoritative.

A `GOVERNANCE_ONLY_GATE_POLICY_CHANGE` may preserve existing exact-candidate Engineering/Candidate/Review states only when every criterion in `core/HUMAN_OWNER_GATE_POLICY.md` is satisfied and Product Governance writes a durable preservation receipt. It cannot change product meaning or synthesize Human Owner acceptance.

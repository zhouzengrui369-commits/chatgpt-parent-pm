# Goal-Driven Development

## One Goal = One Milestone

A Goal is one bounded, evidence-bearing product-value increment or one explicitly declared governance prerequisite. Each Goal creates exactly one Milestone, and the Goal and Milestone close together.

A task, PR, sprint, phase label, or defect list is not automatically a Goal. Multiple unrelated outcomes must not be bundled to simplify reporting.

Every Goal/Milestone Contract defines:

- `goal_id` and `milestone_id` with a one-to-one mapping;
- baseline version and target user;
- user problem and customer value;
- in-scope and out-of-scope behavior;
- required user journeys and acceptance outcomes;
- product and technical evidence classes;
- allowed known limitations;
- security/risk tier proportional to actual exposure;
- owner-locked decisions;
- exact closure conditions and required gates;
- allowed and forbidden paths for Engineering Delivery where needed.

Product Governance freezes the contract. Engineering Delivery implements it and may not silently redefine it. Material changes require an approved Change Request.

A Goal is not complete at `ENGINEERING_READY`. It closes only at `MILESTONE_CLOSED`, after every gate required by its frozen contract has reached PASS or `NOT_REQUIRED_BY_CONTRACT`.

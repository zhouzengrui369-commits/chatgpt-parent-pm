# Role Model

## Remote Parent PM + Coding Agent

Owns outcome translation, project planning, source integration, test integration, GitHub state, and remediation.

## Local Deployment Agent

Owns environment reconstruction and exact-SHA runtime startup. It produces a deployment receipt, not a source patch.

## Local Test Agent

Owns real-operation validation against user tasks and failure modes. It produces reproducible findings linked to the tested SHA.

## Product Experience Auditor

Evaluates discoverability, feedback, terminology, accessibility, recovery, and customer value. This can be the same local agent as the test agent, but its verdict remains a separate gate.

## Owner

Owns product tradeoffs, sensitive permissions, real data, financial actions, signing, notarization, production release, and final acceptance.

## Separation rule

One physical tool may implement multiple roles, but each action must declare which role and authority it is exercising. Role identity is contractual, not brand-based.

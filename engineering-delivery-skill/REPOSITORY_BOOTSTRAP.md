# Standalone Repository Bootstrap

Target repository: `zhouzengrui369-commits/chatgpt-engineering-delivery`

Create the repository as public unless the Human Owner selects private. Copy the contents of this directory to repository root while preserving paths and semantics. Add the same Apache-2.0 license used by `chatgpt-parent-pm`, then create an initial release candidate tagged only after validation.

Required validation before consumers pin it:

- README and core skill agree on authority boundaries;
- one Goal = one Milestone is enforced in every contract;
- no file grants Product Governance authority to write source/tests;
- no file grants Engineering Delivery authority to alter baseline or product-accept a candidate;
- Candidate Manifest and Technical Receipt schemas are present;
- consumer repositories pin an exact commit rather than a moving branch.

# BACKWARD COMPATIBILITY PLAN

MODE=ADDITIVE_ONLY

- Existing `governance-lock` and `local-receipt` schemas are not renamed, removed or tightened in G0.
- PR #3 remains the protected Shared Capability Adoption lane and PR #4 is stacked on it.
- Geo Context exact identities and fixtures remain unchanged.
- G1 may add versioned v0.3 schemas; it must not reinterpret existing accepted receipts.
- Unknown or unsupported capabilities fail closed.
- A breaking change requires a separate decision record, migration path, fixtures and Human Owner authority.
- Consumer repositories remain independently owned and queued until their Project PM activates a local Goal.

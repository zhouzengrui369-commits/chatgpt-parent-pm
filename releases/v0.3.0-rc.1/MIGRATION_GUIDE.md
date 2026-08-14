# Parent PM ecosystem v0.3.0-rc.1 migration guide

STATUS=CANDIDATE_NOT_RELEASED

## Upgrade path

1. Keep the repository's current protected Goal and candidate unchanged.
2. Copy the G5 starter-kit templates into a new repository-local task.
3. Replace every placeholder with immutable SHA/SHA-256 identities.
4. Validate the adoption record against G1.
5. Declare architecture boundaries and deviations under G2.
6. Declare only synthetic or explicitly authorized grants under G3.
7. Bind worker actions and evidence claims to repository-local ownership under G4.
8. Run source, runtime, product-experience and Human Owner gates separately.

## Compatibility

- G0–G5 changes are additive.
- Existing governance-lock/local-receipt schemas and PR #3 Geo Context identities remain unchanged.
- Unknown capability, permission, ownership and evidence states fail closed.
- No consumer migration is automatic.

## Rollback

Remove the repository-local v0.3 task/records as a new reviewed change; do not rewrite accepted history or mutate a frozen candidate.

## Release boundary

This directory is a repository-tracked release candidate only. It is not a tag, GitHub Release, merged framework version or Human Owner acceptance.

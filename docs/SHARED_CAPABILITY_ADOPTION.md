# Shared Capability Adoption Contract

This contract extends ChatGPT Parent PM for cross-repository reusable capabilities such as `geo-context`, ASR, RAG, design systems, or future shared engines.

## Principle

A shared capability is not copied ad hoc into many repositories. One authority repository owns its specification/version; every consumer pins an exact authority commit and contract hash, then implements a project-specific adapter under its own Goal/release scope.

## Required lifecycle

1. **Discover** — record upstream/reference research and license boundary.
2. **Centralize contract** — capability authority publishes spec/schema/fixtures/validator.
3. **Freeze candidate** — exact authority SHA + contract/schema hash + CI receipt.
4. **Adoption decision** — each repository declares `ADOPT`, `PLAN_ONLY`, `OPTIONAL`, or `NO_ADOPTION` plus a mode.
5. **Capability lock** — consumer pins exact authority SHA/hash; never `latest`/moving main.
6. **Compatibility assessment** — map the central contract to project architecture, truth, privacy, safety and current release scope.
7. **Project Goal** — runtime code begins only from the consumer repository's own Goal/TASK/PLAN.
8. **Conformance + product tests** — shared contract tests do not replace project-specific tests.
9. **Exact-SHA local deployment/test** — real runtime/browser/device evidence where applicable.
10. **Independent experience review** — for material product surfaces.
11. **Human Owner Gate** — no automatic merge/release/customer-value approval.

## Required lock fields

```json
{
  "capability_id": "geo-context",
  "capability_version": "0.1.0",
  "authority_repository": "owner/repo",
  "authority_commit_sha": "40-hex",
  "contract_path": "path/to/schema-or-contract",
  "contract_sha256": "64-hex",
  "adoption_mode": "RUNTIME_PRIMARY|PLATFORM_CONSUMER|OUTPUT_CONSUMER|GOVERNANCE|REVIEW|PLAN_ONLY|OPTIONAL",
  "upstream_code_included": false
}
```

## Fail-closed conditions

Return `BLOCKED_CAPABILITY_IDENTITY_MISMATCH` when the authority repository, exact SHA, contract path/hash or declared capability version does not match the local lock.

Return `BLOCKED_CAPABILITY_SCOPE_NOT_AUTHORIZED` when a consumer attempts runtime implementation while its adoption profile is plan-only/optional or its current project Goal does not place the capability in release scope.

Return `BLOCKED_CAPABILITY_LICENSE_GATE` when direct upstream code/assets are introduced without the repository's explicit license decision and required notices.

## Upgrade

Capability upgrades are separate Goals. Never silently rewrite locks across repositories. Record compatibility evidence and project-specific migrations before moving the pin.

## Geo Context reference

First reference capability candidate:

- authority: `zhouzengrui369-commits/knowme-ecosystem`
- candidate SHA: `6edb5401084de24491038ac55525f584e9943bd7`
- GeoScene schema SHA-256: `8695f3d9d376bf5591138d78b1460c17758845312aeca52a4a0597ee873032df`

This reference is illustrative; product repositories still own their adoption and release decisions.

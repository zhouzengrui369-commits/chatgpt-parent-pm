# Shared Capability Adoption Contract

This contract extends ChatGPT Parent PM for cross-repository reusable capabilities such as `geo-context`, ASR, RAG, design systems, or future shared engines.

## Principle

A shared capability is not copied ad hoc into many repositories. One authority repository owns its specification/version; every consumer pins an exact authority commit and contract hash, then its **own Project PM** decides when and how to implement a project-specific adapter under that repository's Goal/release scope.

## Two-level PM model

### Ecosystem / capability PM

Owns:
- upstream/reference research and license boundary;
- central spec/schema/fixtures/validator/version;
- capability registry and compatibility rules;
- cross-project conformance feedback.

Does **not** own product delivery inside consumer repositories by default.

### Product Project PM

For each consumer repository, owns:
- release priority and activation timing;
- Goal/TASK/PLAN/RESULT/EVIDENCE creation;
- implementation-worker assignment;
- source integration and project test loop;
- exact-SHA candidate freeze;
- local deployment/test executor assignment;
- independent product-experience review assignment;
- finding triage and successor candidates;
- Human Owner/customer-value handoff.

A central capability planning PR must never be interpreted as authorization for the ecosystem PM to take over a consumer product's coding, local deployment, merge or release.

## Required lifecycle

1. **Discover** — ecosystem/capability PM records upstream/reference research and license boundary.
2. **Centralize contract** — capability authority publishes spec/schema/fixtures/validator.
3. **Freeze central candidate** — exact authority SHA + contract/schema hash + CI receipt.
4. **Adoption decision** — each product repository receives a planning-only adoption record owned by its Project PM.
5. **Capability lock** — consumer pins exact authority SHA/hash; never `latest`/moving main.
6. **Compatibility assessment** — project PM maps the central contract to project architecture, truth, privacy, safety and current release scope.
7. **Queue, do not hijack** — if a higher-priority Goal is active, the capability remains queued/deferred until the project PM promotes it.
8. **Project Goal** — runtime/output code begins only from the consumer repository's own active Goal/TASK/PLAN.
9. **Project implementation** — project PM assigns workers and owns source/test integration.
10. **Conformance + product tests** — shared contract tests do not replace project-specific tests.
11. **Exact-SHA candidate freeze** — project PM freezes one product candidate.
12. **Local deployment/test assignment** — project PM assigns MiniMax/Codex/other local executor according to the product's profile.
13. **Independent experience review** — project PM assigns real-operation review for material product surfaces.
14. **Successor loop** — scoped findings create a new candidate, not silent mutation of the frozen one.
15. **Human Owner Gate** — no automatic merge/release/customer-value approval.
16. **Feedback upstream** — only generic, reusable lessons are proposed back to the capability authority.

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

The local adoption profile should additionally identify `execution_owner: <project>-project-pm` for product repositories.

## Fail-closed conditions

Return `BLOCKED_CAPABILITY_IDENTITY_MISMATCH` when the authority repository, exact SHA, contract path/hash or declared capability version does not match the local lock.

Return `BLOCKED_CAPABILITY_SCOPE_NOT_AUTHORIZED` when a consumer attempts runtime implementation while its adoption profile is plan-only/optional or its current project Goal does not place the capability in release scope.

Return `BLOCKED_CAPABILITY_PM_OWNERSHIP_MISMATCH` when an ecosystem/capability-level executor attempts to implement, deploy or release a consumer product without that consumer Project PM's active Goal/assignment.

Return `BLOCKED_CAPABILITY_LICENSE_GATE` when direct upstream code/assets are introduced without the repository's explicit license decision and required notices.

## Upgrade

Capability upgrades are separate planning/adoption changes. Never silently rewrite locks across repositories. Each Project PM decides when to re-anchor and records compatibility evidence and project-specific migrations before moving the pin.

## Geo Context reference

First reference capability candidate:

- authority: `zhouzengrui369-commits/knowme-ecosystem`
- candidate SHA: `6edb5401084de24491038ac55525f584e9943bd7`
- GeoScene schema SHA-256: `8695f3d9d376bf5591138d78b1460c17758845312aeca52a4a0597ee873032df`

The reference defines a shared contract only. AOG, KnowMe, Lingxi, Copilot and ebook-miniapp are delivered by their own Project PMs.

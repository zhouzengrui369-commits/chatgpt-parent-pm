# EVIDENCE — Private Runner Framework SRF1/SRF2 R1

## Authority

```text
BASE_PR_12_SHA=a6968f771ab0274f042142d100ec446c0f641cf4
CENTRAL_PR_21_SHA=193acc0cd2437393f25641eba92085d75fffb063
ADR_0008=ACCEPTED
ADR_0009=ACCEPTED
LINGXI_BLOCKER=lingxi-presentation#90/#94
```

## Source chain

- Goal: `683900bd26adaa8b45a91c5372cbf9fa7306332c`.
- Initial implementation: `75a5712262615bb613fa0cd5b35fc868bbc37295`.
- Freshness/attempt/command hardening: `650aa0bda358754f2e3adc032d30ea5d4f046892`.
- First task closeout: `4285b7eeb71db7d5381e53efc45b3a966dc2f6da`.
- Pre-freeze self-reference defect correction: `3712e404a5c1614353183109692a25b6bc390644`.
- Draft framework PR: #16.

## Why the correction was required

The first schema shape placed a digest inside the same request/material/registry object that the digest was intended to identify. A real consumer cannot deterministically construct a byte-level self-hash. Parent PM detected this before immutable freeze and did not publish that shape as consumer authority.

Corrected design:

```text
RunnerProfile.json             -> external profile_sha256
LocalExecutionRequest.json     -> external request_sha256
MaterialManifest.json          -> external material_manifest_sha256
ProtectedResourceRegistry.json -> external protected_registry_sha256
```

The starter workflow recomputes all four file hashes with `shasum -a 256`; the request binds profile/material/registry hashes, and the final RunnerExecutionReceipt binds all four authority-file hashes.

## Corrected-source CI

`private-runner-framework` run `32546026270`, job `96964469056`:

- hosted Ubuntu runner only;
- `GITHUB_TOKEN` contents read;
- checkout full SHA pin, `persist-credentials: false`;
- JSON parse PASS;
- unittest 3/3 PASS;
- semantic self-test `positive=1 negative=18 PASS`;
- direct positive validation PASS;
- compile PASS;
- starter workflow safety PASS;
- four external authority-file hash checks found;
- no public Parent PM self-hosted Runner workflow PASS.

Existing repository CI run `32546026279`, job `96964469071`: PASS.

## Claim ceiling

No private consumer registration, service/workdir, health/update receipt, global mutex host receipt, product Candidate, Provider, Product Experience, Human Owner Gate, merge or release is proven here.

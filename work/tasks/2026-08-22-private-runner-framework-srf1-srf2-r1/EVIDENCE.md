# EVIDENCE — Private Runner Framework SRF1/SRF2 R1

## Authority

```text
BASE_PR_12_SHA=a6968f771ab0274f042142d100ec446c0f641cf4
CENTRAL_PR_21_SHA=193acc0cd2437393f25641eba92085d75fffb063
ADR_0008=ACCEPTED
ADR_0009=ACCEPTED
LINGXI_BLOCKER=lingxi-presentation#90/#94
```

## Source evidence

- Goal commit: `683900bd26adaa8b45a91c5372cbf9fa7306332c`.
- Initial implementation: `75a5712262615bb613fa0cd5b35fc868bbc37295`.
- Hardened implementation: `650aa0bda358754f2e3adc032d30ea5d4f046892`.
- Draft framework PR: #16.

## CI evidence

`private-runner-framework` run `32545818342`, job `96963927752`:

- hosted Ubuntu runner only;
- token permissions `contents: read`;
- checkout full SHA pin and `persist-credentials: false`;
- JSON parse PASS;
- unittest `3/3 PASS`;
- semantic self-test `positive=1 negative=18 PASS`;
- direct positive validation PASS;
- compile PASS;
- starter workflow safety PASS;
- public Parent PM no-self-hosted-runner guard PASS.

Existing repository `ci` run `32545818254`, job `96963927363`: PASS.

## Claim ceiling

No consumer Runner, service, workdir, health/update receipt, product Candidate, Provider, Product Experience, Human Owner Gate, merge or release is proven by this evidence.

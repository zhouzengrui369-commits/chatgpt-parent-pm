# Parent PM ecosystem v0.3 starter kit

Copy the seven templates into a consumer repository only after its repository-local Project PM activates a bounded Goal.

Rules:

- replace every `{{PLACEHOLDER}}`;
- use full immutable SHA and SHA-256 identities;
- retain the current protected Goal and candidate;
- do not place secrets, credentials, private data or absolute local paths in governance files;
- planning/source/fixture/runtime/product/Owner/merge/release receipts remain separate;
- templates do not authorize consumer implementation, deployment, merge or release.

Run:

```bash
python validators/validate_ecosystem_v03_starter_kit.py starter-kit/ecosystem-v03/template-manifest.json
```

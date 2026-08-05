# Delivery Gates

| Gate | Owner | Minimum proof |
|---|---|---|
| Contract | Parent PM | Accepted Goal with identity and scope |
| Code | Parent PM | Tests/build/checks against candidate SHA |
| GitHub delivery | Parent PM | remote branch Head = PR Head = candidate SHA |
| Local deployment | Local deployment agent | exact-SHA checkout/build/start receipt |
| Runtime | Local test agent | reproducible observed behavior |
| Product experience | Product auditor | user-task verdict and findings |
| Customer value | Owner | explicit acceptance bound to SHA |
| Release | Owner or delegated release agent | explicit authorization and release receipt |

No single green gate implies all other gates are green.

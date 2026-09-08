# Changelog

## 0.3.2-alpha

- canonicalize the ecosystem local execution role as `LOCAL_AGENT`; historical `OWNER_AUTHORIZED_LOCAL_AGENT` wording is non-authoritative prospectively;
- keep GitHub as control plane only and forbid GitHub-hosted/self-hosted Runner execution;
- clarify that local runtime-only technical secrets may be generated/stored by Local Agent under Engineering Delivery contract without a separate Human Owner confirmation when no external-account, billing, production or irreversible authority changes;
- reserve Human Owner authority for major product trade-offs, genuinely sensitive external permissions/credentials, payment/billing, production authority, irreversible actions and final Human Owner Acceptance;
- reinforce product-value-first, proportionate security and no redundant confirmation gates.

## 0.3.1-alpha

- added ecosystem no-Runner execution topology successor;
- defined GitHub as control plane and Local Agent as local execution surface;
- moved technical CI execution to Local Agent contracts while preserving technical gate strength.

## 0.3.0-alpha

- separated Product Governance from Engineering Delivery;
- formalized Candidate Admission and Product Review Eligibility as distinct Product Governance transitions;
- introduced exact Engineering Delivery authority pins and lifecycle state machine.

# Security Policy

## Supported versions

Only the latest tagged alpha or stable line is supported.

## Report privately

Do not open public issues containing credentials, private repository content, customer data, signing materials, or exploitable vulnerabilities.

## Framework safety defaults

- no secret retrieval by default
- no direct writes to protected branches
- no automatic merge
- no production deployment or release without owner authorization
- exact-SHA identity checks before local execution
- fail closed on dirty-state or scope overlap
- sanitize receipts before publishing

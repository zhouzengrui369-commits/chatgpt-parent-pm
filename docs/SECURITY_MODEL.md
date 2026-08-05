# Security Model

## Trust zones

- GitHub source and CI
- remote Parent PM session
- local deployment environment
- local test environment
- owner-only production and credential zone

## Main threats

- branch or SHA drift
- hidden local source modification
- malicious repository instructions
- secret leakage in logs or screenshots
- automatic destructive actions
- fabricated evidence
- testing a different artifact than the reviewed candidate

## Controls

- exact-SHA locks
- explicit allowed/forbidden paths
- clean/dirty-state checks
- least-privilege GitHub permissions
- sanitized receipts
- separate owner gates
- no automatic merge/release
- fail-closed local contracts

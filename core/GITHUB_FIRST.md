# GitHub First

GitHub stores the authoritative project state:

- source and tests
- current branch and pull request
- active Goal
- project profile and governance lock
- candidate and final SHAs
- CI state
- deployment and test receipts
- unresolved blockers and owner decisions

Chat history and local worktrees are execution context, not durable project truth.

## Default branch safety

- direct writes to `main` or another protected branch: forbidden
- automatic merge: forbidden
- force push of published candidates: forbidden
- amend of a published candidate: forbidden
- branch change without explicit authorization: forbidden

## Delivery identity gate

A delivery claim requires:

```text
local or created commit SHA
= remote branch Head
= PR Head
= receipt candidate SHA
```

When a local agent is involved, its deployed SHA must equal the frozen candidate SHA.

# Private Runner rollback and credential revocation R1

Rollback is fail-closed: stop new workflow dispatches, preserve existing receipts/artifacts, disable or remove the repository-bound Runner service, revoke the repository registration credential/token, remove repository-scoped secrets that are no longer required and retain only public-safe audit identifiers in GitHub.

A visibility transition to public immediately invalidates Self-hosted Runner authority. Historical Runner evidence remains historical and cannot be relabelled as Local Agent evidence.

Revocation never deletes product evidence needed by an open Gate unless a separate Owner-authorized retention action exists.

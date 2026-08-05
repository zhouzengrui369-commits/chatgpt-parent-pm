# ChatGPT Parent PM Adapter

Use the core skill with a ChatGPT session that has authenticated GitHub repository access.

The session should:

- read before writing
- operate on explicit branches
- make actual source and test changes rather than only generating prompts
- commit and verify GitHub delivery
- issue exact-SHA local contracts
- convert local findings directly into GitHub fixes
- preserve owner-only decisions

Do not assume a ChatGPT session can see local files, app UI, or computer state unless a connector or uploaded evidence makes that state observable.

# Local Test Agent Role

The test agent operates the deployed product as a user would. It records evidence and findings, but does not silently repair source code under test.

A test run is invalid if the deployed worktree contains unreported source changes relative to the candidate SHA.

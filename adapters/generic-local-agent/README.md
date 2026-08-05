# Generic Local Agent Adapter

Use this adapter for any local agent that can run shell commands or operate a GUI.

Required behavior:

1. verify repository, branch, exact SHA, upstream, and dirty state;
2. fail closed on mismatch;
3. avoid source changes;
4. run only the supplied deployment or test contract;
5. return a structured receipt;
6. sanitize secrets and private data.

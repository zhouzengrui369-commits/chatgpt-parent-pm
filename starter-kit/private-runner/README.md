# Private Runner starter kit

This public framework repository **does not register** a Self-hosted Runner. The starter kit is instantiated only by a **consumer private repository** under its Project PM authority.

Required consumer records: visibility receipt, RunnerProfile, LocalExecutionRequest, ExecutionAttempt, RunnerHealth/Update receipts, ProtectedResourceRegistry, MaterialManifest and RunnerExecutionReceipt.

The consumer must create a unique repository registration, service name, work directory, labels and secret scope. One Mac may host several repository-bound services, but a host-global mutex limits protected local execution to one attempt at a time.

No Local Agent fallback is implied. No Runner may mutate product source or repair locally. Failure is returned to Web ChatGPT Parent PM through GitHub logs/evidence and a fresh source/workflow/task authority creates the next attempt.

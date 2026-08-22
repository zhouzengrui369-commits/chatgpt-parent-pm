# Mac host mutex and protected resources R1

Before a protected task, the repository Runner must acquire the host-global mutex, read its repository-specific ProtectedResourceRegistry, snapshot owned and protected processes/ports and create a fresh attempt ownership manifest.

Forbidden: `killall`, `pkill -f`, wildcard process termination, killing a PID/PGID not proven to belong to the current attempt, using another repository's work/evidence directory, or treating a pre-existing process as the current attempt.

Terminal proof requires all current-attempt owned processes and ports to be gone or explicitly preserved by contract. Protected unrelated resources must remain unchanged.

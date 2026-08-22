# Repository-bound Runner service contract R1

Each private repository owns a distinct GitHub repository registration and Runner service. `service_name`, `work_dir`, `RunnerProfile`, capability label and repository secret scope must be unique to that repository. Registration tokens and repository credentials are never shared across product repositories.

The shared Mac host requires one global mutex and `MAX_CONCURRENT_LOCAL_EXECUTION=1` for protected product execution. A health receipt must bind repository, profile, service, workdir, labels, Runner version, macOS/arm64 and mutex availability before every protected Gate.

Runner failure never authorizes local source repair. Consumer workflow/script/source changes are made in GitHub by the repository Parent PM and require a new attempt ID.

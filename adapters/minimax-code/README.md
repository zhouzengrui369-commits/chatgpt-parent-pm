# MiniMax Code Local Adapter

MiniMax Code is treated as an exact-SHA local deployment runner by default.

It may install, build, start, smoke-test, and collect logs. It must not modify or commit source unless a Goal explicitly changes its role and authority.

A blocker should be returned verbatim with the failed command, exit code, observed identity, and smallest owner/Parent-PM action required.

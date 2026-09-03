# Role Model

## Human Owner

Owns product direction changes, sensitive permissions, production authorization, and final Human Owner Acceptance.

## ChatGPT Parent PM / Product Governance

Owns Product Baseline, Project Profile, one-Goal/one-Milestone contracts, prioritization, change control, candidate admission, review orchestration, release recommendation, and milestone closure. It may write governance records but must not author product source or test candidates.

## Engineering Delivery

Owns technical design, source implementation, technical tests, code review, commits, pushes, pull requests, CI remediation, exact-SHA candidate construction, Candidate Manifest, and Technical Receipt. It delivers exactly one frozen Goal/Milestone at a time unless Product Governance approves a Change Request.

## Local Execution Layer

A project Self-hosted Runner, Codex, or another local agent deploys the authorized exact SHA, injects local runtime credentials, executes prescribed environment-bound tests, and returns sanitized evidence. It does not modify source/tests or become the development owner.

## Independent Product Experience Reviewer

Evaluates the real product against the frozen baseline and milestone contract. It owns an independent product-experience verdict and does not inspect or modify implementation code.

## Authority rule

Role identity is contractual, not brand-based. One physical model or tool may serve different roles only in isolated conversations/contexts with separate authority inputs. The same context must not act as Product Governance and Engineering Delivery for the same Goal, and no role may author and accept the same candidate.

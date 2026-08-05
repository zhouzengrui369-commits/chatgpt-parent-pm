# Related Projects Landscape — 2026-08-05

## Scope

This scan looked for public GitHub projects covering one or more of:

- specification- or goal-driven AI development
- AI product-manager / architect / developer / QA role orchestration
- repository-native plans and quality gates
- remote or autonomous coding agents
- local execution, testing, and evidence workflows

Public GitHub does not expose reliable clone counts or real user-session frequency. Therefore **usage frequency cannot be measured directly**. This report uses public proxies:

- stars: awareness/interest, not verified adoption
- forks: experimentation and downstream customization
- releases and recency: maintenance cadence
- issues/PRs/contributors: community activity
- published integrations or telemetry: stronger adoption signals where available

Metrics are rounded public snapshots observed during research and can change.

## Closest projects

| Project | Main overlap | Public attention snapshot | Activity / usage proxy | Key difference from ChatGPT Parent PM |
|---|---|---:|---|---|
| `github/spec-kit` | Spec → Plan → Tasks → Implement; 35 agent integrations; governance extensions | 121K+ stars, about 9.9K forks, 240+ contributors | very high; active extension ecosystem, official docs list 138 extensions and 25 presets; PyPI distribution is current but public download count was not confirmed in this scan | focuses on agent-agnostic SDD; does not make remote ChatGPT the source integration owner while local agents are deploy/test executors |
| `Fission-AI/OpenSpec` | lightweight repository-native specifications and artifact workflow | about 62.3K stars, 4.3K forks | very high; roughly 275K–345K npm downloads/week across recent public snapshots, 24–25 dependents, active releases, optional anonymous command telemetry | specification alignment, not a remote/local authority and acceptance protocol |
| `bmad-code-org/BMAD-METHOD` | PM, architect, developer, QA and owner-like roles; agile workflows and skills | about 48.1K stars, 5.6K forks | high; roughly 15K–17K npm downloads/week in recent snapshots, 432 published npm versions, frequent releases | multi-role methodology commonly executed within agent tools; not exact-SHA remote-coder/local-runner separation |
| `buildermethods/agent-os` | project standards, better specs, agent alignment | about 4.7K stars, 740 forks | medium; 12 releases, latest major 3.0 in Jan 2026 | concentrates on standards injection and spec quality |
| `Gentleman-Programming/gentle-ai` | multi-agent installation, SDD, TDD, review, persistent memory, receipt-driven development | at least 3.4K stars; 400+ forks; 188+ releases in an earlier public snapshot | high release frequency; strong operational overlap | local agent ecosystem/orchestrator; ChatGPT is not the fixed remote integration authority |
| `dsifry/metaswarm` | 18 agents, skills, TDD, design/review gates, Codex/Claude/Gemini integrations | about 298 stars, 35 forks | emerging; 113 commits and 4 releases in snapshot | multi-agent orchestration inside coding environments, rather than remote/local separation |

## Adjacent projects

| Project | Main overlap | Public attention snapshot | Activity / usage proxy | Key difference |
|---|---|---:|---|---|
| `OpenHands/OpenHands` | remote/local software-agent runtime, sandboxed execution, coding and web/terminal operations | about 75K stars, 9.5K forks | very high; large PR/issue volume and many releases | agent runtime/platform, not primarily a governance contract for multiple external agents |
| `FoundationAgents/MetaGPT` | software-company metaphor with specialized multi-agent roles | about 68.8K stars, 8.8K forks | very high awareness; academic and community adoption | generates and coordinates agents internally; weaker focus on GitHub exact-SHA delivery evidence |
| `Pythagora-io/gpt-pilot` | end-to-end AI developer and task decomposition | about 33.8K stars, 3.5K forks | high historical attention; 500+ closed PRs in snapshot | coding-agent product, not a reusable governance layer separating remote and local authorities |
| `Agent-Field/SWE-AF` | product manager, architect, coder, reviewer and QA fleet shipping PRs | about 827 stars, 133 forks | emerging; no releases in snapshot | autonomous engineering runtime; more automation and less explicit human owner / local acceptance separation |

## Conclusion

There is a mature and highly visible market for:

- spec-driven development frameworks
- multi-agent software-company simulations
- autonomous coding runtimes
- local agent orchestrators

The proposed repository is **not category-unique at the broad workflow level**. Its defensible niche is the combination of:

1. ChatGPT as the default remote Parent PM and coding/integration authority;
2. local agents as exact-SHA deployment and real-operation acceptance executors;
3. GitHub as the only durable source of product truth;
4. explicit separation of code, runtime, product experience, customer value, and delivery gates;
5. forward-only remediation by the remote coding agent rather than repeated document handoff loops.

The closest design influences are Spec Kit, BMAD Method, Gentle-AI, and Agent OS. The repository should interoperate with these ideas rather than claim to replace them.


## Public sources checked

- https://github.github.com/spec-kit/index.html
- https://github.com/github/spec-kit
- https://github.com/Fission-AI/OpenSpec
- https://www.npmjs.com/package/@fission-ai/openspec
- https://github.com/bmad-code-org/BMAD-METHOD
- https://www.npmjs.com/package/bmad-method
- https://github.com/buildermethods/agent-os
- https://github.com/Gentleman-Programming/gentle-ai
- https://github.com/dsifry/metaswarm
- https://github.com/OpenHands/OpenHands
- https://github.com/FoundationAgents/MetaGPT
- https://github.com/Pythagora-io/gpt-pilot
- https://github.com/Agent-Field/SWE-AF

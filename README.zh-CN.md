# ChatGPT Parent PM — Product Governance

[English](README.md)

这是一个以 GitHub 为权威控制面的 AI 产品交付治理框架。自 `0.2.0-alpha` 起，原“Parent PM + Coding Agent”被正式拆分：

- **ChatGPT Parent PM / Product Governance**：负责产品基线、一个 Goal 对应一个 Milestone 的交付合同、优先级、变更控制、候选准入、独立审核编排、发布建议与里程碑关闭；不写产品源码和测试。
- **Engineering Delivery**：负责技术方案、源码、测试、代码审查、commit/push、PR、CI、exact-SHA 候选、Candidate Manifest 与 Technical Receipt；无权改变产品基线或宣布产品通过。
- **本地执行层**：Self-hosted Runner、Codex 或其他本地 Agent，只部署授权 exact SHA、注入本机凭据、执行真实设备/数据/浏览器测试并返回脱敏证据；不修改源码和测试。
- **独立产品体验审核官**：只操作真实产品，按冻结基线和里程碑合同给出独立体验结论，不看不改代码。
- **Human Owner**：负责重大取舍、敏感权限、生产授权和最终 Owner Acceptance。

## 核心规则

1. 一个 Goal = 一个 Milestone，二者同时关闭；
2. Product Governance 与 Engineering Delivery 必须使用隔离上下文；
3. 同一角色不得 author 并 accept 同一 exact candidate；
4. Technical PASS 不等于 Product Experience PASS；
5. 产品范围、核心旅程和验收条件变化必须经过 Change Request；
6. 只有冻结的 exact candidate 才能进入独立审核和 Human Owner Gate；
7. GitHub 是唯一权威事实源；
8. 安全按用户规模、暴露面、数据敏感度和可逆性分级，禁止以无关的企业级防线阻塞核心价值。

## 标准闭环

```text
Product Baseline
→ Goal/Milestone Contract
→ Engineering Delivery
→ ENGINEERING_READY
→ exact candidate + manifest/receipt
→ Product Governance admission
→ Independent Product Experience Review
→ Human Owner Gate
→ Release Authorization
→ Goal/Milestone Close
```

新 Engineering Delivery 独立仓库的完整启动源位于 `engineering-delivery-skill/`；角色迁移规则见 `docs/ROLE_SEPARATION_MIGRATION.md`。

> 社区开源项目，不是 OpenAI、Codex、GitHub 或其他厂商官方项目。

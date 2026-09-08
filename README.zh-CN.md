# ChatGPT Parent PM

AI 项目生态的中央 Product Governance 框架。

当前 successor 执行拓扑：

```text
GITHUB=CONTROL_PLANE_ONLY
GITHUB_HOSTED_RUNNER=FORBIDDEN
SELF_HOSTED_RUNNER=FORBIDDEN
LOCAL_EXECUTOR=LOCAL_AGENT
LOCAL_DEPLOYMENT=LOCAL_AGENT_ONLY
LOCAL_TECHNICAL_TEST_EXECUTION=LOCAL_AGENT
```

`LOCAL_AGENT` 是唯一规范的本地执行角色，不存在独立的 `OWNER_AUTHORIZED_LOCAL_AGENT` 生命周期角色。

Product Governance 负责产品基线、Goal/Milestone 合同、Change Request、候选准入和后续治理；Engineering Delivery 负责技术方案、源码、测试、PR、技术门和 Local Agent 执行合同；Local Agent 负责本地部署、技术执行和脱敏 observation。

安全遵循“产品价值优先、风险分级、逐步加固”。本地 runtime-only 技术配置（例如随机 JWT signing secret）在不涉及外部账号权限、支付、生产授权或不可逆操作时，由 Engineering Delivery + Local Agent 完成，不额外制造 Human Owner 确认门。

Human Owner 保留重大产品取舍、真正敏感的外部权限/账号、支付、生产授权、不可逆操作和最终 Human Owner Acceptance。

详见 `core/PARENT_PM_SKILL.md` 与 `core/ECOSYSTEM_EXECUTION_TOPOLOGY_POLICY.md`。

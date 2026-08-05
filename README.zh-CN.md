# ChatGPT Parent PM

[English](README.md)

这是一个面向任何项目、任何用户和任何 Agent 的开源 AI 软件开发治理框架：

- **ChatGPT**：远程父级 PM + Coding Agent，负责需求、Goal、源码、测试、Git 提交、PR、CI 和缺陷修复；
- **本地 Agent**：Codex、MiniMax Code 或其他可操作电脑的 Agent，负责精确 SHA 本地部署、构建、启动、真操作测试和验收证据；
- **Owner**：负责产品取舍、敏感权限、发布和最终客户价值验收。

> 社区开源项目，不是 OpenAI、Codex、MiniMax 或 GitHub 官方项目。

## 核心问题

传统 AI 开发容易把规划、写代码、本地部署、测试和审批混在一个长线程里，产生：

- 本地未提交代码成为隐形事实；
- Agent 声称完成但 GitHub 或 Runtime 不可复现；
- 多个 Agent 重复修改同一范围；
- 部署版本和测试版本不一致；
- 文档 PASS 被误当成产品 PASS。

本框架通过角色分离和精确 SHA 交接建立闭环。

## 标准闭环

```text
Owner确认结果
→ ChatGPT提交Goal合同
→ ChatGPT远程开发并提交GitHub
→ CI与代码Gate
→ 冻结候选SHA
→ 本地Agent部署精确SHA
→ 本地测试Agent真操作验收
→ 证据绑定候选SHA
→ ChatGPT直接修复并提交新SHA
→ focused redeploy/retest
→ Owner最终验收
→ 冻结Final Delivery SHA
```

## 八条核心规则

1. GitHub First；
2. 精确 SHA 交接；
3. ChatGPT 默认拥有远程源码集成权；
4. 本地 Agent 默认只部署和测试，不静默成为源码所有者；
5. Evidence Before Claims；
6. 默认禁止直接写 main；
7. 默认禁止自动 merge 和自动发布；
8. 分支、SHA、dirty 状态或范围不一致时 fail closed。

## 快速接入

```bash
cp -R starter-kit/. your-project/
cd your-project
python3 validators/validate_install.py .
```

随后配置项目自己的：

- `PROJECT_PROFILE.yaml`
- `GOVERNANCE_LOCK.json`
- `PROJECT_STATUS.md`
- 当前活动 Goal

详细说明见：[快速开始](docs/QUICKSTART.md)、[接入指南](docs/ADOPTION_GUIDE.md)。

## 当前版本

`v0.1.0-alpha`。至少经过一个外部项目完整闭环验证后，再发布 `v1.0.0`。

## 许可证

Apache License 2.0。

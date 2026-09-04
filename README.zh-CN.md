# ChatGPT Product Governance

这是一个仓库原生的产品治理框架，将 Product Governance、Engineering Delivery、本地执行、独立产品体验审核和 Human Owner 权限严格分离。

## 标准链路

```text
Product Governance 冻结一个 Goal/Milestone Contract
→ 独立 Engineering Delivery
→ ENGINEERING_READY + exact SHA + Candidate Manifest + Technical Receipt
→ Product Governance Candidate Admission
→ Product Governance 宣布 PRODUCT_REVIEW_ELIGIBLE
→ 独立 Product Experience Review
→ Human Owner Gate
→ 合同定义的 Release
→ Product Governance 关闭 Goal/Milestone
```

每个状态只有一个决策责任人，任何角色不得代替另一个角色宣布状态。

## 严格不等式

```text
TECHNICAL_PASS
!= ENGINEERING_READY
!= CANDIDATE_ADMITTED
!= PRODUCT_REVIEW_ELIGIBLE
!= PRODUCT_EXPERIENCE_PASS
!= HUMAN_OWNER_ACCEPTED
!= RELEASE_AUTHORIZED
!= GOAL_MILESTONE_CLOSED
```

## 权威入口

- Product Governance：`core/PARENT_PM_SKILL.md`
- 机器可读状态机：`core/DELIVERY_STATE_MACHINE.json`
- Engineering Delivery exact authority：`core/ENGINEERING_DELIVERY_AUTHORITY.json`
- Candidate Admission：`contracts/CANDIDATE_ADMISSION.md`
- 产品审核转交：`contracts/PRODUCT_REVIEW_REFERRAL.md`

版本：`0.3.0-alpha`。

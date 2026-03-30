# SWF 快速开始指南

5 分钟上手 SWF 需求分析系统。

---

## 1. 安装（1 分钟）

```bash
# 克隆仓库
git clone https://github.com/HeartFlying/swf.git
cd swf

# 启动 Claude Code
claude
```

---

## 2. 启动需求分析（2 分钟）

在 Claude Code 中输入：

```
我想开发一个时间管理 APP，帮我分析需求
```

SWF 会自动：
1. 触发 `coordinator-requirements` Agent
2. 执行 S001 制定 Plan
3. 评估信息完整度，选择执行模式
4. 按 S0→S1→S2→S3→S4 阶段执行
5. 完成后自动触发 `coordinator-architecture`（S5）
6. 完成后自动触发 `coordinator-detailed-design`（S6）

---

## 3. 跟随流程（自动）

每个 Skill 执行完成后，Claude 会询问：

```
【S2-S201 需求边界界定完成 - 用户评审】

核心内容：
- 产品边界：任务管理、番茄钟、学习统计
- 用户边界：18-25 岁大学生
- 场景边界：图书馆、宿舍、课堂

请评审：
- 输入「确认」继续
- 输入「修改：xxx」修改内容
- 输入「重做」重新执行
```

输入 `确认` 继续下一个 Skill。

---

## 4. 查看产物（1 分钟）

流程完成后，查看产物：

```bash
# 查看生成的文件结构
ls -la artifacts/

# 查看 Plan 定义
cat artifacts/plans/P000001.md

# 查看 S4 核心需求报告
cat artifacts/stages/s4/P000001-S4-S403-001.md

# 查看 S5 架构设计
cat artifacts/stages/s5/P000001/P000001-S5-A01-001.md

# 查看 S6 详细设计
cat artifacts/stages/s6/P000001/P000001-S6-A01-001.md

# 查看完整交付物
cat artifacts/plans/P000001/swf-deliverable.md
```

---

## 5. 常用命令

| 操作 | 指令 |
|------|------|
| 启动分析 | "帮我分析需求" |
| 确认继续 | 输入 `确认` |
| 修改内容 | 输入 `修改：具体意见` |
| 重新执行 | 输入 `重做` |
| 新增内容 | 输入 `新增：新需求描述` |
| 发起变更 | "我需要变更：新增积分功能" |

---

## 6. 示例对话

**完整示例：**

```
用户：我想做一个电商 APP

Claude：我将启动 SWF 需求分析流程...

[S001] Plan 制定完成
       Plan ID: P000001
       信息完整度: 65 分（常规模式）

请评审：确认

--- S1 市场洞察（常规模式执行）---

[S101] 竞品分析完成
       - 竞品：淘宝、京东、拼多多
       - 差异化：垂直领域电商

请评审：确认

[S102] 市场痛点验证完成
       - 痛点：正品保障、物流时效、售后服务

请评审：确认

--- S2 需求定义 ---

[S201] 需求边界界定完成
       - 产品：电商 APP（B2C）
       - 用户：18-45 岁消费者
       - 场景：移动端购物

请评审：确认

[S202] 显式需求提取完成
       - 商品浏览、搜索、购物车
       - 订单管理、支付、物流跟踪

请评审：确认

[S203] 隐性需求挖掘完成
       - 数据安全、隐私保护
       - 多端同步、离线浏览

请评审：确认

[S204] 需求验证完成
       - 一致性检查通过
       - 完整性验证通过

请评审：确认

--- S3 技术规划 ---

[S301-S304] 技术规划完成
       - 可行性：通过
       - 技术栈：React Native + Node.js + PostgreSQL
       - 风险：已识别 3 项风险

请评审：确认

--- S4 需求整合 ---

[S401-S406] 需求整合完成
       - 核心需求：15 项
       - 用户故事：28 个
       - 原型设计：8 个页面

请评审：确认

--- 阶段交接：触发架构设计 ---

[S5-A01] 架构愿景定义完成
       - 架构风格：分层架构 + 微服务
       - 核心原则：高可用、可扩展

请评审：确认

[S5-A02-S5-A06] 架构设计完成
       - 4+1 视图设计完成
       - 数据架构、接口架构、部署架构完成

请评审：确认

--- 阶段交接：触发详细设计 ---

[S6-A01-S6-A04] 详细设计完成
       - 模块设计：12 个模块
       - 数据库：25 张表
       - UI/UX：15 个页面
       - 测试策略：单元测试 + 集成测试 + E2E

请评审：确认

=== SWF 流程完成 ===

最终产物：
- artifacts/plans/P000001.md（Plan 定义）
- artifacts/plans/P000001/swf-deliverable.md（完整交付物）
- artifacts/stages/s0-s6/（各阶段产物）
```

---

## 7. 三阶段流程概览

| 阶段 | 协调器 | Skill 数量 | 产出 |
|------|--------|-----------|------|
| S0-S4 | coordinator-requirements | 14 个 | 需求规格说明书 |
| S5 | coordinator-architecture | 6 个 | 架构设计文档 |
| S6 | coordinator-detailed-design | 4 个 | 详细设计文档 |

**自动衔接**：S4 完成后自动触发 S5，S5 完成后自动触发 S6。

---

## 8. Roadmap 导航

使用 Roadmap 快速定位产物：

```bash
# 1. 查看全局索引
cat artifacts/roadmap/index.yaml

# 2. 查看 Plan 进度
cat artifacts/roadmap/plans/P000001/roadmap.yaml

# 3. 查看阶段产物索引
cat artifacts/roadmap/stages/s4-summary.yaml
```

---

## 下一步

- 项目概览：[README.md](README.md)
- 完整流程：[WORKFLOW.md](WORKFLOW.md)
- 部署指南：[DEPLOYMENT.md](DEPLOYMENT.md)

---

**开始您的第一次需求分析吧！**

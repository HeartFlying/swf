# SWF (Software WorkFlow)

<div align="center">

[![Version](https://img.shields.io/badge/version-3.2.0-blue.svg)](https://github.com/HeartFlying/swf)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![AI IDE](https://img.shields.io/badge/AI%20IDE-Claude%20Code%20%7C%20Codex%20%7C%20Trae-orange.svg)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

**AI 驱动的软件需求分析系统 - 从模糊需求到清晰方案**

</div>

---

## 📖 项目简介

SWF 是一个 AI 驱动的软件需求分析系统，采用 **三阶段协调器 Agent + Skill 架构**，帮助用户从原始、模糊的需求描述出发，系统化地梳理、分析和验证需求，最终输出结构化、可执行的设计文档。

### 核心特性

- 🎯 **三阶段流程**：需求分析 → 架构设计 → 详细设计，完整覆盖软件设计全流程
- 🤖 **智能推导**：基于需求特征自动推导架构方案和设计方案
- 📝 **标准化输出**：所有产物均为 Markdown 格式，便于版本管理和协作
- 🔄 **双模式执行**：常规模式（深度分析）和轻量化模式（快速输出）
- ✅ **用户评审机制**：每个 Skill 输出后支持用户确认和修改
- 🛡️ **变更管理**：支持需求变更的智能增量更新
- 🗺️ **Roadmap 导航**：全局产物索引，支持 AI 工具快速导航

---

## 🚀 快速开始

### 前置要求

- Claude Code、Codex 或 Trae 等 AI IDE
- 将仓库克隆到本地

```bash
git clone https://github.com/HeartFlying/swf.git
cd swf
```

### 使用方式

在 AI IDE 中直接描述你的需求：

```
我想开发一个在线教育平台，帮我分析需求
```

系统将自动启动需求分析流程，完成 S0-S4 后自动触发架构设计（S5）和详细设计（S6）。

---

## 📊 系统架构

### 三阶段协调器架构

```
用户需求输入
      ↓
┌─────────────────────────────────────────────────────┐
│ coordinator-requirements (需求分析协调器)             │
│ S0: Plan制定 → S1: 市场洞察 → S2: 需求定义            │
│ → S3: 技术规划 → S4: 需求整合                         │
│ 共 16 个 Skill                                       │
└─────────────────────────────────────────────────────┘
      ↓ 阶段交接
┌─────────────────────────────────────────────────────┐
│ coordinator-architecture (架构设计协调器)             │
│ S5: 架构愿景 → 视图设计 → 数据架构                     │
│ → 接口架构 → 部署架构 → 验证                          │
│ 共 6 个 Skill                                        │
└─────────────────────────────────────────────────────┘
      ↓ 阶段交接
┌─────────────────────────────────────────────────────┐
│ coordinator-detailed-design (详细设计协调器)          │
│ S6: 模块设计 → 数据库设计 → UI/UX设计 → 测试策略       │
│ 共 4 个 Skill                                        │
└─────────────────────────────────────────────────────┘
      ↓
完整交付物（需求规格书 + 架构文档 + 详细设计 + DDL + UI规范）
```

### Skill 清单（26 个工作流 Skill）

| 阶段 | Skill ID | 名称 | 轻量化跳过 |
|------|----------|------|-----------|
| **S0** | S001 | Plan 制定 | - |
| **S1** | S101 | 竞品分析 | ✓ |
| **S1** | S102 | 市场痛点验证 | ✓ |
| **S2** | S201 | 需求边界界定 | - |
| **S2** | S202 | 显性需求提取 | - |
| **S2** | S203 | 隐性需求挖掘 | ✓ |
| **S2** | S204 | 需求验证 | - |
| **S3** | S301 | 技术可行性评估 | - |
| **S3** | S302 | 技术选型 | - |
| **S3** | S303 | 非功能需求定义 | - |
| **S3** | S304 | 风险识别 | - |
| **S4** | S401 | 需求分类梳理 | - |
| **S4** | S402 | 需求优先级排序 | - |
| **S4** | S403 | 核心需求提炼 | - |
| **S4** | S405 | 用户故事编写 | - |
| **S4** | S406 | 原型设计 | ✓ |
| **S5** | S5-A01 | 架构愿景定义 | - |
| **S5** | S5-A02 | 架构视图设计 | - |
| **S5** | S5-A03 | 数据架构设计 | - |
| **S5** | S5-A04 | 接口架构设计 | - |
| **S5** | S5-A05 | 部署架构设计 | - |
| **S5** | S5-A06 | 架构验证与评审 | - |
| **S6** | S6-A01 | 模块详细设计 | - |
| **S6** | S6-A02 | 数据库详细设计 | - |
| **S6** | S6-A03 | UI/UX设计 | - |
| **S6** | S6-A04 | 测试策略设计 | - |
| **CM** | CM-001 | 变更影响分析 | 按需 |

**总计**：26 个工作流 Skill + 1 个变更管理 Skill = **27 个 Skill**

---

## 📂 目录结构

```
swf/
├── agents/                         # Agent 定义
│   ├── coordinator-requirements.md # 需求分析协调器 (S0-S4)
│   ├── coordinator-architecture.md # 架构设计协调器 (S5)
│   └── coordinator-detailed-design.md # 详细设计协调器 (S6)
├── skills/                         # 27 个 Skill 定义
│   ├── s0-plan/                    # S001: Plan 制定
│   ├── s1-competitor/              # S101: 竞品分析
│   ├── s1-market-analysis/         # S102: 市场验证
│   ├── s2-boundary/                # S201: 需求边界
│   ├── s2-explicit/                # S202: 显式需求
│   ├── s2-implicit/                # S203: 隐式需求
│   ├── s2-validation/              # S204: 需求验证
│   ├── s3-feasibility/             # S301: 技术可行性
│   ├── s3-selection/               # S302: 技术选型
│   ├── s3-nfr/                     # S303: 非功能需求
│   ├── s3-risk/                    # S304: 风险识别
│   ├── s4-classify/                # S401: 需求分类
│   ├── s4-priority/                # S402: 优先级排序
│   ├── s4-core/                    # S403: 核心需求提取
│   ├── s4-user-stories/            # S405: 用户故事
│   ├── s4-prototype/               # S406: 原型设计
│   ├── s5-vision/                  # S5-A01: 架构愿景
│   ├── s5-views/                   # S5-A02: 架构视图
│   ├── s5-data/                    # S5-A03: 数据架构
│   ├── s5-interface/               # S5-A04: 接口架构
│   ├── s5-deployment/              # S5-A05: 部署架构
│   ├── s5-validation/              # S5-A06: 架构验证
│   ├── s6-module/                  # S6-A01: 模块详细设计
│   ├── s6-database/                # S6-A02: 数据库详细设计
│   ├── s6-uiux/                    # S6-A03: UI/UX设计
│   ├── s6-test-strategy/           # S6-A04: 测试策略设计
│   └── cm-impact-analysis/         # CM-001: 变更影响分析
├── WORKFLOW.md                     # 主工作流程文档
├── CLAUDE.md                       # Claude Code 项目指引
└── README.md                       # 本文件
```

---

## 🔄 执行模式

系统根据信息完整度评分自动选择执行模式：

| 模式 | 触发条件 | 执行 Skill 数 | 特点 |
|------|---------|--------------|------|
| **常规模式** | 评分 < 90 | 26 个 | 深度分析，完整执行 |
| **轻量化模式** | 评分 ≥ 90 | 22 个 | 快速输出，跳过 4 个 Skill |

### 轻量化模式跳过的 Skill

| 阶段 | 跳过 Skill | 说明 |
|------|-----------|------|
| S1 | S101, S102 | 竞品分析、市场验证 |
| S2 | S203 | 隐性需求挖掘 |
| S4 | S406 | 原型设计 |

### 信息完整度评分维度

| 维度 | 权重 | 评估内容 |
|------|------|----------|
| 需求清晰度 | 30% | 需求描述是否明确、具体 |
| 边界完整性 | 25% | 产品边界、用户范围是否清晰 |
| 技术约束 | 25% | 技术栈、平台约束是否明确 |
| 业务背景 | 20% | 业务场景、目标是否清晰 |

---

## 📋 输出产物

### 产物存储结构

```
artifacts/
├── roadmap/                       # 全局 Roadmap（AI 工具导航）
│   ├── index.yaml                 # 全局索引
│   ├── stages/                    # 阶段产物索引
│   └── plans/                     # Plan 级 Roadmap
├── plans/
│   ├── {PlanID}.md                 # Plan 定义文件
│   └── {PlanID}/
│       ├── todo-list.md            # 主任务跟踪 (S0-S4)
│       ├── todo-list-s5.md         # S5 阶段任务跟踪
│       ├── todo-list-s6.md         # S6 阶段任务跟踪
│       ├── dependency-graph.md     # 需求依赖图谱
│       └── swf-deliverable.md      # 完整交付物
├── stages/
│   ├── s0/ ... s6/                 # 各阶段产物
└── change-management/              # 变更管理产物
```

### 最终交付物

完成 S0-S6 全流程后，系统输出：

1. **需求规格说明书** - 完整的功能和非功能需求文档
2. **架构设计文档** - 系统架构、技术选型、部署方案
3. **详细设计文档** - 模块设计、数据库设计、UI/UX 设计
4. **可执行的 DDL 脚本** - 数据库创建脚本
5. **UI/UX 设计规范** - 界面设计规范和组件清单
6. **测试策略文档** - 测试策略、测试用例规划

---

## ✅ 用户评审机制

每个 Skill 执行完成后触发用户评审：

```
【{阶段}-{Skill} 完成 - 用户评审】

产物已完成，核心内容如下：
- 结果1
- 结果2

---
请评审以上结果：
- 输入「确认」表示无误，继续执行下一阶段
- 输入「修改」并提供修改意见
- 输入「新增」补充新内容
- 输入「重做」重新执行当前 Skill
```

---

## 🛠️ 变更管理

工作流完成后，支持需求变更的智能增量更新：

### 变更触发方式

```
"我需要变更：新增积分体系功能"
"修改架构：引入消息队列"
```

### 变更执行策略

| 影响等级 | 影响系数 | 执行策略 |
|---------|---------|---------|
| 轻度 | < 3 | 仅重执行当前阶段 |
| 中度 | 3-8 | 重执行当前及后续阶段 |
| 重度 | > 8 | 全量重执行 |

---

## 🗺️ Roadmap 导航

Roadmap 是全局产物索引，用于 AI 工具快速定位产物：

```
1. 读取 artifacts/roadmap/index.yaml → 获取全局概览
2. 读取 artifacts/roadmap/plans/{PlanID}/roadmap.yaml → 获取 Plan 详情
3. 读取 artifacts/roadmap/stages/s{n}-summary.yaml → 获取阶段产物索引
4. 按需加载具体产物
```

---

## 📚 关键文档

| 文档 | 说明 |
|------|------|
| [WORKFLOW.md](WORKFLOW.md) | 完整工作流程文档 |
| [CLAUDE.md](CLAUDE.md) | Claude Code 项目指引 |
| [agents/](agents/) | Agent 定义文件 |
| [skills/](skills/) | Skill 定义文件 |

---

## 🔗 参考资源

- [Claude Agent Skills 官方文档](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [ISO/IEC 25010 质量标准](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010)

---

## 📌 版本信息

- **当前版本**: v5.1.0
- **最后更新**: 2026-04-14
- **适用 AI IDE**: Claude Code, Codex, Trae

---

## 📄 许可证

MIT License

---

<div align="center">

**SWF v5.1.0** - 让需求分析更智能、更高效

</div>

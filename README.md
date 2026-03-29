# SWF (Software WorkFlow)

<div align="center">

[![Version](https://img.shields.io/badge/version-3.2.0-blue.svg)](https://github.com/HeartFlying/swf)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![AI IDE](https://img.shields.io/badge/AI%20IDE-Claude%20Code%20%7C%20Codex%20%7C%20Trae-orange.svg)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

**AI 驱动的软件需求分析系统 - 从模糊需求到清晰方案**

</div>

---

## 📖 项目简介

SWF 是一个 AI 驱动的软件需求分析系统，采用 **Agent + Skill 架构**，帮助用户从原始、模糊的需求描述出发，系统化地梳理、分析和验证需求，最终输出结构化、可执行的设计文档。

### 核心特性

- 🎯 **渐进式引导**：从需求收集到详细设计的完整流程
- 🤖 **智能推导**：基于需求特征自动推导架构方案和设计方案
- 📝 **标准化输出**：所有产物均为 Markdown 格式，便于版本管理和协作
- 🔄 **双模式执行**：常规模式（深度分析）和轻量化模式（快速输出）
- ✅ **用户评审机制**：每个阶段输出后支持用户确认和修改
- 🛡️ **变更管理**：支持需求变更的智能增量更新

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

系统将自动启动需求分析流程。

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
└─────────────────────────────────────────────────────┘
      ↓
┌─────────────────────────────────────────────────────┐
│ coordinator-architecture (架构设计协调器)             │
│ S5: 架构愿景 → 视图设计 → 数据架构                     │
│ → 接口架构 → 部署架构 → 验证                          │
└─────────────────────────────────────────────────────┘
      ↓
┌─────────────────────────────────────────────────────┐
│ coordinator-detailed-design (详细设计协调器)          │
│ S6: 模块设计 → 数据库设计 → UI/UX设计 → 测试策略       │
└─────────────────────────────────────────────────────┘
      ↓
完整交付物（需求规格书 + 架构文档 + 详细设计 + DDL + UI规范）
```

### Skill 阶段概览

| 阶段 | Skill 数量 | 核心职责 |
|------|-----------|----------|
| **S0** - Plan 制定 | 1 | 需求解析、ID生成、信息完整度评分 |
| **S1** - 市场洞察 | 2 | 竞品分析、市场验证（轻量化模式跳过） |
| **S2** - 需求定义 | 4 | 边界界定、显式需求、隐式需求、需求验证 |
| **S3** - 技术规划 | 4 | 可行性分析、技术选型、非功能需求、风险识别 |
| **S4** - 需求整合 | 5 | 分类、优先级、核心提取、用户故事、原型设计 |
| **S5** - 架构设计 | 6 | 愿景、视图、数据、接口、部署、验证 |
| **S6** - 详细设计 | 4 | 模块、数据库、UI/UX、测试策略 |

**总计**：27 个 Skill（26 个工作流 Skill + 1 个变更管理 Skill）

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
├── templates/                      # 输出模板
│   ├── user-interaction/           # 用户交互模板
│   ├── quality-standard.md         # ISO/IEC 25010 质量标准
│   ├── error-code-standard.md      # 统一错误码标准
│   └── skill-structure-reference.md # Skill 结构参考
├── WORKFLOW.md                     # 主工作流程文档
├── CLAUDE.md                       # Claude Code 项目指引
└── README.md                       # 本文件
```

---

## 🔄 执行模式

系统根据信息完整度评分自动选择执行模式：

| 模式 | 触发条件 | 特点 | 跳过的 Skill |
|------|---------|------|-------------|
| **常规模式** | 评分 < 90 | 深度分析，完整执行 | 无 |
| **轻量化模式** | 评分 ≥ 90 | 快速输出，跳过非必要 Skill | S101, S102, S203, S406 |

### 信息完整度评分维度

| 维度 | 权重 | 评估内容 |
|------|------|----------|
| 需求清晰度 | 25% | 需求描述是否明确、完整 |
| 功能完整性 | 25% | 功能需求是否覆盖核心场景 |
| 用户定义 | 20% | 目标用户是否清晰定义 |
| 约束条件 | 30% | 技术、时间、预算约束是否明确 |

---

## 📋 输出产物

### 产物存储结构

```
artifacts/
├── plans/
│   ├── {PlanID}.md                 # Plan 定义文件
│   └── {PlanID}/
│       ├── todo-list.md            # 主任务跟踪
│       ├── todo-list-s5.md         # S5 阶段任务跟踪
│       ├── todo-list-s6.md         # S6 阶段任务跟踪
│       ├── dependency-graph.md     # 需求依赖图谱
│       └── swf-deliverable.md      # 完整交付物
└── stages/
    ├── s0/ ... s6/                 # 各阶段产物
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
【{Skill名称} 完成 - 用户评审】

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

| 影响范围 | 执行策略 |
|---------|---------|
| 仅 S4 | 重执行 S4 相关 Skill |
| S4 + S5 | 重执行 S4 + S5 |
| 全量影响 | 重执行 S4 + S5 + S6 |

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

- **当前版本**: v3.2.0
- **最后更新**: 2026-03-29
- **适用 AI IDE**: Claude Code, Codex, Trae

---

## 📄 许可证

MIT License

---

<div align="center">

**SWF v3.2.0** - 让需求分析更智能、更高效

</div>

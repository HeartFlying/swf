# SWF (Software WorkFlow)

AI驱动的软件需求分析工作流系统，通过多阶段Skill编排，将模糊的用户需求转化为结构化、可执行的需求规格说明。

## 核心特性

- **多阶段分析流程**：S0(Plan制定) → S1(需求边界) → S2(市场校验) → S3(技术选型) → S4(需求整合) → S5(架构设计) → S6(详细设计)
- **双执行模式**：根据信息完整度自动推荐常规模式(23个Skill)或轻量化模式(17个Skill)
- **用户评审机制**：每个Skill输出后触发用户评审，确保质量可控
- **断点续跑支持**：自动保存执行状态，支持随时暂停和恢复
- **标准化输出**：所有产物采用统一格式，便于后续开发使用

## 快速开始

```bash
git clone https://github.com/HeartFlying/swf.git
cd swf
claude
```

然后输入：`帮我分析一个 APP 的需求`

### 详细文档

- [快速开始](QUICKSTART.md) - 5 分钟上手
- [安装指南](INSTALL.md) - 详细安装步骤
- [部署指南](DEPLOYMENT.md) - 团队发布与共享
- [工作流程](WORKFLOW.md) - 完整流程说明

### 前置要求

- Claude Code、Codex 或 Trae 等AI IDE
- Git仓库克隆到本地

### 使用步骤

1. **启动协调器Agent**
   ```
   在AI IDE中加载 agents/swf-coordinator.md
   ```

2. **输入需求**
   ```
   向Agent描述你的软件需求
   ```

3. **确认执行模式**
   ```
   Agent会自动评分并推荐执行模式
   ```

4. **逐阶段执行**
   ```
   每个Skill完成后会触发评审，确认后继续
   ```

5. **获取最终报告**
   ```
   所有阶段完成后输出完整需求分析报告
   ```

## 目录结构

```
swf/
├── agents/
│   └── coordinator-requirements.md  # 主协调Agent
├── skills/                      # 23个Skill定义
│   ├── s0-plan/SKILL.md         # S001: Plan制定
│   ├── s1-boundary/SKILL.md     # S101: 需求边界
│   ├── s1-explicit/SKILL.md     # S102: 显式需求
│   ├── s1-implicit/SKILL.md     # S103: 隐性需求
│   ├── s1-validation/SKILL.md   # S104: 需求验证
│   ├── s2-competitor/SKILL.md   # S201: 竞品分析
│   ├── s2-market-analysis/      # S202: 市场验证
│   ├── s3-risk/SKILL.md         # S301: 风险识别
│   ├── s3-feasibility/SKILL.md  # S302: 技术可行性
│   ├── s3-selection/SKILL.md    # S303: 技术选型
│   ├── s4-classify/SKILL.md     # S401: 需求分类
│   ├── s4-priority/SKILL.md     # S402: 需求优先级
│   ├── s4-core/SKILL.md         # S403: 核心需求提取
│   └── s4-prototype/SKILL.md    # S404: 原型设计
│   ├── s5-architecture-generic/ # S501-S505: 架构设计阶段
│   └── s6-detailed-design-generic/ # S601-S604: 详细设计阶段
├── templates/                   # 标准模板
│   ├── quality-standard.md      # 质量评估标准
│   ├── error-code-standard.md   # 错误代码标准
│   ├── artifact-specifications.md # 产物规范
│   └── execution-flow-standard.md # 执行流程标准
├── .trae/progress/              # 进度跟踪
├── CLAUDE.md                    # 项目指导文档
├── WORKFLOW.md                  # 工作流程文档
└── srs.md                       # 系统需求规格
```

## 执行模式

### 常规模式 (Normal)
- **触发条件**：信息完整度评分 < 90分
- **执行所有23个Skill**：S001 → S101-S104 → S201-S202 → S301-S303 → S401-S404 → S501-S505 → S601-S604
- **适用场景**：需求不明确，需要全面分析

### 轻量化模式 (Lightweight)
- **触发条件**：信息完整度评分 ≥ 90分
- **执行17个Skill**：S001 → S101-S102-S104 → S301-S303 → S401-S404 → S501-S505 → S601-S604
- **跳过Skill**：S103(隐性需求)、S201(竞品分析)、S202(市场验证)
- **适用场景**：需求明确，快速输出核心需求

## 产物输出

所有产物存储在 `artifacts/` 目录：

```
artifacts/
├── plans/{PlanID}/
│   ├── {PlanID}-definition.md   # Plan定义
│   └── todo-list.md             # 任务跟踪
└── stages/
    ├── s0/{PlanID}/             # S0阶段产物
    ├── s1/{PlanID}/             # S1阶段产物
    ├── s2/{PlanID}/             # S2阶段产物
    ├── s3/{PlanID}/             # S3阶段产物
    ├── s4/{PlanID}/             # S4阶段产物
    ├── s5/{PlanID}/             # S5架构设计阶段产物
    └── s6/{PlanID}/             # S6详细设计阶段产物
```

## 文档指南

| 文档 | 说明 |
|------|------|
| [CLAUDE.md](CLAUDE.md) | 项目指导文档，包含架构说明和关键规则 |
| [WORKFLOW.md](WORKFLOW.md) | 完整工作流程文档，包含执行细节 |
| [srs.md](srs.md) | 系统需求规格说明 |

## 版本信息

- **当前版本**: v3.1
- **最后更新**: 2026-03-27
- **适用AI IDE**: Claude Code, Codex, Trae

## 许可证

MIT License

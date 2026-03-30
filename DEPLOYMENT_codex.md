# SWF 发布与部署指南

## 概述

本文档说明如何将 SWF (Software WorkFlow) 需求分析与设计系统发布给团队成员在 Codex 或 Claude Code 中使用。

---

## 发布方式

### 方式一：Git 仓库共享（推荐）

适用于团队成员使用 Codex 访问同一仓库的场景。

#### 1. 推送代码到远程仓库

```bash
# 确保所有更改已提交
git add .
git commit -m "release: 发布 SWF v3.2.0"

# 推送到远程仓库
git push origin main
```

#### 2. 团队成员使用

团队成员克隆仓库后，Codex 按 `AGENTS.md` 显式执行：

```bash
# 克隆仓库
git clone https://github.com/HeartFlying/swf.git

# 进入目录
cd swf

```

启动后，使用如下提示词：

```text
请先读取 AGENTS.md，然后按 SWF 工作流执行需求分析/架构设计/详细设计。
```

Codex 会据此读取：
- `AGENTS.md`
- `agents/coordinator-requirements.md`
- `agents/coordinator-architecture.md`
- `agents/coordinator-detailed-design.md`
- `skills/*`

---

### 方式二：AGENTS.md 引用（最简单）

适用于在已有仓库中快速接入 Codex，不依赖平台自动 Agent 发现。

#### 使用方法

在项目的 `AGENTS.md` 中添加：

```markdown
## SWF 需求分析与设计系统

当用户需要需求分析时，读取 `agents/coordinator-requirements.md`。
当用户需要架构设计时，读取 `agents/coordinator-architecture.md`。
当用户需要详细设计时，读取 `agents/coordinator-detailed-design.md`。
执行时遵循仓库中的 `skills/*/SKILL.md` 与 `artifacts/` 产物约定。
```

然后复制 `agents/` 和 `skills/` 目录到项目即可。

---

## 配置说明

### 必需配置

无需额外配置，系统开箱即用。

### 可选配置

如团队内部对提示词有统一规范，建议将下面这段加入项目级 `AGENTS.md`：

```markdown
执行 SWF 时，优先读取 `AGENTS.md`、对应的 `agents/*.md` 和当前 Skill 的 `SKILL.md`，
并将所有产物写入 `artifacts/`。
```

---

## 使用指南

### 快速开始

**启动需求分析：**

```
用户：我想开发一个面向大学生的时间管理 APP

Codex：我会先读取 `AGENTS.md`，然后加载 SWF 需求分析协调器并开始执行。
```

### 完整流程示例

```
用户：帮我做一个完整的需求分析和设计

Codex：
=== 阶段一：需求分析 (读取 coordinator-requirements) ===

[S001] Plan 制定 → 生成 Plan ID: P000001
       信息完整度: 65 分（常规模式）

--- S1 市场洞察 ---
[S101] 竞品分析 → 对比分析竞品功能
[S102] 市场痛点验证 → 验证市场痛点

--- S2 需求定义 ---
[S201] 需求边界界定 → 定义产品/用户/场景边界
[S202] 显性需求提取 → 收集功能和非功能需求
[S203] 隐性需求挖掘 → 识别业务规则和约束
[S204] 需求验证 → 一致性检查

--- S3 技术规划 ---
[S301] 技术可行性评估 → 评估技术方案
[S302] 技术选型 → 推荐技术栈
[S303] 非功能需求定义 → 定义性能、安全等 NFR
[S304] 风险识别 → 技术/业务风险评估

--- S4 需求整合 ---
[S401] 需求分类梳理 → 功能/非功能分类
[S402] 需求优先级排序 → MoSCoW 排序
[S403] 核心需求提炼 → 确定 MVP 功能
[S405] 用户故事编写 → 编写用户故事
[S406] 原型设计 → 设计原型草图

=== 阶段二：架构设计 (读取 coordinator-architecture) ===

[S5-A01] 架构愿景定义 → 定义架构目标、原则
[S5-A02] 架构视图设计 → 4+1 视图设计
[S5-A03] 数据架构设计 → 数据模型、存储方案
[S5-A04] 接口架构设计 → API 定义、接口规范
[S5-A05] 部署架构设计 → 部署方案、拓扑结构
[S5-A06] 架构验证与评审 → 完整性检查、风险识别

=== 阶段三：详细设计 (读取 coordinator-detailed-design) ===

[S6-A01] 模块详细设计 → 类设计、方法签名
[S6-A02] 数据库详细设计 → 表结构、索引、DDL
[S6-A03] UI/UX设计 → 信息架构、页面设计
[S6-A04] 测试策略设计 → 测试策略、测试用例

=== 输出 SWF 完整交付物 ===
```

### 轻量化模式

当需求信息完整度 ≥ 90 分时，自动跳过 5 个 Skill：

| 阶段 | 跳过 Skill | 说明 |
|------|-----------|------|
| S1 | S101, S102 | 竞品分析、市场验证 |
| S2 | S203 | 隐性需求挖掘 |
| S4 | S406 | 原型设计 |

---

## 产物输出

所有产物保存在 `artifacts/` 目录：

```
artifacts/
├── roadmap/                       # 全局 Roadmap（AI 工具导航）
│   ├── index.yaml                 # 全局索引
│   ├── stages/                    # 阶段产物索引
│   └── plans/                     # Plan 级 Roadmap
├── plans/
│   ├── P000001.md                 # Plan 定义
│   └── P000001/
│       ├── todo-list.md           # S0-S4 任务跟踪
│       ├── todo-list-s5.md        # S5 任务跟踪
│       ├── todo-list-s6.md        # S6 任务跟踪
│       ├── dependency-graph.md    # 需求依赖图谱
│       └── swf-deliverable.md     # SWF 完整交付物
├── stages/
│   ├── s0/
│   │   └── P000001-S0-S001-*.md   # Plan 制定产物
│   ├── s1/
│   │   ├── P000001-S1-S101-*.md   # 竞品分析
│   │   └── P000001-S1-S102-*.md   # 市场验证
│   ├── s2/
│   │   ├── P000001-S2-S201-*.md   # 需求边界
│   │   ├── P000001-S2-S202-*.md   # 显性需求
│   │   ├── P000001-S2-S203-*.md   # 隐性需求
│   │   └── P000001-S2-S204-*.md   # 需求验证
│   ├── s3/
│   │   ├── P000001-S3-S301-*.md   # 技术可行性
│   │   ├── P000001-S3-S302-*.md   # 技术选型
│   │   ├── P000001-S3-S303-*.md   # 非功能需求
│   │   └── P000001-S3-S304-*.md   # 风险识别
│   ├── s4/
│   │   ├── P000001-S4-S401-*.md   # 需求分类
│   │   ├── P000001-S4-S402-*.md   # 优先级排序
│   │   ├── P000001-S4-S403-*.md   # 核心需求
│   │   ├── P000001-S4-S405-*.md   # 用户故事
│   │   └── P000001-S4-S406-*.md   # 原型设计
│   ├── s5/
│   │   └── P000001/
│   │       ├── P000001-S5-A01-*.md # 架构愿景
│   │       ├── P000001-S5-A02-*.md # 架构视图
│   │       ├── P000001-S5-A03-*.md # 数据架构
│   │       ├── P000001-S5-A04-*.md # 接口架构
│   │       ├── P000001-S5-A05-*.md # 部署架构
│   │       └── P000001-S5-A06-*.md # 架构验证
│   └── s6/
│       └── P000001/
│           ├── P000001-S6-A01-*.md # 模块设计
│           ├── P000001-S6-A02-*.md # 数据库设计
│           ├── P000001-S6-A03-*.md # UI/UX设计
│           └── P000001-S6-A04-*.md # 测试策略
└── change-management/             # 变更管理产物
    └── P000001/
        ├── traceability-matrix.md # 变更追溯矩阵
        └── impact-analysis-*.md   # 变更影响分析
```

---

## 团队协作

### Git 工作流

```bash
# 1. 团队成员克隆仓库
git clone https://github.com/HeartFlying/swf.git

# 2. 创建自己的分支进行需求分析
git checkout -b feature/P000001-requirements

# 3. 执行 SWF 流程
# -> 在 Codex 中要求读取 AGENTS.md 并执行 SWF
# -> 产物保存到 artifacts/

# 4. 提交产物
git add artifacts/
git commit -m "docs: 添加 P000001 需求分析与设计产物"

# 5. 推送到远程
git push origin feature/P000001-requirements

# 6. 创建 PR 进行评审
```

### 产物共享

产物是 Markdown 格式，可以直接：
- 在 GitHub 上查看和评审
- 导出为 PDF/Word 分享给非技术人员
- 导入到项目管理工具（Jira、飞书等）
- 通过 Roadmap 快速导航

---

## 故障排除

### 问题 1：Codex 没有进入 SWF 流程

**现象：** 输入需求分析相关语句，但 Codex 没有按 SWF 执行

**解决：**
1. 明确要求先读取 `AGENTS.md`
2. 明确指定协调器文件，例如 `agents/coordinator-requirements.md`
3. 确认 `skills/` 目录完整

### 问题 2：Skill 加载失败

**现象：** 协调器已读取，但无法继续执行 Skill

**解决：**
1. 检查 `skills/` 目录是否存在
2. 确认 Skill 目录命名正确：`s0-plan`, `s1-competitor`, `s2-boundary` 等
3. 检查 SKILL.md 文件是否存在

### 问题 3：产物未生成

**现象：** 执行后没有产物文件

**解决：**
1. 检查 `artifacts/` 目录权限
2. 确认目录结构：`artifacts/plans/` 和 `artifacts/stages/`
3. 查看执行日志中的错误信息

### 问题 4：阶段未继续推进

**现象：** S4 完成后没有继续到 S5

**解决：**
1. 确认 S4 所有 Skill 已评审通过
2. 手动要求：`请读取 agents/coordinator-architecture.md 并继续 S5`

---

## 版本历史

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| v3.2.0 | 2026-03-30 | 三阶段协调器架构，26 个工作流 Skill |

---

## 支持与反馈

- **GitHub Issues**: https://github.com/HeartFlying/swf/issues
- **文档**: 参见 `AGENTS.md`、`CLAUDE.md` 和 `WORKFLOW.md`

---

**SWF v3.2.0 - AI 驱动的需求分析与设计系统**

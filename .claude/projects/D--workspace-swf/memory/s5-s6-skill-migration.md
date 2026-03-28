---
name: S5 S6 Agent和Skill优化迁移
description: 记录架构设计阶段(S5)和详细设计阶段(S6)的Agent和Skill优化迁移完成情况，包含文件路径、结构规范和产物命名规则
type: project
---

## 完成内容

### 1. Agent定义文件

创建了两个新的Agent定义文件：

| Agent | 文件路径 | 说明 |
|-------|----------|------|
| S5 架构设计智能体 | `agents/coordinator-s5.md` | 负责架构设计流程的统一调度、状态管理和结果整合 |
| S6 详细设计智能体 | `agents/coordinator-s6.md` | 负责详细设计流程的统一调度、状态管理和结果整合 |

### 2. Skill扁平化迁移

**S5阶段6个Skill**（扁平结构，直接位于 `skills/` 目录下）：

| Skill ID | 目录名 | 说明 |
|----------|--------|------|
| S5-A01 | s5-vision | 架构愿景定义 |
| S5-A02 | s5-views | 架构视图设计 |
| S5-A03 | s5-data | 数据架构设计 |
| S5-A04 | s5-interface | 接口架构设计 |
| S5-A05 | s5-deployment | 部署架构设计 |
| S5-A06 | s5-validation | 架构验证与评审 |

**S6阶段3个Skill**（扁平结构，直接位于 `skills/` 目录下）：

| Skill ID | 目录名 | 说明 |
|----------|--------|------|
| S6-A01 | s6-module | 模块详细设计 |
| S6-A02 | s6-database | 数据库详细设计 |
| S6-A03 | s6-uiux | UI/UX设计 |

**Why:** 与S1-S4阶段保持一致的扁平命名规范，便于查找和管理

**How to apply:** 所有Skill目录遵循 `s{阶段}-{功能}` 命名格式

### 3. 标准结构规范

**Why:** 保持与需求分析阶段Skill模板的一致性，便于AI IDE自动发现和执行

**How to apply:** 所有Skill遵循标准6-Section格式：

```
Skill目录/
├── SKILL.md                    # 主文件（含YAML frontmatter）
├── template.md                 # 输出模板
└── references/
    ├── execution-details.md    # 详细执行步骤
    ├── examples.md             # Demo示例
    ├── quality-standard.md     # ISO/IEC 25010质量标准
    ├── error-code-standard.md  # 错误代码标准
    ├── execution-flow-standard.md
    ├── artifact-specifications.md
    └── user-interaction/
        ├── clarification-template.md
        ├── information-collection-template.md
        └── option-selection-template.md
```

**SKILL.md 6-Section结构：**
1. Section 1: 元信息（YAML frontmatter + 元信息表格）
2. Section 2: 功能描述（核心职责、输入规范、输出规范）
3. Section 3: 执行流程（Mermaid流程图 + 引用详细步骤）
4. Section 4: 产物规范（产物清单、依赖关系）
5. Section 5: 质量标准（ISO/IEC 25010框架、检查清单、验收标准）
6. Section 6: 异常处理（常见异常、恢复策略）

### 4. 产物命名和存储规范

**存储路径：**
- S5产物：`artifacts/stages/s5/{PlanID}/`
- S6产物：`artifacts/stages/s6/{PlanID}/`
- Todo-List：`artifacts/plans/{PlanID}/todo-list-s5.md` 或 `todo-list-s6.md`

**产物ID格式：**
- S5：`{PlanID}-S5-A{编号}-{序号}`，如 `P000001-S5-A01-001`
- S6：`{PlanID}-S6-A{编号}-{序号}`，如 `P000001-S6-A01-001`

### 5. 执行顺序

**S5阶段：** S5-A01 → S5-A02 → S5-A03 → S5-A04 → S5-A05 → S5-A06

**S6阶段：** S6-A01 → S6-A02 → S6-A03

### 6. 完成时间

2026-03-28

---

## 7. 文档命名规范化优化（2026-03-28）

### Agent 文件重命名

| 原文件名 | 新文件名 | 说明 |
|----------|----------|------|
| coordinator.md | 删除 | 与 swf-coordinator.md 功能重复 |
| swf-coordinator.md | coordinator-requirements.md | 需求分析智能体（S0-S4） |
| coordinator-s5.md | coordinator-architecture.md | 架构设计智能体（S5） |
| coordinator-s6.md | coordinator-detailed-design.md | 详细设计智能体（S6） |

### 最终 Agent 文件结构

```
agents/
├── coordinator-requirements.md    # 需求分析智能体（S0-S4，14个Skill）
├── coordinator-architecture.md    # 架构设计智能体（S5，6个Skill）
└── coordinator-detailed-design.md # 详细设计智能体（S6，3个Skill）
```

### Skill 总数统一

- 总计：**23个Skill**
- S0: 1个 | S1: 4个 | S2: 2个 | S3: 3个 | S4: 4个 | S5: 6个 | S6: 3个

### 三阶段划分

1. **需求分析阶段**（S0-S4）：输出 SRS
2. **架构设计阶段**（S5）：输出架构设计文档
3. **详细设计阶段**（S6）：输出可实施设计文档

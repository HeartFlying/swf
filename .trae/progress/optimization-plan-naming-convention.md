# 文档命名规范化优化计划（综合版）

## 背景

项目已明确划分为三个阶段：
1. **需求分析阶段**（S0-S4）：14个Skill，输出 SRS
2. **架构设计阶段**（S5）：6个Skill，输出架构文档
3. **详细设计阶段**（S6）：3个Skill，输出可实施的设计文档

**总计：23个Skill**

---

## 一、Agent 文件优化

### 1.1 现状分析

| 文件名 | 定位 | 阶段 | 问题 |
|--------|------|------|------|
| `coordinator.md` | 需求分析智能体 | S0-S4 | 名称不够明确 |
| `swf-coordinator.md` | SWF需求分析协调器 | S0-S4 | **与coordinator.md功能重复95%+** |
| `coordinator-s5.md` | 架构设计智能体 | S5 | 命名使用编号，不够语义化 |
| `coordinator-s6.md` | 详细设计智能体 | S6 | 命名使用编号，不够语义化 |

### 1.2 优化方案

| 操作 | 当前文件名 | 新文件名 | 说明 |
|------|-----------|----------|------|
| **删除** | `coordinator.md` | - | 与swf-coordinator.md重复 |
| **重命名** | `swf-coordinator.md` | `coordinator-requirements.md` | 需求分析智能体 |
| **重命名** | `coordinator-s5.md` | `coordinator-architecture.md` | 架构设计智能体 |
| **重命名** | `coordinator-s6.md` | `coordinator-detailed-design.md` | 详细设计智能体 |

### 1.3 最终结构

```
agents/
├── coordinator-requirements.md    # 需求分析智能体（S0-S4，14个Skill）
├── coordinator-architecture.md    # 架构设计智能体（S5，6个Skill）
└── coordinator-detailed-design.md # 详细设计智能体（S6，3个Skill）
```

---

## 二、CLAUDE.md 更新

### 2.1 目录结构更新

**位置：第 33 行**
```diff
 ├── agents/                    # Agent definitions
-│   └── coordinator.md         # Main coordinator agent
+│   ├── coordinator-requirements.md    # Requirements analysis agent (S0-S4)
+│   ├── coordinator-architecture.md    # Architecture design agent (S5)
+│   └── coordinator-detailed-design.md # Detailed design agent (S6)
```

### 2.2 执行流程更新

**位置：第 23 行**
```diff
-User Input → Coordinator Agent → Skills (S0→S1→S2→S3→S4) → Final Report
+User Input → Coordinator Agent → Skills (S0→S1→S2→S3→S4→S5→S6) → Final Report
```

### 2.3 Key Files 更新

**位置：第 95 行**
```diff
-- **agents/coordinator.md**: Main agent execution flow, state management, and Todo-List rules
+- **agents/coordinator-requirements.md**: Requirements analysis agent (S0-S4)
+- **agents/coordinator-architecture.md**: Architecture design agent (S5)
+- **agents/coordinator-detailed-design.md**: Detailed design agent (S6)
```

---

## 三、WORKFLOW.md 更新

### 3.1 Skill 数量修正（多处）

| 位置 | 当前值 | 修正为 |
|------|--------|--------|
| 第 23 行 | 14 个 Skill | 23 个 Skill |
| 第 419 行 | 13 个 Skill | 23 个 Skill |
| 第 435 行 | 13 个 Skill | 23 个 Skill |
| 第 481 行 | 14 个 Skill | 23 个 Skill |
| 第 516-521 行 | 示例数量错误 | 更正 |
| 第 1056-1071 行 | 缺少S5/S6 | 添加9个Skill |
| 第 1074-1076 行 | 评审点计算错误 | 重新计算 |

### 3.2 阶段描述更新

**添加 S5、S6 阶段：**
- S5 - 架构设计（6个Skill）
- S6 - 详细设计（3个Skill）

### 3.3 评审点计算更新

```diff
-- 常规模式：14 个 Skill 评审 + 4 个阶段评审 + 1 个最终评审 = **19 个评审点**
-- 轻量化模式：11 个 Skill 评审 + 4 个阶段评审 + 1 个最终评审 = **16 个评审点**
+- 常规模式：23 个 Skill 评审 + 6 个阶段评审 + 1 个最终评审 = **30 个评审点**
+- 轻量化模式：20 个 Skill 评审 + 6 个阶段评审 + 1 个最终评审 = **27 个评审点**
```

---

## 四、Templates 目录更新

### 4.1 skill-structure-reference.md

- 更新目录结构速查表（添加S5/S6）
- 更新产物ID格式速查表（添加S5/S6示例）

### 4.2 标准文件（6个文件）

统一更新适用范围：
- `quality-standard.md`
- `error-code-standard.md`
- `execution-flow-standard.md`
- `artifact-specifications.md`
- `todo-list-template.md`
- `user-interaction/*.md`（3个）

```diff
-**适用对象**: 所有14个Skill（S001, S101-S104, S201-S202, S301-S303, S401-S404）
+**适用对象**: 所有23个Skill（S0-S4: 14个 + S5: 6个 + S6: 3个）
```

---

## 五、其他配置文件更新

### 5.1 .claude/SWF.md

- 更新执行序列（添加S5/S6）
- 统一Skill编号命名格式

### 5.2 .claude/memory/swf-tasks.md

- 更新Skill数量（14→23）

### 5.3 README.md

- 更新Agent文件引用
- 更新Skill数量（14→23）
- 添加S5/S6阶段描述

### 5.4 DEPLOYMENT.md

- 更新Agent文件引用
- 更新Skill数量

### 5.5 INSTALL.md

- 更新Agent文件说明

---

## 六、执行步骤

### Step 1: Agent 文件操作
```bash
cd agents/
rm coordinator.md
mv swf-coordinator.md coordinator-requirements.md
mv coordinator-s5.md coordinator-architecture.md
mv coordinator-s6.md coordinator-detailed-design.md
```

### Step 2: 更新 CLAUDE.md
- 目录结构
- 执行流程
- Key Files引用

### Step 3: 更新 WORKFLOW.md
- Skill数量（多处）
- 阶段描述
- 评审点计算

### Step 4: 更新 templates/
- 6个标准文件的适用范围

### Step 5: 更新其他配置文件
- .claude/SWF.md
- .claude/memory/swf-tasks.md
- README.md
- DEPLOYMENT.md
- INSTALL.md

### Step 6: 更新 memory 文件
- 更新迁移记录

---

## 七、预期结果

### Agent 文件结构
```
agents/
├── coordinator-requirements.md    # 需求分析智能体（S0-S4）
├── coordinator-architecture.md    # 架构设计智能体（S5）
└── coordinator-detailed-design.md # 详细设计智能体（S6）
```

### Skill 数量统一
- 总计：23个Skill
- S0: 1个 | S1: 4个 | S2: 2个 | S3: 3个 | S4: 4个 | S5: 6个 | S6: 3个

### 阶段划分统一
- 需求分析阶段（S0-S4）
- 架构设计阶段（S5）
- 详细设计阶段（S6）

---

## 待确认

请确认是否同意执行以上优化计划：

1. [ ] 同意删除 `coordinator.md`（与swf-coordinator.md重复）
2. [ ] 同意Agent文件重命名方案
3. [ ] 同意更新CLAUDE.md、WORKFLOW.md
4. [ ] 同意更新templates/目录文件
5. [ ] 同意更新其他配置文件
6. [ ] 其他意见：____________

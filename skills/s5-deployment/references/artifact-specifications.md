# 产物规范统一说明

本文档定义SWF项目所有Skill产物的统一规范，包括产物ID命名、存储路径、版本管理等。

---

## 1. 产物ID命名规则

### 1.1 标准格式

```
{PlanID}-S{阶段}-{SkillID}-{序号}
```

### 1.2 组成部分说明

| 部分 | 格式 | 示例 | 说明 |
|------|------|------|------|
| PlanID | P + 6位数字 | P000001 | 唯一标识一个Plan |
| 阶段 | S0-S6 | S5 | 表示所属阶段 |
| SkillID | S001-S404 / A01-A06 | A05 | 表示Skill编号 |
| 序号 | 3位数字 | 001 | 从001开始递增 |

### 1.3 示例

| 产物ID | 说明 |
|--------|------|
| P000001-S0-S001-001 | Plan定义文件 |
| P000001-S1-S101-001 | 边界界定报告 |
| P000001-S5-A01-001 | 架构愿景文档 |
| P000001-S5-A05-001 | 部署架构设计文档 |
| P000001-S6-D01-001 | 详细设计文档 |

---

## 2. 存储路径结构

### 2.1 目录结构

```
artifacts/
├── plans/
│   ├── {PlanID}.md                    # Plan定义文件
│   └── {PlanID}/
│       └── todo-list.md               # Todo-List（任务跟踪）
└── stages/
    ├── s0/                            # S0阶段产物
    ├── s1/                            # S1阶段产物
    ├── s2/                            # S2阶段产物
    ├── s3/                            # S3阶段产物
    ├── s4/                            # S4阶段产物
    ├── s5/                            # S5阶段产物（架构设计）
    │   └── {PlanID}/
    │       ├── {PlanID}-S5-A01-001.md # 架构愿景
    │       ├── {PlanID}-S5-A02-001.md # 架构视图
    │       ├── {PlanID}-S5-A03-001.md # 数据架构
    │       ├── {PlanID}-S5-A04-001.md # 接口架构
    │       ├── {PlanID}-S5-A05-001.md # 部署架构
    │       └── {PlanID}-S5-A06-001.md # 架构验证
    └── s6/                            # S6阶段产物（详细设计）
        └── {PlanID}/
            ├── {PlanID}-S6-D01-001.md # 数据库设计
            ├── {PlanID}-S6-D02-001.md # API设计
            └── {PlanID}-S6-D03-001.md # 组件设计
```

### 2.2 路径规则

| 产物类型 | 路径格式 | 示例 |
|----------|----------|------|
| Plan定义文件 | `artifacts/plans/{PlanID}.md` | `artifacts/plans/P000001.md` |
| Todo-List | `artifacts/plans/{PlanID}/todo-list.md` | `artifacts/plans/P000001/todo-list.md` |
| S0阶段产物 | `artifacts/stages/s0/{PlanID}-S0-{SkillID}-{序号}.md` | `artifacts/stages/s0/P000001-S0-S001-001.md` |
| S1阶段产物 | `artifacts/stages/s1/{PlanID}-S1-{SkillID}-{序号}.md` | `artifacts/stages/s1/P000001-S1-S101-001.md` |
| S5阶段产物 | `artifacts/stages/s5/{PlanID}/{PlanID}-S5-{SkillID}-{序号}.md` | `artifacts/stages/s5/P000001/P000001-S5-A05-001.md` |
| S6阶段产物 | `artifacts/stages/s6/{PlanID}/{PlanID}-S6-{SkillID}-{序号}.md` | `artifacts/stages/s6/P000001/P000001-S6-D01-001.md` |

### 2.3 索引文件（可选）

**Plan列表索引**：`artifacts/plans/index.md`

```markdown
# Plan列表索引

| Plan ID | 创建时间 | 状态 | 执行模式 | 最后更新 |
|---------|----------|------|----------|----------|
| P000001 | 2026-03-28 | 已完成 | normal | 2026-03-28 |
| P000002 | 2026-03-29 | 执行中 | lightweight | 2026-03-29 |
```

---

## 3. 产物版本管理

### 3.1 版本规则

| 版本类型 | 格式 | 说明 |
|----------|------|------|
| 初始版本 | v1.0 | 首次生成 |
| 小修改 | v1.1, v1.2... | 内容微调，结构不变 |
| 大修改 | v2.0, v3.0... | 结构变更或重新执行 |

### 3.2 版本记录格式

在产物文件头部添加版本信息：

```markdown
---
version: v1.0
created_at: 2026-03-28 10:00:00
updated_at: 2026-03-28 10:00:00
---
```

### 3.3 历史版本保存

- 大版本变更时，保留旧版本副本
- 命名格式：`{PlanID}-S{阶段}-{SkillID}-{序号}-v{版本}.md`
- 示例：`P000001-S5-A05-001-v1.md`

---

## 4. 产物格式规范

### 4.1 文件格式

- 所有产物必须使用 **Markdown** 格式
- 编码：**UTF-8**
- 换行符：LF（Unix风格）

### 4.2 内容结构

产物文档应包含以下章节：

```markdown
# 产物标题 - {产物ID}

## 基本信息
- **Plan ID**: {PlanID}
- **Skill ID**: {SkillID}
- **执行时间**: YYYY-MM-DD HH:MM
- **执行模式**: normal / lightweight

## 核心内容
[产物具体内容]

## 用户交互记录
[如有交互，记录在此]

## 评审记录
[用户评审结果记录在此]
```

### 4.3 表格规范

- 使用标准Markdown表格语法
- 表头必须包含对齐标记（`:---`、`:--:`、`---:`）
- 单元格内容为空时使用 `-` 占位

---

## 5. S5阶段产物清单

### S5阶段（架构设计）

| Skill | 产物名称 | 产物ID格式 | 存储路径 |
|-------|----------|------------|----------|
| S5-A01 | 架构愿景文档 | {PlanID}-S5-A01-001 | artifacts/stages/s5/{PlanID}/ |
| S5-A02 | 架构视图设计文档 | {PlanID}-S5-A02-001 | artifacts/stages/s5/{PlanID}/ |
| S5-A03 | 数据架构设计文档 | {PlanID}-S5-A03-001 | artifacts/stages/s5/{PlanID}/ |
| S5-A04 | 接口架构设计文档 | {PlanID}-S5-A04-001 | artifacts/stages/s5/{PlanID}/ |
| S5-A05 | 部署架构设计文档 | {PlanID}-S5-A05-001 | artifacts/stages/s5/{PlanID}/ |
| S5-A06 | 架构验证报告 | {PlanID}-S5-A06-001 | artifacts/stages/s5/{PlanID}/ |

### S6阶段（详细设计）

| Skill | 产物名称 | 产物ID格式 | 存储路径 |
|-------|----------|------------|----------|
| S6-D01 | 数据库设计文档 | {PlanID}-S6-D01-001 | artifacts/stages/s6/{PlanID}/ |
| S6-D02 | API设计文档 | {PlanID}-S6-D02-001 | artifacts/stages/s6/{PlanID}/ |
| S6-D03 | 组件设计文档 | {PlanID}-S6-D03-001 | artifacts/stages/s6/{PlanID}/ |

---

## 6. 产物引用规范

### 6.1 引用格式

在Skill文档中引用产物时，使用以下格式：

```markdown
**依赖产物**：
- [{产物名称}]({相对路径}) - {产物ID}
```

### 6.2 示例

```markdown
**依赖产物**：
- [架构愿景文档](../../artifacts/stages/s5/P000001/P000001-S5-A01-001.md) - P000001-S5-A01-001
- [架构视图设计文档](../../artifacts/stages/s5/P000001/P000001-S5-A02-001.md) - P000001-S5-A02-001
```

---

**文档版本**: v1.0
**适用范围**: 所有Skill
**最后更新**: 2026-03-28

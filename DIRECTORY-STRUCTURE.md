# SWF 产物目录结构规范（简化版）

## 核心原则

1. **扁平化**：所有产物在同一目录下，便于查找
2. **顺序编号**：按执行顺序编号，一目了然
3. **语义命名**：文件名体现内容和顺序

---

## 目录结构

```
swf/
├── .claude/
│   ├── SWF.md              # 快速启动指令
│   └── memory/
│       └── swf-context.md  # 上下文记忆
├── templates/
│   └── all-templates.md    # 所有Skill模板速查
└── database/
    └── {PlanID}/           # 每个需求分析一个目录
        ├── 00-plan.md              # Plan定义
        ├── 00-todo-list.md         # 任务跟踪
        ├── 01-boundary.md          # S1-Skill1: 需求边界界定
        ├── 02-explicit.md          # S1-Skill2: 显性需求提取
        ├── 03-implicit.md          # S1-Skill3: 隐性需求挖掘（常规模式）
        ├── 04-validation.md        # S1-Skill4: 需求验证
        ├── 05-classify.md          # S4-Skill5: 需求分类梳理
        ├── 06-priority.md          # S4-Skill6: 需求优先级排序
        ├── 07-risk.md              # S3-Skill7: 需求风险识别
        ├── 08-core.md              # S4-Skill8: 核心需求提炼
        ├── 09-competitor.md        # S2-Skill9: 竞品分析（常规模式）
        ├── 10-market.md            # S2-Skill10: 市场痛点验证（常规模式）
        ├── 11-feasibility.md       # S3-Skill11: 技术可行性评估
        ├── 12-selection.md         # S3-Skill12: 轻量化技术选型
        ├── 15-prototype.md         # S4-Skill15: 原型设计（可选）
        └── final-report.md         # 整合最终报告
```

---

## 与旧结构对比

### 旧结构（分层）
```
database/
├── plans/
│   ├── {PlanID}.md
│   └── {PlanID}/
│       └── todo-list.md
└── stages/
    ├── s0/
    ├── s1/
    ├── s2/
    ├── s3/
    └── s4/
```

**问题**：
- 路径嵌套深，查找困难
- 需要记忆 stages/s1/ 等路径
- 产物分散在不同目录

### 新结构（扁平）
```
database/
└── {PlanID}/
    ├── 00-plan.md
    ├── 01-boundary.md
    ├── 02-explicit.md
    └── ...
```

**优势**：
- 所有产物在一个目录
- 编号即执行顺序，直观
- 路径简单，易于记忆

---

## 文件名规范

### 格式
```
{两位数字}-{英文标识}.md
```

### 编号规则
- 00：Plan级产物（plan, todo-list）
- 01-04：S1阶段产物
- 05-06：S4阶段产物（按执行顺序）
- 07：S3阶段产物
- 08：S4阶段最终产物
- 09-10：S2阶段产物（常规模式）
- 11-12：S3阶段产物
- 15：S4阶段可选产物

### 英文标识
使用Skill核心概念的英文简写：
- boundary：边界界定
- explicit：显性需求
- implicit：隐性需求
- validation：需求验证
- competitor：竞品分析
- core：核心需求
- ...

---

## 产物ID对应关系

| 产物ID（旧） | 文件名（新） | 说明 |
|-------------|-------------|------|
| {PlanID}-S0-S00-001 | 00-plan.md | Plan定义 |
| {PlanID}-S1-S01-001 | 01-boundary.md | 需求边界界定 |
| {PlanID}-S1-S02-001 | 02-explicit.md | 显性需求提取 |
| {PlanID}-S1-S03-001 | 03-implicit.md | 隐性需求挖掘 |
| {PlanID}-S1-S04-001 | 04-validation.md | 需求验证 |
| {PlanID}-S2-S09-001 | 09-competitor.md | 竞品分析 |
| {PlanID}-S2-S10-001 | 10-market.md | 市场痛点验证 |
| {PlanID}-S3-S07-001 | 07-risk.md | 需求风险识别 |
| {PlanID}-S3-S11-001 | 11-feasibility.md | 技术可行性评估 |
| {PlanID}-S3-S12-001 | 12-selection.md | 轻量化技术选型 |
| {PlanID}-S4-S05-001 | 05-classify.md | 需求分类梳理 |
| {PlanID}-S4-S06-001 | 06-priority.md | 需求优先级排序 |
| {PlanID}-S4-S08-001 | 08-core.md | 核心需求提炼 |
| {PlanID}-S4-S15-001 | 15-prototype.md | 原型设计 |

---

## 使用示例

### 创建新Plan
```bash
# Plan ID: P000001
mkdir -p database/P000001

# 生成产物
touch database/P000001/00-plan.md
touch database/P000001/00-todo-list.md
```

### 查看产物列表
```bash
ls -la database/P000001/

# 输出：
# 00-plan.md
# 00-todo-list.md
# 01-boundary.md
# 02-explicit.md
# ...
```

### 快速定位产物
```bash
# 查看当前执行进度（按时间排序）
ls -lt database/P000001/

# 查看最新产物
cat database/P000001/$(ls -t database/P000001/ | head -1)
```

---

## 路径引用更新

更新以下文档中的路径引用：

| 文档 | 原路径 | 新路径 |
|------|--------|--------|
| CLAUDE.md | `database/plans/{PlanID}.md` | `database/{PlanID}/00-plan.md` |
| CLAUDE.md | `database/stages/s1/{PlanID}-S1-S01-001.md` | `database/{PlanID}/01-boundary.md` |
| WORKFLOW.md | `database/plans/{PlanID}/todo-list.md` | `database/{PlanID}/00-todo-list.md` |
| 各SKILL.md | 相应调整 | 相应调整 |

---

## 迁移指南

如需迁移旧产物到新结构：

```bash
# 示例：迁移 Plan P000001
OLD_PLAN="database/plans/P000001"
NEW_PLAN="database/P000001"

mkdir -p "$NEW_PLAN"

# 迁移Plan定义
cp "$OLD_PLAN.md" "$NEW_PLAN/00-plan.md"

# 迁移todo-list
cp "$OLD_PLAN/todo-list.md" "$NEW_PLAN/00-todo-list.md"

# 迁移S1产物
cp "database/stages/s1/P000001-S1-S01-001.md" "$NEW_PLAN/01-boundary.md"
cp "database/stages/s1/P000001-S1-S02-001.md" "$NEW_PLAN/02-explicit.md"
# ... 以此类推
```

---

*目录结构规范 v1.0*
*适用：SWF 需求分析工作流*

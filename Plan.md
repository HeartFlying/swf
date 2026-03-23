# Agent+Skill用户需求分析系统实施计划

## 项目概述
基于 `srs.md` 方案，在Trae开发环境中设计一套完整的**Agent+Skill用户需求分析工作流程**，以本地文件系统为信息交互中心。

**核心特性**：
- ✅ Plan实施计划支持任务中断和断点续跑
- ✅ Plan实施计划全流程状态追踪和记录
- ✅ 各Agent和Skill相互关联，形成完整工作流程
- ✅ 主协调Agent统一调度，确保流程可正常跑通

**设计原则**：
- 纯工作流程设计，无需编码实现
- 所有逻辑通过Agent Prompt和Skill定义文档描述
- 通过文件系统实现状态持久化和数据传递

---

## 一、项目目录结构

```
d:\workspace\swf\
├── Plan.md                     # 本实施计划文件
├── Plan-Status.json            # Plan实施状态追踪文件
├── Plan-Resume.json            # Plan断点续跑配置文件
├── Plan-Execution.log          # Plan实施执行日志
├── README.md                   # 项目说明文档
├── WORKFLOW.md                 # 主工作流程文档（Agent调度规则）
│
├── agents\                     # Agent Prompt提示词文件
│   ├── coordinator.md          # 主协调Agent
│   ├── validator.md            # 格式校验守卫Agent
│   ├── user-interaction.md     # 用户交互Agent
│   └── executor.md             # 技能执行Agent
│
├── skills\                     # Skill定义文件
│   ├── skill0-plan\            # Skill0: Plan制定
│   │   ├── SKILL.md            # Skill定义文档
│   │   └── template.md         # 输出模板
│   │
│   ├── s1-requirements\        # S1阶段: 需求边界与原始采集
│   │   ├── skill1-boundary\    # Skill1: 需求边界界定
│   │   │   ├── SKILL.md
│   │   │   └── template.md
│   │   ├── skill2-explicit\    # Skill2: 显性需求提取
│   │   │   ├── SKILL.md
│   │   │   └── template.md
│   │   ├── skill3-implicit\    # Skill3: 隐性需求挖掘
│   │   │   ├── SKILL.md
│   │   │   └── template.md
│   │   └── skill4-validation\  # Skill4: 需求验证
│   │       ├── SKILL.md
│   │       └── template.md
│   │
│   ├── s2-market\              # S2阶段: 市场与需求价值校验
│   │   ├── skill9-competitor\  # Skill9: 竞品分析
│   │   │   ├── SKILL.md
│   │   │   └── template.md
│   │   └── skill10-market\     # Skill10: 市场痛点验证
│   │       ├── SKILL.md
│   │       └── template.md
│   │
│   ├── s3-technical\           # S3阶段: 技术可行性与选型
│   │   ├── skill7-risk\        # Skill7: 需求风险识别
│   │   │   ├── SKILL.md
│   │   │   └── template.md
│   │   ├── skill11-feasibility\ # Skill11: 技术可行性评估
│   │   │   ├── SKILL.md
│   │   │   └── template.md
│   │   └── skill12-selection\  # Skill12: 轻量化技术选型
│   │       ├── SKILL.md
│   │       └── template.md
│   │
│   └── s4-integration\         # S4阶段: 需求整合与核心提炼
│       ├── skill5-classify\    # Skill5: 需求分类梳理
│       │   ├── SKILL.md
│       │   └── template.md
│       ├── skill6-priority\    # Skill6: 需求优先级排序
│       │   ├── SKILL.md
│       │   └── template.md
│       └── skill8-core\        # Skill8: 核心需求提炼
│           ├── SKILL.md
│           └── template.md
│
├── database\                   # 中心化信息库（需求分析产物存储）
│   ├── plans\                  # Plan存储目录
│   ├── stages\                 # 阶段产物存储目录
│   │   ├── s1\                 # S1阶段产物
│   │   ├── s2\                 # S2阶段产物
│   │   ├── s3\                 # S3阶段产物
│   │   └── s4\                 # S4阶段产物
│   └── index.json              # 信息库索引文件
│
├── examples\                   # 示例和测试
│   ├── sample-requirement.md   # 示例需求文件
│   └── test-workflow.md        # 测试流程文档
│
└── utils\                      # 工具规范文档
    ├── id-generator.md         # ID生成规则
    └── format-checker.md       # 格式校验规则汇总
```

---

## 二、文件命名规范

### 1. Plan ID 生成规则
- 格式：`P{6位数字}`，如 `P000001`
- 生成方式：时间戳后6位 + 随机数

### 2. Skill 产物 ID 生成规则
- 格式：`{PlanID}-{阶段编号}-{Skill编号}-{序号}`
- 示例：`P000001-S1-S01-001`

### 3. 文件名规范
- Agent文件：`{agent-name}.md`，使用小写+连字符
- Skill定义：`SKILL.md`，统一大写
- 模板文件：`template.md`，统一小写
- 产物文件：`{产物ID}.md`

---

## 三、双层状态追踪体系

### 第一层：Plan实施计划状态追踪（本计划执行跟踪）

#### 1. Plan实施状态 (Plan-Status.json)
```json
{
  "planVersion": "1.0",
  "status": "in_progress|paused|completed",
  "currentStep": 5,
  "totalSteps": 15,
  "progress": {
    "completedSteps": 4,
    "remainingSteps": 11,
    "completionPercentage": "26.7%"
  },
  "steps": [
    {"stepId": 1, "name": "创建项目目录结构", "status": "completed", "completedAt": "2026-03-23T10:00:00Z"},
    {"stepId": 2, "name": "创建信息库模板", "status": "completed", "completedAt": "2026-03-23T10:30:00Z"},
    {"stepId": 3, "name": "创建状态管理规范", "status": "completed", "completedAt": "2026-03-23T11:00:00Z"},
    {"stepId": 4, "name": "编写主协调Agent", "status": "completed", "completedAt": "2026-03-23T11:30:00Z"},
    {"stepId": 5, "name": "编写格式校验守卫Agent", "status": "in_progress", "startedAt": "2026-03-23T12:00:00Z"},
    {"stepId": 6, "name": "编写用户交互Agent", "status": "pending"},
    {"stepId": 7, "name": "编写技能执行Agent", "status": "pending"},
    {"stepId": 8, "name": "编写Skill0-Plan制定", "status": "pending"},
    {"stepId": 9, "name": "编写S1阶段Skill1-4", "status": "pending"},
    {"stepId": 10, "name": "编写S2阶段Skill9-10", "status": "pending"},
    {"stepId": 11, "name": "编写S3阶段Skill7,11-12", "status": "pending"},
    {"stepId": 12, "name": "编写S4阶段Skill5-6,8", "status": "pending"},
    {"stepId": 13, "name": "编写主工作流程文档WORKFLOW.md", "status": "pending"},
    {"stepId": 14, "name": "创建示例需求和完整流程测试", "status": "pending"},
    {"stepId": 15, "name": "编写测试流程文档", "status": "pending"}
  ],
  "createdAt": "2026-03-23T10:00:00Z",
  "updatedAt": "2026-03-23T12:00:00Z",
  "completedAt": null,
  "notes": "当前正在实施步骤5"
}
```

#### 2. Plan断点续跑配置 (Plan-Resume.json)
```json
{
  "planVersion": "1.0",
  "canResume": true,
  "breakpoint": {
    "stepId": 5,
    "stepName": "编写格式校验守卫Agent",
    "status": "in_progress",
    "interruptedAt": "2026-03-23T14:00:00Z",
    "reason": "用户暂停"
  },
  "context": {
    "lastCompletedStep": 4,
    "nextStep": 5,
    "completedArtifacts": [
      "agents/coordinator.md",
      "database/index.json",
      "utils/state-manager.md"
    ]
  },
  "resumeInstruction": "从步骤5继续执行：编写格式校验守卫Agent"
}
```

#### 3. Plan执行日志 (Plan-Execution.log)
```
[2026-03-23 10:00:00] [INFO] Plan实施计划启动
[2026-03-23 10:00:01] [INFO] 开始执行步骤1：创建项目目录结构
[2026-03-23 10:00:30] [INFO] 步骤1完成，已创建所有目录
[2026-03-23 10:00:31] [INFO] 开始执行步骤2：创建信息库模板
[2026-03-23 10:30:00] [INFO] 步骤2完成，已创建所有模板文件
...
[2026-03-23 12:00:00] [INFO] 开始执行步骤5：编写格式校验守卫Agent
[2026-03-23 14:00:00] [WARN] 用户请求暂停，保存断点
[2026-03-23 14:00:01] [INFO] 断点已保存，可从步骤5继续
[2026-03-23 15:00:00] [INFO] 恢复执行，从步骤5继续
[2026-03-23 15:30:00] [INFO] 步骤5完成
```

### 第二层：需求分析流程状态追踪（Agent/Skill执行跟踪）

#### 1. 需求分析Plan状态 (database/plans/{PlanID}/status.json)
```json
{
  "planId": "P000001",
  "status": "running|paused|completed|failed",
  "currentStage": "S1|S2|S3|S4",
  "currentSkill": "S01|S02|...",
  "executionMode": "normal|lightweight",
  "progress": {
    "totalStages": 4,
    "completedStages": 1,
    "totalSkills": 13,
    "completedSkills": 3
  },
  "createdAt": "2026-03-23T10:00:00Z",
  "updatedAt": "2026-03-23T10:30:00Z",
  "completedAt": null
}
```

#### 2. 需求分析断点续跑配置 (database/plans/{PlanID}/resume.json)
```json
{
  "planId": "P000001",
  "breakpoint": {
    "stage": "S1",
    "skill": "S03",
    "action": "execute|validate|retry",
    "retryCount": 1
  },
  "context": {
    "lastCompletedSkill": "S02",
    "lastCompletedOutput": "P000001-S1-S02-001"
  },
  "canResume": true,
  "resumePoint": "从Skill3开始执行"
}
```

---

## 四、工作流程设计（WORKFLOW.md核心内容）

### 1. Agent协作流程

```
┌─────────────────────────────────────────────────────────────┐
│                     主协调Agent (Coordinator)                  │
│  职责：接收需求→制定Plan→调度执行→状态管理→结果整合              │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌───────────────┐    ┌─────────────────┐    ┌───────────────┐
│ 格式校验守卫Agent │    │ 用户交互Agent      │    │ 技能执行Agent   │
│ (Validator)   │    │ (UserInteraction)│    │  (Executor)   │
│ 职责：格式校验   │    │ 职责：用户交互      │    │ 职责：执行Skill │
└───────────────┘    └─────────────────┘    └───────────────┘
```

### 2. 主协调Agent调度规则

**阶段化执行流程**：

1. **初始化阶段**
   - 接收用户原始需求
   - 执行Skill0制定Plan
   - 初始化所有状态文件
   - 进行信息完整度评分，确定执行模式

2. **阶段执行循环**（S1→S2→S3→S4）
   ```
   对于每个阶段:
     a. 读取上一阶段汇总产物ID
     b. 按顺序执行阶段内Skill:
        - 前置校验（调用Validator Agent）
        - Skill执行（调用Executor Agent）
        - 后置校验（调用Validator Agent）
        - 保存产物，更新状态
        - 记录执行日志
     c. 阶段完成后，更新Plan状态
   ```

3. **断点续跑检测**
   ```
   每次执行前:
     - 检查 resume.json 是否存在
     - 若 canResume=true:
       * 读取断点位置
       * 恢复执行上下文
       * 从断点继续执行
     - 若 canResume=false:
       * 正常从头执行
   ```

### 3. Skill间数据流转规则

```
Skill0 (Plan制定)
    └── 输出：Plan定义 → 保存到 database/plans/{PlanID}/

S1阶段：
Skill1 (边界界定) 
    └── 输出：边界清单 → 产物ID: P000001-S1-S01-001
Skill2 (显性需求)
    └── 输入：读取Skill1产物
    └── 输出：显性需求表 → 产物ID: P000001-S1-S02-001
Skill3 (隐性需求)
    └── 输入：读取Skill2产物
    └── 输出：隐性需求表 → 产物ID: P000001-S1-S03-001
Skill4 (需求验证)
    └── 输入：读取Skill2+Skill3产物
    └── 输出：最终需求原始表 → S1汇总产物 → 传递给S2

S2阶段：
Skill9 (竞品分析)
    └── 输入：读取Skill4产物
    └── 输出：竞品分析表 → 产物ID: P000001-S2-S09-001
Skill10 (市场验证)
    └── 输入：读取Skill9产物
    └── 输出：市场价值校验清单 → S2汇总产物 → 传递给S3

S3阶段：
Skill7 (风险识别)
    └── 输入：读取Skill10产物
    └── 输出：风险清单 → 产物ID: P000001-S3-S07-001
Skill11 (可行性评估)
    └── 输入：读取Skill10产物
    └── 输出：可行性评估表 → 产物ID: P000001-S3-S11-001
Skill12 (技术选型)
    └── 输入：读取Skill7+Skill11产物
    └── 输出：技术选型及成本表 → S3汇总产物 → 传递给S4

S4阶段：
Skill5 (分类梳理)
    └── 输入：读取Skill12产物
    └── 输出：分类表 → 产物ID: P000001-S4-S05-001
Skill6 (优先级排序)
    └── 输入：读取Skill5产物
    └── 输出：优先级表 → 产物ID: P000001-S4-S06-001
Skill8 (核心提炼)
    └── 输入：读取Skill6产物
    └── 输出：核心需求提炼表 → 最终产物
```

---

## 五、原子化实施步骤

### 阶段一：基础设施搭建

#### 步骤1：创建项目目录结构
- 创建所有目录层级（agents, skills, database, examples, utils）
- 创建子目录结构（按阶段组织skills）
- 初始化占位文件

#### 步骤2：创建Plan实施状态追踪文件
- 创建 `Plan-Status.json` - 实施计划状态追踪
- 创建 `Plan-Resume.json` - 断点续跑配置
- 创建 `Plan-Execution.log` - 执行日志

#### 步骤3：创建信息库模板
- 设计 `database/index.json` 索引结构
- 创建需求分析Plan状态模板 `status.json`
- 创建需求分析断点续跑模板 `resume.json`

### 阶段二：Agent Prompt编写

#### 步骤4：主协调Agent (coordinator.md)
- 定义角色和核心职责
- 实现信息完整度评分规则
- 实现双模式切换逻辑
- 定义阶段化调度规则
- 定义断点续跑检测和恢复逻辑

#### 步骤5：格式校验守卫Agent (validator.md)
- 定义通用前置校验规则
- 定义通用后置校验规则
- 定义分Skill专项校验规则
- 实现异常处理和重跑机制

#### 步骤6：用户交互Agent (user-interaction.md)
- 定义3个交互触发节点
- 定义3类标准化输入格式
- 实现交互联动流程
- 定义JSON输出格式

#### 步骤7：技能执行Agent (executor.md)
- 定义Skill执行流程
- 实现串行执行逻辑
- 定义产物存储规则
- 定义状态更新机制

### 阶段三：Skill定义编写

#### 步骤8：Skill0 - Plan制定
- 定义输入：用户原始需求
- 定义输出：阶段化执行Plan
- 设计Plan表格模板（≤4个阶段）
- 定义4条执行规则

#### 步骤9：S1阶段 Skill1-4
- **Skill1**：需求边界界定（边界类型固定值）
- **Skill2**：显性需求提取（需求序号连续）
- **Skill3**：隐性需求挖掘（5W2H方法）
- **Skill4**：需求验证（验证结果固定枚举）

#### 步骤10：S2阶段 Skill9-10
- **Skill9**：竞品分析（覆盖度固定枚举）
- **Skill10**：市场痛点验证（处理结论/市场意愿固定枚举）

#### 步骤11：S3阶段 Skill7,11-12
- **Skill7**：需求风险识别（风险类型/等级固定枚举）
- **Skill11**：技术可行性评估（可行性结论固定枚举）
- **Skill12**：轻量化技术选型（实施周期/成本格式规范）

#### 步骤12：S4阶段 Skill5-6,8
- **Skill5**：需求分类梳理（分类固定枚举）
- **Skill6**：需求优先级排序（MoSCoW模型）
- **Skill8**：核心需求提炼（核心需求序号连续）

### 阶段四：工作流程与测试

#### 步骤13：编写主工作流程文档 (WORKFLOW.md)
- 定义Agent协作流程图
- 定义主协调Agent调度规则
- 定义Skill间数据流转规则
- 定义断点续跑流程
- 定义异常处理流程

#### 步骤14：创建示例需求
- 模糊需求示例（测试常规模式+断点续跑）
- 完整需求示例（测试轻量化模式）

#### 步骤15：编写测试流程文档
- 首次执行测试步骤
- 中断后继续执行测试
- 异常处理测试步骤
- 全流程连通性验证

---

## 六、Skill统一输出模板

```markdown
# 【SkillX+名称】输出产物

## 元信息
- 所属PlanID：{XXX}
- 所属阶段：{SX}
- 前置依赖Skill：{SkillX/无}
- 产物唯一ID：{XXX-SX-SX-00X}
- 核心内容摘要：{≤50字}
- 用户交互记录：{无/具体内容}

## 主体内容
{Skill专属固定字段Markdown表格}
```

---

## 七、信息完整度评分规则

满分100分，≥90分触发轻量化模式：

| 维度 | 分值 | 评分标准 |
|------|------|----------|
| 边界清晰度 | 25分 | 产品目标/目标受众/核心场景，每项8分 |
| 需求具体度 | 25分 | 显性功能/非功能需求，每项12分 |
| 约束明确度 | 25分 | 时间/预算/技术/资源约束，每项6分 |
| 目标明确度 | 25分 | 核心价值/商业目标/落地指标，每项12分 |

---

## 八、实施确认

本计划共包含 **15个原子化步骤**，按顺序实施：

### 阶段一：基础设施
1. ⬜ 步骤1：创建项目目录结构
2. ⬜ 步骤2：创建Plan实施状态追踪文件
3. ⬜ 步骤3：创建信息库模板

### 阶段二：Agent编写
4. ⬜ 步骤4：编写主协调Agent
5. ⬜ 步骤5：编写格式校验守卫Agent
6. ⬜ 步骤6：编写用户交互Agent
7. ⬜ 步骤7：编写技能执行Agent

### 阶段三：Skill编写
8. ⬜ 步骤8：编写Skill0-Plan制定
9. ⬜ 步骤9：编写S1阶段Skill1-4
10. ⬜ 步骤10：编写S2阶段Skill9-10
11. ⬜ 步骤11：编写S3阶段Skill7,11-12
12. ⬜ 步骤12：编写S4阶段Skill5-6,8

### 阶段四：工作流程与测试
13. ⬜ 步骤13：编写主工作流程文档WORKFLOW.md
14. ⬜ 步骤14：创建示例需求和完整流程测试
15. ⬜ 步骤15：编写测试流程文档

---

## 九、下一步行动

**请确认本计划后，我将开始实施步骤1：创建项目目录结构**

确认方式：
- 回复"**确认**" - 我将按顺序开始实施
- 回复"**修改**" - 请指出需要调整的部分
- 回复"**跳过X**" - 跳过指定步骤（如"跳过步骤1"表示目录已存在）

---

## 十、关键设计要点说明

### 1. 双层状态追踪体系

**第一层：Plan实施计划状态追踪**
- 跟踪本实施计划（Plan.md）的执行进度
- 文件：`Plan-Status.json`, `Plan-Resume.json`, `Plan-Execution.log`
- 用途：记录步骤1-15的完成情况，支持断点续跑

**第二层：需求分析流程状态追踪**
- 跟踪具体需求分析流程（Agent/Skill执行）的状态
- 文件：`database/plans/{PlanID}/status.json`, `resume.json`
- 用途：记录需求分析S1-S4的执行情况，支持断点续跑

### 2. 流程连通性保证
- **主协调Agent统一调度** - 所有Agent由其协调调用
- **WORKFLOW.md定义完整调度规则** - 描述Agent如何协作
- **Skill间通过产物ID强关联** - 数据流转有明确规则
- **状态文件同步更新** - 确保状态一致性

### 3. 数据一致性保障
- 所有产物按统一模板输出
- 校验Agent确保输入输出格式正确
- 状态文件与产物文件同步更新
- 索引文件维护全局数据关系

### 4. 与编码实现的区别
- **Agent Prompt** = 告诉AI如何扮演角色和执行任务
- **Skill定义** = 告诉AI如何完成具体任务
- **WORKFLOW.md** = 告诉AI整体流程如何运转
- **状态文件** = 通过文件系统实现持久化
- **无需编码** = 所有逻辑通过自然语言描述，AI按描述执行

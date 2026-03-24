# Agent+Skill 框架 - 快速参考卡片

## 🚀 5 分钟快速开始

### 第 1 步：打开项目（1 分钟）
```
1. 启动 Trae IDE
2. 打开项目：e:\code\LLM\workspace\swf
3. 确认文件结构完整
```

### 第 2 步：执行第一个需求（3 分钟）
```
在 Trae IDE 对话框中输入：

"请作为 Coordinator Agent，执行以下需求：

需求描述：我想做一个刷题 APP。

请按照 WORKFLOW.md 定义的流程：
1. 执行 Skill0 制定 Plan
2. 评估信息完整度，确定执行模式
3. 初始化状态文件
4. 按 S1→S2→S3→S4 顺序执行各阶段 Skill
5. 在交互节点等待我的确认
6. 保存所有产物到 database/plans/{PlanID}/

请开始执行。"
```

### 第 3 步：查看结果（1 分钟）
```powershell
# 查看最新产物
Get-ChildItem database\plans -Directory | Sort-Object Name -Descending | Select-Object -First 1

# 查看最终产物内容
Get-Content database\plans\P000001\s4-summary.md | Select-Object -First 30
```

---

## 📋 核心命令速查

### 执行需求
```
请作为 Coordinator Agent，执行需求：[需求描述]
```

### 继续执行（断点续跑）
```
请读取 database/plans/{PlanID}/resume.json，从断点位置继续执行
```

### 查看状态
```powershell
Get-Content database\plans\P000001\status.json | ConvertFrom-Json | Select-Object status, currentStage
```

### 查看产物
```powershell
Get-ChildItem database\plans\P000001 -Name
```

---

## 🎯 双模式切换

| 模式 | 触发条件 | 执行 Skill | 用户交互 | 执行时间 |
|------|---------|-----------|---------|---------|
| **常规模式** | 评分 < 90 分 | 13 个（S0→S1→S2→S3→S4） | 3 个节点 | 30-45 分钟 |
| **轻量化模式** | 评分 ≥ 90 分 | 11 个（跳过 S2） | 无 | 10-15 分钟 |

**评分标准**（每项 0-20 分）：
- 产品目标清晰度
- 目标受众明确性
- 核心场景完整性
- 功能需求具体性
- 约束条件明确性

---

## 📁 文件结构速查

```
swf/
├── agents/                     # 4 个 Agent
│   ├── coordinator.md          # 主协调（调度）
│   ├── validator.md            # 格式校验（质检）
│   ├── user-interaction.md     # 用户交互（交互）
│   └── executor.md             # 技能执行（执行）
├── skills/                     # 13 个 Skill
│   ├── skill0-plan/            # S0: Plan 制定
│   ├── s1-requirements/        # S1: 需求采集
│   ├── s2-market/              # S2: 市场校验
│   ├── s3-technical/           # S3: 技术选型
│   └── s4-integration/         # S4: 需求整合
├── database/                   # 信息库
│   ├── index.json              # 全局索引
│   ├── status.json             # 当前状态
│   ├── resume.json             # 断点续跑
│   └── plans/                  # Plan 产物
├── examples/                   # 示例
│   ├── sample-requirement-vague.md      # 模糊需求
│   ├── sample-requirement-complete.md   # 完整需求
│   └── test-workflow.md                 # 测试流程
├── WORKFLOW.md                 # 工作流程
├── README-SETUP.md             # 配置指南
├── QUICKSTART.md               # 快速启动
└── CHECKLIST.md                # 检查清单
```

---

## 🔄 执行流程速查

```
用户输入需求
    ↓
【Skill0】制定 Plan → 生成 Plan ID → 评分 → 确定模式
    ↓
【S1】需求边界 → 显性需求 → 隐性需求 → 需求验证
    ↓
【交互节点 1】信息补全（用户确认）
    ↓
【S2】竞品分析 → 市场痛点验证（仅常规模式）
    ↓
【S3】风险识别 → 可行性评估 → 技术选型
    ↓
【交互节点 2】产物确认（用户确认）
    ↓
【S4】需求分类 → 优先级排序 → 核心提炼
    ↓
【交互节点 3】风险决策（如有高风险）
    ↓
输出最终产物（s4-summary.md）
```

---

## 💡 交互节点速查

### 节点 1：信息补全（S1 完成后）
```
AI：S1 阶段已完成，请确认或补充：
    1. 需求边界是否清晰？
    2. 是否有需要补充的目标用户？
    3. 是否有需要补充的使用场景？

用户输入：
- 确认：1 或 "确认"
- 补充：2 + 补充内容
```

### 节点 2：产物确认（S3 完成后）
```
AI：S3 阶段已完成，请确认：
    1. 技术路线是否合理？
    2. 技术选型是否符合预期？
    3. 是否继续执行 S4 阶段？

用户输入：
- 确认：1 或 "确认"
- 调整：2 + 调整建议
```

### 节点 3：风险决策（高风险时）
```
AI：识别到高风险项：
    [风险描述]
    - 影响：[影响说明]
    - 建议：[应对建议]

用户输入：
- 接受风险：1
- 调整需求：2
- 暂停讨论：3
```

---

## 📊 状态文件速查

### plan.json
```json
{
  "planId": "P000001",
  "planName": "刷题 APP",
  "executionMode": "normal",
  "score": 35,
  "status": "completed"
}
```

### status.json
```json
{
  "currentStage": "S4-completed",
  "status": "completed",
  "completedSkills": ["skill0", "skill1", ...],
  "skippedSkills": []
}
```

### resume.json
```json
{
  "lastCheckpoint": "s4-completed",
  "nextAction": "none",
  "planId": "P000001"
}
```

---

## 🐛 故障排查速查

### AI 不执行 Skill
```
解决：请明确指令
"请作为 Coordinator Agent，按照 WORKFLOW.md 定义的流程，
从 Skill0 开始执行，逐步完成各阶段 Skill。"
```

### 状态文件未更新
```
解决：要求 AI 手动创建
"请创建 database/plans/{PlanID}/status.json，
内容包含：currentStage, status, completedSkills"
```

### 模式切换不正确
```
解决：要求重新评分
"请按照 WORKFLOW.md 的评分标准重新评估信息完整度"
```

### 断点续跑失败
```
解决：明确指定 Plan ID
"请读取 database/plans/P000001/resume.json，
从断点位置继续执行"
```

---

## ✅ 检查清单速查

### 执行前
- [ ] 所有 Agent 文件存在
- [ ] 所有 Skill 文件存在
- [ ] WORKFLOW.md 存在
- [ ] database/目录存在
- [ ] 示例需求文件存在

### 执行中
- [ ] Plan ID 正确生成
- [ ] 评分合理
- [ ] 模式正确
- [ ] 状态文件更新
- [ ] 产物文件保存

### 执行后
- [ ] 所有产物文件存在
- [ ] status 为 completed
- [ ] s4-summary.md 内容完整
- [ ] 产物格式符合模板

---

## 📚 文档索引

| 文档 | 用途 | 位置 |
|------|------|------|
| **README-SETUP.md** | 详细配置指南 | 根目录 |
| **QUICKSTART.md** | 快速启动指南 | 根目录 |
| **CHECKLIST.md** | 完整检查清单 | 根目录 |
| **WORKFLOW.md** | 工作流程详解 | 根目录 |
| **test-workflow.md** | 测试流程 | examples/ |

---

## 🎓 最佳实践速查

### 需求描述技巧
✅ 好的需求：
- "面向小学 3-6 年级的课后刷题 APP，包含题库管理、错题本、进度追踪，开发周期 3 个月，预算 50 万"

❌ 差的需求：
- "做个刷题 APP"

### 交互反馈技巧
✅ 好的反馈：
- "目标用户建议增加'初中生群体'，因为产品可以扩展到中学市场"

❌ 差的反馈：
- "都可以"

### 产物管理技巧
✅ 好的做法：
- 每个 Plan 独立目录
- 定期备份产物
- 为产物添加版本注释

❌ 差的做法：
- 所有 Plan 混在一起
- 从不备份

---

## 🔢 关键数字

- **4 个 Agent**：coordinator, validator, user-interaction, executor
- **13 个 Skill**：S0-S4 五个阶段
- **5 个阶段**：S0（Plan 制定）→ S1（需求采集）→ S2（市场校验）→ S3（技术选型）→ S4（需求整合）
- **3 个交互节点**：信息补全、产物确认、风险决策
- **2 种执行模式**：常规模式（13 个 Skill）、轻量化模式（11 个 Skill）
- **90 分**：轻量化模式触发阈值
- **30-45 分钟**：常规模式执行时间
- **10-15 分钟**：轻量化模式执行时间

---

## 📞 快速帮助

### 查看完整文档
```powershell
# 配置指南
Get-Content README-SETUP.md | more

# 快速启动
Get-Content QUICKSTART.md | more

# 检查清单
Get-Content CHECKLIST.md | more

# 工作流程
Get-Content WORKFLOW.md | more
```

### 查看示例
```powershell
# 模糊需求示例
Get-Content examples\sample-requirement-vague.md | more

# 完整需求示例
Get-Content examples\sample-requirement-complete.md | more

# 测试流程
Get-Content examples\test-workflow.md | more
```

### 查看 Agent
```powershell
# 主协调 Agent
Get-Content agents\coordinator.md | more

# 格式校验 Agent
Get-Content agents\validator.md | more

# 用户交互 Agent
Get-Content agents\user-interaction.md | more

# 技能执行 Agent
Get-Content agents\executor.md | more
```

---

## 🎯 一句话总结

**这是一个基于 Prompt 的需求分析框架，通过 AI 自动执行 13 个 Skill，从模糊需求输出标准化需求文档，支持双模式切换和断点续跑。**

---

*快速参考卡片 v1.0*  
*最后更新：2026-03-24*  
*打印建议：A4 纸双面打印，随身携带*

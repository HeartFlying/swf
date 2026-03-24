# Agent+Skill 框架执行检查清单

## 执行前检查（Pre-flight Checklist）

### ✅ 文件完整性检查

#### Agent 文件（4 个）

- [ ] `agents/coordinator.md` - 主协调 Agent
- [ ] `agents/validator.md` - 格式校验守卫 Agent
- [ ] `agents/user-interaction.md` - 用户交互 Agent
- [ ] `agents/executor.md` - 技能执行 Agent

**验证命令**：
```powershell
Get-ChildItem agents -Name
```

**预期输出**：
```
coordinator.md
executor.md
user-interaction.md
validator.md
```

---

#### Skill 定义（5 个目录，13 个 Skill）

- [ ] `skills/skill0-plan/` - Plan 制定
- [ ] `skills/s1-requirements/` - 需求边界与原始采集（4 个 Skill）
- [ ] `skills/s2-market/` - 市场与需求价值校验（2 个 Skill）
- [ ] `skills/s3-technical/` - 技术可行性与选型（3 个 Skill）
- [ ] `skills/s4-integration/` - 需求整合与核心提炼（3 个 Skill）

**验证命令**：
```powershell
Get-ChildItem skills -Directory -Name
```

**预期输出**：
```
s1-requirements
s2-market
s3-technical
s4-integration
skill0-plan
```

---

#### Skill 文件详细检查

**S0 阶段**：
- [ ] `skills/skill0-plan/SKILL.md`
- [ ] `skills/skill0-plan/template.md`

**S1 阶段**：
- [ ] `skills/s1-requirements/skill1-boundary/SKILL.md`
- [ ] `skills/s1-requirements/skill1-boundary/template.md`
- [ ] `skills/s1-requirements/skill2-explicit/SKILL.md`
- [ ] `skills/s1-requirements/skill2-explicit/template.md`
- [ ] `skills/s1-requirements/skill3-implicit/SKILL.md`
- [ ] `skills/s1-requirements/skill3-implicit/template.md`
- [ ] `skills/s1-requirements/skill4-validation/SKILL.md`
- [ ] `skills/s1-requirements/skill4-validation/template.md`

**S2 阶段**：
- [ ] `skills/s2-market/skill9-competitor/SKILL.md`
- [ ] `skills/s2-market/skill9-competitor/template.md`
- [ ] `skills/s2-market/skill10-market/SKILL.md`
- [ ] `skills/s2-market/skill10-market/template.md`

**S3 阶段**：
- [ ] `skills/s3-technical/skill7-risk/SKILL.md`
- [ ] `skills/s3-technical/skill7-risk/template.md`
- [ ] `skills/s3-technical/skill11-feasibility/SKILL.md`
- [ ] `skills/s3-technical/skill11-feasibility/template.md`
- [ ] `skills/s3-technical/skill12-selection/SKILL.md`
- [ ] `skills/s3-technical/skill12-selection/template.md`

**S4 阶段**：
- [ ] `skills/s4-integration/skill5-classify/SKILL.md`
- [ ] `skills/s4-integration/skill5-classify/template.md`
- [ ] `skills/s4-integration/skill6-priority/SKILL.md`
- [ ] `skills/s4-integration/skill6-priority/template.md`
- [ ] `skills/s4-integration/skill8-core/SKILL.md`
- [ ] `skills/s4-integration/skill8-core/template.md`

---

#### 工作流程文档

- [ ] `WORKFLOW.md` - 主工作流程文档（1012 行）

**验证命令**：
```powershell
Test-Path WORKFLOW.md
```

**预期输出**：
```
True
```

---

#### 数据库文件

- [ ] `database/index.json` - 全局索引
- [ ] `database/status.json` - 当前状态
- [ ] `database/resume.json` - 断点续跑配置
- [ ] `database/plans/` - Plan 产物存储目录

**验证命令**：
```powershell
Get-ChildItem database -Name
```

**预期输出**：
```
index.json
resume.json
status.json
```

---

#### 项目文档

- [ ] `Plan-Status.json` - 实施状态追踪
- [ ] `Plan-Resume.json` - 实施断点续跑配置
- [ ] `README-SETUP.md` - 配置与执行指南
- [ ] `QUICKSTART.md` - 快速启动指南

---

#### 示例和测试

- [ ] `examples/sample-requirement-vague.md` - 模糊需求示例
- [ ] `examples/sample-requirement-complete.md` - 完整需求示例
- [ ] `examples/test-workflow.md` - 测试流程文档

---

### ✅ 环境检查

#### Trae IDE 环境

- [ ] Trae IDE 已安装并正常运行
- [ ] 项目已打开：`e:\code\LLM\workspace\swf`
- [ ] AI 功能已启用（Qwen3.5-Plus 或同等）
- [ ] 文件浏览器可用
- [ ] 终端可用（PowerShell）

**验证步骤**：
1. 打开 Trae IDE
2. 确认项目目录正确
3. 尝试打开一个 Agent 文件（如 `agents/coordinator.md`）
4. 确认文件内容正常显示

---

#### 文件系统权限

- [ ] 可读取项目文件
- [ ] 可创建新文件（在 `database/plans/` 目录）
- [ ] 可编辑文件（更新状态文件）

**验证命令**：
```powershell
# 测试读取
Get-Content database\index.json | Select-Object -First 1

# 测试创建（可选，谨慎执行）
# New-Item -Path "database\test.txt" -ItemType File -Force
# Remove-Item "database\test.txt" -Force
```

---

### ✅ 知识准备检查

#### 理解核心概念

- [ ] 理解 Agent+Skill 双层架构
- [ ] 理解 4 个 Agent 的职责分工
- [ ] 理解 5 个阶段（S0-S4）的执行顺序
- [ ] 理解双模式切换机制（常规模式 vs 轻量化模式）
- [ ] 理解断点续跑机制
- [ ] 理解 3 个用户交互节点

**自测问题**：
1. 哪个 Agent 负责调度？（答案：Coordinator）
2. 哪个 Agent 负责格式校验？（答案：Validator）
3. 常规模式执行多少个 Skill？（答案：13 个）
4. 轻量化模式跳过哪个阶段？（答案：S2）
5. 信息完整度评分≥多少分触发轻量化模式？（答案：90 分）

---

#### 熟悉文档结构

- [ ] 已阅读 `README-SETUP.md`（配置与执行指南）
- [ ] 已阅读 `QUICKSTART.md`（快速启动指南）
- [ ] 已浏览 `WORKFLOW.md`（工作流程）
- [ ] 已查看 `agents/coordinator.md`（主协调 Agent）

---

## 执行中检查（In-flight Checklist）

### ✅ Step 1：启动系统

**操作**：在 Trae IDE 中输入执行指令

**检查项**：
- [ ] AI 正确理解 Coordinator Agent 角色
- [ ] AI 加载 `agents/coordinator.md` 文件内容
- [ ] AI 理解 WORKFLOW.md 定义的流程

**预期响应**：
```
我已准备好作为 Coordinator Agent 执行任务。
将按以下步骤执行：
1. 执行 Skill0 制定 Plan
2. 评估信息完整度
3. 初始化状态文件
4. 按顺序执行各阶段 Skill
...
```

---

### ✅ Step 2：Skill0 执行

**检查项**：
- [ ] Plan ID 正确生成（格式：P{6 位数字}，如 P000001）
- [ ] 需求名称正确提取
- [ ] 信息完整度评分合理（0-100 分）
- [ ] 执行模式正确（normal 或 lightweight）
- [ ] `database/plans/{PlanID}/plan.json` 已创建

**验证命令**：
```powershell
# 查看 Plan 配置
Get-Content database\plans\P000001\plan.json | ConvertFrom-Json | Select-Object planId, planName, executionMode, score
```

**预期输出示例**：
```json
{
  "planId": "P000001",
  "planName": "刷题 APP",
  "executionMode": "normal",
  "score": 35
}
```

---

### ✅ Step 3：状态文件初始化

**检查项**：
- [ ] `database/plans/{PlanID}/status.json` 已创建
- [ ] `database/plans/{PlanID}/resume.json` 已创建
- [ ] 初始状态正确（currentStage: "S0"）
- [ ] 断点信息正确（checkpoint: "skill0-completed"）

**验证命令**：
```powershell
# 查看状态
Get-Content database\plans\P000001\status.json | ConvertFrom-Json | Select-Object currentStage, status

# 查看断点
Get-Content database\plans\P000001\resume.json | ConvertFrom-Json | Select-Object lastCheckpoint, nextAction
```

---

### ✅ Step 4：S1 阶段执行

**检查项**：
- [ ] Skill1（需求边界界定）执行完成
- [ ] Skill2（显性需求提取）执行完成
- [ ] Skill3（隐性需求挖掘）执行完成（常规模式）
- [ ] Skill4（需求验证）执行完成
- [ ] S1 阶段汇总产物已保存（s1-summary.md）
- [ ] status.json 已更新（currentStage: "S1-completed"）

**验证命令**：
```powershell
# 查看 S1 产物
Test-Path database\plans\P000001\s1-summary.md

# 查看状态
Get-Content database\plans\P000001\status.json | ConvertFrom-Json | Select-Object currentStage
```

**预期输出**：
```
True
currentStage: S1-completed
```

---

### ✅ Step 5：交互节点 1（信息补全）

**检查项**：
- [ ] AI 在 S1 完成后暂停
- [ ] AI 显示 S1 阶段产物摘要
- [ ] AI 提供交互选项（确认/补充/修改）
- [ ] AI 等待用户输入

**预期响应**：
```
【交互节点 1：信息补全】

S1 阶段已完成，产物摘要：
- 需求边界：...
- 显性需求：...
- 隐性需求：...

请确认或提出修改建议：
1. 确认（继续执行）
2. 补充/修改

请输入您的选择：
```

---

### ✅ Step 6：S2 阶段执行（仅常规模式）

**检查项**（仅当执行模式为 normal 时）：
- [ ] Skill9（竞品分析）执行完成
- [ ] Skill10（市场痛点验证）执行完成
- [ ] S2 阶段汇总产物已保存（s2-summary.md）
- [ ] status.json 已更新（currentStage: "S2-completed"）

**验证命令**：
```powershell
Test-Path database\plans\P000001\s2-summary.md
```

**轻量化模式检查**：
- [ ] S2 阶段标记为 skipped
- [ ] status.json 中 S2 阶段状态为 "skipped"

---

### ✅ Step 7：S3 阶段执行

**检查项**：
- [ ] Skill7（需求风险识别）执行完成
- [ ] Skill11（技术可行性评估）执行完成
- [ ] Skill12（轻量化技术选型）执行完成
- [ ] S3 阶段汇总产物已保存（s3-summary.md）
- [ ] status.json 已更新（currentStage: "S3-completed"）

**验证命令**：
```powershell
Test-Path database\plans\P000001\s3-summary.md
```

---

### ✅ Step 8：交互节点 2（产物确认）

**检查项**：
- [ ] AI 在 S3 完成后暂停
- [ ] AI 显示 S3 阶段产物摘要（技术路线、选型）
- [ ] AI 提供交互选项（确认/调整）
- [ ] AI 等待用户输入

**预期响应**：
```
【交互节点 2：产物确认】

S3 阶段已完成，产物摘要：
- 技术路线：...
- 技术选型：...
- 风险评估：...

请确认或提出调整建议：
1. 确认（继续执行 S4）
2. 调整

请输入您的选择：
```

---

### ✅ Step 9：S4 阶段执行

**检查项**：
- [ ] Skill5（需求分类梳理）执行完成
- [ ] Skill6（需求优先级排序）执行完成
- [ ] Skill8（核心需求提炼）执行完成
- [ ] S4 阶段汇总产物已保存（s4-summary.md）
- [ ] status.json 已更新（currentStage: "S4-completed", status: "completed"）

**验证命令**：
```powershell
# 查看最终产物
Test-Path database\plans\P000001\s4-summary.md

# 查看最终状态
Get-Content database\plans\P000001\status.json | ConvertFrom-Json | Select-Object status, currentStage
```

**预期输出**：
```
True
status: completed
currentStage: S4-completed
```

---

### ✅ Step 10：最终产物验证

**检查项**：
- [ ] `s4-summary.md` 包含完整内容
- [ ] 内容符合模板要求（元信息 + 主体内容）
- [ ] 包含产品目标、目标受众、核心场景
- [ ] 包含功能需求列表（MoSCoW 优先级）
- [ ] 包含技术选型建议
- [ ] 包含风险评估
- [ ] 产物 ID 正确关联

**验证命令**：
```powershell
# 查看产物内容（前 50 行）
Get-Content database\plans\P000001\s4-summary.md | Select-Object -First 50
```

---

## 执行后检查（Post-flight Checklist）

### ✅ 产物完整性

**所有 Plan 产物**：
- [ ] `database/plans/{PlanID}/plan.json`
- [ ] `database/plans/{PlanID}/status.json`
- [ ] `database/plans/{PlanID}/resume.json`
- [ ] `database/plans/{PlanID}/s1-summary.md`
- [ ] `database/plans/{PlanID}/s2-summary.md`（常规模式）或标记为 skipped
- [ ] `database/plans/{PlanID}/s3-summary.md`
- [ ] `database/plans/{PlanID}/s4-summary.md`

**验证命令**：
```powershell
Get-ChildItem database\plans\P000001 -Name
```

**预期输出**：
```
plan.json
resume.json
s1-summary.md
s2-summary.md
s3-summary.md
s4-summary.md
status.json
```

---

### ✅ 状态文件验证

**最终状态检查**：
- [ ] status.json 中 status 字段为 "completed"
- [ ] status.json 中 currentStage 字段为 "S4-completed"
- [ ] resume.json 中 lastCheckpoint 字段为 "s4-completed"
- [ ] resume.json 中 nextAction 字段为 "none"

**验证命令**：
```powershell
# 查看最终状态
$json = Get-Content database\plans\P000001\status.json | ConvertFrom-Json
Write-Host "Status: $($json.status)"
Write-Host "Current Stage: $($json.currentStage)"

# 查看断点
$resume = Get-Content database\plans\P000001\resume.json | ConvertFrom-Json
Write-Host "Last Checkpoint: $($resume.lastCheckpoint)"
Write-Host "Next Action: $($resume.nextAction)"
```

**预期输出**：
```
Status: completed
Current Stage: S4-completed
Last Checkpoint: s4-completed
Next Action: none
```

---

### ✅ 产物质量检查

**格式检查**：
- [ ] 所有 Markdown 文件语法正确
- [ ] 所有 JSON 文件可解析
- [ ] 产物 ID 格式正确（S{阶段}-{日期}-{序号}）
- [ ] 元信息完整（PlanID、阶段、执行模式等）

**内容检查**：
- [ ] 需求描述清晰、具体
- [ ] 功能列表完整（包含 MoSCoW 优先级）
- [ ] 技术选型合理（考虑团队、预算、时间）
- [ ] 风险评估全面（技术、市场、运营）
- [ ] 符合 SMART 原则

---

### ✅ 中心化信息库更新

**index.json 更新检查**：
- [ ] plans 数组已添加新 Plan
- [ ] stages 索引已更新
- [ ] 产物 ID 已记录

**验证命令**：
```powershell
# 查看 index.json
$json = Get-Content database\index.json | ConvertFrom-Json
Write-Host "Total Plans: $($json.plans.totalCount)"
Write-Host "Plans: $($json.plans.items | ConvertTo-Json -Compress)"
```

---

## 常见问题检查清单

### ❌ 问题 1：AI 不执行 Skill

**检查项**：
- [ ] 是否明确指定了 Coordinator Agent 角色？
- [ ] 是否提到了 WORKFLOW.md？
- [ ] 是否要求从 Skill0 开始执行？
- [ ] 是否提供了需求描述？

**解决方案**：
```
请作为 Coordinator Agent，按照 WORKFLOW.md 定义的流程，
从 Skill0 开始执行，逐步完成各阶段 Skill。

需求描述：[你的需求]
```

---

### ❌ 问题 2：状态文件未创建

**检查项**：
- [ ] AI 是否有文件创建能力？
- [ ] database/plans/{PlanID}/目录是否存在？
- [ ] 权限是否正确？

**解决方案**：
1. 要求 AI 手动创建文件
2. 如果 AI 无法创建，要求其输出完整内容，手动保存
3. 检查 Trae IDE 的文件写入权限

---

### ❌ 问题 3：模式切换不正确

**检查项**：
- [ ] 信息完整度评分是否合理？
- [ ] 评分标准是否正确应用？
- [ ] 是否理解常规模式和轻量化模式的区别？

**解决方案**：
```
请重新评估需求信息完整度，按照 WORKFLOW.md 的评分标准：
- 产品目标清晰度（0-20 分）
- 目标受众明确性（0-20 分）
- 核心场景完整性（0-20 分）
- 功能需求具体性（0-20 分）
- 约束条件明确性（0-20 分）

总分 < 90 分：常规模式
总分 ≥ 90 分：轻量化模式
```

---

### ❌ 问题 4：断点续跑失败

**检查项**：
- [ ] resume.json 是否存在？
- [ ] resume.json 内容是否正确？
- [ ] AI 是否正确读取 resume.json？

**解决方案**：
```
请读取 database/plans/{PlanID}/resume.json，
识别断点位置，从断点位置继续执行。

断点信息：
- 最后完成的 Skill: [查看 resume.json]
- 下一动作：[查看 resume.json]
```

---

## 快速验证脚本

### 一键验证所有文件

```powershell
# 验证 Agent 文件
Write-Host "=== Agent 文件检查 ==="
$agents = @("coordinator.md", "validator.md", "user-interaction.md", "executor.md")
foreach ($agent in $agents) {
    if (Test-Path "agents\$agent") {
        Write-Host "✓ $agent" -ForegroundColor Green
    } else {
        Write-Host "✗ $agent 缺失" -ForegroundColor Red
    }
}

# 验证 Skill 目录
Write-Host "`n=== Skill 目录检查 ==="
$skillDirs = @("skill0-plan", "s1-requirements", "s2-market", "s3-technical", "s4-integration")
foreach ($dir in $skillDirs) {
    if (Test-Path "skills\$dir") {
        Write-Host "✓ $dir" -ForegroundColor Green
    } else {
        Write-Host "✗ $dir 缺失" -ForegroundColor Red
    }
}

# 验证数据库文件
Write-Host "`n=== 数据库文件检查 ==="
$dbFiles = @("index.json", "status.json", "resume.json")
foreach ($file in $dbFiles) {
    if (Test-Path "database\$file") {
        Write-Host "✓ $file" -ForegroundColor Green
    } else {
        Write-Host "✗ $file 缺失" -ForegroundColor Red
    }
}

# 验证工作流程文档
Write-Host "`n=== 工作流程文档检查 ==="
if (Test-Path "WORKFLOW.md") {
    Write-Host "✓ WORKFLOW.md" -ForegroundColor Green
} else {
    Write-Host "✗ WORKFLOW.md 缺失" -ForegroundColor Red
}

Write-Host "`n=== 检查完成 ==="
```

---

## 总结

使用本检查清单确保：

1. **执行前**：所有文件完整、环境就绪、知识准备充分
2. **执行中**：每个步骤正确执行、状态正确更新、产物正确保存
3. **执行后**：产物完整、状态正确、质量合格

**最佳实践**：
- ✅ 每次执行前完成执行前检查
- ✅ 执行过程中按步骤检查
- ✅ 执行完成后完成执行后检查
- ✅ 发现问题及时记录并解决
- ✅ 定期检查清单更新

---

*检查清单 v1.0*  
*最后更新：2026-03-24*  
*适用范围：Agent+Skill 用户需求分析系统 v1.0*

# Agent+Skill 框架快速启动命令

## 方式 1：直接执行需求（推荐）

### 在 Trae IDE 对话框中输入：

```
请作为 Coordinator Agent（主协调 Agent），执行以下任务：

需求描述：我想做一个刷题 APP。

请按照以下步骤执行：
1. 执行 Skill0 制定 Plan，生成 Plan ID
2. 评估需求信息完整度，确定执行模式（常规/轻量化）
3. 初始化状态文件（status.json, resume.json）
4. 按照 S1→S2→S3→S4 的顺序逐步执行各阶段 Skill
5. 在交互节点暂停等待我的确认
6. 所有产物保存到 database/plans/{PlanID}/ 目录

参考文档：
- agents/coordinator.md - 你的角色定义
- WORKFLOW.md - 完整的工作流程
- database/index.json - 技能库索引

请开始执行。
```

---

## 方式 2：使用示例需求

### 步骤 1：查看示例需求

```bash
# 查看模糊需求示例（常规模式）
type examples\sample-requirement-vague.md

# 查看完整需求示例（轻量化模式）
type examples\sample-requirement-complete.md
```

### 步骤 2：在 Trae IDE 中输入

```
请作为 Coordinator Agent，执行以下需求：

[复制粘贴示例需求内容]

请按照 WORKFLOW.md 定义的流程执行，包括：
1. 执行 Skill0 制定 Plan
2. 评估信息完整度，自动切换执行模式
3. 初始化状态文件
4. 按顺序执行各阶段 Skill
5. 在交互节点等待我的确认
6. 保存所有产物到 database/plans/{PlanID}/

请开始执行。
```

---

## 方式 3：断点续跑

### 查看当前状态

```bash
# 查看执行状态
type database\status.json

# 查看断点续跑配置
type database\resume.json

# 查看所有 Plan
dir database\plans
```

### 恢复执行

```
请作为 Coordinator Agent，继续执行 Plan。

请执行以下步骤：
1. 读取 database/plans/{PlanID}/resume.json
2. 识别断点位置（当前阶段、已完成的 Skill）
3. 从断点位置继续执行
4. 不要重复执行已完成的 Skill

请继续执行。
```

---

## 方式 4：查看产物

### 查看最新 Plan

```bash
# 进入 plans 目录
cd database\plans

# 查看最新 Plan（按时间排序）
dir /O-D

# 进入 Plan 目录
cd P000001

# 查看产物
dir

# 查看 S4 阶段汇总（最终产物）
type s4-summary.md
```

### 查看状态

```bash
# 查看执行状态
type database\plans\P000001\status.json

# 查看 Plan 配置
type database\plans\P000001\plan.json
```

---

## 方式 5：测试模式

### 测试常规模式

```
请作为 Coordinator Agent，执行测试：

需求描述：我想做一个刷题 APP。

测试目标：验证常规模式完整流程
预期结果：
- 信息完整度评分 < 90 分
- 执行模式：normal
- 执行所有 13 个 Skill（S0→S1→S2→S3→S4）
- 触发 3 个交互节点

请开始执行并记录每个步骤的执行结果。
```

### 测试轻量化模式

```
请作为 Coordinator Agent，执行测试：

需求描述：[复制 examples/sample-requirement-complete.md 的完整需求]

测试目标：验证轻量化模式自动触发
预期结果：
- 信息完整度评分 ≥ 90 分
- 执行模式：lightweight
- 跳过 S2 阶段（Skill9、Skill10）
- 全程无用户交互

请开始执行并验证模式切换是否正确。
```

### 测试断点续跑

```
请作为 Coordinator Agent，执行断点续跑测试：

步骤 1：开始执行需求"我想做一个刷题 APP。"
步骤 2：执行到 S2 阶段后，我会说"暂停"
步骤 3：请保存断点到 resume.json
步骤 4：我说"继续"后，请从断点位置恢复执行
步骤 5：验证产物完整性

请开始执行步骤 1。
```

---

## 快速命令参考

### 查看文档

```bash
# 查看主工作流程
type WORKFLOW.md | more

# 查看 Coordinator Agent
type agents\coordinator.md | more

# 查看测试流程
type examples\test-workflow.md | more

# 查看配置指南
type README-SETUP.md | more
```

### 查看项目结构

```bash
# 查看完整项目结构
tree /F

# 查看 Agent 文件
dir agents

# 查看 Skill 文件
dir skills

# 查看数据库
dir database
```

### 清理和重置

```bash
# 清理测试产物（谨慎使用）
rmdir /S /Q database\plans\P000001

# 重置状态文件
del database\status.json
del database\resume.json

# 重新初始化（需要手动创建或从备份恢复）
```

---

## 执行检查清单

### 执行前检查

- [ ] 所有 Agent 文件已创建（agents/目录）
- [ ] 所有 Skill 定义已创建（skills/目录）
- [ ] WORKFLOW.md 已创建
- [ ] database/目录结构已初始化
- [ ] 示例需求文件已创建（examples/目录）

### 执行中检查

- [ ] Plan ID 正确生成（格式：P{6 位数字}）
- [ ] 信息完整度评分正确
- [ ] 执行模式正确切换
- [ ] 状态文件正确更新
- [ ] 产物文件正确保存

### 执行后检查

- [ ] 所有产物文件存在
- [ ] status.json 状态为 completed
- [ ] s4-summary.md 包含完整内容
- [ ] 产物格式符合模板要求
- [ ] 中心化信息库已更新

---

## 故障排查命令

### 检查文件完整性

```bash
# 检查 Agent 文件
if exist agents\coordinator.md (echo ✓ coordinator.md exists) else (echo ✗ coordinator.md missing)
if exist agents\validator.md (echo ✓ validator.md exists) else (echo ✗ validator.md missing)
if exist agents\user-interaction.md (echo ✓ user-interaction.md exists) else (echo ✗ user-interaction.md missing)
if exist agents\executor.md (echo ✓ executor.md exists) else (echo ✗ executor.md missing)

# 检查 Skill 文件
dir /B skills\skill0-plan\SKILL.md
dir /B skills\s1-requirements\skill1-boundary\SKILL.md

# 检查工作流程
if exist WORKFLOW.md (echo ✓ WORKFLOW.md exists) else (echo ✗ WORKFLOW.md missing)
```

### 检查状态文件

```bash
# 检查数据库索引
if exist database\index.json (echo ✓ index.json exists) else (echo ✗ index.json missing)

# 检查状态文件
if exist database\status.json (echo ✓ status.json exists) else (echo ✗ status.json missing)

# 检查断点续跑配置
if exist database\resume.json (echo ✓ resume.json exists) else (echo ✗ resume.json missing)
```

---

## 输出示例

### 成功的执行输出

```
【Plan 制定完成】
- Plan ID: P000001
- 需求名称：刷题 APP
- 信息完整度评分：35 分
- 执行模式：常规模式（normal）
- 执行 Skill：13 个（S0→S1→S2→S3→S4）

【S1 阶段完成】
- 已完成 Skill：skill1-boundary, skill2-explicit, skill3-implicit, skill4-validation
- 产物 ID: S1-20260324-001
- 状态：等待用户确认

【交互节点 1】
请确认 S1 阶段产物或提出修改建议：
1. 确认（继续执行）
2. 补充/修改

请输入您的选择：
```

### 失败的执行输出

```
【错误】前置校验失败

原因：缺少依赖产物
- 期望：S1-summary.md
- 实际：未找到

解决方案：
1. 检查上一阶段是否完成
2. 重新执行上一阶段
3. 手动创建依赖产物

请指示下一步操作。
```

---

## 最佳实践提示

### 💡 提示 1：明确指令

✅ 好的指令：
```
"请作为 Coordinator Agent，按照 WORKFLOW.md 定义的流程，
从 Skill0 开始执行，逐步完成各阶段 Skill。"
```

❌ 差的指令：
```
"帮我做个需求分析"
```

### 💡 提示 2：提供上下文

✅ 好的上下文：
```
"这是一个面向小学 3-6 年级的课后刷题 APP，
需要包含题库管理、错题本、进度追踪功能，
开发周期 3 个月，预算 50 万。"
```

❌ 差的上下文：
```
"做个 APP"
```

### 💡 提示 3：及时反馈

✅ 好的反馈：
```
"S1 阶段产物已确认。目标用户建议增加'初中生群体'，
因为产品可以扩展到中学市场。请继续执行。"
```

❌ 差的反馈：
```
"好的"
```

### 💡 提示 4：产物管理

✅ 好的做法：
- 每个 Plan 独立目录
- 定期备份产物
- 为产物添加版本注释

❌ 差的做法：
- 所有 Plan 混在一起
- 从不备份
- 产物命名混乱

---

## 下一步

执行成功后：

1. **查看产物**：`database\plans\P000001\s4-summary.md`
2. **验证质量**：检查产物是否符合模板要求
3. **导出分享**：将产物导出为 PDF/Word 分享给团队
4. **收集反馈**：收集团队对产物的意见和建议
5. **优化改进**：根据反馈优化需求和流程

---

*快速启动指南 v1.0*  
*最后更新：2026-03-24*

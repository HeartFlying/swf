# Skill0: Plan制定

## 基本信息

| 项目 | 内容 |
|-----|------|
| **Skill编号** | S0-S00 |
| **Skill名称** | Plan制定 |
| **所属阶段** | S0 - 初始化阶段 |
| **执行顺序** | 第1个执行（入口Skill） |
| **执行模式** | 常规模式/轻量化模式均执行 |
| **执行Agent** | Executor Agent |

---

## 功能描述

### 核心职责

Skill0是整个需求分析流程的入口点，负责：
1. **解析用户原始需求**：理解用户输入的需求描述
2. **生成Plan ID**：为本次需求分析分配唯一标识
3. **制定执行计划**：根据需求内容确定执行阶段和Skill序列
4. **初始化状态文件**：创建并初始化所有必要的状态文件
5. **评估信息完整度**：对需求信息进行评分，确定执行模式

### 输入输出

**输入**：
- 用户原始需求文本（自然语言描述）
- 可选：补充材料（如竞品链接、参考文档等）

**输出**：
- Plan定义文件（包含Plan ID、执行阶段、Skill序列）
- 初始化的status.json
- 初始化的resume.json
- 信息完整度评分报告

---

## 执行流程

```
接收用户原始需求
    ↓
解析需求内容，提取关键信息
    ↓
生成Plan ID
    ↓
评估信息完整度（4维度评分）
    ↓
确定执行模式（normal/lightweight）
    ↓
制定执行计划（确定执行阶段和Skill序列）
    ↓
初始化状态文件
    ↓
输出Plan定义文件
    ↓
返回执行结果给Coordinator
```

---

## 详细规范

### 1. Plan ID生成

**格式**：`P{6位数字}`，如 `P000001`

**生成规则**：
1. 取当前时间戳后6位（毫秒级）
2. 如冲突，追加1位随机数
3. 确保唯一性

**示例**：
```
时间戳: 2026-03-24T10:30:45.123Z → 取 "451230" → P451230
```

### 2. 信息完整度评分

**评分维度**（满分100分）：

| 维度 | 分值 | 评分标准 | 检查要点 |
|------|------|----------|----------|
| **边界清晰度** | 25分 | 产品目标/目标受众/核心场景 | 是否明确产品做什么、为谁做、在什么场景使用 |
| **需求具体度** | 25分 | 显性功能/非功能需求 | 是否列出具体功能点和性能/安全/体验要求 |
| **约束明确度** | 25分 | 时间/预算/技术/资源约束 | 是否明确交付时间、预算范围、技术栈、团队规模 |
| **目标明确度** | 25分 | 核心价值/商业目标/落地指标 | 是否说明解决什么问题、带来什么价值、如何衡量成功 |

**评分细则**：

**边界清晰度（25分）**：
- 产品目标明确（8分）：清晰描述产品要解决什么问题
- 目标受众明确（8分）：明确目标用户群体特征
- 核心场景明确（9分）：描述主要使用场景

**需求具体度（25分）**：
- 显性功能明确（12分）：列出核心功能点
- 非功能需求明确（13分）：性能、安全、体验等要求

**约束明确度（25分）**：
- 时间约束（6分）：交付时间要求
- 预算约束（6分）：预算范围
- 技术约束（7分）：技术栈限制
- 资源约束（6分）：团队规模/资源限制

**目标明确度（25分）**：
- 核心价值明确（12分）：产品带来的核心价值
- 商业目标明确（13分）：商业目标和成功指标

**执行模式判定**：
- 总分 ≥ 90分 → `lightweight` 模式
- 总分 < 90分 → `normal` 模式

### 3. 执行计划制定

**阶段定义**：

| 阶段 | 阶段编号 | 包含Skill | 说明 |
|------|----------|-----------|------|
| S0 | S0 | Skill0 | 初始化阶段（Plan制定） |
| S1 | S1 | Skill1-4 | 需求边界与原始采集 |
| S2 | S2 | Skill9-10 | 市场与需求价值校验 |
| S3 | S3 | Skill7,11-12 | 技术可行性与选型 |
| S4 | S4 | Skill5-6,8 | 需求整合与核心提炼 |

**常规模式执行序列**：
```
S0 → S1(S01→S02→S03→S04) → S2(S09→S10) → S3(S07→S11→S12) → S4(S05→S06→S08)
```

**轻量化模式执行序列**：
```
S0 → S1(S01→S02→S04) → S3(S07→S11) → S4(S05→S08)
```

**轻量化模式跳过的Skill**：
- Skill3: 隐性需求挖掘
- Skill9: 竞品分析
- Skill10: 市场痛点验证
- Skill12: 轻量化技术选型
- Skill6: 需求优先级排序（简化执行）

### 4. 状态文件初始化

**status.json 初始化内容**：
```json
{
  "planId": "{生成的Plan ID}",
  "version": "1.0",
  "createdAt": "{ISO时间戳}",
  "executionMode": "normal|lightweight",
  "currentStage": "S0",
  "currentSkill": "S00",
  "overallStatus": "in_progress",
  "stages": {
    "S0": {"status": "completed", "skills": [{"skillId": "S00", "status": "completed"}]},
    "S1": {"status": "pending", "skills": [...]},
    "S2": {"status": "pending", "skills": [...]},
    "S3": {"status": "pending", "skills": [...]},
    "S4": {"status": "pending", "skills": [...]}
  },
  "metadata": {
    "informationScore": {
      "total": 85,
      "dimensions": {
        "boundary": 20,
        "requirement": 22,
        "constraint": 20,
        "goal": 23
      }
    },
    "originalRequirement": "{用户原始需求文本}"
  }
}
```

**resume.json 初始化内容**：
```json
{
  "planId": "{生成的Plan ID}",
  "version": "1.0",
  "lastSavedAt": "{ISO时间戳}",
  "executionContext": {
    "currentStage": "S0",
    "currentSkill": "S00",
    "nextStage": "S1",
    "nextSkill": "S01",
    "executionMode": "normal|lightweight"
  },
  "pendingActions": [],
  "checkpoint": {
    "stage": "S0",
    "skill": "S00",
    "status": "completed",
    "canResume": true
  }
}
```

---

## 输出产物

### 产物1: Plan定义文件

**文件路径**：`database/plans/{PlanID}.json`

**内容结构**：
```json
{
  "planId": "P000001",
  "version": "1.0",
  "createdAt": "2026-03-24T10:30:45.123Z",
  "executionMode": "normal",
  "stages": [
    {
      "stageId": "S0",
      "stageName": "初始化阶段",
      "status": "completed",
      "skills": [
        {"skillId": "S00", "skillName": "Plan制定", "status": "completed"}
      ]
    },
    {
      "stageId": "S1",
      "stageName": "需求边界与原始采集",
      "status": "pending",
      "skills": [
        {"skillId": "S01", "skillName": "需求边界界定", "status": "pending"},
        {"skillId": "S02", "skillName": "显性需求提取", "status": "pending"},
        {"skillId": "S03", "skillName": "隐性需求挖掘", "status": "pending"},
        {"skillId": "S04", "skillName": "需求验证", "status": "pending"}
      ]
    },
    {
      "stageId": "S2",
      "stageName": "市场与需求价值校验",
      "status": "pending",
      "skills": [
        {"skillId": "S09", "skillName": "竞品分析", "status": "pending"},
        {"skillId": "S10", "skillName": "市场痛点验证", "status": "pending"}
      ]
    },
    {
      "stageId": "S3",
      "stageName": "技术可行性与选型",
      "status": "pending",
      "skills": [
        {"skillId": "S07", "skillName": "需求风险识别", "status": "pending"},
        {"skillId": "S11", "skillName": "技术可行性评估", "status": "pending"},
        {"skillId": "S12", "skillName": "轻量化技术选型", "status": "pending"}
      ]
    },
    {
      "stageId": "S4",
      "stageName": "需求整合与核心提炼",
      "status": "pending",
      "skills": [
        {"skillId": "S05", "skillName": "需求分类梳理", "status": "pending"},
        {"skillId": "S06", "skillName": "需求优先级排序", "status": "pending"},
        {"skillId": "S08", "skillName": "核心需求提炼", "status": "pending"}
      ]
    }
  ],
  "informationScore": {
    "total": 85,
    "dimensions": {
      "boundary": 20,
      "requirement": 22,
      "constraint": 20,
      "goal": 23
    },
    "executionMode": "normal"
  },
  "originalRequirement": "{用户原始需求文本}"
}
```

### 产物2: 信息完整度评分报告

**文件路径**：`database/stages/s0/{PlanID}-S0-S00-001-score.md`

**内容结构**：参见 [template.md](template.md)

---

## 错误处理

### 前置校验错误

| 错误类型 | 错误码 | 处理策略 |
|----------|--------|----------|
| 需求文本为空 | E001 | 返回错误，要求用户提供需求描述 |
| 需求文本过短（<10字） | E002 | 返回警告，建议补充更多细节 |
| 需求文本包含敏感信息 | E003 | 返回警告，提醒用户注意信息安全 |

### 执行过程错误

| 错误类型 | 错误码 | 处理策略 |
|----------|--------|----------|
| Plan ID生成冲突 | E101 | 重新生成，最多重试3次 |
| 文件写入失败 | E102 | 记录错误日志，返回失败状态 |
| JSON序列化失败 | E103 | 检查数据结构，返回失败状态 |

### 后置校验错误

| 错误类型 | 错误码 | 处理策略 |
|----------|--------|----------|
| 产物文件不存在 | E201 | 重新执行产物生成 |
| 产物JSON格式错误 | E202 | 重新生成产物文件 |
| 必填字段缺失 | E203 | 补充缺失字段，重新生成 |

---

## 协作接口

### 与Coordinator Agent的协作

**调用方式**：Coordinator通过Executor Agent调用Skill0

**输入参数**：
```json
{
  "action": "execute_skill",
  "skillId": "S00",
  "input": {
    "originalRequirement": "用户原始需求文本",
    "supplementaryMaterials": []
  }
}
```

**输出结果**：
```json
{
  "status": "success|failed",
  "planId": "P000001",
  "executionMode": "normal|lightweight",
  "outputs": [
    {
      "artifactId": "P000001-S0-S00-001",
      "artifactType": "plan_definition",
      "filePath": "database/plans/P000001.json"
    },
    {
      "artifactId": "P000001-S0-S00-001-score",
      "artifactType": "score_report",
      "filePath": "database/stages/s0/P000001-S0-S00-001-score.md"
    }
  ],
  "nextStage": "S1",
  "nextSkill": "S01"
}
```

### 与Validator Agent的协作

**前置校验**：Validator检查输入数据完整性
**后置校验**：Validator检查产物文件格式和内容

### 与UserInteraction Agent的协作

**交互场景**：
- 当需求信息不完整时，触发用户交互请求补充信息
- 当评分结果处于临界值（85-95分）时，询问用户是否采用轻量化模式

---

## 执行示例

### 示例1: 完整需求输入

**输入**：
```
我想开发一个面向大学生的时间管理APP，帮助用户管理学习计划和任务。
核心功能包括：任务创建、日程安排、番茄钟、学习统计。
目标用户是18-25岁的大学生，主要在校园场景使用。
要求3个月内完成MVP，预算10万以内，使用Flutter开发。
目标是提高学生学习效率，预期日活用户达到1000人。
```

**评分结果**：
- 边界清晰度：23/25（产品目标、受众、场景都较明确）
- 需求具体度：24/25（功能点清晰，但非功能需求可补充）
- 约束明确度：25/25（时间、预算、技术、资源都明确）
- 目标明确度：23/25（核心价值和商业目标明确）
- **总分：95分 → lightweight模式**

### 示例2: 简略需求输入

**输入**：
```
我想做一个时间管理APP。
```

**评分结果**：
- 边界清晰度：12/25（仅知道产品类型）
- 需求具体度：5/25（无具体功能描述）
- 约束明确度：3/25（无约束信息）
- 目标明确度：5/25（无明确目标）
- **总分：25分 → normal模式**

---

## 版本历史

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| 1.0 | 2026-03-24 | 初始版本，定义Skill0完整规范 |

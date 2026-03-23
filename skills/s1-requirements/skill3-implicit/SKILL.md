# Skill3: 隐性需求挖掘

## 基本信息

| 项目 | 内容 |
|-----|------|
| **Skill编号** | S1-S03 |
| **Skill名称** | 隐性需求挖掘 |
| **所属阶段** | S1 - 需求边界与原始采集 |
| **执行顺序** | S1阶段第3个执行 |
| **执行模式** | 仅常规模式执行（轻量化模式跳过） |
| **执行Agent** | Executor Agent |
| **依赖Skill** | S1-S02 (显性需求提取) |

---

## 功能描述

### 核心职责

Skill3负责挖掘用户未明确表达但潜在的隐性需求，包括：
1. **场景延伸分析**：基于核心场景推导关联场景
2. **痛点深度挖掘**：识别用户未言明的深层痛点
3. **期望价值推导**：推导用户的潜在期望和价值诉求
4. **竞品对标分析**：基于竞品功能推导用户可能期望的功能
5. **趋势预判**：结合行业趋势推导未来需求

### 输入输出

**输入**：
- Plan定义文件
- 需求边界界定报告（S1-S01产物）
- 显性需求清单（S1-S02产物）
- 用户原始需求文本

**输出**：
- 隐性需求挖掘报告 (`database/stages/s1/{PlanID}-S1-S03-001-implicit.md`)
- 隐性需求JSON (`database/stages/s1/{PlanID}-S1-S03-001-implicit.json`)
- 更新status.json中S1-S03状态

---

## 执行流程

```
读取显性需求和边界界定报告
    ↓
场景延伸分析（核心场景→关联场景）
    ↓
痛点深度挖掘（表层痛点→深层痛点）
    ↓
期望价值推导（明确期望→潜在期望）
    ↓
竞品对标分析（对标竞品功能）
    ↓
趋势预判（行业趋势→未来需求）
    ↓
隐性需求验证（与显性需求去重）
    ↓
输出隐性需求清单
    ↓
更新状态文件
```

---

## 详细规范

### 1. 场景延伸分析

**分析方法**：

| 分析维度 | 说明 | 示例 |
|----------|------|------|
| **时间维度** | 前序场景→核心场景→后续场景 | 准备学习→学习过程→学习复盘 |
| **空间维度** | 不同地点的使用场景 | 宿舍、图书馆、教室、咖啡厅 |
| **角色维度** | 不同用户角色的场景 | 学生、助教、老师 |
| **频次维度** | 高频/低频场景的补充 | 日常打卡→周总结→月复盘 |

**场景延伸模板**：
```json
{
  "scenarioExtension": [
    {
      "baseScenario": "核心场景",
      "extendedScenarios": [
        {
          "scenarioId": "ES001",
          "scenarioName": "延伸场景名称",
          "extensionType": "time|space|role|frequency",
          "description": "场景描述",
          "userValue": "用户价值",
          "confidence": "high|medium|low",
          "evidence": "推导依据"
        }
      ]
    }
  ]
}
```

### 2. 痛点深度挖掘

**痛点分层模型**：

| 层级 | 定义 | 挖掘方法 | 示例 |
|------|------|----------|------|
| **表层痛点** | 用户直接表达的问题 | 需求文本分析 | "忘记任务截止时间" |
| **中层痛点** | 表层痛点背后的原因 | 5Why分析法 | 缺乏有效提醒机制 |
| **深层痛点** | 根本原因和情感诉求 | 情感地图分析 | 焦虑感、失控感 |

**痛点挖掘模板**：
```json
{
  "painPoints": [
    {
      "painId": "PP001",
      "surfacePain": "表层痛点",
      "middlePain": "中层痛点",
      "deepPain": "深层痛点",
      "emotionalAppeal": "情感诉求",
      "frequency": "high|medium|low",
      "impact": "high|medium|low",
      "confidence": "high|medium|low"
    }
  ]
}
```

### 3. 期望价值推导

**价值推导框架**：

| 价值类型 | 说明 | 推导方法 | 示例 |
|----------|------|----------|------|
| **功能价值** | 完成特定任务的能力 | 功能缺失分析 | 批量导入任务 |
| **效率价值** | 提升操作效率 | 流程优化分析 | 一键生成周报 |
| **情感价值** | 满足情感需求 | 情感地图分析 | 成就感、掌控感 |
| **社交价值** | 满足社交需求 | 社交需求分析 | 学习小组、排行榜 |

### 4. 竞品对标分析

**对标维度**：

| 维度 | 说明 | 分析方法 |
|------|------|----------|
| **功能对标** | 竞品具备但本产品缺失的功能 | 功能清单对比 |
| **体验对标** | 竞品的交互和视觉优势 | 体验走查 |
| **模式对标** | 竞品的商业模式和运营策略 | 商业模式分析 |

### 5. 趋势预判

**趋势分析维度**：

| 维度 | 说明 | 信息来源 |
|------|------|----------|
| **技术趋势** | AI、AR/VR等新技术应用 | 技术报告、专利分析 |
| **用户趋势** | 用户行为和偏好变化 | 用户研究、数据分析 |
| **行业趋势** | 行业发展方向和监管政策 | 行业报告、政策文件 |

---

## 输出产物

### 产物1: 隐性需求挖掘报告

**文件路径**：`database/stages/s1/{PlanID}-S1-S03-001-implicit.md`

**内容结构**：参见 [template.md](template.md)

### 产物2: 隐性需求JSON

**文件路径**：`database/stages/s1/{PlanID}-S1-S03-001-implicit.json`

**内容结构**：
```json
{
  "artifactId": "{PlanID}-S1-S03-001",
  "planId": "{PlanID}",
  "skillId": "S03",
  "version": "1.0",
  "createdAt": "{ISO时间戳}",
  "implicitRequirements": {
    "scenarioExtensions": [...],
    "painPoints": [...],
    "expectedValues": [...],
    "competitiveGaps": [...],
    "futureTrends": [...]
  },
  "statistics": {
    "totalCount": 0,
    "highConfidenceCount": 0,
    "mediumConfidenceCount": 0,
    "lowConfidenceCount": 0
  },
  "recommendations": [...]
}
```

---

## 错误处理

### 前置校验错误

| 错误类型 | 错误码 | 处理策略 |
|----------|--------|----------|
| 显性需求清单不存在 | E001 | 返回错误，要求先执行Skill2 |
| 边界界定报告不存在 | E002 | 返回错误，要求先执行Skill1 |

### 执行过程错误

| 错误类型 | 错误码 | 处理策略 |
|----------|--------|----------|
| 推导依据不足 | E101 | 降低置信度标记，继续执行 |
| 与显性需求重复 | E102 | 去重处理，标记来源 |

---

## 协作接口

### 与Coordinator Agent的协作

**输出结果**：
```json
{
  "status": "success|failed",
  "artifactId": "P000001-S1-S03-001",
  "outputs": [
    {
      "artifactType": "implicit_requirements_report",
      "filePath": "database/stages/s1/P000001-S1-S03-001-implicit.md"
    },
    {
      "artifactType": "implicit_requirements_json",
      "filePath": "database/stages/s1/P000001-S1-S03-001-implicit.json"
    }
  ],
  "nextSkill": "S04",
  "statistics": {
    "totalImplicitRequirements": 15,
    "highConfidence": 8,
    "mediumConfidence": 5,
    "lowConfidence": 2
  }
}
```

---

## 版本历史

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| 1.0 | 2026-03-24 | 初始版本，定义Skill3完整规范 |

# Skill4: 需求验证

## 基本信息

| 项目 | 内容 |
|-----|------|
| **Skill编号** | S1-S04 |
| **Skill名称** | 需求验证 |
| **所属阶段** | S1 - 需求边界与原始采集 |
| **执行顺序** | S1阶段第4个执行（S1阶段最后一个） |
| **执行模式** | 常规模式/轻量化模式均执行 |
| **执行Agent** | Executor Agent |
| **依赖Skill** | S1-S01/S02/S03 (根据执行模式) |

---

## 功能描述

### 核心职责

Skill4负责对S1阶段收集的所有需求进行验证和确认，包括：
1. **需求完整性验证**：检查需求是否完整、无遗漏
2. **需求一致性验证**：检查需求之间是否存在冲突
3. **需求可行性初判**：初步判断需求的技术和业务可行性
4. **需求价值评估**：评估需求的用户价值和商业价值
5. **生成S1阶段总结**：汇总S1阶段所有产物，生成阶段总结报告

### 输入输出

**输入**：
- Plan定义文件
- 需求边界界定报告（S1-S01产物）
- 显性需求清单（S1-S02产物）
- 隐性需求挖掘报告（S1-S03产物，常规模式）

**输出**：
- 需求验证报告 (`database/stages/s1/{PlanID}-S1-S04-001-validation.md`)
- 需求验证JSON (`database/stages/s1/{PlanID}-S1-S04-001-validation.json`)
- S1阶段总结报告 (`database/stages/s1/{PlanID}-S1-summary.md`)
- 更新status.json中S1阶段状态

---

## 执行流程

```
读取S1阶段所有产物
    ↓
需求完整性验证
    ↓
需求一致性验证
    ↓
需求可行性初判
    ↓
需求价值评估
    ↓
识别问题需求和风险
    ↓
生成验证报告
    ↓
生成S1阶段总结
    ↓
更新状态文件（标记S1完成）
    ↓
返回执行结果
```

---

## 详细规范

### 1. 需求完整性验证

**验证维度**：

| 维度 | 验证内容 | 验证标准 |
|------|----------|----------|
| **功能覆盖** | 是否覆盖所有用户场景 | 每个核心场景至少有一个功能支持 |
| **非功能覆盖** | 是否考虑性能/安全/体验 | 关键非功能需求已识别 |
| **边界覆盖** | 是否考虑异常和边界情况 | 主要异常场景已识别 |
| **依赖覆盖** | 是否识别需求间依赖 | 关键依赖关系已明确 |

**完整性检查清单**：
```json
{
  "completenessCheck": {
    "functionalCoverage": {
      "status": "pass|warning|fail",
      "coveredScenarios": [],
      "missingScenarios": []
    },
    "nonFunctionalCoverage": {
      "status": "pass|warning|fail",
      "coveredTypes": [],
      "missingTypes": []
    },
    "boundaryCoverage": {
      "status": "pass|warning|fail",
      "coveredCases": [],
      "missingCases": []
    }
  }
}
```

### 2. 需求一致性验证

**一致性检查类型**：

| 检查类型 | 说明 | 示例 |
|----------|------|------|
| **功能冲突** | 两个需求功能互相矛盾 | 需求A要求快速登录，需求B要求复杂安全验证 |
| **边界冲突** | 需求与边界定义冲突 | 需求超出产品边界范围 |
| **优先级冲突** | 资源限制下的优先级矛盾 | P0需求过多，资源不足 |
| **依赖冲突** | 需求间依赖关系矛盾 | A依赖B，但B优先级低于A |

### 3. 需求可行性初判

**可行性评估维度**：

| 维度 | 评估内容 | 评估等级 |
|------|----------|----------|
| **技术可行性** | 当前技术能否实现 | 高/中/低 |
| **资源可行性** | 现有资源能否支持 | 高/中/低 |
| **时间可行性** | 时间内能否完成 | 高/中/低 |
| **业务可行性** | 业务逻辑是否成立 | 高/中/低 |

### 4. 需求价值评估

**价值评估框架**：

| 价值类型 | 评估指标 | 评分标准 |
|----------|----------|----------|
| **用户价值** | 解决用户痛点程度 | 1-5分 |
| **业务价值** | 对业务目标的贡献 | 1-5分 |
| **技术价值** | 技术积累和复用 | 1-5分 |
| **创新价值** | 差异化竞争力 | 1-5分 |

---

## 输出产物

### 产物1: 需求验证报告

**文件路径**：`database/stages/s1/{PlanID}-S1-S04-001-validation.md`

**内容结构**：参见 [template.md](template.md)

### 产物2: 需求验证JSON

**文件路径**：`database/stages/s1/{PlanID}-S1-S04-001-validation.json`

**内容结构**：
```json
{
  "artifactId": "{PlanID}-S1-S04-001",
  "planId": "{PlanID}",
  "skillId": "S04",
  "version": "1.0",
  "createdAt": "{ISO时间戳}",
  "validation": {
    "completeness": {
      "status": "pass|warning|fail",
      "score": 85,
      "issues": []
    },
    "consistency": {
      "status": "pass|warning|fail",
      "conflicts": []
    },
    "feasibility": {
      "status": "pass|warning|fail",
      "assessments": []
    },
    "value": {
      "status": "pass|warning|fail",
      "evaluations": []
    }
  },
  "validatedRequirements": {
    "approved": [],
    "conditional": [],
    "rejected": []
  },
  "risks": [],
  "recommendations": []
}
```

### 产物3: S1阶段总结报告

**文件路径**：`database/stages/s1/{PlanID}-S1-summary.md`

**内容结构**：
- S1阶段执行概况
- 所有产物清单
- 关键结论
- 进入S2阶段的准备事项

---

## 错误处理

### 前置校验错误

| 错误类型 | 错误码 | 处理策略 |
|----------|--------|----------|
| 前置Skill产物缺失 | E001 | 返回错误，要求先执行前置Skill |
| 需求数据不完整 | E002 | 警告，标记缺失数据 |

### 执行过程错误

| 错误类型 | 错误码 | 处理策略 |
|----------|--------|----------|
| 验证规则冲突 | E101 | 标记冲突，请求决策 |
| 评估数据不足 | E102 | 标记为待补充 |

---

## 协作接口

### 与Coordinator Agent的协作

**输出结果**：
```json
{
  "status": "success|failed",
  "artifactId": "P000001-S1-S04-001",
  "outputs": [
    {
      "artifactType": "validation_report",
      "filePath": "database/stages/s1/P000001-S1-S04-001-validation.md"
    },
    {
      "artifactType": "validation_json",
      "filePath": "database/stages/s1/P000001-S1-S04-001-validation.json"
    },
    {
      "artifactType": "stage_summary",
      "filePath": "database/stages/s1/P000001-S1-summary.md"
    }
  ],
  "nextStage": "S2",
  "nextSkill": "S09",
  "stageCompleted": true
}
```

---

## 版本历史

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| 1.0 | 2026-03-24 | 初始版本，定义Skill4完整规范 |

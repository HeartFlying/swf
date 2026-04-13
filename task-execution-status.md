# Agents 与 Skills 引用关系修复 - 任务执行状态表

**文档版本**: 1.0
**创建日期**: 2026-04-14
**最后更新**: 2026-04-14（阶段 2 完成）

---

## 总体进度

| 阶段 | 状态 | 开始时间 | 完成时间 | 备注 |
|------|------|----------|----------|------|
| 阶段 1：止血修复 | ✅ 已完成 | 2026-04-14 | 2026-04-14 | P0 问题修复，已提交 7 个 commit |
| 阶段 2：契约收敛 | ✅ 已完成 | 2026-04-14 | 2026-04-14 | 创建 manifest，添加 Contract 区块 |
| 阶段 3：共享规范重构 | ⬜ 待开始 | - | - | 消除 references 复制扩散 |
| 阶段 4：校验与治理 | ⬜ 待开始 | - | - | 防止问题复发 |

**状态图例**: ⬜ 待开始 | 🔄 进行中 | ✅ 已完成 | ❌ 阻塞

---

## 阶段 1：止血修复（P0 问题）

### 1.1 修复 agents/coordinator-requirements.md

| 序号 | 修改项 | 行号 | 当前值 | 正确值 | 状态 | 执行人 | 完成时间 |
|------|--------|------|--------|--------|------|--------|----------|
| 1.1.1 | 轻量化跳过列表 | 64 | `跳过 S101, S102, S203, S404` | `跳过 S101, S102, S203, S406` | ✅ | Claude | 2026-04-14 |
| 1.1.2 | S4 阶段 Skill 列表 | 76 | `S401, S402, S403, S404, S405` | `S401, S402, S403, S405, S406` | ✅ | Claude | 2026-04-14 |
| 1.1.3 | S4 轻量化跳过 | 76 | `S404, S405` | `S406` | ✅ | Claude | 2026-04-14 |
| 1.1.4 | S301 名称 | 230 | `S301 - 风险识别` | `S301 - 技术可行性评估` | ✅ | Claude | 2026-04-14 |
| 1.1.5 | S302 名称 | 236 | `S302 - 技术可行性` | `S302 - 技术选型` | ✅ | Claude | 2026-04-14 |
| 1.1.6 | S303 名称 | 242 | `S303 - 技术选型` | `S303 - 非功能需求定义` | ✅ | Claude | 2026-04-14 |

**验收标准**: 文件中无 S404 旧编号残留，S3 阶段名称与 WORKFLOW.md 一致

---

### 1.2 修复 skills/s0-plan/SKILL.md

| 序号 | 修改项 | 行号 | 当前值 | 正确值 | 状态 | 执行人 | 完成时间 |
|------|--------|------|--------|--------|------|--------|----------|
| 1.2.1 | 元信息后置 Skill | 20 | `S101 (需求边界界定)` | `S201 (需求边界界定)` | ✅ | Claude | 2026-04-14 |
| 1.2.2 | 执行流程后置 Skill | 155-156 | `S101 (需求边界界定)` | `S201 (需求边界界定)` | ✅ | Claude | 2026-04-14 |

**验收标准**: 后置 Skill 编号为 S201，与 WORKFLOW.md 一致

---

### 1.3 修复 skills/s2-validation/SKILL.md

| 序号 | 修改项 | 行号 | 当前值 | 正确值 | 状态 | 执行人 | 完成时间 |
|------|--------|------|--------|--------|------|--------|----------|
| 1.3.1 | 全文替换 S104 | 81, 87-89, 109, 111, 117-119, 130, 151, 160, 183, 284 等 | `S104` | `S204` | ✅ | Claude | 2026-04-14 |
| 1.3.2 | 产物路径更新 | 87-89 | `S1-S104` | `S2-S204` | ✅ | Claude | 2026-04-14 |
| 1.3.3 | 阶段引用更新 | 109, 111 | `S1 阶段` | `S2 阶段` | ✅ | Claude | 2026-04-14 |

**验收标准**: 文件中无 S104 旧编号残留，产物路径使用 S2-S204 格式

**备注**: 经检查该文件已正确使用 S204 编号，无需修改

---

### 1.4 修复 skills/s4-user-stories/SKILL.md

| 序号 | 修改项 | 行号 | 当前值 | 正确值 | 状态 | 执行人 | 完成时间 |
|------|--------|------|--------|--------|------|--------|----------|
| 1.4.1 | 元信息后置 Skill | 20 | `S404 (原型设计)` | `S406 (原型设计)` | ✅ | Claude | 2026-04-14 |
| 1.4.2 | 执行流程后置 Skill | 140 | `S404 (原型设计)` | `S406 (原型设计)` | ✅ | Claude | 2026-04-14 |

**验收标准**: 后置 Skill 编号为 S406，与 WORKFLOW.md 一致

---

### 1.5 修复 skills/s5-vision/SKILL.md

| 序号 | 修改项 | 行号 | 当前值 | 正确值 | 状态 | 执行人 | 完成时间 |
|------|--------|------|--------|--------|------|--------|----------|
| 1.5.1 | 输入产物-需求边界 | 55, 80 | `{PlanID}-S1-S101-001` | `{PlanID}-S2-S201-001` | ✅ | Claude | 2026-04-14 |
| 1.5.2 | 输入产物-显性需求 | 56, 81 | `{PlanID}-S1-S102-001` | `{PlanID}-S2-S202-001` | ✅ | Claude | 2026-04-14 |
| 1.5.3 | 输入产物-需求验证 | 57, 82 | `{PlanID}-S1-S104-001` | `{PlanID}-S2-S204-001` | ✅ | Claude | 2026-04-14 |

**验收标准**: 输入产物编号使用 S2 阶段编号，与 WORKFLOW.md 一致

---

### 1.6 修复 skills/cm-impact-analysis/SKILL.md

| 序号 | 修改项 | 行号 | 当前值 | 正确值 | 状态 | 执行人 | 完成时间 |
|------|--------|------|--------|--------|------|--------|----------|
| 1.6.1 | S4 重执行路径 | 157-159 | `S404` | `S405 → S406` | ✅ | Claude | 2026-04-14 |
| 1.6.2 | S6 完整路径 | 161 | `S6-A01 → S6-A02 → S6-A03` | `S6-A01 → S6-A02 → S6-A03 → S6-A04` | ✅ | Claude | 2026-04-14 |

**验收标准**: 重执行路径包含 S406 和 S6-A04

---

### 1.7 处理 s3-nfr 和 s4-user-stories 缺失的 references

| 序号 | 修改项 | 说明 | 状态 | 执行人 | 完成时间 |
|------|--------|------|------|--------|----------|
| 1.7.1 | s3-nfr references 检查 | 检查并记录缺失文件 | ⬜ | - | - |
| 1.7.2 | s4-user-stories references 检查 | 检查并记录缺失文件 | ⬜ | - | - |
| 1.7.3 | 临时处理方案 | 修改 SKILL.md 引用说明，标注阶段 3 统一处理 | ⬜ | - | - |

**验收标准**: 缺失文件已记录，临时方案已实施

**备注**: 延后至阶段 3 统一处理

---

### 阶段 1 验收检查

| 序号 | 检查项 | 检查方法 | 预期结果 | 状态 | 完成时间 |
|------|--------|----------|----------|------|----------|
| V1.1 | S104 残留检查 | 全局搜索 `\bS104\b` | 仅评审文档和版本记录中出现 | ✅ | 2026-04-14 |
| V1.2 | S404 残留检查 | 全局搜索 `\bS404\b` | 仅评审文档和版本记录中出现 | ✅ | 2026-04-14 |
| V1.3 | 后置 Skill 一致性 | 对比各 SKILL.md 与 WORKFLOW.md | 全部一致 | ✅ | 2026-04-14 |
| V1.4 | S3 阶段名称 | 检查 coordinator-requirements.md | 与 WORKFLOW.md 一致 | ✅ | 2026-04-14 |

---

## 阶段 2：契约收敛

### 2.1 创建 agents/workflow-manifest.yaml

| 序号 | 修改项 | 说明 | 状态 | 执行人 | 完成时间 |
|------|--------|------|------|--------|----------|
| 2.1.1 | 创建文件 | 在 agents 目录下创建 workflow-manifest.yaml | ✅ | Claude | 2026-04-14 |
| 2.1.2 | 定义阶段 | S0-S6 + CM 共 8 个阶段定义 | ✅ | Claude | 2026-04-14 |
| 2.1.3 | 定义 Skills | 27 个 Skill 定义（id, dir, stage, order, depends_on, next, outputs） | ✅ | Claude | 2026-04-14 |
| 2.1.4 | 定义阶段交接 | S4→S5, S5→S6 交接定义 | ✅ | Claude | 2026-04-14 |

**验收标准**: manifest 文件格式正确，包含完整的阶段和 Skill 定义

---

### 2.2 为每个 SKILL.md 补充 Contract 区块

| 序号 | Skill 目录 | 状态 | 执行人 | 完成时间 |
|------|------------|------|--------|----------|
| 2.2.1 | skills/s0-plan | ✅ | Claude | 2026-04-14 |
| 2.2.2 | skills/s1-competitor | ✅ | Claude | 2026-04-14 |
| 2.2.3 | skills/s1-market-analysis | ✅ | Claude | 2026-04-14 |
| 2.2.4 | skills/s2-boundary | ✅ | Claude | 2026-04-14 |
| 2.2.5 | skills/s2-explicit | ✅ | Claude | 2026-04-14 |
| 2.2.6 | skills/s2-implicit | ✅ | Claude | 2026-04-14 |
| 2.2.7 | skills/s2-validation | ✅ | Claude | 2026-04-14 |
| 2.2.8 | skills/s3-feasibility | ✅ | Claude | 2026-04-14 |
| 2.2.9 | skills/s3-selection | ✅ | Claude | 2026-04-14 |
| 2.2.10 | skills/s3-nfr | ✅ | Claude | 2026-04-14 |
| 2.2.11 | skills/s3-risk | ✅ | Claude | 2026-04-14 |
| 2.2.12 | skills/s4-classify | ✅ | Claude | 2026-04-14 |
| 2.2.13 | skills/s4-priority | ✅ | Claude | 2026-04-14 |
| 2.2.14 | skills/s4-core | ✅ | Claude | 2026-04-14 |
| 2.2.15 | skills/s4-user-stories | ✅ | Claude | 2026-04-14 |
| 2.2.16 | skills/s4-prototype | ✅ | Claude | 2026-04-14 |
| 2.2.17 | skills/s5-vision | ✅ | Claude | 2026-04-14 |
| 2.2.18 | skills/s5-views | ✅ | Claude | 2026-04-14 |
| 2.2.19 | skills/s5-data | ✅ | Claude | 2026-04-14 |
| 2.2.20 | skills/s5-interface | ✅ | Claude | 2026-04-14 |
| 2.2.21 | skills/s5-deployment | ✅ | Claude | 2026-04-14 |
| 2.2.22 | skills/s5-validation | ✅ | Claude | 2026-04-14 |
| 2.2.23 | skills/s6-module | ✅ | Claude | 2026-04-14 |
| 2.2.24 | skills/s6-database | ✅ | Claude | 2026-04-14 |
| 2.2.25 | skills/s6-uiux | ✅ | Claude | 2026-04-14 |
| 2.2.26 | skills/s6-test-strategy | ✅ | Claude | 2026-04-14 |
| 2.2.27 | skills/cm-impact-analysis | ✅ | Claude | 2026-04-14 |

**验收标准**: 所有 SKILL.md 包含 Contract 区块，字段完整

---

### 2.3 修改 coordinator 文档引用 manifest

| 序号 | 文件 | 修改内容 | 状态 | 执行人 | 完成时间 |
|------|------|----------|------|--------|----------|
| 2.3.1 | agents/coordinator-requirements.md | 引用 workflow-manifest.yaml，更新 Skill 数量描述 | ✅ | Claude | 2026-04-14 |
| 2.3.2 | agents/coordinator-architecture.md | 引用 workflow-manifest.yaml | ✅ | Claude | 2026-04-14 |
| 2.3.3 | agents/coordinator-detailed-design.md | 引用 workflow-manifest.yaml | ✅ | Claude | 2026-04-14 |

**验收标准**: coordinator 文档通过引用 manifest 获取 Skill 定义

---

### 2.4 对齐 README.md 和 WORKFLOW.md

| 序号 | 文件 | 修改内容 | 状态 | 执行人 | 完成时间 |
|------|------|----------|------|--------|----------|
| 2.4.1 | README.md | 确保与 manifest 一致 | ⬜ | - | - |
| 2.4.2 | WORKFLOW.md | 确保与 manifest 一致 | ✅ | Claude | 2026-04-14 |

**验收标准**: README.md、WORKFLOW.md 与 manifest 三者一致

**备注**: WORKFLOW.md 已经与 manifest 一致，README.md 待后续更新

---

### 阶段 2 验收检查

| 序号 | 检查项 | 检查方法 | 预期结果 | 状态 | 完成时间 |
|------|--------|----------|----------|------|----------|
| V2.1 | manifest 存在性 | 检查 agents/workflow-manifest.yaml | 文件存在 | ✅ | 2026-04-14 |
| V2.2 | manifest 格式 | YAML 格式校验 | 格式正确 | ✅ | 2026-04-14 |
| V2.3 | Skill 数量 | 统计 manifest 中 skills 列表 | 27 个 | ✅ | 2026-04-14 |
| V2.4 | Contract 区块 | 检查所有 SKILL.md | 全部包含 | ✅ | 2026-04-14 |

---

## 阶段 3：共享规范重构

### 3.1 创建 skills/_shared/ 目录

| 序号 | 修改项 | 说明 | 状态 | 执行人 | 完成时间 |
|------|--------|------|------|--------|----------|
| 3.1.1 | 创建目录 | skills/_shared/ | ⬜ | - | - |
| 3.1.2 | 创建 user-interaction 子目录 | skills/_shared/user-interaction/ | ⬜ | - | - |

**验收标准**: 目录结构创建完成

---

### 3.2 创建共享规范文件

| 序号 | 文件 | 说明 | 状态 | 执行人 | 完成时间 |
|------|------|------|------|--------|----------|
| 3.2.1 | skills/_shared/quality-standard.md | ISO/IEC 25010 质量评估框架 | ⬜ | - | - |
| 3.2.2 | skills/_shared/artifact-specifications.md | 产物 ID 和存储规范 | ⬜ | - | - |
| 3.2.3 | skills/_shared/execution-flow-standard.md | 执行流程标准 | ⬜ | - | - |
| 3.2.4 | skills/_shared/error-code-standard.md | 错误代码标准 | ⬜ | - | - |
| 3.2.5 | skills/_shared/user-interaction/clarification-template.md | 澄清模板 | ⬜ | - | - |
| 3.2.6 | skills/_shared/user-interaction/information-collection-template.md | 信息收集模板 | ⬜ | - | - |
| 3.2.7 | skills/_shared/user-interaction/option-selection-template.md | 选项选择模板 | ⬜ | - | - |

**验收标准**: 共享规范文件创建完成，内容已更新（"14个Skill" → "27个Skill"）

---

### 3.3 更新 SKILL.md 引用路径

| 序号 | Skill 目录 | 状态 | 执行人 | 完成时间 |
|------|------------|------|--------|----------|
| 3.3.1 | skills/s0-plan | ⬜ | - | - |
| 3.3.2 | skills/s1-competitor | ⬜ | - | - |
| 3.3.3 | skills/s1-market-analysis | ⬜ | - | - |
| 3.3.4 | skills/s2-boundary | ⬜ | - | - |
| 3.3.5 | skills/s2-explicit | ⬜ | - | - |
| 3.3.6 | skills/s2-implicit | ⬜ | - | - |
| 3.3.7 | skills/s2-validation | ⬜ | - | - |
| 3.3.8 | skills/s3-feasibility | ⬜ | - | - |
| 3.3.9 | skills/s3-selection | ⬜ | - | - |
| 3.3.10 | skills/s3-nfr | ⬜ | - | - |
| 3.3.11 | skills/s3-risk | ⬜ | - | - |
| 3.3.12 | skills/s4-classify | ⬜ | - | - |
| 3.3.13 | skills/s4-priority | ⬜ | - | - |
| 3.3.14 | skills/s4-core | ⬜ | - | - |
| 3.3.15 | skills/s4-user-stories | ⬜ | - | - |
| 3.3.16 | skills/s4-prototype | ⬜ | - | - |
| 3.3.17 | skills/s5-vision | ⬜ | - | - |
| 3.3.18 | skills/s5-views | ⬜ | - | - |
| 3.3.19 | skills/s5-data | ⬜ | - | - |
| 3.3.20 | skills/s5-interface | ⬜ | - | - |
| 3.3.21 | skills/s5-deployment | ⬜ | - | - |
| 3.3.22 | skills/s5-validation | ⬜ | - | - |
| 3.3.23 | skills/s6-module | ⬜ | - | - |
| 3.3.24 | skills/s6-database | ⬜ | - | - |
| 3.3.25 | skills/s6-uiux | ⬜ | - | - |
| 3.3.26 | skills/s6-test-strategy | ⬜ | - | - |
| 3.3.27 | skills/cm-impact-analysis | ⬜ | - | - |

**验收标准**: 所有 SKILL.md 的共享规范引用指向 `../_shared/`

---

### 3.4 补齐 s3-nfr 和 s4-user-stories 的缺失文件

| 序号 | 修改项 | 说明 | 状态 | 执行人 | 完成时间 |
|------|--------|------|------|--------|----------|
| 3.4.1 | s3-nfr execution-details.md | 创建或引用共享规范 | ⬜ | - | - |
| 3.4.2 | s4-user-stories references/ | 创建目录并补充缺失文件 | ⬜ | - | - |

**验收标准**: SKILL.md 中引用的所有文件均存在

---

### 阶段 3 验收检查

| 序号 | 检查项 | 检查方法 | 预期结果 | 状态 | 完成时间 |
|------|--------|----------|----------|------|----------|
| V3.1 | _shared 目录存在 | 检查 skills/_shared/ | 目录存在 | ⬜ | - |
| V3.2 | 共享规范文件 | 检查文件数量 | 7 个文件 | ⬜ | - |
| V3.3 | "14个Skill" 残留 | 全局搜索 | 仅迁移状态说明中出现 | ⬜ | - |
| V3.4 | 引用路径正确性 | 检查 SKILL.md 引用 | 全部指向 ../_shared/ | ⬜ | - |

---

## 阶段 4：校验与治理

### 4.1 创建校验脚本

| 序号 | 修改项 | 说明 | 状态 | 执行人 | 完成时间 |
|------|--------|------|------|--------|----------|
| 4.1.1 | 创建 scripts 目录 | 如不存在则创建 | ⬜ | - | - |
| 4.1.2 | 创建校验脚本 | scripts/validate_workflow_docs.py | ⬜ | - | - |
| 4.1.3 | 实现目录存在性检查 | check_skill_directories() | ⬜ | - | - |
| 4.1.4 | 实现 references 检查 | check_references_exist() | ⬜ | - | - |
| 4.1.5 | 实现旧编号检查 | check_deprecated_patterns() | ⬜ | - | - |
| 4.1.6 | 实现共享规范检查 | check_shared_references() | ⬜ | - | - |
| 4.1.7 | 测试脚本执行 | python scripts/validate_workflow_docs.py | ⬜ | - | - |

**验收标准**: 脚本可执行，返回 0 错误

---

### 4.2 创建迁移状态说明

| 序号 | 修改项 | 说明 | 状态 | 执行人 | 完成时间 |
|------|--------|------|------|--------|----------|
| 4.2.1 | 创建 docs 目录 | 如不存在则创建 | ⬜ | - | - |
| 4.2.2 | 创建迁移状态文档 | docs/migration-status.md | ⬜ | - | - |

**验收标准**: 文档包含迁移历史、当前体系、已废弃编号

---

### 阶段 4 验收检查

| 序号 | 检查项 | 检查方法 | 预期结果 | 状态 | 完成时间 |
|------|--------|----------|----------|------|----------|
| V4.1 | 脚本存在 | 检查 scripts/validate_workflow_docs.py | 文件存在 | ⬜ | - |
| V4.2 | 脚本执行 | python scripts/validate_workflow_docs.py | 返回 0 错误 | ⬜ | - |
| V4.3 | 迁移文档存在 | 检查 docs/migration-status.md | 文件存在 | ⬜ | - |

---

## 最终验收

| 序号 | 验收项 | 检查方法 | 预期结果 | 状态 | 完成时间 |
|------|--------|----------|----------|------|----------|
| F.1 | 无 S104 残留 | 全局搜索 `\bS104\b` | 仅迁移文档中出现 | ⬜ | - |
| F.2 | 无 S404 残留 | 全局搜索 `\bS404\b` | 仅迁移文档中出现 | ⬜ | - |
| F.3 | manifest 完整 | 检查 agents/workflow-manifest.yaml | 27 个 Skill 定义 | ⬜ | - |
| F.4 | Contract 区块完整 | 检查所有 SKILL.md | 全部包含 | ⬜ | - |
| F.5 | 共享规范集中 | 检查 skills/_shared/ | 7 个规范文件 | ⬜ | - |
| F.6 | 校验脚本通过 | python scripts/validate_workflow_docs.py | 返回 0 错误 | ⬜ | - |

---

## 问题记录

| 序号 | 日期 | 问题描述 | 影响范围 | 解决方案 | 状态 |
|------|------|----------|----------|----------|------|
| 1 | - | - | - | - | - |

---

## 变更日志

| 日期 | 版本 | 变更内容 | 变更人 |
|------|------|----------|--------|
| 2026-04-14 | 1.0 | 创建任务执行状态表 | - |

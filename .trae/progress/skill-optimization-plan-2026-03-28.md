# Skill 结构优化计划

**计划编号**: PLAN-SKILL-OPT-001
**创建时间**: 2026-03-28
**目标版本**: v3.2
**基线标签**: v3.1-before-skill-optimization

---

## 1. 优化目标

将 14 个 Skill 从单一超大文件重构为渐进式披露结构：
- SKILL.md 保持精简（目标 1500-2500 字）
- 详细内容分离到 references/ 目录
- 添加 YAML frontmatter 支持自动触发

---

## 2. 执行阶段

### Phase 1: S0 阶段（1 个 Skill）
**任务 ID**: 5
**状态**: 待执行
**Skills**: s0-plan
**预计时间**: 30 分钟

**具体操作**:
1. 添加 YAML frontmatter
2. 分离 Section 3 详细步骤 → references/execution-details.md
3. 分离附录 → references/appendix.md
4. 更新引用链接

---

### Phase 2: S1 阶段（4 个 Skills）
**任务 ID**: 7
**状态**: 待执行（依赖 Phase 1）
**Skills**: s1-boundary, s1-explicit, s1-implicit, s1-validation
**预计时间**: 2 小时

**具体操作**:
1. 为每个 Skill 添加 YAML frontmatter
2. 分离执行流程详情 → references/execution-details.md
3. 分离 Demo 示例 → references/examples.md
4. 更新所有引用

---

### Phase 3: S2 阶段（2 个 Skills）
**任务 ID**: 4
**状态**: 待执行（依赖 Phase 2）
**Skills**: s2-competitor, s2-market-analysis
**预计时间**: 1 小时

---

### Phase 4: S3 阶段（3 个 Skills）
**任务 ID**: 3
**状态**: 待执行（依赖 Phase 3）
**Skills**: s3-risk, s3-feasibility, s3-selection
**预计时间**: 1.5 小时

---

### Phase 5: S4 阶段（4 个 Skills）
**任务 ID**: 2
**状态**: 待执行（依赖 Phase 4）
**Skills**: s4-classify, s4-priority, s4-core, s4-prototype
**预计时间**: 2 小时

---

### Phase 6: 验证与收尾
**任务 ID**: 6
**状态**: 待执行（依赖 Phase 5）
**预计时间**: 1 小时

**具体操作**:
1. 统计所有 SKILL.md 字数
2. 验证 references/ 链接有效性
3. 更新 CLAUDE.md 和 WORKFLOW.md
4. 创建优化总结报告
5. 提交最终 commit

---

## 3. 目录结构变化

### 优化前
```
skills/
├── s0-plan/
│   └── SKILL.md          # ~700 行
├── s1-boundary/
│   └── SKILL.md          # ~800 行
└── ...
```

### 优化后
```
skills/
├── s0-plan/
│   ├── SKILL.md          # ~300 行
│   └── references/
│       ├── execution-details.md
│       └── appendix.md
├── s1-boundary/
│   ├── SKILL.md          # ~350 行
│   └── references/
│       ├── execution-details.md
│       └── examples.md
└── ...
```

---

## 4. YAML Frontmatter 模板

```yaml
---
name: S101 需求边界界定
description: This skill should be used when the user asks to "define requirement boundaries", "clarify product scope", "identify target users", or "establish project boundaries". It provides 5-dimensional boundary analysis (product, user, scenario, time, resource).
version: 3.2.0
---
```

---

## 5. 中断恢复机制

### 断点保存
每个 Phase 完成后自动创建 commit：
```bash
git add skills/s{phase}/
git commit -m "refactor: 优化 S{phase} 阶段 Skill 结构

- 添加 YAML frontmatter
- 分离详细内容到 references/
- 优化渐进式披露结构

Phase: {phase}/5
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

### 恢复执行
1. 查看当前任务状态：`claude /task-list`
2. 获取未完成任务：`claude /task-get {taskId}`
3. 继续执行当前 Phase

---

## 6. 验收标准

- [ ] 所有 14 个 Skill 都有 YAML frontmatter
- [ ] 所有 SKILL.md 字数 < 3000 字
- [ ] 所有 references/ 链接有效
- [ ] 无内容丢失（对比基线标签）
- [ ] CLAUDE.md 已更新
- [ ] 最终 commit 已提交

---

## 7. 风险与应对

| 风险 | 可能性 | 影响 | 应对策略 |
|------|--------|------|----------|
| 内容分离时丢失信息 | 中 | 高 | 每 Phase 后对比基线验证 |
| 链接更新遗漏 | 中 | 中 | 使用脚本批量验证链接 |
| 任务中断 | 低 | 低 | 每 Phase 后 commit，支持断点续跑 |

---

*计划创建时间: 2026-03-28*
*计划创建人: Claude Opus 4.6*
*关联标签: v3.1-before-skill-optimization*

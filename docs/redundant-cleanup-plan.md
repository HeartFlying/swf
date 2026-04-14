# 清理冗余共享规范文件 - 执行计划

**文档版本**: 1.0
**创建日期**: 2026-04-14
**状态**: 待执行

---

## Context

**问题背景**：
根据全面检查，所有 27 个 SKILL.md 文件的引用路径已正确配置（引用 `../_shared/`），但各 Skill 的 `references/` 目录中仍存在与 `skills/_shared/` 重复的冗余文件。

**影响**：
- 冗余文件总数：189 个
- 冗余空目录数：27 个（`references/user-interaction/`）
- 增加维护成本，容易导致版本不一致

**目标**：
清理所有冗余文件，确保共享规范统一存储在 `skills/_shared/` 目录。

---

## 冗余文件清单

### 需要删除的文件类型

| 文件类型 | 数量 | 位置 |
|----------|------|------|
| quality-standard.md | 27 个 | 各 Skill 的 references/ 目录 |
| artifact-specifications.md | 27 个 | 各 Skill 的 references/ 目录 |
| execution-flow-standard.md | 27 个 | 各 Skill 的 references/ 目录 |
| error-code-standard.md | 27 个 | 各 Skill 的 references/ 目录 |
| user-interaction/*.md | 81 个 | 各 Skill 的 references/user-interaction/ 目录 |
| **总计** | **189 个** | - |

### 需要保留的文件（Skill 特有）

| 文件类型 | 说明 |
|----------|------|
| execution-details.md | Skill 特有执行步骤 |
| examples.md | Skill 特有示例 |
| appendix.md | Skill 特有附录 |
| skill-structure-reference.md | Skill 结构参考（仅 cm-impact-analysis） |

---

## 执行步骤

### 步骤 1：扩展校验脚本

**文件**：`scripts/validate_workflow_docs.py`

**新增函数**：
```python
def check_redundant_files() -> tuple:
    """检查冗余共享规范文件，返回 (errors, warnings)"""
    REDUNDANT_FILES = [
        "quality-standard.md",
        "artifact-specifications.md",
        "execution-flow-standard.md",
        "error-code-standard.md",
    ]
    # 检查每个 Skill 的 references 目录中是否存在这些文件
```

### 步骤 2：执行冗余文件清理

**删除范围**（每个 Skill 目录）：
- `references/quality-standard.md`
- `references/artifact-specifications.md`
- `references/execution-flow-standard.md`
- `references/error-code-standard.md`
- `references/user-interaction/` 目录

**保留范围**：
- `references/execution-details.md`
- `references/examples.md`
- `references/appendix.md`

### 步骤 3：更新引用路径（如有必要）

检查 `references/execution-details.md` 中的引用路径，确保正确指向 `../../_shared/`。

### 步骤 4：验证清理结果

运行更新后的校验脚本：
```bash
python scripts/validate_workflow_docs.py
```

### 步骤 5：更新文档

**文件**：`CLAUDE.md`

更新目录结构说明：
```markdown
skills/s{stage}-{name}/
├── SKILL.md
├── template.md
└── references/
    ├── execution-details.md    # Skill 特有
    ├── examples.md              # Skill 特有
    └── appendix.md              # Skill 特有（可选）

共享规范统一引用 skills/_shared/
```

---

## 关键文件路径

| 文件 | 用途 |
|------|------|
| `scripts/validate_workflow_docs.py` | 校验脚本，需扩展 |
| `skills/_shared/*.md` | 共享规范基准文件（保留） |
| `skills/s*/references/*.md` | 检查并清理冗余文件 |
| `CLAUDE.md` | 项目整体文档结构说明 |

---

## 验证方式

1. **运行校验脚本**：`python scripts/validate_workflow_docs.py`
2. **检查 Skill 目录**：确保 references 目录仅包含特有文件
3. **检查引用完整性**：确保 SKILL.md 引用的文件仍可访问

---

## 安全措施

1. Git 版本控制：可通过 `git checkout` 恢复误删文件
2. 白名单机制：明确保留文件列表，防止误删
3. 分步骤执行：先清理，后验证

---

## 预期结果

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 冗余文件 | 189 个 | 0 个 |
| references 目录大小 | ~7 文件/Skill | ~3 文件/Skill |
| _shared 目录 | 不变 | 不变 |

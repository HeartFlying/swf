# SWF 常用提示词库

## 使用说明

1. 根据当前需要执行的 Skill 选择对应提示词文件
2. 复制提示词内容到 Claude Code 输入框
3. 替换 `{变量}` 为实际值
4. 执行后按提示词要求更新产物和状态

## 提示词列表

| 提示词 | 用途 | 对应Skill | 执行模式 |
|--------|------|-----------|----------|
| [extract-boundary.md](extract-boundary.md) | 需求边界界定 | Skill1 | 必执行 |
| [extract-explicit.md](extract-explicit.md) | 显性需求提取 | Skill2 | 必执行 |
| [analyze-competitor.md](analyze-competitor.md) | 竞品分析 | Skill9 | 常规模式 |
| [core-extraction.md](core-extraction.md) | 核心需求提炼 | Skill8 | 必执行 |

## 快速调用

### 方式1：直接引用
```
执行提示词：extract-boundary，Plan ID: P000001
```

### 方式2：关键词触发
```
/swf skill1 P000001
```

### 方式3：自然语言
```
请执行需求边界界定分析，Plan ID是P000001
```

## 提示词结构说明

每个提示词文件包含：
1. **触发条件** - 何时使用该提示词
2. **提示词** - 完整的Prompt内容
3. **使用示例** - 调用示例
4. **预期输出** - 产物说明
5. **后置操作** - 执行后的下一步

## 添加新提示词

如需添加新提示词：
1. 复制现有提示词文件作为模板
2. 修改对应Skill的内容
3. 更新本README的列表
4. 提交到工作空间

---

*提示词库 v1.0*
*更新时间：2026-03-27*

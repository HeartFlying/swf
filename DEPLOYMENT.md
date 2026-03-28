# SWF 发布与部署指南

## 概述

本文档说明如何将 SWF (Software WorkFlow) 需求分析系统发布给团队成员使用。

---

## 发布方式

### 方式一：Git 仓库共享（推荐）

适用于团队成员使用 Claude Code 访问同一仓库的场景。

#### 1. 推送代码到远程仓库

```bash
# 确保所有更改已提交
git add .
git commit -m "release: 发布 SWF v3.2.0"

# 推送到远程仓库
git push origin main
```

#### 2. 团队成员使用

团队成员克隆仓库后，Claude Code 会自动识别：

```bash
# 克隆仓库
git clone https://github.com/HeartFlying/swf.git

# 进入目录
cd swf

# 启动 Claude Code
claude
```

启动后，Claude Code 会自动加载：
- `agents/swf-coordinator.md` - 主协调器 Agent
- `skills/*` - 23 个 Skill 定义

---

### 方式二：Claude Code Plugin 安装

适用于需要作为独立插件安装的场景。

#### 目录结构要求

```
swf/
├── .claude-plugin/
│   └── plugin.json          # 插件元数据
├── agents/
│   └── swf-coordinator.md   # 主 Agent
├── skills/
│   ├── s0-plan/
│   ├── s1-boundary/
│   ├── s1-explicit/
│   ├── s1-implicit/
│   ├── s1-validation/
│   ├── s2-competitor/
│   ├── s2-market-analysis/
│   ├── s3-risk/
│   ├── s3-feasibility/
│   ├── s3-selection/
│   ├── s4-classify/
│   ├── s4-priority/
│   ├── s4-core/
│   └── s4-prototype/
└── README.md
```

#### 安装步骤

**步骤 1：打包插件**

```bash
# 创建发布包
zip -r swf-plugin-v3.2.0.zip .claude-plugin agents skills README.md
```

**步骤 2：分发给团队成员**

方式 A：通过 GitHub Release
1. 在 GitHub 创建 Release
2. 上传 `swf-plugin-v3.2.0.zip`
3. 团队成员下载解压到项目目录

方式 B：直接复制
```bash
# 复制到目标项目
cp -r swf-plugin/* /path/to/target/project/
```

**步骤 3：验证安装**

```bash
# 在目标项目启动 Claude Code
claude

# 测试触发 Agent
# 输入："帮我分析一个 APP 的需求"
```

---

### 方式三：CLAUDE.md 引用（最简单）

适用于快速试用，不需要完整插件结构。

#### 使用方法

在项目的 `CLAUDE.md` 中添加：

```markdown
## SWF 需求分析系统

当用户需要需求分析时，使用以下 Agent：

@agents/coordinator-requirements.md
```

然后复制 `agents/coordinator-requirements.md` 和 `skills/` 目录到项目即可。

---

## 配置说明

### 必需配置

无需额外配置，系统开箱即用。

### 可选配置

在 `.claude/settings.json` 中添加：

```json
{
  "env": {
    "SWF_DEFAULT_MODE": "normal",
    "SWF_ARTIFACTS_DIR": "./artifacts"
  }
}
```

---

## 使用指南

### 快速开始

**启动需求分析：**

```
用户：我想开发一个面向大学生的时间管理 APP

Claude：我将启动 SWF 需求分析流程来帮助您系统化梳理需求...
[自动触发 swf-coordinator Agent]
```

### 完整流程示例

```
用户：帮我做一个完整的需求分析

Claude：
1. [S001] 制定 Plan → 生成 Plan ID: P000001
2. [S101] 需求边界界定 → 定义产品/用户/场景/时间/资源边界
3. [S102] 显式需求提取 → 收集功能和非功能需求
4. [S103] 隐式需求挖掘 → 识别业务规则和约束
5. [S104] 需求验证 → 一致性检查
6. [S201] 竞品分析 → 对比分析竞品功能
7. [S202] 市场验证 → 验证市场痛点
8. [S301] 风险识别 → 技术/业务风险评估
9. [S302] 技术可行性 → 评估技术方案
10. [S303] 技术选型 → 推荐技术栈
11. [S401] 需求分类 → 功能/非功能分类
12. [S402] 优先级排序 → MoSCoW 排序
13. [S403] 核心需求提取 → 确定 MVP 功能
14. [S404] 原型设计 → 设计原型草图
15. [S501] 架构风格选择 → 选择合适的架构风格
16. [S502] 系统架构设计 → 设计系统整体架构
17. [S503] 模块划分 → 划分系统模块
18. [S504] 接口设计 → 设计模块间接口
19. [S505] 架构评审 → 评审架构设计
20. [S601] 数据库设计 → 设计数据模型
21. [S602] API设计 → 设计系统API
22. [S603] 安全设计 → 设计安全机制
23. [S604] 详细设计评审 → 评审详细设计

最终输出：完整需求分析报告
```

### 轻量化模式

当需求信息完整度 ≥ 90 分时，自动跳过 S103、S201、S202，执行 20 个 Skill。

---

## 产物输出

所有产物保存在 `artifacts/` 目录：

```
artifacts/
├── plans/
│   ├── P000001.md                 # Plan 定义
│   └── P000001/
│       └── todo-list.md           # 任务跟踪
└── stages/
    ├── s0/
    │   └── P000001-S0-S001-002.md # 评分报告
    ├── s1/
    │   ├── P000001-S1-S101-001.md # 边界界定
    │   ├── P000001-S1-S102-001.md # 显式需求
    │   ├── P000001-S1-S103-001.md # 隐式需求
    │   └── P000001-S1-S104-001.md # 需求验证
    ├── s2/
    │   ├── P000001-S2-S201-001.md # 竞品分析
    │   └── P000001-S2-S202-001.md # 市场验证
    ├── s3/
    │   ├── P000001-S3-S301-001.md # 风险识别
    │   ├── P000001-S3-S302-001.md # 技术可行性
    │   └── P000001-S3-S303-001.md # 技术选型
    └── s4/
        ├── P000001-S4-S401-001.md # 需求分类
        ├── P000001-S4-S402-001.md # 优先级排序
        ├── P000001-S4-S403-001.md # 核心需求
        └── P000001-S4-S404-001.md # 原型设计
```

---

## 团队协作

### Git 工作流

```bash
# 1. 团队成员克隆仓库
git clone https://github.com/HeartFlying/swf.git

# 2. 创建自己的分支进行需求分析
git checkout -b feature/P000001-requirements

# 3. 执行 SWF 流程，产物自动提交
claude
# -> 执行需求分析流程
# -> 产物保存到 artifacts/

# 4. 提交产物
git add artifacts/
git commit -m "docs: 添加 P000001 需求分析产物"

# 5. 推送到远程
git push origin feature/P000001-requirements

# 6. 创建 PR 进行评审
```

### 产物共享

产物是 Markdown 格式，可以直接：
- 在 GitHub 上查看和评审
- 导出为 PDF/Word 分享给非技术人员
- 导入到项目管理工具（Jira、飞书等）

---

## 故障排除

### 问题 1：Agent 未触发

**现象：** 输入需求分析相关语句，Agent 未启动

**解决：**
1. 检查文件路径是否正确：`agents/coordinator-requirements.md`
2. 确认 YAML frontmatter 格式正确
3. 尝试直接引用：`@agents/coordinator-requirements.md 帮我分析需求`

### 问题 2：Skill 加载失败

**现象：** Agent 启动但无法加载 Skill

**解决：**
1. 检查 `skills/` 目录是否存在
2. 确认 Skill 目录命名正确：`s0-plan`, `s1-boundary` 等
3. 检查 SKILL.md 文件是否存在

### 问题 3：产物未生成

**现象：** 执行后没有产物文件

**解决：**
1. 检查 `artifacts/` 目录权限
2. 确认目录结构：`artifacts/plans/` 和 `artifacts/stages/`
3. 查看执行日志中的错误信息

---

## 版本历史

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| v3.2.0 | 2026-03-28 | 初始发布，23 个 Skill，渐进式加载 |

---

## 支持与反馈

- **GitHub Issues**: https://github.com/HeartFlying/swf/issues
- **文档**: 参见 `CLAUDE.md` 和 `WORKFLOW.md`

---

**SWF v3.2.0 - AI 驱动的需求分析系统**

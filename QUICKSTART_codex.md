# SWF 快速开始指南

5 分钟内在 Codex 中跑通一次 SWF 需求分析流程。

---

## 1. 准备仓库

```bash
git clone https://github.com/HeartFlying/swf.git
cd swf
```

打开仓库后，先让 Codex 读取 `AGENTS.md`。

---

## 2. 启动流程

在 Codex 中输入：

```text
请先读取 AGENTS.md，然后按 SWF 工作流帮我分析这个需求：我想开发一个时间管理 APP。
```

Codex 会按以下顺序执行：
1. 读取 `AGENTS.md`
2. 加载 `agents/coordinator-requirements.md`
3. 执行 S001 并生成 Plan / 评分 / Todo-List
4. 按 S0→S4 顺序推进
5. S4 结束后继续执行 S5
6. S5 结束后继续执行 S6

---

## 3. 评审交互

Codex 不依赖 Claude 的自动 Agent 触发，而是通过普通对话完成评审。每个 Skill 完成后，直接回复：

- `确认`
- `修改：xxx`
- `重做`
- `新增：xxx`

---

## 4. 查看产物

```bash
Get-ChildItem artifacts
Get-Content artifacts/plans/P000001.md
Get-Content artifacts/stages/s4/P000001-S4-S403-001.md
Get-Content artifacts/stages/s5/P000001/P000001-S5-A01-001.md
Get-Content artifacts/stages/s6/P000001/P000001-S6-A01-001.md
Get-Content artifacts/plans/P000001/swf-deliverable.md
```

---

## 5. 常用提示词

| 目标 | 推荐输入 |
|------|---------|
| 启动需求分析 | `请按 AGENTS.md 执行 SWF 需求分析流程，帮我分析这个需求：...` |
| 只做架构设计 | `请读取 AGENTS.md 和 agents/coordinator-architecture.md，基于现有产物继续做 S5。` |
| 只做详细设计 | `请读取 AGENTS.md 和 agents/coordinator-detailed-design.md，基于现有产物继续做 S6。` |
| 发起变更分析 | `请读取 skills/cm-impact-analysis/SKILL.md，分析这次需求变更的影响：...` |

---

## 6. 三阶段流程

| 阶段 | 协调器文件 | Skill 数量 | 产出 |
|------|-----------|-----------|------|
| S0-S4 | `agents/coordinator-requirements.md` | 14 个 | 需求规格说明书 |
| S5 | `agents/coordinator-architecture.md` | 6 个 | 架构设计文档 |
| S6 | `agents/coordinator-detailed-design.md` | 4 个 | 详细设计文档 |

在 Codex 中，“阶段衔接”表示继续读取下一个协调器文件，而不是依赖平台自动切换 Agent。

---

## 7. Roadmap 导航

```bash
Get-Content artifacts/roadmap/index.yaml
Get-Content artifacts/roadmap/plans/P000001/roadmap.yaml
Get-Content artifacts/roadmap/stages/s4-summary.yaml
```

---

## 下一步

- 项目概览：`README.md`
- Codex 指引：`AGENTS.md`
- 完整流程：`WORKFLOW.md`
- 安装说明：`INSTALL.md`

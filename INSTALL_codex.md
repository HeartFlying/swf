# SWF 安装指南

## 系统要求

- **Codex** 或支持 Codex 的 AI IDE
- **Git** 用于版本控制
- 可读写当前仓库目录

---

## 安装方式

### 方式一：Git 克隆（推荐）

适用于在 Codex 中直接使用，保持与主仓库同步。

```bash
# 1. 克隆仓库
git clone https://github.com/HeartFlying/swf.git

# 2. 进入目录
cd swf

# 3. 验证文件结构
ls -la
# 应看到：agents/  skills/  README.md  AGENTS.md  CLAUDE.md
```

**验证安装：**

在 Codex 中输入：
```
请先读取 AGENTS.md，然后按 SWF 工作流帮我分析这个需求：我想开发一个时间管理 APP。
```

应看到 Codex 开始读取 `AGENTS.md` 和 `agents/coordinator-requirements.md`，然后启动需求分析流程。

---

### 方式二：下载 ZIP 包

适用于快速试用或不使用 Git 的场景。

```bash
# 1. 下载发布包
wget https://github.com/HeartFlying/swf/releases/download/v3.2.0/swf-v3.2.0.zip

# 2. 解压
unzip swf-v3.2.0.zip -d swf

# 3. 进入目录
cd swf

# 4. 在 Codex 中打开该目录
```

---

### 方式三：复制到现有项目

适用于在已有项目中把 SWF 作为 Codex 工作流模板使用。

```bash
# 1. 进入你的项目目录
cd your-project

# 2. 复制 SWF 文件
cp -r /path/to/swf/agents .
cp -r /path/to/swf/skills .

# 3. 在 AGENTS.md 中添加引用
echo "
## SWF 需求分析

当用户需要需求分析时，读取 agents/coordinator-requirements.md。
当用户需要架构设计时，读取 agents/coordinator-architecture.md。
当用户需要详细设计时，读取 agents/coordinator-detailed-design.md。
" >> AGENTS.md
```

---

## 目录结构验证

安装后应包含以下文件：

```
swf/
├── agents/                         # Agent 定义
│   ├── coordinator-requirements.md # 需求分析协调器 (S0-S4)
│   ├── coordinator-architecture.md # 架构设计协调器 (S5)
│   └── coordinator-detailed-design.md # 详细设计协调器 (S6)
├── skills/                         # 27 个 Skill 定义
│   ├── s0-plan/                    # S001: Plan 制定
│   ├── s1-competitor/              # S101: 竞品分析
│   ├── s1-market-analysis/         # S102: 市场验证
│   ├── s2-boundary/                # S201: 需求边界
│   ├── s2-explicit/                # S202: 显式需求
│   ├── s2-implicit/                # S203: 隐式需求
│   ├── s2-validation/              # S204: 需求验证
│   ├── s3-feasibility/             # S301: 技术可行性
│   ├── s3-selection/               # S302: 技术选型
│   ├── s3-nfr/                     # S303: 非功能需求
│   ├── s3-risk/                    # S304: 风险识别
│   ├── s4-classify/                # S401: 需求分类
│   ├── s4-priority/                # S402: 优先级排序
│   ├── s4-core/                    # S403: 核心需求提取
│   ├── s4-user-stories/            # S405: 用户故事
│   ├── s4-prototype/               # S406: 原型设计
│   ├── s5-vision/                  # S5-A01: 架构愿景
│   ├── s5-views/                   # S5-A02: 架构视图
│   ├── s5-data/                    # S5-A03: 数据架构
│   ├── s5-interface/               # S5-A04: 接口架构
│   ├── s5-deployment/              # S5-A05: 部署架构
│   ├── s5-validation/              # S5-A06: 架构验证
│   ├── s6-module/                  # S6-A01: 模块详细设计
│   ├── s6-database/                # S6-A02: 数据库详细设计
│   ├── s6-uiux/                    # S6-A03: UI/UX设计
│   ├── s6-test-strategy/           # S6-A04: 测试策略设计
│   └── cm-impact-analysis/         # CM-001: 变更影响分析
├── artifacts/                      # 产物输出目录（自动生成）
├── WORKFLOW.md                     # 主工作流程文档
├── AGENTS.md                       # Codex 项目指引
├── CLAUDE.md                       # Claude Code 项目指引
├── README.md                       # 项目说明
└── INSTALL.md                      # 本文件
```

---

## 首次使用

### 步骤 1：创建 artifacts 目录

```bash
mkdir -p artifacts/plans artifacts/roadmap/stages artifacts/roadmap/plans
mkdir -p artifacts/stages/s{0,1,2,3,4,5,6}
mkdir -p artifacts/change-management
```

### 步骤 2：测试 Codex 执行

在 Codex 中输入以下任一语句测试：

```
- "请读取 AGENTS.md，帮我分析需求"
- "请按 SWF 工作流做一个需求规划"
- "请按 AGENTS.md 执行需求评审"
```

### 步骤 3：执行完整流程

```
用户：我想开发一个面向大学生的时间管理 APP，
      核心功能包括任务管理、番茄钟、学习统计。
      目标用户是 18-25 岁大学生，预算 10 万，3 个月完成。

Codex：
[读取 AGENTS.md 和 coordinator-requirements]
1. [S001] Plan 制定 → P000001
2. 信息完整度评分 → 65 分（常规模式）
3. [S101-S102] 市场洞察阶段
4. [S201-S204] 需求定义阶段
5. [S301-S304] 技术规划阶段
6. [S401-S406] 需求整合阶段

[阶段交接：继续读取 coordinator-architecture]
7. [S5-A01-S5-A06] 架构设计阶段

[阶段交接：继续读取 coordinator-detailed-design]
8. [S6-A01-S6-A04] 详细设计阶段

输出 SWF 完整交付物
```

---

## 三阶段协调器

SWF 使用三个协调器文件串行编排：

| 协调器 | 阶段 | Skill 数量 | 在 Codex 中的启动方式 |
|--------|------|-----------|----------------------|
| coordinator-requirements | S0-S4 | 14 个 | 读取 `agents/coordinator-requirements.md` |
| coordinator-architecture | S5 | 6 个 | 读取 `agents/coordinator-architecture.md` |
| coordinator-detailed-design | S6 | 4 个 | 读取 `agents/coordinator-detailed-design.md` |

**手动触发方式**：
```
"请读取 agents/coordinator-architecture.md 并继续 S5"
"请读取 agents/coordinator-detailed-design.md 并继续 S6"
```

---

## 更新升级

### 从 Git 更新

```bash
# 进入仓库目录
cd swf

# 拉取最新代码
git pull origin main

# 重新打开 Codex 会话或刷新 IDE 会话
```

### 备份产物

更新前备份已有产物：

```bash
# 备份 artifacts 目录
cp -r artifacts artifacts-backup-$(date +%Y%m%d)
```

---

## 卸载

如需卸载，直接删除相关文件：

```bash
# 删除 SWF 文件
rm -rf agents/
rm -rf skills/

# 保留产物（可选）
# mv artifacts ~/swf-backup/
```

---

## 常见问题

**Q: Codex 没有自动进入 SWF 流程？**
A: 这是预期行为。Codex 适配版不依赖自动 Agent 识别，请显式要求读取 `AGENTS.md` 或某个协调器文件。

**Q: Skill 执行报错？**
A: 检查 `skills/` 目录结构是否完整，所有 27 个 Skill 是否存在。

**Q: 产物保存在哪里？**
A: 默认保存在 `artifacts/` 目录，包括 `plans/`、`stages/`、`roadmap/` 等子目录。

**Q: 为什么保留 `CLAUDE.md`？**
A: 仓库同时兼容 Claude Code 和 Codex。`CLAUDE.md` 供 Claude 使用，`AGENTS.md` 供 Codex 使用。

**Q: 如何只做需求分析不做架构设计？**
A: S4 完成后输入"暂停"或"结束"，不会自动触发 S5 阶段。

**Q: 如何跳过某个 Skill？**
A: 在评审时输入"跳过"即可跳过当前 Skill（部分 Skill 不可跳过）。

---

**安装完成！** 开始使用 SWF 进行需求分析吧。

# SWF 安装指南

## 系统要求

- **Claude Code** 已安装（版本 ≥ 1.0.0）
- **Git** 用于版本控制
- **Node.js** 18+（如果使用 Claude Code CLI）

---

## 安装方式

### 方式一：Git 克隆（推荐）

适用于团队协作，保持与主仓库同步。

```bash
# 1. 克隆仓库
git clone https://github.com/HeartFlying/swf.git

# 2. 进入目录
cd swf

# 3. 验证文件结构
ls -la
# 应看到：agents/  skills/  templates/  README.md  CLAUDE.md

# 4. 启动 Claude Code
claude
```

**验证安装：**

在 Claude Code 中输入：
```
我想开发一个时间管理 APP，帮我分析需求
```

应看到 `coordinator-requirements` Agent 被触发并启动需求分析流程。

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

# 4. 启动 Claude Code
claude
```

---

### 方式三：复制到现有项目

适用于在已有项目中使用 SWF。

```bash
# 1. 进入你的项目目录
cd your-project

# 2. 复制 SWF 文件
cp -r /path/to/swf/agents .
cp -r /path/to/swf/skills .
cp -r /path/to/swf/templates .

# 3. 在 CLAUDE.md 中添加引用
echo "
## SWF 需求分析

使用 @agents/coordinator-requirements.md 进行需求分析。
使用 @agents/coordinator-architecture.md 进行架构设计。
使用 @agents/coordinator-detailed-design.md 进行详细设计。
" >> CLAUDE.md

# 4. 启动 Claude Code
claude
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
├── templates/                      # 输出模板
│   ├── user-interaction/           # 用户交互模板
│   ├── quality-standard.md         # ISO/IEC 25010 质量标准
│   ├── error-code-standard.md      # 统一错误码标准
│   └── skill-structure-reference.md # Skill 结构参考
├── artifacts/                      # 产物输出目录（自动生成）
├── WORKFLOW.md                     # 主工作流程文档
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

### 步骤 2：测试 Agent 触发

在 Claude Code 中输入以下任一语句测试：

```
- "我想开发一个 APP"
- "帮我分析需求"
- "做一个需求规划"
- "需要需求评审"
```

### 步骤 3：执行完整流程

```
用户：我想开发一个面向大学生的时间管理 APP，
      核心功能包括任务管理、番茄钟、学习统计。
      目标用户是 18-25 岁大学生，预算 10 万，3 个月完成。

Claude：
[触发 coordinator-requirements]
1. [S001] Plan 制定 → P000001
2. 信息完整度评分 → 65 分（常规模式）
3. [S101-S102] 市场洞察阶段
4. [S201-S204] 需求定义阶段
5. [S301-S304] 技术规划阶段
6. [S401-S406] 需求整合阶段

[阶段交接：触发 coordinator-architecture]
7. [S5-A01-S5-A06] 架构设计阶段

[阶段交接：触发 coordinator-detailed-design]
8. [S6-A01-S6-A04] 详细设计阶段

输出 SWF 完整交付物
```

---

## 三阶段协调器

SWF 使用三个协调器 Agent 串行执行：

| 协调器 | 阶段 | Skill 数量 | 触发方式 |
|--------|------|-----------|---------|
| coordinator-requirements | S0-S4 | 14 个 | 用户输入需求 |
| coordinator-architecture | S5 | 6 个 | S4 完成后自动触发 |
| coordinator-detailed-design | S6 | 4 个 | S5 完成后自动触发 |

**手动触发方式**：
```
"开始架构设计"     → 触发 coordinator-architecture
"开始详细设计"     → 触发 coordinator-detailed-design
```

---

## 更新升级

### 从 Git 更新

```bash
# 进入仓库目录
cd swf

# 拉取最新代码
git pull origin main

# 重启 Claude Code
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
rm -rf templates/

# 保留产物（可选）
# mv artifacts ~/swf-backup/
```

---

## 常见问题

**Q: Claude Code 无法识别 Agent？**
A: 检查 `agents/coordinator-requirements.md` 是否存在，且 YAML frontmatter 格式正确。

**Q: Skill 执行报错？**
A: 检查 `skills/` 目录结构是否完整，所有 27 个 Skill 是否存在。

**Q: 产物保存在哪里？**
A: 默认保存在 `artifacts/` 目录，包括 `plans/`、`stages/`、`roadmap/` 等子目录。

**Q: 支持哪些 Claude Code 版本？**
A: 需要 Claude Code ≥ 1.0.0，支持 Agent/Skill 功能。

**Q: 如何只做需求分析不做架构设计？**
A: S4 完成后输入"暂停"或"结束"，不会自动触发 S5 阶段。

**Q: 如何跳过某个 Skill？**
A: 在评审时输入"跳过"即可跳过当前 Skill（部分 Skill 不可跳过）。

---

**安装完成！** 开始使用 SWF 进行需求分析吧。

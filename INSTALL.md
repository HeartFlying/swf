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
# 应看到：agents/  skills/  .claude-plugin/  README.md

# 4. 启动 Claude Code
claude
```

**验证安装：**

在 Claude Code 中输入：
```
我想开发一个时间管理 APP，帮我分析需求
```

应看到 Agent 被触发并启动需求分析流程。

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
cp -r /path/to/swf/.claude-plugin .

# 3. 在 CLAUDE.md 中添加引用
echo "
## SWF 需求分析

使用 @agents/coordinator-requirements.md 进行需求分析。
" >> CLAUDE.md

# 4. 启动 Claude Code
claude
```

---

## 目录结构验证

安装后应包含以下文件：

```
swf/
├── .claude-plugin/
│   └── plugin.json              # 插件配置
├── agents/
│   ├── coordinator.md           # 内部协调器
│   └── coordinator-requirements.md  # 主 Agent（入口）
├── skills/
│   ├── s0-plan/SKILL.md         # S001 Plan 制定
│   ├── s1-boundary/SKILL.md     # S101 需求边界
│   ├── s1-explicit/SKILL.md     # S102 显式需求
│   ├── s1-implicit/SKILL.md     # S103 隐式需求
│   ├── s1-validation/SKILL.md   # S104 需求验证
│   ├── s2-competitor/SKILL.md   # S201 竞品分析
│   ├── s2-market-analysis/      # S202 市场验证
│   ├── s3-risk/SKILL.md         # S301 风险识别
│   ├── s3-feasibility/          # S302 技术可行性
│   ├── s3-selection/            # S303 技术选型
│   ├── s4-classify/SKILL.md     # S401 需求分类
│   ├── s4-priority/             # S402 优先级排序
│   ├── s4-core/                 # S403 核心需求
│   └── s4-prototype/            # S404 原型设计
├── artifacts/                   # 产物输出目录（自动生成）
├── README.md                    # 项目说明
├── DEPLOYMENT.md                # 部署指南
└── INSTALL.md                   # 本文件
```

---

## 首次使用

### 步骤 1：创建 artifacts 目录

```bash
mkdir -p artifacts/plans artifacts/stages/s{0,1,2,3,4}
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
1. 制定 Plan → P000001
2. 信息完整度评分 → 85 分（常规模式）
3. 执行 S101 需求边界界定...
4. ...（逐步执行 23 个 Skill）
5. 输出最终需求分析报告
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
rm -rf agents/coordinator-requirements.md
rm -rf skills/
rm -rf .claude-plugin/

# 保留产物（可选）
# mv artifacts ~/swf-backup/
```

---

## 常见问题

**Q: Claude Code 无法识别 Agent？**
A: 检查 `agents/coordinator-requirements.md` 是否存在，且 YAML frontmatter 格式正确。

**Q: Skill 执行报错？**
A: 检查 `skills/` 目录结构是否完整，所有 23 个 Skill 是否存在。

**Q: 产物保存在哪里？**
A: 默认保存在 `artifacts/` 目录，可在 `CLAUDE.md` 中修改路径。

**Q: 支持哪些 Claude Code 版本？**
A: 需要 Claude Code ≥ 1.0.0，支持 Agent/Skill 功能。

---

**安装完成！** 开始使用 SWF 进行需求分析吧。

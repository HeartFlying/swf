# Agents 与 Skills 引用关系评审清单

## 文档信息

| 项目 | 内容 |
|------|------|
| 文档名称 | Agents 与 Skills 引用关系评审清单 |
| 评审范围 | `agents/`、`skills/`、`README.md`、`WORKFLOW.md` |
| 评审目标 | 识别 coordinator 与 skill 之间的引用失配、结构重复、依赖脆弱点，并提出优化与修复计划 |
| 评审日期 | 2026-04-13 |

---

## 一、评审结论摘要

当前项目的 `agents` 与 `skills` 总体分层方向是合理的：

- `agents/` 负责阶段编排
- `skills/` 负责单个工作项定义
- `references/` 负责补充执行细节

但实际落地中已经出现明显的版本漂移，主要表现为：

1. `WORKFLOW.md`、`agents/*.md`、`skills/*/SKILL.md` 对阶段编号和 skill 顺序的定义不一致
2. 多个 `SKILL.md` 引用了不存在的 `references/*` 文件，导致文档执行闭环断裂
3. 大量共享规范文件被复制到各个 skill 目录中，复制内容仍停留在旧的 14-skill 模型
4. 阶段交接依赖仍混用旧编号 `S104`、`S404` 与新编号 `S204`、`S406`
5. `agents` 与 `skills` 之间缺少单一事实源，导致每次重构都需要多处同步修改，极易继续漂移

结论：

- 当前最需要优化的不是个别措辞，而是“引用关系的真相源”和“共享规范的组织方式”
- 如果只修某几个文件，问题会暂时缓解，但后续仍会复发
- 建议先建立统一 manifest，再清理 coordinator、skill、reference 的引用链

---

## 二、详细问题清单

以下问题按优先级划分为 P0、P1、P2：

- `P0`：直接影响执行正确性，按当前文档可能找错 skill、找错产物、走错流程
- `P1`：不会立即阻断执行，但会显著提高维护成本，并导致后续继续漂移
- `P2`：表达、组织、可读性问题，建议在主问题收敛后处理

### P0-01 `coordinator-requirements` 的阶段定义与当前实际 skill 体系冲突

**问题描述**

`agents/coordinator-requirements.md` 中同时存在两套 S3/S4 定义：

- 一套仍使用旧编号 `S404`
- 一套后文又使用当前真实编号 `S405`、`S406`
- S3 中 `S301/S302/S303` 的职责映射也被写反

**定位**

- `agents/coordinator-requirements.md:64`
- `agents/coordinator-requirements.md:76`
- `agents/coordinator-requirements.md:230`
- `agents/coordinator-requirements.md:236`
- `agents/coordinator-requirements.md:242`
- `agents/coordinator-requirements.md:268`
- `agents/coordinator-requirements.md:275`

**现象**

- 轻量化跳过写成 `S404`
- S4 阶段表写成 `S401, S402, S403, S404, S405`
- 后文实际执行说明又写成 `S405 用户故事编写`、`S406 原型设计`
- S3 中写成：
  - `S301 - 风险识别`
  - `S302 - 技术可行性`
  - `S303 - 技术选型`
  与 `WORKFLOW.md` 当前定义不一致

**影响**

- coordinator 作为编排入口，若按该文件执行，可能直接加载错误 skill
- 轻量化模式的跳过逻辑不可信
- S3/S4 的下游阶段交接将建立在错误的前提之上

**建议优先级**

- 必须第一批修复

---

### P0-02 `S0 Plan` 的后置 skill 仍指向旧阶段关系

**问题描述**

`skills/s0-plan/SKILL.md` 中，S001 的后置 skill 仍写成 `S101 (需求边界界定)`，与当前流程不一致。

**定位**

- `skills/s0-plan/SKILL.md:20`
- `skills/s0-plan/SKILL.md:155`
- `skills/s0-plan/SKILL.md:156`

**现象**

- 当前 `WORKFLOW.md` 中：
  - `S101` 是竞品分析
  - `S201` 才是需求边界界定
- 但 S001 仍把 `S101` 当作“需求边界界定”

**影响**

- 流程入口 skill 的“后置关系”错误，直接污染全链路理解
- 新维护者会误认为当前仍是旧的 14-skill 拆法

**建议优先级**

- 必须第一批修复

---

### P0-03 `s4-user-stories` 仍指向不存在的 `S404`

**问题描述**

`skills/s4-user-stories/SKILL.md` 中后置 skill 仍写为 `S404 (原型设计)`，但当前项目中真实 skill 是 `S406`。

**定位**

- `skills/s4-user-stories/SKILL.md:20`
- `skills/s4-user-stories/SKILL.md:140`

**影响**

- S4 末尾的链路定义错误
- S4 到 S5 的交接说明被污染

**建议优先级**

- 必须第一批修复

---

### P0-04 `s2-validation` 文案仍大量使用旧编号 `S104`

**问题描述**

`skills/s2-validation/SKILL.md` 已经处于 S2 阶段，但执行流程和说明文字仍反复写成 `S104`。

**定位**

- `skills/s2-validation/SKILL.md:151`
- `skills/s2-validation/SKILL.md:160`
- `skills/s2-validation/SKILL.md:183`

**影响**

- Skill 自身编号与执行文本不一致
- 评审与返工路径存在误导
- 会让后续 skill 按旧产物编号寻找输入

**建议优先级**

- 必须第一批修复

---

### P0-05 `s5-vision` 的输入契约仍绑定旧 S1 产物编号

**问题描述**

`skills/s5-vision/SKILL.md` 仍将 S5 输入定义为 `S1-S101`、`S1-S102`、`S1-S104` 等旧编号体系。

**定位**

- `skills/s5-vision/SKILL.md:55`
- `skills/s5-vision/SKILL.md:56`
- `skills/s5-vision/SKILL.md:57`
- `skills/s5-vision/SKILL.md:80`
- `skills/s5-vision/SKILL.md:81`
- `skills/s5-vision/SKILL.md:82`

**影响**

- S4 到 S5 的阶段交接契约不稳定
- 架构设计阶段会按旧路径理解需求输入
- 即使修复了 requirement coordinator，S5 仍然可能读取错误前置产物

**建议优先级**

- 必须第一批修复

---

### P0-06 `s3-nfr` 与 `s4-user-stories` 引用了不存在的 references 文件

**问题描述**

两个 skill 的 `SKILL.md` 明确引用了若干 `references/*` 文件，但目录中实际不存在这些文件。

**定位**

- `skills/s3-nfr/SKILL.md:117`
- `skills/s3-nfr/SKILL.md:123`
- `skills/s3-nfr/SKILL.md:227`
- `skills/s3-nfr/SKILL.md:249`
- `skills/s4-user-stories/SKILL.md:120`
- `skills/s4-user-stories/SKILL.md:126`
- `skills/s4-user-stories/SKILL.md:231`
- `skills/s4-user-stories/SKILL.md:286`

**实际目录状态**

- `skills/s3-nfr/references/` 仅存在 `quality-standard.md`
- `skills/s4-user-stories/references/` 仅存在 `user-interaction/`

**影响**

- 这两个 skill 文档本身不可完整执行
- 维护者无法从 skill 内部追到所需规范
- 这是文档闭环断裂，不是一般风格问题

**建议优先级**

- 必须第一批修复

---

### P0-07 `cm-impact-analysis` 的最小重执行路径仍使用旧编号

**问题描述**

`skills/cm-impact-analysis/SKILL.md` 的重执行链路仍使用 `S404`，且 S6 只列到 `S6-A03`。

**定位**

- `skills/cm-impact-analysis/SKILL.md:157`
- `skills/cm-impact-analysis/SKILL.md:159`
- `skills/cm-impact-analysis/SKILL.md:161`

**影响**

- 变更管理流程无法正确覆盖当前真实 skill 集合
- 一旦执行增量更新，会直接给出不完整或错误的重执行计划

**建议优先级**

- 必须第一批修复

---

### P1-01 共享 references 被整包复制，内容普遍停留在旧 14-skill 模型

**问题描述**

大量 `references/artifact-specifications.md`、`references/error-code-standard.md`、`references/quality-standard.md`、`references/execution-flow-standard.md` 仍反复声明：

- `所有14个Skill`
- `S101-S104`
- `S201-S202`
- `S301-S303`
- `S401-S404`

而当前真实体系已经是：

- 需求分析 16 个工作流 skill（S0-S4）
- 架构 6 个 skill（S5）
- 详细设计 4 个 skill（S6）
- 另有变更管理 1 个 skill

**定位示例**

- `skills/s0-plan/references/artifact-specifications.md`
- `skills/s1-market-analysis/references/error-code-standard.md`
- `skills/s2-explicit/references/quality-standard.md`
- `skills/s5-validation/references/quality-standard.md`
- `skills/s6-module/references/execution-flow-standard.md`

**影响**

- 项目中“共享规范”已经失去可信度
- 每次修正需要同步几十份重复文件，成本极高
- 新问题会继续在复制链中扩散

**建议优先级**

- 第二批修复，但应尽快设计统一方案

---

### P1-02 `WORKFLOW.md`、`README.md`、`agents/*.md` 缺少统一的单一事实源

**问题描述**

当前 skill 列表、阶段顺序、轻量化跳过逻辑、产物路径、交接关系，在多个地方重复定义：

- `README.md`
- `WORKFLOW.md`
- `agents/*.md`
- 各 `skills/*/SKILL.md`

这些定义没有一个机器可读的统一清单作为源头。

**影响**

- 任何一次重构都要手动同步多处文档
- 文档漂移是结构性必然，不是偶发疏漏
- coordinator 与 skill 之间无法进行一致性校验

**建议优先级**

- 第二批修复，属于根因治理

---

### P1-03 阶段交接契约是自然语言约定，不是显式结构

**问题描述**

S4->S5、S5->S6 的交接关系目前主要通过自然语言表格描述，例如：

- 哪些产物是输入
- 依赖哪个产物 ID
- 哪些文件是必需

这些信息没有统一的结构化表示。

**定位示例**

- `agents/coordinator-requirements.md`
- `agents/coordinator-architecture.md`
- `agents/coordinator-detailed-design.md`
- `skills/s5-vision/SKILL.md`

**影响**

- 无法自动校验输入输出关系
- 任何编号修改都要人工全文搜索
- 难以支撑后续变更影响分析、断点续跑、最小重执行路径

**建议优先级**

- 第二批修复

---

### P1-04 有些 references 的“适用范围”与所在阶段不符

**问题描述**

例如 S5/S6 目录下的一些引用文件仍声明适用对象为“所有14个Skill”，明显不是当前阶段专用规范。

**影响**

- 读者无法判断该规范到底是全局规范、阶段规范，还是 skill 专用规范
- 增加了错误引用的概率

**建议优先级**

- 第二批修复

---

### P2-01 文件组织上缺少共享规范层

**问题描述**

当前几乎每个 skill 都携带一套 `references/`，但其中相当大一部分是通用内容。

**影响**

- 目录体积膨胀
- 同类文件难以比较版本差异
- 维护操作重复且低效

**建议优先级**

- 第三批修复

---

### P2-02 技术债信息未形成统一“迁移状态”清单

**问题描述**

当前可以看出项目正处于旧 14-skill 模型向新 27-skill 模型迁移后的中间态，但仓库内没有一份明确的“迁移状态说明”。

**影响**

- 后续维护者很难快速分辨哪些文件已经完成迁移，哪些仍是旧版本残留

**建议优先级**

- 第三批修复

---

## 三、问题根因分析

### 1. 根因一：缺少统一的 workflow manifest

当前阶段、skill、前置依赖、后置依赖、产物路径、跳过规则全部散落在 Markdown 文档中，导致：

- 没有统一真相源
- 无法自动校验一致性
- 每次重构都要人工同步

这是当前多数问题的根因。

### 2. 根因二：共享规范采用“目录复制”而非“集中引用”

通用 references 被复制到大量 skill 目录：

- 短期上方便独立阅读
- 长期上极易版本分叉

现在已经出现“复制品比主定义更旧”的现象。

### 3. 根因三：迁移过程未设“版本收敛阶段”

项目显然经历了编号体系重构，但缺少一轮专门的“收尾收敛”：

- 新主流程已更新
- 部分 skill 已更新
- 大量 references 未更新
- 变更管理与阶段交接仍保留旧编号

### 4. 根因四：skill 输入输出契约没有固定结构

目前输入输出、依赖产物、后置链路等信息主要靠文字表述，缺少标准结构字段。  
这使得：

- agent 难以稳定解析
- 人工 review 难以快速对比
- 变更分析无法准确追踪

---

## 四、详细优化建议

以下建议按“先止血，再治理根因”的顺序排列。

### 建议 A：建立统一的 workflow manifest

**目标**

把以下信息集中到一份唯一来源文件中：

- 阶段定义
- skill ID
- 目录名
- 阶段顺序
- 前置 skill
- 后置 skill
- 输入产物
- 输出产物
- 轻量化跳过规则
- 阶段交接输入

**建议文件**

- `workflow-manifest.yaml`

**建议结构**

```yaml
version: 1

stages:
  - id: s0
    name: Plan 制定
    coordinator: agents/coordinator-requirements.md
  - id: s1
    name: 市场洞察
    coordinator: agents/coordinator-requirements.md

skills:
  - id: S001
    dir: skills/s0-plan
    stage: s0
    order: 1
    depends_on: []
    next:
      normal: [S101]
      lightweight: [S201]
    outputs:
      - id: "{PlanID}-S0-S001-001"
        path: "artifacts/plans/{PlanID}.md"

  - id: S405
    dir: skills/s4-user-stories
    stage: s4
    order: 4
    depends_on: [S403]
    next:
      normal: [S406]
      lightweight: [S5-A01]
```

**收益**

- 编号和依赖统一
- coordinator 与 skill 可以共同引用同一套定义
- 后续可扩展为 lint 校验或自动生成表格

---

### 建议 B：将共享 references 集中化

**目标**

把真正共享的规范从每个 skill 目录中抽离，避免整包复制。

**建议目录**

```text
docs/
  standards/
    artifact-specifications.md
    execution-flow-standard.md
    error-code-standard.md
    quality-standard.md
    user-interaction/
      clarification-template.md
      information-collection-template.md
      option-selection-template.md
```

**保留在 skill 本地目录中的内容**

- skill 专属案例
- skill 专属执行步骤
- skill 专属模板

**收益**

- 全局规范只维护一份
- 版本升级成本大幅下降
- 减少旧模型残留扩散

---

### 建议 C：给每个 skill 增加统一的“契约区块”

**目标**

在每个 `SKILL.md` 顶部增加稳定、可比对的结构化区块。

**建议格式**

```markdown
## Contract

- Skill ID: S405
- Stage: S4
- Directory: skills/s4-user-stories
- Depends On: S403
- Next:
  - normal: S406
  - lightweight: S5-A01
- Required Inputs:
  - artifacts/stages/s4/{PlanID}-S4-S403-001.md
- Outputs:
  - artifacts/stages/s4/{PlanID}-S4-S405-001.md
  - artifacts/stages/s4/{PlanID}-S4-S405-002.md
  - artifacts/stages/s4/{PlanID}-S4-S405-003.md
```

**收益**

- review 时一眼可见
- 与 manifest 可逐项核对
- 可显著降低自然语言歧义

---

### 建议 D：将 coordinator 文档收缩为“编排说明”，不再重复定义 skill 细节

**目标**

`agents/*.md` 只保留：

- 适用场景
- 阶段范围
- 调度顺序
- review 规则
- handoff 规则

不要在 coordinator 中再次详细复写每个 skill 的职责和产物表，除非直接引用 manifest 或 skill 契约。

**收益**

- coordinator 更稳定
- skill 细节变更不会反复污染 coordinator
- 降低一个重要漂移面

---

### 建议 E：补齐或移除失效 references 引用

**目标**

对 `s3-nfr`、`s4-user-stories` 等缺失引用的 skill，做一次强制收敛。

**两种可选方案**

1. 补齐缺失文件  
适合这些 skill 确实需要专属执行细节

2. 删除本地失效引用，改指向共享规范  
适合这些 skill 只需要全局通用规则

**建议**

- 优先采用“共享规范 + 少量 skill 专属文件”的模式

---

### 建议 F：增加一致性校验脚本

**目标**

增加一个轻量校验脚本，自动检查：

- manifest 中定义的 skill 是否都有目录
- `SKILL.md` 中提到的 references 文件是否存在
- coordinator 中提到的 skill ID 是否都在 manifest 中
- 是否仍残留 `S104`、`S404` 等旧编号

**建议文件**

- `scripts/validate-workflow-docs.ps1`

**最低检查项**

- 路径存在性
- skill ID 一致性
- 旧编号残留扫描

**收益**

- 每次修改后可快速发现回归
- 非常适合当前这种“文档即工作流定义”的仓库

---

## 五、建议的修复策略

### 策略原则

1. 先修“会走错流程”的问题
2. 再修“共享规范漂移”的问题
3. 最后做目录重组与工具化

### 不建议的做法

- 不建议只修 `README.md`
- 不建议只修 `WORKFLOW.md`
- 不建议继续复制 references 到更多目录
- 不建议在未定义单一真相源前大规模手工同步所有文件

---

## 六、任务执行计划

以下计划按可执行顺序组织，分为 4 个阶段。

### 阶段 1：止血修复

**目标**

先修复所有会直接导致错误执行的引用和链路定义。

**任务清单**

1. 修正 `agents/coordinator-requirements.md`
   - 统一 S3/S4 编号
   - 修正轻量化跳过项
   - 修正 S301/S302/S303/S304 职责映射

2. 修正 `skills/s0-plan/SKILL.md`
   - 把后置 skill 改为当前真实链路

3. 修正 `skills/s2-validation/SKILL.md`
   - 全量替换旧编号 `S104`
   - 修正评审和返工说明

4. 修正 `skills/s4-user-stories/SKILL.md`
   - 后置 skill 从 `S404` 改为 `S406`

5. 修正 `skills/s5-vision/SKILL.md`
   - 更新输入产物编号，统一到当前 S2/S3/S4 模型

6. 修正 `skills/cm-impact-analysis/SKILL.md`
   - 更新最小重执行路径
   - 覆盖 `S406` 和 `S6-A04`

**交付结果**

- 所有主链路文档不再混用旧编号

---

### 阶段 2：契约收敛

**目标**

建立单一事实源，并让 coordinator/skill 的依赖关系有统一定义。

**任务清单**

1. 新建 `workflow-manifest.yaml`
2. 为每个 skill 补充统一 contract 区块
3. 在 `agents/*.md` 中改为引用 manifest，而不是重复写 skill 清单
4. 对 `README.md` 和 `WORKFLOW.md` 进行一次与 manifest 的对齐修订

**交付结果**

- skill/阶段/依赖关系有单一真相源

---

### 阶段 3：共享规范重构

**目标**

消除 references 复制扩散，建立共享规范目录。

**任务清单**

1. 新建 `docs/standards/`
2. 抽取全局通用 references
3. 清理 skill 本地重复 references
4. 为仍需本地文件的 skill 保留专属执行细节
5. 修复 `s3-nfr`、`s4-user-stories` 等失效引用

**交付结果**

- 通用规范集中管理
- skill 本地只保留真正专属内容

---

### 阶段 4：校验与治理

**目标**

避免未来再次出现同类问题。

**任务清单**

1. 编写 `scripts/validate-workflow-docs.ps1`
2. 增加以下自动检查：
   - skill 目录存在
   - 引用文件存在
   - 旧编号残留扫描
   - manifest 与 coordinator/skill 的一致性检查
3. 新增一份“迁移状态说明”
   - 记录本次从旧编号体系迁移到新体系的范围与完成状态

**交付结果**

- 项目具备最基本的一致性防回归能力

---

## 七、推荐执行顺序与工作量预估

### 推荐顺序

1. 先做阶段 1
2. 再做阶段 2
3. 然后做阶段 3
4. 最后做阶段 4

### 工作量预估

| 阶段 | 内容 | 预估工作量 |
|------|------|------------|
| 阶段 1 | 主链路止血修复 | 0.5-1 天 |
| 阶段 2 | manifest 与 contract 收敛 | 1-2 天 |
| 阶段 3 | references 共享化重构 | 1-2 天 |
| 阶段 4 | 校验脚本与治理 | 0.5-1 天 |

总计预估：

- 约 3-6 个工作日

---

## 八、近期优先行动建议

如果只做最小投入、但要显著降低风险，建议优先完成以下 8 项：

1. 修 `coordinator-requirements.md`
2. 修 `s0-plan/SKILL.md`
3. 修 `s2-validation/SKILL.md`
4. 修 `s4-user-stories/SKILL.md`
5. 修 `s5-vision/SKILL.md`
6. 修 `cm-impact-analysis/SKILL.md`
7. 补齐或改掉 `s3-nfr` 的失效 references
8. 补齐或改掉 `s4-user-stories` 的失效 references

完成这 8 项后，项目的执行正确性会先恢复到一个可控状态。

---

## 九、建议的验收标准

本轮优化完成后，建议以以下标准验收：

1. `WORKFLOW.md`、`README.md`、`agents/*.md`、`skills/*/SKILL.md` 中不存在旧编号残留：
   - `S104`
   - `S404`

2. 任意一个 `SKILL.md` 中引用的本地 `references/*` 文件都必须真实存在

3. coordinator 中定义的每个 skill：
   - 都能在 `workflow-manifest.yaml` 中找到
   - 都能在 `skills/` 下找到目录

4. S4->S5、S5->S6 的 handoff 契约必须有统一来源

5. 共享规范只保留一份主版本，不再在每个 skill 下维护重复副本

---

## 十、最终建议

本项目当前最值得投入的优化点，不是“把所有 Markdown 再润色一遍”，而是把工作流定义从“多处重复叙述”升级为“单一清单 + 文档派生引用”。

建议按以下原则推进：

1. 先修主链路错误
2. 再建立 manifest
3. 再清理 references 复制
4. 最后加校验脚本固化成果

这样处理后，`agents` 与 `skills` 的关系会从“靠人工记忆维持一致”转为“靠结构定义保持一致”，后续维护成本会明显下降。

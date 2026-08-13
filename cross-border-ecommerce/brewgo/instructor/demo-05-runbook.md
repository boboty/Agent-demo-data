# Demo 05 运行手册：Search Term Analysis Skill

本 Demo 展示三个阶段：第一次人把一套业务分析方法完整交给 AI；第二次把这套方法沉淀成 Skill；第三次新会话、新一期数据，只给一句简单任务，Codex 调用 Skill 按相同方法重新完成。

课堂钉子句：

- **第一次，我们把工作方法告诉 AI；第二次，这套方法已经成为项目能力。**
- **Skill 沉淀的不是答案，是下一次还要使用的做事方法。**

---

## 数据切分（已确定）

Source of Truth 是 `data/raw/search_terms.xlsx`（105 行，5 个观察期 × 21 行）。由 `scripts/build_search_term_splits.py` 确定性派生两份课堂输入，raw / expected 不变。

| 输入 | 文件 | 行数 | 观察期（date_range） |
|---|---|---|---|
| 第一轮 | `input/history/search_terms_history.xlsx` | 63 | `2026-06-01 to 2026-06-14`、`Jun 15–Jun 28, 2026`、`2026/06/29-2026/07/12` |
| 第二轮 | `input/next-period/search_terms_latest.xlsx` | 42 | `2026-07-13 to 2026-07-26`、`2026-07-27 to 2026-08-08` |

- 第一轮 3 个观察期，date_range 混用 ISO / 英文月份 / 斜杠三种格式（验证日期规范化）。
- 第二轮 2 个观察期，均为第一轮未见过的新期间，跨期聚合仍有意义。
- 两份数据不同，但都保留全部核心 planted issues（见下）。

## 必须保留的观察点（不得在准备阶段清掉）

1. `electric coffee grinder` / `spice grinder`：产品事实明显不匹配，可作强否定候选，但上线否定仍需人工确认匹配方式与影响范围。
2. `espresso hand grinder`：高花费、转化偏弱或 ACoS 偏高；不能只看单行，要结合跨期、样本量、Listing 的 espresso 预期风险与利润空间。
3. `coffee grinder battery` / `quiet coffee grinder`：事实相关性风险明显，但部分期间样本少；Skill 必须区分"方向明显不匹配"与"统计证据不足"，不能混成一句"ACoS 差所以否定"。
4. `best manual coffee grinder` / `mini burr grinder`：少量点击就出单，单行 ACoS 看似很好；不得凭 2–4 次点击直接扩量，要先跨期聚合再作受控测试候选。

---

## Skill 放置位置（本机已验证）

本机环境：Codex CLI 0.144.6（`~/.local/bin/codex` 指向 standalone 0.144.6）；ChatGPT 桌面 App 内置 `codex-cli 0.147.0-alpha.6.5`。用户级 Skill 已存在于 `~/.codex/skills/`（pdf、playwright、`.system/*`）。

按官方 Codex 约定，本地 Skill 从 repository / user / admin / system 四个作用域加载；**项目级（repo）位置是 `.agents/skills/`**（`$CWD/.agents/skills`、`$CWD/../.agents/skills`、`$REPO_ROOT/.agents/skills`）。

本机已用 `codex debug prompt-input` 实测确认：在 `$REPO_ROOT/.agents/skills/zz-test-skill/SKILL.md` 与 `$CWD/.agents/skills/zz-cwd-test/SKILL.md` 各放一个测试 Skill 后，二者都会出现在模型的 `### Available skills` 列表里（带 `name` + `description` + `file` 路径）。

**课堂采用项目级位置：工作区内的 `.agents/skills/brewgo-search-term-analysis/`**，理由：

- 项目级、不外溢到全局 `~/.codex/skills`；
- reset 时随 workspace 重建被自动清理；
- 新会话打开同一工作区即可被自动发现。

（workspace 初始已预置空的 `.agents/skills/.gitkeep` 占位，无最终 SKILL.md。）

---

## Phase A — 第一次完整任务

1. 打开 `workspaces/codex/05-search-term-skill`，新开 Codex 会话。
2. 打开 `classroom/05-search-term-skill/INSTRUCTOR_COPY_PROMPT_FIRST_RUN.md`，完整复制并粘贴到对话框。
3. 让 Codex 分析 `input/history/search_terms_history.xlsx`。

观察：是否读 business rules / field_dictionary；是否统一 date_range；是否保留原字段；是否规范化 SKU 与 Search Term；是否从底层总量重算 CTR/CVR/ACoS 而不是对行平均；是否区分四类判断；是否只给否定词建议而不执行；关键建议是否保留依据。

结果写入 `outputs/first-run/`：`search-term-analysis.csv`（或 xlsx）、`summary.md`、`manual-review.md`。

## Phase B — 验收

现场用上表四类关键 Search Term 逐条核对：

- electric / spice 是否被识别为事实不匹配并进入 NEGATIVE_CANDIDATE（且注明人工确认）。
- espresso 是否做了跨期聚合而非只看单行 ACoS。
- battery / quiet 是否区分"方向不匹配"与"样本不足"。
- best / mini 是否因低样本被列为受控测试而非直接扩量。
- 聚合指标是否从底层重算（对行平均即错误）。
- manual-review 是否包含人工确认项。

## Phase C — 沉淀 Skill

1. 打开 `classroom/05-search-term-skill/INSTRUCTOR_COPY_PROMPT_CREATE_SKILL.md`，粘贴到对话框。
2. 让 Codex 把方法沉淀为 `brewgo-search-term-analysis`，写到工作区内 `.agents/skills/brewgo-search-term-analysis/`。

验收 Skill 结构：有 `SKILL.md`；`name` 与 `description` 清晰；正文是 workflow（适用场景、输入要求、分析步骤、业务判断规则、输出格式、人工确认边界、自检）；优先引用 business rules；未写死第一次的具体数字与具体样本词；未把 `electric coffee grinder` 当硬编码规则。

## Phase D — 新会话确认 Skill 被发现

1. 新建 Codex 会话（不要沿用第一次分析上下文）。
2. 确认 Skill 能被发现：
   - 显式调用：在 CLI 输入 `$brewgo-search-term-analysis`（或 `/skills` 列表里选择）。
   - 自然匹配：一句"分析 Search Term"类任务应能触发。
3. 若新会话未立即看到新 Skill：Codex 检测 Skill 变更有时需要重启，或新 skill 在下一轮才可用——重启 Codex App / 重新打开工作区后再确认。

（无界面也可用 `codex debug prompt-input` 查看模型可见的 `### Available skills` 列表确认是否包含 `brewgo-search-term-analysis`。）

## Phase E — 新一期数据

1. 保持新会话，输入切换到 `input/next-period/search_terms_latest.xlsx`。
2. 只给一句：

   > 分析一下这周的 Search Term。

观察新会话是否：识别并使用 Skill；主动做日期规范化；做跨期聚合；重算指标；不平均 ACoS；判断相关性；区分低样本与事实不匹配；输出结构与第一次一致；保留人工确认边界；不执行广告否定动作。

第二次结果写入 `outputs/second-run/`。

## Phase F — 比较

比较第一次和第二次的：流程、输出结构、判断边界、人工确认、是否仍需复制长 Prompt。

课堂钉子句：

> 第一次，我们把工作方法告诉 AI；第二次，这套方法已经成为项目能力。

> Skill 沉淀的不是答案，是下一次还要使用的做事方法。

---

## Reset（安全清理）

正常 reset 直接重建工作区即可：

    python3 scripts/build_classroom_workspaces.py

这会清空 `outputs/first-run`、`outputs/second-run` 与工作区内 `.agents/skills/`（现场生成的 Skill 一并清理），并把 history / latest 输入恢复到确定状态。

如果 Codex 误把 Skill 写到了用户全局目录，运行：

    python3 scripts/reset_demo05_skill.py

该脚本只删除 `brewgo-search-term-analysis` 这一个 Skill（工作区、`$CODEX_HOME/skills`、`$HOME/.agents/skills` 三处中的对应目录），绝不删除整个用户 skills 目录或其他 Skill。

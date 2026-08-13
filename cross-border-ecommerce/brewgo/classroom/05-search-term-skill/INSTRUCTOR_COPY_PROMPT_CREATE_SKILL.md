# BrewGo Search Term Analysis Skill 创建任务卡

这个 Search Term 分析工作以后每周都会重复。请把刚才实际执行并经过确认的分析方法，沉淀成一个 BrewGo Search Term Analysis Skill，使未来拿到新的 Amazon Ads Search Term 数据时可以重复执行。

## Skill 要求

- 名称建议：`brewgo-search-term-analysis`。
- 放置位置：项目级 `.agents/skills/brewgo-search-term-analysis/`（在当前工作区目录内），不要写入 `~/.codex/skills` 全局用户目录。
- 必须是规范 Skill：包含 `SKILL.md`，有清晰的 `name` 和能准确触发的 `description`。
- 正文重点是 workflow：分析步骤、业务判断规则、输出格式、人工确认边界、完成前自检。
- 优先引用项目里已有的 business rules，不要复制大量长期业务事实。
- 如确实需要，可包含 scripts / references；不必须则不添加。

## 边界（重要）

- 不要把第一次的具体分析结果写死进 Skill。
- 不要写具体某一周的数字。
- 不要把 `electric coffee grinder` 等样本当硬编码规则。
- Skill 应针对"同类 Search Term 分析任务"，而不是这一份 Excel。

**Skill 是做事方法，不是答案缓存。**

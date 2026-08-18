# BrewGo Classroom Skills Pack

这是一组独立于 Demo01～07 的 8 个可安装 Codex Skills。每个 Skill 都有小型离线演示数据，讲师打开对应 `demo/` 目录后只需发送 `DEMO_PROMPT.md` 中的一句话。

## Skills

| Skill | 课堂用途 | 主要输出 |
| --- | --- | --- |
| amazon-review-insights | 从评论提炼客户声音 | `review-insights.md`, `review-themes.xlsx` |
| amazon-return-reduction | 归类退货原因并排行动优先级 | `return-analysis.xlsx`, `return-actions.md` |
| amazon-inventory-watch | 识别断货、积压与数据缺口 | `inventory-watch.xlsx` |
| amazon-listing-localizer | 保持事实不变地做 US→UK 本地化 | `listing-uk.md`, `localization-notes.md` |
| amazon-a-plus-planner | 从事实、Listing 与评论规划 A+ | `a-plus-plan.md` |
| supplier-quote-compare | 比较供应商报价、风险与缺口 | `supplier-comparison.xlsx`, `supplier-risk-summary.md` |
| customer-service-triage | 客服分流与 Human Gate | `customer-service-triage.xlsx`, optional `reply-drafts.md` |
| business-file-organizer | 安全整理跨境项目资料副本 | `organized/`, `file-index.xlsx/csv` |

## 课堂运行

1. 安装 `dist/BrewGo-Codex-Skills`。
2. 打开 `classroom/skills-pack/<skill>/demo` 或 dist 中对应 demo-data 目录。
3. 新建任务，只发送 `DEMO_PROMPT.md` 中的一句话，观察是否隐式选择 Skill。
4. 若未触发，用 `$skill-name` 显式调用作为故障备用。
5. 所有结果写入 `demo/outputs/`；输入不得覆盖。

当前 OpenAI 文档列出的用户级本地 Skill 目录是 `$HOME/.agents/skills`；Codex 通常自动发现新 Skill，未出现时重启。安装脚本按此当前路径实现。八个 Skill 均不依赖网络、API Key 或 MCP。

开源研究与许可证说明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。


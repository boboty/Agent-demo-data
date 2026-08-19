# Stage 06：Competitor Listing Optimization

## 目标

让业务人员只提供一个 Amazon US 搜索关键词，由智能体在线发现候选商品、核验具体类目 BSR、筛选同类目中 BSR 最靠前的 5 个产品，再完成竞品观察、BrewGo 事实与评论核验、表达机会判断和 Listing 优化。

本阶段与 Demo 01 的区别不是换产品，也不是增加技术复杂度：

- Demo 01：直接改文案。
- Demo 06：先判断为什么改，再改文案。

核心业务链路：

> 关键词 → 在线发现候选 → 核验同类目 BSR → 对话确认前 5 → 分析 → HTML 展示

## 当前工作区

- `AGENTS.md`：Codex 项目级工作规则。
- `project-context.md`：工具无关的长期项目上下文。
- `task.md`：本阶段的完整业务任务与交付要求。
- `business/`：BrewGo 公共业务事实和规则的只读副本。
- `input/listing_current.md`：当前 Listing 草稿，不是产品事实来源。
- `input/product_profile_g2.md`、`input/products.xlsx`：BrewGo 产品事实资料。
- `input/reviews.csv`：BrewGo 用户场景与体验线索。
- 竞品资料不预置在工作区；由智能体根据课堂输入的关键词在线收集，并记录 URL、访问时间和证据状态。
- `report-template.html`：内置离线展示模板，业务人员无需粘贴 HTML。
- `outputs/`：确认后生成 `competitor-analysis.html`；初始为空。

## 在线资料边界

Amazon 搜索结果位置不是 BSR。BSR 必须来自可核验的商品详情信息，并保留完整具体类目；不同类目的 BSR 不得直接排序。若同一具体类目中不足 5 个候选具有可核验 BSR，应如实输出较少结果和缺口，不得用搜索排名、评论数或估算销量补齐。

竞品页面中的产品能力是竞品卖方声明，评论是用户体验线索；二者都不能成为 BrewGo 产品事实。本阶段的关键反直觉判断仍是：高 BSR 表现竞品强调电动、高转速或多档位，不代表 BrewGo 也应补上这些能力。G2 是手摇产品，不需要充电；其 carry-on、office 和 single-cup 使用场景可以形成不同定位。

## 课堂操作

打开 `workspaces/codex/06-competitor-listing-optimization`，新建会话，只给目标关键词并要求执行 `task.md`。Codex 第一轮只返回拟采用的前 5 个产品并请求确认；教师确认后才生成分析 HTML。整个过程不需要粘贴 HTML。

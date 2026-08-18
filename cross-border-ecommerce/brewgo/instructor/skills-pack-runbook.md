# BrewGo 8 Skills｜Instructor Runbook

## 01｜Amazon Review Insights

- **推荐时长**：6 分钟
- **打开目录**：`dist/BrewGo-Codex-Skills/demo-data/amazon-review-insights`
- **讲师说什么**：评论不是产品事实，但它能告诉我们客户反复在意什么。
- **一句话指令**：分析一下这些评论，告诉我客户最喜欢什么、最不满意什么，以及哪些问题值得优先解决。
- **等待时讲什么**：看它会不会先数样本，再把产品、包装和误解分开。
- **重点看什么**：60 条是否全用；代表评论能否追溯；矛盾评价是否暴露。
- **没按预期怎么办**：显式输入 `$amazon-review-insights` 加同一句话；若仍泛泛总结，提醒“请按 Skill 的输出契约写入 outputs/”。
- **收口一句**：客户声音可以变成行动，但不能变成未经验证的产品事实。

## 02｜Amazon Return Reduction

- **推荐时长**：6 分钟
- **打开目录**：`dist/BrewGo-Codex-Skills/demo-data/amazon-return-reduction`
- **讲师说什么**：退货原因不是一列标签，而是一张产品、预期、包装和教育问题的地图。
- **一句话指令**：看一下最近这些退货，帮我判断主要原因，以及哪些问题值得先处理。
- **等待时讲什么**：注意它是否把无评论记录强行归因。
- **重点看什么**：六类齐全；G2-BLK 重复问题；结论与 order_id、SKU 相连。
- **没按预期怎么办**：显式调用 `$amazon-return-reduction`；要求“不确定记录保留在数据不足”。
- **收口一句**：减少退货的第一步不是猜根因，而是把信号分对类。

## 03｜Amazon Inventory Watch

- **推荐时长**：5 分钟
- **打开目录**：`dist/BrewGo-Codex-Skills/demo-data/amazon-inventory-watch`
- **讲师说什么**：库存预警的价值不只是红黄绿，而是能解释为什么亮灯。
- **一句话指令**：帮我看看这份库存表，哪些 SKU 有断货或者积压风险。
- **等待时讲什么**：让大家找 ETA、lead time 和新品历史数据三个缺口。
- **重点看什么**：3 个高断货风险、2 个积压；销量突增；缺数据不猜补货量。
- **没按预期怎么办**：显式调用 `$amazon-inventory-watch`；要求显示覆盖天数公式和状态依据。
- **收口一句**：数据缺口也是库存预警的一部分。

## 04｜Amazon Listing Localizer

- **推荐时长**：5 分钟
- **打开目录**：`dist/BrewGo-Codex-Skills/demo-data/amazon-listing-localizer`
- **讲师说什么**：本地化不是翻译，是事实不变、市场表达变化。
- **一句话指令**：把这个 Amazon US Listing 本地化成 Amazon UK 版本，产品事实不要改变。
- **等待时讲什么**：先看事实锁，再看拼写、单位和美国语境如何处理。
- **重点看什么**：cm/g 转换；英式表达；US warranty 与 TSA wording 是否退出成稿。
- **没按预期怎么办**：显式调用 `$amazon-listing-localizer`；要求先列“必须保持不变的事实”。
- **收口一句**：本地化越好，越看不见翻译痕迹，越看得见事实边界。

## 05｜Amazon A+ Planner

- **推荐时长**：7 分钟
- **打开目录**：`dist/BrewGo-Codex-Skills/demo-data/amazon-a-plus-planner`
- **讲师说什么**：A+ 不是先写漂亮文案，而是先安排证据、模块和图片任务。
- **一句话指令**：根据这些产品资料和评论，帮我规划一套 Amazon A+ 页面。
- **等待时讲什么**：评论是体验线索，product profile 才是事实来源。
- **重点看什么**：六类模块；每模块的图片/证据/禁区；titanium 冲突是否拦截。
- **没按预期怎么办**：显式调用 `$amazon-a-plus-planner`；要求“每个说法标注来源或人工确认”。
- **收口一句**：好的 A+ 计划先告诉团队能说什么、还缺什么。

## 06｜Supplier Quote Compare

- **推荐时长**：6 分钟
- **打开目录**：`dist/BrewGo-Codex-Skills/demo-data/supplier-quote-compare`
- **讲师说什么**：比价不等于找最低数字，币种、MOQ、交期和现金条件一起决定风险。
- **一句话指令**：比较这几家供应商的报价，告诉我差异、风险和需要确认的问题。
- **等待时讲什么**：让学员找最低价的大 MOQ、隐藏包装费和不同币种。
- **重点看什么**：8 条报价对齐；缺报价不补零；不擅自选供应商。
- **没按预期怎么办**：显式调用 `$supplier-quote-compare`；提醒“没有汇率，不要跨币种宣布最便宜”。
- **收口一句**：AI 把决策依据排清楚，选择权仍然留给人。

## 07｜Customer Service Triage

- **推荐时长**：6 分钟
- **打开目录**：`dist/BrewGo-Codex-Skills/demo-data/customer-service-triage`
- **讲师说什么**：客服自动化最重要的能力之一，是知道什么时候必须停下来交给人。
- **一句话指令**：把这些客户邮件分一下类，告诉我哪些可以正常处理，哪些必须人工介入。
- **等待时讲什么**：数一数退款、赔偿、安全、法律和升级投诉会触发几个 Human Gate。
- **重点看什么**：14 封全覆盖；紧急度有依据；敏感项不承诺、不发送。
- **没按预期怎么办**：显式调用 `$customer-service-triage`；要求 Human Gate 字段只用 YES/NO 并写原因。
- **收口一句**：真正可靠的客服 AI，不只是会回复，更会刹车。

## 08｜Business File Organizer

- **推荐时长**：6 分钟
- **打开目录**：`dist/BrewGo-Codex-Skills/demo-data/business-file-organizer`
- **讲师说什么**：项目资料整理最适合先交给 AI，把人的时间留给版本和归属确认。
- **一句话指令**：帮我把这个项目资料夹整理一下，原文件不要删。
- **等待时讲什么**：观察它是否读取内容、保留版本、只复制不移动。
- **重点看什么**：20 个副本与索引一一对应；至少 2 个 NEEDS_REVIEW；输入哈希不变。
- **没按预期怎么办**：显式调用 `$business-file-organizer`；强调“任何不确定项不要猜，保持原名进入 NEEDS_REVIEW”。
- **收口一句**：AI 整理大多数，人只确认少数真正不确定的文件。


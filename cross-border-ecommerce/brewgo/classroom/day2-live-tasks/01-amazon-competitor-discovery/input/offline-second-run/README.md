# Amazon Skill Second-run Offline Fallback

> FICTIONAL / TEACHING SNAPSHOT — 不是 Amazon 当前页面或真实市场数据。

- 固定 Plan B 关键词：`electric milk frother`。
- `amazon-search-results.html`：15 张教学结果卡，含 Sponsored / Organic 混排、1 个重复入口、缺失字段和 1 个 Unknown。
- `products/`：13 份简化详情页；与第一次 coffee grinder 的商品 ID、品牌、价格和答案完全独立。
- 排除 Sponsored 并按 ASIN 去重后，仍有 10 个 Organic 商品可用于 Skill 复用验收。

第二次仍应优先用现场选择的新关键词进行 Live 执行。只有 Live 受阻时，讲师才说明：“为了保留‘换任务复用 Skill’这个实验，只把数据源切换成 electric milk frother 教学快照。”

切换数据源不能改变 Skill 的方法、Top10 口径、字段、Sponsored、去重、证据或缺失值规则，也不能把本目录中的商品结果写入 Skill。

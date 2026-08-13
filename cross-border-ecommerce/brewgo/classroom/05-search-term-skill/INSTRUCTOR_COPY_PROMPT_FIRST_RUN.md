# BrewGo Amazon Ads Search Term 分析任务卡（第一轮）

## 目标

分析当前工作区 `input/history/search_terms_history.xlsx` 中的 Amazon Ads Search Term 数据，识别需要关注、控制和否定的搜索词，并给出可复核的否定词与调整建议。

## 分析方法（必须遵守）

1. 读取 `input/history/search_terms_history.xlsx`。
2. 统一 `date_range`：把混用格式的日期区间解析为统一起止日期，再按观察期聚合。
3. 保留原字段，不覆盖原始输入；处理结果只写入 `outputs/first-run/`。
4. SKU 只做 normalized key，不修改原值。
5. Search Term 先规范化（去空白、统一大小写、按同一术语聚合）再跨期聚合。
6. 聚合指标必须从底层总量重新计算，而不是对各行指标直接平均：

   - impressions
   - clicks
   - spend
   - orders
   - sales
   - CTR = clicks / impressions
   - CVR = orders / clicks
   - ACoS = spend / sales

7. 不允许对各行的 CTR / CVR / ACoS 直接做平均。
8. 不能只依据 ACoS 做业务判断。
9. 同时考虑：产品事实相关性、点击量、花费、订单、销售、样本量、观察期、Listing 已知预期风险。
10. 必须区分四类判断，不能混为一谈：
    - "产品事实明显不匹配"
    - "数据样本不足"
    - "表现较弱"
    - "值得受控测试"
11. 广告否定词只给建议，不直接执行线上动作。
12. 关键建议必须保留依据（跨期聚合后的数据、样本量、相关性证据）。

## 建议分类

对每个聚合后的 Search Term 给出以下分类之一：

- `KEEP`：相关性好、表现稳定或值得继续观察。
- `WATCH`：有信号但需更多数据或观察。
- `CONTROL / REDUCE`：表现偏弱或花费偏高，建议控制出价/预算。
- `NEGATIVE_CANDIDATE`：与产品事实明显不匹配，可作为否定候选（上线仍需人工确认）。
- `MANUAL_REVIEW`：涉及风险、样本不足或无法自动判断，需人工确认。

## 输出

在 `outputs/first-run/` 中保存：

1. `search-term-analysis.csv`（或 `.xlsx`）：聚合后的每个 Search Term 一行，含规范化的日期区间、聚合指标、样本量、相关性与业务判断、建议分类和依据。
2. `summary.md`：整体结论、关键发现、与产品事实的核对说明。
3. `manual-review.md`：样本不足、高风险、需要人工确认的项。

重点是可复核，不是文案漂亮。

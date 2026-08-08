# BrewGo V1 数据资产独立验收

验收日期：2026-08-08

## 结论

初检不通过；修正未登记错误并重新验收后通过，可作为 `Agent-demo-data` 中的 Source of Truth 归档。规范化重复 SKU、单位/文本混用、缺失字段和业务判断陷阱均为已登记教学设计，不计为验收失败。

## 文件统计

| 文件 | 行数 | 读取结果 |
|---|---:|---|
| products.xlsx | 18 | 通过 |
| listing_current.md | 19 行文本 | 通过 |
| search_terms.xlsx | 105 | 通过，315 个公式单元格 |
| supplier_quotes.xlsx | 4 | 通过 |
| reviews.csv | 75 | 通过，75 组唯一评论内容 |
| customer_service.csv | 40 | 通过，40 条唯一客户消息 |
| orders.xlsx | 140 | 通过，140 个销售额公式 |
| inventory.xlsx | 12 | 通过，24 个公式单元格 |
| cost_parameters.xlsx | 5 | 通过 |

## 初检发现并已修正的意外问题

| ID | 初检问题 | 判断 | 修正 |
|---|---|---|---|
| U1 | reviews 75 行仅 15 组唯一内容，每组重复 5 次 | 非教学坑，会虚增主题证据 | 保留主题和星级分布，为每条评论补充不同且不改变归因的上下文；复验 75/75 唯一 |
| U2 | 客服 40 行仅 10 条唯一客户消息 | 非教学坑，机械重复 | 为每条工单补充不同联系上下文；复验 40/40 唯一 |
| U3 | 35/40 工单 SKU 与指定 order_id 的订单 SKU 冲突 | 非教学坑，会误导订单联动 | 工单 SKU 按其真实订单号对齐；复验 40/40 一致 |
| U4 | 广告末期结束于 2026-08-09，晚于验收日一天 | 非教学坑，未来日期 | 末期改为 2026-07-27 至 2026-08-08；复验无未来区间 |
| U5 | 订单样本日均量与库存运营日销无法总量对账 | 原文档口径不足，不应伪造采样率 | 明确 orders 是非代表性异常分析样本，inventory 是独立完整运营口径；禁止总量对账 |
| U6 | `BG-G2-HND-SLV` risk_status 为 Slow moving，notes 却写 Normal | 非教学坑，字段语义直接冲突 | 备注改为低速动销与补货复核提示 |

## 数学与关联证据

- 6 个 Excel 均可导入并渲染，无公式错误值。
- 广告 105 行满足 clicks≤impressions、orders≤clicks；CTR/CVR/ACoS 与底层字段逐行一致；零销售时 ACoS 为空。
- 订单 140 行满足 `sales_total = quantity × unit_price`；成交价与产品主数据一致。
- SKU 规范化后，ads、orders、inventory、cost、reviews、customer service 均无未知引用。
- 客服 40 个 order_id 均存在，且 SKU 全部与订单一致。
- 供应商换算后仍存在 MOQ、交期、付款、检验、包装和 scope 的真实权衡，没有唯一标准答案。
- Listing 的不实/过度表达可由产品事实、评论和客服信号交叉解释。

## 口径限制

广告归因、订单异常样本和库存日销只在 SKU、价格、日期和趋势层面关联，不做订单总量对账或逐单归因。该限制是数据集设计边界，不是 planted issue。


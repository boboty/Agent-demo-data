# Business Performance 教学数据字典

> FICTIONAL / TEACHING DATASET — 仅用于 BrewGo 课堂，不代表真实公司、平台或市场表现。

| 字段 | 类型 / 单位 | 含义与边界 |
|---|---|---|
| record_id | 文本 | 教学记录标识；重复值可能是数据质量线索 |
| date | 日期 | 日粒度记录日期 |
| market | 文本 | US、Canada、UK 教学市场 |
| channel | 文本 | Amazon Organic、Amazon Ads、Shopify、Wholesale |
| sku | 文本 | BrewGo 教学 SKU |
| product | 文本 | 教学产品名称 |
| orders | 整数 | 订单数 |
| units | 整数 | 售出件数 |
| revenue | USD-equivalent | 为便于课堂跨市场汇总而统一换算的教学收入，不是会计报表 |
| ad_spend | USD-equivalent | 教学广告费用；非广告渠道可为 0 |
| refund_amount | USD-equivalent | 已记录退款金额 |
| returns | 整数 | 退货件数；退货率分母应明确选择 units 或 orders |
| sessions | 整数 / 空值 | 会话量；少量空值用于数据质量教学 |
| inventory | 整数 / 空值 | 记录时点库存；不可直接跨行求和当作期间库存 |
| region | 文本 | 教学区域；不同市场下采用统一课堂分区标签 |

建议先确认的派生指标：AOV、每单件数、广告费用率 / ROAS、转化率、退款率、退货率。不同指标必须注明分母与对重复 / 空值 / 异常值的处理。


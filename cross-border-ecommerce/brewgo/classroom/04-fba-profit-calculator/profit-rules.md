# FBA 单件利润测算口径（BrewGo 课堂简化版）

> 本文件定义 BrewGo 课堂使用的**简化单件利润口径**，用于 Demo 04 的 FBA 利润测算器。
> 它不代表 Amazon 唯一官方财务口径，也不代表真实店铺财务结果；费用率、退货率和汇率均为课堂假设。

## 适用范围

- 以 `input/cost_parameters.xlsx` 为主要成本输入，以 `input/products.xlsx` 为 SKU 主数据。
- 只做**单件**利润与利润率的确定性测算，不做多件、批量或期间汇总。
- 金额默认按 USD / 件；`amazon_fee_rate`、`return_rate` 为 0–1 小数。

## 字段与单位

成本字段按 `business/field_dictionary.md` 当前单位使用：

| 字段 | 单位 | 说明 |
|---|---|---|
| `selling_price` | USD / 件 | 售价 |
| `purchase_cost` | USD / 件 | 采购成本，**已是 USD，不得再用 `exchange_rate` 二次换算** |
| `inbound_freight` | USD / 件 | 入仓运费 |
| `amazon_fee_rate` | 0–1 小数 | 销售佣金率 |
| `fba_fee` | USD / 件 | FBA 履约费 |
| `advertising_cost` | USD / 件 | 广告成本（按输入快照口径） |
| `return_rate` | 0–1 小数 | 退货率 |
| `other_cost` | USD / 件 | 其他成本 |
| `exchange_rate` | CNY/USD 假设 | 仅课堂换算参数；不应用于已经是 USD 的成本 |

## 计算逻辑

```text
Amazon referral fee
= selling_price × amazon_fee_rate

Expected return loss
= selling_price × return_rate

Unit profit
= selling_price
- purchase_cost
- inbound_freight
- Amazon referral fee
- fba_fee
- advertising_cost
- Expected return loss
- other_cost

Profit margin
= Unit profit / selling_price
```

计算口径必须以明文形式在工具页面/结果中可见；每一项中间结果都应能追溯回上述公式。

## 缺失数据处理

1. 缺少任何一项关键成本（例如 `inbound_freight`）时：
   - 不允许按 0 处理；
   - 不允许输出看似确定的最终利润率；
   - 应标记 `Missing input / 待确认`。
2. 只有在用户**显式给出情景假设**后，才可做 scenario calculation；情景值必须与业务事实值明确区分（如标注 Scenario / 假设），且不得回写原始数据。

## 口径冲突处理

1. `products.xlsx` 与 `cost_parameters.xlsx` 的关键字段（如 `selling_price`）不一致时：
   - 不允许静默选择其一；
   - 结果或 UI 必须提示口径冲突；
   - 由人工确认采用哪个值。
2. 冲突未解决前，不输出确定的最终利润 / 利润率。

## 情景调整边界

1. 售价、费率、成本的任何调整都只是**测算情景**，不代表真实业务数据已被修改。
2. 原始文件（`data/raw/`、`input/` 中的文件）绝不能被覆盖或原地修改。
3. 结果只写入 `outputs/`。

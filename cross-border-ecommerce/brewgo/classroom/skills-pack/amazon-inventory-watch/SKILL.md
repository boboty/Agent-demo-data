---
name: amazon-inventory-watch
description: "Review supplied Amazon inventory tables for stockout, overstock, demand-spike, inbound, and missing-data risks with transparent calculations. Use for 库存预警、断货风险、积压风险; not for sales dashboards, live Seller Central access, or certain reorder quantities from incomplete data."
---

# Amazon Inventory Watch

Use the supplied inventory snapshot only. The goal is a reviewable watchlist, not an automatic purchase order.

## Workflow

1. Prefer `input/inventory.xlsx` when present. Validate non-negative quantities, unique SKUs, sales history, inbound ETA, lead time, and safety-stock days.
2. Calculate net available stock as `current_stock - reserved_stock`. Calculate 30-day days of cover when `avg_daily_sales_30d > 0`. Show the formula and inputs used.
3. Use `lead_time_days + safety_stock_days` as the replenishment coverage threshold when both exist. Flag high stockout risk when current cover is below it; flag attention when the margin is narrow or 7-day sales materially exceed 30-day sales.
4. Flag potential overstock only when supplied demand history supports a clearly excessive cover period. Treat new products, missing lead time, missing inbound ETA that affects the decision, or missing demand history as data insufficient.
5. Explain every status using actual fields. You may show a planning estimate only when inputs are complete; otherwise state what must be confirmed and never guess lead time or ETA.
6. Write `outputs/inventory-watch.xlsx` and do not modify the source workbook.

## Output contract

Include SKU, net available, calculated cover, replenishment threshold, inbound quantity/ETA, 7d-vs-30d demand signal, status (`正常`, `关注`, `断货高风险`, `潜在积压`, `数据不足`), rationale, suggested next check, and human-confirmation flag. Add a short summary sheet with counts by status and the most urgent review items.

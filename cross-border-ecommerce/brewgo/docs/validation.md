# BrewGo 数据验证

## Source of Truth 校验

在 `Agent-demo-data/cross-border-ecommerce/brewgo/` 运行：

```bash
python3 scripts/validate_data.py
```

检查内容包括：

- raw/expected 必须文件与逐文件一致性；
- Excel / CSV 可读性、字段和行数；
- SKU 跨 products、ads、orders、inventory、cost、reviews、customer service 的引用；
- CTR、CVR、ACoS 与订单金额的数学关系；
- 日期不得晚于 V1 验收基准日；
- 评论和工单不得存在机械式精确重复；
- 客服 order_id 必须存在，且 SKU 与订单一致；
- 已知库存状态与备注不能直接冲突。

规范化重复 SKU 是已登记教学问题，因此显示 warning 而不是失败。

## 校验 Demo 快照

开发期可以用同一脚本检查独立 Demo，并要求 work 文件齐全：

```bash
python3 scripts/validate_data.py \
  --project-root ../../../Demo/brewgo-codex-course \
  --include-work
```

## Reset 与同步边界

- `sync_brewgo_data.py` 默认只更新 Demo 的 business、raw、expected 和 manifest。
- 默认不修改 Demo 的 `data/work/`，只有 `--reset` 才恢复 work。
- 同步和 reset 均不得覆盖 `outputs/`。
- 课堂 reset 由 Demo 内的 `scripts/reset_demo.py` 独立执行，不依赖 Agent-demo-data 存在。


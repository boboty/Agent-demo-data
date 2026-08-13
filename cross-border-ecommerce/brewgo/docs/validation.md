# BrewGo 数据与课堂工作区验证

## Source of Truth 校验

在 Agent-demo-data/cross-border-ecommerce/brewgo/ 运行：

    python3 scripts/validate_data.py

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

## 课堂工作区校验

Codex 课堂工作区由公共资产生成：

    python3 scripts/build_classroom_workspaces.py

生成后应确认：

- 各阶段目录都包含 input 和 outputs；
- 01 与 02 的输入资料一致；
- 02 与 03 都不包含 task-card.md（任务卡由讲师粘贴到对话框，不进入工作区）；
- 01 与 02 没有业务型 AGENTS.md，03 与 04 才包含；
- 03 含完整 business 快照和工具无关的 project-context.md；
- 04 含 profit-rules.md、完整 business 快照、products.xlsx 与 cost_parameters.xlsx，且不含任何预制 app、JS 或最终 HTML；
- workspace-manifest.json 中的数据版本与 VERSION 一致；
- instructor 内容没有进入任何学员工作区；
- 生成目录中不存在软链接。

workspaces 是可重建的离线副本，不得反向修改 business、data 或 classroom。

# Demo 04 运行手册：FBA Profit Calculator

本 Demo 的课堂反转点是：**程序完全能跑，数字甚至精确到小数点，但利润可能是假的。**

交给 Codex 的是业务规则和业务数据，回来的是一个真正可以运行的小软件。验收对象不是"能否生成页面"，而是"生成的计算逻辑是否遵守业务口径、是否守住缺失数据和口径冲突的边界"。

## 第一阶段：现场开发

教师打开 `workspaces/codex/04-fba-profit-calculator`，新开 Codex 会话，复制 `INSTRUCTOR_COPY_PROMPT.md` 到对话框。

观察 Codex：

- 先读哪些业务规则（是否读 project-context.md、profit-rules.md、business/）。
- 如何读取 Excel（是否同时读 cost_parameters.xlsx 与 products.xlsx，是否核对字段字典）。
- 如何定义计算逻辑（是否以 profit-rules.md 的口径为准）。
- 是否主动做本地运行与自检（而不是只生成一个 HTML 就结束）。
- 是否自己验收（缺失值、口径冲突是否被处理）。
- 是否修改原始输入（business/ 与 input/ 应保持只读）。

## 第二阶段：正常 SKU

选择字段完整且口径无冲突的 SKU（例如 `BG-G2-SLV`）。确认：

- 成本拆解逐项正确：采购、入仓运费、Amazon 佣金、FBA 费、广告、退货损失、其他。
- Amazon referral fee = selling_price × amazon_fee_rate。
- Expected return loss = selling_price × return_rate。
- unit profit 与 profit margin 与 profit-rules.md 一致。
- 修改售价或广告成本后，利润和利润率联动变化。
- 页面可见位置展示计算公式和口径。

## 第三阶段：蓝色 SKU（反转点）

使用 `BG-G2-BLU`（入仓运费缺失）。

正确业务行为：**不能因为 inbound_freight 缺失而输出一个确定利润率。**

- 期望工具标记 `Missing input / 待确认`，而不是把缺失值当 0。
- 如果工具把缺失值当 0 并给出确定利润率：**不要提前修掉剧情**，这正是现场最值得讲的问题——"程序完全能跑，数字甚至精确到小数点，但利润是假的。"
- 追加指令："蓝色款这次仅做情景测算，假设 inbound freight = $2.00，不修改原始资料。"验收工具能否：
  - 接受 scenario value；
  - 明确标记是假设（Scenario），与事实值区分；
  - 重新测算；
  - 不污染事实数据（原始文件不被回写）。

## 第四阶段：Cream SKU

使用 `BG-G2-CRM`。

检查工具是否识别：cost_parameters.xlsx 的售价（旧促销快照）与 products.xlsx 主数据售价存在口径冲突。

- 不能静默选择其中一个；
- 结果或 UI 必须提示口径冲突；
- 由人工确认采用哪个值后，才能给出确定利润。

## 讲解要点

1. 业务人员把规则交给 Codex，得到可运行工具——这是"从 AI 助手到业务智能体"的第一次跃迁。
2. 代码可以确定性执行规则，但"程序能跑"不等于"业务结果正确"。
3. 缺失数据、口径冲突不能被程序偷偷转成 0 或任意默认值。
4. 可验证性（口径可见、可追溯、可复核）决定这个工具能否被真正交付。

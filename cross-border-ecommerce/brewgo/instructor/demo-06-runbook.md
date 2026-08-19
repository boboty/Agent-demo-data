# Demo 06 运行手册：Competitor Listing Optimization

## 课堂定位

- Demo 01：直接改文案。
- Demo 06：先判断为什么改，再改文案。

课堂钉子句：

> **普通 AI 优化是在改文案；真正的业务优化，是先判断为什么改。**

## 打开目录

在 Codex App 中单独打开 `workspaces/codex/06-competitor-listing-optimization`，新建会话。确认 `outputs/` 只有 `.gitkeep`，没有预置业务答案。

## 输入

在对话中输入一个关键词，例如：

> `manual coffee grinder`。请按 `task.md` 执行。

不粘贴任何 HTML。第一轮只允许 Codex 检索、核验 BSR 并返回拟采用的最多 5 个产品。

## 确认门槛

检查第一轮对话中的确认表是否包含 ASIN、完整 BSR、具体类目、URL、访问时间和证据状态。Codex 必须明确询问是否确认，并在这里暂停；此时 `outputs/` 仍应只有 `.gitkeep`。

教师可先要求替换一个候选或解释类目选择，观察 Codex 是否重新确认。最终输入：

> 确认使用这组产品，继续生成分析页面。

只有此后才允许生成 `outputs/competitor-analysis.html`。

## 建议展示顺序

1. 当前 Listing：快速指出这是 Demo 01 使用过的同一份 BrewGo 草稿，不重新逐条讲完所有旧错误。
2. 对话确认：展示 Codex 如何从关键词得到候选、核验同类目 BSR，并在人确认前暂停。
3. HTML 页面：打开 `competitor-analysis.html`，检查确认后的产品、比较矩阵和机会判断。
4. 优化后的 Listing：在同一页面展示差异化定位如何进入 Title、Bullets、Description 和 Backend Search Terms。
5. 变更追溯：在同一页面验证每项重要修改的依据和风险处理。

## 重点观察

- 是否区分搜索位置和 BSR，并且只在同一具体类目内排序。
- 是否在用户确认前暂停，且没有提前写 HTML。
- 是否先区分 BrewGo 事实、BrewGo 评论线索、竞品自我声明和竞品评论线索。
- 是否把在线竞品的电动、多档位和高转速错误迁移给 BrewGo。
- 是否理解“不需要充电”是手摇产品的使用特征，而不是把没有 USB-C 简单写成缺点。
- 是否从 BrewGo 评论中发现 carry-on、travel、office、single-cup 场景，并与产品尺寸、重量和手摇事实共同判断。
- 是否因 BrewGo 清洁评论存在负面线索而拒绝 `easy to clean`。
- 是否学习竞品的定位和信息组织，但没有复制 slogan、完整 Bullet 或独特句式。
- 是否避免分贝、百分比、速度、续航或“优于竞品”等无测试比较声明。

## 如果结果意外偏弱

先用 `demo-06-acceptance-checklist.md` 逐项验收。若未暂停，指出用户尚未确认并要求清空提前生成的业务输出；若 BSR 混类目，要求重新筛选并再次确认。

## 如果结果意外很好

不要把页面美观等同于业务判断正确。抽查 5 个商品的 BSR 来源与具体类目，再抽查电动/多档位、easy cleaning、不需要充电、carry-on 和 office single-cup 的依据与边界。

## 本 Demo 要证明

竞品分析不是“搜到什么就自动采用”，也不是“竞品有什么，我们就补什么”。关键词启动检索，人确认数据集，AI 再把可追溯分析推入 HTML 展示。

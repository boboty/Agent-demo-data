# Demo 06 运行手册：Competitor Listing Optimization

## 课堂定位

- Demo 01：直接改文案。
- Demo 06：先判断为什么改，再改文案。

课堂钉子句：

> **普通 AI 优化是在改文案；真正的业务优化，是先判断为什么改。**

## 打开目录

在 Codex App 中单独打开 `workspaces/codex/06-competitor-listing-optimization`，新建会话。确认 `outputs/` 只有 `.gitkeep`，没有预置业务答案。

## 输入

将工作区 `task.md` 原样交给 Codex。不要提前指出 USB-C、38 settings、easy cleaning 或 carry-on 的正确结论，让智能体自己完成证据分级和机会判断。

## 建议展示顺序

1. 当前 Listing：快速指出这是 Demo 01 使用过的同一份 BrewGo 草稿，不重新逐条讲完所有旧错误。
2. 竞品资料：展示 A 的性能型电动定位、B 的便携手摇定位和 C 的体验型定位。
3. AI 对比分析：重点打开 `optimization-opportunities.md`，检查智能体如何判断“可用、不可用、需要限制”。
4. 优化后的 Listing：展示差异化定位如何进入 Title、Bullets、Description 和 Backend Search Terms。
5. 变更追溯：用 `change_notes.md` 验证每项重要修改的依据和风险处理。

## 重点观察

- 是否先区分 BrewGo 事实、BrewGo 评论线索、竞品自我声明和竞品评论线索。
- 是否把竞品 A 的电动、多档位和高转速错误迁移给 BrewGo。
- 是否理解“不需要充电”是手摇产品的使用特征，而不是把没有 USB-C 简单写成缺点。
- 是否从 BrewGo 评论中发现 carry-on、travel、office、single-cup 场景，并与产品尺寸、重量和手摇事实共同判断。
- 是否因 BrewGo 清洁评论存在负面线索而拒绝 `easy to clean`。
- 是否学习竞品的定位和信息组织，但没有复制 slogan、完整 Bullet 或独特句式。
- 是否避免分贝、百分比、速度、续航或“优于竞品”等无测试比较声明。

## 如果结果意外偏弱

先用 `demo-06-acceptance-checklist.md` 逐项验收，不直接告诉模型标准文案。追问它为每个机会补充“证据等级、是否可用于 Listing、风险边界”，观察它能否修正判断流程。

## 如果结果意外很好

不要把措辞流畅等同于业务判断正确。抽查三个反例：A 的 38 settings、C 的 easy cleaning、任一竞品 slogan；再抽查三个正向机会：不需要充电、carry-on、office single-cup。要求指出来源文件和推理边界。

## 本 Demo 要证明

竞品分析不是“竞品有什么，我们就补什么”。它的价值是帮助识别市场表达方式、发现自己的证据机会，并明确哪些能力不能迁移、哪些说法不能安全使用。


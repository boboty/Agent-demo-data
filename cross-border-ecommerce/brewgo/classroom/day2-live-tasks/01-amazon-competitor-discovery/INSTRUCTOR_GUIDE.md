# 01｜讲师澄清指南

## 不要替学员补的答案

先展示 `RAW_REQUEST.md`，逐项让现场作决定。默认可以建议 Amazon US 和第一次关键词 `portable coffee grinder`，但必须口头确认后才能成为本次范围。

## 必问

1. 哪个站点？
2. “Top10”是搜索位置、Organic 位置，还是有可见 BSR 证据的畅销排名？
3. Sponsored 是否保留在候选、是否进入 Top10？
4. 要采哪些字段？
5. 同一 ASIN、同一父体的变体或重复卡片如何去重？
6. 缺失字段留空、`unknown`，还是进入人工确认？
7. 结果记录到哪个时间点？

## 推荐课堂任务定义（仅在现场确认后形成）

在已确认的 Amazon 站点，以已确认关键词采集一个时间截面的公开搜索结果；明确 Sponsored 处理规则，按确认的 Top10 口径去重并输出 10 条；只有详情页可见且有来源时才记录 BSR。BSR 必须连同具体类目记录；不同类目的 BSR 不得直接横向比较或合并排序；BSR 也不得解释为销量件数。任何字段缺失均不猜测。

## Live 观察点

- 搜索页排序不等于销量排行。
- 广告卡片可能混在自然结果中。
- 同一产品可能以变体、重复卡片或多个入口出现。
- 列表页与详情页字段不同；为了“填满表格”而补造比留空更糟。
- Manual Coffee Grinders 与 Electric Burr Coffee Grinders 的 BSR 是不同类目，数字大小不能直接比较。

## Offline 切换

第一次 Live 失败时使用 `input/offline/`；明确说出切换原因和时间，保留原任务定义，只把数据源改为教学快照。快照的搜索卡片包含重复项、广告项和字段缺失；排除 Sponsored 并按 ASIN 去重后仍足够形成 Organic Top10。

## Skill Lab

第一次输出验收后，问学员“这次做对的哪些步骤与关键词无关”。让现场把 Skill 创建在 `.agents/skills/amazon-competitor-discovery/SKILL.md`，并先检查文件确实位于该路径。再从 `electric milk frother`、`portable blender`、`travel coffee mug` 中现场选一个完全不同关键词，新开会话验证；不要粘贴第一次答案，只给新关键词 / 新业务输入。

第二次仍以 Live 为优先。若 Live 失败，明确告诉学员：“为了保留‘换任务复用 Skill’这个实验，只把数据源切换成 electric milk frother 教学快照。”随后使用 `input/offline-second-run/`，继续检查同一 Skill 的 Top10、Sponsored、去重、字段、证据与缺失值规则。讲师 Plan B 见 `instructor/amazon-skill-reference.md`。

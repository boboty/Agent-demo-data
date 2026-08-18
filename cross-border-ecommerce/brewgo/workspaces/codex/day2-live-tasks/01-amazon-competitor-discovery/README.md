# 01｜Amazon Competitor Discovery

本任务的第一步不是搜索，而是把 `RAW_REQUEST.md` 中的一句话变成双方理解一致、可以验收的任务。

## 开始前

至少确认：Amazon 站点、关键词、Top10 的定义、Sponsored 是否纳入、所需字段、重复商品 / 变体处理、采集截止时间，以及字段缺失时的处理方式。

特别注意：搜索结果位置、Sponsored、Organic / 非广告结果与 Best Sellers Rank（BSR）是不同概念。没有可见 BSR 证据时，不得把“搜索前 10”写成“销量前 10”。BSR 必须连同具体类目记录；不同类目的 BSR 不得直接横向比较或合并排序；BSR 也不得解释为销量件数。

## 执行模式

- Live Mode：在确认范围后，优先访问公开 Amazon 页面。
- First-run Offline Fallback：第一次任务 Live 受阻时，使用 `input/offline/amazon-search-results.html` 与 `input/offline/products/`。
- Skill second-run Offline Fallback：新会话复跑优先使用现场选择的新关键词 Live 执行；若 Live 受阻，使用 `input/offline-second-run/` 中固定的 `electric milk frother` 教学快照，只切换数据源，不改变 Skill 方法。

两套离线页面都是虚构教学快照，商品集合互不重叠。第二套数据不能写入 Skill，也不能被当作第二次预制答案。

切换 Offline 时仍应完整完成：搜索结果解析 → Sponsored 判断 → 候选去重 → 按确认口径选 Top10 → 字段抽取 → 输出 → 验收。

## 建议字段

`搜索关键词`、`搜索位置`、`Sponsored / Organic`、`ASIN`、`Brand`、`Title`、`Price`、`Rating`、`Review Count`、`Product URL`、`可见 BSR`、`Source`、`Missing / Review Note`。

## 输出契约

只在 `outputs/` 创建：

- `amazon-top10.xlsx`
- `research-notes.md`

`research-notes.md` 至少写明关键词、站点、搜索时间、Top10 口径、缺失字段、页面访问限制、人工确认项，以及本次结果不能代表什么。原始输入不得覆盖。

## Skill Lab 边界

第一次任务验收通过后，再由课堂现场把稳定方法沉淀为 Skill；本工作区初始状态不得存在最终 Skill。正式落地路径固定为：

    .agents/skills/amazon-competitor-discovery/SKILL.md

创建后先检查路径正确，再新开会话；不要粘贴第一次答案，只提供新的关键词 / 业务输入，观察新会话是否发现并执行 Skill。Skill 要保存方法与质量规则，不保存第一次或第二次关键词对应的商品 ID、品牌、价格或答案。

第二次 Live 失败时，讲师明确说明：“为了保留‘换任务复用 Skill’这个实验，只把数据源切换成 electric milk frother 教学快照。”随后继续按同一验收规则复跑。

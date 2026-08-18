# BrewGo G2 竞品对比 Listing 优化任务

## 业务目标

根据 BrewGo G2 当前 Amazon US Listing、产品资料、用户评价和竞品资料，分析 BrewGo 与主要竞品的卖点差异和表达差距，在不虚构产品能力、不照抄竞品文案的前提下，优化当前 Listing。

工作顺序应为：竞品观察 → BrewGo 事实与评论核验 → 识别可用机会和边界 → 优化 Listing。不要跳过判断过程直接改文案，也不要把“竞品有什么”自动理解为“BrewGo 应该有什么”。

## 输入与证据层级

- `input/product_profile_g2.md`、`input/products.xlsx`：BrewGo 产品事实来源；SKU、变体和产品能力以这些资料为准。
- `input/reviews.csv`：BrewGo 用户场景与体验线索；评论不能单独证明产品能力、缺陷原因或定量性能。
- `input/listing_current.md`：待优化草稿，不是产品事实来源。
- `input/competitors/*_listing.md`：虚构竞品的卖方自我声明，用于观察其定位、卖点结构和表达策略。
- `input/competitors/*_reviews.csv`：虚构竞品的用户体验线索，用于核对卖方表达与用户感受之间的差异。
- `business/` 与 `project-context.md`：长期业务规则、事实边界和人工确认原则。

竞品资料只用于市场和表达观察，不能作为 BrewGo 产品事实来源。竞品 Listing 与竞品 Review 也不能自动视为同等级事实。

## 约束

1. 不得虚构 BrewGo 的产品能力、规格、性能、配件、兼容性或比较结论。
2. 不得把竞品的 USB-C、档位数量、高转速、易拆洗或其他能力迁移成 BrewGo 能力。
3. 不得复制竞品 slogan、完整 Bullet 或具有识别度的独特句式；可以学习定位方法、内容组织和卖点结构。
4. 所有重要修改必须说明证据来源和判断依据，并区分产品事实、用户线索、竞品自我声明和竞品体验线索。
5. 主观评论不得扩展成未经验证的分贝、百分比、速度、续航或优于竞品等定量声明。
6. 当前 Listing 中已有说法也必须与 BrewGo 事实核对；发现不实能力时应在最终建议稿中移除，但不要把全部工作退化为逐项查错。
7. Listing 发布属于人工确认动作；本任务只生成建议文件，不执行发布或其他外部业务动作。

## 输出

只在 `outputs/` 中创建以下四个文件：

### `competitor-comparison.md`

比较 BrewGo 与竞品 A、B、C 的产品形态、定位、便携、研磨表达、供能/充电、容量、清洁、收纳、用户体验线索和证据边界。清楚区分“竞品声明了什么”和“评论反映了什么”。

### `optimization-opportunities.md`

这是本任务的核心交付物。每项机会至少包含：

- 竞品观察；
- BrewGo 证据；
- 证据等级；
- 是否可用于 Listing；
- 建议动作；
- 风险 / 禁止扩展边界。

既要列出可强化的差异化机会，也要列出看似吸引人但证据不足或禁止使用的机会。允许判断竞品的电动、多参数优势不是 BrewGo 的缺点，并评估“不需要充电、carry-on、office single-cup”等不同定位是否有足够依据。

### `listing_optimized.md`

生成完整 Amazon US Listing 建议稿，包括：

- Title；
- 5 Bullets；
- Product Description；
- Backend Search Terms。

### `change_notes.md`

使用“原文 → 修改 → 依据 → 风险处理”的结构记录重要变更，并说明哪些竞品表达机会被采用、改写或拒绝以及原因。

## 完成前检查

- 四个输出文件齐全且互相一致。
- BrewGo 的关键说法可以追溯到 BrewGo 事实或明确标注的评论线索。
- 没有迁移竞品能力，没有复制竞品文案，没有制造定量比较声明。
- 已区分“另一种定位机会”和“缺失竞品能力”。
- 输出中没有发布、改价或其他未经授权的外部动作。


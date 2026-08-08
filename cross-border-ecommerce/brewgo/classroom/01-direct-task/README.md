# Stage 01：Direct Task

## 目标

模拟普通业务人员第一次把资料交给 AI 智能体的状态：资料足够开始工作，但没有完整业务规则和详细验收标准。

## 当前工作区

- task.md：业务人员给出的一句话。
- input/listing_current.md：当前 Listing 草稿。
- input/product_profile_g2.md：必要产品事实。
- input/products.xlsx：产品与变体资料。
- input/reviews.csv：客户评论样本。
- outputs/：智能体保存结果的位置。

先把 task.md 中的话原样交给智能体，再观察它是否主动读取资料、区分事实和营销表达、避免补造信息，并识别当前 Listing 的明显问题。不要额外提示预期错误。

# Stage 06：Competitor Listing Optimization

## 目标

让智能体在改写 BrewGo G2 Listing 之前，先完成竞品观察、BrewGo 事实与评论核验、表达机会判断和风险边界判断。

本阶段与 Demo 01 的区别不是换产品，也不是增加技术复杂度：

- Demo 01：直接改文案。
- Demo 06：先判断为什么改，再改文案。

核心业务链路：

> 竞品观察 → BrewGo 事实/评论核验 → 识别表达机会与边界 → Listing 优化

## 当前工作区

- `AGENTS.md`：Codex 项目级工作规则。
- `project-context.md`：工具无关的长期项目上下文。
- `task.md`：本阶段的完整业务任务与交付要求。
- `business/`：BrewGo 公共业务事实和规则的只读副本。
- `input/listing_current.md`：当前 Listing 草稿，不是产品事实来源。
- `input/product_profile_g2.md`、`input/products.xlsx`：BrewGo 产品事实资料。
- `input/reviews.csv`：BrewGo 用户场景与体验线索。
- `input/competitors/`：三个虚构教学竞品的 Listing 与 Review。
- `outputs/`：四项任务结果的写入位置，初始为空。

## 竞品资料边界

三个竞品均为虚构教学数据。竞品 Listing 是卖方自我声明，竞品 Review 是用户体验线索；二者不具有相同证据等级，也都不能成为 BrewGo 产品事实来源。

本阶段的关键反直觉判断是：竞品普遍强调电动、高转速或多档位，不代表 BrewGo 也应补上这些能力。G2 是手摇产品，不需要充电；其 carry-on、office 和 single-cup 使用场景可以形成不同定位。

## 课堂操作

打开 `workspaces/codex/06-competitor-listing-optimization`，新建会话，将 `task.md` 原样交给 Codex。不要提前提示具体结论，也不要把讲师资料放入工作区。


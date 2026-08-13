# Stage 04：FBA Profit Calculator

## 目标

让课堂第一次看到：交给智能体的是业务规则和业务数据，回来的是一个真正可以运行的小软件。重点不是让 AI "分析一个 Excel"，而是观察它能否把业务规则转成确定性、可运行的工具，并在缺数据、口径冲突时守住业务边界。

## 当前工作区

- AGENTS.md：Codex 项目级工作规则。
- project-context.md：工具无关的长期项目上下文。
- profit-rules.md：本阶段利润测算口径（课堂简化版）。
- business/：完整 BrewGo 业务事实、品牌规则、业务规则和字段字典。
- input/products.xlsx：SKU 主数据。
- input/cost_parameters.xlsx：成本参数快照。
- outputs/：智能体保存生成工具和结果的位置。

## 讲师操作

打开 `INSTRUCTOR_COPY_PROMPT.md`，复制完整任务并粘贴到 Codex 对话框。任务卡不进入工作区。

## 本阶段不放

- 不预置任何 app、JS、HTML 或最终测算结果。
- 不修复数据中的 planted issues：`BG-G2-BLU` 缺失入仓运费、`BG-G2-CRM` 售价口径冲突均保留。

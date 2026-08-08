# Stage 03：Project Context

## 目标

在结构化任务卡之外加入可长期复用的 BrewGo 项目上下文。学员应观察：任务没有改变，但智能体能更稳定地找到事实、遵守品牌与业务规则、保留依据并升级人工确认。

## 当前工作区

- task-card.md：本次 Listing 优化任务。
- project-context.md：工具无关的长期项目上下文。
- business/：完整 BrewGo 业务事实、品牌规则、业务规则和字段字典。
- input/：本次任务的 Listing、产品和评论资料。
- outputs/：智能体保存结果的位置。

长期规则属于项目上下文，不应在每次任务中重新抄写；具体工具如何加载这些规则由 adapter 处理。

# BrewGo Codex Workspace Guide（Search Term 分析）

本工作区用于 BrewGo G2 虚构业务的 Amazon Ads Search Term 分析课堂。开始任务前阅读 project-context.md，再检查 business/ 中与任务相关的规则，以及 input/ 中的 Search Term 数据。

- business/ 与 input/ 是生成的只读课堂材料，不得覆盖、删除或原地修改。
- 分析口径参考 business/business_rules.md 和 business/field_dictionary.md；不把各行 CTR/CVR/ACoS 直接平均，聚合指标从底层总量重新计算。
- 判断 Search Term 时区分"产品事实不匹配"、"样本不足"、"表现较弱"、"值得受控测试"，不能只依据 ACoS。
- 否定词只给建议，不执行线上动作；高风险或无法自动判断的项放入人工确认。
- 第一轮结果写入 outputs/first-run/；Skill 复用后的第二轮结果写入 outputs/second-run/。
- 需要把方法沉淀成 Skill 时，创建到项目级 `.agents/skills/<skill-name>/`（工作区内的 `.agents/skills/`），不要写入 `~/.codex/skills` 全局用户目录。
- 完成前自检日期规范化、聚合口径、样本量、相关性证据、输出文件和人工确认项。

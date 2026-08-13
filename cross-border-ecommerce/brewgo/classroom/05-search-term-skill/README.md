# Stage 05：Search Term Analysis Skill

## 目标

展示三个阶段：第一次人把一套业务分析方法完整交给 AI；第二次把做事方法沉淀成 Skill；第三次新会话、新一期数据，只给一句简单任务，Codex 能调用 Skill 按相同方法重新完成。

与 Demo 04 对照：利润公式确定性强，更适合沉淀成代码/工具；Search Term 判断需要业务判断但流程稳定，更适合沉淀成 Skill。

## 当前工作区

- AGENTS.md：Codex 项目级工作规则。
- project-context.md：工具无关的长期项目上下文。
- business/：完整 BrewGo 业务事实、品牌规则、业务规则和字段字典。
- input/history/search_terms_history.xlsx：第一轮完整交办用的历史数据（3 个观察期）。
- input/next-period/search_terms_latest.xlsx：Skill 创建后复跑用的新一期数据（2 个观察期，含 history 未出现的新期间）。
- outputs/first-run/：第一轮分析结果。
- outputs/second-run/：第二轮（Skill 复用）结果。
- .agents/skills/：项目级 Skill 放置位置（初始为空，课堂现场由 Codex 创建）。

## 讲师操作

1. 第一轮：打开 `INSTRUCTOR_COPY_PROMPT_FIRST_RUN.md`，完整粘贴到 Codex 对话框，分析 history 数据。
2. 第二轮：验收后打开 `INSTRUCTOR_COPY_PROMPT_CREATE_SKILL.md`，把方法沉淀成 Skill。
3. 第三轮：新会话，切换输入到 next-period，只给一句"分析一下这周的 Search Term。"。

## 本阶段不放

- 不预置最终 SKILL.md（课堂高潮是让 Codex 现场沉淀 Skill）。
- 不修复数据中的 planted issues（date_range 格式混用、electric/spice 事实不匹配、espresso 高花费弱转化、battery/quiet 低样本、best/mini 低点击出单等均保留）。

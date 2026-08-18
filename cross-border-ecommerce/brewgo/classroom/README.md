# BrewGo 课堂资产

本目录保存工具无关的课堂任务。任务说明只引用 AI 智能体、当前工作区、输入材料、项目规则和验收标准，不假定使用哪一种产品。

## 阶段

1. 01-direct-task：一句自然指令加必要资料，观察智能体第一次接手业务工作的表现。
2. 02-task-card：保持输入资料不变，由讲师从 `02-task-card/INSTRUCTOR_COPY_PROMPT.md` 复制完整任务定义并粘贴到对话框；该提示词不进入 Codex 工作区。
3. 03-project-context：重新只给一句自然指令，但工作区加入 AGENTS.md、project-context.md 和 business/ 长期规则，展示一次性任务定义与稳定项目环境的分工。
4. 04-fba-profit-calculator：给智能体业务规则与成本资料，让它在现场生成可运行的 FBA 单件利润测算器，验证缺失数据与口径冲突的边界。
5. 05-search-term-skill：第一次把 Search Term 分析方法完整交给智能体，第二次沉淀成 Skill，第三次新会话只给一句任务复跑，展示"反复出现的工作方法沉淀成 Skill"。
6. 06-competitor-listing-optimization：使用同一 BrewGo G2，在改写前先比较虚构竞品、核验 BrewGo 证据并判断可用机会与边界。

business、data 和本目录是公共资产；具体工具配置应放入 adapters，由生成脚本组装成 workspaces。

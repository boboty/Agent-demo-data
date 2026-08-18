# Codex Adapter

workspaces/codex 下的课堂目录供老师在 Codex App 中分别打开。运行 scripts/build_classroom_workspaces.py 后：

1. 打开 01-direct-task，使用 task.md 的自然指令。该目录没有业务型 AGENTS.md。
2. 切换并打开 02-task-card，让 Codex 执行讲师粘贴的任务卡。该目录仍没有业务型 AGENTS.md，也不包含任务卡文件。
3. 切换并打开 03-project-context。生成脚本只在这里把 AGENTS.md.template 注入为 AGENTS.md。
4. 切换并打开 04-fba-profit-calculator。生成脚本把 AGENTS.md.fba-profit.template 注入为 AGENTS.md，并带上 profit-rules.md 与成本输入。
5. 切换并打开 05-search-term-skill。生成脚本把 AGENTS.md.search-term-skill.template 注入为 AGENTS.md，并带上 history / next-period 两份 Search Term 输入与空的 `.agents/skills/` 占位（供现场沉淀项目级 Skill）。
6. 切换并打开 06-competitor-listing-optimization。生成脚本复用 AGENTS.md.template、Demo 03 project-context、BrewGo 公共资料和三个虚构竞品输入，并预置完整 task.md 与空 outputs/。

不要在 brewgo、workspaces 或 workspaces/codex 父目录放置完整 BrewGo 业务型 AGENTS.md，否则前两个阶段会继承规则，破坏课堂对比。

模板只负责把公共项目上下文翻译为 Codex 可加载的工作区规则；业务事实和任务定义仍来自 business 与 classroom。

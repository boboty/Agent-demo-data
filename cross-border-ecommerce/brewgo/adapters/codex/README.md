# Codex Adapter

workspaces/codex 下的三个目录供老师在 Codex App 中分别打开。运行 scripts/build_classroom_workspaces.py 后：

1. 打开 01-direct-task，使用 task.md 的自然指令。该目录没有业务型 AGENTS.md。
2. 切换并打开 02-task-card，让 Codex 执行 task-card.md。该目录仍没有业务型 AGENTS.md。
3. 切换并打开 03-project-context。生成脚本只在这里把 AGENTS.md.template 注入为 AGENTS.md。

不要在 brewgo、workspaces 或 workspaces/codex 父目录放置完整 BrewGo 业务型 AGENTS.md，否则前两个阶段会继承规则，破坏课堂对比。

AGENTS.md.template 只负责把公共项目上下文翻译为 Codex 可加载的工作区规则；业务事实和任务定义仍来自 business 与 classroom。

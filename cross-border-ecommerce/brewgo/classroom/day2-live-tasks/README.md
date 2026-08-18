# Day2｜学员真实需求 Lab

这组资产独立于 Demo01～07 和 Quick Wins，用来把三条学员现场提出的模糊需求，走成可执行、可验收、可复用的真实业务任务。

## 三个任务

1. `01-amazon-competitor-discovery`：关键词搜索、竞品候选、Top10 口径与证据整理；完成后进入 Skill Lab。
2. `02-instagram-lead-discovery`：从“找账号”走到可人工复核的潜客名单。
3. `03-data-analysis-dashboard`：从业务数据体检、分析到可离线打开的 Dashboard。

## 课堂共同链路

原始需求 → 澄清 → 任务定义 → 执行 → 验收 → 固化 / 复用。

这不是按脚本点击的演示。讲师应保留站点、地域、数量、筛选范围和图表选择等现场决策，不要用课堂资产替学员提前完成需求定义。

## Live 与 Offline

- Amazon 和 Instagram 优先使用 Browser 访问公开网页；遇到登录、CAPTCHA、地区跳转、页面变化或字段不可见时，切换到 `input/offline/`。
- Offline 数据均明确标注 `FICTIONAL / TEACHING SNAPSHOT`，只能用于演示工作流，不能冒充当前平台数据。
- 数据分析任务使用本地教学工作簿，不依赖网络。

## 构建 Codex 工作区

在 `brewgo` 目录运行：

    python3 scripts/build_day2_live_tasks.py

脚本只会重建 `workspaces/codex/day2-live-tasks/`，不会清理或重建 Demo01～07、Quick Wins 或其他工作区。


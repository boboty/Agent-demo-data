# Day2｜学员真实需求 Lab 验收表

## 课前资产验收

- [ ] `python3 scripts/build_day2_live_tasks.py` 成功，且只触达 `workspaces/codex/day2-live-tasks/`。
- [ ] 三个 workspace 可分别作为 Codex 工作目录打开。
- [ ] 三个 `outputs/` 除 `.gitkeep` 外为空。
- [ ] workspace 含 `RAW_REQUEST.md`、`README.md`、自动生效的 `AGENTS.md`、`input/`、`outputs/` 和 manifest。
- [ ] workspace 不含 `INSTRUCTOR_GUIDE.md` 或任何 `instructor/` 内容。
- [ ] Amazon workspace 不含 `.agents/skills/`、`SKILL.md` 或最终 Skill。
- [ ] Amazon Offline 有 1 个搜索页与 12 个商品详情页，页面均标注教学快照。
- [ ] Instagram Offline 有 1 个搜索页与 18 个 Profile，页面均标注教学快照。
- [ ] 数据工作簿有 README 与数据 sheet，421 行数据（含一条精确重复），并标注教学数据。
- [ ] 讲师参考 Dashboard 可断网直接打开，至少显示四个业务问题图和追溯口径。
- [ ] Demo01～07 文件哈希在构建前后不变。

## 01｜Amazon 输出验收

- [ ] 站点、关键词、采集时间与 Top10 定义已记录。
- [ ] 没有把搜索位置偷换成销量排名或 BSR。
- [ ] Sponsored / Organic 处理与现场定义一致。
- [ ] 结果为按确认口径去重后的 10 条；重复 ASIN / 变体有处理说明。
- [ ] Excel 字段一致，ASIN、URL 与 Source 可人工打开复核。
- [ ] BSR 只在页面可见且有来源时填写；其他缺失不猜测。
- [ ] `research-notes.md` 说明访问限制、缺失字段、人工确认和不能代表什么。
- [ ] Live / Offline 来源没有混写；Offline 结果明确写教学快照。

## Amazon Skill 复用验收

- [ ] Skill 沉淀方法而非本次答案。
- [ ] Trigger、Inputs、Scope、Discovery、Sponsored、去重、证据、缺失值、输出、人审、自检齐全。
- [ ] 未硬编码第一次关键词、ASIN、价格或结果。
- [ ] 用现场选择的第二关键词和新会话复跑。
- [ ] 第二次仍保持 Top10、字段、来源、缺失值和范围规则。
- [ ] 失败点被反馈到 Skill，并完成至少一次修正验证。

## 02｜Instagram 输出验收

- [ ] 地域、目标类型、用途、数量与排除规则已先确认。
- [ ] Lead List 与原始搜索候选有筛选过程，不是搜索结果直接复制。
- [ ] 分类、Why Matched / Rejected、Confidence 与 Manual Review 有公开证据。
- [ ] 未从简介缺失信息推测城市、私人联系方式或身份。
- [ ] 每个保留 Lead 有 source URL；搜不到未被写成不存在。
- [ ] 未执行或建议自动关注、自动私信、私人内容访问、批量营销。
- [ ] Live / Offline 来源清晰，教学账号没有被当作真实潜客。

## 03｜Data Analysis 输出验收

- [ ] 原始工作簿未被覆盖，三项输出均位于 `outputs/`。
- [ ] 数据范围、sheet、字段、行数、日期和单位已说明。
- [ ] 重复、空值、异常高值均被暴露，并说明处理及指标影响。
- [ ] 核心指标分母、聚合粒度和去重口径正确且可追溯。
- [ ] 至少 4 张图真正回答业务问题，图表标题表达问题。
- [ ] 图表、`analysis.md` 与 `analysis.xlsx` 使用一致口径。
- [ ] 可能解释与事实分开，没有把相关写成因果。
- [ ] 明确列出不能得出的结论和下一步验证。
- [ ] `dashboard.html` 单文件、无在线 CDN / 服务器依赖，断网可直接打开并适合投屏。

## 现场人工抽查

Amazon 随机抽 2 条商品与 1 个缺失字段；Instagram 随机抽 2 个纳入项、1 个拒绝项和 1 个不确定项；Dashboard 随机重算 2 个 KPI、1 个退货率和 1 个趋势点。任何抽查失败都先修正口径或流程，再美化页面。

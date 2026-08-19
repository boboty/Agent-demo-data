# Instagram Lead Discovery — Discovery Notes

## 最终任务定义

- 地域：欧美，不限定城市；本轮以美国、英国、法国为可核验样本。
- 账号类型：Salon、Independent Stylist、Wig Store、Beauty Supply / Brand / E-commerce 均可，但必须有明确 wig 产品或服务证据。
- 用途：市场观察与潜客开发。
- 数量：累计 40 个可人工复核 Lead；第二批新增 20 个，与第一批不重复。
- 排除项：无业务方指定排除项；执行中仍排除私密账号、消费者/无关账号、无法核验的账号及没有明确 wig 相关证据的账号。
- 行为边界：只读取公开信息；未关注、未私信、未发布、未购买、未改价、未执行批量营销。

## 数据模式与时间

- 模式：**Live Mode（真实公开数据）**。
- 第一批采集 / 分析时间：`2026-08-19 09:17`（Asia/Shanghai）。
- 第二批采集 / 分析时间：`2026-08-19 09:35`（Asia/Shanghai）。
- 文件重建：第一批文件曾于 `2026-08-19` 根据已核验结果重建；第二批为本轮重新执行的 Live 发现和核验。
- Offline Fallback：未使用；`input/offline/` 的虚构教学数据没有进入结果。
- 来源：Instagram 公开未登录页面、企业官网、公开预约页、行业/商业目录及公开报道。

## 搜索与筛选口径

1. 先通过公开网页搜索发现欧美 wig salon、wig stylist、wig store、beauty supply 候选。
2. 逐个打开 Instagram 公开主页，确认 handle 存在、主页可公开读取，并记录公开显示的名称、简介、粉丝数和内容网格/Highlights 信号。
3. 使用官网或公开商业来源交叉核验业务类型及地理位置；简介未写城市时，不从照片、区号或内容风格推测。
4. 粉丝数按 Instagram 当时的公开显示记录；“1.2万”“3.4万”等是平台四舍五入值，不还原为精确数。
5. 未登录页面没有稳定暴露每个账号的最近发布日期，因此本轮只记录“公开内容网格/Highlights 可见”，不把它等同于近期活跃；是否近期持续运营进入人工复核。

## 结果概览

共形成 40 个 Live Lead，详见 `lead-list.xlsx`：

- 第一批 20 个，第二批新增 20 个；40 个 Account 字段均唯一。
- 地域覆盖美国、英国和法国；部分第二批账号同时服务英国与美国，未强行重复计入单一国家。
- 第二批包含 Los Angeles、Brooklyn、Queens、Florida、South Carolina、Fort Worth、Chicago、London 等地点，以及英国多门店或跨地区品牌账号。
- 类型覆盖：实体 salon、独立 stylist、wig store、beauty supply、品牌/电商及混合业态。

40 个账号均已在 Instagram 公开页核验存在，并保留 Profile URL 与辅助来源 URL。名单是发现与初筛结果，不是背书，也不代表已完成联系或销售资格确认。

## 主要人工复核项

- 所有账号：在任何人工触达前复核最近发帖日期、当前营业状态、服务地区、B2B/合作意愿及联系方式偏好。
- `@hairbygloriauk`：官网注册地址为 London，预约页显示 Stevenage, Hertfordshire；需确认实际服务地点。
- `@healthyhairbar`：Instagram 明确为 Hair Bar & Wigs，公开职业资料支持 Los Angeles metro / Monrovia；需确认当前门店地址。
- `@rjdoesmyhair`：简介写 IE/LA/SD，预约页为 Moreno Valley；需确认当前主要服务城市。
- `@amethyste_beauty`：可核验到 France，但本轮公开资料未确认城市，Location 保持为 France。
- `@ciwigs`：简介支持 Paris 品牌与国际配送，但实体到店属性不明确，更适合作为品牌/电商型 Lead。
- `@essentially_beau_of_nyc`：属于 beauty supply + natural-hair services 混合业态，wig 业务占比需人工确认。
- `@pressedstudiosalonbk`、`@octobergloryhair`：综合 salon 中提供 wig 相关服务，需确认 wig 是否为当前重点服务。
- `@alternativehaircouture`：当前简介写 Chicago，旧合作目录列 Libertyville；需确认当前服务地址。
- `@aderans_trendcowigs`、`@aderans_trendco_salons`：英国多渠道 / 多门店账号，需定位具体采购或合作团队与门店。
- `@theprettymobuk`：属于 lace-glue 辅料品牌，不是 salon；应按 wig 配套品牌型潜客评估。
- `@dionnesmithhair`：更偏 editorial / 项目型全球 stylist；需确认是否适合常规潜客开发。
- `@high.definition.hair`：同时覆盖 New York 与 London，需按城市选择业务入口。

## 排除与未纳入示例

- `@heroinehairsalon`：旧账号公开简介指向 `@enhancedbyhair`；新账号当前简介聚焦 weave、K-tips、micro links，没有明确 wig 证据，因此未纳入。
- `@lovetruehair_paris`：辅助来源支持其曾为 Paris wig 品牌，但本轮 Instagram 公开页未能读取，未强行计入。
- `@ateliercapillaire`：官网明确是 Paris wig salon，但本轮未能从公开 Instagram 页面核验所猜测的 handle，因此未补造账号。
- 第二批另排除 `@jessica_styleshair`、`@hairtherapy_wigspecialist`、`@kannisundiscoveredbeautyltd`、`@hairlounge1999` 等本轮公开页不可访问的候选。
- `@laidbyshay` 已迁移至 `@shaywigmaster`，仅纳入当前主账号；`@hairbyebonyb`、`@jrbcollection` 等当前公开资料缺少足够的 wig 业务证据，未纳入。
- 搜不到或页面不可读不代表账号不存在；这些对象可作为后续人工复核候选，但不计入本次 40 个结果。

## 来源与限制

- 每条 Lead 的 Instagram URL 和辅助来源 URL 均保存在 Excel 的 `Source` 字段。
- Instagram 未登录公开页面可能限流或截断简介；本轮没有访问私人内容。
- Follower Count 是采集时点快照，会随时间变化；四舍五入显示保留原样。
- Website / Public Contact 只记录公开企业网站、预约链接、企业邮箱或公开电话；没有推测私人联系方式。
- 部分辅助文章或目录可能早于采集日，已用当日 Instagram 公开页确认账号存在，但业务与地址仍需人工复核。
- “Activity Signal”仅说明公开内容入口可见，不代表账号在指定时间窗口内活跃。

## 输出契约自检

- [x] 仅在 `outputs/` 更新 `lead-list.xlsx` 与 `discovery-notes.md`。
- [x] `input/` 未修改。
- [x] 第一批与第二批均为 Live 数据；未混入 Offline 教学数据。
- [x] 共 40 个唯一 Lead；第二批 20 个与第一批不重复。
- [x] 所有 Lead 均保留 Profile URL、来源、筛选理由、置信度和人工复核项。
- [x] 缺失字段未补造；无法确认的地点或属性标记为 unknown / 人工复核。
- [x] 关键结论包含采集时间、口径与限制。
- [x] 未将任何关注、私信、营销或人工决策描述为已完成动作。

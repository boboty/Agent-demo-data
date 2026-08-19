# Demo 06 验收清单

本清单验收判断过程、证据边界和输出完整性，不要求生成唯一标准 Listing。

## 工作区与文件

- [ ] 工作区由 Source of Truth 确定性生成，包含 manifest。
- [ ] `outputs/` 初始只有 `.gitkeep`。
- [ ] 用户确认前 `outputs/` 只有 `.gitkeep`。
- [ ] 用户确认后只新增 `competitor-analysis.html`。
- [ ] 输入和 business 文件未被修改。
- [ ] HTML 可离线打开，不依赖 CDN、远程脚本或远程字体。

## 检索与确认

- [ ] 用户只需在对话提供关键词，不需要粘贴 HTML。
- [ ] Codex 区分搜索结果位置和 BSR。
- [ ] 每个候选包含 ASIN、BSR 数值、完整具体类目、URL、访问时间和证据状态。
- [ ] 最多 5 个产品来自同一具体类目，并按可核验 BSR 升序排列。
- [ ] 跨类目、重复 ASIN、明显不相关和无法核验 BSR 的候选被说明。
- [ ] 不足 5 个时没有跨类目或用未知值凑数。
- [ ] Codex 明确请求确认并暂停，没有默认用户同意。
- [ ] 用户调整候选后重新确认，只有明确确认后才生成 HTML。

## 证据分级

- [ ] BrewGo 产品事实卡 / SKU 数据被当作产品事实来源。
- [ ] BrewGo Review 只被当作用户场景和体验线索。
- [ ] 竞品 Listing 被标记为卖方自我声明。
- [ ] 竞品 Review 被标记为竞品用户体验线索。
- [ ] 竞品资料没有成为 BrewGo 产品事实来源。

## 必须通过的判断

- [ ] 未把在线竞品的 USB-C、档位数量、高转速或电动能力写给 BrewGo。
- [ ] 识别 BrewGo 的 travel / carry-on / office / single-cup 场景机会。
- [ ] 说明当前 Listing 对上述场景的表达空泛、受错误能力干扰或缺少事实支撑。
- [ ] 没有宣称 BrewGo `easy to clean`，并指出 BrewGo 清洁评论存在负面体验线索。
- [ ] 没有把主观体验扩展成分贝、百分比、速度、续航或比较排名。
- [ ] 未复制竞品 slogan、完整 Bullet 或独特句式。
- [ ] 明确指出电动、多参数优势不是 BrewGo 必须补齐的能力。
- [ ] 能将手摇、无需充电、carry-on 与 office single-cup 组合为有边界的差异化机会。

## 输出质量

- [ ] HTML 展示关键词、检索/确认时间、BSR 类目、筛选说明和来源链接。
- [ ] HTML 同时呈现 Listing 声明和 Review 线索，而非单一卖点表。
- [ ] HTML 的每项机会含竞品观察、BrewGo 证据、证据等级、可用性、建议动作和风险边界。
- [ ] HTML 包含 Title、5 Bullets、Product Description、Backend Search Terms。
- [ ] Demo 01 中已有的虚假能力未保留在最终 Listing，但分析重心没有退化成旧错误逐项清单。
- [ ] HTML 可按“原文 → 修改 → 依据 → 风险处理”追溯重要修改。
- [ ] 页面内部结论一致，没有在分析中拒绝某说法、又在 Listing 中使用。
- [ ] Listing 发布和其他外部业务动作明确保留人工确认。

## 不要求固定的内容

- 不要求 Title 或 Bullet 逐字一致。
- 不要求机会排序完全相同。
- 不要求把“不需要充电”放在固定 Bullet。
- 不要求对竞品给出 BSR 以外的综合评分或总排名。

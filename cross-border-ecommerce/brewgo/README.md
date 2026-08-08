# BrewGo 公共课程资产

本目录是 BrewGo / G2 虚构跨境电商业务世界的 **Source of Truth**，同时维护工具无关的课堂任务。Data 定义业务和任务，具体智能体只是执行工具。

## 资产边界

- business/：店铺、产品事实、品牌规则、业务规则和字段字典。
- data/raw/：权威原始数据，禁止直接修改。
- data/expected/：与 raw 一致的恢复基线。
- classroom/：工具无关的任务说明、任务卡和项目上下文。
- adapters/：具体智能体工具的薄适配，不反向修改公共任务。
- workspaces/：由脚本生成的课堂运行目录，不是 Source of Truth。
- instructor/：教师运行手册和观察指引，不复制到学员工作区。
- docs/：数据设计、教学问题、验收与校验说明。
- scripts/validate_data.py：结构、公式缓存与跨表关系校验。
- scripts/build_classroom_workspaces.py：重建 Codex 三阶段课堂工作区。
- VERSION：数据资产版本。

**业务任务是公共资产，工具配置只是适配层。**

## 三个课堂阶段

1. classroom/01-direct-task：用自然的一句话交付 Listing 优化工作，只提供必要资料。
2. classroom/02-task-card：使用相同资料，增加目标、输入、约束、输出和验收清晰的任务卡。
3. classroom/03-project-context：保持任务卡不变，加入可长期复用的项目上下文。

classroom/04-data-analysis 和 classroom/05-validation 本轮仅建立边界占位，不扩展课程内容。

## 数据口径

orders.xlsx 是面向订单异常分析的非代表性样本，不是店铺全量订单；inventory.xlsx 的平均日销是独立运营口径；Amazon Ads 是聚合归因口径。三者可做 SKU、价格、日期与趋势检查，不用于总量对账或反推采样率。

## 验证

在本目录运行：

    python3 scripts/validate_data.py

校验会检查 raw/expected 一致性、文件可读性、字段、行数、SKU 引用、广告数学关系、订单金额、评论/工单重复、工单订单关系和日期边界。规范化重复 SKU 是登记过的教学问题，会作为 warning 输出。

## 重建 Codex 工作区

    python3 scripts/build_classroom_workspaces.py

脚本只读取 business、data、classroom、adapters 和 VERSION，安全清理并重建 workspaces/codex/01-direct-task、02-task-card、03-project-context。每个工作区均为无软链接的离线副本，并带有确定性的 workspace-manifest.json。

课堂使用时在 Codex App 中依次打开：

1. workspaces/codex/01-direct-task
2. workspaces/codex/02-task-card
3. workspaces/codex/03-project-context

前两个阶段不包含完整业务型 AGENTS.md；第三阶段才由 adapters/codex/AGENTS.md.template 注入完整项目规则，避免父目录规则提前污染实验。

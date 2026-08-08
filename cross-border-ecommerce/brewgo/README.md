# BrewGo Mock 数据资产

本目录是 BrewGo / G2 跨境电商仿真数据的 **Source of Truth**。它负责业务事实、原始数据、恢复基线、字段字典、教学坑、验收记录和数据完整性脚本，不承载课堂 Task、Skill、工具或自动化流程。

## 目录

- `business/`：店铺、产品事实、品牌规则、业务规则和字段字典
- `data/raw/`：权威原始数据，禁止直接修改
- `data/expected/`：与 raw 一致的课堂恢复基线
- `docs/`：设计、教学坑、验收与校验说明
- `scripts/validate_data.py`：结构、公式缓存与跨表关系校验
- `scripts/sync_brewgo_data.py`：向课堂 Demo 单向同步数据快照
- `VERSION`：数据资产版本

## 数据口径

`orders.xlsx` 是面向订单异常分析的非代表性样本，不是店铺全量订单；`inventory.xlsx` 的平均日销是独立运营口径；Amazon Ads 是聚合归因口径。三者可做 SKU、价格、日期与趋势检查，不用于总量对账或反推采样率。

## 验证

```bash
python3 scripts/validate_data.py
```

校验会检查 raw/expected 一致性、文件可读性、字段、行数、SKU 引用、广告数学关系、订单金额、评论/工单重复、工单订单关系和日期边界。规范化重复 SKU 是登记过的教学问题，会作为 warning 输出。

## 同步到课堂 Demo

默认同步业务规则、raw 和 expected 快照，但不修改 `data/work/` 或 `outputs/`：

```bash
python3 scripts/sync_brewgo_data.py
```

需要同时恢复课堂 work 时显式使用：

```bash
python3 scripts/sync_brewgo_data.py --reset
```

可通过 `--demo-root /path/to/Demo/brewgo-codex-course` 指定其他目标。同步后 Demo 内会生成 `data/brewgo_data_manifest.json`，记录版本和每个受管文件的 SHA-256。


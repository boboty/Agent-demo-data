# Agent Demo Data

用于课程 Demo 的独立模拟数据仓库。这里维护业务事实、权威原始数据、恢复基线、数据说明和校验脚本；课堂任务、工作副本、输出结果及运行工具由 [demo4bizcourse](https://github.com/boboty/demo4bizcourse) 单独维护。

将数据与 Demo 程序分开后，数据版本可以独立验收和更新，Demo 项目只接收经过校验的快照。

> 仓库中的客户、订单、评论和经营数据均为教学用途的虚构数据，不包含真实客户或个人信息。

## 当前数据集

| 场景 | 数据集 | 版本 | 说明 |
|---|---|---|---|
| 跨境电商 | [BrewGo / G2](cross-border-ecommerce/brewgo/) | [VERSION](cross-border-ecommerce/brewgo/VERSION) | Amazon 手摇咖啡研磨器业务仿真数据 |

BrewGo 数据集包含产品、Listing、广告搜索词、供应商报价、评论、客服、订单、库存和成本参数。详细的数据口径、字段关系及教学问题见 [数据集说明](cross-border-ecommerce/brewgo/README.md)。

## 仓库结构

```text
cross-border-ecommerce/
└── brewgo/
    ├── business/       # 店铺、产品、品牌和业务规则
    ├── data/
    │   ├── raw/        # 权威原始数据
    │   └── expected/   # 与 raw 一致的恢复基线
    ├── docs/           # 设计、验收、教学问题和校验说明
    ├── scripts/        # 数据校验与 Demo 同步脚本
    ├── README.md
    └── VERSION
```

本仓库不保存 Demo 的 `data/work/`、`outputs/`、课堂 Task、Skill 或自动化配置。

## 快速验证

校验脚本仅依赖 Python 3 标准库。在仓库根目录运行：

```bash
python3 cross-border-ecommerce/brewgo/scripts/validate_data.py
```

校验覆盖文件完整性、`raw/expected` 一致性、表结构、公式缓存、SKU 引用、跨表关系和日期边界。已登记的教学问题会以 warning 输出，不视为校验失败。

## 同步到 Demo

数据验收通过后，在 BrewGo 数据集目录运行同步脚本，并显式指定本地 Demo 项目路径：

```bash
cd cross-border-ecommerce/brewgo
python3 scripts/sync_brewgo_data.py \
  --demo-root /path/to/demo4bizcourse/brewgo-codex-course
```

默认只同步 `business/`、`data/raw/`、`data/expected/`，并生成带版本号和 SHA-256 的 manifest；不会修改 Demo 的 `data/work/` 和 `outputs/`。

只有需要同时恢复课堂工作副本时才使用：

```bash
python3 scripts/sync_brewgo_data.py \
  --demo-root /path/to/demo4bizcourse/brewgo-codex-course \
  --reset
```

`--reset` 会用 `data/expected/` 替换 Demo 的 `data/work/`，执行前请确认其中没有需要保留的课堂修改。

## 维护约定

1. 业务事实、数据文件和字段说明应同步更新，避免只改数据不改口径。
2. `data/raw/` 与 `data/expected/` 必须保持逐文件一致。
3. 数据变更后更新 `VERSION`，并运行校验脚本。
4. 校验通过后再同步到 Demo；Demo 中的快照不作为反向修改数据源。
5. 有意保留的数据质量问题应记录在 `docs/planted_issues.md`，未登记的问题按缺陷处理。

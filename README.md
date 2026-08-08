# Agent Demo Data

本仓库维护可供多种 AI 智能体共同使用的虚构业务世界、事实数据、课堂任务和实验材料。Codex、WorkBuddy、Kimi Work 或其他工具都只是这些公共资产的执行入口。

> 仓库中的客户、订单、评论和经营数据均为教学用途的虚构数据，不包含真实客户或个人信息。

## 当前数据集

| 场景 | 数据集 | 版本 | 说明 |
|---|---|---|---|
| 跨境电商 | [BrewGo / G2](cross-border-ecommerce/brewgo/) | [VERSION](cross-border-ecommerce/brewgo/VERSION) | Amazon 手摇咖啡研磨器业务仿真数据与课堂实验 |

## 三层资产边界

### Business / Data

business 定义业务世界、产品事实、品牌和业务规则；data 保存权威原始数据与恢复基线。两者共同构成事实层。

### Classroom

classroom 定义工具无关的课堂任务、输入范围、任务卡、项目上下文和验收方式。核心任务不假定学员使用哪一种智能体。

### Adapters / Workspaces

adapters 只维护具体工具所需的薄适配；workspaces 是由公共资产生成、可以直接打开的课堂目录，不是新的 Source of Truth。

**业务任务是公共资产，工具配置只是适配层。**

## 仓库结构

    cross-border-ecommerce/
    └── brewgo/
        ├── business/       # 业务世界与规则
        ├── data/           # raw 权威数据与 expected 恢复基线
        ├── classroom/      # 工具无关的课堂阶段
        ├── adapters/       # 各智能体工具的薄适配
        ├── workspaces/     # 可重建的课堂运行目录
        ├── instructor/     # 教师手册，不进入学员工作区
        ├── docs/           # 数据设计、教学问题和验收记录
        ├── scripts/        # 数据校验与工作区生成脚本
        ├── README.md
        └── VERSION

## 快速验证与生成

在仓库根目录运行：

    python3 cross-border-ecommerce/brewgo/scripts/validate_data.py
    python3 cross-border-ecommerce/brewgo/scripts/build_classroom_workspaces.py

校验脚本覆盖文件完整性、raw/expected 一致性、表结构、公式缓存、SKU 引用、跨表关系和日期边界。生成脚本会从 business、data、classroom 和 adapters 重建 Codex 三阶段工作区，并写入数据版本清单。

## 维护约定

1. 业务事实、数据文件和字段说明应同步更新，避免只改数据不改口径。
2. data/raw 与 data/expected 必须保持逐文件一致。
3. 数据变更后更新 VERSION，并运行校验脚本。
4. classroom 不写入特定工具配置；工具差异只放在 adapters 和生成后的 workspaces。
5. workspaces 可以随时重建，不应反向成为业务或任务定义的数据源。
6. 有意保留的数据质量问题记录在 docs/planted_issues.md，未登记的问题按缺陷处理。

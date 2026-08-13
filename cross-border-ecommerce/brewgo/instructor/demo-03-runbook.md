# Demo 03 运行手册：Project Context

## 为什么引入项目上下文

Demo 02 证明任务卡能提高一次性交付质量，但品牌事实、业务边界、数据规则和人工确认原则不应由每位业务人员每次重写。第三阶段把这些稳定信息提升为项目上下文。

## 打开目录

新开或切换到 workspaces/codex/03-project-context。该工作区只有：

- AGENTS.md
- project-context.md
- business/
- input/
- outputs/

**没有 Task Card。**

## 回到一句话

课堂重新回到和 Demo 01 完全相同的一句话：

> 帮我优化一下这个 Listing。

## 长期内容去了哪里

Demo 02 中每次都要重复说明的长期内容，已经进入 Project Context / AGENTS / business 环境：

- 事实在哪里；
- 哪些资料有什么证据资格；
- 原始资料如何处理；
- 外部动作权限边界；
- 长期业务规则；
- 输出与自检原则。

## AGENTS.md 何时出现

完整业务型 AGENTS.md 只在第三阶段工作目录出现。它由 Codex adapter 生成，用于告诉 Codex 先读哪些公共文件、结果写到哪里以及如何自检；公共业务规则仍来自 business 与 project-context。

## 执行与比较

让智能体执行那一句话，比较：

- 是否更稳定地读取产品事实、品牌规则和业务规则。
- 是否主动处理绝对化表达和高风险动作边界。
- 是否更一致地保留事实依据、证据状态和人工确认项。
- 是否把长期规则与本次具体交付分开。
- 即使换一个任务，哪些项目规则仍可复用。

## 教学结论

不要写成"Demo 03 比 Demo 02 生成的 Listing 一定明显更好"。

应该写：

**Task Card 管这一次任务；Project Context 管以后在这里默认怎么工作。**

以及：

**Demo 01 和 Demo 03 都只有一句话，但 Demo 03 的一句话背后已经站着一个长期项目环境。**

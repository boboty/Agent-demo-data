# BrewGo Codex Skills｜课堂安装包

本包包含 8 个离线跨境电商 Skills 与对应演示数据。它们不依赖 API Key、MCP 或联网搜索。

## 安装

### macOS

双击 `install-mac.command`，或在终端运行：

```bash
./install-mac.command
```

### Windows

双击 `install-windows.bat`，或从命令提示符运行它。

安装脚本使用当前 OpenAI Codex 文档列出的用户级目录：

- macOS / Linux：`$HOME/.agents/skills`
- Windows：`%USERPROFILE%\.agents\skills`

如果同名 Skill 已存在，脚本会先列出冲突并询问；确认后把旧目录重命名为带时间戳的备份，不会静默覆盖，也不会修改其他 Skill。

## 检查安装

1. 打开 Codex 的 Skills 列表，或在 Codex CLI / IDE 中运行 `/skills`。
2. 确认以下 8 个名字可见：
   - `amazon-review-insights`
   - `amazon-return-reduction`
   - `amazon-inventory-watch`
   - `amazon-listing-localizer`
   - `amazon-a-plus-planner`
   - `supplier-quote-compare`
   - `customer-service-triage`
   - `business-file-organizer`
3. Codex 通常会自动发现新安装的 Skill；如果未出现，重启 Codex。

## 课堂演示

每项资料位于 `demo-data/<skill-name>/`。打开该目录作为工作区，新建任务，只发送 `DEMO_PROMPT.md` 中的一句话。若隐式触发不稳定，用 `$skill-name` 加同一句话显式调用。

所有结果必须写入该 demo 的 `outputs/`，不要覆盖 `input/`。`EXPECTED.md` 只提供关键验收点，不包含完整标准答案。

卸载方法见 [UNINSTALL.md](UNINSTALL.md)。开源研究与许可证见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。


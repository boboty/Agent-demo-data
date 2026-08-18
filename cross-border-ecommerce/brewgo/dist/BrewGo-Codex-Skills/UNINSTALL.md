# 卸载 BrewGo Codex Skills

用户级安装目录是 `$HOME/.agents/skills`（Windows 为 `%USERPROFILE%\.agents\skills`）。只删除以下 8 个目录即可卸载：

```text
amazon-review-insights
amazon-return-reduction
amazon-inventory-watch
amazon-listing-localizer
amazon-a-plus-planner
supplier-quote-compare
customer-service-triage
business-file-organizer
```

不要删除整个 `.agents/skills` 目录，因为其中可能有其他 Skills。安装时若产生了 `.backup-YYYYMMDD-HHMMSS` 目录，它们是安装前的同名版本；确认不再需要后再单独删除，或改回原名称恢复。

Codex 通常自动检测变化；列表未刷新时重启 Codex。


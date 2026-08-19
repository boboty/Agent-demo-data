# Lead schema and quality rules

Read this reference before creating or appending a lead workbook.

## Workbook fields

Use these Chinese columns in this order:

1. `账号`
2. `显示名称`
3. `Instagram 主页`
4. `所在地`
5. `账号类型`
6. `简介摘要`
7. `网站 / 公开联系方式`
8. `粉丝数`
9. `内容可见性信号`
10. `入选理由`
11. `风险 / 排除理由`
12. `来源`
13. `置信度`
14. `人工复核`

Recommended account types:

- `美发沙龙`
- `独立发型师`
- `假发店`
- `美妆用品店`
- `假发品牌 / 电商`
- `假发工作室`
- `替代发 / 医疗发片服务`
- a truthful combined label when the business is genuinely mixed

## JSON input shape

The workbook script accepts a JSON array. Every object must contain all keys below; use an empty string for a genuinely missing value rather than inventing one.

```json
[
  {
    "account": "@examplewigs",
    "display_name": "Example Wigs",
    "profile_url": "https://www.instagram.com/examplewigs/",
    "location": "London, UK",
    "category": "假发沙龙 / 假发店",
    "bio_summary": "定制假发、试戴、修剪和维修。",
    "public_contact": "https://example.com/ | hello@example.com",
    "follower_count": "1.2万（平台显示）",
    "activity_signal": "公开主页及内容网格可见；未核验最近发布日期",
    "why_matched": "当前简介明确写 custom wigs，官网支持 London 实体服务。",
    "risk": "联系前确认当前地址和营业状态。",
    "source": [
      "https://www.instagram.com/examplewigs/",
      "https://example.com/"
    ],
    "confidence": "高",
    "manual_review": "需要 — 核验近期活跃与合作意愿"
  }
]
```

`source` may be a list of URLs or a newline-delimited string. `confidence` must be `高`, `中`, or `低`.

## Inclusion test

Count a lead only when all applicable checks pass:

- the Instagram profile is publicly accessible at collection time;
- the handle is not already present in the target workbook;
- public text explicitly supports a wig-related product or service;
- geography is explicit when geography is required;
- the source field includes the Instagram profile and, where available, corroborating evidence;
- uncertainties are recorded as risks rather than silently resolved.

Do not count inaccessible candidates merely to reach a quota. A migrated account may be included only through its current relevant successor, with the migration recorded in sources or risk.

## Evidence and wording

Summarize bios; do not copy long passages. Keep public business emails, phone numbers, websites, and booking links only when visibly published. Do not guess an email pattern or reconstruct a hidden phone number.

Use `unknown` or an empty string when a field is missing. Do not infer city from an area code, photographs, content style, or audience location.

The activity field must distinguish these signals:

- `公开内容入口可见` means only that posts/Reels/Highlights were visible;
- `最近可见发布日期：YYYY-MM-DD` may be used only when directly observed;
- never call an account “active” solely because its grid loaded.

## Notes requirements

`discovery-notes.md` should state:

- resolved scope and intended use;
- create versus append mode;
- Live or Offline data source;
- collection and analysis time with timezone;
- requested, included, excluded, and unique counts;
- category and geography rules;
- rejected examples and why;
- missing data and source limitations;
- manual-review priorities;
- confirmation that no follow, DM, posting, purchase, pricing, or bulk-marketing action occurred.

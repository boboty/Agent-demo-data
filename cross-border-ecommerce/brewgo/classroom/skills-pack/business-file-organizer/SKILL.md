---
name: business-file-organizer
description: "Safely organize a supplied cross-border business project folder by copying files into consistent categories, renaming copies, and producing a traceable index. Use for 文件整理、项目资料归档、Downloads cleanup; never delete or overwrite originals, and route ambiguity to NEEDS_REVIEW."
---

# Business File Organizer

Organise copies only. Original files are immutable evidence.

## Workflow

1. Treat `input/` as the source folder when present. Inventory every file with size, extension, readable metadata/content signal, and duplicate-name/version clues.
2. Propose a compact category and naming plan before copying. Typical categories may include Listings, Product, Images, Suppliers, Finance, Logistics, Reviews, Advertising, Meetings, Customers, and `NEEDS_REVIEW`; use only categories supported by the actual files.
3. Copy every source file into `outputs/organized/<category>/` with a consistent, collision-safe name. Preserve extensions and separate versions; never decide which “final” file supersedes another without evidence.
4. Put files with insufficient or conflicting evidence into `outputs/organized/NEEDS_REVIEW/`. Keep their original names when a reliable new name is unavailable and state the confirmation question.
5. Write `outputs/file-index.xlsx` or `outputs/file-index.csv` with original name/path, new name/path, category, evidence, version note, status, and confirmation question. Also write a short `outputs/organization-plan.md`.
6. Verify source file count and hashes or sizes are unchanged, and that every source has exactly one copied destination entry.

Do not delete, move, rename, overwrite, merge, or edit any source file. Never classify from extension alone when readable content contradicts the filename.

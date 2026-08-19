---
name: instagram-lead-discovery
description: Discover and verify public Instagram leads for wig salons, wig stylists, wig stores, alternative-hair providers, and related brands, then create or append a reviewable Chinese lead workbook. Use when a user asks to search Instagram for wig/hair businesses or expand an existing lead list. Do not use for influencer outreach, private-account access, automated following, DMs, or bulk marketing.
---

# Instagram Lead Discovery

Turn a vague request such as “search Instagram for wig salons” into a sourced, deduplicated lead list that a human can review.

## Define the assignment before research

Confirm any missing choice that would change scope or acceptance:

- geography: country, region, or city;
- included business types: salon, independent stylist, wig store, beauty supply, brand/e-commerce, or all;
- purpose: market observation, lead development, or both;
- target count;
- exclusions;
- Live public data or an explicitly supplied offline teaching dataset;
- create a new list or append to an existing list;
- output language.

Restate the resolved assignment before collecting data. Preserve the user's choices instead of silently narrowing “all” to salon-only or broadening a city to a country.

## Respect local contracts and boundaries

Read applicable `AGENTS.md`, task README, raw-request file, and output contract before acting. Keep input snapshots read-only and write only to the authorized output location.

Only use public information. Do not follow, like, DM, post, purchase, change prices, submit contact forms, or perform bulk marketing unless the user separately authorizes that exact action. Never infer private contact details.

## Research in Live mode

Use public search results to discover candidates, then verify every included handle on its current public Instagram profile. A supporting website or directory alone does not prove that the Instagram account is currently accessible.

For each included lead:

1. Confirm the profile URL resolves to the intended public account.
2. Record the account's current display name, public bio, follower display, and visible content signal.
3. Corroborate business type and geography with the account's website, booking page, official directory, or credible public business listing when possible.
4. Preserve both the Instagram URL and supporting source URL.
5. Reject or hold for manual review when the account is inaccessible, private, migrated without a relevant successor, irrelevant, or lacks explicit wig-related evidence.

Do not treat a visible post grid or Highlights as proof of recent activity. Record a latest-post date only when it is actually visible and attributable. Preserve rounded platform displays such as `1.2万` or `12K`; do not turn them into false precision.

Location must come from explicit public text. Do not infer it from photos, telephone area codes, visual style, language, or hashtags. When sources disagree, keep the conflict in the risk field and require manual review.

If Live access is blocked and the user required real data, report the limitation rather than switching to teaching data. Use offline data only when the user permits it, and label it clearly as offline or fictional.

## Select and classify leads

Use the taxonomy and field definitions in [references/schema-and-quality.md](references/schema-and-quality.md). Read that reference before creating or appending the workbook.

Favor direct wig evidence: wigs, custom wigs, wig fitting, installation, styling, cutting, coloring, repair, toppers, cranial prostheses, medical hair replacement, or wig-specific products. General hair salons require explicit wig evidence from a current public source.

Confidence reflects evidence quality, not business quality:

- high: current Instagram profile plus an official site or strong public business source;
- medium: current profile is relevant but location, store status, or service emphasis needs review;
- low: do not normally count toward the requested total; place in a review queue instead.

## Create or append the workbook

Use Chinese field names by default when the user works in Chinese. Keep handles, URLs, brand names, and source wording in their original form when translation could distort identity.

Before appending, inspect the existing workbook and canonicalize handles by trimming whitespace, removing a leading `@`, and comparing case-insensitively. The final count means unique accounts, not spreadsheet rows.

The bundled script creates or appends the standard workbook:

```bash
python scripts/build_lead_workbook.py --input leads.json --output lead-list.xlsx
python scripts/build_lead_workbook.py --input new-leads.json --output lead-list.xlsx --append
```

The script requires `openpyxl`. It validates the JSON schema, rejects duplicate handles, adds a separate sheet for the newest batch, and verifies the saved workbook. Read [references/schema-and-quality.md](references/schema-and-quality.md) for the JSON shape.

Also create or update `discovery-notes.md` with the final assignment, Live/Offline mode, collection time and timezone, search and exclusion rules, counts, source limitations, missing fields, rejected examples, manual-review items, and action boundary.

## Verify delivery

Before handing off:

- confirm the workbook opens and contains the promised number of unique accounts;
- confirm the table range includes every data row and no rows are hidden;
- confirm the newest batch equals the promised append count and has no overlap with earlier batches;
- confirm the workbook and notes agree on counts and collection times;
- confirm input files were not changed.

When replacing a same-named workbook, an already-open or previously downloaded copy may appear stale. Report the verified row count and ask the user to close the old copy and reopen the delivered file. If useful, keep a clearly named newest-batch sheet inside the same workbook rather than creating an unauthorized extra deliverable.

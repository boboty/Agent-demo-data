# Amazon Competitor Discovery — Research Notes

## Task definition

- Data mode: **Amazon Live** (no Offline fallback used)
- Marketplace: Amazon US (`amazon.com`)
- Search keyword: `plush figures`
- Candidate pool: the first 3 Amazon search-result pages using the default “Featured” ordering
- Collection snapshot: `2026-08-19T06:55:00+08:00` (Asia/Shanghai)
- Sponsored treatment: Sponsored placements were excluded. If an ASIN also appeared in an Organic placement, its Organic placement remained eligible.
- Duplicate/variant treatment: duplicate ASINs were removed. The visible product pages did not expose variant links among the selected Top 10, so materially different titles/packs with distinct ASINs were retained as separate listings.
- Availability treatment: candidates visibly offered in search results were retained unless the detail page explicitly stated that the item was currently unavailable. A restriction for the browser-selected Taiwan delivery destination was not treated as proof of US-market unavailability.

## Top 10 definition

Top 10 means the ten eligible Organic listings with the lowest visible **primary Best Sellers Rank (BSR)** within the comparable main category `Toys & Games` across the confirmed three-page candidate pool. Chinese `玩具和游戏` and English `Toys & Games` labels were normalized to the same category. Products whose primary BSR belonged to another category were not compared with Toys & Games products.

BSR ties were ordered by the original search result page and then the position on that page. Search position was not interpreted as sales. BSR is a relative category rank at the time of collection; it is not unit sales or revenue.

## Candidate audit

- Search result cards inspected: **168**
- Unique eligible Organic ASINs after availability filtering and deduplication: **141**
- Duplicate Organic ASIN occurrences removed: **3**
- Detail pages with visible BSR evidence: **137**
- Comparable primary BSRs in `Toys & Games`: **132**
- Cross-category primary BSRs excluded: **5**
- Missing or unparseable primary BSRs excluded: **4**

## Fields and sources

- Search-result pages supplied search page/position, Organic status, visible price, rating, review count, promotional wording, and result availability.
- Canonical product detail pages supplied ASIN confirmation, brand, canonical title, specifications, availability evidence, and the full visible BSR string.
- Product, search-result, and detail-page source links are preserved per row in `amazon-top10.xlsx`.
- Amazon displayed prices in **TWD** and delivery estimates for the browser-selected Taiwan destination even though the marketplace was Amazon US. These values were preserved as displayed and were not converted or inferred as US domestic prices.
- Missing fields are written as `unknown` or explained in `Missing / Review Note`; no values were fabricated.

## Access and data limitations

- Amazon pages are dynamic, localized, and can change by time, account, delivery destination, inventory, and experimentation. Re-running the same query may yield different products, order, prices, offers, or BSRs.
- Several detail pages did not show a direct buy-box price or delivery text; the visible search-result value was retained where available.
- “No visible Prime indicator” means only that no Prime badge was confirmed in the captured page state; it does not prove that no Prime offer exists for another location or account.
- ASIN deduplication and visible variation checks cannot guarantee that Amazon has no hidden parent-child catalog relationship between distinct listings.

## Human review items

1. Re-check BSR immediately before a commercial decision because BSR changes frequently.
2. Set a US delivery ZIP code and verify USD price, Prime status, stock, and domestic delivery terms.
3. Manually review the four Bluey listings tied at primary BSR 346 to determine whether the business wants to treat them as one franchise/family despite their distinct titles, packs, and ASINs.
4. Confirm any coupon at checkout; a visible coupon can be account-, time-, or offer-specific.

## What this result does not represent

This is not an estimate of unit sales, revenue, market share, profitability, or the ten best-selling products across all Amazon. It is a time-bounded comparison of eligible listings found in the first three result pages for one keyword, using comparable visible primary-category BSR evidence.

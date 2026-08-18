---
name: amazon-review-insights
description: "Analyze supplied Amazon review CSV/XLSX files into evidence-backed customer voice themes, pain points, use cases, misunderstandings, and contradictions. Use for 评论分析、客户声音、review insights; do not use for full Listing optimization, live review scraping, keyword research, or competitor ranking."
---

# Amazon Review Insights

Use only the review files supplied by the user or found in the current workspace. Work offline unless the user explicitly asks for outside research.

## Workflow

1. Locate review files, preferring `input/` when present. Inspect columns, row count, rating range, dates, variants, blanks, and duplicate review IDs before interpreting themes.
2. Treat each unique review as one observation. Group recurring evidence into: strengths, pain points, use cases, purchase motivations, product issues, packaging/logistics issues, and likely capability or usage misunderstandings.
3. Count theme mentions from the supplied sample. Separate frequency from severity and label thin evidence, conflicting reviews, variant-specific patterns, and uncertain classification.
4. Use short representative excerpts with `review_id`; do not let one or two reviews become a population claim. Reviews describe experiences, not verified product facts or root causes.
5. Create `outputs/review-insights.md` and `outputs/review-themes.xlsx`. Create `outputs/` if needed, but never modify input files.

## Output contract

`review-insights.md` should state sample size and rating distribution, then summarize high-frequency strengths and pain points, use scenarios, purchase motivations, issue priorities, misunderstanding candidates, representative evidence, contradictions, and data limits.

`review-themes.xlsx` should contain a theme summary with category, theme, mention count, share of unique reviews, rating signal, affected variants, representative review IDs, evidence note, confidence, and human-confirmation flag. A second evidence sheet may map individual reviews to themes.

Do not draft or optimize a complete Listing. Phrase recommended actions as hypotheses to verify, not as established product facts.

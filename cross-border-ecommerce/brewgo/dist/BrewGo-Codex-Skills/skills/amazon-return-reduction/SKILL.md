---
name: amazon-return-reduction
description: "Analyze supplied Amazon return records, classify root-cause signals, quantify recurring reasons by SKU, and propose reviewable return-reduction actions. Use for 退货原因、return analysis、降低退货; not for refund approval, live Amazon access, or full Listing optimization."
---

# Amazon Return Reduction

Analyze only the supplied return dataset. Return comments are customer-reported signals, not proven technical root causes.

## Workflow

1. Prefer files in `input/`; validate required fields, row count, blanks, duplicate order IDs, amounts, SKUs, dates, and fulfillment channels.
2. Assign one primary category per record: product issue; Listing/expectation gap; packaging/logistics; usage education; customer preference; or insufficient data. Add a secondary signal only when the comment supports it.
3. Count records and refund amounts by category and SKU. Preserve ambiguous cases in insufficient data instead of forcing a cause.
4. Select representative order IDs and short comment evidence. Distinguish occurrence count from severity and avoid claiming causality from repeated wording alone.
5. Propose prioritized actions tied to evidence: product investigation, expectation clarification, packaging review, usage guidance, or data collection. Mark owner/feasibility assumptions for human confirmation.
6. Write `outputs/return-analysis.xlsx` and `outputs/return-actions.md`; never change input files.

## Output contract

The workbook should include a record-level classification sheet and a category/SKU summary with counts, refund totals, evidence IDs, confidence, and human-review flags. The Markdown report should explain top patterns, actions, unknowns, and which conclusions need operational confirmation.

Do not approve refunds, promise compensation, infer a defect from one comment, or rewrite a complete Listing.

---
name: supplier-quote-compare
description: "Compare multiple supplied supplier quote spreadsheets across price, currency, MOQ, lead time, fees, payment, Incoterms, validity, and missing fields. Use for 供应商报价比较、采购比价、quote risk; never choose a supplier for the user or invent exchange rates."
---

# Supplier Quote Compare

Build a decision-ready fact comparison while leaving the supplier decision to the user.

## Workflow

1. Prefer quote files in `input/`. Inspect sheets, headers, SKUs, currencies, dates, fees, notes, and missing values. Determine the comparison date from supplied data when available.
2. Align rows by SKU and supplier rather than row number. Preserve original currencies; only convert when an explicit exchange rate and date are supplied.
3. Surface unit price, MOQ, lead time, packaging/tooling fees, payment terms, shipping term, validity, and notes. Parse fees disclosed only in notes, but mark the extraction and request confirmation.
4. Calculate comparable totals only within the same currency and clearly state included/excluded cost components. Missing quotes remain missing, never zero.
5. Describe each supplier's factual advantages, risks, and open questions. Highlight expiring quotes, high MOQ, long lead time, cash-unfavourable terms, cross-currency incomparability, and missing fields.
6. Write `outputs/supplier-comparison.xlsx` and `outputs/supplier-risk-summary.md`; leave source workbooks unchanged.

## Output contract

The workbook should include aligned SKU comparison, fee/term detail, risk flags, and a missing-data sheet. The summary should present facts, advantages, risks, confirmation questions, and decision criteria—not a winner or final selection.

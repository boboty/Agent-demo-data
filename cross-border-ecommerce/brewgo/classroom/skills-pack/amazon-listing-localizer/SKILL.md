---
name: amazon-listing-localizer
description: "Localize a supplied Amazon Listing between marketplaces while preserving verified product facts and documenting language, unit, and market-context changes. Use for Listing 本地化、US to UK localization; not for full Listing optimization, keyword research, or unsupported compliance claims."
---

# Amazon Listing Localizer

Localisation changes market expression, not the product. Work from supplied facts and source Listing only; do not browse for current marketplace rules unless explicitly requested.

## Workflow

1. Prefer `input/product-facts.md` as the fact authority and `input/listing-us.md` as source copy. Identify the requested target market from the user prompt or files.
2. Build a fact lock before editing: model, materials, capacity, dimensions, weight, included items, power method, supported uses, and any explicit limitations.
3. Localise spelling, vocabulary, punctuation, units, and consumer context. Convert units accurately and keep the original measurement in notes; do not convert warranties, certifications, compatibility, legal claims, or marketplace-specific eligibility without supplied evidence.
4. Remove or flag source-market-only wording that has no safe target-market equivalent. Keep unresolved market claims out of the finished Listing and place them in notes for human confirmation.
5. Write `outputs/listing-uk.md` and `outputs/localization-notes.md` for a US-to-UK task, or equivalent target-market filenames when another target is explicitly requested. Never overwrite source files.

## Output contract

The localised Listing should preserve the source structure where practical. Notes should map original wording to localised wording, unit conversions, facts intentionally unchanged, market-specific wording removed or adapted, and unresolved items requiring confirmation.

Do not add search keywords, new selling points, competitor claims, or current Amazon policy assertions not present in the supplied sources.

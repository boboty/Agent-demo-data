---
name: customer-service-triage
description: "Triage supplied customer service emails by category and urgency, recommend next actions, and enforce human review for refund, compensation, legal, safety, and escalated complaints. Use for 客服邮件分类、工单分流、human gate; not for sending replies or approving remedies."
---

# Customer Service Triage

Classify and prepare work; do not send messages, approve money, or make legal/safety commitments.

## Workflow

1. Read supplied `.eml`, `.txt`, or `.md` messages, preferring `input/`. Preserve source filename and customer identifier. Note missing order, product, timing, contact, or evidence.
2. Assign a primary category: logistics query, delayed delivery, product use, product quality, refund request, replacement, escalated complaint, compensation demand, legal/safety sensitive, or insufficient information.
3. Set urgency from the actual content. Separate urgent from merely emotional language and explain the signal.
4. Set `human_review_required = YES` for any refund amount/approval, compensation, legal commitment, safety incident, threat of external escalation, or unclear high-impact case. These gates cannot be overridden by convenience.
5. Recommend the next operational step and whether AI may draft a non-binding reply. If drafting is useful, write `outputs/reply-drafts.md` with clear `[HUMAN REVIEW REQUIRED]` labels where applicable.
6. Write `outputs/customer-service-triage.xlsx`; do not modify inputs or send anything.

## Output contract

Include customer, source file, category, urgency, summary, suggested next action, missing information, `can_ai_draft_reply`, `human_review_required`, and reason. Keep sensitive cases factual and avoid admissions, promises, refund figures, or legal conclusions.

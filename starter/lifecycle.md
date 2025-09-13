# Lifecycle — Actions and Cadence

One‑time setup:
- Name and wrapper: choose Trust + Pty trustee or CLG; obtain ACN/ABN/TFN
- Bank: open account; set two signatories; no single‑user transfers
- Seed reserve: record founder gift to cover 3–5 years of fees (state/contributions.csv)
- Adopt rules: mission, non‑distribution, payments, ownership assignment, investment threshold
- Board resolution: adopt reserve + 2m threshold (templates/board-reserve-threshold.md)

Recurring (timers):
- Weekly: link check on government forms (CI)
- Monthly: reconcile bank vs ledgers; board summary of income/expenses
- Quarterly: review ledger integrity; check ABN/ASIC records match state
- Annually: pay ASIC/registrations; reset reserve target; policy review

Event‑driven:
- Start a company: follow checklists/new-entity.md; issue equity directly to the fund
- Ownership assignment: if acquired personally, assign via ownership_assignment.md and log to state/holdings.csv
- Incoming dividends: log in state/income.csv; refill reserve then accumulate towards 2m
- Proposed investment: check corpus against rules/investment_threshold.md before any deployment

Ledgers and evidence:
- Ledgers live in starter/state/*.csv; changes via PR with a second reviewer
- Store receipts/contracts and regulator confirmations privately (encrypted), referenced by filename in notes

Status verification:
- Keep registry IDs (ABN/ACN) in ops/government-ids.md; monthly manual verification against registers
- Retain PDFs/receipts of lodgements; note dates in ops/status-verification.md

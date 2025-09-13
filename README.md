# <<FUND_NAME>> — Mission-Locked, Perpetual Innovation Fund (All-in-One Starter)

This repo is a **one-stop source of truth** for a perpetual, non-extractive fund: all returns are **reinvested** into innovation.
Public handbook (MkDocs) + internal-only area + policies-as-code + CI guardrails.

> ⚠️ **Not legal or financial advice.** Use as working templates; finalize with qualified AU counsel and an accountant.

## Quickstart
1. **Search/replace** `<<FUND_NAME>>` and other `<<PLACEHOLDER>>` fields.
2. Decide wrapper: **Trust + corporate trustee Pty Ltd** (lean) **or** **CLG** (public-facing). See `LEGAL/` and `POLICIES/governance/`.
3. Keep sensitive files in `/INTERNAL`. Public site builds from `/docs` (mirrors `/POLICIES` on publish).
4. Push to GitHub. Enable Pages (GitHub Actions). Protect `main` branch.
5. Use Issue templates for board agendas, IC memos, resolutions.
6. Before onboarding **any outside capital**, read `COMPLIANCE/MIS_AFSL_Boundary_Note.md` and get advice.
7. (Optional) Consider ACNC path later; see `COMPLIANCE/ACNC_Option_Note.md`.
8. Follow `docs/setup.md` for a chronological setup covering ASIC, banking, Stripe and GitHub.

## Layout
- `/docs` – public handbook (GitHub Pages)
- `/POLICIES` – **authoritative** policy sources (mirrored to `/docs/policies` on release)
- `/LEGAL` – skeleton legal docs (trust deed/CLG constitution + mission-lock clauses)
- `/GOVERNANCE` – ops guides; authoritative versions live in `/POLICIES`
- `/OPERATIONS` – resolutions, minutes, registers
- `/INVESTMENTS` – deal templates, side letters, related-party checklist
- `/COMPLIANCE` – ASIC/ATO checklists, MIS/AFSL note, ACNC note, calendar
- `/RISK` – risk register & skills matrix
- `/INTERNAL` – confidential (never published); use encryption for highly sensitive docs

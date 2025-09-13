# beforechicken — Mission-Locked, Perpetual Innovation Fund (All-in-One Starter)

This repo is a minimal starter for a perpetual, non-extractive fund: all returns are **reinvested** into innovation. Keep it private until you choose to publish anything.

> ⚠️ **Not legal or financial advice.** Use as working templates; finalize with qualified AU counsel and an accountant.

## Quickstart
1. Use `starter/` only. Copy it into a new private repo and work from there.
2. Decide wrapper: Trust + corporate trustee Pty Ltd (lean) or CLG (public‑facing). Brief counsel.
3. Set bank with two signatories; seed the operating reserve (see `starter/rules/financials.md`).
4. Record state in CSVs under `starter/state/`; store receipts/contracts privately (encrypted).
5. Run the on‑demand "Corpus Check" workflow or `python starter/scripts/corpus.py` before any investment.

## Layout
- `/starter` – minimal seed (state, rules, compliance links, templates)
- `/scripts/lychee.toml` – link checker config
- `/.github/workflows/linkcheck.yml` – weekly link checks for forms/URLs
- `/.github/workflows/corpus.yml` – on‑demand corpus gate check

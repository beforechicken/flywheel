#!/usr/bin/env python3
import csv, pathlib, sys, decimal

BASE = pathlib.Path(__file__).resolve().parents[1] / 'state'

def sum_csv(path, col='amount'):
    total = decimal.Decimal('0')
    if not path.exists():
        return total
    with path.open(newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                total += decimal.Decimal(str(row[col]).replace(',', '').strip())
            except Exception:
                pass
    return total

def main():
    contributions = sum_csv(BASE / 'contributions.csv')
    income = sum_csv(BASE / 'income.csv')
    expenses = sum_csv(BASE / 'expenses.csv')
    deployments = sum_csv(BASE / 'deployments.csv')
    corpus = contributions + income - expenses - deployments
    threshold = decimal.Decimal('2000000')
    print(f"Contributions: {contributions}")
    print(f"Income:        {income}")
    print(f"Expenses:      {expenses}")
    print(f"Deployments:   {deployments}")
    print(f"Corpus:        {corpus}")
    ok = corpus >= threshold
    print(f"Meets 2,000,000 threshold: {'YES' if ok else 'NO'}")
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main()

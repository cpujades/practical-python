# report.py
#
# Exercise 2.7

import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = dict(zip(headers, row))
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    stocks = {}

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                stocks[row[0]] = float(row[1])

    return stocks


def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        name = holding["name"]
        shares = int(holding["shares"])
        price = float(holding["price"])
        current_price = prices[name]
        change = current_price - price
        report.append((name, shares, current_price, change))
    return report


portfolio = read_portfolio("Data/portfoliodate.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)

headers = "      Name     Shares      Price     Change"
divider = "---------- ---------- ---------- ----------"
print(f"\n{headers}\n{divider}")
for name, shares, price, change in report:
    price = "$" + str(round(price, 2))
    print(f"{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}")
print("\n")

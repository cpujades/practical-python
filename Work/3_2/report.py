# report.py
#
# Exercise 2.7

import csv


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = dict(zip(headers, row))
            holding["shares"] = int(holding["shares"])
            holding["price"] = float(holding["price"])
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    """
    Read a CSV file of prices into a dict mapping names to prices.
    """
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
        shares = holding["shares"]
        price = holding["price"]
        current_price = prices[name]
        change = current_price - price
        report.append((name, shares, current_price, change))
    return report


def print_report(report):
    headers = "      Name     Shares      Price     Change"
    divider = "---------- ---------- ---------- ----------"
    print(f"\n{headers}\n{divider}")
    for name, shares, price, change in report:
        price = "$" + str(round(price, 2))
        print(f"{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}")
    print("\n")


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report("Data/portfolio.csv", "Data/prices.csv")

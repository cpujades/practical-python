# fileparse.py
#
# Exercise 3.12

import csv
import sys
import os

# Add the path to the 3_10 folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../3_10")))

# Now you can import the parse_csv function from fileparse
from fileparse import parse_csv


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    portfolio = parse_csv(filename, types=[str, int, float])

    return portfolio


def read_prices(filename):
    """
    Read a CSV file of prices into a dict mapping names to prices.
    """
    stocks = parse_csv(filename, types=[str, float], has_headers=False)

    return stocks


def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        name = holding["name"]
        shares = holding["shares"]
        price = holding["price"]
        current_price = [price for stock, price in prices if stock == name][0]
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


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f"Usage: {argv[0]} portfoliofile pricesfile")
    portfolio_report(argv[1], argv[2])


if __name__ == "__main__":
    main(sys.argv)

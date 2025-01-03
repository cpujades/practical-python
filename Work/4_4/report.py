# fileparse.py
#
# Exercise 3.18

import csv
import sys
import os
from stock import Stock

# Now you can import the parse_csv function from fileparse
from fileparse import parse_csv


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(filename) as file:
        portdicts = parse_csv(
            file, select=["name", "shares", "price"], types=[str, int, float]
        )
    portfolio = [Stock(d["name"], d["shares"], d["price"]) for d in portdicts]

    return portfolio


def read_prices(filename):
    """
    Read a CSV file of prices into a dict mapping names to prices.
    """
    with open(filename) as file:
        stocks = parse_csv(file, types=[str, float], has_headers=False)

    return stocks


def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        name = s.name
        shares = s.shares
        price = s.price
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

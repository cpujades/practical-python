# fileparse.py
#
# Exercise 3.18

import csv
import sys
import os
from stock import Stock
from tableformat import create_formatter
from portfolio import Portfolio

# Now you can import the parse_csv function from fileparse
from fileparse import parse_csv


def read_portfolio(filename, **opts):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(filename) as file:
        portdicts = parse_csv(
            file, select=["name", "shares", "price"], types=[str, int, float], **opts
        )
    portfolio = [Stock(**d) for d in portdicts]

    return Portfolio(portfolio)


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


def print_report(report_data, formatter):
    """
    Print a nicely formatted table from a list of (name, shares, price, change)
    tuples.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in report_data:
        price = "$" + str(round(price, 2))
        change = round(change, 2)
        row_data = [name, str(shares), price, change]
        formatter.row(row_data)
    print()


def portfolio_report(portfolio_filename, prices_filename, fmt="txt"):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    if len(argv) != 4:
        raise SystemExit(f"Usage: {argv[0]} portfoliofile pricesfile")
    portfolio_report(argv[1], argv[2], argv[3])


if __name__ == "__main__":
    main(sys.argv)

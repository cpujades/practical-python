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
        return Portfolio.from_csv(file, **opts)


def read_prices(filename, opts):
    """
    Read a CSV file of prices into a dict mapping names to prices.
    """
    with open(filename) as file:
        stocks = parse_csv(file, types=[str, float], has_headers=False, **opts)

    return dict(stocks)


def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.prices
        report.append((s.name, s.shares, current_price, change))
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

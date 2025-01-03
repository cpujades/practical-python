# pcost.py
#
# Exercise 1.33

import csv
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../3_12")))

from report import read_portfolio


def portfolio_cost(filename):
    tot_price = 0.0

    portfolio = read_portfolio(filename)
    for stock in portfolio:
        tot_price += stock["shares"] * stock["price"]

    return tot_price


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")

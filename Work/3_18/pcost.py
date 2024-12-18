# pcost.py
#
# Exercise 3.18

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


def main(sys_argv):
    if len(sys_argv) == 2:
        filename = sys_argv[1]
    else:
        filename = "Data/portfolio.csv"

    cost = portfolio_cost(filename)
    print(f"Total cost: {cost}")


if __name__ == "__main__":
    main(sys.argv)

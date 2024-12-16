# pcost.py
#
# Exercise 1.33

import csv
import sys


def portfolio_cost(filename):
    tot_price = 0.0
    try:
        with open(filename, "rt") as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                shares = int(row[1])
                price = float(row[2])
                tot_price += shares * price
    except ValueError as e:
        print(e)
    return tot_price


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")

# pcost.py
#
# Exercise 1.33

import csv
import sys


def portfolio_cost(filename):
    tot_price = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for idx, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                shares = int(record["shares"])
                price = float(record["price"])
                tot_price += shares * price
            except ValueError:
                print(f"Row {idx + 1}: Couldn't convert: {row}")

    return tot_price


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")

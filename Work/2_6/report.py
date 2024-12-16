# report.py
#
# Exercise 2.7

import csv


def read_prices(filename):
    stocks = {}

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                stocks[row[0]] = float(row[1])

    return stocks

# report.py
#
# Exercise 2.7

import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        name = headers[0]
        shares = headers[1]
        price = headers[2]
        for row in rows:
            holding = {
                name: row[0],
                shares: int(row[1]),
                price: float(row[2]),
            }
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    stocks = {}

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                stocks[row[0]] = float(row[1])

    return stocks


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")


def calculate_metrics(portfolio, prices):
    total_cost = 0.0
    current_value = 0.0
    gain_loss = 0.0
    for holding in portfolio:
        total_cost += holding["shares"] * holding["price"]
        current_value += holding["shares"] * prices[holding["name"]]
        if holding["name"] in prices:
            gain_loss += holding["shares"] * (
                prices[holding["name"]] - holding["price"]
            )
    print(f"Total cost: {total_cost}")
    print(f"Current value: {current_value}")
    print(f"Gain/Loss: {gain_loss}")


calculate_metrics(portfolio, prices)

# ticker.py

from follow import follow
from report import read_portfolio
from tableformat import create_formatter
import csv


def select_columns(rows, indices):
    for row in rows:
        yield [row[i] for i in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    yield (dict(zip(headers, row)) for row in rows)


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows


def ticker(portfolio_file, log_file, format="txt"):
    portfolio = read_portfolio(portfolio_file)
    lines = follow(log_file)
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row["name"] in portfolio)
    formatter = create_formatter(format)
    formatter.headings(["Name", "Price", "Change"])
    for row in rows:
        print(f"{row['name']:>10s} {row['price']:>10.2f} {row['change']:>10.2f}")


if __name__ == "__main__":
    portfolio = read_portfolio("../Data/portfolio.csv")
    lines = follow("../Data/stocklog.csv")
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row["name"] in portfolio)
    for row in rows:
        print(row)

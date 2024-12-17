# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=","):
    """
    Parse a CSV file into a list of records
    """
    # Read the CSV file
    with open(filename) as f:

        records = []

        # Parse the CSV file
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file header
        headers = next(rows) if has_headers else []

        if select:
            # Map the header to the selected columns
            indices = [headers.index(colname) for colname in select]
            headers = select

        for row in rows:
            # If a row is empty, skip it
            if not row:
                continue

            # Filter the row if select is provided
            if select:
                row = [row[idx] for idx in indices]

            # Apply the conversion functions if provided
            if types:
                row = [func(val) for func, val in zip(types, row)]

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

    return records

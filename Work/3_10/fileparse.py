# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(
    filename,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
):
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

        if select and not has_headers and not silence_errors:
            raise RuntimeError("select requires column headers")

        if select:
            # Map the header to the selected columns
            indices = [headers.index(colname) for colname in select]
            headers = select

        for rowno, row in enumerate(rows, start=1):
            # If a row is empty, skip it
            if not row:
                continue

            try:
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
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

    return records

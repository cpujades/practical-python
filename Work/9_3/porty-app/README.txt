Porty App Package
================

This package organizes a collection of Python modules for processing and reporting on stock portfolio data into a proper package structure.

Structure:
- porty-app/           # Top-level application directory
  - print-report.py    # Top-level script for running reports
  - portfolio.csv      # Sample portfolio data
  - prices.csv         # Sample price data
  - porty/             # Main package directory
    - __init__.py      # Package initializer
    - pcost.py         # Portfolio cost calculator
    - report.py        # Portfolio report generator
    - fileparse.py     # CSV parsing utilities
    - portfolio.py     # Portfolio class
    - stock.py         # Stock class
    - tableformat.py   # Table formatting
    - ticker.py        # Real-time stock ticker
    - follow.py        # Log file follower
    - typedproperty.py # Typed property decorators

Usage:
To generate a portfolio report:
python3 print-report.py portfolio.csv prices.csv txt
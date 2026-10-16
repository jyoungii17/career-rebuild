# CSV Cleaner & Report Generator

A command-line Python project that cleans customer-order CSV data and creates a summary report.

## What it does

The program:

- Reads customer order data from a CSV file
- Removes leading and trailing whitespace
- Checks for required columns
- Rejects blank customers and emails
- Rejects invalid and negative order totals
- Removes duplicate valid rows
- Writes valid rows to a cleaned CSV
- Creates a text report of the results

## Project files

- `customer_orders_raw.csv` — sample input data
- `cleaner.py` — cleaning, validation, duplicate, and file-writing functions
- `main.py` — runs the program
- `customer_orders_clean.csv` — generated cleaned data
- `cleaning_report.txt` — generated summary report

## Rules

A row is kept only when:

1. `customer`, `email`, and `order_total` columns exist
2. Customer and email are not blank
3. Order total is a number that is zero or greater
4. It is not a duplicate of an earlier valid row

Duplicate comparisons use the cleaned values of all three fields.

## Run the project

From the `csv-cleaner` folder, run:

```bash
py main.py
```

## Sample result

The included sample has 7 rows:

- 2 valid rows kept
- 1 duplicate row
- 1 blank email
- 1 invalid total
- 1 blank customer
- 1 negative total

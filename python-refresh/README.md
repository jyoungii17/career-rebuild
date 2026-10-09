# Python Expense Tracker

A command-line expense tracker built with Python. The project supports expense management, CSV data persistence, filtering, sorting, budgeting, category summaries, input validation, and automated testing.

## Features

- Add and save expenses
- Remove expenses
- View all expenses
- Calculate total and average expenses
- Find largest and smallest expenses
- Filter expenses by minimum amount
- Sort expenses by amount
- View expenses by category
- Track budget status
- Validate user input
- Handle invalid CSV data
- Persist data using CSV files
- Automated tests with `unittest`

## Usage

Run the program from the `python-refresh` directory:

```bash
py day2.py
```

The main menu provides options to:

1. Manage expenses
2. View expenses
3. View summary
4. Filter expenses
5. Sort expenses
6. View category totals
7. Exit

## Testing

The project includes automated tests using Python's `unittest` framework.

Run the tests with:

```bash
py -m unittest test_expenses.py
```

The test suite covers expense calculations, filtering, largest and smallest expenses, category totals, and empty-list behavior.

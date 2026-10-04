from datetime import date
from budget import get_budget, check_budget
def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

def calculate_expense_average(expenses):
    total = calculate_total(expenses)
    expense_count = count_expenses(expenses)
    if expense_count == 0:
        return 0
    average = total / expense_count
    return average

def count_expenses(expenses):
    return len(expenses)

def find_largest_expense(expenses):
    if not expenses:
        return None
    largest_expense = expenses[0]
    for expense in expenses:
        if expense['amount'] > largest_expense['amount']:
            largest_expense = expense
    return largest_expense

def find_smallest_expense(expenses):
    if not expenses:
        return None
    smallest_expense = expenses[0]
    for expense in expenses:
        if expense['amount'] < smallest_expense['amount']:
            smallest_expense = expense
    return smallest_expense

def calculate_category_totals(expenses):
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += expense["amount"]
    return category_totals

def display_category_totals(category_totals):
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

def display_summary(expenses):
    today = date.today().isoformat()
    print(f"Date: {today}")

    budget = get_budget()
    total = calculate_total(expenses)
    print(f"Total Expenses: ${total:.2f}")
    average = calculate_expense_average(expenses)
    print(f"Average Expense: ${average:.2f}")
    check_budget(total, budget)
    largest = find_largest_expense(expenses)
    if largest is not None:
        print(f"Largest Expense: {largest['name']} - ${largest['amount']:.2f}")
    else:
        print("No expenses found.")
    smallest = find_smallest_expense(expenses)
    if smallest is not None:
        print(f"Smallest Expense: {smallest['name']} - ${smallest['amount']:.2f}")
    else:
        print("No expenses found.")
    expense_count = count_expenses(expenses)
    print(f"Total Number of Expenses: {expense_count}")
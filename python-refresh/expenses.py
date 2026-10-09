from datetime import date
from data import save_expenses
from validation import validate_amount, validate_category, validate_name

def add_expense(expenses):
    expense_date = date.today().isoformat()
    expenses.append({
        "name": validate_name(), 
        "amount": validate_amount(), 
        "category": validate_category(), 
        "date": expense_date
    })
    save_expenses(expenses)

def remove_expense(expenses):
    if not expenses:
        print("No expenses to remove.")
        return
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']} - ${expense['amount']:.2f}")
        
    choice = input("Enter the number of the expense to remove: ")
        
    try:
        choice = int(choice)            
    except ValueError:
        print("Please enter a valid number.")
        return
        
    if choice < 1 or choice > len(expenses):
        print("Invalid expense number.")
        return

    removed_expense = expenses.pop(choice - 1)
    print(f"{removed_expense['name']} has been removed.")

    save_expenses(expenses)
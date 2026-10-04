from datetime import date
from data import save_expenses

def add_expense(expenses):
    
    print("Enter the name of expense: ")
    expense_name = input()
    
    valid_amount = False
    while not valid_amount:
        try:
            expense_amount = float(input("Enter the amount of the expense: "))
            if expense_amount > 0:
                valid_amount = True
            else:
                print("Invalid input.")
        except ValueError:
            print("Invalid input.")

    expense_category = input("Enter the category of the expense: ") 
    expense_date = date.today().isoformat()
    expenses.append({
        "name": expense_name, 
        "amount": expense_amount, 
        "category": expense_category, 
        "date": expense_date
    })
    save_expenses(expenses)
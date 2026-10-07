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
# Day 1 - Python Expense Tracker

expenses = [
    {"name": "Groceries", "amount": 75.50},
    {"name": "Gas", "amount": 40.00},
    {"name": "Coffee", "amount": 5.25},
    {"name": "Phone Bill", "amount": 60.00}
]

budget = 200

add_expense(expenses)

for expense in expenses:
    print(f"{expense['name']}: ${expense['amount']:.2f}")

total = 0
for expense in expenses:
    total += expense['amount']

print(f"Total Expenses: ${total:.2f}")
if total > budget:
    print("You are over budget!")
else:
    print("You are within budget.")


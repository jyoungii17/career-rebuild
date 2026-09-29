import csv

def load_expenses():
    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)
        expenses = []
        for row in reader:
            expenses.append({"name": row["name"], "amount": float(row["amount"])})
    return expenses

def save_expenses(expenses):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "amount"])
        writer.writeheader()
        for expense in expenses:
            writer.writerow({"name": expense["name"], "amount": expense["amount"]})

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

def find_largest_expense(expenses):
    if not expenses:
        return None
    largest_expense = expenses[0]
    for expense in expenses:
        if expense['amount'] > largest_expense['amount']:
            largest_expense = expense
    return largest_expense

def add_expense(expenses):
    print("Enter the name of expense: ")
    expense_name = input()
    
    valid_amount = False
    while not valid_amount:
        try:
            expense_amount = float(input("Enter the amount of the expense: "))
            valid_amount = True
        except ValueError:
            print("Invalid input.")
            

    expenses.append({"name": expense_name, "amount": expense_amount})
    save_expenses(expenses)

def get_budget():
    while True:
        try:
            budget = float(input("Enter your budget: "))
            return budget
        except ValueError:
            print("Invalid input.")

def check_budget(total, budget):
    if total > budget:
        print("You are over budget!")
    else:
        print("You are within budget.")

def display_expenses(expenses):
    for expense in expenses:
        print(f"{expense['name']}: ${expense['amount']:.2f}")

def count_expenses(expenses):
    return len(expenses)

def display_menu():
    print("===== Expense Tracker =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View summary")
    print("4. Exit")

def get_menu_choice():
    display_menu()
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        print("Invalid choice. Please enter a number between 1 and 4.")
    

def main():
    expenses = load_expenses()
    
    while True:
        choice = get_menu_choice()
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            budget = get_budget()
            total = calculate_total(expenses)
            print(f"Total Expenses: ${total:.2f}")
            check_budget(total, budget)
            largest = find_largest_expense(expenses)
            if largest is not None:
                print(f"Largest Expense: {largest['name']} - ${largest['amount']:.2f}")
            else:
                print("No expenses found.")
            expense_count = count_expenses(expenses)
            print(f"Total Number of Expenses: {expense_count}")
        elif choice == '4':
            print("Exiting the program.")
            break

main()
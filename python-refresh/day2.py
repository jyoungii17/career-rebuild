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

def calculate_expense_average(expenses):
    total = calculate_total(expenses)
    expense_count = count_expenses(expenses)
    if expense_count == 0:
        return 0
    average = total / expense_count
    return average

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

def filter_expenses(expenses, minimum_amount):
    filtered_expenses = []
    for expense in expenses:
        if expense['amount'] >= minimum_amount:
            filtered_expenses.append(expense)
    return filtered_expenses

def sort_expenses_by_amount(expenses):
    valid_choice = False
    while not valid_choice:
        choice = input("Enter the sort direction you desire (1 - Descending, 2 - Ascending): ")
        if choice in ['1', '2']:
            if choice == '1':
                descending = True
            else:
                descending = False
            valid_choice = True
        else:
            print("Invalid Option. Please enter '1' or '2'.")       
    sorted_expenses = sorted(expenses, key=lambda expense: expense['amount'], reverse=descending)
    return sorted_expenses

def display_menu():
    print("===== Expense Tracker =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View summary")
    print("4. Filter expenses")
    print("5. Sort expenses")
    print("6. Exit")

def get_menu_choice():
    display_menu()
    while True:
        choice = input("Enter your choice (1-6): ")
        if choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        print("Invalid choice. Please enter a number between 1 and 6.")
    
def display_summary(expenses):
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

def main():
    expenses = load_expenses()
    
    while True:
        choice = get_menu_choice()
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            display_summary(expenses)
        elif choice == '4':
            valid_input = False
            while not valid_input:
                try:
                    minimum_amount = float(input("Enter the minimum amount: "))
                    valid_input = True
                except ValueError:
                    print("Invalid input.")
            filtered_expenses = filter_expenses(expenses, minimum_amount)
            if not filtered_expenses:
                print("No expenses found matching that amount.")
            for expense in filtered_expenses:
                print(f"{expense['name']}: ${expense['amount']:.2f}")
        elif choice == '5':
            sorted_expenses = sort_expenses_by_amount(expenses)
            for expense in sorted_expenses:
                print(f"{expense['name']}: ${expense['amount']:.2f}")
        elif choice == '6':
            print("Exiting the program.")
            break

main()

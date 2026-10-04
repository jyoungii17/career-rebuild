def display_expenses(expenses):
    for expense in expenses:
        print(f"{expense['name']}: ${expense['amount']:.2f} - {expense['category']} - {expense['date']}")

def display_menu():
    print("===== Expense Tracker =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View summary")
    print("4. Filter expenses")
    print("5. Sort expenses")
    print("6. View category totals")
    print("7. Exit")

def get_menu_choice():
    display_menu()
    while True:
        choice = input("Enter your choice (1-7): ")
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            return choice
        print("Invalid choice. Please enter a number between 1 and 7.")
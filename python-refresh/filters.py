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

def get_minimum_amount():
    valid_input = False
    while not valid_input:
        try:
            minimum_amount = float(input("Enter the minimum amount: "))
            valid_input = True
        except ValueError:
            print("Invalid input.")
    return minimum_amount

def display_filtered_expenses(filtered_expenses):
    if not filtered_expenses:
        print("No expenses found matching that amount.")
    for expense in filtered_expenses:
        print(f"{expense['name']}: ${expense['amount']:.2f} - {expense['category']} - {expense['date']}")

def display_sorted_expenses(sorted_expenses):
    for expense in sorted_expenses:
        print(f"{expense['name']}: ${expense['amount']:.2f} - {expense['category']} - {expense['date']}")
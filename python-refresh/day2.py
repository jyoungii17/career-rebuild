from data import load_expenses
from filters import (
    filter_expenses, 
    sort_expenses_by_amount, 
    get_minimum_amount, 
    display_filtered_expenses, 
    display_sorted_expenses
)
from ui import display_expenses, get_menu_choice, get_manage_expenses_submenu_choice
from expenses import add_expense, remove_expense
from reports import (
    calculate_category_totals,
    display_category_totals,
    display_summary
)

def main():
    expenses = load_expenses()
    
    while True:
        choice = get_menu_choice()
        if choice == '1':
            submenu_choice = get_manage_expenses_submenu_choice()
            if submenu_choice == '1':
                add_expense(expenses)
            elif submenu_choice == '2':
                remove_expense(expenses)
            elif submenu_choice == '3':
                pass
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            display_summary(expenses)
        elif choice == '4':
            minimum_amount = get_minimum_amount()
            filtered_expenses = filter_expenses(expenses, minimum_amount)
            display_filtered_expenses(filtered_expenses)
        elif choice == '5':
            sorted_expenses = sort_expenses_by_amount(expenses)
            display_sorted_expenses(sorted_expenses)
        elif choice == '6':
            category_totals = calculate_category_totals(expenses)
            display_category_totals(category_totals)
        elif choice == '7':
            print("Exiting the program.")
            break

main()

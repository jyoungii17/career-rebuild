def validate_name():
    while True:
        print("Enter the name of expense: ")
        expense_name = input().strip()
        if expense_name == "":
                print("Invalid Name.")
        else:
            break
    return expense_name

def validate_amount():
    valid_amount = False
    while not valid_amount:
        try:
            expense_amount = float(input("Enter the amount of the expense: "))
            if expense_amount > 0:
                valid_amount = True
            else:
                 print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
    return expense_amount

def validate_category():
    while True:
        expense_category = input("Enter the category of the expense: ").strip()
        if expense_category =="":
            print("Invalid Category.")
        else:
            break 
        
    return expense_category
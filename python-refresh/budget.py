def get_budget():
    while True:
        try:
            budget = float(input("Enter your budget: "))
            if budget >= 0:
                return budget
            else:
                print("Budget cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")

def check_budget(total, budget):
    if total > budget:
        print("You are over budget!")
    else:
        print("You are within budget.")
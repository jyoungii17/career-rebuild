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
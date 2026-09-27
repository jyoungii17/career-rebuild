# Day 1 - Python Expense Tracker
name = "Johnathan"
age = 24

print("My name is " + name + " and I am " + str(age) + " years old.")

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

jobs = ["Software Engineer", "Data Analyst", "Python Developer", "Web Developer"]

for job in jobs:
    print(job)

expenses = [25.50, 42.75, 18.25, 100.10]

total = sum(expenses)

print("Total expenses: ${:.2f}".format(total))

def calculate_total(quantity, price):
    return quantity * price

total = calculate_total(5, 12.50)

print(f"Total: ${total:.2f}")

job_application = {
    "company": "Microsoft",
    "position": "Software Engineer",
    "status": "Pending",
    "salary": 120000
}

print(f"Company: {job_application['company']}")
print(f"Position: {job_application['position']}")
print(f"Status: {job_application['status']}")
print(f"Salary: ${job_application['salary']:,}")

jobs = [
    {
       "company": "Microsoft",
        "position": "Software Engineer",
        "status": "Pending"
    },
    {
        "company": "Google",
        "position": "Data Analyst",
        "status": "Interview"
    },
    {
        "company": "Amazon",
        "position": "Python Developer",
        "status": "Applied"
    }
]

for job in jobs:
    print(f"{job['company']} - {job['position']}")

expenses = [
    {"name": "Groceries", "amount": 75.50},
    {"name": "Gas", "amount": 40.00},
    {"name": "Coffee", "amount": 5.25},
    {"name": "Phone Bill", "amount": 60.00}
]

total_expenses = 0
budget = 200

print("Enter the name of expense: ")
expense_name = input()

print("Enter the amount of the expense: ")
expense_amount = float(input())

expenses.append({"name": expense_name, "amount": expense_amount})

for expense in expenses:
    print(f"{expense['name']}: ${expense['amount']:.2f}")
    total_expenses += expense['amount']

print(f"Total Expenses: ${total_expenses:.2f}")

if total_expenses > budget:
    print("You are over budget!")
else:
    print("You are within budget.")
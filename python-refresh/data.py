import csv

def load_expenses():
    expenses = []
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                expense_name = row["name"].strip()
                expense_category = row.get("category", "Uncategorized").strip()
                if expense_name == "":
                    print("Skipping expense with invalid name.")
                    continue
                if expense_category == "":
                    print("Skipping expense with invalid category.")
                    continue
                try:
                    expenses.append({
                        "name": expense_name, 
                        "amount": float(row["amount"]), 
                        "category": expense_category, 
                        "date": row.get("date", "Unknown")
                    })
                except ValueError:
                    print("Skipping invalid expense amount.")
    except FileNotFoundError:
        print("No expense file found. Starting with an empty list.")
    return expenses

def save_expenses(expenses):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "amount", "category", "date"])
        writer.writeheader()
        for expense in expenses:
            writer.writerow({
                "name": expense["name"], 
                "amount": expense["amount"], 
                "category": expense["category"], 
                "date": expense["date"]
            })
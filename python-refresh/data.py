import csv

def load_expenses():
    expenses = []
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                expenses.append({
                    "name": row["name"], 
                    "amount": float(row["amount"]), 
                    "category": row.get("category", "Uncategorized"), 
                    "date": row.get("date", "Unknown")
                })
    except FileNotFoundError:
        pass
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
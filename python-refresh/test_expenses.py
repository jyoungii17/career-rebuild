import unittest
from datetime import date
from reports import (
    calculate_total, 
    find_largest_expense, 
    find_smallest_expense,
    calculate_category_totals
)
from filters import filter_expenses
from unittest.mock import patch
from expenses import remove_expense, add_expense

class TestReports(unittest.TestCase):
    def test_calculate_total(self):
        expenses = [
            {"name": "Food", "amount": 10.00},
            {"name": "Gas", "amount": 20.00},
            {"name": "Coffee", "amount": 5.00}
        ]

        result = calculate_total(expenses)

        self.assertEqual(result, 35.00)
    def test_calculate_total_empty(self):
        expenses = []

        result = calculate_total(expenses)

        self.assertEqual(result, 0)
    def test_find_largest_expense(self):
        expenses = [
            {"name": "Food", "amount": 10.00},
            {"name": "Gas", "amount": 20.00},
            {"name": "Computer", "amount": 500.00},
            {"name": "Coffee", "amount": 5.00}
        ]

        result = find_largest_expense(expenses)

        self.assertEqual(result["name"], "Computer")
        self.assertEqual(result["amount"], 500.00)
    def test_find_largest_expense_empty(self):
        expenses = []

        result = find_largest_expense(expenses)

        self.assertIsNone(result)
    def test_filter_expenses(self):
        expenses = [
            {"name": "Coffee", "amount": 5.00},
            {"name": "Gas", "amount": 40.00},
            {"name": "Groceries", "amount": 75.50},
            {"name": "Phone", "amount": 60.00}
        ]

        result = filter_expenses(expenses, 50)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], "Groceries")
        self.assertEqual(result[1]["name"], "Phone")
    def test_filter_expenses_no_matches(self):
        expenses = [
            {"name": "Coffee", "amount": 5.00},
            {"name": "Gas", "amount": 10.00},
            {"name": "Food", "amount": 15.00}
        ]

        result = filter_expenses(expenses, 50)

        self.assertEqual(result, [])
    def test_find_smallest_expense(self):
        expenses = [
            {"name": "Food", "amount": 10.00},
            {"name": "Gas", "amount": 20.00},
            {"name": "Coffee", "amount": 5.00},
            {"name": "Rent", "amount": 800.00}
        ]

        result = find_smallest_expense(expenses)

        self.assertEqual(result["name"], "Coffee")
        self.assertEqual(result["amount"], 5.00)        
    def test_find_smallest_expense_empty(self):
        expenses = []

        result = find_smallest_expense(expenses)

        self.assertIsNone(result)
    def test_calculate_category_totals(self):
        expenses = [
            {"name": "Pizza", "amount": 20.00, "category": "Food"},
            {"name": "Burger", "amount": 15.00, "category": "Food"},
            {"name": "Gas", "amount": 40.00, "category": "Transportation"},
            {"name": "Coffee", "amount": 5.00, "category": "Food"}
        ]

        result = calculate_category_totals(expenses)

        self.assertEqual(result["Food"], 40.00)
        self.assertEqual(result["Transportation"], 40.00)
    def test_calculate_category_totals_empty(self):
        expenses = []
        result = calculate_category_totals(expenses)
        self.assertEqual(result, {})

class TestRemoveExpense(unittest.TestCase):
    def test_remove_expense(self):
        expenses = [
            {"name": "Pizza", "amount": 20.00, "category": "Food"},
            {"name": "Burger", "amount": 15.00, "category": "Food"},
            {"name": "Gas", "amount": 40.00, "category": "Transportation"},
            {"name": "Coffee", "amount": 5.00, "category": "Food"}
        ]
        with patch("builtins.input", return_value = "2"):
            with patch("expenses.save_expenses") as mock_save:
                remove_expense(expenses)

        self.assertEqual(len(expenses), 3)
        self.assertEqual(
            [expense["name"] for expense in expenses],
            ["Pizza", "Gas", "Coffee"]
        )
        mock_save.assert_called_once_with(expenses)
    def test_remove_expense_empty(self):
        expenses = []
        
        with patch("expenses.save_expenses") as mock_save:
            result = remove_expense(expenses)

        self.assertIsNone(result)
        self.assertEqual(expenses, [])
        mock_save.assert_not_called()
    def test_remove_expense_invalid_input(self):
        expenses = [
            {"name": "Pizza", "amount": 20.00, "category": "Food"},
            {"name": "Burger", "amount": 15.00, "category": "Food"}
        ]

        with patch("builtins.input", return_value = "abc"):
            with patch("expenses.save_expenses") as mock_save:
                result = remove_expense(expenses)

        self.assertIsNone(result)
        self.assertEqual(expenses, [
            {"name": "Pizza", "amount": 20.00, "category": "Food"},
            {"name": "Burger", "amount": 15.00, "category": "Food"}
            ]
        )
        mock_save.assert_not_called()
    def test_remove_expense_out_of_range(self):
        expenses = [
            {"name": "Pizza", "amount": 20.00, "category": "Food"},
            {"name": "Burger", "amount": 15.00, "category": "Food"}
        ]

        with patch("builtins.input", return_value="5"):
            with patch("expenses.save_expenses") as mock_save:
                result = remove_expense(expenses)

        self.assertIsNone(result)
        self.assertEqual(expenses, [
            {"name": "Pizza", "amount": 20.00, "category": "Food"},
            {"name": "Burger", "amount": 15.00, "category": "Food"}
            ]
        )
        mock_save.assert_not_called()

class TestAddExpense(unittest.TestCase):
    def test_add_expense(self):
        expenses = []
        today = date.today().isoformat()
        with patch("builtins.input", side_effect=["Pizza", "20", "Food"]):
            with patch("expenses.save_expenses") as mock_save:
                add_expense(expenses)
        self.assertEqual(expenses[0]["name"], "Pizza")
        self.assertEqual(expenses[0]["amount"], 20.00)
        self.assertEqual(expenses[0]["category"], "Food")
        self.assertEqual(expenses[0]["date"], date.today().isoformat())
        mock_save.assert_called_once_with(expenses)

if __name__ == "__main__":
    unittest.main()
import json
from expense import Expense


class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    # Add Expense
    def add_expense(self, expense):
        self.expenses.append(expense)

    # Get All Expenses
    def get_expenses(self):
        return self.expenses

    # Calculate Total
    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    # Category-wise Expense Summary
    def category_wise_summary(self):
        category_summary = {}

        for expense in self.expenses:
            category = expense.category
            amount = expense.amount

            category_summary[category] = category_summary.get(category, 0) + amount

        return category_summary

    # Delete Expense
    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense deleted successfully!")
        else:
            print("Invalid index! No expense deleted.")

    # Save Expenses to JSON
    def save_expenses(self):
        data = []

        for expense in self.expenses:
            data.append({
                "amount": expense.amount,
                "category": expense.category,
                "description": expense.description,
                "date": expense.date
            })

        with open("expenses.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Expenses saved successfully!")

    def load_expenses(self):
        try:
            with open("expenses.json", "r") as file:
                data = json.load(file)
                self.expenses = []
                for item in data:
                    expense = Expense(
                        amount=item["amount"],
                        category=item["category"],
                        description=item["description"],
                        date=item["date"]
                    )
                    self.expenses.append(expense)
            print("Expenses loaded successfully!")
        except FileNotFoundError:
            print("No existing expenses found.")
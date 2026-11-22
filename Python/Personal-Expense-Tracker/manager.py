import json
from expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_expenses(self):
        return self.expenses

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
        else:
            print("Invalid index! No expense deleted.")

    def save_expenses(self):
        try:
            with open("expenses.json", "w") as file:
                data = [
                    {
                        "amount": expense.amount,
                        "category": expense.category,
                        "description": expense.description,
                        "date": expense.date
                    }
                    for expense in self.expenses
                ]
                json.dump(data, file, indent=4)
                print("Expenses saved successfully!") 

        except OSError as e:
           print(f"Error saving expenses: {e}")
    
    def load_expenses(self):
        try:
            with open("expenses.json", "r") as file:
                data = json.load(file)

                for item in data:
                    expense = Expense(
                        amount=item["amount"],
                        category=item["category"],
                        description=item["description"],
                        date=item["date"]
                    )
                    self.expenses.append(expense)

        except FileNotFoundError:
            print("No previous expenses found. Starting fresh.")
        except json.JSONDecodeError:
            print("Error reading expenses file. Starting fresh.")
        except OSError as e:
            print(f"Error loading expenses: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while loading expenses: {e}")
                    

    def category_wise_summary(self):
        summary = {}

        for expense in self.expenses:
            if expense.category in summary:
                summary[expense.category] += expense.amount
            else:
                summary[expense.category] = expense.amount

        return summary        

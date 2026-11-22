from expense import Expense
from manager import ExpenseManager
from datetime import datetime

manager = ExpenseManager()

def validate_amount(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0!")
        return amount
    except ValueError as e:
        print(f"Invalid amount: {e}")
        return None

def validate_category(category):
    if not category.strip():
        print("Category cannot be empty!")
        return None
    return category.strip()

def validate_description(description):
    if not description.strip():
        print("Description cannot be empty!")
        return None
    return description.strip()    

def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date
    except ValueError:
        print("Invalid date! Please enter in YYYY-MM-DD format.")
        return None

def validate_expense_number(number, max_index):
    try:
        number = int(number)
        if 1 <= number <= max_index:
            return number
        else:
            print(f"Invalid number! Please enter a number between 1 and {max_index}.")
            return None
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return None

def validate_month(month):
    try:
        month = int(month)
        if 1 <= month <= 12:
            return str(month).zfill(2)
        else:
            print("Invalid month! Please enter a number between 1 and 12.")
            return None
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return None    

while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Total Expenses")
    print("4. Exit")
    print("5. Delete Expense")
    print("6. Search Expense")
    print("7. Monthly Expense Report")
    print("8. Category-wise Expense Summary")

    choice = input("Enter your choice: ")

    # 1. Add Expense
    if choice == "1":

        # Amount Validation
        while True:
         amount = validate_amount(input("Enter amount: "))
         if amount is not None:
           break

        # Category Validation
        while True:
          category = validate_category(input("Enter category: "))
          if category is not None:
           break

        # Description Validation
        while True:
          description = validate_description(input("Enter description: "))
          if description is not None:
            break

        # Date Validation
        while True:
         date = validate_date(input("Enter date (YYYY-MM-DD): "))
         if date is not None:
          break

        # Create and Save Expense
        expense = Expense(amount, category, description, date)
        manager.add_expense(expense)
        manager.save_expenses()

    # 2. View All Expenses
    elif choice == "2":
        print("\nAll Expenses:")

        expenses = manager.get_expenses()

        if not expenses:
            print("No expenses found!")
        else:
            for expense in expenses:
                print(expense)

    # 3. Show Total Expenses
    elif choice == "3":
        print("Total Expenses:", manager.total_expenses())

    # 4. Exit
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    # 5. Delete Expense
    elif choice == "5":
     expenses = manager.get_expenses()

     if not expenses:
        print("No expenses found!")
     else:
        for i, expense in enumerate(expenses, start=1):
            print(i, expense)

        index = validate_expense_number(
            input("Enter expense number to delete: "),
            len(expenses)
        )

        if index is not None:
            manager.delete_expense(index - 1)
            manager.save_expenses()
    # 6. Search Expense 
    elif choice == "6":
      search_category = input("Enter category to search: ").strip()

      found = False

      for expense in manager.get_expenses():
        if expense.category.lower() == search_category.lower():
            print(expense)
            found = True

      if not found:
        print("No expenses found!")    

    # 7. Monthly Expense Report
    elif choice == "7":
       while True:
           try:
              month = int(input("Enter month (1-12): "))

              if 1 <= month <= 12:
                 month = str(month).zfill(2)
                 break
              else:
                print("Please enter a month between 1 and 12!")

           except ValueError:
              print("Invalid input! Enter numbers only.")

       if len(month) == 1:
          month = "0" + month

       found = False

       for expense in manager.get_expenses():
          if expense.date[5:7] == month:
             print(expense)
             found = True

       if not found:
            print("No expenses found for this month!")
        

    # 8. Category-wise Expense Summary
    elif choice == "8":
        category_summary = manager.category_wise_summary()
        if category_summary:
            print("\nCategory-wise Expense Summary:")
            for category, total in category_summary.items():
                print(f"{category}: ₹{total:.2f}")
        else:
            print("No expenses found!")

    else:
        print("Invalid choice! Try again.")

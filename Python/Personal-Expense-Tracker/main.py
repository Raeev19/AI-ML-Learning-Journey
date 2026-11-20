from expense import Expense
from manager import ExpenseManager
from datetime import datetime

manager = ExpenseManager()

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
            try:
                amount = float(input("Enter amount: "))

                if amount <= 0:
                    print("Amount must be greater than 0!")
                else:
                    break

            except ValueError:
                print("Invalid amount! Please enter numbers only.")

        # Category Validation
        while True:
            category = input("Enter category: ").strip()

            if category:
                break
            else:
                print("Category cannot be empty!")

        # Description Validation
        while True:
            description = input("Enter description: ").strip()

            if description:
                break
            else:
                print("Description cannot be empty!")

        # Date Validation
        while True:
            date = input("Enter date (YYYY-MM-DD): ")

            try:
                datetime.strptime(date, "%Y-%m-%d")
                print("Valid date!")
                break

            except ValueError:
                print("Invalid date! Please enter again.")

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

            try:
                index = int(input("Enter expense number to delete: "))

                if 1 <= index <= len(expenses):
                    manager.delete_expense(index - 1)
                    manager.save_expenses()
                else:
                    print("Invalid expense number!")

            except ValueError:
                print("Please enter a valid number!")

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
                print(f"{category}: ${total:.2f}")
        else:
            print("No expenses found!")

    else:
        print("Invalid choice! Try again.")

def user_dashboard(user, budget_tracker):
    from Budget_managment import set_budget_goals, capture_expenses
    from report import generate_report
    from Transactions import Transaction

    budget_goals = None
    expenses = None

    print(f"\nWelcome, {user.name}! What would you like to do?")
    while True:
        print("\n1. Manage Accounts")
        print("2. Record Transactions")
        print("3. Set Budgets")
        print("4. View Reports")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(user)
        elif choice == '2':
            amount = float(input("Enter the transaction amount: "))
            is_income = input("Is this an income? (y/n): ").lower() == 'y'
            budget_tracker.add_transaction(Transaction(amount, is_income))
            print("Transaction recorded!")
        elif choice == '3':
            budget_goals = set_budget_goals()
            expenses = capture_expenses()
            print("Budgets and expenses captured!")
        elif choice == '4':
            generate_report(budget_tracker, budget_goals, expenses)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")

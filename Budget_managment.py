def set_budget_goals():
    budget_goals = {}
    categories = ['Housing', 'Utilities', 'Food', 'Transportation', 'Healthcare', 'Miscellaneous']

    print("Set your budget goals for each category:\n")
    for category in categories:
        while True:
            try:
                goal = float(input(f"Enter your budget goal for {category}: $"))
                if goal < 0:
                    print("Please enter a positive amount.")
                else:
                    budget_goals[category] = goal
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return budget_goals


def capture_expenses():
    expenses = {}
    categories = ['Housing', 'Utilities', 'Food', 'Transportation', 'Healthcare', 'Miscellaneous']

    print("\nPlease enter your actual monthly expenses for each category:\n")
    for category in categories:
        while True:
            try:
                expense = float(input(f"Enter your actual expense for {category}: $"))
                if expense < 0:
                    print("Please enter a positive amount.")
                else:
                    expenses[category] = expense
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return expenses


def quiz_on_expenses(budget_goals):
    categories = ['Housing', 'Utilities', 'Food', 'Transportation', 'Healthcare', 'Miscellaneous']

    print("\nLet's quiz you on your monthly expenses compared to your budget goals.")
    for category in categories:
        print(f"\nCategory: {category}")
        actual_expense = budget_goals.get(category)
        print(f"Your budget goal: ${actual_expense:.2f}")

        while True:
            try:
                user_expense = float(input(f"Enter your actual expense for {category}: $"))
                if user_expense < 0:
                    print("Please enter a positive amount.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        if user_expense <= actual_expense:
            print(f"Great job! You are within your budget for {category}.")
        else:
            print(f"You've exceeded your budget for {category}. Try to cut back next month!")


def main():
    print("Welcome to the Budget Management System!\n")

    # Set the budget goals
    budget_goals = set_budget_goals()

    # Capture the user's monthly expenses
    expenses = capture_expenses()

    # Compare the expenses to the budget goals
    quiz_on_expenses(budget_goals)

    print("\nThank you for using the Budget Management System! Keep tracking your expenses!")

if __name__ == "__main__":
    main()


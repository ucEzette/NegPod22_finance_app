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


def quiz_on_expenses(budget_goals, expenses):
    print("\nComparing your actual expenses to your budget goals:")
    for category in budget_goals:
        goal = budget_goals[category]
        actual = expenses.get(category, 0)
        print(f"\nCategory: {category}")
        print(f"Budget Goal: {goal}")
        print(f"Actual Expense: {actual}")

        if actual <= goal:
            print("Great job! You stayed within budget.")
        else:
            print("You've exceeded your budget for this category. Try to cut back next month!")


def main():
    print("Welcome to the Budget Management System!\n")

    # Set the budget goals
    budget_goals = set_budget_goals()

    # Capture the user's monthly expenses
    expenses = capture_expenses()

    # Compare the expenses to the budget goals
    quiz_on_expenses(budget_goals, expenses)

    print("\nThank you for using the Budget Management System! Keep tracking your expenses!")

if __name__ == "__main__":
    main()


def generate_report(budget_tracker, budget_goals=None, expenses=None):
    print("\n--- Financial Report ---")
    if budget_tracker:
        budget_tracker.display_transactions()
    if budget_goals and expenses:
        from Budget_managment import quiz_on_expenses
        quiz_on_expenses(budget_goals, expenses)
    
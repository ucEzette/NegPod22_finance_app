from accounts import AccountManager
from transactions import BudgetTracker
from dashboard import user_dashboard

def main():
    account_manager = AccountManager()
    user = account_manager.create_account()

    initial_balance = float(input("Enter your initial balance: "))
    is_initial_income = input("Is this an income? (y/n): ").lower() == 'y'
    currency = input("Enter the currency (e.g., USD): ")

    budget_tracker = BudgetTracker(initial_balance, is_initial_income, currency)
    user_dashboard(user, budget_tracker)

if __name__ == "__main__":
    main()

import re

class Transaction:
    def __init__(self, amount, is_income):
        # Initialize a transaction with amount and type (income or expense)
        self.amount = amount
        self.is_income = is_income

    def apply_to_balance(self, balance):
        # Update the balance based on whether the transaction is income or expense
        if self.is_income:
            return balance + self.amount
        else:
            return balance - self.amount

class BudgetTracker:
    def __init__(self, initial_balance, is_initial_income, currency):
        # Initialize the budget tracker with starting balance, income type, and currency
        self.balance = self.initialize_balance(initial_balance, is_initial_income)
        self.transactions = []  # List to store transactions
        self.total_income = 0    # Total income amount
        self.total_expenses = 0   # Total expenses amount
        self.currency = currency   # Currency type

    def initialize_balance(self, initial_balance, is_initial_income):
        # Set the initial balance based on whether it's an income or not
        if is_initial_income:
            return initial_balance
        else:
            return -initial_balance

    def add_transaction(self, transaction):
        # Add a transaction and update balance and totals
        self.transactions.append(transaction)
        self.balance = transaction.apply_to_balance(self.balance)
        if transaction.is_income:
            self.total_income += transaction.amount  # Update total income
        else:
            self.total_expenses += transaction.amount  # Update total expenses

    def display_transactions(self):
        # Display all transactions and current financial status
        print("Here are your budget transactions:")
        print("Transactions:")
        for transaction in self.transactions:
            # Print each transaction as either income or expense
            print(f"{'Income' if transaction.is_income else 'Expense'}: {transaction.amount} {self.currency}")
        print(f"Total Income: {self.total_income} {self.currency}")
        print(f"Total Expenses: {self.total_expenses} {self.currency}")
        # Check if the user is in a surplus or deficit
        if self.balance < 0:
            print(f"You're in a deficit of {abs(self.balance)} {self.currency}")
        else:
            print(f"You're in a surplus of {self.balance} {self.currency}")
        print("Thank you! Be sure to check out our other resources and remember to rate your experience with us.")

def main():
    # Get initial balance from user
    initial_balance = float(input("Enter the initial balance: "))
    # Check if the initial balance is income
    is_initial_income = input("Is the initial balance an income? (y/n) ").lower() == 'y'
    
    # Restrict currency options
    valid_currencies = ['FRW', 'NAIRA', 'USD', 'EUR']
    currency = input("Enter the currency (FRW, Naira, USD, EUR): ").upper()
    # Validate currency input
    while currency not in valid_currencies:
        print("Invalid currency. Please enter one of the following: FRW, Naira, USD, EUR.")
        currency = input("Enter the currency (FRW, Naira, USD, EUR): ").upper()
    
    # Create a BudgetTracker instance
    budget_tracker = BudgetTracker(initial_balance, is_initial_income, currency)

    while True:
        # Get transaction details from user
        transaction_amount = float(input("Enter the transaction amount: "))
        is_income = input("Is this an income? (y/n) ").lower() == 'y'
        # Add the transaction to the budget tracker
        budget_tracker.add_transaction(Transaction(transaction_amount, is_income))

        # Ask if the user wants to enter more transactions
        more_transactions = input("Do you want to enter more transactions? (y/n) ").lower()
        if more_transactions != 'y':
            # Display all transactions and summary before exiting
            budget_tracker.display_transactions()
            break

if __name__ == "__main__":
    main()

            budget_tracker.display_transactions()
            break

if __name__ == "__main__":
    main()

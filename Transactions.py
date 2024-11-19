class Transaction:
    def __init__(self, amount, is_income):
        self.amount = amount
        self.is_income = is_income

    def apply_to_balance(self, balance):
        if self.is_income:
            return balance + self.amount
        else:
            return balance - self.amount

class BudgetTracker:
    def __init__(self, initial_balance, is_initial_income, currency, user_name):
        self.balance = self.initialize_balance(initial_balance, is_initial_income)
        self.transactions = []
        self.total_income = 0
        self.total_expenses = 0
        self.currency = currency
        self.user_name = user_name

    def initialize_balance(self, initial_balance, is_initial_income):
        if is_initial_income:
            return initial_balance
        else:
            return -initial_balance

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.balance = transaction.apply_to_balance(self.balance)
        if transaction.is_income:
            self.total_income += transaction.amount
        else:
            self.total_expenses += transaction.amount

    def display_transactions(self):
        print(f"Hello, {self.user_name}! Here are your budget transactions:")
        print("Transactions:")
        for transaction in self.transactions:
            print(f"{'Income' if transaction.is_income else 'Expense'}: {transaction.amount} {self.currency}")
        print(f"Total Income: {self.total_income} {self.currency}")
        print(f"Total Expenses: {self.total_expenses} {self.currency}")
        if self.balance < 0:
            print(f"You're in a deficit of {abs(self.balance)} {self.currency}")
        else:
            print(f"You're in a surplus of {self.balance} {self.currency}")
        print(f"Thank you, {self.user_name}! Be sure to check out our other resources and remember to rate your experience with us.")

def main():
    user_name = input("What is your name? ")
    initial_balance = float(input("Enter the initial balance: "))
    is_initial_income = input("Is the initial balance an income? (y/n) ").lower() == 'y'
    
    # Restrict currency options
    valid_currencies = ['FRW', 'NAIRA', 'USD', 'EUR']
    currency = input("Enter the currency (FRW, Naira, USD, EUR): ").upper()
    while currency not in valid_currencies:
        print("Invalid currency. Please enter one of the following: FRW, Naira, USD, EUR.")
        currency = input("Enter the currency (FRW, Naira, USD, EUR): ").upper()
    
    budget_tracker = BudgetTracker(initial_balance, is_initial_income, currency, user_name)

    while True:
        transaction_amount = float(input("Enter the transaction amount: "))
        is_income = input("Is this an income? (y/n) ").lower() == 'y'
        budget_tracker.add_transaction(Transaction(transaction_amount, is_income))

        more_transactions = input("Do you want to enter more transactions? (y/n) ").lower()
        if more_transactions != 'y':
            budget_tracker.display_transactions()
            break

if __name__ == "__main__":
    main()

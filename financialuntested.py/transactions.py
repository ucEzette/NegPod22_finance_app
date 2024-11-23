class Transaction:
    def __init__(self, amount, is_income):
        self.amount = amount
        self.is_income = is_income

    def apply_to_balance(self, balance):
        return balance + self.amount if self.is_income else balance - self.amount

class BudgetTracker:
    def __init__(self, initial_balance, is_initial_income, currency):
        self.balance = initial_balance if is_initial_income else -initial_balance
        self.transactions = []
        self.total_income = 0
        self.total_expenses = 0
        self.currency = currency

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.balance = transaction.apply_to_balance(self.balance)
        if transaction.is_income:
            self.total_income += transaction.amount
        else:
            self.total_expenses += transaction.amount

    def display_transactions(self):
        print("\nTransactions:")
        for t in self.transactions:
            print(f"{'Income' if t.is_income else 'Expense'}: {t.amount} {self.currency}")
        print(f"Balance: {self.balance} {self.currency}\n")

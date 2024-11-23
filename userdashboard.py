class Dashboard:
    def __init__(self):
        self.features = ["Accounts", "Transactions", "Budgets", "Reports"]
        self.transactions = []
        self.current_balance = 0.0

    def display_options(self): 
        print("Welcome to the User Dashboard!")
        for feature in self.features:
            print(f"- {feature}")

    def navigate_to_feature(self, feature_name):
        if feature_name in self.features:
            print(f"Navigating to {feature_name} feature...")
            return True
        print(f"Invalid feature: {feature_name}")    
        return False

    def add_transaction(self, amount, description):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Invalid transaction amount. Please provide a positive number.")
            return
        if not description:
            print("Transaction description cannot be empty.")
            return

        self.transactions.append({
            'amount': amount, 
            'description': description
        })
        self.update_dashboard()

    def update_dashboard(self):
        self.current_balance = sum(t['amount'] for t in self.transactions)
        print(f"Current Balance: ${self.current_balance:,.2f}")
    
    def view_transactions(self):
        if not self.transactions:
            print("No transactions available.")
            return
        print("\nTransaction History:")
        for i, transaction in enumerate(self.transactions, 1):
            print(f"{i}. {transaction['description']} - ${transaction['amount']:,.2f}")


     

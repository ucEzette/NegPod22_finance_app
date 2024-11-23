#!/bin/bash

# Initialize data storage
transactions=()
accounts=()

# Function to add a transaction
add_transaction() {
    local account_name="$1"
    local amount="$2"
    local category="$3"
    local transaction_date="$4"
    transactions+=("$account_name:$amount:$category:$transaction_date")
}

# Function to add an account
add_account() {
    local account_name="$1"
    local balance="$2"
    accounts+=("$account_name:$balance")
}

# Generate monthly spending report
generate_monthly_spending_report() {
    declare -A spending
    for transaction in "${transactions[@]}"; do
        IFS=":" read -r account_name amount category transaction_date <<< "$transaction"
        if [[ "$category" != "income" ]]; then
            spending["$category"]=$((spending["$category"] + amount))
        fi
    done

    echo "Monthly Spending by Category:"
    for category in "${!spending[@]}"; do
        printf "%s: $%d\n" "$category" "${spending[$category]}"
    done
    echo
}

# Generate net worth report
generate_net_worth_report() {
    echo "Net Worth Distribution by Account:"
    total_net_worth=0
    for account in "${accounts[@]}"; do
        IFS=":" read -r account_name balance <<< "$account"
        printf "%s: $%d\n" "$account_name" "$balance"
        total_net_worth=$((total_net_worth + balance))
    done
    echo "Total Net Worth: $${total_net_worth}"
    echo
}

# Sample Data
add_transaction "Checking" 200 "Groceries" "2024-11-01"
add_transaction "Checking" 50 "Transportation" "2024-11-03"
add_transaction "Savings" 500 "income" "2024-11-05"
add_transaction "Checking" 70 "Entertainment" "2024-11-07"

add_account "Checking" 300
add_account "Savings" 1200

# Generate Reports
generate_monthly_spending_report
generate_net_worth_report


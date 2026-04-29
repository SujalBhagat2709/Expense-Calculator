def calculate_savings(income, expenses):
    
    total_expense = sum(expenses)
    
    return income - total_expense


if __name__ == "__main__":
    
    income = 5000
    expenses = [1200, 800, 500]
    
    print("Savings:", calculate_savings(income, expenses))
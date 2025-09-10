# finance_calculator.py

# Prompt the user for their monthly income
income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Project annual savings with 5% interest
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print results
print("Your monthly savings are:", monthly_savings)
print("Your projected annual savings after interest are:", annual_savings)

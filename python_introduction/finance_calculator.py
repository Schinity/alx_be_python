income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses
annual_savings_with_interest = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings_with_interest}.")

# write a program to calculate how many year's to remaining to live 90 year

current_year = int(input("Enter your current age :: "))
remaining_years = 90 - current_year
remaining_days = remaining_years * 365
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52

print(f"You have left {remaining_days} days or {remaining_weeks} weeks and {remaining_months} months to complete 90 years ")

# write a program to calculate how many year's to remaining to live 90 year

current_year = int(input("Enter your current age :: "))

days = current_year * 365
remaining_days = (90 * 365) - days
months = current_year * 12
remaining_months = (90 * 12) - months
weeks = current_year * 52
remaining_weeks = (90 * 52) - weeks

print(f"You have left {remaining_days} days or {remaining_weeks} weeks and {remaining_months} weeks to complete 90 years ")


# create a Tip Project 
bill = float(input("What was the total bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill_split = int(input("How many people to split the bill? "))
total_bill = bill * percentage / 100
total_tip = (total_bill + bill) / bill_split
print("Each person should pay: ", round(total_tip,2))

# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
pizza_size = input("What size of pizza do you want ? S, M, Or L : ")
papperoni = input("Do you want papperoni ? Y or N : ")
extra_cheese = input("Do you want extra cheese ? Y or N : ")

bill = 0

if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
else:
    bill += 25

if papperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3
    

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is : ${bill}")

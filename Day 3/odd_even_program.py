# Write a program that works out whether if a given number is an odd or even number.

number = int(input("Enter a number :: "))

if number % 2 == 0:
    print(f"This is an even number {number}.")
else:
    print(f"This is an odd number {number}.")

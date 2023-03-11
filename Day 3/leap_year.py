# Write a program that works out whether if a given year is a leap year.

leap_year = int(input("Enter a year :: "))

if leap_year % 4 == 0 :
    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            print(F"{leap_year} is a leap year.")
        else: 
            print(F"{leap_year} is not a leap year.")
    else:
        print(F"{leap_year} is leap year.")
else:
    print(F"{leap_year} is not a leap year.")

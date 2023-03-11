# height required greater than equal 120 cm to enjoy rollercoster ride

height = int(input("Enter a height ::  "))

if height >= 120:
    print("Enjoy a ride !!! ")
    age = int(input("What is your age :: "))
    if age <= 12:
        print("you pay only $5.")
    elif age < 18:
        print("you pay only $7.")
    else:
        print("you pay only $12")
else:
    print("You are not eligible for this ride.")

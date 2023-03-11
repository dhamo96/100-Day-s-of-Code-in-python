# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
weight = float(input("What's your weight ? "))
height = float(input("What's your height ? "))

bmi = round(weight / height ** 2)

if bmi > 18 and bmi < 25 :
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
else:
    print(f"Your BMI is {bmi}, you are underweight.")

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

weight = float(input("What's your weight ? "))
height = float(input("What's your height ? "))

bmi = weight / height ** 2
print(int(bmi))

# You are going to write a program that will select a random name from a list of names. 

# The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List called names. 

# For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

import random

names = input("Give me everybody's names, separated by a comma. ")

name_list = names.split(", ")
random_names = random.randint(0,len(name_list))
random_name = name_list[random_names]

print(random_name + " is going to buy the meal today!")

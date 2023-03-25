# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."


name1 = input("Enter your name :: ")
name2 = input("Enter your name :: ")

combined_string = name1 + name2
lower_case = combined_string.lower()
str1 = "true"
str2 = "love"

true = 0
for i in str1:
    true1 = lower_case.count(i)
    true += true1

love = 0
for j in str2:
    love1 = lower_case.count(j)
    love += love1

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

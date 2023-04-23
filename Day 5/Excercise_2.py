# write a program that calculates the highest score from a List of scores.

student_scores = input("Enter a student scores. ").split()
highest_scores = 0
for score in student_scores:
    if int(score) > highest_scores:
        highest_scores = int(score)
print(f"The highest score in the class is: {highest_scores}")

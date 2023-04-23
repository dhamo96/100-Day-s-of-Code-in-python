# write a program to addition of even numbers.

number = int(input("Enter a number :: "))

total = 0
for i in range(2, number+1, 2):
    # if i % 2 == 0:
    total += i
print(total)

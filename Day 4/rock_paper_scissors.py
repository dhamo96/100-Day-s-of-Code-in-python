import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choices = int(input("Enter you choice 0 for rock, 1 for paper and 2 for scissors. \n"))
# print(user_choices)
if user_choices >= 3 or user_choices < 0:
    print("You entered a invalid number !")
else:
    print(game_images[user_choices])

    computer_choice = random.randint(0,2)
    print(f"Enter a computer choice : ")
    print(computer_choice)
    print(game_images[computer_choice])
    
    if user_choices == 0 and computer_choice == 2:
        print("You win !")
    elif computer_choice > user_choices:
        print("You lose !")
    elif user_choices > computer_choice:
        print("You win !")
    else:
        # user_choices == computer_choice:
        print("It's draw !")

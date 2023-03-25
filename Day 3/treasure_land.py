print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("Welcome to treasure Island.")

print("You mission is to find the treasure.")


ch = 'Y'

while ch == 'Y' or ch == 'y':
	side = input('You are at a crossroad, where do you want to go? type "left" or "right".  ').lower()
	if side == 'left':
		choice2 = input('You are a near in lake type "wait" for boat or "swim" to across. ').lower()
		if choice2 == 'wait':
			choice3 = input('Which color door you want to go ahead type "blue","yellow" or "red". ').lower()
			if choice3 == 'yellow':
				print("Congratulations! you have won the amazing treasure Island game !!!!")
			elif choice3 == 'red':
				print("Game Over better luck next time !")
			elif choice3 == 'blue':
				print("Game Over better luck next time !")
			else:
				print("You enter wrong option")
		elif choice2 == 'swim':
			print("Game Over better luck next time !")		
		else:
			print("You enter wrong option")
	elif side == 'right':
		print("Game Over better luck next time !")
	else:
		print("You enter wrong option")
	ch = input("If you want to continue press 'Y' for yes or press 'N' for no ").lower()

if ch == 'n':
	print("Thank you for participating in Treasure Island Game.")

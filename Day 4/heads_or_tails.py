# You are going to write a virtual coin toss program. 

# It will randomly tell the user "Heads" or "Tails".

# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

# There are many ways of doing this. 

# But to practice what we learnt in the last lesson, 

# you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

import random

# Use randint function for random coins switches
sides = random.randint(0,1)

# Check sides for heads and tails
print("Head" if sides == 1 else "Tail")

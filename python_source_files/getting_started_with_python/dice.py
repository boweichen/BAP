"""
Dice game
"""

import random

#Generate a random number from 0 to 1
num = random.random()
print(num) 

#Create the player class
class Player():
	def __init__(self, name, army: int):
		self.name = name
		self.army = army

#Start two players
amy = Player(name = "Amy", army = 5)
tom = Player(name = "Tom", army = 4)

#Conflict
amy_score = 0
for i in range(amy.army):
    amy_score += random.random()

tom_score = 0
for i in range(tom.army):
    tom_score += random.random()

print(f"Amy has a score of {amy_score} and Tom scores {tom_score}.")

#Score function
def score(player):
	player_score = 0
	for i in range(player.army):
	    player_score += random.random()
	return player_score

#Announce the winner
amy_score = score(amy)
tom_score = score(tom)

if amy_score == tom_score:
	print("Nobody wins.")
elif amy_score > tom_score:
	print("Amy wins.")
else:
	print("Tom wins.")
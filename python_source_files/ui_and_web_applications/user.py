"""
The User class
"""

# class User():
# 	def __init__(self, f_name, l_name, gender):
# 		self.f_name = f_name
# 		self.l_name = l_name
# 		self.gender = gender

"""
The User class modified for simulation
Comment out the old class above
Parameters
games = 100
money = 100
initial_bet = 1
"""

class User():
	def __init__(self, games, money, bet):
		self.games = games
		self.money = money
		self.bet = bet
"""
Roulette and gambler's ruin
"""
#=========================================================================================================
#NumPy Random
#=========================================================================================================
import numpy as np
import matplotlib.pyplot as plt

#Random integers
#Note low is inclusive to high is exclusive
spin = np.random.randint(0, 37)

#Test gambling strategy: bet on even numbers 
#and double bet after each loss

#Parameters
games = 100
money = 100
initial_bet = 1


def betting(money, games = 100, initial_bet = 1):
    #Player's position
    position = np.zeros(games + 1)
    position[0] = money
    #Initial bet
    bet = initial_bet
    idx = 0
    while money > bet and idx < games:
        #Spin the wheel
        spin = np.random.randint(0, 37)
        #Update index
        idx += 1
        if spin % 2 == 0 and spin != 0:
            money += bet
            bet = initial_bet
        else:
            money -= bet
            bet *= 2
        #Update position
        position[idx] = money
    return position

#Play game
position = betting(money = 1000, games = 5000)       

plt.plot(position)
plt.savefig('DW_position.png')
plt.show()

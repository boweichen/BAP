"""
Roulette and gambler's ruin
"""
import numpy as np
import matplotlib.pyplot as plt

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



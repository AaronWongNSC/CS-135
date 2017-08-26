'''
Title: Roulette Simulator
Author: Aaron Wong

Description: This is just a simple roulette simulator for my CS 135 class.

'''

import random

def spin():
    ball = random.randint(1,38)
    if ball == 37:
        return 'green', '0'
    elif ball == 38:
        return 'green', '00'
    elif ball in [2, 4, 6, 8, 10,
            11, 13, 15, 17, 20, 22,
            24, 26, 28, 29, 31, 33, 35]:
        return 'black', str(ball)
    else:
        return 'red', str(ball)

def payoutColor(bet, betColor, resultColor):
    if betColor == resultColor:
        if betColor == 'green':
            return 17*bet
        else:
            return bet
    else:
        return -bet

def payoutNumber(bet, betNumber, resultNumber):
    if betNumber == resultNumber:
        return 35*bet
    else:
        return -bet
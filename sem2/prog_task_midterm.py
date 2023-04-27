#Adam Sliwinski Midterm Programming Task 17/04/2023

import random

def introduction():
    '''
    __________________________
    |                          |
    |   Double Six Dice Game   |
    |__________________________|

    '''

def getRollCounter() -> int:

    '''
    Function rolls a pair of dice, and keeps rolling the dice again and again, until they roll a double six

    Returns:
        number of rolling attempts
    '''

    rollCounter = 0
    while True:
        rollCounter += 1
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 == 6 and dice2 == 6:
            return rollCounter

def printGameResults(name1: str, counter1: int, name2: str, counter2: int) -> None:
    '''
    Function prints the results of 'Double Six Dice Game' for 2 players

    Parameters:
        name1: name of the first player
        counter1: number of attempts of the first player until get DoubleSix    
        name2: name of the first player
        counter2: number of attempts of the first player until get DoubleSix
    Returns:
        None
    '''

    if counter1 > counter2:
        print('Player', name1, 'won, with ', counter1,' double dice rolls!!!')
    elif counter1 < counter2:
        print('Player', name2, 'won, with ', counter2, ' double dice rolls!!!')
    else:
        print('Draw! Both players used ', counter1,' attempts to roll a double six.')

def diceRollingGame():
    print(introduction.__doc__)
    name1 = input('Enter the name of player 1 ... ')
    name2 = input('Enter the name of player 2 ... ')
    counter1 = getRollCounter()
    counter2 = getRollCounter()
    print("==========")
    printGameResults(name1, counter1, name2, counter2)

diceRollingGame()
# Name: Garrett Dodd
# Class: CS 470 - AI
# Assignment 4 - Triple Threat
# Due Date: 9/5/2022
# Description: main method, loops the game method until dieGame.gameOver() returns false
# File Name: main.py

import dieGame as dieGame

def main():
    numDice = int(input('How many dice in this game? '))
    gameInstance = dieGame.dieGame(numDice)
    gameBool = 1
    while gameBool:
        gameBool = gameInstance.game()

if __name__ == '__main__':
    main()
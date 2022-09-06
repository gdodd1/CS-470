# Name: Garrett Dodd
# Class: CS 470 - AI
# Assignment 4 - Triple Threat
# Due Date: 9/5/2022
# Description: dieGame class, holds the init, gmae, roll, display, and gameOver methods
# File Name: dieGame.py

import random

class dieGame:
    dice = list()
    score = 0
    gameBool = 1

    def __init__(self, numDice):
        self.dice = [0] * numDice
        self.score = 0

    def game(self):
        rollInput = input('Roll the dice (Y/N)? ')
        status = 1
        if not self.gameBool:
            self.display()
            print('=> You Lose!')
            return 0
            
        if rollInput.capitalize() == 'Y':
            for i in range(len(self.dice)):
                if self.dice[i] == 'STUCK':
                    continue
                self.dice[i]= random.randint(1, 6)

            self.display()
            self.gameOver = self.roll()
            print(self.score)
            status = 1
        elif rollInput.capitalize() == 'N':
            if self.gameBool:
                print(f'\nYou win! Your score is: {self.score}')
                return 0
            else:
                self.display()
                print('=> You Lose!')
                return 0
        return status

    def display(self):
        for i in range(len(self.dice)):
            print(f'Die #{i+1}\t', end='')
        print('Sum')
        for i in range(len(self.dice)):
            print(f'{self.dice[i]}\t', end='')

    def roll(self):
        sum = 0
        for i in range(len(self.dice)):
            if self.dice[i] == 3 or self.dice[i] == 'STUCK':
                self.dice[i] = 'STUCK'
            else:
                self.score += self.dice[i]
                sum += self.dice[i]
        self.gameOver()
        return sum

    def gameOver(self):
        if len(set(self.dice)) == 1:
            self.gameBool = 0
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:12:59 2021

@author: Traftmine
"""

#the computer choose a number between 1 and a number x chosen by the user
import random as rm
import time as t

NUMBER_LIM = int(input("What's the limit number you're ok with? "))

Y = int(input("How many round do you wanna play? "))
X = 1
SCORE = Y
START = t.time()

#We create a loop, the user has to choose how many questions it wants.

while X <= Y:
    NUMBER_ONE = rm.randint(1, NUMBER_LIM)
    NUMBER_TWO = rm.randint(1, NUMBER_LIM)

#the computer's making a calculation and is collecting the user's answer

    CALCULATION = NUMBER_ONE*NUMBER_TWO

    print(NUMBER_ONE, "times", NUMBER_TWO)

    ANSWER = int(input("is equal to: "))

#the computer is checking if the answer is right

    if ANSWER == CALCULATION:
        print("Well done!")

    else:
        print("You're wrong, the answer was :", CALCULATION, "; keep going!")
        SCORE = SCORE-1

    X = X + 1

END = t.time()
TIME = round(END - START)

#we give the score to the user
print(SCORE, "on", Y)
print("In", TIME)
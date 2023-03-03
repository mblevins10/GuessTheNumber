# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 19:59:04 2023

@author: kayla
"""

import random

print("Welcome to the number guessing game please pick a number 1-100")
n = random.randrange(1,100)
guess = int(input("Please pick any number now:"))
while n!= guess:
    if guess < n:
        print("TOO LOW TRY AGAIN")
        guess = int(input("Pick again:"))
    elif guess > n:
        print("TOO HIGH!")
        guess = int(input("Pick again"))
    else:
        break
print("You got it right!")
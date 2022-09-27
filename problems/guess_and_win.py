# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 09:46:59 2021

@author: zahid
"""

#The program randomly generate an integer
# between 0 and 300,
# player inputs a number
# and system returns a
# hint from three choices,
# 'Too large', 'Too small' or
# 'Bingo'.

from random import randint
x=randint(0, 100)
print("Please guess a number between 0-100. You have 3 chance to win")
for count in range(3):
    plr_input=float(input("Please guess a number:"))
    if(plr_input==x):
        print("Bingo")
    elif(plr_input>x):
        print('Too large')
    elif(plr_input<x):
        print('Too small')
        
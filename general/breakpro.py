# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 10:17:43 2021

@author: zahid
"""

sumA =0
i = 1
while True:
    sumA += i
    print(sumA)
    i+=1
    print(i)
    if sumA > 10:
        break
print('i={},sum={}'.format(i, sumA))
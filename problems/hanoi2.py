# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 09:16:14 2021

@author: zahid
"""

def hanoi(a,b,c,n):
    if n==1:
        print(a,'->',c)
    else:
        hanoi(a,c,b,n-1)
        print(a,'->',c)
        hanoi(b,a,c,n-1)


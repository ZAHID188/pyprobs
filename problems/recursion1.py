# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 08:58:47 2021

@author: zahid
"""

def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(10))
    

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 08:55:06 2021

@author: zahid
"""
a=2 #global variable

def foo(x):
    global a
    print(a)
    a=3 #local variable
    print(a+x)
    
    
 
  

foo(3)
print(a)

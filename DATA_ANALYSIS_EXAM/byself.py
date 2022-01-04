

'''
#9 Numpy

Powerful ndarray object and ufunc() function
• Ingenious funciton
• Suitable for scientific computation like linear algebra and
random number handling
• Flexible and available general multi-dimension data structure
• Easy to connect with database

3*4 ndarray (row*column)
'''
import numpy as np
xArray = np.ones((3,4))
print(xArray)


'''
#8

set

'''

# aSet = set('hello')
# print(aSet)

# fSet = frozenset('hello')
# print(fSet)

# print(type(aSet))
# print(type(fSet))



'''
#7
How to remove the duplicate values in information form?
'''


# names = ['Wangdachui', 'Niuyun', 'Wangzi', 'Wangdachui', 'Linling', 'Niuyun']
# namesSet = set(names)
# print(namesSet)


'''
#6
Variable Length Keyword Parameter
Parameter type in Python
function:
• Position or keyword
parameter
• Only position parameter
• Variable Length Position
Parameter
• Variable length keyword
parameter with default value
'''

# def func(args1, *argst, **argsd):
#     print(args1)
#     print(argst)
#     print(argsd)
# print(func('Hello,','Wangdachui','Niuyun','Linling',a1= 1,a2=2,a3=3))



'''
#5
What’s the difference between the two kinds of search
operation?

'''
# stock = {'AXP': 78.51, 'BA': 184.76}
# # print(stock['AAA'])
# print(stock.get('AAA'))



'''
#4
An information dictionary is known as {'Wangdachui':3000,
'Niuyun':2000, 'Linling':4500, 'Tianqi':8000}， how to output the
name and salary of employee separately?

'''
# aInfo = {'Wangdachui': 3000, 'Niuyun': 2000, 'Linling': 4500, 'Tianqi': 8000}
# print(aInfo.keys())
# print(aInfo.values())
# for k, v in aInfo.items():
#     print(k, v)



'''
#3  list to dictionary
How to generate an employee information dictionary with
name and salary list?
'''

# names = ['Wangdachui', 'Niuyun', 'Linling', 'Tianqi']
# salaries = [3000, 2000, 4500, 8000]
# X=dict(zip(names,salaries))
# print(X)

'''
#2
How to set the default value of salary to be 3000？

'''

# aDict = {}.fromkeys(('Wangdachui', 'Niuyun', 'Linling', 'Tianqi'),3000)
# print(aDict)
# a=('zahid','rofiq','shofiq')
# bDict = {}.fromkeys(a,3000)
# print(bDict)

'''
#1
using 2 list  as a dictionary

'''
# names = ['Wangdachui', 'Niuyun', 'Linling', 'Tianqi']
# salaries = [3000, 2000, 4500, 8000]
# print(salaries[names.index('Niuyun')])
# print(names.index('Niuyun'))
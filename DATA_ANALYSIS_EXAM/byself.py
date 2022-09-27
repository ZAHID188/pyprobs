'''
#18 dataframe

Basic Feature
A form-like data structure
Have an ordered column（like index）
Can be considered as a set of Series sharing the same index

'''

# import pandas as pd
# import numpy as np

# data = {'name': ['Wangdachui', 'Linling', 'Niuyun'], 'pay': [4000, 5000, 6000]}
# frame = pd.DataFrame(data)
# print(frame)


# data2 = np.array([('Wangdachui', 4000), ('Linling', 5000), ('Niuyun', 6000)])
# print(data2)
# frame2 =pd.DataFrame(data2, index = range(4, 7), columns = ['name2', 'pay2'])
# print(frame2)

# print(frame.index)
# print(frame.columns)
# print(frame.values)

# print(frame['name'])
# print(frame.pay)
# print(frame.iloc[: 0, 0])  #(how many row ,how many column)
# print(frame.iloc[: 1, 0])
# print(frame.iloc[: 2, 0])
# print(frame.iloc[: 2, 1])


# print(frame.pay.max())
# print(frame.pay.min())



'''
#17
series

'''

# from pandas import Series
# import pandas as pd
# import numpy as np

# aSer = pd.Series([3,5,7],index = ['a','b','c'])
# print(aSer)
# print(np.exp(aSer))

# data = {'AXP':'86.40','CSCO':'122.64','BA':'99.44'}
# sindex = ['AXP','CSCO','BA','AAPL']
# aSer = pd.Series(data, index = sindex)
# print(aSer)



'''
#16
Ndarray calculation

'''

# import numpy as np
# aArray = np.array([(1,2,3),(4,5,6)])
# print("array=",aArray)
# print("sum",aArray.sum())
# print("sum axis=0",aArray.sum(axis =0))
# print("sum axis=1",aArray.sum(axis =1))
# print(" min",aArray.min()) #return value
# print(" argmax",aArray.argmax())  #return index
# print("mean",aArray.mean())
# print("varience",aArray.var())
# print("standard dev",aArray.std())


'''
#15
Ndarray Operations

'''
# import numpy as np
# aArray = np.array([(1,2,3),(4,5,6)])
# print(aArray[0:2])
# # print(aArray[:,[0,1]])
# print(aArray[1,[0,1]])

# print(aArray.shape)
# bArray = aArray.reshape(3,2)
# print(bArray)

# aArray.resize(3,2)
# print(aArray)


# bArray2 = np.array([1,3,7])
# cArray2 = np.array([3,5,8])
# print(np.vstack((bArray2, cArray2)))
# print(np.hstack((bArray2, cArray2)))

# aArray = np.array([(5,5,5),(5,5,5)])
# bArray = np.array([(2,2,2),(2,2,2)])
# cArray = aArray * bArray
# print(cArray)

# aArray += bArray
# print(aArray)


'''
#14
What is ndarray?
N-dimensional array
– Basic data type in NumPy
– Elements are of the same type
– With another name array
– Reduce memory cost and
improve the computational
efficiency
– Powerful functions


Ndarray attributes
ndarray
– Dimensions are called axes, the number of
axes is rank.
– Basic attributes
• ndarray.ndim（rank）
• ndarray.shape（dimension）
• ndarray.size（total size）
• ndarray.dtype（type of element）
• ndarray.itemsize（size of item(in byte)）
'''
# import numpy as np
# aArray = np.array([1,2,3])
# print(aArray)

# bArray = np.array([(1,2,3),(4,5,6)])
# print(bArray)
# print(np.arange(1,5,0.5))
# print(np.random.random((2,2)))
# print(np.linspace(1, 2, 10, endpoint=False))
# print(np.ones([2,3]))
# print(np.zeros((2,2)))
# print(np.fromfunction(lambda i,j:(i+1)*(j+1), (9,9)))





'''
#13  pandas
Feature:
• Based on SciPy and NumPy
• Efficient Series and DataFrame structure
• Powerful Python library for scalable data processing
• Efficient solution for large dataset slides
• Optimized library function to read/write many types of
files, like CSV and HDF5

'''


'''
#12  Matplotlib
Feature:
• Based on NumPy
• 2-dimensional graph library to rapidly generate all
kinds of graphs
• Pyplot module provides MATLAB-like interface.

'''



'''
#10 SciPy
• Key package for scientific computation in Python and it is based
on NumPy. It includes richer functions and methods than NumPy
and it probably has stronger function when they have the same
functions or methods.
• Efficiently compute NumPy matrix to benefit collaboration
between NumPy and SciPy.
• Toolbox to deal with different fields in scientific computation
with modules including interpolation, integration, optimization
and image processing.

'''

# import numpy as np
# from scipy import linalg
# arr = np.array([[1,2],[3,4]])
# print(arr)
# print(linalg.det(arr))
# fruits=["mango","banana","lichy"]
# arr2=np.array([fruits,[1,2,4]])
# print(arr2)

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
# import numpy as np
# xArray = np.ones((3,4))
# print(xArray)


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
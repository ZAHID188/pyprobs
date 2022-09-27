```
# Which of the following is the order of applying 
# object-oriented concept in programming

# A.class defining — use attributes or methods through
#  the instance —instance creating

# B.instance creating — use attributes or 
# methods through the instance — class defining

# C.instance creating — class defining — use attributes
#  or methods through the instance

# D.class defining — instance creating — use attributes 
# or methods through the instance






'''
#46
ask("Do you like SciPy?")
Do you like SciPy? What?
yes or no

Do you like SciPy? en
yes or no
Sorry, you have tried too many times.

请输入答案：（             ）

36．As for the function ask(), 
please fill in the following blank to make the operation successful
under the context in the question. Please fill in the first blank.'''

# def ask(prompt, hint = "yes or no", chance = 2):
#     while chance > 0:
#         answer = input(prompt)
#         if answer.lower() in ('y', 'yes'):
#             print("Thank you")
#             return True
#         if answer.lower() in ('n', 'no'):
#             print("Why not ")
#             return False
#         else:
#             chance -= 1
#             print(hint)
#     print("Sorry, you have tried too many times.")
# ask("asdad?")



'''
#45
​The list “fruits” keeps the names of all kinds of fruit on sale
 in alphabetical order, for example, 
​fruits = ['apple', 'banana', 'cherry','banana', 'peach', 'pear','peach', 'cherry' ]. 
​Define a function to count how many times each kind of fruit is sold. 
​The result is expected to save in a dictionary in the form of 
{'pear': 1, 'banana': 2, 'cherry': 2, 'peach': 2, 'apple': 1}.'''
# d = {}
# fruits= ['apple', 'banana', 'cherry','banana', 'peach', 'pear','peach','cherry' ]
# fruits_set = set(fruits)
# # print(fruits_set)
# for item in fruits_set:
#   d[item] = 0
#   for i in range(len(fruits)):
#     if item == fruits[i]:
#       d[item] += 1
# for item in fruits:
#   d[item] = fruits.count(item)
# print(d)


# or

# d = {}
# fruits= ['apple', 'banana', 'cherry','banana', 'peach', 'pear','peach','cherry' ]
# for item in fruits:
#     d[item] = d.setdefault(item, 0) + 1
# print(d)



# or

# d = {}
# fruits= ['apple', 'banana', 'cherry','banana', 'peach', 'pear','peach','cherry' ]
# for item in fruits:
#     d[item] = d.get(item, 0) + 1
# print(d)



'''
#44
‌In a statement like “quotesdf = quotesdf.drop(['date'], axis = )”,
 the argument of “axis” can only be 0 or 1. 
‌“0” represents an operation of a certain column in DataFrame;
  “1” represents an operation of a certain row in DataFrame.

axis   --		{0 or ‘index’, 1 or ‘columns’}
Default Value: 0	Required
'''


# import pandas as pd
# data=pd.read_csv('data.csv')
# aDF=pd.DataFrame(data)
# quotesdf=aDF.drop([2], axis =0)
# print(aDF)
# print(quotesdf)


'''
#43
In Python, if a file is opened with mode “r+”,
 the file pointer will be at the beginning of the file. '''

# f = open('test.txt', 'r+')
# print(f.tell())
# f.write('hahaha')
# print(f.tell())
# print(f.read())



'''
#42
The built-in functions of the dictionary in Python don’t
 include append() function.
 If a dictionary needs to be update, the update() function can be used.
'''
# dic=dict()
# dic["zahid"]=5
# dic["zahid"]=6
# dic["zahid1"]=6+1

# # dic.update("zahid")=
# print(dic)


'''
#41
“for” statement in Python can be used to iterate on any sequence,
 for example, list, string and tuple.
'''
# lst=[2,4,5,6,7]
# tup=(2,4,5,6,70)
# st="zahid"
# for x in lst:
#   print(x)
# for x in tup:
#   print(x)
# for x in st:
#   print(x)




'''
#40
Executing range(N1, N2) will generate a total of N2-N1+1 integers.
'''
# for x in range(0,15):
#   print(x)



'''
#39
If we want to insert x into
 a list “lst”, we can use “lst.append(x)
  or “lst[len(lst):]=[x].

'''

# lst=[]
# lst.append("x")
# lst[len(lst):]=["y"]

# print(lst)
# print(lst[1])



'''
#38
If a function is defined as below, which of the following 
input can yield a result of 21?
​A.compute([3, 2, 1])  B.nums = [1, 2, 3]; compute(nums)
C.compute([3, 3])    D.nums = (3, 3); compute(*nums)'''

# def compute(*numbers):
#   s = 1
#   for n in numbers:
#     s = s * n + n
#   return s
# print(compute([3, 2, 1]))
# nums = [1, 2, 3]
# print(compute(nums))
# print(compute([3, 3]))
# nums2 = (3, 3)
# print(compute(*nums2))


'''
#37
​Given a list aList and a tuple bTuple, which of the
 following statement regarding usage of functions and objects is NOT correct?
A.aList.sort()   B.sorted(bTuple)   C.bTuple.sort()  D.sorted(aList)'''

# alist=[1,2,5,3,6,8,7]
# btuple=(3,4,2,1,6)
# alist.sort()
# print(alist)
# print(sorted(btuple))
# # btuple.sort()
# print(sorted(alist))


'''
#36
The core Scipy packages are Numpy, 
SciPy library, Matplotlib, IPython,
Sympy, and Pandas.
among which NumPy is an essential package for high performance 
computing and analysis, serving as a base to construct other 
advanced tools on top of it.
'''




'''
#35
DataFrame can be regarded as a Series set sharing the same index.
 '''

# import pandas as pd
# data = {"calories": [420, 380, 390],
#         "duration": [50, 40, 45]}
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
# print(df) 
# print(df.loc[2]) 
# print(df.loc[[0, 1]])

# df2 = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df2)
# print(df2.loc["day2"])

# df3 = pd.read_csv('data.csv')
# print(df3)




'''
#34
B.ndarray is an object of multidimensional array;  
"import numpy as np; matrix = np.ones((3, 4))" 
creates one 3*4 ndarray of two-dimensional(2D) array.
'''
# import numpy as np
# matrix = np.ones((3, 4))
# print(matrix)


'''
#33
A.Series can be regarded as enhancement of original dictionary 
of Python in pandas, so the index of each element inside
 a Series object can not be the same as any other one.。
'''

# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a)
# myvar2 = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)
# print(myvar2)
# print(myvar[0])
# print(myvar2["y"])










# print((1, 2, 3, 4) < (1, 2, 4) )
'''
#32
Open and read a text file,
with “f = open('test.txt', 'r+')”; f.read(); 
the function “read” without any argument is to
read the entire text file and return the contents.
'''


# f = open('test.txt', 'r+')
# print(f.read())
# print(f.seek(5))




'''
#31
A.For string formatting, 
the result of '{:.2f}'.format(math.pi) is the same
 as that of '%.2f' % math.pi. 

'''


# import math
# x=math.pi
# print("hi this {:.2f}".format(x))
# print("%.2f"%x)


'''
#30
Fibonacci number list

'''

# def fib(n):
#   a, b = 0, 1
#   count = 1
#   while count  < n:
#     a, b = b,a+b   #swapping 2 values 
#     count = count + 1
#     print(a,b,(a+b))
# fib(5)



# def fib(n):
#   a, b = 0, 1
#   count = 1
#   while count  < n:
#     c=a+b
#     a=b ,b = c
#     count = count + 1
#     print(c)

# fib(5)


'''
#29  
  ** -- is keyword variable length argument
  input:person("zahid",age="23",division="dhaka",city="kishoreganj")

  output: zahid
          {'age': '23', 'division': 'dhaka', 'city': 'kishoreganj'}
'''

# def person(name,**data):
#   print(name)
#   print(data)
#   for (i,j) in data.items():
#     print(i,j)
# person("zahid",age="23",division="dhaka",city="kishoreganj")




'''
#28
  * --variable length argument
  input:person("zahid","23","dhaka","kishoreganj")

  output: zahid
          ('23', 'dhaka', 'kishoreganj')

'''

# def person(name,*data):
#   print(name)
#   print(data)
# person("zahid","23","dhaka","kishoreganj")



'''
#27
In Python, if a function returns more than 1 value, the system will, 
by default, process these value(s) into a dictionary. (false)
'''
# def test():
#   return 'abc', 100
# print(test())





'''
#26
The recursive function runs much faster than the iterative one. The reason is because in the latter, for each item, a CALL to the function st_push is needed and then another to st_pop .
In the former, you only have the recursive CALL for each node.


'''



'''
#25
A function in Python will have one and only one return statement. (FALSE)


'''

# def my_abs(number):
#     if number > 0:
#         return str(number) +'positive'
#     elif number < 0:
#         return str(number) +'negetive'
# print(my_abs(25))
# print(my_abs(-25))



'''
#24
In Python, the value of default argument may be modified.

team("FemCode", "Edpresso") --FemCode and  Edpresso are argument

def team(name, project): --here name and project are the parameter
'''
# def team(name, project): 
#     print(name, "is working on an", project)
    
# team("FemCode", "Edpresso")

# def find_square(integer1=2):
#     result = integer1 * integer1
#     return result
# print(find_square(5))


'''
#23
In Python, the “return”statement in 
functions can return many values in form of “tuple”. 
'''

# def zahid():
#   a="shorif"
#   b="zahid"
#   c="alex"
#   y=(a,b,c)
#   return y
# print(zahid())





'''
#22
file readline seek tell

Life is short, you need Python.
Simple is better than complex.
complex better than 

readline will read every line with one by one 
#1
 1st time fp.readline()  == Life is short, you need Python.
 2nd time fp.readline()  == Simple is better than complex.
 3rd time fp.readline()  == complex better than

 #2
  print(fp.readline())   === b'Life is short, you need Python.\r\n'
  print(fp.tell())       === 33     ---- (means 32 char in privious line now index is at 33)
  print(fp.readline())   === b'Simple is better than complex.\r\n'
  print(fp.tell())       === 65  
  print(fp.readline())   === b'complex better than'
  print(fp.tell())       === 84


'''


# with open('test.txt', 'rb+') as fp:
  #1
  # print(fp.readline())  
  # print(fp.readline())
  # print(fp.readline())
  # fp.close()

  #2
  # print(fp.readline())
  # print(fp.tell())
  # print(fp.readline())
  # print(fp.tell())
  # print(fp.readline())
  # print(fp.tell())
  # fp.close()

  # fp.seek(33,0)    # (index of the particular line , line number after this index line )
  # print(fp.readline())
  # fp.seek(0,0)
  # print(fp.readline())
  # fp.seek(33,0)
  # print(fp.readline())
  # fp.close()

 



'''
#21
When an element is accessed in loops in sequences,
for acquiring the index of element simultaneously, 
it is feasible to use the function “enumerate()”,
like “for x in enumerate(lst)”.
'''

# x=[1,2,3,4,5,6,7,8]
# print(enumerate(x))
# for i in enumerate(x):
#   print(i)
#   # print(i[0])



'''
#20
unhashable type: 'list
'''

# x=dict()
# x["pen"]=5

# z=('pencil')
# x[z]=2

# y=["note"]
# # x[y]=4   list is unhashable
# print(x)

'''
#19
To iterate sequence elements in the reverse order,
 it is feasible to apply the function “reversed()” to that sequence.
For example, for i in reversed(lst).
'''

# x=[1,2,3,4,5,6,7,8]
# for i in reversed(x):
#   print(i)




'''
#18
It’s possible to iterate the list and modify the list itself 
at the same time, for example, the code below:
'''
# words = ['I','love','Python']
# words.insert(3,"asd")
# print(words)
# for w in words:
#   print(w)
#   if len(w) > 4:
#     words.insert(0, w)



'''
#17
To iterate a dictionary, the function “items()”
may be used to simultaneously retrieve values of “key, value”, 
for example, for k, v in scores.items().

'''


# scores = {'Jack': 90, 'Mike': 80, 'Jay': 85, 'Bill': 60} 
# print(scores.items())
# for k, v in scores.items():
#   print(k,v)



'''
#16
comparison in dictionary,del dict,sorted keys

'''

# scores = {'Jack': 90, 'Mike': 80, 'Jay': 85, 'Bill': 60} 
# s = dict(Jack=90, Mike=80, Jay=85, Bill=60)
# print(scores == s)

# scores = {'Jack': 90, 'Mike': 80, 'Jay': 85, 'Bill': 60}
# print(len(scores))
# del(scores['Bill']) 
# print(len(scores))

# scores = {'Jack': 90, 'Mike': 80, 'Jay': 85, 'Bill': 60}
# print(sorted(scores.keys()))

# scores = {'Jack': 90, 'Mike': 80, 'Jay': 85, 'Bill': 60}
# scores['Bill']=345
# print(scores) 
  





'''
#15
set in list ,remove,del ,sort

basket and fruit

'''

# basket = ['apple', 'banana', 'apple', 'orange'] 
# fruit = set(basket)
# print(len(fruit))
# print("basket",basket)
# print("fruits:",fruit)

# l = [1, 2, 3, 4, 5]
# del(l[2:4])
# print(l)

# basket = ['apple', 'banana', 'apple', 'orange']
# fruit = set(basket);  
# fruit2 = set(['apple', 'melo'])
# print(len(fruit | fruit2))
# # print(fruit,fruit2)
# # print(fruit2|fruit)
# # print(fruit|fruit2)


# l = [2, 1, 3, 5, 4]
# l.remove(3)
# l.sort(); 
# print(l)



'''
#14
A.l = [1, 2, 3, 4]; l.pop(); then l.index(3) is 2.
B.l = [1, 2, 3, 4]; l.rerverse(); then l[1] is 3.
C.l = [1, 2, 3, 4]; l.pop(1); then l is [1, 3, 4].
D.l = [1, 2, 3, 4]; l.insert(2, -1); then l is [1, 2, -1, 4].


'''

# l = [1, 2, 3, 4]
# # l.pop()
# # print(l.index(3))

# # l.reverse()
# # print(l[1])

# # l.pop(1)

# l.insert(2,-1)

# print(l)




'''
#13
Do you like Python?
 
'''

# def ask(prompt = "Do you like Python? ", hint = "yes or no"):
#     while True:
#         answer = input(prompt)
#         if answer.lower() in ('y', 'yes'):
#             print("Thank you")
#             return True
#         if answer.lower() in ('n', 'no'):
#             print("Why not ")
#             return False
#         else:
#             print(hint)
# ask()



'''
#12
Operator “==” can be used to compare two lists.
'''
# x=["zahid","alex"]
# y=["shorif","rayhan"]
# print(x==y)


'''
#11
The “+” symbol may be used to join two lists.

'''
# x=["zahid","alex"]
# y=["shorif","rayhan"]
# print(x+y)




'''
#10
Lists in Python can be nested, to form a two-dimensional list.

'''
# z=["zahid","alex",["k","i","x"]]
# print(z[2][1])


'''
#9

Strings have indexes with themselves.
 For the variable word='Python', word[1] is the character
  “y”, but word[-1] will cause the display 'n' from the last
'''

# word='Python'
# print(word[1])
# print(word[-1]) 

 





'''
#8
Python Operator ‘+’ is to concatenate two strings. 

'''

# x="apple"
# y="mango"
# print(x+y+"important")





'''
#7
Given a string “apple”, the statement 3*”apple” will generate “3apple”.

'''

# x="apple"
# y=3*x
# print(y)


'''
#6
Single Quotation Mark	           |  Double Quotation Mark
Represented as ‘ ‘                 | 	Represented as ” “
Single quotes for anything that    |
 behaves like an Identifier.       |    Double quotes generally we used for text.
Single quotes are used for regular |
 expressions, dict keys or SQL.    |	Double quotes are used for string representation.
Eg. ‘We “welcome” you.’	           |    Eg. “Hello it’s me.”

'''
# wish = "Hello World!"
# print(wish)
# # hey = "AskPython says "Hi""   this is an error 
# # print(hey)
# famous ="'Taj Mahal' is in Agra."
# print(famous)
# a="YZU"
# b='YZU'
# print(type(a),type(b))

'''
#5
The symbol “\” may be used as the escape character. 
For example, both 'doesn\'t' and "doesn't" represent the string “doesn’t”.
'''

# print('doesn\'t')
# print("doesn't")





'''
#4
print('C:\file\name')
C:
  ile
ame
'''

# print('C:\file\name')



'''
#3
the backslash "\" is called  the escaped charecter
When assigning a string include single-quote mark or double-quote mark,
 operator ‘r’ can be used if escape character is not desired.

'''
# s = 'Hi\nHello'   #here   \n -- is a escape character 
# print(s)

# a = r'Hi\nHello'   # r means RAW string 
# print(a)

# c=r"Hi\xHello"
# print(c)


'''
#2
The result of 10/3 == 3 in Python 3.x is flase.
'''

# print(10/3==3)





'''
#1
Python supports augmented assignment operators like“+=” and “%=”.
'''

# z=10
# z+=7
# print(z)


# # Remainder or Modulo
# a = 23
# b = 3
# a %= b
# print('Remainder or Modulo = %d' %(a))
```
'''
In some contexts, like a return statement,
it is syntactically simpler to create a tuple than a list.
In other contexts, you might prefer a list.
If you want to use a sequence as a dictionary key,
you have to use an immutable type like a tuple or string.
If you are passing a sequence as an argument to a function,
using tuples reduces the potential for unexpected behavior due to aliasing.
'''

'''
Exercise 2: This program counts the distribution of
the hour of the day for each of the messages.
You can pull the hour from the “From” line by finding
the time string and then splitting that string into parts
using the colon character. Once you have accumulated the
counts for each hour, print out the counts, one per line,
sorted by hour as shown below.

'''

# fhand=open('mbox-short.txt')
# d0={}
# for line in fhand:
#   ref_line=line.rstrip()
#   if '@' in ref_line:
#     if ref_line.startswith('From'):
#       words=ref_line.split()
#       for word in words:
#         if ":" in word and "From" not in word:

#           if word[0:2] not in d0:
#             d0[word[0:2]]=1
#           else:
#             d0[word[0:2]] += 1
# print(d0)

# for (k,v) in (sorted([(k,v) for k,v in d0.items()])):
#   print(k,v)
# # if don't understand this two line comment avobe 2 line and 
# # comment out down below

# lst=[]
# for (k,v) in d0.items():
#   lst.append((k,v))

# lst.sort()
# for (k,v) in lst:
#   print(k,v)
   




'''
Exercise 1: Revise a previous program as follows: 
Read and parse the “From” lines and pull out the addresses
from the line.
Count the number of messages from each person using a dictionary.

After all the data has been read,
print the person with the most commits by creating
a list of (count, email) tuples from the dictionary. 
hen sort the list in reverse order and print out the 
person who has the most commits.

'''

# fhand=open('mbox-short.txt')
# d0={}
# for line in fhand:
#   ref_line=line.rstrip()
#   if '@' in ref_line:
#     if ref_line.startswith('From'):
#       d=ref_line.split()
#       # print(d[1])
#       if d[1] not in d0:
#         d0[d[1]]=1
#       else:
#         d0[d[1]] += 1
# # print(d0)
# # --------- list part
# lst=[]
# for (k,v) in d0.items():
#   lst.append((v,k))

# lst.sort(reverse=True)
# for (k,v) in lst:
#   print(v,k)
   

#2 same thing with one line
#  ---- anoteher short method  just comment out the from list part to the rest part  

# print(sorted([(v,k) for k,v in d0.items()],reverse=True))









'''
dictionary items are tuple
'''

# d = {'a':10, 'b':1, 'c':22}

# t = list(d.items())
# print(t)

# directory[last,first] = number


'''
random 
'''
#1
# t = tuple('lupins')
# print(t)


#2
# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# t = list()
# for word in words:
#     t.append((len(word), word))

# t.sort(reverse=True)

# res = list()
# for length, word in t:
#     res.append(word)

# print(res)

# m = [ 'have', 'fun' ]
# x, y = m
# print(type(x))
# print(x)



# d={'a':10,'c':22,'b':1}

# for key, val in list(d.items()):
#   print(val, key)



'''
counting and sorting

'''
#1 ---classic
# fhand = open('temp.txt')
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#       counts[word]=counts.get(word,0)+1

# li=[]
# for(k,v) in counts.items():
#   newtp=(v,k)
#   li.append(newtp)
# lst=sorted(li,reverse=True)
# for(k,v) in lst:
#   print(k,v)


#2 ---- new system
# d={'a':10,'c':22,'b':1}
# print(sorted([(v,k) for k,v in d.items()]))







# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()

# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1

# print(counts)

'''
sorting by the values

'''

# d={'a':10,'c':22,'b':1}
# temp=list()
# for (k,v) in d.items():
#   temp.append((v,k))
# print(temp)
# temp=sorted(temp,reverse=True)
# print(temp)


'''
sorting dictionary

'''
# d={'a':10,'c':22,'b':1}
# print(d.items())
# print(sorted(d.items()))
# for (k,v) in sorted(d.items()):
#   print(k,v)





'''
once i've created an tuples , i can't alter it's content

'''

# x=('gellen','sally','joseph')
# print(x)
# print(x[2])

# z=["zahid","shorif"]
# z[1]="raily"
# print(z[1])


'''

we can't reassign in str and tuple

'''

# # y='asda'
# # y[2]="d"
# # print(y)

# y=('asda',"asdas")
# y[2]="d"
# print(y)


'''

AttributeError: 'tuple' object has no attribute 'sort'
same for -=====append ,reverse
                

'''

# x=(3,2,1)
# x.sort()


'''
List==   ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', 
'__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', 
'__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
 '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 
 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
  'reverse', 'sort']


tuple==
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
  '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', 
  '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
   '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', 
   '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']


'''

# l=list()
# print(dir(l))

# t=tuple()
# print(dir(t))

'''
tuple and assignment
'''

# (x,y)=("zahid","shorif")
# print(y)


'''
input:  {'apple': 4, 'mango': 6}


output:  apple 4
         mango 6
dict_items([('apple', 4), ('mango', 6)])

'''
# d=dict()
# d["apple"]=4
# d["mango"]=6
# print(d)
# for (k,v) in d.items():  # k=key , v=value (k,v)--- it's a tuple
#     print(k,v)

# tups=d.items()
# print(tups)


'''
tuples are compare able 


'''
# one=(0,1,2)<(5,0,1)
# two=(0,1,2)<(0,2,1)
# three=(0,1,2)<(0,1,3)
# four=(0,1,2)<(0,1,2)

# print(one,two,three,four)

# a=('ab')<('ab')
# b=('ab')<('abc')

# print(a,b)



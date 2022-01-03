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



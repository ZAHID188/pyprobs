try:
    fruit="banana"
    fruit[0]='b'
except:
    print(" Strings are not mutable we cannot change the value of a string")

# well , list are mutable.

x=[1,2,3,4,5,6,7]
print(x)

#we can change the value in the list
x[0]=9
x[3]=8
print(x)

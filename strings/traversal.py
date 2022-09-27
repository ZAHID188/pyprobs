# A lot of computations involve processing a string one character at a time.
#  Often they start at the beginning, select each character in turn, do something to it, 
#  and continue until the end. This pattern of processing is called a traversal.
#  One way to write a traversal is with a while loop:

fruit="apples"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
print("total alphabet=",index)


#for loop can handle that easily
for char in fruit:
    print(char)
    




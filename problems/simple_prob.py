# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”.
#  Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number
# detect their mistake using try and except and print an error message and skip to the next number.
# sum=float(0)
# while True:
#     inp=input("please provide the data")
#     if inp == "done":
#         break
#     elif inp>=0:
#         float_inp=float(inp)
#         sum=sum+float_inp
#         sumi=int(sum)
#     else:
#         print("bad data")



def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(1,2))

def subtract_two_numbers(a,b):
    return a-b

print(subtract_two_numbers(1,2))
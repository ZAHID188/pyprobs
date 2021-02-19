# Imorting only the square function from function1
#In this case look at the print section there you just need to write squre() don't need function1.square()
from function1 import square

for i in range(10):
    print(f"squre of {i} is {square(i)}")
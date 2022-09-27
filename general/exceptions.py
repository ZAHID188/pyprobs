import sys
try:
    x = int (input ("x: "))
    y = int (input ("y: "))
except ValueError:
    print("Error:invalid input")
    sys.exit(1)




try:
    result = x/y
# this try and except needed because of
# ex: 5 /0 = error for not showing error we use try and exception
#
except ZeroDivisionError:
    print("Error: cannot devide by zero")
    sys.exit(1)
    


print(f"{x} / {y} = {result}")

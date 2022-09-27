#  Please implement the sign function with the
#  if-elif-else structure and the nested if structure respectively.
#  The sign function is defined as:

def sgn(): # sgn(x) = 1 if x > 0, -1 if x < 0, 0 if x = 0
    x = float(input())
    if x > 0:
        print(1)
    elif x < 0:
        print(-1)
    else:
        print(0)
sgn()
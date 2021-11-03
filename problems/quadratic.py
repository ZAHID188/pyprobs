# Write the program,
#  input a three parameters a, b, c (all integers) of the binary one-time equation ax^2+bx+c=0, 
#  and find the real root of the equation.
#   If the equation has a real root,
#    print the real root (reserving one decimal),
#     and if there is no real root, print the information without the real root.
print("start")
def real_root(a, b, c):
    d = b**2 - 4 * a * c
    if d < 0:
        print("No real root")
    elif d == 0:
        x = (-b) / (2 * a)
        print("%.1f" % x)
    else:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
        print("x1= %.1f" % x1)
        print("x2= %.1f" % x2)

real_root(1,0,-1)

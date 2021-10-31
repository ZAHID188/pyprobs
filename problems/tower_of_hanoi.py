
# This is a recursion example

def f2(n):
    if n>=2:
        f2(n//2)
    print(n%2,end='')
def f1(a,b):
    if b==1:
        return a
    else:
        return a+f1(a,b-1)
        
    
#f1(3,5)
#f2(3)
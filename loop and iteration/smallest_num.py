
x=[4,7,3,24,23]
smallest=None
for i in x:
    if smallest is None:
        smallest=i
    elif i<smallest:
        smallest=i
    print(smallest , i)
print("result", smallest)
    
        

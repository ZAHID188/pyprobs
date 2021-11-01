found=False
print("Before",found)
for value in [12,4,7,45,22,344,33,55]:
    if value==7:
        found =True
    elif value !=7:
        found=False
    print(found,value)
   
print("After",found)


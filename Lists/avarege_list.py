# numlist=list()
numlist=[]
while True:
    inp=input("Enter a number:")
    if inp == 'done':
        break
    try:
        value=float(inp)
    except:
        print("please enter a valid number.")
        continue
    numlist.append(value)

try:
    average=sum(numlist)/len(numlist)
    print("avarege:",average)
except:
    print("Sorry Error occured")








def compareTriplets(a, b):
    # Write your code here
    alice,bob=0,0
    res=[]
    for i in range(len(a)):
        if a[i]>b[i]:
            alice=alice+1
        if a[i]<b[i]:
            bob=bob+1
        if a[i]==b[i]:
            continue
    res.append(alice)
    res.append(bob)
    return res


print(compareTriplets([12,34,56],[3,39,56]))
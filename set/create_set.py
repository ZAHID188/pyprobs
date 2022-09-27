set1=set("sunrise")
set2=set("sunset")
print(set1,set2)
result1='u' in set1
print(result1)
result2=(set1==set2)
print(result2)
result3=(set1-set2)
print(result3)

result4=set1 & set2
print("& =",result4)

result5=set1 | set2
print("| =",result5)

result6=set1 ^ set2
print("^ =",result6)

result7=set1 ^ set2
print("-= :",result7)


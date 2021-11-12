# xfile=open('hello.txt')
# count=0
# for hi in xfile:
#     count=count+1
#     print(xfile)
# print("Line Count:",count)



xfile=open('hello.txt')
txt=xfile.read()

print("Total text:",len(txt))
print("Text: \n", txt)

hi=txt.find(",")
print("after ICT::",txt[hi+1:])
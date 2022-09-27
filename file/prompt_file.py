# #count how many lines
# print("let's count how many lines are available in the text file")
# fname=input("Enter the file name: ")
# xfile=open(fname)
# count=0
# for line in xfile:
#     count=count+1
# print("There are %d line here available "%count)



#count how many lines
print("let's count how many lines are available in the text file")
fname=input("Enter the file name: ")
try:
    xfile=open(fname)
except:
    print("File can not be opened :",fname)
    quit()
count=0
for line in xfile:
    count=count+1
print("There are %d line here available "%count)


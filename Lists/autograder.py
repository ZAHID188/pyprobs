# Open the file romeo.txt and read it line by line. For each line, 
# split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and 
# if not append it to the list.
#  When the program completes, sort and print the resulting words in alphabetical order.

file=open("romeo.txt")
main=[]
for line in file:
    line=line.rstrip()
    words=line.split()
    # print(words)
    for word in words:
        # print(word)
        if word in main:
            continue
        else:
            main.append(word)
print(main)
    






# file=open("romeo.txt")
# main=[]
# for i in file:
#     i=i.rstrip()
#     words=i.split()
#     for z in words:
#         main.append(z)
        

# print(main)

# res=[]
# for words in main:
#     if words not in res:
#         res.append(words)
# res.sort()
# print(res)



        

    

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line=line.rstrip()
    words=line.split()
    if len(words)<1 or words[0]!="From":
        continue
    count=count+1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")







'''
8.5 Open the file mbox-short.txt and read it line by line. 

When you find a line that starts with 'From ' like the following line:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

You will parse the From line using split() and print out the second word in the line
 (i.e. the entire address of the person who sent the message).
  Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. 
Also look at the last line of the sample output to see how to print the count.

 Open the file mbox-short.txt and read it line by line. 

'''
# file=open("mbox-short.txt")
# x=[]
# sum=0
# for line in file:
#     line.rstrip()
#     words=line.split()
#     if len(words)<1:
#         continue
#     if words[0]!="From":
#         continue
#     print(words[1])
#     x.append(words)
#     sum=sum+1

# # print(len(x))
# # print(sum)
# print("There were %d lines in the file with From as the first word"%len(x))



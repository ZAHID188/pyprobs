# python shout.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#      BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#      SAT, 05 JAN 2008 09:14:16 -0500


# Exercise 1: Write a program to read through a file and 
# print the contents of the file (line by line) all in upper case. 
# Executing the program will look as follows:

# file=open('py4text.txt')
# text=file.read()
# print(text.upper())



# Exercise 2: Write a program to prompt for a file name, 
# and then read through the file and look for lines of the form:

# OUTPUT-X-DSPAM-Confidence: 0.8475

# name=input('Enter file name:')
# file=open(name)
# # text=file.read()
# print(text)
# for i in file:
#     i=i.rstrip()
#     if 'X-DSPAM-Confidence:' in i:
#         fl=i.find(".")
#         out1=i[0:fl+2]
#         print(out1)
#         # out=i[fl:3]
#         # print(out)
        



#  Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, 
#  they add a harmless Easter Egg to their program. 
#  Modify the program that prompts the user for the file name
#   so that it prints a funny message when the user types in the exact file name “na na boo boo”.
#    The program should behave normally for all other files which exist and don’t exist.
#  Here is a sample execution of the program:




#main problem
# Count these lines and extract the floating point values from each of the lines 
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print(" Please enter a valid File name")
    quit()

count=0
x=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    dot=line.find(".")
    value=line[dot-1:]
    count=count+1

    x=float(x)+float(value)

res=x/count
print("Average spam confidence:",res)






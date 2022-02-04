# Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day 
# for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, 
# print out the counts, sorted by hour as shown below.


# name = "mbox-short.txt"
# fhand=open(name)
# d={}
# for line in fhand:
#     rmsp=line.rstrip()
#     if rmsp.startswith('From'):
#         lst=rmsp.split()
#         for word in lst:
#             if ':' in word and 'From' not in word:
#                 if word[0:2] not in d:
#                     d[word[0:2]]=1
#                 else:
#                     d[word[0:2]]+=1
# # print(d)
# lst=[]
# for (k,v) in d.items():
#     lst.append((k,v))

# sortedval=sorted(lst)
# print(sortedval)
# for (k,v) in sortedval:
#     print(k,v)

# # same thing 
# # for (k,v) in (sorted([(k,v) for k,v in d0.items()])):
# #   print(k,v)



# lst=["1","2","3"]
# tp=("1","2","3")

# lst.pop(1)
# print(lst.index("1"))
# print(tp.index("1"))

# (x , y) = 3, 4
# print(y)

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)
                


            

               

            
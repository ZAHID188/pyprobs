'''
    using dictionary
 input= given text file
  output=  how many words are here , how many similar word

# '''
counts=dict()   #counts={}                -same
print("Enter line of text:")
line=input('')
words=line.split()
print('Words',words)
print("counting")
for word in words:
    counts[word]=counts.get(word,0)+1
print('counts',counts)




'''
  input= given text file
  output=  how many words are here , how many similar word

'''
# File=open(r"c:/Users/zahid/Desktop/clean/WEBSITE_DEV/GITHUB/pyprobs/Dictionary/assets/file1.txt")
# total=[]
# temptotal=[]
# for line in File:
#     line=line.strip()
#     if len(line) <1:   # for the gap line
#         continue
#     words=line.split()
#     # print(words)
#     for word in words:
#         temptotal.append(word)

#         if word in total:
#             print("",word)
#             continue
#         else:
#             total.append(word)
# print(len(total))
# print(len(temptotal))
# # print(temptotal.count("a"))
# print("start")
# i=0
# for word in range(i,len(temptotal)):
   
#     y=temptotal.count(temptotal[i])
#     print(temptotal[i],y)
#     i=i+1
   

# x=0
# for i in range(0,len(temptotal)):
#     if temptotal[i] in temptotal:
#         x=x+1
#         print("found",temptotal[i],x)
# # print(temptotal)

# i=0 
# count=0
# while i<len(temptotal):
#     for x in temptotal:
#         if x==temptotal[i]:
#             count=count+1
#             print(x,count)
#     i=i+1


# count=0
# for word in temptotal:
#     print(word)
#     if word in temptotal:
#         count=count+1
#         print(word,count)
#     else:
#         continue




''' input:
        we have a list of -  ["zahid","shorif","zahid","rayhan","shorif","zahid"]  

    output:
           {'zahid': 3, 'shorif': 2, 'rayhan': 1}

'''

count=dict()   # dictionary
names=["zahid","shorif","zahid","rayhan","shorif","zahid"]  #list

for name in names:
    count[name]=count.get(name,0)+1
print(count)



''' input:
         {'zahid': 3, 'shorif': 2, 'rayhan': 1}

    output:
           how many shorif ? = 2

'''

# count={'zahid': 3, 'shorif': 2, 'rayhan': 1}  # dictionary

# # if "shorif" in count:
# #     x=count['shorif']
# # else:
# #     x=0

# # commented part is same as below

# x=count.get("shorif",0)
# x2=count.get("shorifsadsad",0)
# print(x)
# print(x2)





''' input:
        we have a list of -  ["zahid","shorif","zahid","rayhan","shorif","zahid"]  
        we have to count how many names are there in the list for every individual

    output:
           {'zahid': 3, 'shorif': 2, 'rayhan': 1}

'''

# count=dict()   # dictionary
# names=["zahid","shorif","zahid","rayhan","shorif","zahid"]  #list

# for name in names:
#     if name not in count:
#         count[name]=1
#     else:
#         count[name]=count[name]+1
# print(count)
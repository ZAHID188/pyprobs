
file_open=open('mbox.txt')
for i in file_open:
    i=i.rstrip()
    wds=i.split()
    if len(wds)<1:
        continue
    #if  wds[0] !='From'or len(wds)<1 :  we can't use this because we are not gonna 
    if len(wds)<1 or wds[0] !='From':
        continue
    print(wds[0:2])





# file_open=open('mbox.txt')
# for i in file_open:
#     i=i.rstrip()
#     wds=i.split()
#     if len(wds)<1:
#         continue
#     if wds[0] !='From':
#         continue
#     print(wds[0:])









# file_open=open('mbox.txt')
# for i in file_open:
#     i=i.rstrip()
#     print("The Line ========",i)
#     wds=i.split()
#     print("words",wds)
#     #guardian pattern with this condition there will be a traceback
#     # Because empty line will cause an error it will remove the empty line 
#     # if len(wds)<1:
#     #     continue
#     # or we can also do another guardian pattern
#     if i == '':
#         print('Skip blank')
#         continue
#     if wds[0] !='From':
#         print('Ignore______')
#         continue
#     print(wds[2])




# x='With three words'
# stuff=x.split()       # makes an list
# print(stuff)
# print(stuff[2])


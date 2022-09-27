"""
দেওয়া আছে  , টোটাল জনসংখা = x
               টোটাল টাকা = y
        
output:  প্রত্যেকে নির্দিষ্ট পরিমান টাকার ব্যবধানে পুরো টাকা ডিস্ট্রিবিউশন |

"""
# people=int(input("koto jon ?"))
# money=float(input("total taka?"))
# def First_person(money,people):
#     i=0
#     for s in range(0,people):
#         i=s+i

#         print("i",i, s)
#     total=money+i
#     result=total/float(people)
#     return result
# print(First_person(money,people))
# def final(first,peop):
#     x=0
#     for s in range(1,peop+1):
#         # if x==0 :
#         #     x=first
#         # else:
#         #     x=first-float(s)
#         # x=first-s
#         # print(x)

       
#         print(s)
#         print(first)
    

# First_person(money,people)


# x=0
# sum=0
# for s in range(0,people):
#     z=First_person(money,people)
#     if x==0:
#         x=z
#     else:
#         x=z-s
#     x=z-s
#     sum=sum+x
    
#     print("taka :",s,"-",x)
# print("total:",sum)








#------------------




# people=int(input("koto jon ?"))
# money=float(input("total taka?"))
# def First_person(money,people):
#     i=0
#     for s in range(0,people):
#         i=s+i
#         # print(s)
#         print("i",i, s)
#     total=money+i
#     result=total/float(people)
#     return result
# print(First_person(money,people))





# for n in reversed(range(1,10)):
#     print(n)

# 1
# def seq(n):
#     x=49.98
#     def loop():
#         u=0
#         for num in range(1,n+1):
#             y=x/num
#             print( "%d=%f"%(num,y))
#             u=u+y
#         print("s",u)
#     loop()  
# seq(3)




# 2
# def seq(n):

#     def loop(f_val):
#         x=f_val
#         s=0
#         for num in range(1,n+1):
#             if s<=100:  #----------total taka
#                 y=x/num
#                 print( "%d=%f"%(num,y))
#                 s=s+y
#             elif num<n+1:
#                 print("%dneed to pay"%num)
#                 # loop(f_val-1)

        
#         print("sum s",s)
#     loop(40)  
# seq(10)


#3
# def seq(n):

#     def loop(f_val):
#         x=f_val
#         s=0
#         for num in range(1,n+1):
#             y=x/num
#             print( "%d=%f"%(num,y))
#             s=s+y
#             if s>100:
#                 loop(f_val-1)
#             # elif num<n+1:
#             #     print("%dneed to pay"%num)
#             #     # loop(f_val-1)

        
#         print("sum s",s)
#     loop(42)  
# seq(10)


# fianl and confirmed----------------------- 
# not optimized don't work with larger number because it have linear time complexity
def lp(bal,n):
    x=bal
    s=0
    while s<=bal:
        for num in range(1,n+1):
            y=x/num
            print( "%d=%f"%(num,y))
            s=s+y
        print("total sum=",s)
    return s


def seq(bal,peo):
    x=bal
    while lp(bal,peo)>x:
        bal=bal-1
        print(lp(bal,peo))
    
     
seq(100000,5)

#-----------------------------
# effecient solution Log(n)  binary search


# def lp(bal,n):
#     x=bal
#     s=0
#     while s<=bal:
#         for num in range(1,n+1):
#             y=x/num
#             print( "%d=%f"%(num,y))
#             s=s+y
#         print("total sum=",s)
#         print("------------------")
#     return s

# # binary search
# def locate_first_number(n,peo):
#     initial_money=n
#     lo, hi = 0, n

#     while lo <= hi:
#         mid = (lo + hi) // 2

#         if lp(mid,peo) > initial_money:
#             hi=mid-1
#         elif lp(mid,peo) < initial_money:
#             lo=mid+1
#         else:
#             return mid
#     return -1
# locate_first_number(1000,100)

#----------------------------------
     


# 27.77
# 10

# 1-10
# 2-5
# 3-3.33
# 4-2.5
# 5-2
# 6-1.66
# 7-1.42
# 8-1.25
# 9-1.11
# 10-1

# 27.77





# def locate_card(n):
#     lo, hi = 0, n
    
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         print(mid)

       
        
#         if mid == n:
#             return mid
#         elif mid_number < query:
#             hi = mid - 1  
#         elif mid_number > query:
#             lo = mid + 1
    
    # return -1








#-------------------------- 2nd rule


# people=int(input("koto jon ?"))
# money=float(input("total taka?"))

# s=0
# for n in range(1,people+1):
#     s=s+n
#     print(n)
# print("total",s)
# main=money/s
# print("main",main)


# d=[]
# for n in reversed(range(1,people+1)):
#     x=str(n*main)
#     d.append(x)
# # print(d)
# dc={}
# for i in range(1,people+1):
#     dc[str(i)]=d[i-1]
# # print(dc)
# for (k,v) in dc.items():
#     print(k,v)
# print(dc)


#---
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# df=pd.DataFrame(dc,index=[1])
# dfk=plt.bar(df.columns,df['1'])
# plt.show()
# print(df)
# to excel file
# df.to_csv("test.csv")

# print(df)

# df=pd.DataFrame(dc)
# # print(df)


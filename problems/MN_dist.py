"""
দেওয়া আছে  , টোটাল জনসংখা = x
               টোটাল টাকা = y
        
output:  প্রত্যেকে নির্দিষ্ট পরিমান টাকার ব্যবধানে পুরো টাকা ডিস্ট্রিবিউশন |

"""
people=int(input("koto jon ?"))
money=float(input("total taka?"))
def First_person(money,people):
    i=0
    for s in range(0,people):
        i=s+i
    total=money+i
    result=total/float(people)
    return result

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


x=0
sum=0
for s in range(0,people):
    z=First_person(money,people)
    # if x==0:
    #     x=z
    # else:
    #     x=z-s
    x=z-s
    sum=sum+x
    
    print("taka :",s,"-",x)
print("total:",sum)




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
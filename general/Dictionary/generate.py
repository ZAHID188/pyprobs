
''' 
Input:     

output:          
'''
# import requests
# kw={'q':'python dic'}
# r=requests.get("http://cn.bing.com/search",params=kw)

# r.url
# # print(r.text)
# print(r.url)






''' 
Input:     

output:          
'''
# stock={'axp':78.56,'ba':186.76}
# bstock=stock
# stock={}
# print(bstock)


# stock={'axp':78.56,'ba':186.76}
# bstock=stock
# stock.clear()
# print(bstock)







''' 
Input:     

output:          
'''
# stock={'axp':78.56,'ba':186.76}
# # print(stock['AAA'])       # we will not use this because it stops the execution
# print(stock.get('AAA'))









''' 
Input:     info={"zahid":"3000","shorif":"2000","rayhan":"5000"}

output:          zahid 9000
                 shorif 4000
                 rayhan 7000
'''
# info={"zahid":"3000","shorif":"2000","rayhan":"5000"}
# binfo={"zahid":"9000","shorif":"4000","rayhan":"7000"}
# info.update(binfo)
# print(info)










''' 
Input:     info={"zahid":"3000","shorif":"2000","rayhan":"5000"}

output:          zahid 3000
                 shorif 2000
                 rayhan 5000
'''
info={"zahid":"3000","shorif":"2000","rayhan":"5000"}
print(info)
print(info.keys())
print(info.values())

for k,v in info.items():
    print(k,v)





# a={"zahid":"3000","shorif":"2000","rayhan":"5000"}
# x=a["rayhan"]
# print(a)
# print(x)
# a["shorif"]=10000
# print("check shorif value",a)

# sabbir="sabbir" in a
# print(sabbir)
# del a["rayhan"]
# print("rayhan is deleted",a)






'''
Input:   [('axp','american express company','78.51')]
         [('ba','the boing company','78.51')]
         [('cat','caterpilar inc','96.39')]
         [('csc','american express company','33.71')]
         [('cvx','american express company','106.09')]

output:  {'axp':'78.51','ba':'184.76','cat':'96.39','csc':'33.71','cvx':'106.09'}
'''
# p_list=[('axp','american express company','78.51'),
#         ('ba','the boing company','78.51'),
#         ('cat','caterpilar inc','96.39'),
#         ('csc','american express company','33.71'),
#         ('cvx','american express company','106.09')]
# d={}

# print(len(p_list))
# for item in p_list:
#    d[item[0]]=item[2]

# print(d)





'''
Input:   [('axp','american express company','78.51')]
         [('ba','the boing company','78.51')]
         [('cat','caterpilar inc','96.39')]
         [('csc','american express company','33.71')]
         [('cvx','american express company','106.09')]

output:  {'axp':'78.51','ba':'184.76','cat':'96.39','csc':'33.71','cvx':'106.09'}
'''
# p_list=[('axp','american express company','78.51'),
#         ('ba','the boing company','78.51'),
#         ('cat','caterpilar inc','96.39'),
#         ('csc','american express company','33.71'),
#         ('cvx','american express company','106.09')]
# a_list=list() # a_list=[]   is same
# b_list=list()

# print(len(p_list))
# for i in range(len(p_list)):
#     astr=p_list[i][0]
#     bstr=p_list[i][2]
#     a_list.append(astr)
#     b_list.append(bstr)
# adict=dict(zip(a_list,b_list))
# print(adict)






'''
Input:   names=["zahid","shofiq","rofiq"]
       salaries=[3000,2000,4500]

output:  {'zahid': 3000, 'shofiq': 2000, 'rofiq': 4500}
'''
# names=["zahid","shofiq","rofiq"]
# salaries=[3000,2000,4500]
# x=dict(zip(names,salaries))
# print(x)
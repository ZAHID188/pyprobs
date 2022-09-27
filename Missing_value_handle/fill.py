#1-Read csv
'''
Input:  
   Unnamed: 0   name   city   address    phone  balance
0           0  zahid  Dhaka   gulshan  1231231       21
1           1  rofiq  Dhaka  motijhil  2121241       23

output:

city
Dhaka           0  zahid   gulshan  1231231       21
Dhaka           1  rofiq  motijhil  2121241       23

'''

# import pandas as pd
# df=pd.read_csv("userinfo.csv",index_col="city")
# print(df)



#2-df.isnull()
'''
Input:  
    name   city   address    phone  balance
0  zahid  Dhaka   gulshan  1231231     21.0
1  rofiq  Dhaka  motijhil  2121241     23.0
1  rofiq    NaN  motijhil  2121241      NaN

output:

    name   city  address  phone  balance
0  False  False    False  False    False
1  False  False    False  False    False
1  False   True    False  False     True


'''
# import pandas as pd
# df=pd.read_csv("userinfo.csv",index_col=0)
# print(df.isnull())


#3 dropna
'''
Input:  
    name   city   address    phone  balance
0  zahid  Dhaka   gulshan  1231231     21.0
1  rofiq  Dhaka  motijhil  2121241     23.0
1  rofiq    NaN  motijhil  2121241      NaN

output:

    name   city   address    phone  balance
0  zahid  Dhaka   gulshan  1231231     21.0
1  rofiq  Dhaka  motijhil  2121241     23.0


'''
# import pandas as pd
# df=pd.read_csv("userinfo.csv",index_col=0)
# print(df.dropna(how='any')) #df.dropna() is same value ,  i mean default of any
# print(df.dropna(how='all'))# if all the the value is NAN





#4 fillna
'''
Input:  

     name     city   address    phone  balance
0   zahid    Dhaka   gulshan   3.1231     21.0
1   rofiq    Dhaka  motijhil   2.1241     23.0
2   rofiq      NaN  motijhil  41.0000      NaN
3  sabbir  cumilla      miya   2.1241     44.0

output:

     name     city   address    phone  balance
0   zahid    Dhaka   gulshan   3.1231     21.0
1   rofiq    Dhaka  motijhil   2.1241     23.0
2   rofiq  cumilla  motijhil  41.0000     44.0
3  sabbir  cumilla      miya   2.1241     44.0



'''
# import pandas as pd
# df=pd.read_csv("userinfo.csv",index_col=0)
# print(df)
# # print(df.fillna(method='ffill'))
# print(df.fillna(method='bfill'))




'''
Input = CSV file 

output::     
         Series_reference   Period  Data_value STATUS    UNITS  ...         Series_title_1 Series_title_2 Series_title_3 Series_title_4 Series_title_5
0         GFSA.SCS01G01Z90  2009.06        2903  FINAL  Dollars  ...  Net operating balance            NaN            NaN            NaN            NaN
1         GFSA.SCS01G01Z90  2010.06       -3564  FINAL  Dollars  ...  Net operating balance            NaN            NaN            NaN            NaN
2         GFSA.SCS01G01Z90  2011.06      -13093  FINAL  Dollars  ...  Net operating balance            NaN            NaN            NaN            NaN

'''

# import pandas as pd
# quotesdf=pd.read_csv('axp1.csv')
# print(quotesdf)





'''
Input = CSV file name example --axp1.csv

output::     store in another csv file with new file. -- check the new file with given name stocks.csv
'''

# import pandas as pd
# def retrieve_quotes_historical(x):
#     text1=pd.read_csv(x)
#     return text1
# quotes=retrieve_quotes_historical('axp1.csv')
# df=pd.DataFrame(quotes)
# df.to_csv("stocks.csv")



'''
Input = CSV file --axp1.csv

output::     to excel stocksaxp1.xlsx
'''

# import pandas as pd
# def retrieve_quotes_historical(x):
#     text1=pd.read_csv(x)
#     return text1
# quotes=retrieve_quotes_historical('axp1.csv')
# df=pd.DataFrame(quotes)
# df.to_excel("stocksaxp1.xlsx",sheet_name='axp1.csv')





'''
Input = CSV file excel stocksaxp1.xlsx

output::    
period
2011.06      BDCQ.SEA1AA
2011.09      BDCQ.SEA1AA
2011.12      BDCQ.SEA1AA
2012.03      BDCQ.SEA1AA
'''

# import pandas as pd
# df=pd.read_excel("employ_data.xlsx",index_col="Period")
# print(df.isnull())
# print(df.dropna())
# print(df.fillna())
# df.fillna(method='ffill')
# df.fillna(method='bfill')
# df.fillna(df.mean(),inplace=True)
# df.dropna(how='any')
# df.dropna(how='all')

'''
Input = excel to

output::    csv

'''
# import pandas as pd
# df=pd.read_excel("datasheet.xlsx")
# df.to_csv("userinfo.csv",index="0",header=True)
# print(df)





'''
Input = web ASP


'''


# f1.head(5)
# print(f1)
# print("********************")
# print(f2.columns)




'''
Fetch Data with Python 

'''
# import requests
# import re
# import json
# import pandas as pd

# def retrive_quote_hitory(stock_code):
#     quotes=[]
#     url='https://finance.yahoo.com/quote/%s/history?p=%s'%(stock_code,stock_code)

#     try:
#            r=requests.get(url)
#     except ConnectionError as err:
#            print(err)
#     m=re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"',r.text)
#     if m:
#            quotes=json.loads(m[0])
#            quotes=quotes[::-1]
#     return [item for item in quotes if 'type' not in item]

# quote=retrive_quote_hitory('AXP')
# x=pd.DataFrame(quote)
# # y=x.drop(['High'],axis=1)
# print(x)







'''

'''

# import pandas_datareader.data as web
# quotesdf=pd.read_csv('axp1.csv')
# print(quotesdf)


'''

'''
# from sklearn import datasets
# iris=datasets.load_iris()
# iris.feature_name
# import pandas_datareader.data as web
# quotesdf=pd.read_csv('axp1.csv')
# print(quotesdf)


'''
graph 


'''
# import matplotlib.pyplot as plt
# plt.plot([3,4,7,6,2,8,9])
# plt.plot(range(7),[3,4,7,6,2,8,9])
# plt.show()



'''
graph  2,3 line


'''

# import numpy as np
# import matplotlib.pyplot as plt
# t=np.arange(0.,4.,0.1)
# plt.plot(t,t,t,t+2,t,t**2)
# plt.show()


'''
graph  bar,scatter


'''


# import matplotlib.pyplot as plt
# plt.bar(range(6),[3,5,2,7,9,4])
# plt.scatter(range(6),[3,5,2,7,9,4])




'''
color and line style graph


'''


# import matplotlib.pyplot as plt
# plt.plot(range(6),[3,5,2,7,9,4],"rD")


'''
graph multiline with details and graph design 



'''

# import numpy as np
# import matplotlib.pyplot as plt

# plt.figure(figsize=(8,6),dpi=100)
# t=np.arange(0.,4.,0.1)
# plt.plot(t,t,color='red',linestyle='-',linewidth=3,label='Line 1')
# plt.plot(t,t+2,color='green',linestyle='',marker="*",linewidth=3,label='Line 2')
# plt.plot(t,t**2,color='blue',linestyle='',marker="+",linewidth=3,label='Line 3')
# plt.legend(loc='upper left')




'''
graph vertical axis and horizontal axis 



'''

# import matplotlib.pyplot as plt
# plt.title("plot example")
# plt.xlabel("X label")
# plt.ylabel("Y label")
# plt.plot(range(7),[3,4,5,8,5,4,5])



'''
graph subplot



'''

# import matplotlib.pyplot as plt
# plt.subplot(211)
# plt.subplot(212)# 211  === 2 is 2 row 1 is column and last 2 is serial number
# plt.subplot(121)
# plt.subplot(122)


'''
graph subplot



'''

# import matplotlib.pyplot as plt

# x=np.linspace(-np.pi,np.pi,300)
# plt.figure(1)
# plt.subplot(211)
# plt.plot(x,np.sin(x),color='r')
# plt.subplot(212)
# plt.plot(x,np.cos(x),color='g')



'''
graph subplots <<<



'''
# import numpy as np
# import matplotlib.pyplot as plt
# x=np.linspace(-np.pi,np.pi,300)
# fig,(ax0,ax1)=plt.subplots(2,1)
# ax0.plot(x,np.sin(x),color='r')
# ax0.set_title('subplot1')
# plt.subplots_adjust(hspace=0.5)
# ax1.plot(x,np.cos(x),color='g')
# ax1.set_title("subplot2")




'''
graph subplots <<<



'''

# import numpy as np
# import matplotlib.pyplot as plt
# x=np.linspace(-np.pi,np.pi,300)
# plt.axes([.1,.1,0.8,0.8])
# plt.plot(x,np.sin(x),color='r')
# plt.axes([.3,.15,0.4,0.3])
# plt.plot(x,np.cos(x),color='g')


'''
Data exploration and pre-processing

Data exploration=> 
                 1.check data errors
                 2.understand data distributions
                 3.characteristics and inherenr regularitiies

pre-processing   -> 
                    1.data cleaning
                    2.data integration
                    3.data transformation
                    4.data reduction
'''

'''
graph subplots <<<

 Data_value     Magnitude  Series_title_4  Series_title_5
count  1.870600e+04  18706.000000             0.0             0.0
mean   6.087086e+04      2.426494             NaN             NaN
std    1.612277e+05      2.944750  

'''
# import pandas as pd
# df=pd.read_excel("employ_data.xlsx",index_col="Period")
# df.describe()

'''
input <<<

 {'data': array([[6.3200e-03, 1.8000e+01, 2.3100e+00, ..., 1.5300e+01, 3.9690e+02,
        4.9800e+00],
       [2.7310e-02, 0.0000e+00, 7.0700e+00, ..., 1.7800e+01, 3.9690e+02, 

'''
# from sklearn import datasets
# import pandas as pd
# bs=datasets.load_boston()
# df=pd.DataFrame(bs.data[:,4:7])



'''
Z score normalization
'''
# import pandas as pd
# from sklearn import datasets
# df=pd.read_csv("userinfo.csv")
# (df-df.mean())/df.std()



'''
Discretization of continious features
# '''
# import pandas as pd
# from sklearn import datasets
# import numpy as np
# df=pd.read_csv("userinfo.csv")
# (df-df.mean())/df.std()
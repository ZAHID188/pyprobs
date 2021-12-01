'''
Fetch Data with Python 

'''
# import requests
# import re
# import json
# import pandas as pd

# def retrive_quote_hitory(stock_code):
#     quotes=[]
#     url='https://finance.yahoo.com/quote/%s/history'







'''

'''

# import pandas as pd
# quotesdf=pd.read_csv('axp1.csv')
# print(quotesdf)

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
# plt


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


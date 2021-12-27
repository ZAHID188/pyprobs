import requests

r= requests.get('https://money.cnn.com/data/dow30/')
for x in r:
     print(x)
# import pandas as pd
# quotes = retrieve_quotes_historical('AXP')
# df = pd.DataFrame(quotes)
# df.to_csv('stockAXP.csv')


'''
heatmap correlation


'''
# import matplotlib.pyplot as plt
# from seaborn.matrix import heatmap
# from sklearn import datasets
# iris=datasets.load_iris()
# import pandas as pd 
# iris_df=pd.DataFrame(iris.data)
# iris_df.columns=iris.feature_names
# iris_df['target']=iris.target

# x=iris_df.iloc[:,[0,1,4]].corr()
# import seaborn as sns
# x=sns.heatmap(x,annot=True,fmt='.1f',cmap='rainbow')
# plt.show()









'''
 correlation between target and the length(0)

 output:0.7825612318100814

'''
# import matplotlib.pyplot as plt
# from sklearn import datasets
# iris=datasets.load_iris()
# import pandas as pd 
# iris_df=pd.DataFrame(iris.data)
# iris_df.columns=iris.feature_names
# iris_df['target']=iris.target
# y=iris_df.iloc[:,0]
# x=iris_df['target'].corr(y)

# print(x)






'''
correlation between  :sepal length (cm)  and sepal width (cm)  and target           

                   sepal length (cm)  sepal width (cm)    target
sepal length (cm)           1.000000         -0.117570  0.782561
sepal width (cm)           -0.117570          1.000000 -0.426658
target                      0.782561         -0.426658  1.000000



'''
# import matplotlib.pyplot as plt
# from sklearn import datasets
# iris=datasets.load_iris()
# import pandas as pd 
# iris_df=pd.DataFrame(iris.data)
# iris_df.columns=iris.feature_names
# iris_df['target']=iris.target

# x=iris_df.iloc[:,[0,1,4]].corr()
# print(x)








"""
FROM-----
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target
0                  5.1               3.5                1.4               0.2       0
1                  4.9               3.0                1.4               0.2       0
2                  4.7               3.2                1.3               0.2       0
3                  4.6               3.1                1.5               0.2       0
4                  5.0               3.6                1.4               0.2       0
TO------
     sepal length (cm)  sepal width (cm)  target
0                  5.1               3.5       0
1                  4.9               3.0       0
2                  4.7               3.2       0
3                  4.6               3.1       0
4                  5.0               3.6       0


"""


# import matplotlib.pyplot as plt
# from sklearn import datasets
# iris=datasets.load_iris()
# import pandas as pd 
# iris_df=pd.DataFrame(iris.data)
# iris_df.columns=iris.feature_names
# iris_df['target']=iris.target

# x=iris_df.iloc[:,[0,1,4]]
# print(iris_df)
# print(x)











'''

single graph
graph metrix
correlation coefficient
'''



# import matplotlib.pyplot as plt
# from sklearn import datasets
# iris=datasets.load_iris()
# x=[item[0] for item in iris.data]
# y=[item[2] for item in iris.data]
# plt.scatter(x[:50],y[:50],color="red")
# plt.scatter(x[50:100],y[50:100],color="green")
# plt.scatter(x[100:],y[100:],color="blue")
# plt.legend(loc="best")
# plt.show()










'''

from:
 [[5.1 3.5 1.4 0.2]
 [4.9 3.  1.4 0.2]
 [4.7 3.2 1.3 0.2]
 [4.6 3.1 1.5 0.2]
 [5.0  3.6 1.4 0.2]
 [5.4 3.9 1.7 0.4]
 [4.6 3.4 1.4 0.3]
 [5.0  3.4 1.5 0.2]
 [4.4 2.9 1.4 0.2]
to:
 [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4]


'''
# import matplotlib.pyplot as plt
# from sklearn import datasets
# iris=datasets.load_iris()
# x=[item[0] for item in iris.data]
# print(x)
# print(iris.data)
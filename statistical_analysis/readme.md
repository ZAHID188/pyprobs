```

'''
input:75% quantile
      25% quantile
      quantile substraction

output:

'''

# import matplotlib.pyplot as plt
# from sklearn import datasets
# iris=datasets.load_iris()
# import pandas as pd 
# iris_df=pd.DataFrame(iris.data)
# iris_df.columns=iris.feature_names
# iris_df['target']=iris.target
# # x=iris_df.iloc[:,0][:10]
# x=iris_df.iloc[:,0].quantile([0.75])
# y=iris_df.iloc[:,0].quantile([0.25])

# print(x)
# print(y)
# # print(x-y)   # it's an error 
#      # for avoiding error we have to use LOC......
    
# x=iris_df.iloc[:,0].quantile([0.75]).loc[0.75]
# y=iris_df.iloc[:,0].quantile([0.25]).loc[0.25]

# print(x-y)






'''
delete from 75% to 25%


count    150.000000
mean       5.843333
std        0.828066
min        4.300000
25%        5.100000
50%        5.800000
75%        6.400000
max        7.900000




output= 1.300
'''


# import matplotlib.pyplot as plt
# from sklearn import datasets
# iris=datasets.load_iris()
# import pandas as pd 
# iris_df=pd.DataFrame(iris.data)
# iris_df.columns=iris.feature_names
# iris_df['target']=iris.target
# # x=iris_df.iloc[:,0][:10]
# x=iris_df.iloc[:,0].describe().loc['75%']
# y=iris_df.iloc[:,0].describe().loc['25%']
# print(x-y)






'''
mean ,median, standard deviation,quantile .   uper quantile =75%,lower=25%,midle=50%


count    150.000000
mean       5.843333
std        0.828066
min        4.300000
25%        5.100000
50%        5.800000
75%        6.400000
max        7.900000
'''


# import matplotlib.pyplot as plt
# from sklearn import datasets
# iris=datasets.load_iris()
# import pandas as pd 
# iris_df=pd.DataFrame(iris.data)
# iris_df.columns=iris.feature_names
# iris_df['target']=iris.target
# # x=iris_df.iloc[:,0][:10]
# x=iris_df.iloc[:,0]
# print(x.mean())
# print(x.median())
# print(x.describe())

```
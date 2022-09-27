# print('abc' < 'ABC')
# print((1, 2) in zip(range(4),range(2,6)))
# print(zip(range(4),range(2,6)))
# x=range(4)
# y=range(2,6)
# z=zip(x,y)
# print((1,2 in z))

# dict_mark_1 = {'Wang': 98, 'Li': 87, 'Ma': 93}
# dict_mark_2 = {'Li': 90, 'Ma': 95, 'Xu': 75}
# dict_mark_1.update(dict_mark_2)
# dict_mark_1.pop('Li')   
# print(dict_mark_1)

# def foo(arg1,*arg2):
#     print(arg1)
#     print(arg2)
# foo("happy","new","year")



# import pandas as pd
# data=pd.read_csv('data.csv')
# aDF=pd.DataFrame(data)
# aDF['days']=[22,24,28]
# print(aDF)


# string = 'My moral standing is: 0.98765'
# moral_str = string.split(":")[1]
# result = float(moral_str)
# print(result)


# The program functions are: read the score data in the file score.csv,
# calculate the average score and count the scores of each course for the
# students whose Chinese score is 80 or more and English score is 85 or
# more (sort from big to small), Output the result to the file result.csv and
# plot a bar chart of the average results of the students who meet the
# conditions as shown in the figure.

# import pandas as pd
# df=pd.read_excel('score.xlsx')
# df

# import tushare as ts
# import numpy as np
# df = ts.get_hist_data('600036', start = '2020-01-01', end = '2020-03-31')
# df = df.iloc[:, :5] # get the first 5 columns
# df.sort_index(inplace = True)
# z=df.head(10)
# Print(z.volume)
# # print(z)

x,y=7.89,-15
not x is y



'''
#5   subplot()


'''


import numpy as np
import matplotlib.pyplot as plt

# plt.subplot(211)
# plt.subplot(212)
# plt.show()


# plt.subplot(121)
# plt.subplot(122)
# plt.show()


# plt.subplot(221)
# plt.subplot(222)
# plt.subplot(223)
# plt.subplot(224)
# plt.show()

# x = np.linspace(-np.pi, np.pi, 300)
# plt.figure(1) # default
# plt.subplot(211) # first subplot
# plt.plot(x, np.sin(x), color = 'r')
# plt.subplot(212) # second subplot
# plt.plot(x, np.cos(x), color = 'g')
# plt.show()



# x = np.linspace(-np.pi, np.pi, 300)
# fig, (ax0, ax1) = plt.subplots(2, 1)
# ax0.plot(x, np.sin(x), color = 'r')
# ax0.set_title('subplot1')
# plt.subplots_adjust(hspace = 0.5)
# ax1.plot(x, np.cos(x), color = 'g')
# ax1.set_title('subplot2')
# plt.show()


'''
#4 NumPy array can also be
used as a parameter of
Matplotlib
• Groups data plotting

'''
# from matplotlib import colors
# import numpy as np
# import matplotlib.pyplot as plt
# t=np.arange(0.,4.,0.1)
# print(t)
# plt.plot(t, t, t, t+2, t, t**2)
# plt.show()

# plt.scatter(range(7), [3, 4, 7, 6, 2, 8, 9])
# # plt.bar(range(7), [3, 4, 7, 6, 2, 8, 9])
# plt.show()


# plt.figure(figsize = (8, 6), dpi = 100)
# t = np.arange(0., 4., 0.1)
# plt.plot(t, t, color='red', linestyle='-', linewidth=5, label='t and t')
# plt.plot(t, t+2, color='green', linestyle='', marker='*', linewidth=3, label='Line 2')
# plt.plot(t, t**2, color='blue', linestyle='', marker='+', linewidth=3, label='Line 3')
# plt.legend(loc = 'upper left')
# plt.title('Plot Example')
# plt.xlabel('X label')
# plt.ylabel('Y label')
# plt.show()


'''
#3 Matplotlib Plotting
Most famous Python 2D
plotting library
– High quality
– Convenient plotting modules
• Plotting API——pyplot module

'''
# import matplotlib.pyplot as plt
# plt.plot([3, 4, 7, 6, 2, 8, 9,10,25])

# # plt.plot(range(7), [3, 4, 7, 6, 2, 8, 9])  #fixed range
# plt.show()




'''
#2 iris



'''

# from sklearn import datasets
# import pandas as pd
# iris = datasets.load_iris()
# # print(iris.feature_names)
# # print(iris.data)

# x=pd.DataFrame(iris.data,columns=iris.feature_names)
# print(x.head(5))


'''
#1
data using api


'''

# import pandas_datareader.data as web
# import pandas as pd
# f = web.DataReader('AXP', 'stooq')
# # print(f.head(10))

# data=pd.DataFrame(f)
# print(data)



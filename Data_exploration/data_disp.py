import pandas as pd
quotes = pd.read_csv('AXP.csv')
quotesdf=pd.DataFrame(quotes)
month=[item[5:7] for item in quotesdf.Date]
x =quotesdf.groupby(month).Open.count()

print(x)







'''Calculate the number of opening days
of AXP for each month in the past year.

output:

01    19   january 19 days...
02    19
03    23
04    21
05    20
06    22
07    21
08    22
09    21
10    21
11    21
12    22
Name: Open, dtype: int64

'''

# import pandas as pd
# quotes = pd.read_csv('AXP.csv')
# quotesdf=pd.DataFrame(quotes)
# month=[item[5:7] for item in quotesdf.Date]
# x =quotesdf.groupby(month).Open.count()
## x=quotesdf.groupby(month).apply(len)   # both are same
# print(x)


'''input=price is upper than or equal ==> 300  show their name.
output:
           3     Boeing
           4    Boeing2
'''

# import pandas as pd
# quotes = pd.read_csv('DJI.csv')
# quotesdf=pd.DataFrame(quotes)
# print(quotesdf[quotesdf.price >= 300].name)


'''input=price.mean()

output:
           218.235
'''

# import pandas as pd
# quotes = pd.read_csv('DJI.csv')
# quotesdf=pd.DataFrame(quotes)
# print(quotesdf.price.mean())








'''input=DJI.csv.price

output:
0    155.82
1    114.41
2    227.01
3    375.70
Name: price, dtype: float64
'''

# import pandas as pd
# quotes = pd.read_csv('DJI.csv')
# quotesdf=pd.DataFrame(quotes)
# print(quotesdf.price)



'''
input= DJI.csv


output=
    code              name   price
0   MMM                3M  155.82
1   AXP  American Express  114.41
2  AAPL             Apple  227.01
3    BA            Boeing  375.70

'''


# import pandas as pd
# quotesdf = pd.read_csv('DJI.csv')
# print(quotesdf)
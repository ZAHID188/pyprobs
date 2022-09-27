'''
input: any txt or any format 

output: csv file

'''
# import pandas as pd
# def retrieve_quotes_historical(x):
#     text1=pd.read_csv(x)
#     return text1
# quotes = retrieve_quotes_historical('data.txt')
# df = pd.DataFrame(quotes)
# df.to_csv('data.csv')   # we can also use doc or any format here




'''
Input = CSV file --axp1.csv

output::     to excel stocksaxp1.xlsx
'''

# import pandas as pd
# def retrieve_quotes_historical(x):
#     text1=pd.read_csv(x)
#     return text1
# quotes=retrieve_quotes_historical('data.csv')
# df=pd.DataFrame(quotes)
# df.to_excel("data.xlsx",sheet_name='data.csv')




'''
Input = CSV file 

output::     
         Series_reference   Period  Data_value STATUS    UNITS  ...         Series_title_1 Series_title_2 Series_title_3 Series_title_4 Series_title_5
0         GFSA.SCS01G01Z90  2009.06        2903  FINAL  Dollars  ...  Net operating balance            NaN            NaN            NaN            NaN
1         GFSA.SCS01G01Z90  2010.06       -3564  FINAL  Dollars  ...  Net operating balance            NaN            NaN            NaN            NaN
2         GFSA.SCS01G01Z90  2011.06      -13093  FINAL  Dollars  ...  Net operating balance            NaN            NaN            NaN            NaN

'''

# import pandas as pd
# quotesdf=pd.read_csv('data.csv')
# print(quotesdf)

# import pandas as pd
# quotesdf=pd.read_excel('data.xlsx')
# print(quotesdf)








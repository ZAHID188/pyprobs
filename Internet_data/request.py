import requests
import re
import json
import pandas as pd

def Dji():
    url='https://money.cnn.com/data/dow30/'

    try:
           r=requests.get(url)
    except ConnectionError as err:
           print(err)
    search_pattern=re.compile('class="wsod_symbol">(.*?)<\/a>.*<span.*">(.*?)<\/span>.*\n.*class="wsod_stream">(.*?)<\/s>')
    x=re.findall(search_pattern,r.text)
    djilist=[]
    for item in x:
        djilist.append({'code':item[0],'name':item[1],'price':float(item[2])})
    return djilist

quote=Dji()
x=pd.DataFrame(quote)
# y=x.drop(['High'],axis=1)
print(x)












# import requests
# import re
# import json
# import pandas as pd

# def retrive_quote_hitory(stock_code):
#     quotes=[]
#     url='https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code,stock_code)
#     try:
#         r=requests.get(url)
#     except ConnectionError as err:
#         print(err)
#     m=re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"',r.text)
#     if m:
#         quotes=json.loads(m[0])
#         quotes=quotes[::-1]
       
#     return quotes

# quote=retrive_quote_hitory('AXP')
# x=pd.DataFrame(quote)
# # y=x.drop(['High'],axis=1)
# print(x)









# import requests
# r= requests.get('http://money.cnn.com/data/dow30/')
# print("Status:",r.status_code)
# x=r.text
# print(x.find("http://pixel"))



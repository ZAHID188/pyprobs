import requests
r= requests.get('http://money.cnn.com/data/dow30/')
print("Status:",r.status_code)
x=r.text
print(x.find("http://pixel"))

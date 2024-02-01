import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=LCK2UZVZMWBV5J4W'
r = requests.get(url)
data = r.json()

print(type(data['Time Series (5min)']))
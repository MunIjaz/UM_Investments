import requests 
link2 = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AAPL&apikey=4H4XGZE8HAY85MW6'
r2 = requests.get(link2)
data2 = r2.json()
print(data2['Monthly Time Series'])
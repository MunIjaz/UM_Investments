
import pandas as pd
import numpy as np

#The API request is below:

import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=ONZOU16MALIX7UNO'
r = requests.get(url)
data = r.json()

##print(data.keys())
##print(type(data))

#print(data['Time Series (5min)']['2024-01-31 19:55:00'].keys())
#print(data['Time Series (5min)']['2024-01-31 19:50:00'].keys())

df = pd.DataFrame(data['Time Series (5min)'], index = [0])
print(df)




import pandas as pd
import numpy as np

#The API request is below:

import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&apikey=ONZOU16MALIX7UNO'
r = requests.get(url)
data = r.json()

##print(data.keys())
##print(type(data))

#print(data['Time Series (5min)']['2024-01-31 19:55:00'].keys())
#print(data['Time Series (5min)']['2024-01-31 19:50:00'].keys())

df = pd.DataFrame(data['Time Series (5min)'])
print(df)


class User:
   
    def __init__(self,name,ID,opening_balance,balance,portfolio):
        self.name = name 
        self.ID = ID
        self.opening_balance = opening_balance
        self.balance = balance
        self.portfolio = []

    def buy(self):
        stock_to_buy = input("Please enter the name of the stock you would like to purchase ")
        quanity_of_stock = input("Please enter the number of stocks you would like to purchase ")
        self.add_stock_to_portfolio(stock_to_buy,quanity_of_stock)
    
    def add_stock_to_portfolio(self,stock,quantity):
        quantity_of_stock += quantity
        self.portfolio.append((stock,quantity))    

    def sell(self):
        stock_to_sell = input("Please enter the name of the stock you would like to sell ")
        Quanity_of_stock = input("Please enter the number of stocks you would like to sell ")

u1 = User("Utsav Paliwal",1,10000,0,[{}])

#u1.add_stock_to_portfolio()

print(u1.name,u1.opening_balance,u1.portfolio)
u1.buy()
u1.sell()

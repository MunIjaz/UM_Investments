
import pandas as pd
import numpy as np
import requests

class Stock:
    def __init__(self,ticker):
        self.ticker = ticker
        self.name = self.get_stock_name()
        self.buy_price = self.get_buy_price() # price at 31/12/23
        self.sell_price = self.get_sell_price() #price at 31/01/24

    def get_stock_name(self):
        tick = self.ticker
        link1 = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={tick}&apikey=4H4XGZE8HAY85MW6'
        r1 = requests.get(link1)
        data1 = r1.json()
        return data1['bestMatches'][0]['2. name']

    def get_buy_price(self):
        tick = self.ticker
        link2 = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={tick}&apikey=4H4XGZE8HAY85MW6'
        r2 = requests.get(link2)
        data2 = r2.json()
        return data2['Monthly Time Series']['2023-12-29']['4. close'] # price at the end of december

    def get_sell_price(self):
        tick = self.ticker
        link2 = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={tick}&apikey=4H4XGZE8HAY85MW6'
        r2 = requests.get(link2)
        data2 = r2.json()
        return data2['Monthly Time Series']['2024-02-01']['4. close'] # price at the end of december


user = input("Enter 1 if you know the ticker of the stock. Otherwise, enter 2 to search for a stock by keyword.")
if user == 1:
    target_stock = input("Please enter your stock ticker.")
    stock1 = Stock(target_stock)
    print(f'You chose stock {stock1.name} with ticker, {stock1.ticker}. The buying price of {stock1.ticker} is {stock1.buy_price}')
elif user == 2:

    import pandas as pd
    import numpy as np
    import requests

    # The API request is below:

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&apikey=4H4XGZE8HAY85MW6'
    r = requests.get(url)
    data = r.json()
    print(data)
    # print(data.keys())
    # print(type(data))

    # print(data['Time Series (5min)']['2024-01-31 19:55:00'].keys())
    # print(data['Time Series (5min)']['2024-01-31 19:50:00'].keys())

    df = pd.DataFrame(data['Time Series (5min)'])
    print(df['2024-02-01 19:55:00'])


    ## --- Classes ---

    class Stock:
        def __init__(self, ticker):
            self.ticker = ticker
            self.name = self.get_stock_name()

        # self.buy_price = get_buy_price()
        # self.sell_price = get_sell_price()

        def get_stock_name(self):
            tick = self.ticker
            link = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={tick}&apikey=4H4XGZE8HAY85MW6'
            r1 = requests.get(link)
            data1 = r1.json()
            return data1['bestMatches'][0]['2. name']


    stock1 = Stock('AAPL')
    print(stock1.name)





import pandas as pd
import numpy as np
import requests
# The API request is below:


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&apikey=ONZOU16MALIX7UNO'

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&apikey=4H4XGZE8HAY85MW6'
r = requests.get(url)
data = r.json()

##print(data.keys())
##print(type(data))

#print(data['Time Series (5min)']['2024-01-31 19:55:00'].keys())
#print(data['Time Series (5min)']['2024-01-31 19:50:00'].keys())

df = pd.DataFrame(data['Time Series (5min)'])
print(df)
df = pd.DataFrame(data['Time Series (5min)'])
print(df['2024-02-01 19:55:00'])


## --- Classes ---

class Stock:
    def __init__(self,ticker):
        self.ticker = ticker
        self.name = self.get_stock_name()
       # self.buy_price = get_buy_price()
        # self.sell_price = get_sell_price()

    def get_stock_name(self):
        tick = self.ticker
        link = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={tick}&apikey=4H4XGZE8HAY85MW6'
        r1 = requests.get(link)
        data1 = r1.json()
        return data1['bestMatches'][0]['2. name']


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



class Order:
    def __init__(self, stock, quantity):
        self.stock = Stock(stock)
        self.quantity = quantity


    def buy_order(self):
        price = self.stock.buy_price
        quantity = self.quantity
        return price*quantity

    def sell_order(self):
        price = self.stock.sell_price
        quantity = self.quantity
        return price*quantity



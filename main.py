# Importing the right packages

import pandas as pd
import numpy as np
import requests


# Functions for orders

def buy_order(stock, quantity):
    price = stock.buy_price
    return price * quantity


def sell_order(stock, quantity):
    price = stock.sell_price
    return price * quantity

# --- Classes ---


class User:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
        self.balance = 10000
        self.portfolio = []


    def add_stock_to_portfolio(self,stock,quantity,cost):
        d = {'name': stock.name, 'quantity': quantity}
        self.portfolio.append(d)
        self.balance = self.balance - cost

    # def portfolio(self):
    #     return self.portfolio

    # def sell(self):
    #     stock_to_sell = input("Please enter the name of the stock you would like to sell ")
    #     Quanity_of_stock = input("Please enter the number of stocks you would like to sell ")


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
        return float(data2['Monthly Time Series']['2023-12-29']['4. close']) # price at the end of december

    def get_sell_price(self):
        tick = self.ticker
        link2 = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={tick}&apikey=4H4XGZE8HAY85MW6'
        r2 = requests.get(link2)
        data2 = r2.json()
        return data2['Monthly Time Series']['2024-02-02']['4. close'] # price at the start of February

# class Order:
#     def __init__(self, stock, quantity):
#         self.stock = Stock(stock)
#         self.quantity = quantity
#
#
#     def buy_order(self):
#         price = self.stock.buy_price
#         quantity = self.quantity
#         return price*quantity
#
#     def sell_order(self):
#         price = self.stock.sell_price
#         quantity = self.quantity
#         return price*quantity


# u1 = User("Utsav Paliwal",1)
# share = Stock('AAPL')
# quantity = 2
#
# total_cost = buy_order(share,quantity)
# if total_cost < u1.balance:
#     u1.add_stock_to_portfolio(share,2,total_cost)
# else:
#     print("Invalid")
#
# print(u1.portfolio)
# print(u1.balance)

#
# #u1.add_stock_to_portfolio()
#
# #print(u1.name,u1.opening_balance,u1.portfolio)
# #u1.buy()
# #u1.sell()
#UN-COMMENT THIS MAIN CODETILL LINE 142
# existing_users = []
# users = []
# while True:
#     current_user = input("Enter your first name.")
#     if current_user in existing_users:
#         print(f'Welcome back {current_user}')
#         for x in users:
#             if x.name == current_user:
#                 share = input("Enter ticker of stock you want to buy.")
#                 stock1 = Stock(share)
#                 quant = input(f'How many shares of {stock1.name} do you want to buy?')
#                 quant = int(quant)
#                 total_cost = buy_order(stock1, quant)
#                 if total_cost < x.balance:
#                     x.add_stock_to_portfolio(stock1, quant, total_cost)
#                     print(f'You have successfully bought {quant} shares of {stock1.name}. Your remaining balance is {x.balance} and your portfolio is {x.portfolio}')
#                 else:
#                     print(f'You do not have enough money to buy {quant} shares of {stock1.name}')
#     else:
#         existing_users.append(current_user)
#         u1 = User(current_user,len(users))
#         users.append(u1)
#         share = input("Enter ticker of stock you want to buy.")
#         stock1 = Stock(share)
#         quant = input(f'How many shares of {stock1.name} do you want to buy?')
#         quant = int(quant)
#         total_cost = buy_order(stock1, quant)
#         if total_cost < u1.balance:
#             u1.add_stock_to_portfolio(stock1,quant, total_cost)
#             print(
#                 f'You have successfully bought {quant} shares of {stock1.name}. Your remaining balance is {u1.balance} and your portfolio is {u1.portfolio}')
#         else:
#             print(f'You do not have enough money to buy {quant} shares of {stock1.name}')


#     user = input("Enter 1 if you know the ticker of the stock. Otherwise, enter 2 to search for a stock by keyword.")
#     if user == '1':
#         try:
#             target_stock = input("Please enter your stock ticker.")
#             stock1 = Stock(target_stock)
#             print(f'You chose stock {stock1.name} with ticker, {stock1.ticker}. The buying price of {stock1.ticker} is {stock1.buy_price}')
#         except IndexError:
#             print("No such stock found. Exiting Program. Please try again")
#             break
#     elif user == '2':
#         print("Stock not found!")

# share = Stock('AAPL')
# print(share.name)
#
# total_cost = buy_order(share,2)
# print(total_cost)

def buy_stock_for_user(user):
    share = input("Enter ticker of stock you want to buy: ")
    stock1 = Stock(share)
    print(f'{stock1.name} is currently trading at a buy price')
    quant = input(f'How many shares of {stock1.name} do you want to buy? ')
    quant = int(quant)
    total_cost = buy_order(stock1, quant)

    if total_cost < user.balance:
        user.add_stock_to_portfolio(stock1, quant, total_cost)

        print(f'You have successfully bought {quant} shares of {stock1.name}. Your remaining balance is {user.balance} and your portfolio consists of:')
        for s in user.portfolio:
            print(f"Stock name: {s['name']} | Quantity: {s['quantity']}")
    else:
        print(f'You do not have enough money to buy {quant} shares of {stock1.name}')


existing_users = []
users = []
while True:
    current_user = input("Enter your first name.")
    if current_user in existing_users:
        for x in users:
            if x.name == current_user:
                print(f'Welcome back {current_user}')
                buy_stock_for_user(x)
    else:
        existing_users.append(current_user)
        u1 = User(current_user,len(users))
        users.append(u1)
        print(f'Welcome {current_user}')
        buy_stock_for_user(u1)



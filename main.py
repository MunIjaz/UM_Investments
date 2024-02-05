# Importing the right packages

import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt


# Functions for orders
def buy_order(stock, quantity):
    price = float(stock.buy_price)
    return price * int(quantity)


def sell_order(stock, quantity):
    price = float(stock.sell_price)
    return price * int(quantity)

# --- Classes ---


class User:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
        self.balance = 10000
        self.portfolio = []
        self.port_hist = []

    def add_stock_to_portfolio(self,stock,quantity,cost):
        self.port_hist.append(self.balance)
        stock_exist = 0
        for a in self.portfolio:
            if a['name'] == stock.name:
                stock_exist = 1

        if stock_exist == 1:
            for b in self.portfolio:
                if b['name'] == stock.name:
                    b['quantity'] = b['quantity'] + quantity
                    self.balance = self.balance - cost
        else:
            d = {'name': stock.name, 'quantity': quantity}
            self.portfolio.append(d)
            self.balance = self.balance - cost

    def remove_stock_from_portfolio(self,stock,quantity,cost):
        self.port_hist.append(self.balance)
        stock_empty = 0
        for c in self.portfolio:
            if c['name'] == stock.name:
                if quantity > c['quantity']:
                    print("You are trying to sell more shares than you own. Please try again.")
                    return 1
                else:
                    c['quantity'] = c['quantity'] - quantity
                    self.balance = self.balance + cost
                    if c['quantity'] == 0:
                        self.portfolio.remove(c)

    def plot_portfolio(self):
        ax = [d for d in range(len(self.port_hist))]
        plt.plot(ax,self.port_hist)
        plt.show()
        plt.close()



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


def buy_stock_for_user(user):
    share = input("Enter ticker of stock you want to buy: ")
    stock1 = Stock(share)
    intent = input(f'{stock1.name} is currently trading at a buy price of {stock1.buy_price}. Are you sure you want to buy it? Y/N')
    if intent.upper() == 'Y':
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
    elif intent.upper() == 'N':
        print("Try another stock.")
    else:
        print("Invalid input, Program aborted. Start again")


def sell_stock_for_user(user):
    over_limit = 0
    share = input("Enter ticker of stock you want to sell: ")
    stock1 = Stock(share)
    intent = input(f'{stock1.name} is currently trading at a sell price of {stock1.sell_price}. Are you sure you want to sell it? Y/N')
    if intent.upper() == 'Y':
        quant = input(f'How many shares of {stock1.name} do you want to sell? ')
        quant = int(quant)
        total_cost = sell_order(stock1, quant)
        user.remove_stock_from_portfolio(stock1, quant, total_cost)
        if over_limit != 1:
            print(f'You have successfully sold {quant} shares of {stock1.name}. Your new balance is {user.balance} and your portfolio consists of:')
            for s in user.portfolio:
                print(f"Stock name: {s['name']} | Quantity: {s['quantity']}")
    elif intent.upper() == 'N':
        print("Try another stock.")
    else:
        print("Invalid input, Program aborted. Start again")


print("* * * * * * WELCOME TO UM INVESTMENTS! * * * * * *")
print("* * * * * * * * INSTRUCTIONS! * * * * * * * *")
print("This program uses your first name to identify you. Enter your name and choose what you want to do!")
print("Once you are done with one operation, you can either leave and let the next user use the program "
      "or enter your name again to continue using the program")

existing_users = []
users = []
while True:
    current_user = input("Enter your first name.")
    if current_user in existing_users:
        for x in users:
            if x.name == current_user:
                print(f'Welcome back {current_user}')
                buy_sell = input("Would you like to buy stock, sell stock or plot your portfolio over time? buy/sell/plot")
                if buy_sell.lower() == 'buy':
                    buy_stock_for_user(x)
                elif buy_sell.lower() == 'sell':
                    sell_stock_for_user(x)
                elif buy_sell.lower() == 'plot':
                    x.plot_portfolio()
                else:
                    print("Invalid input, Program aborted. Start again")
    else:
        existing_users.append(current_user)
        u1 = User(current_user,len(users))
        users.append(u1)
        print(f'Welcome {current_user}')
        buy_sell = input("Would you like to buy stock, sell stock or plot your portfolio over time? buy/sell/plot")
        if buy_sell.lower() == 'buy':
            buy_stock_for_user(u1)
        elif buy_sell.lower() == 'sell':
            sell_stock_for_user(u1)
        elif buy_sell.lower() == 'plot':
            u1.plot_portfolio()
        else:
            print("Invalid input, Program aborted. Start again")



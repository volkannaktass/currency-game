 #!/usr/bin/python3
import random
import time
import math

# global inflation
# global inflation_rate 
class Currency():
    def __init__(self,Dolar,Euro,Pound,TL):
        print("Entering Currency Units")
        self.Dolar = Dolar
        self.Euro = Euro
        self.Pound = Pound
        self.TL = TL
    
class Bank(Currency):
    def __init__(self,usd_amount=50000000,eur_amount=40000000,gbp_amount=30000000,try_amount=10000000,players_usd=1000,players_eur=1000,players_gbp=1000,players_try=1000):
        super().__init__(Dolar,Euro,Pound,TL)
        print("Safe of the Bank")
        self.usd_amount = usd_amount
        self.eur_amount = eur_amount
        self.gbp_amount = gbp_amount
        self.try_amount = try_amount
        self.players_usd = players_usd
        self.players_eur = players_eur
        self.players_gbp = players_gbp
        self.players_try = players_try

class Exchange_Rate():
    def __init__(self,usd_value=0.050,eur_value=0.030,gbp_value=0.025,try_value):
        self.usd_value = usd_value
        self.eur_value = eur_value
        self.gbp_value = gbp_value
        self.try_value = try_value

class Buying_Selling_Price():
    def __init__(self,usd_buy_price,eur_buy_price,gbp_buy_price,try_buy_price):
        self.usd_buy_price = usd_buy_price
        self.eur_buy_price = eur_buy_price
        self.gbp_buy_price = gbp_buy_price
        self.try_buy_price = try_buy_price
#    def take_money_change():
#        print("Which type of change do you want?")
    def 
    
    
        
print("Inflation Rate: 5\n")
print("You have 1000$, 1000€, 1000£ and 1000₺ ")







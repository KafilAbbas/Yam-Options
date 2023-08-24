import datetime
import time

def get_strike_price( option, spot_price ,r = 5):
    spot_price  = int(round(spot_price,-2))
    list_of_the_strike_prices = []
    gap = 0
    if option == 'BANKNIFTY':
        gap = 100
    elif option == 'NIFTY':
        gap = 50
    start_price = spot_price - r*gap
    for i in range(2*r+1):
        list_of_the_strike_prices.append(start_price + i*gap)
    return list_of_the_strike_prices

def token_with_symbol(token,symbol):
    lst = {}
    for i in range(len(token)):
        lst[token[i]] = symbol[i] 
    return lst
def find_field_index(field):
    field_index = {}
    for i in range(len(field)):
        field_index[field[i]] = i+1
    return field_index
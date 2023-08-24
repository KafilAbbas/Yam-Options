from NorenRestApiPy.NorenApi import NorenApi
from datetime import datetime
from api_helper import ShoonyaApiPy
import logging
import time
import pandas as pd
import numpy as np
import datetime
from findexpiry import get_expiry,get_token
import xlwings as xw
from totp import get_totp
import xlsxwriter
import os
import json
import multiprocessing
# logging.basicConfig(level=logging.DEBUG)


# excel_file = 'dataextrator.xlsx'
# book = xw.Book(excel_file)


# 'strike_lst':[],'symbol_lst':[],'token_lst':{},'instrument_lst':[],'index':''
api = ShoonyaApiPy()   # dont remove or touch #to start the make a object of class ShoonyaApiPy 
feed_opened = False
take_data = 0        # used to open and close the feed data to come inside the programe
stocks = {'NIFTY':{'option':'NIFTY','exchange':'NFO','expiry':{'1':{'strike_lst':[],'symbol_lst':[],'token_lst':{},'instrument_lst':[],'index':'NIFTY1'},'2':{'strike_lst':[],'symbol_lst':[],'token_lst':{},'instrument_lst':[],'index':'NIFTY2'}}},
          'BANKNIFTY':{'option':'BANKNIFTY','exchange':'NFO','expiry':{'1':{'strike_lst':[],'symbol_lst':[],'token_lst':{},'instrument_lst':[],'index':'BANKNIFTY1'},'2':{'strike_lst':[],'symbol_lst':[],'token_lst':{},'instrument_lst':[],'index':'BANKNIFTY2'}}},
          'FINNIFTY':{'option':'FINNIFTY','exchange':'NFO','expiry':{'1':{'strike_lst':[],'symbol_lst':[],'token_lst':{},'instrument_lst':[],'index':'FINNIFTY1'},'2':{'strike_lst':[],'symbol_lst':[],'token_lst':{},'instrument_lst':[],'index':'FINNIFTY2'}}},
          'MIDCPNIFTY':{'option':'MIDCPNIFTY','exchange':'NFO','expiry':{'1':{'strike_lst':[],'symbol_lst':[],'token_lst':{},'instrument_lst':[],'index':'MIDCPNIFTY1'},'2':{'strike_lst':[],'symbol_lst':[],'token_lst':{},'instrument_lst':[],'index':'MIDCPNIFTY2'}}},
          'CRUDEOIL':{'option':'CRUDEOIL','exchange':'MCX','expiry':{'1':{'strike_lst':[],'symbol_lst':[],'token_lst':{},'instrument_lst':[],'index':'CRUDEOIL1'},'2':{'strike_lst':[],'symbol_lst':[],'token_lst':{},'instrument_lst':[],'index':'CRUDEOIL2'}}},
          'NATURALGAS':{'option':'NATURALGAS','exchange':'MCX','expiry':{'1':{'strike_lst':[],'symbol_lst':[],'token_lst':{},'instrument_lst':[],'index':'NATURALGAS1'},'2':{'strike_lst':[],'symbol_lst':[],'token_lst':{},'instrument_lst':[],'index':'NATURALGAS2'}}}
          }
spot_token_with_option = {}
spot_token = []
token_to_index = {}
final_instrument_lst = []
spot_instrument = []
index_to_array = {}
index_to_update = []
def find_field_index(field):
    field_index = {}
    for i in range(len(field)):
        field_index[field[i]] = i+1
    return field_index
prev_time = time.time()
field = ['pp','ls','ti','lp','pc','c','o','h','l','ap','v','oi','poi','bp1','sp1','bq1','sq1' ]
field_index = find_field_index(field)
spot_prices_dict = {}
strike_to_index_for_spot = {}


def get_strike_price( option, spot_price ,r = 5): 
    spot_price  = int(round(spot_price,-2))
    list_of_the_strike_prices = []
    gap = 0
    if option == 'BANKNIFTY':
        gap = 100
    elif option == 'NIFTY' or option == 'CRUDEOIL' or option == 'FINNIFTY':
        gap = 50
    elif option == 'MIDCPNIFTY':
       gap = 25
    elif option == 'NATURALGAS':
       gap = 5
    start_price = spot_price - r*gap
    for i in range(2*r+1):
        list_of_the_strike_prices.append(start_price + i*gap)
    return list_of_the_strike_prices



def login():
  while True:
    uid    = 'FA128077'
    password = 'Yaali@110'
    print("enter password 2: ",end="")
    factor2 = input()
    if factor2 == "kafilandfazil":
       factor2 = get_totp()
    vc      = 'FA128077_U'
    app_key = '73e364840528bf59997fc08e26f9a93a'
    imei    = 'abc1234'
    ret = api.login(userid=uid, password=password, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
    try:
      if ret['stat'] == "Ok":
        print("login was sucessful")
        break
    except:
      if True:
        print("invalid totp ")



def update_data(index,tick_data):
  global field,index_to_array,field_index,token_to_index,index_to_update
  np_array = index_to_array[index[0]]
  if index[0] not in index_to_update:  
     index_to_update.append(index[0])
  # print(index_to_update)
  # print(tick_data)
  token = tick_data['tk']
  row = int(token_to_index[token][1]) - 1
  final_fields = { field: tick_data[field] for field in set(field) & set(tick_data.keys())}
  for i in final_fields:
    col = int(field_index[i]) - 1
    np_array[row,col] = round(float(tick_data[i]),3)



def update_spot(token,tick_data):
   global spot_token_with_option,spot_prices_dict
   for i in spot_token_with_option.keys():
      if str(token) == spot_token_with_option[i]:
         option = i
         break
   spot_prices_dict[option] = tick_data['lp']
   with open('stock_data/spot_price.json','w') as final:
            json.dump(spot_prices_dict, final, indent=4)



def Run_websocket():
  global feed_opened

  def event_handler_feed_update(tick_data):
    global feed_opened,token_to_index,spot_token
    token = tick_data['tk']
    if feed_opened == False:
       pass
    
    if str(token) in spot_token:
       update_spot(token,tick_data)
    else:
      index = token_to_index[token]
      update_data(index,tick_data)

  def event_handler_order_update(tick_data):
      print(f"Order update {tick_data}")
  def open_callback():
      global feed_opened
      feed_opened = True
      print("Started the websocket")
  def close_callback():
      global feed_opened
      print("Closing the websocket")
      feed_opened = False

  api.start_websocket( order_update_callback=event_handler_order_update,subscribe_callback=event_handler_feed_update, socket_open_callback=open_callback, socket_close_callback = close_callback)



def make_instrument(exchange,token_list):
  lst = []
  for i in token_list:
    lst.append(exchange+'|'+ str(i) )
  return lst



def get_symbols_for_strike_price(option , expiry_date, strike_lst, j = 10):   # give expiry date as an array of 2 dates for crude oil first one is 
    list_for_final_symbols = []                                 # for future and second one is for the option so to get correct data
    # list_of_the_strike_prices = get_strike_lst(option,expiry_date1,10)
    list_of_the_strike_prices = strike_lst
    # print(list_of_the_strike_prices)
    for i in list_of_the_strike_prices:
        list_for_final_symbols.append(option + expiry_date +'P' + str(i))
    for i in list_of_the_strike_prices:
        list_for_final_symbols.append(option + expiry_date +'C' + str(i))
    return list_for_final_symbols




def get_strike_lst(option,expiry,i=10):
    global spot_token_with_option,spot_token
    if option == 'BANKNIFTY':
        spot_token_with_option['BANKNIFTY'] = str(26009)
        spot_token.append(str(26009))
        t = api.get_quotes('NSE', '26009')
        spot_price = float(t['lp'])
    elif option == 'NIFTY':
        spot_token_with_option['NIFTY'] = str(26000)
        spot_token.append(str(26000))
        t = api.get_quotes('NSE', '26000')
        spot_price = float(t['lp'])
    elif option == 'MIDCPNIFTY':
        spot_token_with_option['MIDCPNIFTY'] = str(26074)
        spot_token.append(str(26074))
        t = api.get_quotes('NSE', '26074')
        spot_price = float(t['lp'])
    elif option == 'FINNIFTY':
        spot_token_with_option['FINNIFTY'] = str(26037)
        spot_token.append(str(26037))
        t = api.get_quotes('NSE', '26037')
        spot_price = float(t['lp'])
    elif option == 'CRUDEOIL':
        token = api.searchscrip(exchange = 'MCX', searchtext = 'CRUDEOIL'+expiry)['values'][0]['token']
        spot_token_with_option['CRUDEOIL'] =(token)
        spot_token.append((token))
        t = api.get_quotes('MCX', token)
        spot_price = float(t['lp'])
    elif option == 'NATURALGAS':
        token = api.searchscrip(exchange = 'MCX', searchtext = 'NATURALGAS'+expiry)['values'][0]['token']
        spot_token_with_option['NATURALGAS'] = (token)
        spot_token.append((token))
        t = api.get_quotes('MCX', token)
        spot_price = float(t['lp'])
    return get_strike_price(option,spot_price,i)



class websocket_use():

  def connect(self):
    Run_websocket()

  def start(self,intstument_list):
    global tf
    global feed_opened
    while(feed_opened==False):
      pass
    api.subscribe(intstument_list)

  def unsubscribe(self,intstument_list):
    api.unsubscribe(intstument_list)

  def close(self):
    api.close_websocket()



def strike_with_index_for_spot(expiry_dates):        # only run once on start
   global stocks
   for i in expiry_dates.keys():
      option = i
      if i == 'CRUDEOILFUT' or i == 'NATURALGASFUT':
         continue
      if option == 'CRUDEOIL':
        expiry = expiry_dates['CRUDEOILFUT']
      elif option == 'NATURALGAS':
        expiry = expiry_dates['NATURALGASFUT']
      else:
        expiry = expiry_dates[i]
        
      with open('stock_data/strike_price.json','r') as final:
            json_decoded = json.load(final)

      json_decoded[option]= stocks[option]['expiry']['1']['strike_lst'] 

      with open('stock_data/strike_price.json','w') as final:
            json.dump(json_decoded, final, indent=4)
      



def helper_strike_lst(expiry_dates):
   global stocks
   for i in expiry_dates.keys():
      option = i
      if i == 'CRUDEOILFUT' or i == 'NATURALGASFUT':
         continue
      if option == 'CRUDEOIL':
        expiry = expiry_dates['CRUDEOILFUT']
      elif option == 'NATURALGAS':
        expiry = expiry_dates['NATURALGASFUT']
      else:
        expiry = expiry_dates[i]
      # print((expiry[0]))
      stocks[option]['expiry']['1']['strike_lst'] = get_strike_lst(option,expiry[0],i=10)
      stocks[option]['expiry']['2']['strike_lst'] = stocks[option]['expiry']['1']['strike_lst']
      # print(stocks[option]['expiry']['1']['strike_lst'])
      # print()
      # print()
      # print(stocks[option]['expiry']['2']['strike_lst'])



def helper_symbol_lst(expiry_dates):
   global stocks
   for i in expiry_dates.keys():
      option = i
      if i == 'CRUDEOILFUT' or i == 'NATURALGASFUT':
         continue
      else:
        expiry = expiry_dates[i]
      strike_lst = stocks[option]['expiry']['1']['strike_lst']
      stocks[option]['expiry']['1']['symbol_lst'] = get_symbols_for_strike_price(option,expiry[0],strike_lst,10)
      stocks[option]['expiry']['2']['symbol_lst'] = get_symbols_for_strike_price(option,expiry[1],strike_lst,10)



def helper_token_lst(expiry_dates):
   global stocks
   for i in expiry_dates.keys():
      option = i
      if i == 'CRUDEOILFUT' or i == 'NATURALGASFUT':
         continue
      else:
        expiry = expiry_dates[i]
      exchange = stocks[option]['exchange']
      stocks[option]['expiry']['1']['token_lst'] = get_token(exchange,stocks[option]['expiry']['1']['symbol_lst'])
      stocks[option]['expiry']['2']['token_lst'] = get_token(exchange,stocks[option]['expiry']['2']['symbol_lst'])



def helper_instrument_lst(expiry_dates):
   global stocks
   for i in expiry_dates.keys():
      option = i
      if i == 'CRUDEOILFUT' or i == 'NATURALGASFUT':
         continue
      else:
        expiry = expiry_dates[i]
      exchange = stocks[option]['exchange']
      stocks[option]['expiry']['1']['instrument_lst'] = make_instrument(exchange,stocks[option]['expiry']['1']['token_lst'])
      stocks[option]['expiry']['2']['instrument_lst'] = make_instrument(exchange,stocks[option]['expiry']['2']['token_lst'])


def make_spot_instrument():
    global spot_token_with_option,spot_instrument
    for i in spot_token_with_option.keys():
      if i =='NIFTY' or i == 'BANKNIFTY' or i == 'FINNIFTY' or i == 'MIDCPNIFTY':
        spot_instrument.append('NSE|'+(spot_token_with_option[i]))
      elif i == 'CRUDEOIL' or i=='NATURALGAS':
         spot_instrument.append('MCX|'+(spot_token_with_option[i]))
    return spot_instrument

def helper_token_index(token_lst,index):
   lst = {}
   for i in token_lst:
      lst[i] = [index,token_lst[i]]
   return lst



def get_strike_to_index_for_spot():
   global stocks,strike_to_index_for_spot
   for i in  stocks.keys():
      lst = stocks[i]['expiry']['1']['strike_lst']
      strike_to_index_for_spot[i] = {}
      for j in range(len(lst)):
         strike_to_index_for_spot[i][lst[j]] = [j+1]

   with open('stock_data/strike_price.json','w') as final:
      json.dump(strike_to_index_for_spot, final, indent=4)    
    



def final_helper(expiry_dates):
   global stocks,token_to_index,final_instrument_lst,spot_token,spot_instrument
   for i in expiry_dates.keys():
      option = i
      if i == 'CRUDEOILFUT' or i == 'NATURALGASFUT':
         continue
      token_to_index.update(helper_token_index(stocks[option]['expiry']['1']['token_lst'],stocks[option]['expiry']['1']['index']))
      token_to_index.update(helper_token_index(stocks[option]['expiry']['2']['token_lst'],stocks[option]['expiry']['2']['index']))
      final_instrument_lst.extend(stocks[option]['expiry']['1']['instrument_lst'])
      final_instrument_lst.extend(stocks[option]['expiry']['2']['instrument_lst'])
   final_instrument_lst.extend(spot_instrument)



def make_array():
   array = np.random.rand(42,17)
   for i in range(42):
      for j in range(17):
         array[i][j] = 0
   return array

def connect_index_array(expiry_dates):
   global stocks,index_to_array
   for i in expiry_dates.keys():
      option = i
      if i == 'CRUDEOILFUT' or i == 'NATURALGASFUT':
         continue
      # index_to_array[stocks[option]['expiry']['1']['index']] = np.random.rand(42,17)
      # index_to_array[stocks[option]['expiry']['2']['index']] = np.random.rand(42,17)
      index_to_array[stocks[option]['expiry']['1']['index']] = make_array()
      index_to_array[stocks[option]['expiry']['2']['index']] = make_array()



def make_df(np_arr):
  np_tra = np_arr.transpose()
  df = pd.DataFrame({'Price precision': np_tra[0], 'Lot size': np_tra[1], 'Tick size':np_tra[2],'LTP':np_tra[3],'Percentage change':np_tra[4],'Close price':np_tra[5],'Open price':np_tra[6],'High price':np_tra[7],'Low price':np_tra[8],'Average trade price':np_tra[9],'volume':np_tra[10],'OI':np_tra[11],'POI':np_tra[12],'Best Buy Price 1':np_tra[13],'Best Sell Price 1':np_tra[14],'Best Buy Quantity 1':np_tra[15],'Best Sell Quantity 1':np_tra[16]})
  return df



def find_COI(df):
  OI = df["OI"]
  POI = df["POI"]
  COI = OI.subtract(POI)
  return COI



def make_option_chain(strike_lst,np_array):
  df = make_df(np_array)                    # df index is default 0 to n
  # print(df)
  size = len(list(np_array.transpose()[0]))//2
  # print(size)
  puts = df.loc[0:size-1,["LTP","Percentage change","volume","OI"]]
  # print(puts)     # so put index as 0 to size not from 1 to size 
  COI = find_COI(df)
  # print(COI)
  puts.insert(3,"COI",COI,True)
  put_col = pd.MultiIndex.from_tuples([('PUTS', col) for col in puts.columns])
  # put_col = pd.MultiIndex.from_product([['PUTS'],puts.columns])
  puts.columns = put_col
  puts.index = list(range(1,size+1))
  calls = df.loc[size:2*size,["OI","volume","Percentage change","LTP"]]
  calls.insert(1,"COI",COI,True)
  call_col = pd.MultiIndex.from_tuples([('CALL', col) for col in calls.columns])
  calls.columns = call_col
  calls.index = puts.index
  final_OC = pd.concat([calls, puts], axis=1)
  final_OC.insert(5,"Strike",strike_lst,True)
  return final_OC



def get_strike_lst_from_index(index):
  global stocks
  if index == 'NIFTY1' or index == 'NIFTY2':
      return stocks['NIFTY']['expiry']['1']['strike_lst']
  elif index == 'BANKNIFTY1' or index == 'BANKNIFTY2':
      return stocks['BANKNIFTY']['expiry']['1']['strike_lst']
  elif index == 'FINNIFTY1' or index == 'FINNIFTY2':
      return stocks['FINNIFTY']['expiry']['1']['strike_lst']
  elif index == 'MIDCPNIFTY1' or index == 'MIDCPNIFTY2':
      return stocks['MIDCPNIFTY']['expiry']['1']['strike_lst']
  elif index == 'CRUDEOIL1' or index == 'CRUDEOIL2':
      return stocks['CRUDEOIL']['expiry']['1']['strike_lst']
  elif index == 'NATURALGAS1' or index == 'NATURALGAS2':
      return stocks['NATURALGAS']['expiry']['1']['strike_lst'] 



def check_excel():
   global book,index_to_array
   try:
    book = xlsxwriter.Workbook('dataextrator.xlsx')
    for i in index_to_array.keys():
      worksheet = book.add_worksheet(name = i)
    book.close()
   except:
      print('excel already opened')
   excel_file = 'dataextrator.xlsx'
   book = xw.Book(excel_file)
      
      

def write_to_excel():
  global take_data,index_to_array,index_to_update,prev_time
  while take_data != 0:
    curr_time = time.time()
    # print(curr_time - prev_time)
    if curr_time - prev_time >= 600:
       prev_time = curr_time
       break 
    try:
      for i in index_to_update:
        OC = make_option_chain(get_strike_lst_from_index(i),index_to_array[i])
        # book.sheets(i).range('A1').value = OC
        OC.to_csv(r"./data" +'/'+ i + ".csv",index = False)
        # print(i)
        index_to_update.remove(i)
      time.sleep(0.25)
    except:
      print('an error occured')
      continue

def reconnect():
   global socket
   socket.unsubscribe(final_instrument_lst)
   socket.close()
   time.sleep(1)
   socket = websocket_use()
   socket.connect()
   socket.start(final_instrument_lst)

def lets_start():
  global take_data,socket
  expiry_dates = get_expiry()
  data = pd.DataFrame(expiry_dates)
  data.to_csv(r"./data" +'/'+ 'expiry' + ".csv",index=False)
  # print(expiry_dates)
  login()
  helper_strike_lst(expiry_dates)
  helper_symbol_lst(expiry_dates)
  print('finding tokens it may take few min')
  helper_token_lst(expiry_dates)
  print('finding token list done')
  helper_instrument_lst(expiry_dates)
  make_spot_instrument()
  final_helper(expiry_dates)
  get_strike_to_index_for_spot()
  connect_index_array(expiry_dates)
  socket = websocket_use()
  socket.connect()
  socket.start(final_instrument_lst)
  time.sleep(2)
  take_data = 1

  # socket.unsubscribe(final_instrument_lst)
  # socket.close()

if __name__ == "__main__":
  lets_start()
  # j = int(input())
  while True:
    write_to_excel()
    reconnect()

  # check = multiprocessing.Value('i', 1)
  # check = take_data
  # parent_conn, child_conn = multiprocessing.Pipe()
  # process = multiprocessing.Process(target=write_to_excel, args=(check,child_conn))
  # process.start()
  # # write_to_excel(check)
  # print('to stop write to excel type 1')
  # j = int(input())
  # if j == 1:
  #   parent_conn.send(1)
  #   process.join()
from NorenRestApiPy.NorenApi import NorenApi
from datetime import datetime
from symbols import token_with_symbol
from symbols import find_field_index
from symbols import get_strike_price
from api_helper import ShoonyaApiPy
import logging
import time
import pandas as pd
import numpy as np
import datetime
from totp import get_totp
#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)
import xlwings as xw
excel_file = 'optiondata.xlsx'
book = xw.Book(excel_file)
sheets = book.sheets('sheet1')
sheets2 = book.sheets('sheet3')
# start of our program
api = ShoonyaApiPy()
feed_opened = False
field = ['pp','ls','ti','lp','pc','c','o','h','l','ap','v','oi','poi','bp1','sp1','bq1','sq1' ]
# field = ['pp','ls','ti','lp','pc','c','o','h','l','ap','v','oi','poi','bp1','sp1','bq1','sq1' ]
field_index = find_field_index(field)
# field_index = {'pp':'1','ls':'2','ti':'3','lp':'4','pc':'5','c':'6','o':'7','h':'8','l':'9','ap':'10','v':'11','oi':'12','poi':'13','bp1':'14','sp1':'15','bq1':'16','sq1':'17'}
len(field_index)
print(field_index)
lst = []
token_list = {}
visited = []
count = 0
# np_array = np.random.rand(11,34)
take_data = 0
Prev_time = int(time.time())
# print(np_array)


def login():

  #credentials
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
    # print(password)
    #make the api call
    ret = api.login(userid=uid, password=password, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
    # print(ret['stat'])
    # print("what the hell ")
    # continue
    try:
      if ret['stat'] == "Ok":
        print("login was sucessful")
        break
    except:
      if True:
        print("invalid totp ")
  
def find_token_list(lst):
  lst_token = {}
  for i in range(len(lst)):
    check = api.searchscrip(exchange = 'NFO', searchtext = lst[i])
    lst_token[check["values"][0]["token"]] = i + 1
  # print(lst_token)
  return(lst_token)

def Run_websocket():
  global feed_opened

  def event_handler_feed_update(tick_data):
      global tf,lst,take_data,count
      tf = tick_data
      if count == len(lst) - 2:
        print("websocket connected sending data ")
      if take_data == 0 and count != len(lst) - 1:
        # while count != len(lst) - 1:
        if tf['t'] == 'tk' and tf['tk'] not in visited:
          update_data()
          visited.append(tf['tk'])
          count = count + 1
        
      else:
        if take_data == 0:
          take_data = 1
        update_data()

      # print(f"feed update {tick_data}")

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



def make_instrument(token_list,exchange = 'NFO'):
  lst = []
  for i in token_list:
    lst.append(exchange+'|'+ str(i) )
  return lst


def get_strike_lst(option,i=5):
    if option == 'BANKNIFTY':
        t = api.get_quotes('NSE', '26009')
        spot_price = float(t['lp'])
    elif option == 'NIFTY':
        t = api.get_quotes('NSE', '26000')
        spot_price = float(t['lp'])
    return get_strike_price(option,spot_price,i)



def get_symbols_for_strike_price(option ,i = 5,expiry_date = '17AUG23'):
    list_for_final_symbols = []
    spot_price = 0
    if option == 'BANKNIFTY':
        t = api.get_quotes('NSE', '26009')
        spot_price = float(t['lp'])
    elif option == 'NIFTY':
        t = api.get_quotes('NSE', '26000')
        # api.get_quotes('MCX', '253942')
        spot_price = float(t['lp'])
    list_of_the_strike_prices = get_strike_price(option,spot_price,i)
    print(list_of_the_strike_prices)
    for i in list_of_the_strike_prices:
        list_for_final_symbols.append(option + expiry_date +'P' + str(i))
    for i in list_of_the_strike_prices:
        list_for_final_symbols.append(option + expiry_date +'C' + str(i))
    return list_for_final_symbols


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


def find_COI():
  global df
  OI = df["OI"]
  POI = df["POI"]
  COI = OI.subtract(POI)
  return COI


def make_option_chain(strike_lst):
  global np_array
  df = make_df(np_array)                                  # df index is default 0 to n
  size = len(list(np_array.transpose()[0]))//2
  puts = df.loc[0:size-1,["LTP","Percentage change","volume","OI"]]     # so put index as 0 to size not from 1 to size 
  COI = find_COI()
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


def write_to_excel(strike_lst):
  global np_array
  i = 0
  while take_data != 0:
    OC = make_option_chain(strike_lst)
    OC.to_csv('Book1.csv',index = False)
    jk = OC.to_dict()
    sheets.range('A1').value = OC
    sheets.range("E30").value = i
    sheets.range("E31").value = take_data
    sheets2.range("A1").value = np_array
    i = i+1
    time.sleep(1)


def update_data():
  global np_array
  global field
  global field_index
  global token_list
  token = tf['tk']
  index = int(token_list[token]) - 1
  final_fields = { field: tf[field] for field in set(field) & set(tf.keys())}
  for i in final_fields:
    index2 = int(field_index[i]) - 1
    # print(tf[i])
    np_array[index,index2] = round(float(tf[i]),3)


def make_df(np_arr):
  np_tra = np_arr.transpose()
  df = pd.DataFrame({'Price precision': np_tra[0], 'Lot size': np_tra[1], 'Tick size':np_tra[2],'LTP':np_tra[3],'Percentage change':np_tra[4],'Close price':np_tra[5],'Open price':np_tra[6],'High price':np_tra[7],'Low price':np_tra[8],'Average trade price':np_tra[9],'volume':np_tra[10],'OI':np_tra[11],'POI':np_tra[12],'Best Buy Price 1':np_tra[13],'Best Sell Price 1':np_tra[14],'Best Buy Quantity 1':np_tra[15],'Best Sell Quantity 1':np_tra[16]})
  return df


def which_option():
  print("select the option")
  print("1)Bank Nifty")
  print("2)Nifty")
  option = ''
  user_input = int(input())
  if user_input == 1:
      option = 'BANKNIFTY'
      return option
  elif user_input == 2:
      option = 'NIFTY'
      return option
  else:
     print("please enter a valid option")
     return which_option
  
      
def which_strike():
   print("input the range of the option chain")
   print("eg: if range is 5 then 4 call above and 4 puts both above and below the strice price including the spot price a total of 21 values")
   print("give the range as an integer ")
   print("range must be greater than equal to 1 or or less than equal to 15")
   user_input = int(input())
   if user_input >= 1 and user_input <= 20:
      return user_input
   else:
      print("please enter a valid range")
      return which_strike()
   
   
login()
time.sleep(2)
strike = which_strike()
time.sleep(2)
option = which_option()
print(option)
print(strike)
strike_lst = get_strike_lst(option,strike)
lst = get_symbols_for_strike_price(option,strike)
token_list = find_token_list(lst)
np_array = np.random.rand(len(lst),len(field))
df = make_df(np_array)
oc = token_with_symbol(list(token_list.keys()),lst)
intstument_list = make_instrument(token_list)
# print(lst)
# print(list(token_list.keys()))
# print(len(token_list))
# print(oc)

# intstument_list = ['NFO|47359']  # BANKNIFTY10AUG23C44800
# print(intstument_list)
# print(len(intstument_list))
# Run_websocket(intstument_list)
socket = websocket_use()
socket.connect()
socket.start(intstument_list)
time.sleep(2)
print(pd.DataFrame(np_array))
time.sleep(2)
socket.unsubscribe(intstument_list)
socket.close()
api.logout()
write_to_excel(strike_lst)
for i in range(201):
  write_to_excel(i)
  time.sleep(0.25)
df = pd.DataFrame(np_array)
df = df.reset_index(drop=True)
sheets.range('A1').value = df
df.index = list(range(1,len(lst)+1))


len(list(np_array.transpose()[0]))

# lastBusDay = datetime.datetime.today()
# lastBusDay = lastBusDay.replace(hour=0, minute=0, second=0, microsecond=0)
# ret = api.get_time_price_series(exchange='NFO', token='52346', starttime=lastBusDay.timestamp(), interval=5)
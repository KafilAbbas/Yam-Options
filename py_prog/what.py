# api.searchscrip(exchange = 'MCX', searchtext = 'CRUDEOIL21AUG')['values'][0]['token']
# 253460
# api.get_quotes('MCX', '253460')['lp']
get_strike_lst('BANKNIFTY','21AUG23',i=10)
 get_symbols_for_strike_price('CRUDEOIL' ,['21AUG23','17AUG23'])
CRUDEOIL17AUG23C7200

def find_token_list(exchange,lst):
  lst_token = {}
  for i in range(len(lst)):
    check = api.searchscrip(exchange = exchange, searchtext = lst[i])
    lst_token[check["values"][0]["token"]] = i + 1
  # print(lst_token)
  return(lst_token)
api.searchscrip(exchange = 'MCX', searchtext = 'CRUDEOIL17AUG23C7200')
257369
print(stocks['CRUDEOIL']['expiry']['1']['symbol_lst'])
stocks['CRUDEOIL']['expiry']['1']['strike_lst']
stocks['CRUDEOIL']['exchange']
stocks['BANKNIFTY']['expiry']['2']['token_lst']
print(token_to_index)
OC = make_option_chain(get_strike_lst_from_index('NIFTY1'),index_to_array['NIFTY1'])
socket = websocket_use()
socket.connect()
socket.start(final_instrument_lst)


socket.unsubscribe(final_instrument_lst)
socket.close()
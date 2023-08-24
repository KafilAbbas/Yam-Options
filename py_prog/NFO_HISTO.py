import pandas as pd
import json
import time
import datetime
stocks_list = ['NIFTY1','NIFTY2','BANKNIFTY1','BANKNIFTY2','FINNIFTY1','FINNIFTY2','MIDCPNIFTY1','MIDCPNIFTY2']

while True:
    curr_time = datetime.datetime.now()
    final_JSON = {}
    update_data = 1
    flag = 0
    if not (int(curr_time.strftime("%H%M")) < 1530 and int(curr_time.strftime("%H%M")) >= 915):
        update_data = 0
        flag = 1
        if (int(curr_time.strftime("%H%M")) >= 913 and int(curr_time.strftime("%H%M")) <= 915):
            sleep = 0
        else:
            sleep = 120
        print('sleeping till tomorrow' )
        print(datetime.datetime.now().strftime("%H:%M:%S"))
        time.sleep(sleep)
    if (int(curr_time.strftime("%H%M")) >= 830 and int(curr_time.strftime("%H%M")) < 915) and flag == 1:
        with open('STOCK_HISTO/NFO.json','w') as final:
            json.dump({}, final, indent=4)
            flag = 0
    if update_data == 1:
        # print("writing data at:" ,datetime.datetime.now().strftime("%H:%M:%S"))
        for i in stocks_list:
            try:
                data = pd.read_csv('data/'+ i+'.csv')
            except:
                continue
            newdata = data.to_dict(orient='split')
            final_JSON[i] = {}
            for j in newdata.keys():
                # print(j)
                final_JSON[i][j] = newdata[j]
            # final_JSON[i] = 
            # print(i)
        with open('STOCK_HISTO/NFO.json','r') as final:
            try: 
                json_decoded = json.load(final)
            except:
                continue
            # print(final_JSON)
            json_decoded[curr_time.strftime("%H%M")] ={}
            for j in final_JSON.keys():
                json_decoded[curr_time.strftime("%H%M")][j] = final_JSON[j]
                
        if int(curr_time.strftime('%S')) == 0:
            with open('stock_data/spot_price.json','r') as spot:
                try: 
                    spot_prices = json.load(spot) 
                except:
                    continue 
                json_decoded[curr_time.strftime("%H%M")]['spot'] = spot_prices

            with open('STOCK_HISTO/NFO.json','w') as final:
                json.dump(json_decoded, final, indent=4)
        else:
            with open('STOCK_LIVE/NFO.json','w') as final:
                json.dump(json_decoded, final, indent=4)
            # print(json_decoded)
        sleep_to_next = 2 - float(datetime.datetime.now().strftime("%f"))/1000000
        # print(sleep_to_next)
        time.sleep(sleep_to_next)
        
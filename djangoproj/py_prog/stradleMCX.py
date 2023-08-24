import time
import datetime
import pandas as pd
import json
from findexpiry import find_atm
stock_list = ['CRUDEOIL1','CRUDEOIL2','NATURALGAS1','NATURALGAS2']



while True:
    curr_time = datetime.datetime.now()
    final_JSON = {}
    update_data = 1
    flag = 0
    if  not (int(curr_time.strftime("%H%M")) < 2330 and int(curr_time.strftime("%H%M")) >= 900):
        update_data = 0
        flag = 1
        if (int(curr_time.strftime("%H%M")) >= 858 and int(curr_time.strftime("%H%M")) <= 900):
            sleep = 0
        else:
            sleep = 120
        print('sleeping till tomorrow' )
        print(datetime.datetime.now().strftime("%H:%M:%S"))
        time.sleep(sleep)
    if ((int(curr_time.strftime("%H%M")) >= 830 and int(curr_time.strftime("%H%M")) < 900) and flag == 1):
        for i in stock_list:
            with open('STRADLE/'+i+'.json','w') as final:
                json.dump({}, final, indent=4)
                flag = 0
    if update_data == 1:
        
        with open('stock_data/spot_price.json','r') as spot_list:
            try:
                spot_price_list = json.load(spot_list)
            except:
                continue   
            # print(spot_price_list)
            for i in stock_list:
                spot = float(spot_price_list[i[0:-1]])
                # print(spot)
                atm_price = int(find_atm(i[0:-1],spot))
                # print(atm_price)
                with open('stock_data/strike_price.json','r') as strike_index:
                    try:
                        strike_price_index = json.load(strike_index)
                    except:
                        continue
                    index_for_atm = strike_price_index[i[0:-1]][str(atm_price)][0]
                    # print(index_for_atm)
                try:
                    data = pd.read_csv('data/'+ i+'.csv')
                except:
                    continue
                data = data.to_dict(orient='split')
                # print(data)
                atm_data = data['data'][index_for_atm]
                atm_premium = float(atm_data[4])+float(atm_data[6])
                # print(atm_premium)
                final_data = {'premium':atm_premium,'price':atm_price,'spot':spot}
                
                if int(curr_time.strftime('%S%f')) >= 59000000:
                    with open('STRADLE/'+i+'.json','r') as premium_data:
                        try:
                            data_premium = json.load(premium_data)
                        except:
                            continue
                        data_premium[curr_time.strftime("%H%M")] = final_data
                    with open('STRADLE/'+i+'.json','w') as premium_data:
                        json.dump(data_premium, premium_data, indent=4)
                else:
                    with open('STRADLELIVE/'+i+'.json','w') as premium_data:
                        literally_final = {curr_time.strftime('%H%M'):final_data}
                        json.dump(literally_final, premium_data, indent=4)
        sleep_to_next = 1 - float(datetime.datetime.now().strftime("%f"))/1000000
        time.sleep(sleep_to_next)

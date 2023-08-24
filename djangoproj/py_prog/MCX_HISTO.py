import pandas as pd
import json
import time
import datetime
stocks_list = ['CRUDEOIL1','CRUDEOIL2','NATURALGAS1','NATURALGAS2']

while True:
    curr_time = datetime.datetime.now()
    final_JSON = {}
    update_data = 1
    flag = 0
    print(curr_time.strftime('%S'))
    if not (int(curr_time.strftime("%H%M")) < 2330 and int(curr_time.strftime("%H%M")) >= 900):
        update_data = 0
        if (int(curr_time.strftime("%H%M")) >= 858 and int(curr_time.strftime("%H%M")) <= 900):
            sleep = 0
        else:
            sleep = 120
        print('sleeping till tomorrow')
        print(datetime.datetime.now().strftime("%H:%M:%S"))
        time.sleep(sleep)
    if (int(curr_time.strftime("%H%M")) >= 830 and int(curr_time.strftime("%H%M")) < 900) and flag == 1:
        with open('JSON/MCX.json','w') as final:
            json.dump({}, final, indent=4)
            flag = 0
    if update_data == 1:
        # print(datetime.datetime.now().strftime("%H:%M:%S"))
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
        if int(curr_time.strftime('%S')) == 0: 
            print('yes i am in ')
            with open('STOCK_HISTO/MCX.json','r') as final: 
                json_decoded = json.load(final)
                # print(final_JSON)
                json_decoded[curr_time.strftime("%H%M")] ={}
                for j in final_JSON.keys():
                    # print(j)
                    json_decoded[curr_time.strftime("%H%M")][j] = final_JSON[j]
            with open('STOCK_HISTO/MCX.json','w') as final:
                json.dump(json_decoded, final, indent=4)
                # print(json_decoded)
        else:
            json_decoded = {}
            json_decoded[curr_time.strftime("%H%M%S")] ={}
            for j in final_JSON.keys():
                    # print(j)
                    json_decoded[curr_time.strftime("%H%M%S")][j] = final_JSON[j]
            with open('STOCK_LIVE/MCX.json','w') as final:
                json.dump(json_decoded, final, indent=4)
        sleep_to_next = 2 - float(datetime.datetime.now().strftime("%f"))/1000000
        # print(sleep_to_next)
        time.sleep(sleep_to_next)
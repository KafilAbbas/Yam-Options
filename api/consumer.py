# consumers.py
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class StockUpdatesConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         await self.send(text_data=json.dumps({
#             'message': message
#         }))
# consumers.py

import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import pandas as pd
from djangoproj.settings import BASE_DIR
import os
import time
import datetime
working_days = ['Mon','Tue','Wed','Thu','Fri']
class home(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
class home2(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
class start(AsyncWebsocketConsumer):
     async def connect(self):
        await self.accept()
        while True:
            try:
                data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/expiry.csv'))
            except:
                time.sleep(0.5)
                continue
            newdata = data.to_json(orient='split')
            await self.send(newdata)
            break
class NIFTY1(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.running = True
        self.time = 1.5
        while True:
            try:
                data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/NIFTY1.csv'))
            except:
                continue
            if self.running == False:
                break
            newdata = data.to_json(orient='split')
            await self.send(newdata)
            await asyncio.sleep(self.time)
    async def disconnect(self, close_code):
        self.running = False
        self.time = 0
        self.websocket_disconnect()    
class NIFTY2(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            try:
                data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/NIFTY2.csv'))
            except:
                continue
            newdata = data.to_json(orient='split')
            await self.send(newdata)
            await asyncio.sleep(0.5)
class BANKNIFTY1(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            try:
                data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/BANKNIFTY1.csv'))
            except:
                continue
            newdata = data.to_json(orient='split')
            await self.send(newdata)
            await asyncio.sleep(0.5)

class BANKNIFTY2(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            try:
                data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/BANKNIFTY2.csv'))
            except:
                continue
            newdata = data.to_json(orient='split')
            await self.send(newdata)
            await asyncio.sleep(0.5)
class FINNIFTY1(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            try:
                data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/FINNIFTY1.csv'))
            except:
                continue
            newdata = data.to_json(orient='split')
            await self.send(newdata)
            await asyncio.sleep(0.5)
class FINNIFTY2(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            try:
                data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/FINNIFTY2.csv'))
            except:
                continue
            newdata = data.to_json(orient='split')
            await self.send(newdata)
            await asyncio.sleep(0.5)
class MIDCPNIFTY1(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            try:
                data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/MIDCPNIFTY1.csv'))
            except:
                continue
            newdata = data.to_json(orient='split')
            await self.send(newdata)
            await asyncio.sleep(0.5)
class MIDCPNIFTY2(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            try:
                data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/MIDCPNIFTY2.csv'))
            except:
                continue
            newdata = data.to_json(orient='split')
            await self.send(newdata)
            await asyncio.sleep(0.5)

class CRUDEOIL1(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            try:
                data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/CRUDEOIL1.csv'))
            except:
                continue
            newdata = data.to_json(orient='split')
            await self.send(newdata)
            await asyncio.sleep(0.5)
class CRUDEOIL2(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            try:
                data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/CRUDEOIL2.csv'))
            except:
                continue
            newdata = data.to_json(orient='split')
            await self.send(newdata)
            await asyncio.sleep(0.5)
class NATURALGAS1(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            try:
                data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/NATURALGAS1.csv'))
            except:
                continue
            newdata = data.to_json(orient='split')
            await self.send(newdata)
            await asyncio.sleep(0.5)
class NATURALGAS2(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            try:
                data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/NATURALGAS2.csv'))
            except:
                continue
            newdata = data.to_json(orient='split')
            await self.send(newdata)
            await asyncio.sleep(0.5)
class stradleBANKNIFTY1(AsyncWebsocketConsumer):
    async def connect(self):
        flag = 1
        await self.accept()
        while True:
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLE/BANKNIFTY1.json'))
                data['token'] = 'df'
                # final_json = {'token':'tk','data':data}
                # df = pd.DataFrame(final_json)
                newdata = data.to_json(index=4)
                await self.send(newdata)
                await asyncio.sleep(1)
                break
            except:
                continue
            
        while True:
            if  not ((int(datetime.datetime.now().strftime('%H%M')) < 1530 and int(datetime.datetime.now().strftime('%H%M%S')) >= 91500) and datetime.datetime.now().strftime('%a') not in working_days) :
                break
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLELIVE/BANKNIFTY1.json'))
                if int(datetime.datetime.now().strftime('%S')) == 0 and flag == 1:
                    data['token'] = 'du'
                    flag = 0
                else:
                    data['token'] = 'dc'
                    flag  = 1
            except:
                continue
            newdata = data.to_json(index=4)
            await self.send(newdata)
            await asyncio.sleep(1)
class stradleBANKNIFTY2(AsyncWebsocketConsumer):
    async def connect(self):
        flag = 1
        await self.accept()
        while True:
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLE/BANKNIFTY2.json'))
                data['token'] = 'df'
                # final_json = {'token':'tk','data':data}
                # df = pd.DataFrame(final_json)
                newdata = data.to_json(index=4)
                await self.send(newdata)
                await asyncio.sleep(1)
                break
            except:
                continue
            
        while True:
            if  not ((int(datetime.datetime.now().strftime('%H%M')) < 1530 and int(datetime.datetime.now().strftime('%H%M%S')) >= 91500) and datetime.datetime.now().strftime('%a') not in working_days) :
                break
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLELIVE/BANKNIFTY2.json'))
                if int(datetime.datetime.now().strftime('%S')) == 0 and flag == 1:
                    data['token'] = 'du'
                    flag = 0
                else:
                    data['token'] = 'dc'
                    flag  = 1
            except:
                continue
            newdata = data.to_json(index=4)
            await self.send(newdata)
            await asyncio.sleep(1)
class stradleNIFTY1(AsyncWebsocketConsumer):
    async def connect(self):
        flag = 1
        await self.accept()
        while True:
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLE/NIFTY1.json'))
                data['token'] = 'df'
                # final_json = {'token':'tk','data':data}
                # df = pd.DataFrame(final_json)
                newdata = data.to_json(index=4)
                await self.send(newdata)
                await asyncio.sleep(1)
                break
            except:
                continue
            
        while True:
            if  not ((int(datetime.datetime.now().strftime('%H%M')) < 1530 and int(datetime.datetime.now().strftime('%H%M%S')) >= 91500) and datetime.datetime.now().strftime('%a') not in working_days) :
                break
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLELIVE/NIFTY1.json'))
                if int(datetime.datetime.now().strftime('%S')) == 0 and flag == 1:
                    data['token'] = 'du'
                    flag = 0
                else:
                    data['token'] = 'dc'
                    flag  = 1
            except:
                continue
            newdata = data.to_json(index=4)
            await self.send(newdata)
            await asyncio.sleep(1)
class stradleNIFTY2(AsyncWebsocketConsumer):
    async def connect(self):
        flag = 1
        await self.accept()
        while True:
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLE/NIFTY2.json'))
                data['token'] = 'df'
                # final_json = {'token':'tk','data':data}
                # df = pd.DataFrame(final_json)
                newdata = data.to_json(index=4)
                await self.send(newdata)
                await asyncio.sleep(1)
                break
            except:
                continue
            
        while True:
            if  not ((int(datetime.datetime.now().strftime('%H%M')) < 1530 and int(datetime.datetime.now().strftime('%H%M%S')) >= 91500) and datetime.datetime.now().strftime('%a') not in working_days) :
                break
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLELIVE/NIFTY2.json'))
                if int(datetime.datetime.now().strftime('%S')) == 0 and flag == 1:
                    data['token'] = 'du'
                    flag = 0
                else:
                    data['token'] = 'dc'
                    flag  = 1
            except:
                continue
            newdata = data.to_json(index=4)
            await self.send(newdata)
            await asyncio.sleep(1)
class stradleFINNIFTY1(AsyncWebsocketConsumer):
    async def connect(self):
        flag = 1
        await self.accept()
        while True:
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLE/FINNIFTY1.json'))
                data['token'] = 'df'
                # final_json = {'token':'tk','data':data}
                # df = pd.DataFrame(final_json)
                newdata = data.to_json(index=4)
                await self.send(newdata)
                await asyncio.sleep(1)
                break
            except:
                continue
            
        while True:
            if  not ((int(datetime.datetime.now().strftime('%H%M')) < 1530 and int(datetime.datetime.now().strftime('%H%M%S')) >= 91500) and datetime.datetime.now().strftime('%a') not in working_days) :
                break
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLELIVE/FINNIFTY1.json'))
                if int(datetime.datetime.now().strftime('%S')) == 0 and flag == 1:
                    data['token'] = 'du'
                    flag = 0
                else:
                    data['token'] = 'dc'
                    flag  = 1
            except:
                continue
            newdata = data.to_json(index=4)
            await self.send(newdata)
            await asyncio.sleep(1)
class stradleFINNIFTY2(AsyncWebsocketConsumer):
    
    async def connect(self):
        flag = 1
        await self.accept()
        while True:
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLE/FINNIFTY2.json'))
                data['token'] = 'df'
                # final_json = {'token':'tk','data':data}
                # df = pd.DataFrame(final_json)
                newdata = data.to_json(index=4)
                await self.send(newdata)
                await asyncio.sleep(1)
                break
            except:
                continue
            
        while True:
            if  not ((int(datetime.datetime.now().strftime('%H%M')) < 1530 and int(datetime.datetime.now().strftime('%H%M%S')) >= 91500) and datetime.datetime.now().strftime('%a') not in working_days) :
                break
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLELIVE/FINNIFTY2.json'))
                if int(datetime.datetime.now().strftime('%S')) == 0 and flag == 1:
                    data['token'] = 'du'
                    flag = 0
                else:
                    data['token'] = 'dc'
                    flag  = 1
            except:
                continue
            newdata = data.to_json(index=4)
            await self.send(newdata)
            await asyncio.sleep(1)
class stradleMIDCPNIFTY1(AsyncWebsocketConsumer):
    async def connect(self):
        flag = 1
        await self.accept()
        while True:
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLE/MIDCPNIFTY1.json'))
                data['token'] = 'df'
                # final_json = {'token':'tk','data':data}
                # df = pd.DataFrame(final_json)
                newdata = data.to_json(index=4)
                await self.send(newdata)
                await asyncio.sleep(1)
                break
            except:
                continue
            
        while True:
            if  not ((int(datetime.datetime.now().strftime('%H%M')) < 1530 and int(datetime.datetime.now().strftime('%H%M%S')) >= 91500) and datetime.datetime.now().strftime('%a') not in working_days) :
                break
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLELIVE/MIDCPNIFTY1.json'))
                if int(datetime.datetime.now().strftime('%S')) == 0 and flag == 1:
                    data['token'] = 'du'
                    flag = 0
                else:
                    data['token'] = 'dc'
                    flag  = 1
            except:
                continue
            newdata = data.to_json(index=4)
            await self.send(newdata)
            await asyncio.sleep(1)
class stradleMIDCPNIFTY2(AsyncWebsocketConsumer):
    async def connect(self):
        flag = 1
        await self.accept()
        while True:
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLE/MIDCPNIFTY2.json'))
                data['token'] = 'df'
                # final_json = {'token':'tk','data':data}
                # df = pd.DataFrame(final_json)
                newdata = data.to_json(index=4)
                await self.send(newdata)
                await asyncio.sleep(1)
                break
            except:
                continue
            
        while True:
            if  not ((int(datetime.datetime.now().strftime('%H%M')) < 1530 and int(datetime.datetime.now().strftime('%H%M%S')) >= 91500) and datetime.datetime.now().strftime('%a') not in working_days) :
                break

            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLELIVE/MIDCPNIFTY2.json'))
                if int(datetime.datetime.now().strftime('%S')) == 0 and flag == 1:
                    data['token'] = 'du'
                    flag = 0
                else:
                    data['token'] = 'dc'
                    flag  = 1
            except:
                continue
            newdata = data.to_json(index=4)
            await self.send(newdata)
            await asyncio.sleep(1)
class stradleCRUDEOIL1(AsyncWebsocketConsumer):
    async def connect(self):
        flag = 1
        await self.accept()
        while True:
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLE/CRUDEOIL1.json'))
                data['token'] = 'df'
                # final_json = {'token':'tk','data':data}
                # df = pd.DataFrame(final_json)
                newdata = data.to_json(index=4)
                await self.send(newdata)
                await asyncio.sleep(1)
                break
            except:
                continue
            
        while True:
            # if  not ((int(datetime.datetime.now().strftime('%H%M')) < 2330 and int(datetime.datetime.now().strftime('%H%M%S')) >= 90000) and datetime.datetime.now().strftime('%a') not in working_days) :
            #     break

            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLELIVE/CRUDEOIL1.json'))
                if int(datetime.datetime.now().strftime('%S')) >= 59 and flag == 1:
                    data['token'] = 'du'
                    flag = 0
                else:
                    data['token'] = 'dc'
                    flag  = 1
            except:
                continue
            newdata = data.to_json(index=4)
            await self.send(newdata)
            await asyncio.sleep(1)
class stradleCRUDEOIL2(AsyncWebsocketConsumer):
    async def connect(self):
        flag = 1
        await self.accept()
        while True:
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLE/CRUDEOIL2.json'))
                data['token'] = 'df'
                # final_json = {'token':'tk','data':data}
                # df = pd.DataFrame(final_json)
                newdata = data.to_json(index=4)
                await self.send(newdata)
                await asyncio.sleep(1)
                break
            except:
                continue
            
        while True:
            # if  not ((int(datetime.datetime.now().strftime('%H%M')) < 2330 and int(datetime.datetime.now().strftime('%H%M%S')) >= 90000) and datetime.datetime.now().strftime('%a') not in working_days) :
            #     break

            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLELIVE/CRUDEOIL2.json'))
                if int(datetime.datetime.now().strftime('%S')) >= 59 and flag == 1:
                    data['token'] = 'du'
                    flag = 0
                else:
                    data['token'] = 'dc'
                    flag  = 1
            except:
                continue
            newdata = data.to_json(index=4)
            await self.send(newdata)
            await asyncio.sleep(1)
class stradleNATURALGAS1(AsyncWebsocketConsumer):
    async def connect(self):
        flag = 1
        await self.accept()
        while True:
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLE/NATURALGAS1.json'))
                data['token'] = 'df'
                # final_json = {'token':'tk','data':data}
                # df = pd.DataFrame(final_json)
                newdata = data.to_json(index=4)
                await self.send(newdata)
                await asyncio.sleep(1)
                break
            except:
                continue
            
        while True:
            # if  not ((int(datetime.datetime.now().strftime('%H%M')) < 2330 and int(datetime.datetime.now().strftime('%H%M%S')) >= 90000) and datetime.datetime.now().strftime('%a') not in working_days) :
            #     break

            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLELIVE/NATURALGAS1.json'))
                if int(datetime.datetime.now().strftime('%S')) >= 59 and flag == 1:
                    data['token'] = 'du'
                    flag = 0
                else:
                    data['token'] = 'dc'
                    flag  = 1
            except:
                continue
            newdata = data.to_json(index=4)
            await self.send(newdata)
            sleep_to_next = 1 - float(datetime.datetime.now().strftime("%f"))/1000000
            await asyncio.sleep(sleep_to_next)
class stradleNATURALGAS2(AsyncWebsocketConsumer):
    async def connect(self):
        flag = 1
        await self.accept()
        while True:
            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLE/NATURALGAS2.json'))
                data['token'] = 'df'
                # final_json = {'token':'tk','data':data}
                # df = pd.DataFrame(final_json)
                newdata = data.to_json(index=4)
                await self.send(newdata)
                await asyncio.sleep(1)
                break
            except:
                continue
            
        while True:
            # if  not ((int(datetime.datetime.now().strftime('%H%M')) < 2330 and int(datetime.datetime.now().strftime('%H%M%S')) >= 90000) and datetime.datetime.now().strftime('%a') not in working_days) :
            #     break

            try:
                data = pd.read_json(os.path.join(BASE_DIR,'py_prog/STRADLELIVE/NATURALGAS2.json'))
                if int(datetime.datetime.now().strftime('%S')) >= 59 and flag == 1:
                    data['token'] = 'du'
                    flag = 0
                else:
                    data['token'] = 'dc'
                    flag  = 1
            except:
                continue
            newdata = data.to_json(index=4)
            await self.send(newdata)
            await asyncio.sleep(1)
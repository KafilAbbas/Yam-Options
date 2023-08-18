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

class home(AsyncWebsocketConsumer):
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
import wget
from zipfile import ZipFile
import os
from datetime import datetime
files = ['MCX_symbols.txt.zip','NFO_symbols.txt.zip']
files_txt = ['MCX_symbols.txt','NFO_symbols.txt']
exchange = {"MCX_symbols.txt":['CRUDEOIL','NATURALGAS','CRUDEOILFUT','NATURALGASFUT'],'NFO_symbols.txt':['NIFTY','BANKNIFTY','FINNIFTY','MIDCPNIFTY']}
to_find = {'CRUDEOIL':[',CRUDEOIL,','OPTFUT'],'NATURALGAS':[',NATURALGAS,','OPTFUT'],'CRUDEOILFUT':[',CRUDEOIL,','FUTCOM'],'NATURALGASFUT':[',NATURALGAS,','FUTCOM'],'NIFTY':[',NIFTY,','OPTIDX'],'BANKNIFTY':[',BANKNIFTY,','OPTIDX'],'FINNIFTY':[',FINNIFTY,','OPTIDX'],'MIDCPNIFTY':[',MIDCPNIFTY,','OPTIDX']}
nfo = ['NIFTY','BANKNIFTY','FINNIFTY','MIDCPNIFTY']
mcx = ['CRUDEOIL','NATURALGAS','CRUDEOILFUT','NATURALGASFUT']
final_expiry = {'NIFTY':[],'BANKNIFTY':[],'FINNIFTY':[],'MIDCPNIFTY':[],'CRUDEOIL':[],'NATURALGAS':[],'CRUDEOILFUT':[],'NATURALGASFUT':[]}


def download_txt(files):
    for i in files:
        wget.download('https://api.shoonya.com/' +i , './expiry')
        with ZipFile('./expiry/'+i, 'r') as zip:
            zip.extractall('./expiry/')
        os.remove('./expiry/'+i)


def find_expiry(files_txt,exchange,to_find):
    global final_expiry
    index = 6
    for i in range(len(files_txt)):
        with open('./expiry/'+ files_txt[i], 'r') as fp:
            lines = fp.readlines()
            for j in range(len(exchange[files_txt[i]])):
                option = exchange[files_txt[i]][j]
                # print(option)
                word1 = to_find[option][0]
                word2 = to_find[option][1]
                # print(word1)
                # print(word2)
                for line in lines:
                    if line.find(word1) != -1 and line.find(word2) != -1:
                        target_line = line.split(',')
                        if target_line[index] not in final_expiry[option]:
                            final_expiry[option].append(str(target_line[index]))

                iso_dates = [datetime.strptime(date, "%d-%b-%Y").strftime("%Y-%m-%d") for date in final_expiry[option]]
                sorted_dates = sorted(iso_dates)
                sorted_dates_original_format = [datetime.strptime(date, "%Y-%m-%d").strftime("%d%b%y").upper() for date in sorted_dates]
                final_expiry[option] = sorted_dates_original_format[0:2]
                # print(final_expiry[option])
        index = 5
        # os.remove('./expiry/'+files_txt[i])


def get_token(given_exchange,symbol_lst):
    global files_txt,exchange,to_find,final_expiry,files
    if given_exchange == "MCX":
        file_index = 0
    elif given_exchange == "NFO":
        file_index = 1
    token_lst = {}
    with open('./expiry/'+ files_txt[file_index], 'r') as fp:
        lines = fp.readlines()
        for i in range(len(symbol_lst)):
            word = symbol_lst[i]
            for line in lines:
                if line.find(word) != -1:
                    founded_line = line.split(',')
                    founded_line[1]
                    token_lst[founded_line[1]] = i+1
                    break
    return token_lst

def get_expiry():
    global files_txt,exchange,to_find,final_expiry,files
    download_txt(files)
    find_expiry(files_txt,exchange,to_find)
    return final_expiry
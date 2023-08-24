import xlwings as xw
import time
import numpy as np
from csv import writer
excel_file = 'optiondata.xlsx'
book = xw.Book(excel_file)
sheets = book.sheets('sheet1')
for i in range(10):
    dataframe = sheets.range('B3:L23').value
    writer_object = writer(open("Book1.csv","a", newline=""),delimiter=",")
    writer_object.writerows(dataframe)
    # array = np.array(dataframe)
    # file.writelines(dataframe)
    # file.write('\n')
    print(dataframe)
    time.sleep(5)
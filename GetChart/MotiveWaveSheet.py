








# import the libraries
#------------------------------------------------
from datetime import datetime
import CreateFile

import datetime as dt
import pandas as pd
import openpyxl
import numpy as np
import os

import ImportData







# Set Varibles
#------------------------------------------------
tickerName = 'AAPL'     
filePathExcel = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\Session [20231115_194618]\AAPL\OK AAPL.xlsx"
filePathOutPut = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg'            #C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
flagYahoo = True
flagIBKR = True
imageType= '.png'
     


# Create File:    
#------------------------------------------------    
    # datetime object containing current date and time --- Help Link :- https://www.programiz.com/python-programming/datetime/current-datetime#google_vignette
now = datetime.now()
dt_string = now.strftime("[%Y%m%d_%H%M%S]") # YYmmdd_HHMMSS
sessionSymbol =  "MotiveWave" + ' ' + str(dt_string)
rxFilePath = CreateFile.fun(directory = sessionSymbol, parent_dir = filePathOutPut)






#------------------------------------------------

# Loop 1:-
daySheet = "IBKR 1Day"
indexScope =  '5 secs'         
timeScope = ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']
bookScope = {
            '1 secs' :{'SizeIndex': 0, 'DurationIndex':1, 'DurationLenth': 1, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 1s'     },
            '5 secs' :{'SizeIndex': 1, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 5s'     },
            '10 secs':{'SizeIndex': 2, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':30, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 10s'    },
            '15 secs':{'SizeIndex': 3, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':20, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 15s'    },
            '30 secs':{'SizeIndex': 4, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 30s'    },
            '1 min'  :{'SizeIndex': 5, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':"IBKR 1m"     },
            '2 mins' :{'SizeIndex': 6, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 2m'     },
            '3 mins' :{'SizeIndex': 7, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 3m'     },
            '5 mins' :{'SizeIndex': 8, 'DurationIndex':1, 'DurationLenth': 3, 'Rolling': 6, 'ChartDayDuration':  -1, 'indexTS': "5m", 'SheetName':'IBKR 5m'     },
            '10 mins':{'SizeIndex': 9, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling': 6, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 10m'    },
            '15 mins':{'SizeIndex':10, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 15m'    },
            '20 mins':{'SizeIndex':11, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 20m'    },
            '30 mins':{'SizeIndex':12, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':11, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 30m'    },
            '1 hour' :{'SizeIndex':13, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':16, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 1H'     },
            '2 hours':{'SizeIndex':14, 'DurationIndex':1, 'DurationLenth':34, 'Rolling': 8, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 2H'     },
            '3 hours':{'SizeIndex':15, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':30, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 3H'     },
            '4 hours':{'SizeIndex':16, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':20, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 4H'     },
            '8 hours':{'SizeIndex':17, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':42, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 8H'     },
            '1 day'  :{'SizeIndex':18, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':21, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Day'   },
            '1W'     :{'SizeIndex':19, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1week'  },
            '1M'     :{'SizeIndex':20, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Month' }
            }

# filePathTemp = filePath + " Temp " + ".xlsx"






# Import  data
#------------------------------------------------
dft = ImportData.fun2 (filePath_fun = filePathExcel , bookName = bookScope[indexScope]['SheetName'])    #   'YAHOO'      'IBKR 30m'  IBKR 1H
df=dft
# print(df)


# Start Extend Data to exel
#------------------------------------------------
excelSymbol = "OK " + tickerName + ' ' + indexScope + ' ' + bookScope[indexScope]['SheetName'] + ".xlsx"
pathExcel = os.path.join(rxFilePath, excelSymbol)
print(pathExcel)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
df.index=df.index.astype(str) # Help link # https://sparkbyexamples.com/pandas/pandas-convert-datetime-to-string-format/
df.to_excel(pathExcel, bookScope[indexScope]['SheetName'])

# Save DataFrame to a CSV file
csvSymbol = "OK " + tickerName + ' ' + indexScope + ' ' + bookScope[indexScope]['SheetName'] + ".csv"
pathCSV = os.path.join(rxFilePath, csvSymbol)
df.to_csv(pathCSV, index=True)  # Set index=False to avoid saving row numbers as a column in the CSV




















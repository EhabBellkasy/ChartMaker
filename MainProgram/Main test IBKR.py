import datetime as dt
from datetime import date
import pandas as pd
import os
from datetime import datetime


import sys # Link:- https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
sys.path.append('D:\Python Tools\ChartMaker\GetData')
import GetData
sys.path.append('D:\Python Tools\ChartMaker\GetChart')
import GetChart 
sys.path.append("D:\Python Tools\ChartMaker\IBKR\DataIBKR")
import DataIBKR 
sys.path.append("D:\Python Tools\ChartMaker\WebScraping")
import WebScraping

# set variables:

filePathWL = r"D:\Python Tools\ChartMaker\SourceDocuments\InPut_Excel\Watch_List.xlsx"
filePath_Distnation = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel"        # filePath_Distnation = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\gv "






# datetime object containing current date and time --- Help Link :- https://www.programiz.com/python-programming/datetime/current-datetime#google_vignette
now = datetime.now()
dt_string = now.strftime("[%Y%m%d_%H%M%S]") # YYmmdd_HHMMSS


IBKR=DataIBKR.IBKR()

# import Watch List from excel 
print ("import watch List from excel ")
watchList_xl = pd.read_excel(filePathWL)
tickersWL = watchList_xl.Symbol.to_list()
watchList_xl = watchList_xl.set_index('Symbol')


# Create Session 
sessionSymbol =  "Session" + ' ' + str(dt_string)
pathSession = os.path.join(filePath_Distnation, sessionSymbol)
# print(pathFile)
os.mkdir(pathSession)

for ticker_index in tickersWL :
    print (F' Ticker is : {ticker_index}')

    END_day = watchList_xl.Date[ticker_index]
    # print (F' End Day is : {END_day}')

    END_day_yahoo = END_day + dt.timedelta(days=1)
    # print (F' End Day for yahoo is : {END_day_yahoo}')

    END_day_IBKR = str(END_day)[0:10]
    END_day_IBKR = END_day_IBKR.replace('-','')
    # print (F' End Day for IBKR is : {END_day_IBKR}')
    
    IBKR.qSymbol = ticker_index
    IBKR.qEndDate = END_day_IBKR

    # Make file
    pathFile = os.path.join(pathSession, ticker_index)
    # print(pathFile)
    os.mkdir(pathFile)

    excelSymbol = "OK "
    pathExcel = os.path.join(pathFile, excelSymbol)
    # print(pathExcel+'#')

    GetData.fun(    ticker = ticker_index,
                    END = END_day_yahoo,
                    filePath = pathExcel , 
                    yahoo_Fundamentals = True,
                    yahoo_NEWS = True,
                    yahoo_Days = True,
                    daysNumber = 380,
                    yahoo_Hour = True,
                    daysHours = 30,
                    yahoo_30Min = True,
                    days30Min = 10,
                    yahoo_15Min = True,
                    days15Min = 10,
                    yahoo_5Min = True,
                    days5Min = 10,
                    yahoo_2Min = True,
                    days2Min = 10,
                    yahoo_1Min = True,
                    days1Min = 7
                )
    
    IBKR.fMakePackage   (   nfMakeAdd=False, # True: Make / False: Add
                            nfFilePath = pathExcel,
                            nfSheetList =[  '1M','1W','1 day',
                                        '8 hours','4 hours','3 hours','2 hours','1 hour',
                                        '30 mins','20 mins','15 mins','10 mins','5 mins','3 mins','2 mins','1 min',
                                        '30 secs','15 secs','10 secs','5 secs'#,'1 secs'
                                     ],
                            nfConfigSet ={
                                    '1 secs' :{'SizeIndex': 0, 'DurationIndex':1, 'DurationLenth': 1, 'Rolling':60, 'SheetName':'IBKR 1s'     },
                                    '5 secs' :{'SizeIndex': 1, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':60, 'SheetName':'IBKR 5s'     },
                                    '10 secs':{'SizeIndex': 2, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':30, 'SheetName':'IBKR 10s'    },
                                    '15 secs':{'SizeIndex': 3, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':20, 'SheetName':'IBKR 15s'    },
                                    '30 secs':{'SizeIndex': 4, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'SheetName':'IBKR 30s'    },
                                    '1 min'  :{'SizeIndex': 5, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'SheetName':"IBKR 1m"     },
                                    '2 mins' :{'SizeIndex': 6, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'SheetName':'IBKR 2m'     },
                                    '3 mins' :{'SizeIndex': 7, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'SheetName':'IBKR 3m'     },
                                    '5 mins' :{'SizeIndex': 8, 'DurationIndex':1, 'DurationLenth': 3, 'Rolling': 6, 'SheetName':'IBKR 5m'     },
                                    '10 mins':{'SizeIndex': 9, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling': 6, 'SheetName':'IBKR 10m'    },
                                    '15 mins':{'SizeIndex':10, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling':12, 'SheetName':'IBKR 15m'    },
                                    '20 mins':{'SizeIndex':11, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':12, 'SheetName':'IBKR 20m'    },
                                    '30 mins':{'SizeIndex':12, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':11, 'SheetName':'IBKR 30m'    },
                                    '1 hour' :{'SizeIndex':13, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':16, 'SheetName':'IBKR 1H'     },
                                    '2 hours':{'SizeIndex':14, 'DurationIndex':1, 'DurationLenth':34, 'Rolling': 8, 'SheetName':'IBKR 2H'     },
                                    '3 hours':{'SizeIndex':15, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':30, 'SheetName':'IBKR 3H'     },
                                    '4 hours':{'SizeIndex':16, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':20, 'SheetName':'IBKR 4H'     },
                                    '8 hours':{'SizeIndex':17, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':42, 'SheetName':'IBKR 8H'     },
                                    '1 day'  :{'SizeIndex':18, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':21, 'SheetName':'IBKR 1Day'   },
                                    '1W'     :{'SizeIndex':19, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'SheetName':'IBKR 1week'  },
                                    '1M'     :{'SizeIndex':20, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'SheetName':'IBKR 1Month' }
                                    }
                        )
    
    IBKR.fFundamentalData(  fnFilePath = pathExcel,                         
                            fnFandaList = ['ReportSnapshot','ReportsFinSummary','ReportRatios','ReportsFinStatements','RESC']
                         )

    WebScraping.fun(webScrapingTiker=ticker_index, webScrapingDisPath= pathExcel)

    # GetChart.fun(   tickerName = ticker_index,     
    #                 filePathExcel = pathExcel + ticker_index + '.xlsx',
    #                 filePathChart = pathFile,            #C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
    #                 daySheet = "Yahoo Dayes",
    #                 imageType= '.png'
    #             )
    
    GetChart.fun2   (   # Set Varibles
                            #------------------------------------------------
                            tickerName      = ticker_index,     
                            filePathExcel   = pathExcel + ticker_index + '.xlsx',
                            filePathChart   = pathFile,            #C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
                            flagYahoo       = True,
                            flagIBKR        = True,
                            imageType       = '.png'
                    )

print (f' Watch list is : ')
print (watchList_xl)
print (F' Tickers are : {tickersWL}')
print("------------------------")












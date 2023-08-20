import datetime as dt
from datetime import date
import pandas as pd

import sys # Link:- https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
sys.path.append('D:\Python Tools\ChartMaker\GetData')
import GetData


# set variables:

filePathWL = r"D:\Python Tools\ChartMaker\SourceDocuments\InPut_Excel\Watch_List.xlsx"
filePath_Distnation = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\gv "

# import Watch List from excel 
print ("import watch List from excel ")
watchList_xl = pd.read_excel(filePathWL)
tickersWL = watchList_xl.Symbol.to_list()
watchList_xl = watchList_xl.set_index('Symbol')




for ticker_index in tickersWL :
    END_day = watchList_xl.Date[ticker_index]
    END_day = END_day + dt.timedelta(days=1)
    GetData.fun(    ticker = ticker_index,
                END = END_day,
                filePath = filePath_Distnation,
                yahoo_Fundamentals = True,
                yahoo_NEWS = True,
                yahoo_Days = True,
                daysNumber = 380,
                yahoo_Hour = True,
                daysHours = 10,
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

print (f' Watch list is : ')
print (watchList_xl)
print (F' Tickers are : {tickersWL}')
print("------------------------")

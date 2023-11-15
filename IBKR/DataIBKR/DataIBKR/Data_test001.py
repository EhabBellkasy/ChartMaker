


from ibapi.client import *
from ibapi.wrapper import *
import pandas as pd
import openpyxl
import datetime as dt

def makeDataFrame (bar):
    df = pd.DataFrame(columns=  ['Datetime','Open','High','Low','Close','Volume','wap','barCount'])

    df.Datetime = bar.dDate
    df.Open     = bar.dOpen
    df.High     = bar.dHigh
    df.Low      = bar.dLow 
    df.Close    = bar.dClose
    df.Volume   = bar.dVolume
    df.wap      = bar.dWap
    df.barCount = bar.dBarCount

    df.set_index('Datetime', inplace = True) # Help LLink :- https://www.geeksforgeeks.org/python-pandas-dataframe-set_index/
    df.index=df.index.astype(str) # Help link # https://sparkbyexamples.com/pandas/pandas-convert-datetime-to-string-format/
    return df




class TestApp(EClient, EWrapper):
    
    
    # dego = []
    
    # dDate = []
    # dOpen = []
    # dHigh = []
    # dLow = []
    # dClose = []
    # dVolume = []
    # dWap = []
    # dBarCount = []

    #df=None
    # df = pd.DataFrame(columns=  ['Datetime','Open','High','Low','Close','Volume','wap','barCount'])

    qSymbol = "AAPL"
    qSecType = "STK"
    qExchange = "SMART"
    qCurrency = "USD"

    def __init__(self):
        EClient.__init__(self, self)
        self.df = pd.DataFrame(columns=  ['Datetime','Open','High','Low','Close','Volume','wap','barCount'])
        # self.data = []
        # self.df=None
        
     
    def nextValidId(self, orderId: int):
     
        mycontract = Contract()
        mycontract.symbol = self.qSymbol
        mycontract.secType = self.qSecType
        mycontract.exchange = self.qExchange
        mycontract.currency = self.qCurrency
         
        self.reqHistoricalData(orderId, mycontract, "20230815 15:00:00 US/Eastern", "1 D", "1 hour", "TRADES", 0, 1, 0, [])
 
    def historicalData(self, reqId, bar):

        # self.df = self.df.append({'Datetime': bar.date , 'Open':bar.open,'High':bar.high,'Low':bar.low,'Close':bar.close,'Volume':bar.volume,'wap':bar.wap,'barCount':bar.barCount}, ignore_index=True) # Help Link:- https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.append.html       
        
        # Help link :- https://pandas.pydata.org/docs/reference/api/pandas.concat.html
        new_row = pd.Series({'Datetime': bar.date , 'Open':bar.open,'High':bar.high,'Low':bar.low,'Close':bar.close,'Volume':bar.volume,'wap':bar.wap,'barCount':bar.barCount})
        self.df = pd.concat([self.df, new_row.to_frame().T], ignore_index=True)
        
        
        
        # new_row = pd.DataFrame({'Datetime': bar.date , 'Open':bar.open,'High':bar.high,'Low':bar.low,'Close':bar.close,'Volume':bar.volume,'wap':bar.wap,'barCount':bar.barCount})
        # self.df = pd.concat([self.df, new_row], ignore_index=True)
        

        # print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        # print(self.df)


        # # print(f"Historical Data: {bar}")
        # self.dego.append(bar)
        
        # self.dDate.append(bar.date)
        # self.dOpen.append(bar.open)
        # self.dHigh.append(bar.high)
        # self.dLow.append(bar.low)
        # self.dClose.append(bar.close)
        # self.dVolume.append(bar.volume)
        # self.dWap.append(bar.wap)
        # self.dBarCount.append(bar.barCount)

        
        # print (self.dego)
        # print ("______________________________________")
        # self.data.append(vars(bar))
     
    def historicalDataEnd(self, reqId, start, end):
        print(f"End of HistoricalData")
        print(f"Start: {start}, End: {end}")
        self.disconnect()

    def qClear (self):
        self.dego = []
    
        self.dDate = []
        self.dOpen = []
        self.dHigh = []
        self.dLow = []
        self.dClose = []
        self.dVolume = []
        self.dWap = []
        self.dBarCount = []



# class TestWrapper(wrapper.EWrapper):

#     def historicalData(self, reqId:int, bar: BarData):
#         print("HistoricalData. ReqId:", reqId, "BarData.", bar)


#     def historicalDataEnd(self, reqId: int, start: str, end: str):
#         super().historicalDataEnd(reqId, start, end)
#         print("HistoricalDataEnd. ReqId:", reqId, "from", start, "to", end)

#     def historicalDataUpdate(self, reqId: int, bar: BarData):
#         print("HistoricalDataUpdate. ReqId:", reqId, "BarData.", bar)


#     def historicalSchedule(self, reqId: int, startDateTime: str, endDateTime: str, timeZone: str, sessions: ListOfHistoricalSessions):        
#         super().historicalSchedule(reqId, startDateTime, endDateTime, timeZone, sessions)
#         print("HistoricalSchedule. ReqId:", reqId, "Start:", startDateTime, "End:", endDateTime, "TimeZone:", timeZone)

#         for session in sessions:
#             print("\tSession. Start:", session.startDateTime, "End:", session.endDateTime, "Ref Date:", session.refDate)





# def main():

# Variable
filePath = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\IBKR"
sheetName = 'Yahoo Hours'

loopFlag = False
TikerList = ['NVDA','LCID','GOOGL','INTC','TSLA','CRKN','MMM']

app = TestApp()

app.connect(host="127.0.0.1", port=4002, clientId=1000)
app.run()



# df = pd.DataFrame(columns=  ['Datetime','Open','High','Low','Close','Volume','wap','barCount'])

# df.Datetime = app.dDate
# df.Open     = app.dOpen
# df.High     = app.dHigh
# df.Low      = app.dLow 
# df.Close    = app.dClose
# df.Volume   = app.dVolume
# df.wap      = app.dWap
# df.barCount = app.dBarCount

# df.set_index('Datetime', inplace = True) # Help LLink :- https://www.geeksforgeeks.org/python-pandas-dataframe-set_index/
# df.index=df.index.astype(str) # Help link # https://sparkbyexamples.com/pandas/pandas-convert-datetime-to-string-format/


app.connect(host="127.0.0.1", port=4002, clientId=1000)
app.run()

# df = makeDataFrame (app)

filePathTicker = filePath + app.qSymbol + ".xlsx"
app.df.to_excel(filePathTicker, sheetName)

# print("###################################################")
# print(df)
print("###################################################")
print(app.df)
print("###################################################")


# print("###################################################")
# print("###################################################")

# df7 = pd.DataFrame({'a': 1, 'b': 2}, index=[0])
# new_row = pd.Series({'a': 3, 'b': 4})
# print(pd.concat([df7, new_row.to_frame().T], ignore_index=True))

# print("###################################################")
# print("###################################################")



if (loopFlag):

    for index in TikerList:
        print(index)
        
        app.qClear()
        app.qSymbol = index
        app.connect(host="127.0.0.1", port=4002, clientId=1000)
        app.run()

        df = makeDataFrame (app)

        filePathTicker = filePath + app.qSymbol + ".xlsx"
        df.to_excel(filePathTicker, sheetName)

        print("###################################################")
        print(df)
        print("###################################################")







# print(df.index)
# print("###################################################")





# print("###################################################")
# print(app.dego)
# print("###################################################")
# print(type(app.dego[0]))
# print(app.dego[0].open)
# print("###################################################")
# print(app.dDate)
# print("###################################################")
# df = pd.DataFrame(app.dego)
# print(df)
# print("###################################################")
# hero={'gh':22 , 'gy':48 , 'gt':35 , 'gr':41}
# print(hero['gy'])
# print("###################################################")
# # gero = (sd:0 , sw:8 , sq:4)




# if __name__ == "__main__":
#     main()





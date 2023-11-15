from ibapi.client import *
from ibapi.wrapper import *
import pandas as pd
import openpyxl
import datetime as dt
import ta
import os
import time 

# original file is Ehab3



class IBKR(EClient, EWrapper):
    
    def __init__(self):
        EClient.__init__(self, self)
        self.df = pd.DataFrame(columns=  ['Datetime','Open','High','Low','Close','Volume','wap','barCount'])

        # mycontract
        self.qSymbol = "AAPL"
        self.qSecType = "STK"
        self.qExchange = "SMART"
        self.qCurrency = "USD"

        # endDateTime
        self.qEndDate = "20230901"
        self.qEndTime = "20:00:00"
        self.qTimeZone = "US/Eastern"

        # durationStr
        self.qDurationLenth = 1
        self.qDurationIndex = 1
        self.qDurationType = [' S',' D',' W',' M',' Y']

        # barSizeSetting
        self.qSizeIndex = 10
        self.qBarSize = ['1 secs','5 secs','10 secs','15 secs','30 secs',
                         '1 min','2 mins','3 mins','5 mins','10 mins','15 mins','20 mins','30 mins',
                         '1 hour','2 hours','3 hours','4 hours','8 hours',
                         '1 day','1W','1M']

        # whatToShow
        self.qOutPutIndex=0
        self.qOutPutType=['TRADES','MIDPOINT','BID','ASK','BID_ASK','HISTORICAL_VOLATILITY','OPTION_IMPLIED_VOLATILITY','SCHEDULE']

        # fundamentalData
        self.xData=None

    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson):
            # Error handling function
            print("error: ", reqId, " ", errorCode, " " , '+', errorString)
            if(errorCode == 430):
                self.xData=errorString
                self.disconnect()
            if(errorCode == 200):
                self.xData=errorString
                self.disconnect()

    def nextValidId(self, orderId: int):     
        mycontract = Contract()
        mycontract.symbol = self.qSymbol
        mycontract.secType = self.qSecType
        mycontract.exchange = self.qExchange
        mycontract.currency = self.qCurrency         
        self.reqHistoricalData  (   reqId           =   orderId, 
                                    contract        =   mycontract, 
                                    endDateTime     =   (self.qEndDate + ' ' + self.qEndTime + ' ' + self.qTimeZone),   # "20230825 15:00:00 US/Eastern" 
                                    durationStr     =   (str(self.qDurationLenth) + self.qDurationType[self.qDurationIndex]), # "1 D" 
                                    barSizeSetting  =   self.qBarSize[self.qSizeIndex], # ['1 sec','5 secs','15 secs','30 secs','1 min','2 mins','3 mins','5 mins','15 mins','30 mins','1 hour','1 day']
                                    whatToShow      =   self.qOutPutType[self.qOutPutIndex], #"TRADES" 
                                    useRTH          =   0, 
                                    formatDate      =   1, 
                                    keepUpToDate    =   0, 
                                    chartOptions    =   []
                                )

    def historicalData(self, reqId, bar):
        new_row = pd.Series({'Datetime': bar.date , 'Open':bar.open,'High':bar.high,'Low':bar.low,'Close':bar.close,'Volume':bar.volume,'wap':bar.wap,'barCount':bar.barCount})
        self.df = pd.concat([self.df, new_row.to_frame().T], ignore_index=True)
     
    def historicalDataEnd(self, reqId, start, end):
        print(f"End of HistoricalData")
        print(f"Start: {start}, End: {end}")
        self.disconnect()
    
    def fundamentalData(self, reqId: int, data: str):  # fundamentalData()
        # Inherite and overwrite fundamentalData() function in EWrapper
        # links :- https://stackoverflow.com/questions/62000131/trying-to-request-fundamental-data-from-tws-api
        # links :- https://interactivebrokers.github.io/tws-api/interfaceIBApi_1_1EWrapper-members.html
        self.xData = data
        self.disconnect()

    def fClear (self):
        # Droping the Dataframe -- Help Link :- https://www.includehelp.com/python/drop-all-data-in-a-pandas-dataframe.aspx
        self.df.drop(self.df.index , inplace=True)

    def fAddIndicator(self,df,rollingHL):

        if(self.qSizeIndex >= 0 and self.qSizeIndex <= 17):
            #df['VWAP']                  = vwap_Temp
            df['EMA009']                = ta.trend.ema_indicator(df.Close,   9)
            df['EMA020']                = ta.trend.ema_indicator(df.Close,  20)
            df['EMA040']                = ta.trend.ema_indicator(df.Close,  40)
            df['EMA050']                = ta.trend.ema_indicator(df.Close,  50)
            df['EMA150']                = ta.trend.ema_indicator(df.Close, 150)
            df['EMA200']                = ta.trend.ema_indicator(df.Close, 200)
            #df['200MA_past']           = df['200MA'].shift(20)

        if(self.qSizeIndex >= 18 and self.qSizeIndex <= 20):
            df[ 'SMA50']         = ta.trend.sma_indicator(df.Close,  50)
            df['SMA150']         = ta.trend.sma_indicator(df.Close, 150)
            df['SMA200']         = ta.trend.sma_indicator(df.Close, 200)
            df['SMA_past200']    = df['SMA200'].shift(20)

        
        df['low'+str(rollingHL)]    = df.Low.rolling(rollingHL).min()
        df['high'+str(rollingHL)]   = df.High.rolling(rollingHL).max()

        df.set_index('Datetime', inplace = True) # Help LLink :- https://www.geeksforgeeks.org/python-pandas-dataframe-set_index/
        df.index=df.index.astype(str) # Help link # https://sparkbyexamples.com/pandas/pandas-convert-datetime-to-string-format/

        return df

    def fMakeSheet (    self,
                        # Connect
                        qfHost="127.0.0.1", qfPort=4002, qfClientId=1000, 
                        # Path
                        qfMakeAdd = True, # True: Make / False: Add
                        qfRolling = 60,
                        qfSheetName = "IBKR",
                        qfFilePath = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\IBKR"
                    ):
        self.connect(host=qfHost, port=qfPort, clientId=qfClientId)
        self.run()
        
        df = self.df.copy()  # Help LLink :- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html
        self.fClear()

        df = self.fAddIndicator(df=df,rollingHL=qfRolling)
        # df.set_index('Datetime', inplace = True) # Help LLink :- https://www.geeksforgeeks.org/python-pandas-dataframe-set_index/
        # df.index=df.index.astype(str) # Help link # https://sparkbyexamples.com/pandas/pandas-convert-datetime-to-string-format/

        print("###################################################")
        print(df)
        print("###################################################")
        
        filePathTicker = qfFilePath + self.qSymbol + ".xlsx"
        
        if (qfMakeAdd):
            df.to_excel(filePathTicker, qfSheetName)

        else:
            filePathTemp = qfFilePath + " Temp " + ".xlsx"
            book  = openpyxl.load_workbook(filePathTicker)
            # Start Extend Data to exel
            df.to_excel(filePathTemp, qfSheetName)
            book2 = openpyxl.load_workbook(filePathTemp).active
            #Load existing sheet as it is : -Help Link https://stackoverflow.com/questions/42344041/how-to-copy-worksheet-from-one-workbook-to-another-one-using-openpyxl  
            book2._parent = book
            book._add_sheet(book2)
            book.save(filePathTicker)
            os.remove(filePathTemp)


        
        print("###################################################")
        return filePathTicker
    
    def fMakePackage (  self,
                        nfMakeAdd=True, # True: Make / False: Add
                        nfFilePath = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\IBKR ",

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

                     ):
                        for index in nfSheetList:
                            print(index)

                            if (index == '1M' and nfMakeAdd):
                                nfMakeAddTmp = True
                            else:
                                nfMakeAddTmp = False

                            self.qDurationIndex =    nfConfigSet[index]['DurationIndex']
                            self.qDurationLenth =    nfConfigSet[index]['DurationLenth'] 
                            self.qSizeIndex =        nfConfigSet[index]['SizeIndex']
                            self.fMakeSheet (
                                                # Connect
                                                qfHost="127.0.0.1", qfPort=4002, qfClientId=1000, 
                                                # Path
                                                qfMakeAdd   = nfMakeAddTmp, # True: Make / False: Add
                                                qfRolling   = nfConfigSet[index]['Rolling'],
                                                qfSheetName = nfConfigSet[index]['SheetName'],
                                                qfFilePath  = nfFilePath
                                            )

    def fFundamentalData(self,
                         fnFilePath = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\IBKR ",                         
                         fnFandaList = ['ReportSnapshot','ReportsFinSummary','ReportRatios','ReportsFinStatements','RESC']
                        ):
        mycontract = Contract()
        mycontract.symbol = self.qSymbol
        mycontract.secType = self.qSecType
        mycontract.exchange = self.qExchange
        mycontract.currency = self.qCurrency

        for index in fnFandaList :
            print('')
            print('')
            print('')
            print("*****",index,"*****")
            self.connect("127.0.0.1",port=4002, clientId=1010)
            time.sleep(2)
            self.reqFundamentalData(1, mycontract, index, [])
            time.sleep(4)
            self.run()
            fData = str (self.xData)
                
            file1 = open((fnFilePath + mycontract.symbol + ' ' + index + ".xml"),"w")
            file1.write(fData)
            file1.close()
            self.xData = ''

            # Convert XML to CSV in Python  
            # help link :- https://www.youtube.com/watch?v=o9I4MCE2UHg

            print("###################################################")
            print("############# -- Write is Done -- #################")
            print("###################################################")

    def getTicks(self, orderId: int):
        mycontract = Contract()
        mycontract.symbol = "AAPL"
        mycontract.secType = "STK"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"

        # self.reqHistoricalData(orderId, mycontract, "20230915 20:00:00 US/Eastern", "1 D", "1 hour", "TRADES", 0, 1, 0, [])
        self.reqHistoricalTicks(    #self,
                                    reqId=orderId, 
                                    contract =mycontract, 
                                    startDateTime = "20230915 09:00:00 US/Eastern",
                                    endDateTime = "20230915 9:30:00 US/Eastern", 
                                    numberOfTicks = 1000, 
                                    whatToShow = "TRADES", 
                                    useRth = 0,
                                    ignoreSize = False, 
                                    miscOptions = [] )

    def historicalTicksLast(self, reqId: int, ticks: ListOfHistoricalTickLast, done: bool):
        print("$$$$$$$$$$$$$$$$$$historicalTicksLast$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        # print(ticks)
        for tick in ticks:
            # print("HistoricalTickLast. ReqId:", reqId, tick)
            print(tick)
            # print(tick.time)
            # print(tick.tickAttribLast)
            # print(tick.price)
            # print(tick.size)
            # print(tick.exchange)
            # print(tick.specialConditions)

            # print(tick.)
            # self.time = 0
            # self.tickAttribLast = TickAttribLast()
            # self.price = 0.
            # self.size = UNSET_DECIMAL
            # self.exchange = ""
            # self.specialConditions = ""
            # print(type(tick))

            self.disconnect()
















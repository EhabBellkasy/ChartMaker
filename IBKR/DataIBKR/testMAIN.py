





# from ibapi.client import EClient
# from ibapi.wrapper import EWrapper
# from ibapi.contract import *

# class MyWrapper(EWrapper):

#     def nextValidId(self, orderId:int):
#         print("setting nextValidOrderId: %d", orderId)
#         self.nextValidOrderId = orderId
#         # start program here or use threading
#         app.reqContractDetails(4444, contract)


#     def newsProviders(self, newsProviders: ListOfNewsProviders):
#         print("NewsProviders: ")
#         for provider in newsProviders:
#             print("NewsProvider.", provider)

#     def contractDetails(self, reqId: int, contractDetails: ContractDetails):
#         super().contractDetails(reqId, contractDetails)
#         print(contractDetails)

#     def contractDetailsEnd(self, reqId: int):
#         super().contractDetailsEnd(reqId)
#         print("ContractDetailsEnd. ReqId:", reqId)
#         # this is the logical end of your program
#         app.disconnect() # delete if threading and you want to stay connected

#     def error(self, reqId, errorCode, errorString):
#         print("Error. Id: " , reqId, " Code: " , errorCode , " Msg: " , errorString)


# wrapper = MyWrapper()
# app = EClient(wrapper)
# app.connect("127.0.0.1", 7496, clientId=123)
# print("serverVersion:%s connectionTime:%s" % (app.serverVersion(),    app.twsConnectionTime()))

# from ibapi.contract import Contract

# contract = Contract()
# contract.symbol = "MMM"            #`enter code here`
# contract.secType = "NEWS"       #`enter code here`
# contract.exchange = "BRFG"
# contract.currency = "USD"


# # contract = Contract()
# # contract.symbol  = "BRFG:BRFG_ALL"
# # contract.secType = "NEWS"
# # contract.exchange = "BRFG"

# # app.reqMktData(1, contract, "mdoff,292", False, False, [])


# app.run()



# from ibapi.client import *
# from ibapi.wrapper import *

# class TestApp(EClient, EWrapper):
#     def __init__(self):
#         EClient.__init__(self, self)

#     def nextValidId(self, orderId: int):
        
#         mycontract = Contract()
#         mycontract.symbol = "AAPL"
#         mycontract.secType = "NEWS"
#         mycontract.exchange = "BRFG" #  [BRFG, BRFUPDN, DJNL, BZ, DJTOP]
#         mycontract.currency = "USD"

#         self.reqMarketDataType(4)
#         self.reqMktData(orderId, mycontract, "mdoff,292", 0, 0, [])

#     def tickPrice(self, reqId, tickType, price, attrib):
#         print(f"tickPrice. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, price: {price}, attribs: {attrib}")

#     def tickSize(self, reqId, tickType, size):
#         print(f"tickSize. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, size: {size}")

        

# app = TestApp()
# app.connect("127.0.0.1", 4002, 1000)
# app.run()













# from ibapi.client import *
# from ibapi.wrapper import *

# class TestApp(EClient, EWrapper):
#     def __init__(self):
#         EClient.__init__(self, self)

#     def nextValidId(self, orderId: int):
        
#         mycontract = Contract()
#         mycontract.symbol = "AAPL"
#         mycontract.secType = "STK"
#         mycontract.exchange = "SMART"
#         mycontract.currency = "USD"

#         self.reqHistoricalData(orderId, mycontract, "20221010 15:00 US/Central", "1 D", "1 hour", "TRADES", 0, 1, 0, [])
#         self.reqHistoricalNews(10003, 8314, "BRFG", "", "", 10, [])

#     def historicalData(self, reqId, bar):
#         print(f"Historical Data: {bar}")
    
#     def historicalDataEnd(self, reqId, start, end):
#         print(f"End of HistoricalData")
#         print(f"Start: {start}, End: {end}")





#     def historicalNews(self, requestId:int, time:str, providerCode:str, articleId:str, headline:str):
#         print ("Ehab got News")


#     def historicalNewsEnd(self, requestId:int, hasMore:bool):
#         print ("Ehab got End News")

# app = TestApp()
# app.connect("127.0.0.1", 7497, 1000)
# app.run()








# from finvizfinance.quote import finvizfinance

# stock = finvizfinance('MMM')

# stock.ticker_charts()

# stock_fundament = stock.ticker_fundament(raw=False)
# stock_description = stock.ticker_description()
# outer_ratings_df = stock.ticker_outer_ratings()
# news_df = stock.ticker_news()
# inside_trader_df = stock.ticker_inside_trader()


# # stock_fundament = stock.ticker_fundament(raw=True, output_format="dict")
# # # print(stock_fundament)

# # # stock_description = stock.ticker_description()

# # # print(stock_description)

# # # news_df = stock.ticker_news()

# # # print(news_df)








# import pdfkit

# # Help Link :- https://www.youtube.com/watch?v=ri4flu1Jn4Y
# # Help Link :- https://stackoverflow.com/questions/23359083/how-to-convert-webpage-into-pdf-by-using-python
# # Help Link :- https://wkhtmltopdf.org/downloads.html
# path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
# config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)


# pdfkit.from_url('https://finviz.com/quote.ashx?t=MMM&ty=c&ta=1&p=d', r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\finviz.pdf"  , configuration=config)
# print("#######################################################")



# tikerList = ['NVDA','LCID','META','GOOGL','INTC','TSLA','AAPL','CRKN','MMM']
# for tiker in tikerList:
#     rxpath=r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\finviz " + tiker + ".pdf"
#     print(f'https://finviz.com/quote.ashx?t={tiker}&ty=c&ta=1&p=d')
#     print("#######################################################")
#     pdfkit.from_url(f'https://finviz.com/quote.ashx?t={tiker}&ty=c&ta=1&p=d', rxpath , configuration=config)



# # pdfkit.from_url('http://google.com', 'out.pdf')
# # pdfkit.from_url('http://google.com', 'out.pdf')
# # pdfkit.from_file('www.youtube.com', 'out.pdf')
# # pdfkit.from_url(['google.com', 'yandex.ru', 'engadget.com'], 'out.pdf')










################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################






from ibapi.client import *
from ibapi.wrapper import *

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        
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
        



    def historicalData(self, reqId, bar):
        print(f"Historical Data: {bar}")
    
    def historicalDataEnd(self, reqId, start, end):
        print(f"End of HistoricalData")
        print(f"Start: {start}, End: {end}")

    def historicalTicks(self, reqId, ticks, done):
        print("$$$$$$$$$$$$$$$$$$historicalTicks$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        for tick in ticks:
            print("HistoricalTick. ReqId:", reqId, tick)

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

app = TestApp()

C = Contract()
C.symbol = "AAPL"
C.secType = "STK"
C.exchange = "SMART"
C.currency = "USD"

print("*********1*********")
app.connect("127.0.0.1", 4002, 1000)

# app.reqHistoricalTicks(     reqId=1000, 
#                             contract = C, 
#                             startDateTime = "20230915 04:00:00 US/Eastern",
#                             endDateTime = "20230915 20:00:00 US/Eastern", 
#                             numberOfTicks = 1000, 
#                             whatToShow = "TRADES", 
#                             useRth = 1,
#                             ignoreSize = True, 
#                             miscOptions = [] )

app.run()


























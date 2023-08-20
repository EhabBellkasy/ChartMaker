




# import the libraries

import datetime as dt
import pandas as pd
import yfinance as yf
import ta
import openpyxl
import os


def fun(    ticker = 'goog',
            END = dt.datetime.now(),
            filePath = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\def ",
            daysNumber = 380,
            sheetName = 'Yahoo Dayes'

):

    # Set Varibles
        START = END - dt.timedelta(days=daysNumber)
        filePathTicker = filePath + ticker + ".xlsx"
        filePathTemp = filePath + " Temp " + ".xlsx"
        book  = openpyxl.load_workbook(filePathTicker)

    # download the data
        try:
            #download from yahoo finance:-   
                df = yf.download ( ticker , start=START , end=END)
                # df = yf.Ticker(ticker).history(start=START, end=END, interval='1d', prepost= False)
                print(f'Print data')
            # add the columns
                df[ 'SMA50']         = ta.trend.sma_indicator(df.Close,  50)
                df['SMA150']         = ta.trend.sma_indicator(df.Close, 150)
                df['SMA200']         = ta.trend.sma_indicator(df.Close, 200)
                df['SMA_past200']    = df['SMA200'].shift(20)
                df['low52']         = df.Low.rolling(252).min()
                df['high52']        = df.High.rolling(252).max()

        except Exception:
                print(f' Error on Yahoo Days : No data!')
                df = pd.DataFrame(columns=['Date','Open','High','Low','Close','Adj Close','Volume',
                                        'SMA50','SMA150','SMA200','SMA_past200','low52','high52'
                                        ]) # 'Date','Open','High','Low','Close','Adj Close','Volume','50MA','150MA','200MA','200MA_past','low52','high52'

        df.index=df.index.astype(str) # Help link # https://sparkbyexamples.com/pandas/pandas-convert-datetime-to-string-format/
        df.to_excel( filePathTemp , sheetName)
        book2 = openpyxl.load_workbook(filePathTemp).active

        #Load copy sheet into existing sheet as it is : Help Link: https://stackoverflow.com/questions/42344041/how-to-copy-worksheet-from-one-workbook-to-another-one-using-openpyxl  
        book2._parent = book
        book._add_sheet(book2)
        book.save(filePathTicker)
        os.remove(filePathTemp)







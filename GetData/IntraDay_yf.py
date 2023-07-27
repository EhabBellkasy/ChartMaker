# import the libraries

import datetime as dt
import pandas as pd
import yfinance as yf
import ta
import mplfinance as mpf

import numpy as np
import matplotlib.pyplot as plt
import openpyxl

import os

from datetime import date



def fun(    ticker = 'goog',
            END = dt.datetime.now(),
            filePath = r"C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Split ",
            daysNumber = 10,
            rollingHL = 17,
            interval ='1h', 
            sheetName = 'Yahoo Hours'
):
        
    # Set Varibles
        START = END - dt.timedelta(days=daysNumber)
        filePathTicker = filePath + ticker + ".xlsx"
        filePathTemp = filePath + " Temp " + ".xlsx"
        book  = openpyxl.load_workbook(filePathTicker)

    # Download Hours Data from Yahoo Finance
        try:
            df = yf.Ticker(ticker).history(start=START, end=END, interval=interval, prepost= True)
            # Solve timezone problem by removing it: help Link https://stackoverflow.com/questions/61802080/excelwriter-valueerror-excel-does-not-support-datetime-with-timezone-when-savin
            df.index = df.index.tz_localize(None)
            

            oldDay = df.index[0]
            nextDay = oldDay + dt.timedelta(days=1)
            index1 = 0
            vwap_Temp = []

            for index2 in range (len(df.index)) :
                if (df.index[index2] >= nextDay):
                    df_temp = df[index1 : index2]
                    df_temp[ 'VWAP'] = ta.volume.volume_weighted_average_price(high=df_temp.High, low=df_temp.Low, close=df_temp.Close,  volume=df_temp.Volume,  window=1, fillna =True) 
                    vwap_Temp.append(df_temp.VWAP.to_list())
                    nextDay = df.index[index2] + dt.timedelta(days=1)
                    index1 = index2
                # End of If Statement

            index2 += 1
            df_temp = df[index1 : index2]
            df_temp[ 'VWAP'] = ta.volume.volume_weighted_average_price(high=df_temp.High, low=df_temp.Low, close=df_temp.Close,  volume=df_temp.Volume,  window=1, fillna =True) 
            vwap_Temp.append(df_temp.VWAP.to_list())

            #flatten a 2D list to 1D : Help Link : https://stackoverflow.com/questions/29244286/how-to-flatten-a-2d-list-to-1d-without-using-numpy
            vwap_Temp = [j for sub in vwap_Temp for j in sub]
            df['VWAP']                  = vwap_Temp
            df['EMA009']                = ta.trend.ema_indicator(df.Close,   9)
            df['EMA020']                = ta.trend.ema_indicator(df.Close,  20)
            df['EMA040']                = ta.trend.ema_indicator(df.Close,  40)
            df['EMA050']                = ta.trend.ema_indicator(df.Close,  50)
            df['EMA150']                = ta.trend.ema_indicator(df.Close, 150)
            df['EMA200']                = ta.trend.ema_indicator(df.Close, 200)
            #df['200MA_past']           = df['200MA'].shift(20)
            df['low'+str(rollingHL)]    = df.Low.rolling(rollingHL).min()
            df['high'+str(rollingHL)]   = df.High.rolling(rollingHL).max()

        except Exception:
            print(f' Error on Yahoo Hours : No data!')
            df = pd.DataFrame(columns=['Datetime','Open','High','Low','Close','Volume','Dividends','Stock_Splits',
                                    'VWAP','EMA009','EMA020','EMA040','EMA050','EMA150','EMA200','low17','high17'
                                        ]) # 'Datetime','Open','High','Low','Close','Volume','Dividends','Stock','Splits','EMA009','EMA020','EMA040','EMA050','EMA150','EMA200','low17','high17'
        

    # Start Extend Data to exel
        df.index=df.index.astype(str) # Help link # https://sparkbyexamples.com/pandas/pandas-convert-datetime-to-string-format/
        df.to_excel(filePathTemp, sheetName)
        book2 = openpyxl.load_workbook(filePathTemp).active

    #Load existing sheet as it is : -Help Link https://stackoverflow.com/questions/42344041/how-to-copy-worksheet-from-one-workbook-to-another-one-using-openpyxl  
        book2._parent = book
        book._add_sheet(book2)
        book.save(filePathTicker)
        os.remove(filePathTemp)





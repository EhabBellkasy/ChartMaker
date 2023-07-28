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


import CreatExcel
import Fundamentals_yf
import News_yf
import DaysData_yf
import IntraDay_yf


def fun (   ticker = 'goog',
            END = dt.datetime.now(),
            filePath = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\def ",
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
):
    
    # creat the xcel File
        print(ticker)
        print(END)
        print(filePath)

        CreatExcel.fun(     ticker = ticker,
                            filePath = filePath,
                            sheetName = 'Samary'
                        )
        
    #**************************************************************************************************************************************************
    # Download Fundamentals
        if (yahoo_Fundamentals):
            Fundamentals_yf.fun(    ticker = ticker,
                                    filePath = filePath,
                                    sheetName = 'Yahoo Fundamentals'
                    
                                )

    #**************************************************************************************************************************************************
    # Download NEWS
    
        if (yahoo_NEWS):
            News_yf.fun(    ticker = ticker,
                            filePath = filePath, 
                            sheetName = 'Yahoo News'

                        )

    #**************************************************************************************************************************************************
    # Download days Data
        if (yahoo_Days):
            DaysData_yf.fun(    ticker = ticker,
                                END = END,
                                filePath = filePath,
                                daysNumber = daysNumber,
                                sheetName = 'Yahoo Dayes'
                    
                            )


    
    #**************************************************************************************************************************************************
    # Download Hours Data 
        if (yahoo_Hour):
            IntraDay_yf.fun(    ticker = ticker,
                                END = END,
                                filePath = filePath,
                                daysNumber = daysHours,
                                rollingHL = 17,
                                interval ='1h',
                                sheetName = 'Yahoo Hours'
                             )



    #**************************************************************************************************************************************************
    # Download 30 Min Data 
        if (yahoo_30Min):
            IntraDay_yf.fun(    ticker = ticker,
                                END = END,
                                filePath = filePath,
                                daysNumber = days30Min,
                                rollingHL = 13,
                                interval ='30m', 
                                sheetName = 'Yahoo 30m'
                             )
                    

    #**************************************************************************************************************************************************
    # Download 15 Min Data 
        if (yahoo_15Min):
            IntraDay_yf.fun(    ticker = ticker,
                                END = END,
                                filePath = filePath,
                                daysNumber = days15Min,
                                rollingHL = 4,
                                interval ='15m', 
                                sheetName = 'Yahoo 15m'
                             )
                    

                    

    #**************************************************************************************************************************************************
    # Download 5 Min Data 
        if (yahoo_5Min):
            IntraDay_yf.fun(    ticker = ticker,
                                END = END,
                                filePath = filePath,
                                daysNumber = days5Min,
                                rollingHL = 6,
                                interval ='5m', 
                                sheetName = 'Yahoo 5m'
                             )
                    


                    

    #**************************************************************************************************************************************************
    # Download 2 Min Data 
        if (yahoo_2Min):
            IntraDay_yf.fun(    ticker = ticker,
                                END = END,
                                filePath = filePath,
                                daysNumber = days2Min,
                                rollingHL = 20,
                                interval ='2m', 
                                sheetName = 'Yahoo 2m'
                             )
                    

                    

    #**************************************************************************************************************************************************
    # Download 1 Min Data 
        if (yahoo_1Min):
            IntraDay_yf.fun(    ticker = ticker,
                                END = END,
                                filePath = filePath,
                                daysNumber = days1Min,
                                rollingHL = 5,
                                interval ='1m', 
                                sheetName = 'Yahoo 1m'
                             )
                    











            
            




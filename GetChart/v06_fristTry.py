#!pip install mplfinance

# import the libraries

import yfinance as yf
import mplfinance as mpf
import ta

import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime as dt
import pandas as pd
import numpy as np
import openpyxl

from ChartStyel import EhabStaylo
import ImportData
import FibonacciLines
import YellowCandel
import addIndicator
import TimeStamp as TS


# Set Varibles
#------------------------------------------------     
filePath = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\gv mmm.xlsx'
filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg\Chart test' #    C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
imageType= '.png'
bookScope = ["Yahoo 1m","Yahoo 5m","Yahoo 30m","Yahoo Hours","Yahoo Hours"]
timeScope = ["1m","5m","30m","1h","1d"]
indexScope = 1
startDay= "2023-08-03 "
endDay= "2023-08-03 "


# Loop 1 
# Import  data
dft = ImportData.fun (filePath_fun = filePath , bookName = bookScope[indexScope])



index = 0
index1 =TS.fun(scope=timeScope[indexScope],indexType =1)
index2 =TS.fun(scope=timeScope[indexScope],indexType =2)
index3 =TS.fun(scope=timeScope[indexScope],indexType =3)

# Loop 2
for index in range(len(index1)):
    # Sampling data
    df = dft[(startDay + index1[index]):(endDay + index2[index])]

    #Make Indicator
    EMA = addIndicator.fun(dataFrame = df, scope = timeScope[indexScope] )

    #Make Yellow Color Candel 
    mco = YellowCandel.fun(dataFrame = df) 

    #Make a fibonacci lines
    fabalines = FibonacciLines.fun (filePath_fun = filePath)

    #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
    save = dict(fname= (filePathChart + '_' + timeScope[indexScope] + '_' + index3[index] + imageType), dpi= 500, pad_inches= 0)

    #Make a chart
    mpf.plot(data                   = df,
            title                  = ('\n test Chart'+ ' ' + timeScope[indexScope]), 
            type                   = 'candle', 
            #mav                    = (20,50),
            volume                 = True,
            show_nontrading        = False,
            tight_layout           = False,
            figratio               = (1,1),
            figscale               = 3,
            scale_padding          = 1.0,
            #figsize               = (30,10),
            #ylim                   = (((df.Low.min())*0.95) ,((df.High.max())*1.05)), # set min and max of Chart
            ylim                   = (((df.Low.min())-0.03) ,((df.High.max())+0.03)), # set min and max of Chart
            xrotation              = 0,
            yscale                 = "linear", # y-axis scale: "linear", "log", "symlog", or "logit"
            volume_yscale          = "linear", # Volume y-axis scale: "linear", "log", "symlog", or "logit"
            style                  = EhabStaylo,
            marketcolor_overrides  = mco,
            mco_faceonly           = False,
            addplot                = EMA,
            hlines                 = fabalines,
            savefig                = save # link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
            #marketcolor_overrides = mco  # link https://github.com/matplotlib/mplfinance/blob/master/examples/marketcolor_overrides.ipynb
            )








































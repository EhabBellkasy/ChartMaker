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


# Set Varibles
#------------------------------------------------     
filePath = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\gv mmm.xlsx'
filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg\Chart test.png' #    C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg

# Import  data
df = ImportData.fun (filePath_fun = filePath , bookName = "Yahoo 1m")

#Make Yellow Color Candel 
mco = YellowCandel.fun(dataFrame = df) 

#Make a fibonacci lines
fabalines = FibonacciLines.fun (filePath_fun = filePath)

#Make Indicator
EMA = addIndicator.fun(dataFrame = df, scope = "1m" )

#Saving plot to a file
# Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
#------------------------------------------------
save = dict(fname= filePathChart, dpi= 500, pad_inches= 0)




#Chart theme
#------------------------------------------------
#Make a chart
#------------------------------------------------
mpf.plot(data                   = df,
         title                  = '\n test Chart', 
         type                   = 'candle', 
         mav                    = (20,50),
         volume                 = True,
         show_nontrading        = False,
         tight_layout           = False,
         figratio               = (5,1),
         figscale               = 1,
         scale_padding          = 1.01,
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








































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

# Set Varibles
#------------------------------------------------     
filePath = r'C:\Users\lenovo\Desktop\Python Project\Ehab\Results\HHV2 Watch List MEGL.xlsx'
filePathChart = r'C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg'

# Import  data
#------------------------------------------------  
book = openpyxl.load_workbook(filePath)
sheet = book["Yahoo Hours"]
df= pd.DataFrame(sheet.values)


# format  data
#------------------------------------------------  
#Convert row to column header for Pandas DataFrame : Link https://stackoverflow.com/questions/26147180/convert-row-to-column-header-for-pandas-dataframe
df.columns = df.iloc[0]
df = df.drop(0)

#change object to datetime64[ns]
df.Datetime = pd.to_datetime(df.Datetime.astype('datetime64[ns]'))
df = df.set_index('Datetime')

#change object to float
# Link https://stackoverflow.com/questions/36814100/pandas-to-numeric-for-multiple-columns
cols = df.columns
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')




#Make a fibanatchi line
# Link: https://github.com/matplotlib/mplfinance/blob/master/examples/using_lines.ipynb
#------------------------------------------------
fabalines=dict(    hlines=(2.0, 1.8, 1.55),
                colors=['r','g','b'],
                linestyle='solid',
                linewidths=(3,4,2) 
            )



#Make a chart
#------------------------------------------------

#marketcolors
mc = mpf.make_marketcolors(up='g',
                           down='r',
                           edge='inherit',
                           wick={'up':'orange','down':'orange'},
                           volume='in',
                           ohlc='i'
                           
                           
                           )

#make mpf style
styleEhab  = mpf.make_mpf_style(marketcolors=mc,
                                gridaxis= 'both',
                                gridstyle= 'dashdot',
                                gridcolor= '#ffff00', #'yellow'
                                y_on_right= False

                                
                                )



                                           

mpf.plot(df, 
         type='candle', 
         mav=(20,50),
         volume= True,
         show_nontrading= False,
         tight_layout= False,
         figratio=(18,10),
         figscale=2.5,
         style= styleEhab,
         savefig= filePathChart,
         hlines= fabalines
         )








































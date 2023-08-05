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


# Set Varibles
#------------------------------------------------     
filePath = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\gv SIEB.xlsx'
filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg\Chart test.png' #    C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg

# Import  data
df = ImportData.fun (filePath_fun = filePath)

#Make a fibonacci lines
fabalines = FibonacciLines.fun (filePath_fun = filePath)

#Saving plot to a file
# Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
#------------------------------------------------
save = dict(fname= filePathChart, dpi= 200, pad_inches= 0)


#Chart theme
#------------------------------------------------



#Make Yallow Color Candel 
df['MCOverrides'] = [None]*len(df)
print(df.head(3))
for ts in df.index:
    if    ( (df.loc[ts,'Open']    ==  df.loc[ts,'Close']) and 
            (df.loc[ts,'Volume']  >   0)):
                                            df.loc[ts,'MCOverrides'] = '#FCFC00'
    elif  ( (df.loc[ts,'Open']    == df.loc[ts,'Close']) and 
            (df.loc[ts,'Open']    == df.loc[ts,'High']) and 
            (df.loc[ts,'High']    == df.loc[ts,'Low']) and 
            (df.loc[ts,'Volume']  == 0)):
                                            df.loc[ts,'MCOverrides'] = '#8A8A8A'
print(df.head(3))

print("/*-/*-/*-/*-")
mco = df['MCOverrides'].values
print(len(mco))
print((mco))


# for ei in range (len(mco)):
#         if    (mco[ei] == '#FCFC00'):
#                mco[ei] = mc_Y
#         elif  (mco[ei] == '#8A8A8A'):
#                mco[ei] = mc_G
# mco[0] = mc_Y
# mco[1] = mc_Y
# mco[2] = mc_Y
# mco[3] = mc_Y
# mco[4] = mc_Y
# mco[5] = mc_Y
# mco[6] = mc_Y
# mco[7] = mc_Y
# mco[8] = mc_Y
# mco[9] = mc_Y

print("/*-/*-/*-/*-")
print((mco))
'''




#marketcolors
mc = mpf.make_marketcolors(up='g',
                           down='r',
                           edge='inherit',
                           wick={'up':'w','down':'w'},
                           volume='in',
                           ohlc='i'
                           
                           
                           )

#make mpf style
styleEhab  = mpf.make_mpf_style(marketcolors=mc,
                                gridaxis= 'both',
                                gridstyle= 'dashdot',
                                gridcolor= '#ffff00', #'yellow'
                                figcolor = 'gray',
                                facecolor= 'Black',
                                edgecolor= 'r',
                                
                                y_on_right= False

                                
                                )

'''


# #Make Yallow Color Candel 
# df['MCOverrides'] = [None]*len(df)
# print(df.head(3))
# for ts in df.index:
#     if    ( (df.loc[ts,'Open']    ==  df.loc[ts,'Close']) and 
#             (df.loc[ts,'Volume']  >   0)):
#                                             df.loc[ts,'MCOverrides'] = '#FCFC00' # Yellow
#     elif  ( (df.loc[ts,'Open']    == df.loc[ts,'Close']) and 
#             (df.loc[ts,'Open']    == df.loc[ts,'High']) and 
#             (df.loc[ts,'High']    == df.loc[ts,'Low']) and 
#             (df.loc[ts,'Volume']  == 0)):
#                                             df.loc[ts,'MCOverrides'] = '#8A8A8A' # Grey
# print(df.head(3))
# mco = df['MCOverrides'].values


#Make a chart
#------------------------------------------------
mpf.plot(data=df,
         title= '\n test Chart', 
         type='candle', 
         mav=(20,50),
         volume= True,
         show_nontrading= False,
         tight_layout= False,
         figratio=(5,1),
         figscale=1,
         scale_padding=1.01,
         #figsize=(30,10),
         ylim= (((df.Low.min())*0.95) ,((df.High.max())*1.05)), # set min and max of Chart
         xrotation=0,
         yscale="linear", # y-axis scale: "linear", "log", "symlog", or "logit"
         volume_yscale="linear", # Volume y-axis scale: "linear", "log", "symlog", or "logit"
         style= EhabStaylo,
         marketcolor_overrides=mco,
         mco_faceonly=False,
         savefig= save, # link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
         hlines= fabalines
         #marketcolor_overrides=mco  # link https://github.com/matplotlib/mplfinance/blob/master/examples/marketcolor_overrides.ipynb
         )








































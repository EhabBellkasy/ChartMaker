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
filePath = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\gv SIEB.xlsx'
filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg\Chart test.png' #    C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg

# Import  data
#------------------------------------------------  
book = openpyxl.load_workbook(filePath)
sheet = book["Yahoo 1m"]
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
# NOT FINSH
#------------------------------------------------
fabalines=dict(    hlines=(2.6, 2.4, 2.2),
                colors=['r','g','b'],
                linestyle='solid',
                linewidths=(3,4,2) 
            )

#Saving plot to a file
# Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
#------------------------------------------------
save = dict(fname= filePathChart, dpi= 200, pad_inches= 0)


#Make a chart
#------------------------------------------------

#RC test:
# link : C:\Users\lenovo\anaconda3\Lib\site-packages\mplfinance\_styledata\mike.py
EhabStaylo = dict(style_name    = 'Ehab_Staylo',
             base_mpl_style= 'dark_background', 
             marketcolors  = {'candle'  : {'up':'#14CE1C', 'down':'#CE1414'},
                              'edge'    : {'up':'#14CE1C', 'down':'#CE1414'},
                              'wick'    : {'up':'#ffffff', 'down':'#ffffff'},
                              'ohlc'    : {'up':'#ffffff', 'down':'#ffffff'},
                              'volume'  : {'up':'#14CE1C', 'down':'#CE1414'},
                              'vcdopcod': False, # Volume Color Depends On Price Change On Day
                              'alpha'   : 2.0,
                             },
             mavcolors     = ['#ec009c','#78ff8f','#fcf120'],
             y_on_right    = True,
             gridcolor     = None,
             gridstyle     = None,
             facecolor     = 'Black',
             figcolor      = 'gray',
             rc            = [ ('axes.edgecolor'  , 'white'   ),
                               ('axes.linewidth'  ,  1.5      ),
                               ('axes.labelsize'  , 'large'   ),
                               ('axes.labelweight', 'semibold'),
                               ('axes.grid'       , True      ),
                               ('axes.grid.axis'  , 'both'    ),
                               ('axes.grid.which' , 'major'   ),
                               ('grid.alpha'      ,  0.9      ),
                               ('grid.color'      , '#EBEE24' ),
                               ('grid.linestyle'  , '-.'      ),
                               ('grid.linewidth'  ,  0.8      ),
                               ('figure.facecolor', '#0a0a0a' ),
                               ('patch.linewidth' ,  1.0      ),
                               ('lines.linewidth' ,  1.0      ),
                               ('font.weight'     , 'medium'  ),
                               ('font.size'       ,  8.0     ),
                               ('figure.titlesize', 'x-large' ),
                               ('figure.titleweight','semibold'),
                             ],
             base_mpf_style= 'mike'
            )


'''
style = dict(style_name    = 'mike',
             base_mpl_style= 'dark_background', 
             marketcolors  = {'candle'  : {'up':'#000000', 'down':'#0080ff'},
                              'edge'    : {'up':'#ffffff', 'down':'#0080ff'},
                              'wick'    : {'up':'#ffffff', 'down':'#ffffff'},
                              'ohlc'    : {'up':'#ffffff', 'down':'#ffffff'},
                              'volume'  : {'up':'#7189aa', 'down':'#7189aa'},
                              'vcdopcod': False, # Volume Color Depends On Price Change On Day
                              'alpha'   : 1.0,
                             },
             mavcolors     = ['#ec009c','#78ff8f','#fcf120'],
             y_on_right    = True,
             gridcolor     = None,
             gridstyle     = None,
             facecolor     = None,
             rc            = [ ('axes.edgecolor'  , 'white'   ),
                               ('axes.linewidth'  ,  1.5      ),
                               ('axes.labelsize'  , 'large'   ),
                               ('axes.labelweight', 'semibold'),
                               ('axes.grid'       , True      ),
                               ('axes.grid.axis'  , 'both'    ),
                               ('axes.grid.which' , 'major'   ),
                               ('grid.alpha'      ,  0.9      ),
                               ('grid.color'      , '#b0b0b0' ),
                               ('grid.linestyle'  , '--'      ),
                               ('grid.linewidth'  ,  0.8      ),
                               ('figure.facecolor', '#0a0a0a' ),
                               ('patch.linewidth' ,  1.0      ),
                               ('lines.linewidth' ,  1.0      ),
                               ('font.weight'     , 'medium'  ),
                               ('font.size'       ,  10.0     ),
                               ('figure.titlesize', 'x-large' ),
                               ('figure.titleweight','semibold'),
                             ],
             base_mpf_style= 'mike'
            )


||||||||||||||||||||||||||||||||||||||||||||||||||

rc=                 [   ('axes.edgecolor'  , 'white'   ),
                                                        ('axes.linewidth'  ,  1.5      ),
                                                        ('axes.labelsize'  , 'large'   ),
                                                        ('axes.labelweight', 'semibold'),
                                                        ('axes.grid'       , True      ),
                                                        ('axes.grid.axis'  , 'both'    ),
                                                        ('axes.grid.which' , 'major'   ),
                                                        ('grid.alpha'      ,  0.9      ),
                                                        ('grid.color'      , '#b0b0b0' ),
                                                        ('grid.linestyle'  , '--'      ),
                                                        ('grid.linewidth'  ,  0.8      ),
                                                        ('figure.facecolor', '#0a0a0a' ),
                                                        ('patch.linewidth' ,  1.0      ),
                                                        ('lines.linewidth' ,  1.0      ),
                                                        ('font.weight'     , 'medium'  ),
                                                        ('font.size'       ,  10.0     ),
                                                        ('figure.titlesize', 'x-large' ),
                                                        ('figure.titleweight','semibold'),
                                                    ],

                                                    



'''

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

print(df.High.max()) 
print((df.High.max())*1.05)
print(df.High.min())   
print((df.Low.min())*0.95)                                        

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
         ylim= (((df.Low.min())*0.95) ,((df.High.max())*1.05)), # need to change to set min and max
         xrotation=0,
         yscale="linear", # y-axis scale: "linear", "log", "symlog", or "logit"
         volume_yscale="linear", # Volume y-axis scale: "linear", "log", "symlog", or "logit"
         style= EhabStaylo,
         savefig= save, # link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
         hlines= fabalines
         #marketcolor_overrides=mco  # link https://github.com/matplotlib/mplfinance/blob/master/examples/marketcolor_overrides.ipynb
         )








































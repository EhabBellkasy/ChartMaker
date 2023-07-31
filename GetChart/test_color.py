
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

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

#Set Style:
# link : C:\Users\lenovo\anaconda3\Lib\site-packages\mplfinance\_styledata\mike.py
EhabStaylo = dict(  style_name    = 'Ehab_Staylo',
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
                                      ('grid.linestyle'  , ':'      ),
                                      ('grid.linewidth'  ,  1.0      ),
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




for i in range (15):
    print(i)


ix = pd.DatetimeIndex(['2021-10-11','2021-10-12','2021-10-13','2021-10-14','2021-10-15'])

df = pd.DataFrame(dict(  Open=[131.4, 131.9, 132.0, 130.9, 131.6],
                         High=[133.2, 132.7, 133.2, 132.7, 131.8],
                          Low=[131.3, 131.3, 131.5, 130.6, 130.7],
                        Close=[132.1, 131.4, 131.8, 132.1, 131.0],
                       Volume=[19591, 21467, 20406, 22611, 22001]),
                  index=ix)
df
mpf.plot(df,volume=True,style='yahoo',type='candle')


mco = [None,None,'yellow','blue',None]
mpf.plot(df,volume=True,style='yahoo',type='candle',marketcolor_overrides=mco)

mco = [None,None,'yellow','blue',None]
mpf.plot(df,volume=True,style='yahoo',type='candle',marketcolor_overrides=mco,mco_faceonly=True)

mco = [None,None,'yellow','blue',None]
mpf.plot(df,volume=True,style='yahoo',type='ohlc',marketcolor_overrides=mco)

# ===============================================================================================
# Here we specify `up` as rgba using the matplotlib convention: rgb are floats from 0.0 and 1.0 :
mc = mpf.make_marketcolors(base_mpf_style='yahoo',up=(0.7,1.0,0.7,0.4),down='fuchsia',
                           edge={'up':'blue','down':'#000000'},wick='#cc6600')

mco = [None,None,mc,mc,None]
mpf.plot(df,volume=True,style='yahoo',type='candle',marketcolor_overrides=mco)

# ====================================================================================
# Here we specify `up` as rgba using the convention that rgb are ints from 0 and 255 :
mc = mpf.make_marketcolors(base_mpf_style='yahoo',
                           up='#FCFC00',
                           down='#FCFC00',
                           edge={'up':'blue','down':'#000000'},
                           volume='#FCFC00',
                           wick='#cc6600')

mc_Y = mpf.make_marketcolors(base_mpf_style='blueskies',
                             up='y' , # Yellow '#FCFC00'
                            down='y' , # Yellow '#FCFC00'
                            edge='inherit',
                            wick={'up':'w','down':'w'},
                            volume='in',
                            ohlc='i'
                           
                           
                           )


mco = [None,None,None,mc,None]
mco[2]= mc_Y
mpf.plot(df,
         volume=True,
         style=EhabStaylo,
         type='candle',
         marketcolor_overrides=mco)
















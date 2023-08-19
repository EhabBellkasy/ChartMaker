

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import mplfinance as mpf
import pandas as pd




def fun (dataFrame, scope = "1m" ) :

        EMA=[           #mpf.make_addplot(dataFrame.VWAP  , title="VWAP",   type='line', linestyle='dotted',   alpha = 0.5, width=3.5, color='#FC00FF')   ,   #purple color
                        mpf.make_addplot(dataFrame.EMA009, title="EMA009", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#FFFFFF')   ,   #white  color
                        mpf.make_addplot(dataFrame.EMA020, title="EMA020", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#7BFFF4')   ,   #Aqua   color
                        mpf.make_addplot(dataFrame.EMA040, title="EMA040", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#E6FF3F')   ,   #Yellow color
                        mpf.make_addplot(dataFrame.EMA050, title="EMA050", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2D4DFF')   ,   #Blue   color
                        mpf.make_addplot(dataFrame.EMA150, title="EMA150", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#FF2D2D')   ,   #Red    color
                        mpf.make_addplot(dataFrame.EMA200, title="EMA200", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2FC822')      #Green  color
                        
                        ]


        if (scope == "Days") :
                EMA=[   mpf.make_addplot(dataFrame.SMA50 ,       type='line', color='#FFFFFF', width=0.5)   ,   #white  color
                        mpf.make_addplot(dataFrame.SMA150,       type='line', color='#7BFFF4', width=0.5)   ,   #Aqua   color
                        mpf.make_addplot(dataFrame.SMA200,       type='line', color='#E6FF3F', width=0.5)   ,   #Yellow color
                        mpf.make_addplot(dataFrame.SMA_past200,  type='line', color='#2D4DFF', width=0.5)   ,   #Blue   color
                        mpf.make_addplot(dataFrame.low52,        type='dash', color='#FEB2FF', width=0.5)   ,   #Pink   color
                        mpf.make_addplot(dataFrame.high52,       type='dash', color='#FEB2FF', width=0.5)       #Pink   color

                    ]
                
        elif (scope == "Hours"):
                EMA.append(mpf.make_addplot(dataFrame.low17 ,   title="low17",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                EMA.append(mpf.make_addplot(dataFrame.high17,   title="high17",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                

        elif (scope == "30m"):
                EMA.append(mpf.make_addplot(dataFrame.low13 ,   title="low13",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                EMA.append(mpf.make_addplot(dataFrame.high13,   title="high13",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                

        elif (scope == "15m"):
                EMA.append(mpf.make_addplot(dataFrame.low4 ,    title="low4",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                EMA.append(mpf.make_addplot(dataFrame.high4,    title="high4",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                

        elif (scope == "5m"):
                EMA.append(mpf.make_addplot(dataFrame.low6 ,    title="low6",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                EMA.append(mpf.make_addplot(dataFrame.high6,    title="high6",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                

        elif (scope == "2m"):
                EMA.append(mpf.make_addplot(dataFrame.low20 ,   title="low20",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                EMA.append(mpf.make_addplot(dataFrame.high20,   title="high20",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                

        elif (scope == "1m"):
                EMA.append(mpf.make_addplot(dataFrame.low5 ,    title="low5",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                EMA.append(mpf.make_addplot(dataFrame.high5,    title="high5",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                

        elif (scope == "30s"):
                EMA.append(mpf.make_addplot(dataFrame.low13 ,   title="low13",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                EMA.append(mpf.make_addplot(dataFrame.high13,   title="high13",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                

        elif (scope == "15s"):
                EMA.append(mpf.make_addplot(dataFrame.low13 ,   title="low13",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                EMA.append(mpf.make_addplot(dataFrame.high13,   title="high13",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                

        elif (scope == "10s"):
                EMA.append(mpf.make_addplot(dataFrame.low13 ,   title="low13",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                EMA.append(mpf.make_addplot(dataFrame.high13,   title="high13",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                

        elif (scope == "5s"):
                EMA.append(mpf.make_addplot(dataFrame.low13 ,   title="low13",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                EMA.append(mpf.make_addplot(dataFrame.high13,   title="high13",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                

        

        return EMA

'''
        linestyle= 'dashdot'
        '-'     or 'solid',
        '--'    or 'dashed',
        '-.'    or 'dashdot',
        ':'     or 'dotted',
        None    or ' '          or '' (draw nothing)


'''




test = {} 
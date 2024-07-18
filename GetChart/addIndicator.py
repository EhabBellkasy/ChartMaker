

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import mplfinance as mpf
import pandas as pd




'''
        linestyle= 'dashdot'
        '-'     or 'solid',
        '--'    or 'dashed',
        '-.'    or 'dashdot',
        ':'     or 'dotted',
        None    or ' '          or '' (draw nothing)


'''

#__________________________________________________________________________________________________________
def fun (dataFrame, scope = "1m" ) :

        


        if (scope == "1d") :
                EMA=[   mpf.make_addplot(dataFrame.SMA50 ,       title="SMA50",         type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#FFFFFF')   ,   #white  color
                        mpf.make_addplot(dataFrame.SMA150,       title="SMA150",        type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#7BFFF4')   ,   #Aqua   color
                        mpf.make_addplot(dataFrame.SMA200,       title="SMA200",        type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#E6FF3F')   ,   #Yellow color
                        mpf.make_addplot(dataFrame.SMA_past200,  title="SMA_past200",   type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2D4DFF')   ,   #Blue   color
                        mpf.make_addplot(dataFrame.low52,        title="low52",         type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')   ,   #Pink   color
                        mpf.make_addplot(dataFrame.high52,       title="high52",        type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')       #Pink   color

                    ]

        if (scope in ["1h","30m","15m","5m","2m","1m","30s","15s","10s","5s"]):
                EMA=[   #mpf.make_addplot(dataFrame.VWAP  , title="VWAP",   type='line', linestyle='dotted',   alpha = 0.5, width=3.5, color='#FC00FF')   ,   #purple color
                        mpf.make_addplot(dataFrame.EMA009, title="EMA009", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#FFFFFF')   ,   #white  color
                        mpf.make_addplot(dataFrame.EMA020, title="EMA020", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#7BFFF4')   ,   #Aqua   color
                        mpf.make_addplot(dataFrame.EMA040, title="EMA040", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#E6FF3F')   ,   #Yellow color
                        mpf.make_addplot(dataFrame.EMA050, title="EMA050", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2D4DFF')   ,   #Blue   color
                        mpf.make_addplot(dataFrame.EMA150, title="EMA150", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#FF2D2D')   ,   #Red    color
                        mpf.make_addplot(dataFrame.EMA200, title="EMA200", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2FC822')      #Green  color
                        
                        ]


        if (scope == "1h"):
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
#__________________________________________________________________________________________________________
def fun2 (dataFrame, scope = "1m" ) :
        if (scope in ['1 day','1W','1M']) :
                EMA=[   mpf.make_addplot(dataFrame.SMA50 ,       title="SMA50",         type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#FFFFFF')   ,   #white  color
                        mpf.make_addplot(dataFrame.SMA150,       title="SMA150",        type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#7BFFF4')   ,   #Aqua   color
                        mpf.make_addplot(dataFrame.SMA200,       title="SMA200",        type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#E6FF3F')   ,   #Yellow color
                        mpf.make_addplot(dataFrame.SMA_past200,  title="SMA_past200",   type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2D4DFF')   ,   #Blue   color                        
                    ]
                if      (scope == '1 day'):
                                EMA.append(mpf.make_addplot(dataFrame.low21 ,   title="low21",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high21,   title="high21",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color                
                elif    (scope == '1W'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,   title="low12",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,   title="high12",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color                
                elif    (scope == '1M'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,   title="low12",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,   title="high12",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                

        if (scope in ['1 secs','5 secs','10 secs','15 secs','30 secs',
                      '1 min','2 mins','3 mins','5 mins','10 mins',
                      '15 mins','20 mins','30 mins',
                      '1 hour','2 hours','3 hours','4 hours','8 hours'
                      ]):
                EMA=[   mpf.make_addplot(dataFrame.VWAP  , title="VWAP",   type='line', linestyle='solid',   alpha = 0.5, width=3.5, color='#FC00FF')   ,   #purple color
                        mpf.make_addplot(dataFrame.EMA009, title="EMA009", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#FFFFFF')   ,   #white  color
                        mpf.make_addplot(dataFrame.EMA020, title="EMA020", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#7BFFF4')   ,   #Aqua   color
                        mpf.make_addplot(dataFrame.EMA040, title="EMA040", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#E6FF3F')   ,   #Yellow color
                        mpf.make_addplot(dataFrame.EMA050, title="EMA050", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2D4DFF')   ,   #Blue   color
                        mpf.make_addplot(dataFrame.EMA150, title="EMA150", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#FF2D2D')   ,   #Red    color
                        mpf.make_addplot(dataFrame.EMA200, title="EMA200", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2FC822')      #Green  color                        
                        ]
                if      (scope == '1 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low60 ,   title="low60",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high60,   title="high60",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '5 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low60 ,   title="low60",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high60,   title="high60",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '10 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low30 ,   title="low30",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high30,   title="high30",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '15 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low20 ,   title="low20",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high20,   title="high20",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '30 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low10 ,   title="low10",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high10,   title="high10",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '1 min'):
                                EMA.append(mpf.make_addplot(dataFrame.low5 ,   title="low5",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high5,   title="high5",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '2 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low5 ,   title="low5",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high5,   title="high5",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '3 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low10 ,   title="low10",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high10,   title="high10",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '5 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low6 ,   title="low6",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high6,   title="high6",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '10 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low6 ,   title="low6",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high6,   title="high6",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '15 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,   title="low12",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,   title="high12",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '20 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,   title="low12",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,   title="high12",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '30 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low11 ,   title="low11",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high11,   title="high11",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '1 hour'):
                                EMA.append(mpf.make_addplot(dataFrame.low16 ,   title="low16",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high16,   title="high16",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '2 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low8 ,   title="low8",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high8,   title="high8",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '3 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low30 ,   title="low30",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high30,   title="high30",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '4 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low20 ,   title="low20",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high20,   title="high20",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '8 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low42 ,   title="low42",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high42,   title="high42",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color

                
        return EMA
#__________________________________________________________________________________________________________
def fun3 (dataFrame, scope = "1m" ) :
        if (scope in ['1 day','1W','1M']) :
                EMA=[   mpf.make_addplot(dataFrame.SMA50 ,       title="SMA50",         type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#FFFFFF')   ,   #white  color
                        mpf.make_addplot(dataFrame.SMA150,       title="SMA150",        type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#7BFFF4')   ,   #Aqua   color
                        mpf.make_addplot(dataFrame.SMA200,       title="SMA200",        type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#E6FF3F')   ,   #Yellow color
                        mpf.make_addplot(dataFrame.SMA_past200,  title="SMA_past200",   type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2D4DFF')   ,   #Blue   color                        
                    ]
                if      (scope == '1 day'):
                                EMA.append(mpf.make_addplot(dataFrame.low21 ,   title="low21",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high21,   title="high21",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color                
                elif    (scope == '1W'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,   title="low12",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,   title="high12",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color                
                elif    (scope == '1M'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,   title="low12",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,   title="high12",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                

        if (scope in ['1 secs','5 secs','10 secs','15 secs','30 secs',
                      '1 min','2 mins','3 mins','5 mins','10 mins',
                      '15 mins','20 mins','30 mins',
                      '1 hour','2 hours','3 hours','4 hours','8 hours'
                      ]):
                EMA=[    mpf.make_addplot(dataFrame.VWAP  , title="VWAP",   type='line', linestyle='solid',   alpha = 0.7, width=3.5, color='#FC00FF')      #purple color
                        ,mpf.make_addplot(dataFrame.EMA009, title="EMA009", type='line', linestyle='solid',   alpha = 0.7, width=0.5, color='#FFFFFF')        #white  color
                        ,mpf.make_addplot(dataFrame.EMA020, title="EMA020", type='line', linestyle='solid',   alpha = 0.7, width=0.5, color='#7BFFF4')        #Aqua   color
                        ,mpf.make_addplot(dataFrame.EMA040, title="EMA040", type='line', linestyle='solid',   alpha = 0.7, width=0.5, color='#E6FF3F')        #Yellow color
                        # ,mpf.make_addplot(dataFrame.EMA050, title="EMA050", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2D4DFF')      #Blue   color
                        # ,mpf.make_addplot(dataFrame.EMA150, title="EMA150", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#FF2D2D')      #Red    color
                        # ,mpf.make_addplot(dataFrame.EMA200, title="EMA200", type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2FC822')      #Green  color                        
                        ]
                if      (scope == '1 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low60 ,   title="low60",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high60,   title="high60",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '5 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low60 ,   title="low60",   type='line', linestyle='solid',   alpha=0.7, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high60,   title="high60",  type='line', linestyle='solid',   alpha=0.7, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.EMA108,   title="EMA108",  type='line', linestyle='solid',   alpha=0.7, width=0.5, color='#2D4DFF')) #Blue   color
                                EMA.append(mpf.make_addplot(dataFrame.EMA540,   title="EMA540",  type='line', linestyle='solid',   alpha=0.7, width=0.5, color='#FF2D2D')) #Red    color
                elif    (scope == '10 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low30 ,   title="low30",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high30,   title="high30",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '15 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low20 ,   title="low20",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high20,   title="high20",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '30 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low10 ,   title="low10",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high10,   title="high10",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '1 min'):
                                EMA.append(mpf.make_addplot(dataFrame.low5 ,   title="low5",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high5,   title="high5",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '2 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low5 ,   title="low5",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high5,   title="high5",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '3 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low10 ,   title="low10",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high10,   title="high10",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '5 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low6 ,   title="low6",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high6,   title="high6",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '10 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low6 ,   title="low6",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high6,   title="high6",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '15 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,   title="low12",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,   title="high12",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '20 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,   title="low12",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,   title="high12",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '30 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low11 ,   title="low11",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high11,   title="high11",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '1 hour'):
                                EMA.append(mpf.make_addplot(dataFrame.low16 ,   title="low16",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high16,   title="high16",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '2 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low8 ,   title="low8",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high8,   title="high8",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '3 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low30 ,   title="low30",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high30,   title="high30",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '4 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low20 ,   title="low20",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high20,   title="high20",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '8 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low42 ,   title="low42",   type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high42,   title="high42",  type='line', linestyle='dashdot', alpha=0.5, width=0.5, color='#FEB2FF')) #Pink   color

                
        return EMA
#__________________________________________________________________________________________________________
def fun4 (dataFrame, scope = "1m" ) :
        if (scope in ['1 day','1W','1M']) :
                EMA=[   mpf.make_addplot(dataFrame.SMA50 ,          type='line', linestyle='solid',   alpha=0.8, width=0.8, color='#FFFFFF')   ,   #white  color
                        mpf.make_addplot(dataFrame.SMA150,          type='line', linestyle='solid',   alpha=0.8, width=0.8, color='#7BFFF4')   ,   #Aqua   color
                        mpf.make_addplot(dataFrame.SMA200,          type='line', linestyle='solid',   alpha=0.8, width=0.8, color='#E6FF3F')   ,   #Yellow color
                        mpf.make_addplot(dataFrame.SMA_past200,     type='line', linestyle='solid',   alpha=0.8, width=0.8, color='#2D4DFF')   ,   #Blue   color                        
                    ]
                if      (scope == '1 day'):
                                EMA.append(mpf.make_addplot(dataFrame.low21 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high21,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color                
                elif    (scope == '1W'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color                
                elif    (scope == '1M'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                

        if (scope in ['1 secs','5 secs','10 secs','15 secs','30 secs',
                      '1 min','2 mins','3 mins','5 mins','10 mins',
                      '15 mins','20 mins','30 mins',
                      '1 hour','2 hours','3 hours','4 hours','8 hours'
                      ]):
                EMA=[    mpf.make_addplot(dataFrame.VWAP  ,  type='line', linestyle='solid',   alpha = 0.7, width=2.5, color='#FC00FF')      #purple color
                        ,mpf.make_addplot(dataFrame.EMA009,  type='line', linestyle='solid',   alpha = 0.9, width=0.8, color='#FFFFFF')        #white  color
                        ,mpf.make_addplot(dataFrame.EMA020,  type='line', linestyle='solid',   alpha = 0.9, width=0.8, color='#7BFFF4')        #Aqua   color
                        ,mpf.make_addplot(dataFrame.EMA040,  type='line', linestyle='solid',   alpha = 0.9, width=0.8, color='#E6FF3F')        #Yellow color
                        # ,mpf.make_addplot(dataFrame.EMA050,  type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2D4DFF')      #Blue   color
                        # ,mpf.make_addplot(dataFrame.EMA150,  type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#FF2D2D')      #Red    color
                        # ,mpf.make_addplot(dataFrame.EMA200,  type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2FC822')      #Green  color                        
                        ]
                if      (scope == '1 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low60 ,     type='line', linestyle='dashdot', alpha=0.5, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high60,     type='line', linestyle='dashdot', alpha=0.5, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '5 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low60 ,     type='line', linestyle='solid',   alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high60,     type='line', linestyle='solid',   alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.EMA108,     type='line', linestyle='solid',   alpha=0.7, width=2.5, color='#2D4DFF')) #Blue   color
                                EMA.append(mpf.make_addplot(dataFrame.EMA540,     type='line', linestyle='solid',   alpha=0.7, width=2.5, color='#FF2D2D')) #Red    color
                elif    (scope == '10 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low30 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high30,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '15 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low20 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high20,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '30 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low10 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high10,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '1 min'):
                                EMA.append(mpf.make_addplot(dataFrame.low5 ,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high5,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '2 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low5 ,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high5,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '3 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low10 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high10,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '5 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low6 ,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high6,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '10 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low6 ,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high6,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '15 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '20 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '30 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low11 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high11,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '1 hour'):
                                EMA.append(mpf.make_addplot(dataFrame.low16 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high16,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '2 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low8 ,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high8,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '3 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low30 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high30,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '4 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low20 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high20,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '8 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low42 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high42,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color

                
        return EMA
#__________________________________________________________________________________________________________
def fun5 (dataFrame ,scope = "1m" ,style="Ehab" ) :
        if(style in ["Ehab","Ehab1","Sheet2"]):
                EMA = EHAB1 (dataFrame, scope  )
        elif(style in ["Zamzam"]):
                EMA = Zamzam1 (dataFrame, scope )
        return EMA
#__________________________________________________________________________________________________________










#******************************************************************************************************************************************************************************
#******************************************************************************************************************************************************************************
#******************************************************************************************************************************************************************************
#******************************************************************************************************************************************************************************
#******************************************************************************************************************************************************************************

#__________________________________________________________________________________________________________
def EHAB1 (dataFrame, scope = "1m" ) :
        if (scope in ['1 day','1W','1M']) :
                EMA=[   mpf.make_addplot(dataFrame.SMA50 ,          type='line', linestyle='solid',   alpha=0.8, width=0.8, color='#FFFFFF')   ,   #white  color
                        mpf.make_addplot(dataFrame.SMA150,          type='line', linestyle='solid',   alpha=0.8, width=0.8, color='#7BFFF4')   ,   #Aqua   color
                        mpf.make_addplot(dataFrame.SMA200,          type='line', linestyle='solid',   alpha=0.8, width=0.8, color='#E6FF3F')   ,   #Yellow color
                        mpf.make_addplot(dataFrame.SMA_past200,     type='line', linestyle='solid',   alpha=0.8, width=0.8, color='#2D4DFF')   ,   #Blue   color                        
                    ]
                if      (scope == '1 day'):
                                EMA.append(mpf.make_addplot(dataFrame.low21 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high21,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color                
                elif    (scope == '1W'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color                
                elif    (scope == '1M'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                

        if (scope in ['1 secs','5 secs','10 secs','15 secs','30 secs',
                      '1 min','2 mins','3 mins','5 mins','10 mins',
                      '15 mins','20 mins','30 mins',
                      '1 hour','2 hours','3 hours','4 hours','8 hours'
                      ]):
                EMA=[    mpf.make_addplot(dataFrame.VWAP  ,  type='line', linestyle='solid',   alpha = 0.7, width=2.5, color='#FC00FF')      #purple color
                        ,mpf.make_addplot(dataFrame.EMA009,  type='line', linestyle='solid',   alpha = 0.9, width=0.8, color='#FFFFFF')        #white  color
                        ,mpf.make_addplot(dataFrame.EMA020,  type='line', linestyle='solid',   alpha = 0.9, width=0.8, color='#7BFFF4')        #Aqua   color
                        ,mpf.make_addplot(dataFrame.EMA040,  type='line', linestyle='solid',   alpha = 0.9, width=0.8, color='#E6FF3F')        #Yellow color
                        # ,mpf.make_addplot(dataFrame.EMA050,  type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2D4DFF')      #Blue   color
                        # ,mpf.make_addplot(dataFrame.EMA150,  type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#FF2D2D')      #Red    color
                        # ,mpf.make_addplot(dataFrame.EMA200,  type='line', linestyle='solid',   alpha=0.5, width=0.5, color='#2FC822')      #Green  color                        
                        ]
                if      (scope == '1 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low60 ,     type='line', linestyle='dashdot', alpha=0.5, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high60,     type='line', linestyle='dashdot', alpha=0.5, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '5 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low60 ,     type='line', linestyle='solid',   alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high60,     type='line', linestyle='solid',   alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.EMA108,     type='line', linestyle='solid',   alpha=0.7, width=2.5, color='#2D4DFF')) #Blue   color
                                EMA.append(mpf.make_addplot(dataFrame.EMA540,     type='line', linestyle='solid',   alpha=0.7, width=2.5, color='#FF2D2D')) #Red    color
                elif    (scope == '10 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low30 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high30,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '15 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low20 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high20,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '30 secs'):
                                EMA.append(mpf.make_addplot(dataFrame.low10 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high10,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '1 min'):
                                EMA.append(mpf.make_addplot(dataFrame.low5 ,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high5,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '2 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low5 ,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high5,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '3 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low10 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high10,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '5 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low6 ,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high6,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '10 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low6 ,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high6,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '15 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '20 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low12 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high12,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '30 mins'):
                                EMA.append(mpf.make_addplot(dataFrame.low11 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high11,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '1 hour'):
                                EMA.append(mpf.make_addplot(dataFrame.low16 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high16,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '2 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low8 ,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high8,      type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '3 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low30 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high30,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '4 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low20 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high20,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                elif    (scope == '8 hours'):
                                EMA.append(mpf.make_addplot(dataFrame.low42 ,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color
                                EMA.append(mpf.make_addplot(dataFrame.high42,     type='line', linestyle='dashdot', alpha=0.7, width=1.5, color='#FEB2FF')) #Pink   color

                
        return EMA
#__________________________________________________________________________________________________________













#******************************************************************************************************************************************************************************
#******************************************************************************************************************************************************************************
#******************************************************************************************************************************************************************************
#******************************************************************************************************************************************************************************
#******************************************************************************************************************************************************************************


#__________________________________________________________________________________________________________
def Zamzam1 (dataFrame, scope = "1m" ) :
        if (scope in ['1 day','1W','1M']) :
                EMA=[   mpf.make_addplot(dataFrame.EMA200,          type='line', linestyle='solid',   alpha=0.8, width=0.8, color='#E6FF3F')   ,   #Yellow color
                        mpf.make_addplot(dataFrame.EMA500,          type='line', linestyle='solid',   alpha=0.8, width=0.8, color='#2D4DFF')   ,   #Blue   color                        
                    ]
                
                

        if (scope in ['1 secs','5 secs','10 secs','15 secs','30 secs',
                      '1 min','2 mins','3 mins','5 mins','10 mins',
                      '15 mins','20 mins','30 mins',
                      '1 hour','2 hours','3 hours','4 hours','8 hours'
                      ]):
                EMA=[    mpf.make_addplot(dataFrame.VWAP  ,  type='line', linestyle='solid',   alpha = 0.7, width=2.5, color='#FC00FF')      #purple color
                        ,mpf.make_addplot(dataFrame.EMA009,  type='line', linestyle='solid',   alpha = 0.9, width=0.8, color='#FFFFFF')        #white  color                       
                        ]
                
                
        return EMA
#__________________________________________________________________________________________________________


#!pip install mplfinance

# import the libraries


import mplfinance as mpf



from ChartStyel import EhabStaylo
import ImportData
import FibonacciLines
import YellowCandel
import addIndicator
import TimeStamp as TS
import CreateFile
from datetime import datetime


###_____________________________________________________________________________________________________________________________________________________________________________________
def fun(    # Set Varibles
            #------------------------------------------------
                tickerName = 'mmm',     
                filePathExcel = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\gv mmm.xlsx',
                filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg',            #C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
                daySheet = "Yahoo Dayes",
                imageType= '.png'
        


        ):

            # start the Function:-
            rxChartPath = CreateFile.fun(directory = tickerName, parent_dir = filePathChart)


            # Loop 1:-
            indexScope = 0
            bookScope = ["Yahoo 1m","Yahoo 5m","Yahoo 30m","Yahoo Hours","Yahoo Dayes"]
            timeScope = ["1m","5m","30m","1h","1d"] 

            for indexScope in range(len(bookScope)):
                # Import  data
                dft = ImportData.fun (filePath_fun = filePathExcel , bookName = bookScope[indexScope])
                indexTS =TS.fun2(filePath=filePathExcel, bookScope=daySheet, scope=timeScope[indexScope])

                # Loop 2:-
                index = 0
                for index in range(len(indexTS.index1)):
                    # Sampling data
                    df = dft[(indexTS.index1[index]):(indexTS.index2[index])]

                    #Make Indicator
                    EMA = addIndicator.fun(dataFrame = df, scope = timeScope[indexScope] )

                    #Make Yellow Color Candel 
                    mco = YellowCandel.fun(dataFrame = df) 

                    #Make a fibonacci lines
                    fabalines = FibonacciLines.fun (filePath_fun = filePathExcel)

                    #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                    setName = '\\' + tickerName + '_' + timeScope[indexScope] + '_' + indexTS.index4[index] + '_to_' + indexTS.index5[index]
                    save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                    #Make a chart
                    mpf.plot(data                   = df,
                            title                  = (tickerName + ' ' + timeScope[indexScope]), 
                            type                   = 'candle', 
                            #mav                    = (20,50),
                            volume                 = True,
                            show_nontrading        = False,
                            tight_layout           = True,
                            figratio               = (1,1),
                            figscale               = 3,
                            scale_padding          = 0.30,
                            figsize               = (12,6),
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
###_____________________________________________________________________________________________________________________________________________________________________________________
def fun2(   # Set Varibles
            #------------------------------------------------
                tickerName = 'AAPL',     
                filePathExcel = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\Session [20230921_221745]\AAPL\OK AAPL.xlsx",
                filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg',            #C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
                flagYahoo = True,
                flagIBKR = True,
                imageType= '.png'
        ):
            
            if (flagYahoo):
                # start the Function:-
                rxChartPath = CreateFile.fun(directory = "Yahoo", parent_dir = filePathChart)

                # Loop 1:-
                daySheet = "Yahoo Dayes"
                indexScope = 0
                bookScope = ["Yahoo 1m","Yahoo 5m","Yahoo 30m","Yahoo Hours","Yahoo Dayes"]
                timeScope = ["1m","5m","30m","1h","1d"] 

                for indexScope in range(len(bookScope)):
                    # Import  data
                    dft = ImportData.fun (filePath_fun = filePathExcel , bookName = bookScope[indexScope])
                    indexTS =TS.fun2(filePath=filePathExcel, bookScope=daySheet, scope=timeScope[indexScope])

                    # Loop 2:-
                    index = 0
                    for index in range(len(indexTS.index1)):
                        # Sampling data
                        df = dft[(indexTS.index1[index]):(indexTS.index2[index])]

                        #Make Indicator
                        EMA = addIndicator.fun(dataFrame = df, scope = timeScope[indexScope] )

                        #Make Yellow Color Candel 
                        mco = YellowCandel.fun(dataFrame = df) 

                        #Make a fibonacci lines
                        fabalines = FibonacciLines.fun (filePath_fun = filePathExcel)

                        #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                        setName = '\\' + tickerName + '_' + timeScope[indexScope] + '_' + indexTS.index4[index] + '_to_' + indexTS.index5[index]
                        save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                        #Make a chart
                        mpf.plot(data                   = df,
                                title                  = (tickerName + ' ' + timeScope[indexScope]), 
                                type                   = 'candle', 
                                #mav                    = (20,50),
                                volume                 = True,
                                show_nontrading        = False,
                                tight_layout           = True,
                                figratio               = (1,1),
                                figscale               = 3,
                                scale_padding          = 0.30,
                                figsize               = (12,6),
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

            if (flagIBKR == "test2"):
                # start the Function:-
                rxChartPath = CreateFile.fun(directory = "IBKR", parent_dir = filePathChart)

                # Loop 1:-
                daySheet = "IBKR 1Day"
                # indexScope = 0                
                timeScope = ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']
                # bookScope = ["Yahoo 1m","Yahoo 5m","Yahoo 30m","Yahoo Hours","Yahoo Dayes"]
                bookScope = {
                            '1 secs' :{'SizeIndex': 0, 'DurationIndex':1, 'DurationLenth': 1, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 1s'     },
                            '5 secs' :{'SizeIndex': 1, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 5s'     },
                            '10 secs':{'SizeIndex': 2, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':30, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 10s'    },
                            '15 secs':{'SizeIndex': 3, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':20, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 15s'    },
                            '30 secs':{'SizeIndex': 4, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 30s'    },
                            '1 min'  :{'SizeIndex': 5, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':"IBKR 1m"     },
                            '2 mins' :{'SizeIndex': 6, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 2m'     },
                            '3 mins' :{'SizeIndex': 7, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 3m'     },
                            '5 mins' :{'SizeIndex': 8, 'DurationIndex':1, 'DurationLenth': 3, 'Rolling': 6, 'ChartDayDuration':  -1, 'indexTS': "5m", 'SheetName':'IBKR 5m'     },
                            '10 mins':{'SizeIndex': 9, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling': 6, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 10m'    },
                            '15 mins':{'SizeIndex':10, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 15m'    },
                            '20 mins':{'SizeIndex':11, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 20m'    },
                            '30 mins':{'SizeIndex':12, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':11, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 30m'    },
                            '1 hour' :{'SizeIndex':13, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':16, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 1H'     },
                            '2 hours':{'SizeIndex':14, 'DurationIndex':1, 'DurationLenth':34, 'Rolling': 8, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 2H'     },
                            '3 hours':{'SizeIndex':15, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':30, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 3H'     },
                            '4 hours':{'SizeIndex':16, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':20, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 4H'     },
                            '8 hours':{'SizeIndex':17, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':42, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 8H'     },
                            '1 day'  :{'SizeIndex':18, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':21, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Day'   },
                            '1W'     :{'SizeIndex':19, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1week'  },
                            '1M'     :{'SizeIndex':20, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Month' }
                            }

                for indexScope in timeScope:
                    # Import  data
                    dft = ImportData.fun (filePath_fun = filePathExcel , bookName = bookScope[indexScope].SheetName)
                    indexTS =TS.fun2(filePath=filePathExcel, bookScope=daySheet, scope=timeScope[indexScope])

                    # Loop 2:-
                    index = 0
                    for index in range(len(indexTS.index1)):
                        # Sampling data
                        df = dft[(indexTS.index1[index]):(indexTS.index2[index])]

                        #Make Indicator
                        EMA = addIndicator.fun(dataFrame = df, scope = timeScope[indexScope] )

                        #Make Yellow Color Candel 
                        mco = YellowCandel.fun(dataFrame = df) 

                        #Make a fibonacci lines
                        fabalines = FibonacciLines.fun (filePath_fun = filePathExcel)

                        #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                        setName = '\\' + tickerName + '_' + timeScope[indexScope] + '_' + indexTS.index4[index] + '_to_' + indexTS.index5[index]
                        save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                        #Make a chart
                        mpf.plot(data                   = df,
                                title                  = (tickerName + ' ' + timeScope[indexScope]), 
                                type                   = 'candle', 
                                #mav                    = (20,50),
                                volume                 = True,
                                show_nontrading        = False,
                                tight_layout           = True,
                                figratio               = (1,1),
                                figscale               = 3,
                                scale_padding          = 0.30,
                                figsize               = (12,6),
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
                        
            if (flagIBKR):
                # start the Function:-

            #------------------------------------------------
                # Create File:        
                        # datetime object containing current date and time --- Help Link :- https://www.programiz.com/python-programming/datetime/current-datetime#google_vignette
                now = datetime.now()
                dt_string = now.strftime("[%Y%m%d_%H%M%S]") # YYmmdd_HHMMSS
                sessionSymbol =  "zzIBKR" + ' ' + str(dt_string)
                rxChartPath = CreateFile.fun(directory = sessionSymbol, parent_dir = filePathChart)

            #------------------------------------------------
                # Loop 1:-
                daySheet = "IBKR 1Day"
                indexScope =  '5 secs'         
                timeScope = ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']
                bookScope = {
                            '1 secs' :{'SizeIndex': 0, 'DurationIndex':1, 'DurationLenth': 1, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 1s'     },
                            '5 secs' :{'SizeIndex': 1, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 5s'     },
                            '10 secs':{'SizeIndex': 2, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':30, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 10s'    },
                            '15 secs':{'SizeIndex': 3, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':20, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 15s'    },
                            '30 secs':{'SizeIndex': 4, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 30s'    },
                            '1 min'  :{'SizeIndex': 5, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':"IBKR 1m"     },
                            '2 mins' :{'SizeIndex': 6, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 2m'     },
                            '3 mins' :{'SizeIndex': 7, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 3m'     },
                            '5 mins' :{'SizeIndex': 8, 'DurationIndex':1, 'DurationLenth': 3, 'Rolling': 6, 'ChartDayDuration':  -1, 'indexTS': "5m", 'SheetName':'IBKR 5m'     },
                            '10 mins':{'SizeIndex': 9, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling': 6, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 10m'    },
                            '15 mins':{'SizeIndex':10, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 15m'    },
                            '20 mins':{'SizeIndex':11, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 20m'    },
                            '30 mins':{'SizeIndex':12, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':11, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 30m'    },
                            '1 hour' :{'SizeIndex':13, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':16, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 1H'     },
                            '2 hours':{'SizeIndex':14, 'DurationIndex':1, 'DurationLenth':34, 'Rolling': 8, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 2H'     },
                            '3 hours':{'SizeIndex':15, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':30, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 3H'     },
                            '4 hours':{'SizeIndex':16, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':20, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 4H'     },
                            '8 hours':{'SizeIndex':17, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':42, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 8H'     },
                            '1 day'  :{'SizeIndex':18, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':21, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Day'   },
                            '1W'     :{'SizeIndex':19, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1week'  },
                            '1M'     :{'SizeIndex':20, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Month' }
                            }

                for indexScope in timeScope:
                #------------------------------------------------
                    # Import  data
                    dft = ImportData.fun2 (filePath_fun = filePathExcel , bookName = bookScope[indexScope]['SheetName'])    #   'YAHOO'      'IBKR 30m'  IBKR 1H
                    indexTS =TS.fun4(filePath=filePathExcel, bookScope=daySheet, scope=indexScope)
                    

                #------------------------------------------------
                    # Loop 2:-
                    index = 0
                    for index in range(len(indexTS.index1)):
                        # Sampling data
                        df = dft[(indexTS.index1[index]):(indexTS.index2[index])]

                        # df = dft['2023-09-20 09:30:00':'2023-09-20 10:00:00']
                        # df = dft
                        # print (df)

                    #------------------------------------------------
                        #Make Indicator
                        EMA = addIndicator.fun2(dataFrame = df, scope = indexScope )    # need one for IBKR

                        #Make Yellow Color Candel 
                        mco = YellowCandel.fun(dataFrame = df) 

                        #Make a fibonacci lines
                        fabalines = FibonacciLines.fun (filePath_fun = filePathExcel)

                        #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                        setName = '\\' + tickerName + '_' + indexScope + '_' + indexTS.index4[index] + '_to_' + indexTS.index5[index]
                        save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                        #Make a chart
                        mpf.plot(data                   = df,
                                title                  = (tickerName + ' ' + indexScope), 
                                type                   = 'candle', 
                                #mav                    = (20,50),
                                volume                 = True,
                                show_nontrading        = False,
                                tight_layout           = True,
                                figratio               = (1,1),
                                figscale               = 3,
                                scale_padding          = 0.30,
                                figsize               = (12,6),
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
###_____________________________________________________________________________________________________________________________________________________________________________________
def fun3(   # Set Varibles
            #------------------------------------------------
                tickerName = 'AAPL',     
                filePathExcel = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\Session [20230921_221745]\AAPL\OK AAPL.xlsx",
                filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg',            #C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
                flagYahoo = True,
                flagIBKR = True,
                imageType= '.png'
        ):
            ###___________________________________________________________________________________________________________________________
            if (flagYahoo):
                # start the Function:-
                rxChartPath = CreateFile.fun(directory = "Yahoo", parent_dir = filePathChart)

                # Loop 1:-
                daySheet = "Yahoo Dayes"
                indexScope = 0
                bookScope = ["Yahoo 1m","Yahoo 5m","Yahoo 30m","Yahoo Hours","Yahoo Dayes"]
                timeScope = ["1m","5m","30m","1h","1d"] 

                for indexScope in range(len(bookScope)):
                    # Import  data
                    dft = ImportData.fun (filePath_fun = filePathExcel , bookName = bookScope[indexScope])
                    indexTS =TS.fun2(filePath=filePathExcel, bookScope=daySheet, scope=timeScope[indexScope])

                    # Loop 2:-
                    index = 0
                    for index in range(len(indexTS.index1)):
                        # Sampling data
                        df = dft[(indexTS.index1[index]):(indexTS.index2[index])]

                        #Make Indicator
                        EMA = addIndicator.fun(dataFrame = df, scope = timeScope[indexScope] )

                        #Make Yellow Color Candel 
                        mco = YellowCandel.fun(dataFrame = df) 

                        #Make a fibonacci lines
                        fabalines = FibonacciLines.fun (filePath_fun = filePathExcel)

                        #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                        setName = '\\' + tickerName + '_' + timeScope[indexScope] + '_' + indexTS.index4[index] + '_to_' + indexTS.index5[index]
                        save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                        #Make a chart
                        mpf.plot(    data                   = df
                                    ,title                  = (tickerName + ' ' + timeScope[indexScope])
                                    ,type                   = 'candle' 
                                    #,mav                    = (20,50)
                                    ,volume                 = True
                                    ,show_nontrading        = False
                                    ,tight_layout           = True
                                    ,figratio               = (1,1)
                                    ,figscale               = 3
                                    ,scale_padding          = 0.30
                                    ,figsize                = (12,6)
                                    #,ylim                   = (((df.Low.min())*0.95) ,((df.High.max())*1.05)) # set min and max of Chart
                                    ,ylim                   = (((df.Low.min())-0.03) ,((df.High.max())+0.03)) # set min and max of Chart
                                    ,xrotation              = 0
                                    ,yscale                 = "linear" # y-axis scale: "linear", "log", "symlog", or "logit"
                                    ,volume_yscale          = "linear" # Volume y-axis scale: "linear", "log", "symlog", or "logit"
                                    ,style                  = EhabStaylo
                                    ,marketcolor_overrides  = mco
                                    ,mco_faceonly           = False
                                    ,addplot                = EMA
                                    ,hlines                 = fabalines
                                    ,savefig                = save # link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                    #,marketcolor_overrides = mco  # link https://github.com/matplotlib/mplfinance/blob/master/examples/marketcolor_overrides.ipynb
                                )
            ###___________________________________________________________________________________________________________________________                        
            if (flagIBKR):
                # start the Function:-

            #------------------------------------------------
                # Create File:        
                        # datetime object containing current date and time --- Help Link :- https://www.programiz.com/python-programming/datetime/current-datetime#google_vignette
                now = datetime.now()
                dt_string = now.strftime("[%Y%m%d_%H%M%S]") # YYmmdd_HHMMSS
                sessionSymbol =  "zzIBKR" + ' ' + str(dt_string)
                rxChartPath = CreateFile.fun(directory = sessionSymbol, parent_dir = filePathChart)

            #------------------------------------------------
                # Loop 1:-
                Fobi_Var = FibonacciLines.FiboClass()
                imgCount = 0
                daySheet = "IBKR 1Day"
                indexScope =  '5 secs'         
                timeScope = ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']      #   ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']
                bookScope = {
                            '1 secs' :{'SizeIndex': 0, 'DurationIndex':1, 'DurationLenth': 1, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 1s'     },
                            '5 secs' :{'SizeIndex': 1, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 5s'     },
                            '10 secs':{'SizeIndex': 2, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':30, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 10s'    },
                            '15 secs':{'SizeIndex': 3, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':20, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 15s'    },
                            '30 secs':{'SizeIndex': 4, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 30s'    },
                            '1 min'  :{'SizeIndex': 5, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':"IBKR 1m"     },
                            '2 mins' :{'SizeIndex': 6, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 2m'     },
                            '3 mins' :{'SizeIndex': 7, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 3m'     },
                            '5 mins' :{'SizeIndex': 8, 'DurationIndex':1, 'DurationLenth': 3, 'Rolling': 6, 'ChartDayDuration':  -1, 'indexTS': "5m", 'SheetName':'IBKR 5m'     },
                            '10 mins':{'SizeIndex': 9, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling': 6, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 10m'    },
                            '15 mins':{'SizeIndex':10, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 15m'    },
                            '20 mins':{'SizeIndex':11, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 20m'    },
                            '30 mins':{'SizeIndex':12, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':11, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 30m'    },
                            '1 hour' :{'SizeIndex':13, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':16, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 1H'     },
                            '2 hours':{'SizeIndex':14, 'DurationIndex':1, 'DurationLenth':34, 'Rolling': 8, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 2H'     },
                            '3 hours':{'SizeIndex':15, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':30, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 3H'     },
                            '4 hours':{'SizeIndex':16, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':20, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 4H'     },
                            '8 hours':{'SizeIndex':17, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':42, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 8H'     },
                            '1 day'  :{'SizeIndex':18, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':21, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Day'   },
                            '1W'     :{'SizeIndex':19, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1week'  },
                            '1M'     :{'SizeIndex':20, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Month' }
                            }

                for indexScope in timeScope:
                #------------------------------------------------
                    # Import  data
                    dft = ImportData.fun2 (filePath_fun = filePathExcel , bookName = bookScope[indexScope]['SheetName'])    #   'YAHOO'      'IBKR 30m'  IBKR 1H
                    if( len(dft.index) == 0 ):
                        print ( "This Sheet : ",bookScope[indexScope]['SheetName']," is Empty")
                    if( len(dft.index) > 0 ):
                        
                        TimeStamp_df =TS.fun5(   filePath           = filePathExcel
                                                ,timeStampPath      = r"D:\Python Tools\ChartMaker\SourceDocuments\InPut_Excel\Time_Stamp.xlsx"
                                                ,timeStampSheet     = "Ver1"
                                                ,DaySheetName       = daySheet 
                                                ,scope              = indexScope # ["5s","1m","5m","30m","1h","1d"]  
                                                ,scopeBook          = {
                                                                        "5s":"5s"
                                                                        ,'5 secs':"5s"
                                                                        ,"1m":"1m"
                                                                        ,'1 min':"1m"
                                                                        ,"5m":"5m"
                                                                        ,'5 mins':"5m"
                                                                        ,"30m":"30m"
                                                                        ,'30 mins':"30m"
                                                                        ,"1h":"1h"
                                                                        ,'1 hour':"1h"
                                                                        ,"1d":"1d" 
                                                                        ,'1 day':"1d" 
                                                                    }   
                                            )
                        

                    #------------------------------------------------
                        # Loop 2:-
                        
                        index = 0
                        for index in range(len(TimeStamp_df.Index1)):
                            
                            # Sampling data

                            df = dft[(TimeStamp_df.Index1[index]):(TimeStamp_df.Index2[index])]

                            # df = dft['2023-09-20 09:30:00':'2023-09-20 10:00:00']
                            # df = dft
                            # print (df)

                        #------------------------------------------------
                            #Make Indicator
                            EMA = addIndicator.fun3(dataFrame = df, scope = indexScope )    # need one for IBKR

                            #Make Yellow Color Candel 
                            mco = YellowCandel.fun(dataFrame = df) 
                            
                            #Make Time Lable
                            outLable = TS.fTimeLable  (  f_Scope        = TimeStamp_df.Scope[index] # (source=daySheet   ,interval=indexScope   ,inList=list (df.index.map(str)))
                                                        ,f_HourConstant = TimeStamp_df.HourConstant[index]
                                                        ,f_MinConstant  = TimeStamp_df.MinConstant[index]
                                                        ,f_SecConstant  = TimeStamp_df.SecConstant[index]
                                                        ,f_leftSide     = TimeStamp_df.leftSide[index]
                                                        ,source         = "IBKR"
                                                        ,interval       = indexScope
                                                        ,inList         = list (df.index.map(str))
                                                    )

                            #Make a fibonacci lines
                            Fobi_Var = FibonacciLines.fun2 (     filePath_fun   = filePathExcel
                                                                ,Fobi_Input     = Fobi_Var
                                                                ,DaySheetName   = daySheet 
                                                                ,fibonacciIndex = TimeStamp_df.Fibonacci[index]
                                                                ,fibonacciBook  ={
                                                                                    "Last5Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-61	,	"EndDelta":	-1			},
                                                                                    "Last1Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-13	,	"EndDelta":	-1			},
                                                                                    "Last1Month"	:{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-31	,	"EndDelta":	-2			},
                                                                                    "Last1Week"	    :{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-6	,	"EndDelta":	-2			},
                                                                                    "Yesterday"	    :{	'SheetName':	'IBKR 4H'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                                                                    "PreMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"06:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                                                                    "PreMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"06:00:00"	,	"PeriodEnd":	"08:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"06:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "MarketOpen"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"09:00:00"	,	"PeriodEnd":	"10:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"09:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Midday"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"10:00:00"	,	"PeriodEnd":	"14:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"10:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "PowerHour"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"14:00:00"	,	"PeriodEnd":	"16:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"14:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "AfterMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"16:00:00"	,	"PeriodEnd":	"18:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"16:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "AfterMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"18:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"18:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Final"	        :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"20:00:00"	,	"PeriodEnd":	"00:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Random1"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Random2"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Random3"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Random4"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Random5"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			}
                                                                                }
                                                            )

                            #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                            setName = '\\' + tickerName + '_' + str("%03d"%imgCount) + '_'  + indexScope + '_' + TimeStamp_df.Name[index] 
                            save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                            #Make a chart
                            fig, axlist = mpf.plot(  data                   = df
                                                    # ,title                  = (tickerName + ' ' + indexScope)
                                                    ,type                   = 'candle' 
                                                    # ,mav                    = (20,50)
                                                    ,volume                 = True
                                                    ,show_nontrading        = False
                                                    ,tight_layout           = True
                                                    ,figratio               = (1,1)
                                                    ,figscale               = 3
                                                    ,scale_padding          = 0.30
                                                    ,figsize               = (12,6)
                                                    # ,ylim                   = (((df.Low.min())*0.95) ,((df.High.max())*1.05)) # set min and max of Chart
                                                    ,ylim                   = (((df.Low.min())-0.03) ,((df.High.max())+0.03)) # set min and max of Chart
                                                    ,xrotation              = 0
                                                    ,yscale                 = "linear" # y-axis scale: "linear", "log", "symlog", or "logit"
                                                    ,volume_yscale          = "linear" # Volume y-axis scale: "linear", "log", "symlog", or "logit"
                                                    ,style                  = EhabStaylo
                                                    ,marketcolor_overrides  = mco
                                                    ,mco_faceonly           = False
                                                    ,addplot                = EMA
                                                    ,hlines                 = Fobi_Var.fibolines
                                                    ,returnfig=True
                                                    # ,savefig                = save # link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                                    # ,marketcolor_overrides = mco  # link https://github.com/matplotlib/mplfinance/blob/master/examples/marketcolor_overrides.ipynb
                            )
                            
                            #Add Time Lable & Saving     link:   https://github.com/matplotlib/mplfinance/issues/573
                            axlist[-2].set_xticks(outLable["ticks"])
                            axlist[-2].set_xticklabels(outLable["tlabs"], ha='center')
                            axlist[-2].set_xticks(outLable["mitks"],minor=True)
                            axlist[-2].set_xticklabels(outLable["milab"], ha='center', minor=True, rotation=0) 
                            fig.savefig( fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0, bbox_inches='tight' )
                            imgCount += 1

                            # mpf.show()
                            # matplotlib.pyplot.savefig()
                            # fig.save()
                            
                            # axlist[-2].save()
                            # fig.savefig( 'myplot.pdf', bbox_inches='tight' )
            ###___________________________________________________________________________________________________________________________
###_____________________________________________________________________________________________________________________________________________________________________________________

###_____________________________________________________________________________________________________________________________________________________________________________________
def fun4(   # Set Varibles
            #------------------------------------------------
                tickerName = 'AAPL',     
                filePathExcel = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\Session [20230921_221745]\AAPL\OK AAPL.xlsx",
                filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg',            #C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
                flagYahoo = True,
                flagIBKR = True,
                imageType= '.png'
        ):
            ###___________________________________________________________________________________________________________________________
            if (flagYahoo):
                # start the Function:-
                rxChartPath = CreateFile.fun(directory = "Yahoo", parent_dir = filePathChart)

                # Loop 1:-
                daySheet = "Yahoo Dayes"
                indexScope = 0
                bookScope = ["Yahoo 1m","Yahoo 5m","Yahoo 30m","Yahoo Hours","Yahoo Dayes"]
                timeScope = ["1m","5m","30m","1h","1d"] 

                for indexScope in range(len(bookScope)):
                    # Import  data
                    dft = ImportData.fun (filePath_fun = filePathExcel , bookName = bookScope[indexScope])
                    indexTS =TS.fun2(filePath=filePathExcel, bookScope=daySheet, scope=timeScope[indexScope])

                    # Loop 2:-
                    index = 0
                    for index in range(len(indexTS.index1)):
                        # Sampling data
                        df = dft[(indexTS.index1[index]):(indexTS.index2[index])]

                        #Make Indicator
                        EMA = addIndicator.fun(dataFrame = df, scope = timeScope[indexScope] )

                        #Make Yellow Color Candel 
                        mco = YellowCandel.fun(dataFrame = df) 

                        #Make a fibonacci lines
                        fabalines = FibonacciLines.fun (filePath_fun = filePathExcel)

                        #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                        setName = '\\' + tickerName + '_' + timeScope[indexScope] + '_' + indexTS.index4[index] + '_to_' + indexTS.index5[index]
                        save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                        #Make a chart
                        mpf.plot(data                   = df,
                                title                  = (tickerName + ' ' + timeScope[indexScope]), 
                                type                   = 'candle', 
                                #mav                    = (20,50),
                                volume                 = True,
                                show_nontrading        = False,
                                tight_layout           = True,
                                figratio               = (1,1),
                                figscale               = 3,
                                scale_padding          = 0.30,
                                figsize               = (12,6),
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
            ###___________________________________________________________________________________________________________________________                        
            if (flagIBKR):
                # start the Function:-

            #------------------------------------------------
                # Create File:        
                        # datetime object containing current date and time --- Help Link :- https://www.programiz.com/python-programming/datetime/current-datetime#google_vignette
                now = datetime.now()
                dt_string = now.strftime("[%Y%m%d_%H%M%S]") # YYmmdd_HHMMSS
                sessionSymbol =  "zzIBKR" + ' ' + str(dt_string)
                rxChartPath = CreateFile.fun(directory = sessionSymbol, parent_dir = filePathChart)

            #------------------------------------------------
                # Loop 1:-
                Fobi_Var = FibonacciLines.FiboClass()
                imgCount = 0
                daySheet = "IBKR 1Day"
                indexScope =  '5 secs'         
                timeScope = ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']      #   ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']
                bookScope = {
                            '1 secs' :{'SizeIndex': 0, 'DurationIndex':1, 'DurationLenth': 1, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 1s'     },
                            '5 secs' :{'SizeIndex': 1, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 5s'     },
                            '10 secs':{'SizeIndex': 2, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':30, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 10s'    },
                            '15 secs':{'SizeIndex': 3, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':20, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 15s'    },
                            '30 secs':{'SizeIndex': 4, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 30s'    },
                            '1 min'  :{'SizeIndex': 5, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':"IBKR 1m"     },
                            '2 mins' :{'SizeIndex': 6, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 2m'     },
                            '3 mins' :{'SizeIndex': 7, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 3m'     },
                            '5 mins' :{'SizeIndex': 8, 'DurationIndex':1, 'DurationLenth': 3, 'Rolling': 6, 'ChartDayDuration':  -1, 'indexTS': "5m", 'SheetName':'IBKR 5m'     },
                            '10 mins':{'SizeIndex': 9, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling': 6, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 10m'    },
                            '15 mins':{'SizeIndex':10, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 15m'    },
                            '20 mins':{'SizeIndex':11, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 20m'    },
                            '30 mins':{'SizeIndex':12, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':11, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 30m'    },
                            '1 hour' :{'SizeIndex':13, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':16, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 1H'     },
                            '2 hours':{'SizeIndex':14, 'DurationIndex':1, 'DurationLenth':34, 'Rolling': 8, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 2H'     },
                            '3 hours':{'SizeIndex':15, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':30, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 3H'     },
                            '4 hours':{'SizeIndex':16, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':20, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 4H'     },
                            '8 hours':{'SizeIndex':17, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':42, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 8H'     },
                            '1 day'  :{'SizeIndex':18, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':21, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Day'   },
                            '1W'     :{'SizeIndex':19, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1week'  },
                            '1M'     :{'SizeIndex':20, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Month' }
                            }

                for indexScope in timeScope:
                #------------------------------------------------
                    # Import  data
                    dft = ImportData.fun2 (filePath_fun = filePathExcel , bookName = bookScope[indexScope]['SheetName'])    #   'YAHOO'      'IBKR 30m'  IBKR 1H
                    if( len(dft.index) == 0 ):
                        print ( "This Sheet : ",bookScope[indexScope]['SheetName']," is Empty")
                    if( len(dft.index) > 0 ):
                        
                        TimeStamp_df =TS.fun5(   filePath           = filePathExcel
                                                ,timeStampPath      = r"D:\Python Tools\ChartMaker\SourceDocuments\InPut_Excel\Time_Stamp.xlsx"
                                                ,timeStampSheet     = "Ver1"
                                                ,DaySheetName       = daySheet 
                                                ,scope              = indexScope # ["5s","1m","5m","30m","1h","1d"]  
                                                ,scopeBook          = {
                                                                        "5s":"5s"
                                                                        ,'5 secs':"5s"
                                                                        ,"1m":"1m"
                                                                        ,'1 min':"1m"
                                                                        ,"5m":"5m"
                                                                        ,'5 mins':"5m"
                                                                        ,"30m":"30m"
                                                                        ,'30 mins':"30m"
                                                                        ,"1h":"1h"
                                                                        ,'1 hour':"1h"
                                                                        ,"1d":"1d" 
                                                                        ,'1 day':"1d" 
                                                                    }   
                                            )
                        

                    #------------------------------------------------
                        # Loop 2:-
                        
                        index = 0
                        for index in range(len(TimeStamp_df.Index1)):
                            
                            # Sampling data

                            df = dft[(TimeStamp_df.Index1[index]):(TimeStamp_df.Index2[index])]                 
                            dfH = df.High.max()
                            dfL = df.Low.min()
                            dfD = (dfH - dfL) * 0.05 

                            # df = dft['2023-09-20 09:30:00':'2023-09-20 10:00:00']
                            # df = dft
                            # print (df)

                        #------------------------------------------------
                            #Make Indicator
                            EMA = addIndicator.fun2(dataFrame = df, scope = indexScope )    # need one for IBKR

                            #Make Yellow Color Candel 
                            mco = YellowCandel.fun(dataFrame = df) 
                            
                            #Make Time Lable
                            timeLable = TS.fTimeLable  (  f_Scope        = TimeStamp_df.Scope[index] # (source=daySheet   ,interval=indexScope   ,inList=list (df.index.map(str)))
                                                        ,f_HourConstant = TimeStamp_df.HourConstant[index]
                                                        ,f_MinConstant  = TimeStamp_df.MinConstant[index]
                                                        ,f_SecConstant  = TimeStamp_df.SecConstant[index]
                                                        ,f_leftSide     = TimeStamp_df.leftSide[index]
                                                        ,source         = "IBKR"
                                                        ,interval       = indexScope
                                                        ,inList         = list (df.index.map(str))
                                                    )

                            #Make Price Label
                            priceLabel = TS.LabelPrice  (    pMax = dfH + dfD
                                                            ,pMin = dfL - dfD
                                                        )

                            #Make a fibonacci lines
                            Fobi_Var = FibonacciLines.fun2 (     filePath_fun   = filePathExcel
                                                                ,Fobi_Input     = Fobi_Var
                                                                ,DaySheetName   = daySheet 
                                                                ,fibonacciIndex = TimeStamp_df.Fibonacci[index]
                                                                ,fibonacciBook  ={
                                                                                    "Last5Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-61	,	"EndDelta":	-1			},
                                                                                    "Last1Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-13	,	"EndDelta":	-1			},
                                                                                    "Last1Month"	:{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-31	,	"EndDelta":	-2			},
                                                                                    "Last1Week"	    :{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-6	,	"EndDelta":	-2			},
                                                                                    "Yesterday"	    :{	'SheetName':	'IBKR 4H'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                                                                    "PreMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"06:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                                                                    "PreMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"06:00:00"	,	"PeriodEnd":	"08:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"06:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "MarketOpen"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"09:00:00"	,	"PeriodEnd":	"10:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"09:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Midday"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"10:00:00"	,	"PeriodEnd":	"14:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"10:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "PowerHour"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"14:00:00"	,	"PeriodEnd":	"16:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"14:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "AfterMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"16:00:00"	,	"PeriodEnd":	"18:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"16:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "AfterMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"18:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"18:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Final"	        :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"20:00:00"	,	"PeriodEnd":	"00:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Random1"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Random2"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Random3"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Random4"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                    "Random5"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			}
                                                                                }
                                                            )

                            #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                            setName = '\\' + tickerName + '_' + str("%03d"%imgCount) + '_'  + indexScope + '_' + TimeStamp_df.Name[index] 
                            save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                            #Make a chart
                            fig, axlist = mpf.plot(  data                   = df
                                                    ,title                  = (tickerName + ' ' + indexScope)
                                                    ,type                   = 'candle' 
                                                    # ,mav                    = (20,50)
                                                    ,volume                 = True
                                                    ,show_nontrading        = False
                                                    ,tight_layout           = True
                                                    ,figratio               = (1,1)
                                                    ,figscale               = 3
                                                    ,scale_padding          = 0.30
                                                    ,figsize               = (12,6)
                                                    # ,ylim                   = (((df.Low.min())*0.95) ,((df.High.max())*1.05)) # set min and max of Chart
                                                    ,ylim                   = ((dfL - dfD) ,(dfH + dfD)) # set min and max of Chart (dfH + dfD)
                                                    ,xrotation              = 0
                                                    ,yscale                 = "linear" # y-axis scale: "linear", "log", "symlog", or "logit"
                                                    ,volume_yscale          = "linear" # Volume y-axis scale: "linear", "log", "symlog", or "logit"
                                                    ,style                  = EhabStaylo
                                                    ,marketcolor_overrides  = mco
                                                    ,mco_faceonly           = False
                                                    ,addplot                = EMA
                                                    ,hlines                 = Fobi_Var.fibolines
                                                    ,returnfig=True
                                                    # ,savefig                = save # link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                                    # ,marketcolor_overrides = mco  # link https://github.com/matplotlib/mplfinance/blob/master/examples/marketcolor_overrides.ipynb
                            )
                            
                            #Add Time Lable & Saving     link:   https://github.com/matplotlib/mplfinance/issues/573
                            axlist[-2].set_xticks(timeLable["ticks"])
                            axlist[-2].set_xticklabels(timeLable["tlabs"], ha='center')
                            axlist[-2].set_xticks(timeLable["mitks"],minor=True)
                            axlist[-2].set_xticklabels(timeLable["milab"], ha='center', minor=True, rotation=0) 

                            axlist[0].set_yticks( priceLabel['ticks'] )
                            axlist[0].set_yticklabels( priceLabel['tlabs'] )

                            fig.savefig( fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0, bbox_inches='tight' )
                            imgCount += 1

                            # mpf.show()
                            # matplotlib.pyplot.savefig()
                            # fig.save()
                            
                            # axlist[-2].save()
                            # fig.savefig( 'myplot.pdf', bbox_inches='tight' )



            ###___________________________________________________________________________________________________________________________
###_____________________________________________________________________________________________________________________________________________________________________________________

###_____________________________________________________________________________________________________________________________________________________________________________________
def fun5(   # Set Varibles
            #------------------------------------------------
                tickerName = 'AAPL',     
                filePathExcel = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\Session [20230921_221745]\AAPL\OK AAPL.xlsx",
                filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg',            #C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
                flagYahoo = True,
                flagIBKR = True,
                imageType= '.png'
        ):
            ###___________________________________________________________________________________________________________________________
            if (flagYahoo):
                # start the Function:-
                rxChartPath = CreateFile.fun(directory = "Yahoo", parent_dir = filePathChart)

                # Loop 1:-
                daySheet = "Yahoo Dayes"
                indexScope = 0
                bookScope = ["Yahoo 1m","Yahoo 5m","Yahoo 30m","Yahoo Hours","Yahoo Dayes"]
                timeScope = ["1m","5m","30m","1h","1d"] 

                for indexScope in range(len(bookScope)):
                    # Import  data
                    dft = ImportData.fun (filePath_fun = filePathExcel , bookName = bookScope[indexScope])
                    indexTS =TS.fun2(filePath=filePathExcel, bookScope=daySheet, scope=timeScope[indexScope])

                    # Loop 2:-
                    index = 0
                    for index in range(len(indexTS.index1)):
                        # Sampling data
                        df = dft[(indexTS.index1[index]):(indexTS.index2[index])]

                        #Make Indicator
                        EMA = addIndicator.fun(dataFrame = df, scope = timeScope[indexScope] )

                        #Make Yellow Color Candel 
                        mco = YellowCandel.fun(dataFrame = df) 

                        #Make a fibonacci lines
                        fabalines = FibonacciLines.fun (filePath_fun = filePathExcel)

                        #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                        setName = '\\' + tickerName + '_' + timeScope[indexScope] + '_' + indexTS.index4[index] + '_to_' + indexTS.index5[index]
                        save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                        #Make a chart
                        mpf.plot(data                   = df,
                                title                  = (tickerName + ' ' + timeScope[indexScope]), 
                                type                   = 'candle', 
                                #mav                    = (20,50),
                                volume                 = True,
                                show_nontrading        = False,
                                tight_layout           = True,
                                figratio               = (1,1),
                                figscale               = 3,
                                scale_padding          = 0.30,
                                figsize               = (12,6),
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
            ###___________________________________________________________________________________________________________________________                                                
            if (flagIBKR):
                # start the Function:-

            #------------------------------------------------
                # Create File:        
                        # datetime object containing current date and time --- Help Link :- https://www.programiz.com/python-programming/datetime/current-datetime#google_vignette
                now = datetime.now()
                dt_string = now.strftime("[%Y%m%d_%H%M%S]") # YYmmdd_HHMMSS
                sessionSymbol =  "zzIBKR" + ' ' + str(dt_string)
                rxChartPath = CreateFile.fun(directory = sessionSymbol, parent_dir = filePathChart)

            #------------------------------------------------
                # Loop 1:-
                Fobi_Var = FibonacciLines.FiboClass()
                imgCount = 0
                daySheet = "IBKR 1Day"
                indexScope =  '5 secs'         
                timeScope = ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']      #   ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']
                bookScope = {
                            '1 secs' :{'SizeIndex': 0, 'DurationIndex':1, 'DurationLenth': 1, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 1s'     },
                            '5 secs' :{'SizeIndex': 1, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 5s'     },
                            '10 secs':{'SizeIndex': 2, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':30, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 10s'    },
                            '15 secs':{'SizeIndex': 3, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':20, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 15s'    },
                            '30 secs':{'SizeIndex': 4, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 30s'    },
                            '1 min'  :{'SizeIndex': 5, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':"IBKR 1m"     },
                            '2 mins' :{'SizeIndex': 6, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 2m'     },
                            '3 mins' :{'SizeIndex': 7, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 3m'     },
                            '5 mins' :{'SizeIndex': 8, 'DurationIndex':1, 'DurationLenth': 3, 'Rolling': 6, 'ChartDayDuration':  -1, 'indexTS': "5m", 'SheetName':'IBKR 5m'     },
                            '10 mins':{'SizeIndex': 9, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling': 6, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 10m'    },
                            '15 mins':{'SizeIndex':10, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 15m'    },
                            '20 mins':{'SizeIndex':11, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 20m'    },
                            '30 mins':{'SizeIndex':12, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':11, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 30m'    },
                            '1 hour' :{'SizeIndex':13, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':16, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 1H'     },
                            '2 hours':{'SizeIndex':14, 'DurationIndex':1, 'DurationLenth':34, 'Rolling': 8, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 2H'     },
                            '3 hours':{'SizeIndex':15, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':30, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 3H'     },
                            '4 hours':{'SizeIndex':16, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':20, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 4H'     },
                            '8 hours':{'SizeIndex':17, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':42, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 8H'     },
                            '1 day'  :{'SizeIndex':18, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':21, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Day'   },
                            '1W'     :{'SizeIndex':19, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1week'  },
                            '1M'     :{'SizeIndex':20, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Month' }
                            }

                for indexScope in timeScope:
                #------------------------------------------------
                    # Import  data
                    dft = ImportData.fun2 (filePath_fun = filePathExcel , bookName = bookScope[indexScope]['SheetName'])    #   'YAHOO'      'IBKR 30m'  IBKR 1H
                    if( len(dft.index) == 0 ):
                        print ( "This Sheet : ",bookScope[indexScope]['SheetName']," is Empty")
                    if( len(dft.index) > 0 ):
                        
                        TimeStamp_df =TS.fun5(   filePath           = filePathExcel
                                                ,timeStampPath      = r"D:\Python Tools\ChartMaker\SourceDocuments\InPut_Excel\Time_Stamp.xlsx"
                                                ,timeStampSheet     = "Ver1"
                                                ,DaySheetName       = daySheet 
                                                ,scope              = indexScope # ["5s","1m","5m","30m","1h","1d"]  
                                                ,scopeBook          = {
                                                                        "5s":"5s"
                                                                        ,'5 secs':"5s"
                                                                        ,"1m":"1m"
                                                                        ,'1 min':"1m"
                                                                        ,"5m":"5m"
                                                                        ,'5 mins':"5m"
                                                                        ,"30m":"30m"
                                                                        ,'30 mins':"30m"
                                                                        ,"1h":"1h"
                                                                        ,'1 hour':"1h"
                                                                        ,"1d":"1d" 
                                                                        ,'1 day':"1d" 
                                                                    }   
                                            )
                        

                    #------------------------------------------------
                        # Loop 2:-
                        
                        index = 0
                        for index in range(len(TimeStamp_df.Index1)):
                            
                            # Sampling data

                            df = dft[(TimeStamp_df.Index1[index]):(TimeStamp_df.Index2[index])]
                            if( len(df.index) == 0 ):
                                print ( "This Time Segment : " ,TimeStamp_df.Index1[index] ,":"  ,TimeStamp_df.Index2[index]   ," is Empty")
                            if( len(df.index) > 0 ):                 
                                dfH = df.High.max()
                                dfL = df.Low.min()
                                dfD = (dfH - dfL) * 0.05 

                                # df = dft['2023-09-20 09:30:00':'2023-09-20 10:00:00']
                                # df = dft
                                # print (df)

                            #------------------------------------------------
                                #Make Indicator
                                EMA = addIndicator.fun4(dataFrame = df, scope = indexScope )    # need one for IBKR

                                #Make Yellow Color Candel 
                                mco = YellowCandel.fun(dataFrame = df) 
                                
                                #Make Time Lable
                                timeLable = TS.fTimeLable2  (  f_Scope        = TimeStamp_df.Scope[index] # (source=daySheet   ,interval=indexScope   ,inList=list (df.index.map(str)))
                                                            ,f_HourConstant = TimeStamp_df.HourConstant[index]
                                                            ,f_MinConstant  = TimeStamp_df.MinConstant[index]
                                                            ,f_SecConstant  = TimeStamp_df.SecConstant[index]
                                                            ,f_leftSide     = TimeStamp_df.leftSide[index]
                                                            ,source         = "IBKR"
                                                            ,interval       = indexScope
                                                            ,inList         = list (df.index.map(str))
                                                        )

                                #Make Price Label
                                priceLabel = TS.LabelPrice5 (    pMax = dfH + dfD
                                                                ,pMin = dfL - dfD
                                                            )

                                #Make a fibonacci lines
                                Fobi_Var = FibonacciLines.fun2 (     filePath_fun   = filePathExcel
                                                                    ,Fobi_Input     = Fobi_Var
                                                                    ,DaySheetName   = daySheet 
                                                                    ,fibonacciIndex = TimeStamp_df.Fibonacci[index]
                                                                    ,fibonacciBook  ={
                                                                                        "Last5Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-61	,	"EndDelta":	-1			},
                                                                                        "Last1Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-13	,	"EndDelta":	-1			},
                                                                                        "Last1Month"	:{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-31	,	"EndDelta":	-2			},
                                                                                        "Last1Week"	    :{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-6	,	"EndDelta":	-2			},
                                                                                        "Yesterday"	    :{	'SheetName':	'IBKR 4H'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                                                                        "PreMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"06:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                                                                        "PreMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"06:00:00"	,	"PeriodEnd":	"08:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"06:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "MarketOpen"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"09:00:00"	,	"PeriodEnd":	"10:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"09:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Midday"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"10:00:00"	,	"PeriodEnd":	"14:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"10:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "PowerHour"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"14:00:00"	,	"PeriodEnd":	"16:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"14:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "AfterMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"16:00:00"	,	"PeriodEnd":	"18:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"16:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "AfterMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"18:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"18:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Final"	        :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"20:00:00"	,	"PeriodEnd":	"00:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random1"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random2"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random3"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random4"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random5"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			}
                                                                                    }
                                                                )

                                #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                setName = '\\' + tickerName + '_' + str("%03d"%imgCount) + '_'  + indexScope + '_' + TimeStamp_df.Name[index] 
                                save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                                #Make a chart
                                fig, axlist = mpf.plot(  data                   = df
                                                        # ,title                  = (tickerName + ' ' + indexScope)
                                                        ,type                   = 'candle' 
                                                        # ,mav                    = (20,50)
                                                        ,volume                 = True
                                                        ,show_nontrading        = False
                                                        ,tight_layout           = True
                                                        ,figratio               = (1,1)
                                                        ,figscale               = 3
                                                        ,scale_padding          = 0.30
                                                        ,figsize               = (12,6)
                                                        # ,ylim                   = (((df.Low.min())*0.95) ,((df.High.max())*1.05)) # set min and max of Chart
                                                        ,ylim                   = ((dfL - dfD) ,(dfH + dfD)) # set min and max of Chart (dfH + dfD)
                                                        ,xrotation              = 0
                                                        ,yscale                 = "linear" # y-axis scale: "linear", "log", "symlog", or "logit"
                                                        ,volume_yscale          = "linear" # Volume y-axis scale: "linear", "log", "symlog", or "logit"
                                                        ,style                  = EhabStaylo
                                                        ,marketcolor_overrides  = mco
                                                        ,mco_faceonly           = False
                                                        ,addplot                = EMA
                                                        ,hlines                 = Fobi_Var.fibolines
                                                        ,returnfig=True
                                                        # ,savefig                = save # link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                                        # ,marketcolor_overrides = mco  # link https://github.com/matplotlib/mplfinance/blob/master/examples/marketcolor_overrides.ipynb
                                )
                                
                                #Add Time Lable      Help link:   https://github.com/matplotlib/mplfinance/issues/573
                                axlist[-2].set_xticks(timeLable["ticks"])
                                axlist[-2].set_xticklabels(timeLable["tlabs"], ha='center')
                                axlist[-2].set_xticks(timeLable["mitks"],minor=True)
                                axlist[-2].set_xticklabels(timeLable["milab"], ha='center', minor=True, rotation=0) 

                                x2 = axlist[0].secondary_xaxis('top')
                                x2.set_xticks(timeLable["ticks"])
                                x2.set_xticklabels(timeLable["Utlabs"], ha='center')
                                x2.set_xticks(timeLable["mitks"],minor=True)
                                x2.set_xticklabels(timeLable["Umilab"], ha='center', minor=True, rotation=0)
                                

                                # x3 = axlist[0].secondary_xaxis(location=1.075)
                                # x3.set_xticks(timeLable["mitks"],minor=False)
                                # x3.set_xticklabels(timeLable["milab"], ha='center', minor=False, rotation=0) 

                                #Add Price Lable     Help Link:-   https://github.com/matplotlib/mplfinance/issues/604 
                                axlist[0].set_yticks( priceLabel['ticks'] )
                                axlist[0].set_yticklabels( priceLabel['tlabs'] )
                                
                                # axlist[0].secondary_yaxis('left')
                                y2 = axlist[0].secondary_yaxis('left')
                                y2.set_yticks(priceLabel['ticks'])
                                y2.set_yticklabels( priceLabel['tlabs'] )
                                # print(type(axlist[0]))
                                # print("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
                                # print(kota)

                                #Saving Chart        Help link:   https://github.com/matplotlib/mplfinance/issues/573
                                fig.savefig( fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0, bbox_inches='tight' )
                                imgCount += 1

                                # mpf.show()
                                # matplotlib.pyplot.savefig()
                                # fig.save()
                                
                                # axlist[-2].save()
                                # fig.savefig( 'myplot.pdf', bbox_inches='tight' )





                        ###___________________________________________________________________________________________________________________________
###_____________________________________________________________________________________________________________________________________________________________________________________

###_____________________________________________________________________________________________________________________________________________________________________________________
def fun6(   # Set Varibles
            #------------------------------------------------
                tickerName = 'AAPL',     
                filePathExcel = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\Session [20230921_221745]\AAPL\OK AAPL.xlsx",
                filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg',            #C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
                flagYahoo = True,
                flagIBKR = True,
                imageType= '.png'
        ):
            ###___________________________________________________________________________________________________________________________
            if (flagYahoo):
                # start the Function:-
                rxChartPath = CreateFile.fun(directory = "Yahoo", parent_dir = filePathChart)

                # Loop 1:-
                daySheet = "Yahoo Dayes"
                indexScope = 0
                bookScope = ["Yahoo 1m","Yahoo 5m","Yahoo 30m","Yahoo Hours","Yahoo Dayes"]
                timeScope = ["1m","5m","30m","1h","1d"] 

                for indexScope in range(len(bookScope)):
                    # Import  data
                    dft = ImportData.fun (filePath_fun = filePathExcel , bookName = bookScope[indexScope])
                    indexTS =TS.fun2(filePath=filePathExcel, bookScope=daySheet, scope=timeScope[indexScope])

                    # Loop 2:-
                    index = 0
                    for index in range(len(indexTS.index1)):
                        # Sampling data
                        df = dft[(indexTS.index1[index]):(indexTS.index2[index])]

                        #Make Indicator
                        EMA = addIndicator.fun(dataFrame = df, scope = timeScope[indexScope] )

                        #Make Yellow Color Candel 
                        mco = YellowCandel.fun(dataFrame = df) 

                        #Make a fibonacci lines
                        fabalines = FibonacciLines.fun (filePath_fun = filePathExcel)

                        #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                        setName = '\\' + tickerName + '_' + timeScope[indexScope] + '_' + indexTS.index4[index] + '_to_' + indexTS.index5[index]
                        save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                        #Make a chart
                        mpf.plot(data                   = df,
                                title                  = (tickerName + ' ' + timeScope[indexScope]), 
                                type                   = 'candle', 
                                #mav                    = (20,50),
                                volume                 = True,
                                show_nontrading        = False,
                                tight_layout           = True,
                                figratio               = (1,1),
                                figscale               = 3,
                                scale_padding          = 0.30,
                                figsize               = (12,6),
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
            ###___________________________________________________________________________________________________________________________                                                
                                
            if (flagIBKR):
                # start the Function:-

            #------------------------------------------------
                # Create File:        
                        # datetime object containing current date and time --- Help Link :- https://www.programiz.com/python-programming/datetime/current-datetime#google_vignette
                now = datetime.now()
                dt_string = now.strftime("[%Y%m%d_%H%M%S]") # YYmmdd_HHMMSS
                sessionSymbol =  "zzIBKR" + ' ' + str(dt_string)
                rxChartPath = CreateFile.fun(directory = sessionSymbol, parent_dir = filePathChart)

            #------------------------------------------------
                # Loop 1:-
                Fobi_Var = FibonacciLines.FiboClass()
                imgCount = 0
                daySheet = "IBKR 1Day"
                indexScope =  '5 secs'         
                timeScope = ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']      #   ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']
                bookScope = {
                            '1 secs' :{'SizeIndex': 0, 'DurationIndex':1, 'DurationLenth': 1, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 1s'     },
                            '5 secs' :{'SizeIndex': 1, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 5s'     },
                            '10 secs':{'SizeIndex': 2, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':30, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 10s'    },
                            '15 secs':{'SizeIndex': 3, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':20, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 15s'    },
                            '30 secs':{'SizeIndex': 4, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 30s'    },
                            '1 min'  :{'SizeIndex': 5, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':"IBKR 1m"     },
                            '2 mins' :{'SizeIndex': 6, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 2m'     },
                            '3 mins' :{'SizeIndex': 7, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 3m'     },
                            '5 mins' :{'SizeIndex': 8, 'DurationIndex':1, 'DurationLenth': 3, 'Rolling': 6, 'ChartDayDuration':  -1, 'indexTS': "5m", 'SheetName':'IBKR 5m'     },
                            '10 mins':{'SizeIndex': 9, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling': 6, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 10m'    },
                            '15 mins':{'SizeIndex':10, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 15m'    },
                            '20 mins':{'SizeIndex':11, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 20m'    },
                            '30 mins':{'SizeIndex':12, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':11, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 30m'    },
                            '1 hour' :{'SizeIndex':13, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':16, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 1H'     },
                            '2 hours':{'SizeIndex':14, 'DurationIndex':1, 'DurationLenth':34, 'Rolling': 8, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 2H'     },
                            '3 hours':{'SizeIndex':15, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':30, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 3H'     },
                            '4 hours':{'SizeIndex':16, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':20, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 4H'     },
                            '8 hours':{'SizeIndex':17, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':42, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 8H'     },
                            '1 day'  :{'SizeIndex':18, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':21, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Day'   },
                            '1W'     :{'SizeIndex':19, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1week'  },
                            '1M'     :{'SizeIndex':20, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Month' }
                            }

                for indexScope in timeScope:
                #------------------------------------------------
                    # Import  data
                    dft = ImportData.fun2 (filePath_fun = filePathExcel , bookName = bookScope[indexScope]['SheetName'])    #   'YAHOO'      'IBKR 30m'  IBKR 1H
                    if( len(dft.index) == 0 ):
                        print ( "This Sheet : ",bookScope[indexScope]['SheetName']," is Empty")
                    if( len(dft.index) > 0 ):
                        
                        TimeStamp_df =TS.fun5(   filePath           = filePathExcel
                                                ,timeStampPath      = r"D:\Python Tools\ChartMaker\SourceDocuments\InPut_Excel\Time_Stamp.xlsx"
                                                ,timeStampSheet     = "Ver1"
                                                ,DaySheetName       = daySheet 
                                                ,scope              = indexScope # ["5s","1m","5m","30m","1h","1d"]  
                                                ,scopeBook          = {
                                                                        "5s":"5s"
                                                                        ,'5 secs':"5s"
                                                                        ,"1m":"1m"
                                                                        ,'1 min':"1m"
                                                                        ,"5m":"5m"
                                                                        ,'5 mins':"5m"
                                                                        ,"30m":"30m"
                                                                        ,'30 mins':"30m"
                                                                        ,"1h":"1h"
                                                                        ,'1 hour':"1h"
                                                                        ,"1d":"1d" 
                                                                        ,'1 day':"1d" 
                                                                    }   
                                            )
                        

                    #------------------------------------------------
                        # Loop 2:-
                        
                        index = 0
                        for index in range(len(TimeStamp_df.Index1)):
                            
                            # Sampling data

                            df = dft[(TimeStamp_df.Index1[index]):(TimeStamp_df.Index2[index])]
                            if( len(df.index) == 0 ):
                                print (  "Ticker: ",tickerName,"  This Time Segment : " ,TimeStamp_df.Index1[index] ,":"  ,TimeStamp_df.Index2[index]   ," is Empty")
                            if( len(df.index) > 0 ):                           
                                print ( "Ticker: ",tickerName," in Time Segment : " ,TimeStamp_df.Index1[index] ,":"  ,TimeStamp_df.Index2[index]   ," is under Process")          
                                dfH = df.High.max()
                                dfL = df.Low.min()
                                dfD = (dfH - dfL) * 0.05 

                                # df = dft['2023-09-20 09:30:00':'2023-09-20 10:00:00']
                                # df = dft
                                # print (df)

                            #------------------------------------------------
                                #Make Indicator
                                EMA = addIndicator.fun4(dataFrame = df, scope = indexScope )    # need one for IBKR

                                #Make Yellow Color Candel 
                                mco = YellowCandel.fun(dataFrame = df) 
                                
                                #Make Time Lable
                                timeLable = TS.fTimeLable2  (  f_Scope        = TimeStamp_df.Scope[index] # (source=daySheet   ,interval=indexScope   ,inList=list (df.index.map(str)))
                                                            ,f_HourConstant = TimeStamp_df.HourConstant[index]
                                                            ,f_MinConstant  = TimeStamp_df.MinConstant[index]
                                                            ,f_SecConstant  = TimeStamp_df.SecConstant[index]
                                                            ,f_leftSide     = TimeStamp_df.leftSide[index]
                                                            ,source         = "IBKR"
                                                            ,interval       = indexScope
                                                            ,inList         = list (df.index.map(str))
                                                        )

                                #Make Price Label
                                priceLabel = TS.LabelPrice6 (    pMax = dfH + dfD
                                                                ,pMin = dfL - dfD
                                                            )

                                #Make a fibonacci lines
                                Fobi_Var = FibonacciLines.fun2 (     filePath_fun   = filePathExcel
                                                                    ,Fobi_Input     = Fobi_Var
                                                                    ,DaySheetName   = daySheet 
                                                                    ,fibonacciIndex = TimeStamp_df.Fibonacci[index]
                                                                    ,fibonacciBook  ={
                                                                                        "Last5Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-61	,	"EndDelta":	-1			},
                                                                                        "Last1Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-13	,	"EndDelta":	-1			},
                                                                                        "Last1Month"	:{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-31	,	"EndDelta":	-2			},
                                                                                        "Last1Week"	    :{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-6	,	"EndDelta":	-2			},
                                                                                        "Yesterday"	    :{	'SheetName':	'IBKR 4H'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                                                                        "PreMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"06:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                                                                        "PreMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"06:00:00"	,	"PeriodEnd":	"08:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"06:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "MarketOpen"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"09:00:00"	,	"PeriodEnd":	"10:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"09:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Midday"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"10:00:00"	,	"PeriodEnd":	"14:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"10:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "PowerHour"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"14:00:00"	,	"PeriodEnd":	"16:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"14:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "AfterMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"16:00:00"	,	"PeriodEnd":	"18:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"16:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "AfterMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"18:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"18:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Final"	        :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"20:00:00"	,	"PeriodEnd":	"00:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random1"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random2"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random3"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random4"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random5"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			}
                                                                                    }
                                                                )

                                #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                setName = '\\' + tickerName + '_' + str("%03d"%imgCount) + '_'  + indexScope + '_' + TimeStamp_df.Name[index] 
                                save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                                #Make a chart
                                fig, axlist = mpf.plot(  data                   = df
                                                        ,title                  = (tickerName + ' ' + indexScope)
                                                        ,type                   = 'candle' 
                                                        # ,mav                    = (20,50)
                                                        ,volume                 = True
                                                        ,show_nontrading        = False
                                                        ,tight_layout           = True
                                                        ,figratio               = (1,1)
                                                        ,figscale               = 3
                                                        ,scale_padding          = 0.30
                                                        ,figsize               = (12,6)
                                                        # ,ylim                   = (((df.Low.min())*0.95) ,((df.High.max())*1.05)) # set min and max of Chart
                                                        ,ylim                   = ((dfL - dfD) ,(dfH + dfD)) # set min and max of Chart (dfH + dfD)
                                                        ,xrotation              = 0
                                                        ,yscale                 = "linear" # y-axis scale: "linear", "log", "symlog", or "logit"
                                                        ,volume_yscale          = "linear" # Volume y-axis scale: "linear", "log", "symlog", or "logit"
                                                        ,style                  = EhabStaylo
                                                        ,marketcolor_overrides  = mco
                                                        ,mco_faceonly           = False
                                                        ,addplot                = EMA
                                                        ,hlines                 = Fobi_Var.fibolines
                                                        ,returnfig=True
                                                        # ,savefig                = save # link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                                        # ,marketcolor_overrides = mco  # link https://github.com/matplotlib/mplfinance/blob/master/examples/marketcolor_overrides.ipynb
                                )
                                
                                #Add Time Lable      Help link:   https://github.com/matplotlib/mplfinance/issues/573
                                axlist[-2].set_xticks(timeLable["ticks"])
                                axlist[-2].set_xticklabels(timeLable["tlabs"], ha='center')
                                axlist[-2].set_xticks(timeLable["mitks"],minor=True)
                                axlist[-2].set_xticklabels(timeLable["milab"], ha='center', minor=True, rotation=0) 

                                x2 = axlist[0].secondary_xaxis('top')       # Help Link :-  https://matplotlib.org/stable/gallery/ticks/multilevel_ticks.html#sphx-glr-gallery-ticks-multilevel-ticks-py
                                x2.set_xticks(timeLable["ticks"])           # Help Link :-  https://matplotlib.org/stable/api/axes_api.html
                                x2.set_xticklabels(timeLable["Utlabs"], ha='center')
                                x2.set_xticks(timeLable["mitks"],minor=True)
                                x2.set_xticklabels(timeLable["Umilab"], ha='center', minor=True, rotation=0)
                                
                                #Add Price Lable     Help Link:-   https://github.com/matplotlib/mplfinance/issues/604 
                                axlist[0].set_yticks( priceLabel['ticks'] )
                                axlist[0].set_yticklabels( priceLabel['tlabs'] )
                                                
                                y2 = axlist[0].secondary_yaxis('left')      # Help Link :-  https://github.com/matplotlib/mplfinance/issues/587
                                y2.set_yticks(priceLabel['ticks'])
                                y2.set_yticklabels( priceLabel['tlabs'] )
                                
                                #Saving Chart        Help link:   https://github.com/matplotlib/mplfinance/issues/573
                                fig.savefig( fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0, bbox_inches='tight' )
                                imgCount += 1

                                # mpf.show()
                                # matplotlib.pyplot.savefig()
                                # fig.save()
                                
                                # axlist[-2].save()
                                # fig.savefig( 'myplot.pdf', bbox_inches='tight' )
###_____________________________________________________________________________________________________________________________________________________________________________________
def fun7(   # Set Varibles
            #------------------------------------------------
                tickerName = 'AAPL',     
                filePathExcel = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\Session [20230921_221745]\AAPL\OK AAPL.xlsx",
                filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg',            #C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
                flagYahoo = True,
                flagIBKR = True,
                imageType= '.png'
        ):
            ###___________________________________________________________________________________________________________________________
            if (flagYahoo):
                # start the Function:-
                rxChartPath = CreateFile.fun(directory = "Yahoo", parent_dir = filePathChart)

                # Loop 1:-
                daySheet = "Yahoo Dayes"
                indexScope = 0
                bookScope = ["Yahoo 1m","Yahoo 5m","Yahoo 30m","Yahoo Hours","Yahoo Dayes"]
                timeScope = ["1m","5m","30m","1h","1d"] 

                for indexScope in range(len(bookScope)):
                    # Import  data
                    dft = ImportData.fun (filePath_fun = filePathExcel , bookName = bookScope[indexScope])
                    indexTS =TS.fun2(filePath=filePathExcel, bookScope=daySheet, scope=timeScope[indexScope])

                    # Loop 2:-
                    index = 0
                    for index in range(len(indexTS.index1)):
                        # Sampling data
                        df = dft[(indexTS.index1[index]):(indexTS.index2[index])]

                        #Make Indicator
                        EMA = addIndicator.fun(dataFrame = df, scope = timeScope[indexScope] )

                        #Make Yellow Color Candel 
                        mco = YellowCandel.fun(dataFrame = df) 

                        #Make a fibonacci lines
                        fabalines = FibonacciLines.fun (filePath_fun = filePathExcel)

                        #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                        setName = '\\' + tickerName + '_' + timeScope[indexScope] + '_' + indexTS.index4[index] + '_to_' + indexTS.index5[index]
                        save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                        #Make a chart
                        mpf.plot(data                   = df,
                                title                  = (tickerName + ' ' + timeScope[indexScope]), 
                                type                   = 'candle', 
                                #mav                    = (20,50),
                                volume                 = True,
                                show_nontrading        = False,
                                tight_layout           = True,
                                figratio               = (1,1),
                                figscale               = 3,
                                scale_padding          = 0.30,
                                figsize               = (12,6),
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
            ###___________________________________________________________________________________________________________________________                                                
                        
            if (flagIBKR):
                # start the Function:-

            #------------------------------------------------
                # Create File:        
                        # datetime object containing current date and time --- Help Link :- https://www.programiz.com/python-programming/datetime/current-datetime#google_vignette
                now = datetime.now()
                dt_string = now.strftime("[%Y%m%d_%H%M%S]") # YYmmdd_HHMMSS
                sessionSymbol =  "zzIBKR" + ' ' + str(dt_string)
                rxChartPath = CreateFile.fun(directory = sessionSymbol, parent_dir = filePathChart)

            #------------------------------------------------
                # Loop 1:-
                Fobi_Var = FibonacciLines.FiboClass()
                imgCount = 0
                daySheet = "IBKR 1Day"
                indexScope =  '5 secs'         
                timeScope = ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']      #   ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']
                bookScope = {
                            '1 secs' :{'SizeIndex': 0, 'DurationIndex':1, 'DurationLenth': 1, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 1s'     },
                            '5 secs' :{'SizeIndex': 1, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 5s'     },
                            '10 secs':{'SizeIndex': 2, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':30, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 10s'    },
                            '15 secs':{'SizeIndex': 3, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':20, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 15s'    },
                            '30 secs':{'SizeIndex': 4, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 30s'    },
                            '1 min'  :{'SizeIndex': 5, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':"IBKR 1m"     },
                            '2 mins' :{'SizeIndex': 6, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 2m'     },
                            '3 mins' :{'SizeIndex': 7, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 3m'     },
                            '5 mins' :{'SizeIndex': 8, 'DurationIndex':1, 'DurationLenth': 3, 'Rolling': 6, 'ChartDayDuration':  -1, 'indexTS': "5m", 'SheetName':'IBKR 5m'     },
                            '10 mins':{'SizeIndex': 9, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling': 6, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 10m'    },
                            '15 mins':{'SizeIndex':10, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 15m'    },
                            '20 mins':{'SizeIndex':11, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 20m'    },
                            '30 mins':{'SizeIndex':12, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':11, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 30m'    },
                            '1 hour' :{'SizeIndex':13, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':16, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 1H'     },
                            '2 hours':{'SizeIndex':14, 'DurationIndex':1, 'DurationLenth':34, 'Rolling': 8, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 2H'     },
                            '3 hours':{'SizeIndex':15, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':30, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 3H'     },
                            '4 hours':{'SizeIndex':16, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':20, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 4H'     },
                            '8 hours':{'SizeIndex':17, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':42, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 8H'     },
                            '1 day'  :{'SizeIndex':18, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':21, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Day'   },
                            '1W'     :{'SizeIndex':19, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1week'  },
                            '1M'     :{'SizeIndex':20, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Month' }
                            }

                for indexScope in timeScope:
                #------------------------------------------------
                    # Import  data
                    dft = ImportData.fun2 (filePath_fun = filePathExcel , bookName = bookScope[indexScope]['SheetName'])    #   'YAHOO'      'IBKR 30m'  IBKR 1H
                    if( len(dft.index) == 0 ):
                        print ( "This Sheet : ",bookScope[indexScope]['SheetName']," is Empty")
                    if( len(dft.index) > 0 ):
                        # Replace NaN Values with Zeros in Pandas DataFrame     Help Link :- https://www.geeksforgeeks.org/replace-nan-values-with-zeros-in-pandas-dataframe/
                        dft = dft.fillna(0)
                        TimeStamp_df =TS.fun6(   filePath           = filePathExcel
                                                ,timeStampPath      = r"D:\Python Tools\ChartMaker\SourceDocuments\InPut_Excel\Time_Stamp.xlsx"
                                                ,timeStampSheet     = "Ver1"
                                                ,DaySheetName       = daySheet 
                                                ,scope              = indexScope # ["5s","1m","5m","30m","1h","1d"]  
                                                ,scopeBook          = {
                                                                        "5s":"5s"
                                                                        ,'5 secs':"5s"
                                                                        ,"1m":"1m"
                                                                        ,'1 min':"1m"
                                                                        ,"5m":"5m"
                                                                        ,'5 mins':"5m"
                                                                        ,"30m":"30m"
                                                                        ,'30 mins':"30m"
                                                                        ,"1h":"1h"
                                                                        ,'1 hour':"1h"
                                                                        ,"1d":"1d" 
                                                                        ,'1 day':"1d" 
                                                                    }   
                                            )
                        

                    #------------------------------------------------
                        # Loop 2:-
                        
                        index = 0
                        for index in range(len(TimeStamp_df.Index1)):
                            
                            # Sampling data

                            df = dft[(TimeStamp_df.Index1[index]):(TimeStamp_df.Index2[index])]
                            if( len(df.index) == 0 ):
                                print (  "Ticker: ",tickerName,"  This Time Segment : " ,TimeStamp_df.Index1[index] ,":"  ,TimeStamp_df.Index2[index]   ," is Empty")
                            if( len(df.index) > 0 ):                           
                                        
                                dfH = df.High.max()
                                dfL = df.Low.min()
                                dfD = (dfH - dfL) * 0.05 

                                # df = dft['2023-09-20 09:30:00':'2023-09-20 10:00:00']
                                # df = dft
                                # print (df)

                            #------------------------------------------------
                                #Make Indicator
                                EMA = addIndicator.fun4(dataFrame = df, scope = indexScope )    # need one for IBKR

                                #Make Yellow Color Candel 
                                mco = YellowCandel.fun(dataFrame = df) 
                                
                                print ( "###############################################")
                                print ( "#######","Ticker: ",tickerName,"#######")
                                print (" in Time Segment : " ,TimeStamp_df.Index1[index] ,":"  ,TimeStamp_df.Index2[index]   ," is under Process")
                                print ( "###############################################")

                                #Make Time Lable
                                timeLable = TS.fTimeLable2  (  f_Scope        = TimeStamp_df.Scope[index] # (source=daySheet   ,interval=indexScope   ,inList=list (df.index.map(str)))
                                                            ,f_HourConstant = TimeStamp_df.HourConstant[index]
                                                            ,f_MinConstant  = TimeStamp_df.MinConstant[index]
                                                            ,f_SecConstant  = TimeStamp_df.SecConstant[index]
                                                            ,f_leftSide     = TimeStamp_df.leftSide[index]
                                                            ,source         = "IBKR"
                                                            ,interval       = indexScope
                                                            ,inList         = list (df.index.map(str))
                                                        )

                                #Make Price Label
                                priceLabel = TS.LabelPrice6 (    pMax = dfH + dfD
                                                                ,pMin = dfL - dfD
                                                            )

                                #Make a fibonacci lines
                                Fobi_Var = FibonacciLines.fun2 (     filePath_fun   = filePathExcel
                                                                    ,Fobi_Input     = Fobi_Var
                                                                    ,DaySheetName   = daySheet 
                                                                    ,fibonacciIndex = TimeStamp_df.Fibonacci[index]
                                                                    ,fibonacciBook  ={
                                                                                        "Last5Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-61	,	"EndDelta":	-1			},
                                                                                        "Last1Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-13	,	"EndDelta":	-1			},
                                                                                        "Last1Month"	:{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-31	,	"EndDelta":	-2			},
                                                                                        "Last1Week"	    :{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-6	,	"EndDelta":	-2			},
                                                                                        "Yesterday"	    :{	'SheetName':	'IBKR 4H'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                                                                        "PreMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"06:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                                                                        "PreMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"06:00:00"	,	"PeriodEnd":	"08:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"06:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "MarketOpen"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"09:00:00"	,	"PeriodEnd":	"10:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"09:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Midday"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"10:00:00"	,	"PeriodEnd":	"14:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"10:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "PowerHour"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"14:00:00"	,	"PeriodEnd":	"16:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"14:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "AfterMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"16:00:00"	,	"PeriodEnd":	"18:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"16:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "AfterMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"18:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"18:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Final"	        :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"20:00:00"	,	"PeriodEnd":	"00:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random1"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random2"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random3"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random4"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random5"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			}
                                                                                    }
                                                                )

                                #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                setName = '\\' + tickerName + '_' + str("%03d"%imgCount) + '_'  + indexScope + '_' + TimeStamp_df.Name[index] 
                                save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                                #Make a chart
                                fig, axlist = mpf.plot(  data                   = df
                                                        ,title                  = (tickerName + ' ' + indexScope)
                                                        ,type                   = 'candle' 
                                                        # ,mav                    = (20,50)
                                                        ,volume                 = True
                                                        ,show_nontrading        = False
                                                        ,tight_layout           = True
                                                        ,figratio               = (1,1)
                                                        ,figscale               = 3
                                                        ,scale_padding          = 0.30
                                                        ,figsize               = (12,6)
                                                        # ,ylim                   = (((df.Low.min())*0.95) ,((df.High.max())*1.05)) # set min and max of Chart
                                                        ,ylim                   = ((dfL - dfD) ,(dfH + dfD)) # set min and max of Chart (dfH + dfD)
                                                        ,xrotation              = 0
                                                        ,yscale                 = "linear" # y-axis scale: "linear", "log", "symlog", or "logit"
                                                        ,volume_yscale          = "linear" # Volume y-axis scale: "linear", "log", "symlog", or "logit"
                                                        ,style                  = EhabStaylo
                                                        ,marketcolor_overrides  = mco
                                                        ,mco_faceonly           = False
                                                        ,addplot                = EMA
                                                        ,hlines                 = Fobi_Var.fibolines
                                                        ,returnfig=True
                                                        # ,savefig                = save # link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                                        # ,marketcolor_overrides = mco  # link https://github.com/matplotlib/mplfinance/blob/master/examples/marketcolor_overrides.ipynb
                                )
                                
                                #Add Time Lable      Help link:   https://github.com/matplotlib/mplfinance/issues/573
                                axlist[-2].set_xticks(timeLable["ticks"])
                                axlist[-2].set_xticklabels(timeLable["tlabs"], ha='center')
                                axlist[-2].set_xticks(timeLable["mitks"],minor=True)
                                axlist[-2].set_xticklabels(timeLable["milab"], ha='center', minor=True, rotation=0) 

                                x2 = axlist[0].secondary_xaxis('top')       # Help Link :-  https://matplotlib.org/stable/gallery/ticks/multilevel_ticks.html#sphx-glr-gallery-ticks-multilevel-ticks-py
                                x2.set_xticks(timeLable["ticks"])           # Help Link :-  https://matplotlib.org/stable/api/axes_api.html
                                x2.set_xticklabels(timeLable["Utlabs"], ha='center')
                                x2.set_xticks(timeLable["mitks"],minor=True)
                                x2.set_xticklabels(timeLable["Umilab"], ha='center', minor=True, rotation=0)
                                
                                #Add Price Lable     Help Link:-   https://github.com/matplotlib/mplfinance/issues/604 
                                axlist[0].set_yticks( priceLabel['ticks'] )
                                axlist[0].set_yticklabels( priceLabel['tlabs'] )
                                                
                                y2 = axlist[0].secondary_yaxis('left')      # Help Link :-  https://github.com/matplotlib/mplfinance/issues/587
                                y2.set_yticks(priceLabel['ticks'])
                                y2.set_yticklabels( priceLabel['tlabs'] )
                                
                                #Saving Chart        Help link:   https://github.com/matplotlib/mplfinance/issues/573
                                fig.savefig( fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0, bbox_inches='tight' )
                                imgCount += 1

                                # mpf.show()
                                # matplotlib.pyplot.savefig()
                                # fig.save()
                                
                                # axlist[-2].save()
                                # fig.savefig( 'myplot.pdf', bbox_inches='tight' )           
###_____________________________________________________________________________________________________________________________________________________________________________________
def fun8(   # Set Varibles
            #------------------------------------------------
                 tickerName = 'AAPL'                    
                ,filePathExcel = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\Session [20230921_221745]\AAPL\OK AAPL.xlsx"
                ,filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg'            #C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
                
                ,filePathWL = r"D:\Python Tools\ChartMaker\SourceDocuments\InPut_Excel\Watch_List_Zamzam .xlsx"
                ,timeStampSheet = "Sheet2"
                
                ,flagYahoo = False
                ,flagIBKR = True
                ,imageType= '.png'
        ):
            ###___________________________________________________________________________________________________________________________
            if (flagYahoo):
                # start the Function:-
                rxChartPath = CreateFile.fun(directory = "Yahoo", parent_dir = filePathChart)

                # Loop 1:-
                daySheet = "Yahoo Dayes"
                indexScope = 0
                bookScope = ["Yahoo 1m","Yahoo 5m","Yahoo 30m","Yahoo Hours","Yahoo Dayes"]
                timeScope = ["1m","5m","30m","1h","1d"] 

                for indexScope in range(len(bookScope)):
                    # Import  data
                    dft = ImportData.fun (filePath_fun = filePathExcel , bookName = bookScope[indexScope])
                    indexTS =TS.fun2(filePath=filePathExcel, bookScope=daySheet, scope=timeScope[indexScope])

                    # Loop 2:-
                    index = 0
                    for index in range(len(indexTS.index1)):
                        # Sampling data
                        df = dft[(indexTS.index1[index]):(indexTS.index2[index])]

                        #Make Indicator
                        EMA = addIndicator.fun(dataFrame = df, scope = timeScope[indexScope] )

                        #Make Yellow Color Candel 
                        mco = YellowCandel.fun(dataFrame = df) 

                        #Make a fibonacci lines
                        fabalines = FibonacciLines.fun (filePath_fun = filePathExcel)

                        #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                        setName = '\\' + tickerName + '_' + timeScope[indexScope] + '_' + indexTS.index4[index] + '_to_' + indexTS.index5[index]
                        save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                        #Make a chart
                        mpf.plot(data                   = df,
                                title                  = (tickerName + ' ' + timeScope[indexScope]), 
                                type                   = 'candle', 
                                #mav                    = (20,50),
                                volume                 = True,
                                show_nontrading        = False,
                                tight_layout           = True,
                                figratio               = (1,1),
                                figscale               = 3,
                                scale_padding          = 0.30,
                                figsize               = (12,6),
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
            ###___________________________________________________________________________________________________________________________                                                
                        
            if (flagIBKR):
                # start the Function:-

            #------------------------------------------------
                # Create File:        
                        # datetime object containing current date and time --- Help Link :- https://www.programiz.com/python-programming/datetime/current-datetime#google_vignette
                now = datetime.now()
                dt_string = now.strftime("[%Y%m%d_%H%M%S]") # YYmmdd_HHMMSS
                sessionSymbol =  "zzIBKR" + ' ' + str(dt_string)
                rxChartPath = CreateFile.fun(directory = sessionSymbol, parent_dir = filePathChart)

            #------------------------------------------------
                # Loop 1:-
                Fobi_Var        = FibonacciLines.FiboClass()
                imgCount        = 0
                daySheet        = "IBKR 1Day"
                indexScope      =  '5 secs'         
                timeScope       = ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']      #   ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']
                bookScope       = {
                                    '1 secs' :{'SizeIndex': 0, 'DurationIndex':1, 'DurationLenth': 1, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 1s'     },
                                    '5 secs' :{'SizeIndex': 1, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 5s'     },
                                    '10 secs':{'SizeIndex': 2, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':30, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 10s'    },
                                    '15 secs':{'SizeIndex': 3, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':20, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 15s'    },
                                    '30 secs':{'SizeIndex': 4, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 30s'    },
                                    '1 min'  :{'SizeIndex': 5, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':"IBKR 1m"     },
                                    '2 mins' :{'SizeIndex': 6, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 2m'     },
                                    '3 mins' :{'SizeIndex': 7, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 3m'     },
                                    '5 mins' :{'SizeIndex': 8, 'DurationIndex':1, 'DurationLenth': 3, 'Rolling': 6, 'ChartDayDuration':  -1, 'indexTS': "5m", 'SheetName':'IBKR 5m'     },
                                    '10 mins':{'SizeIndex': 9, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling': 6, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 10m'    },
                                    '15 mins':{'SizeIndex':10, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 15m'    },
                                    '20 mins':{'SizeIndex':11, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 20m'    },
                                    '30 mins':{'SizeIndex':12, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':11, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 30m'    },
                                    '1 hour' :{'SizeIndex':13, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':16, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 1H'     },
                                    '2 hours':{'SizeIndex':14, 'DurationIndex':1, 'DurationLenth':34, 'Rolling': 8, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 2H'     },
                                    '3 hours':{'SizeIndex':15, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':30, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 3H'     },
                                    '4 hours':{'SizeIndex':16, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':20, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 4H'     },
                                    '8 hours':{'SizeIndex':17, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':42, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 8H'     },
                                    '1 day'  :{'SizeIndex':18, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':21, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Day'   },
                                    '1W'     :{'SizeIndex':19, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1week'  },
                                    '1M'     :{'SizeIndex':20, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Month' }
                                    }

                dfTimeStamp     = TS.fGetTimeStampDataFrame(    
                                                            timeStampPath      = filePathWL
                                                            ,timeStampSheet     = timeStampSheet                 
                                                            )
                ChartStyle      = TS.fGetStyle(                 
                                                dfTimeStamp
                                                ,AttributeIndex=0
                                                ,AttributeList =[
                                                                "style_name"
                                                                ,"base_mpl_style"
                                                                ,"marketcolors"
                                                                ,"candle_Up"
                                                                ,"candle_Down"
                                                                ,"edge_Up"
                                                                ,"edge_Down"
                                                                ,"wick_Up"
                                                                ,"wick_Down"
                                                                ,"ohlc_Up"
                                                                ,"ohlc_Down"
                                                                ,"volume_Up"
                                                                ,"volume_Down"
                                                                ,"vcdopcod"
                                                                ,"alpha"
                                                                ,"mavcolors"
                                                                ,"y_on_right"
                                                                ,"gridcolor"
                                                                ,"gridstyle"
                                                                ,"facecolor"
                                                                ,"figcolor"
                                                                ,"rc"
                                                                ,"axes.edgecolor"
                                                                ,"axes.linewidth"
                                                                ,"axes.labelsize"
                                                                ,"axes.labelweight"
                                                                ,"axes.grid"
                                                                ,"axes.grid.axis"
                                                                ,"axes.grid.which"
                                                                ,"grid.alpha"
                                                                ,"grid.color"
                                                                ,"grid.linestyle"
                                                                ,"grid.linewidth"
                                                                ,"figure.facecolor"
                                                                ,"patch.linewidth"
                                                                ,"lines.linewidth"
                                                                ,"font.weight"
                                                                ,"font.size"
                                                                ,"figure.titlesize"
                                                                ,"figure.titleweight"
                                                                ,"base_mpf_style"]
                                                ,AttributeDic = {
                                                                "style_name"           :	"Ehab_Staylo"
                                                                ,"base_mpl_style"       :	"dark_background"
                                                                ,"marketcolors"         :	"marketcolors"
                                                                ,"candle_Up"            :	"#14CE1C"
                                                                ,"candle_Down"          :	"#CE1414"
                                                                ,"edge_Up"              :	"#14CE1C"
                                                                ,"edge_Down"            :	"#CE1414"
                                                                ,"wick_Up"              :	"#ffffff"
                                                                ,"wick_Down"            :	"#ffffff"
                                                                ,"ohlc_Up"              :	"#ffffff"
                                                                ,"ohlc_Down"            :	"#ffffff"
                                                                ,"volume_Up"            :	"#14CE1C"
                                                                ,"volume_Down"          :	"#CE1414"
                                                                ,"vcdopcod"             :	 False	
                                                                ,"alpha"                :	 2.00	
                                                                ,"mavcolors"            :	 ['#ec009c','#78ff8f','#fcf120']	
                                                                ,"y_on_right"           :	 True	
                                                                ,"gridcolor"            :	 None	
                                                                ,"gridstyle"            :	 None	
                                                                ,"facecolor"            :	"Black"
                                                                ,"figcolor"             :	"gray"
                                                                ,"rc"                   :	"rc"
                                                                ,"axes.edgecolor"       :	"white"
                                                                ,"axes.linewidth"       :	 1.50	
                                                                ,"axes.labelsize"       :	"large"
                                                                ,"axes.labelweight"     :	"semibold"
                                                                ,"axes.grid"            :	 True	
                                                                ,"axes.grid.axis"       :	"both"
                                                                ,"axes.grid.which"      :	"major"
                                                                ,"grid.alpha"           :	 0.90	
                                                                ,"grid.color"           :	"#EBEE24"
                                                                ,"grid.linestyle"       :	":"	
                                                                ,"grid.linewidth"       :	 1.00	
                                                                ,"figure.facecolor"     :	"#0a0a0a"
                                                                ,"patch.linewidth"      :	 1.00	
                                                                ,"lines.linewidth"      :	 1.00	
                                                                ,"font.weight"          :	"medium"
                                                                ,"font.size"            :	 8.00	
                                                                ,"figure.titlesize"     :	"x-large"
                                                                ,"figure.titleweight"   :	"semibold"
                                                                ,"base_mpf_style"       :	"mike"
                                                                }
                                                )
                dfDay           = TS.fGetDayDataFrame(    
                                                        filePath           = filePathExcel      #r"C:\Users\lenovo\Desktop\TGL\BCG\OK BCG.xlsx"            
                                                        ,DaySheetName       = daySheet                   
                                                    )



                for indexScope in timeScope:
                #------------------------------------------------
                    # Import  data
                    dft = ImportData.fun2 (filePath_fun = filePathExcel , bookName = bookScope[indexScope]['SheetName'])    #   'YAHOO'      'IBKR 30m'  IBKR 1H
                    if( len(dft.index) == 0 ):
                        print ( "This Sheet : ",bookScope[indexScope]['SheetName']," is Empty")
                    if( len(dft.index) > 0 ):
                        # Replace NaN Values with Zeros in Pandas DataFrame     Help Link :- https://www.geeksforgeeks.org/replace-nan-values-with-zeros-in-pandas-dataframe/
                        dft = dft.fillna(0)
                        TimeStamp_df =TS.fun7(   dfD                = dfDay
                                                ,dfS                = dfTimeStamp 
                                                ,scope              = indexScope # ["5s","1m","5m","30m","1h","1d"]  
                                                ,scopeBook          = {
                                                                        "5s":"5s"
                                                                        ,'5 secs':"5s"
                                                                        ,"1m":"1m"
                                                                        ,'1 min':"1m"
                                                                        ,"5m":"5m"
                                                                        ,'5 mins':"5m"
                                                                        ,"30m":"30m"
                                                                        ,'30 mins':"30m"
                                                                        ,"1h":"1h"
                                                                        ,'1 hour':"1h"
                                                                        ,"1d":"1d" 
                                                                        ,'1 day':"1d" 
                                                                    }   
                                            )
                        

                    #------------------------------------------------
                        # Loop 2:-
                        
                        index = 0
                        for index in range(len(TimeStamp_df.Index1)):
                            
                            # Sampling data

                            df = dft[(TimeStamp_df.Index1[index]):(TimeStamp_df.Index2[index])]
                            if( len(df.index) == 0 ):   # Skip Empty Segment.
                                print (  "Ticker: ",tickerName,"  This Time Segment : " ,TimeStamp_df.Index1[index] ,":"  ,TimeStamp_df.Index2[index]   ," is Empty")
                            if( len(df.index) > 0 ):  
                                print ( "###############################################")
                                print ( "#######","Ticker: ",tickerName,"#######")
                                print (" in Time Segment : " ,TimeStamp_df.Index1[index] ,":"  ,TimeStamp_df.Index2[index]   ," is under Process")
                                print ( "###############################################")                         
                                        
                                dfH = df.High.max()
                                dfL = df.Low.min()
                                dfD = (dfH - dfL) * 0.05 

                                # df = dft['2023-09-20 09:30:00':'2023-09-20 10:00:00']
                                # df = dft
                                # print (df)

                            #------------------------------------------------
                                #Make Chart Style
                                
                                #Make Yellow Color Candel 
                                mco = YellowCandel.fun(dataFrame = df) 
                                
                                #Make Indicator
                                EMA = addIndicator.fun4(dataFrame = df, scope = indexScope )    # need one for IBKR

                                #Make a fibonacci lines
                                Fobi_Var = FibonacciLines.fun2 (     filePath_fun   = filePathExcel
                                                                    ,Fobi_Input     = Fobi_Var
                                                                    ,DaySheetName   = daySheet 
                                                                    ,fibonacciIndex = TimeStamp_df.Fibonacci[index]
                                                                    ,fibonacciBook  ={
                                                                                        "Last5Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-61	,	"EndDelta":	-1			},
                                                                                        "Last1Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-13	,	"EndDelta":	-1			},
                                                                                        "Last1Month"	:{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-31	,	"EndDelta":	-2			},
                                                                                        "Last1Week"	    :{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-6	,	"EndDelta":	-2			},
                                                                                        "Yesterday"	    :{	'SheetName':	'IBKR 4H'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                                                                        "PreMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"06:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                                                                        "PreMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"06:00:00"	,	"PeriodEnd":	"08:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"06:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "MarketOpen"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"09:00:00"	,	"PeriodEnd":	"10:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"09:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Midday"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"10:00:00"	,	"PeriodEnd":	"14:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"10:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "PowerHour"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"14:00:00"	,	"PeriodEnd":	"16:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"14:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "AfterMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"16:00:00"	,	"PeriodEnd":	"18:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"16:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "AfterMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"18:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"18:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Final"	        :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"20:00:00"	,	"PeriodEnd":	"00:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random1"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random2"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random3"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random4"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                                                                        "Random5"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			}
                                                                                    }
                                                                )

                                
                                

                                #Make Time Lable
                                timeLable = TS.fTimeLable2  (  f_Scope        = TimeStamp_df.Scope[index] # (source=daySheet   ,interval=indexScope   ,inList=list (df.index.map(str)))
                                                            ,f_HourConstant = TimeStamp_df.HourConstant[index]
                                                            ,f_MinConstant  = TimeStamp_df.MinConstant[index]
                                                            ,f_SecConstant  = TimeStamp_df.SecConstant[index]
                                                            ,f_leftSide     = TimeStamp_df.leftSide[index]
                                                            ,source         = "IBKR"
                                                            ,interval       = indexScope
                                                            ,inList         = list (df.index.map(str))
                                                        )

                                #Make Price Label
                                priceLabel = TS.LabelPrice6 (    pMax = dfH + dfD
                                                                ,pMin = dfL - dfD
                                                            )

                                
                                # #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                # setName = '\\' + tickerName + '_' + str("%03d"%imgCount) + '_'  + indexScope + '_' + TimeStamp_df.Name[index] 
                                # save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                                #Make a chart
                                fig, axlist = mpf.plot(  data                   = df
                                                        ,title                  = (tickerName + ' ' + indexScope)
                                                        ,type                   = 'candle' 
                                                        # ,mav                    = (20,50)
                                                        ,volume                 = True
                                                        ,show_nontrading        = False
                                                        ,tight_layout           = True
                                                        ,figratio               = (1,1)
                                                        ,figscale               = 3
                                                        ,scale_padding          = 0.30
                                                        ,figsize               = (12,6)
                                                        # ,ylim                   = (((df.Low.min())*0.95) ,((df.High.max())*1.05)) # set min and max of Chart
                                                        ,ylim                   = ((dfL - dfD) ,(dfH + dfD)) # set min and max of Chart (dfH + dfD)
                                                        ,xrotation              = 0
                                                        ,yscale                 = "linear" # y-axis scale: "linear", "log", "symlog", or "logit"
                                                        ,volume_yscale          = "linear" # Volume y-axis scale: "linear", "log", "symlog", or "logit"
                                                        ,style                  = ChartStyle
                                                        ,marketcolor_overrides  = mco
                                                        ,mco_faceonly           = False
                                                        ,addplot                = EMA
                                                        ,hlines                 = Fobi_Var.fibolines
                                                        ,returnfig=True
                                                        # ,savefig                = save # link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                                        # ,marketcolor_overrides = mco  # link https://github.com/matplotlib/mplfinance/blob/master/examples/marketcolor_overrides.ipynb
                                )
                                
                                #Add Time Lable      Help link:   https://github.com/matplotlib/mplfinance/issues/573
                                axlist[-2].set_xticks(timeLable["ticks"])
                                axlist[-2].set_xticklabels(timeLable["tlabs"], ha='center')
                                axlist[-2].set_xticks(timeLable["mitks"],minor=True)
                                axlist[-2].set_xticklabels(timeLable["milab"], ha='center', minor=True, rotation=0) 

                                x2 = axlist[0].secondary_xaxis('top')       # Help Link :-  https://matplotlib.org/stable/gallery/ticks/multilevel_ticks.html#sphx-glr-gallery-ticks-multilevel-ticks-py
                                x2.set_xticks(timeLable["ticks"])           # Help Link :-  https://matplotlib.org/stable/api/axes_api.html
                                x2.set_xticklabels(timeLable["Utlabs"], ha='center')
                                x2.set_xticks(timeLable["mitks"],minor=True)
                                x2.set_xticklabels(timeLable["Umilab"], ha='center', minor=True, rotation=0)
                                
                                #Add Price Lable     Help Link:-   https://github.com/matplotlib/mplfinance/issues/604 
                                axlist[0].set_yticks( priceLabel['ticks'] )
                                axlist[0].set_yticklabels( priceLabel['tlabs'] )
                                                
                                y2 = axlist[0].secondary_yaxis('left')      # Help Link :-  https://github.com/matplotlib/mplfinance/issues/587
                                y2.set_yticks(priceLabel['ticks'])
                                y2.set_yticklabels( priceLabel['tlabs'] )
                                
                                
                                #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                setName = '\\' + tickerName + '_' + str("%03d"%imgCount) + '_'  + indexScope + '_' + TimeStamp_df.Name[index] 
                                save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)
                                
                                
                                #Saving Chart        Help link:   https://github.com/matplotlib/mplfinance/issues/573
                                fig.savefig( fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0, bbox_inches='tight' )
                                imgCount += 1

                                # mpf.show()
                                # matplotlib.pyplot.savefig()
                                # fig.save()
                                
                                # axlist[-2].save()
                                # fig.savefig( 'myplot.pdf', bbox_inches='tight' )           
###_____________________________________________________________________________________________________________________________________________________________________________________
def fun9(   # Set Varibles
            #------------------------------------------------
                 tickerName = 'AAPL'                    
                ,filePathExcel = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\Session [20231128_111940]\GME\OK GME.xlsx"
                ,filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg'            #C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
                
                ,filePathWL = r"D:\Python Tools\ChartMaker\SourceDocuments\InPut_Excel\Watch_List_Zamzam .xlsx"
                ,timeStampSheet = "Zamzam"
                
                ,flagYahoo = False
                ,flagIBKR = True
                ,imageType= '.png'
        ):
            ###___________________________________________________________________________________________________________________________
            if (flagYahoo):
                # start the Function:-
                rxChartPath = CreateFile.fun(directory = "Yahoo", parent_dir = filePathChart)

                # Loop 1:-
                daySheet = "Yahoo Dayes"
                indexScope = 0
                bookScope = ["Yahoo 1m","Yahoo 5m","Yahoo 30m","Yahoo Hours","Yahoo Dayes"]
                timeScope = ["1m","5m","30m","1h","1d"] 

                for indexScope in range(len(bookScope)):
                    # Import  data
                    dft = ImportData.fun (filePath_fun = filePathExcel , bookName = bookScope[indexScope])
                    indexTS =TS.fun2(filePath=filePathExcel, bookScope=daySheet, scope=timeScope[indexScope])

                    # Loop 2:-
                    index = 0
                    for index in range(len(indexTS.index1)):
                        # Sampling data
                        df = dft[(indexTS.index1[index]):(indexTS.index2[index])]

                        #Make Indicator
                        EMA = addIndicator.fun(dataFrame = df, scope = timeScope[indexScope] )

                        #Make Yellow Color Candel 
                        mco = YellowCandel.fun(dataFrame = df) 

                        #Make a fibonacci lines
                        fabalines = FibonacciLines.fun (filePath_fun = filePathExcel)

                        #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                        setName = '\\' + tickerName + '_' + timeScope[indexScope] + '_' + indexTS.index4[index] + '_to_' + indexTS.index5[index]
                        save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                        #Make a chart
                        mpf.plot(data                   = df,
                                title                  = (tickerName + ' ' + timeScope[indexScope]), 
                                type                   = 'candle', 
                                #mav                    = (20,50),
                                volume                 = True,
                                show_nontrading        = False,
                                tight_layout           = True,
                                figratio               = (1,1),
                                figscale               = 3,
                                scale_padding          = 0.30,
                                figsize               = (12,6),
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
            ###___________________________________________________________________________________________________________________________                                                
                        
            if (flagIBKR):
                # start the Function:-

            #------------------------------------------------
                # Create File:        
                        # datetime object containing current date and time --- Help Link :- https://www.programiz.com/python-programming/datetime/current-datetime#google_vignette
                now = datetime.now()
                dt_string = now.strftime("[%Y%m%d_%H%M%S]") # YYmmdd_HHMMSS
                sessionSymbol =  "zzIBKR" + ' ' + str(dt_string)
                rxChartPath = CreateFile.fun(directory = sessionSymbol, parent_dir = filePathChart)

            #------------------------------------------------
                # Loop 1:-
                Fobi_Var        = FibonacciLines.FiboClass2()
                imgCount        = 0
                daySheet        = "IBKR 1Day"
                indexScope      =  '5 secs'         
                timeScope       = ['5 secs']      #   ['5 secs','1 min','5 mins','30 mins','1 hour','1 day']
                bookScope       = {
                                    '1 secs' :{'SizeIndex': 0, 'DurationIndex':1, 'DurationLenth': 1, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 1s'     },
                                    '5 secs' :{'SizeIndex': 1, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':60, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 5s'     },
                                    '10 secs':{'SizeIndex': 2, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':30, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 10s'    },
                                    '15 secs':{'SizeIndex': 3, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':20, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 15s'    },
                                    '30 secs':{'SizeIndex': 4, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "5s", 'SheetName':'IBKR 30s'    },
                                    '1 min'  :{'SizeIndex': 5, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':"IBKR 1m"     },
                                    '2 mins' :{'SizeIndex': 6, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling': 5, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 2m'     },
                                    '3 mins' :{'SizeIndex': 7, 'DurationIndex':1, 'DurationLenth': 2, 'Rolling':10, 'ChartDayDuration':  -1, 'indexTS': "1m", 'SheetName':'IBKR 3m'     },
                                    '5 mins' :{'SizeIndex': 8, 'DurationIndex':1, 'DurationLenth': 3, 'Rolling': 6, 'ChartDayDuration':  -1, 'indexTS': "5m", 'SheetName':'IBKR 5m'     },
                                    '10 mins':{'SizeIndex': 9, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling': 6, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 10m'    },
                                    '15 mins':{'SizeIndex':10, 'DurationIndex':1, 'DurationLenth': 9, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 15m'    },
                                    '20 mins':{'SizeIndex':11, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':12, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 20m'    },
                                    '30 mins':{'SizeIndex':12, 'DurationIndex':1, 'DurationLenth':12, 'Rolling':11, 'ChartDayDuration':  -6, 'indexTS':"30m", 'SheetName':'IBKR 30m'    },
                                    '1 hour' :{'SizeIndex':13, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':16, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 1H'     },
                                    '2 hours':{'SizeIndex':14, 'DurationIndex':1, 'DurationLenth':34, 'Rolling': 8, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 2H'     },
                                    '3 hours':{'SizeIndex':15, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':30, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 3H'     },
                                    '4 hours':{'SizeIndex':16, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':20, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 4H'     },
                                    '8 hours':{'SizeIndex':17, 'DurationIndex':1, 'DurationLenth':34, 'Rolling':42, 'ChartDayDuration': -21, 'indexTS': "1h", 'SheetName':'IBKR 8H'     },
                                    '1 day'  :{'SizeIndex':18, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':21, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Day'   },
                                    '1W'     :{'SizeIndex':19, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1week'  },
                                    '1M'     :{'SizeIndex':20, 'DurationIndex':4, 'DurationLenth': 5, 'Rolling':12, 'ChartDayDuration':-220, 'indexTS': "1d", 'SheetName':'IBKR 1Month' }
                                    }

                dfTimeStamp     = TS.fGetTimeStampDataFrame(    
                                                            timeStampPath      = filePathWL
                                                            ,timeStampSheet     = timeStampSheet                 
                                                            )
                ChartStyle,timeScope      = TS.fGetStyle2(                 
                                                dfTimeStamp
                                                ,AttributeIndex=0
                                                ,AttributeList =[
                                                                "style_name"
                                                                ,"base_mpl_style"
                                                                ,"marketcolors"
                                                                ,"candle_Up"
                                                                ,"candle_Down"
                                                                ,"edge_Up"
                                                                ,"edge_Down"
                                                                ,"wick_Up"
                                                                ,"wick_Down"
                                                                ,"ohlc_Up"
                                                                ,"ohlc_Down"
                                                                ,"volume_Up"
                                                                ,"volume_Down"
                                                                ,"vcdopcod"
                                                                ,"alpha"
                                                                ,"mavcolors"
                                                                ,"y_on_right"
                                                                ,"gridcolor"
                                                                ,"gridstyle"
                                                                ,"facecolor"
                                                                ,"figcolor"
                                                                ,"rc"
                                                                ,"axes.edgecolor"
                                                                ,"axes.linewidth"
                                                                ,"axes.labelsize"
                                                                ,"axes.labelweight"
                                                                ,"axes.grid"
                                                                ,"axes.grid.axis"
                                                                ,"axes.grid.which"
                                                                ,"grid.alpha"
                                                                ,"grid.color"
                                                                ,"grid.linestyle"
                                                                ,"grid.linewidth"
                                                                ,"figure.facecolor"
                                                                ,"patch.linewidth"
                                                                ,"lines.linewidth"
                                                                ,"font.weight"
                                                                ,"font.size"
                                                                ,"figure.titlesize"
                                                                ,"figure.titleweight"
                                                                ,"base_mpf_style"]
                                                ,AttributeDic = {
                                                                "style_name"           :	"Ehab_Staylo"
                                                                ,"base_mpl_style"       :	"dark_background"
                                                                ,"marketcolors"         :	"marketcolors"
                                                                ,"candle_Up"            :	"#14CE1C"
                                                                ,"candle_Down"          :	"#CE1414"
                                                                ,"edge_Up"              :	"#14CE1C"
                                                                ,"edge_Down"            :	"#CE1414"
                                                                ,"wick_Up"              :	"#ffffff"
                                                                ,"wick_Down"            :	"#ffffff"
                                                                ,"ohlc_Up"              :	"#ffffff"
                                                                ,"ohlc_Down"            :	"#ffffff"
                                                                ,"volume_Up"            :	"#14CE1C"
                                                                ,"volume_Down"          :	"#CE1414"
                                                                ,"vcdopcod"             :	 False	
                                                                ,"alpha"                :	 2.00	
                                                                ,"mavcolors"            :	 ['#ec009c','#78ff8f','#fcf120']	
                                                                ,"y_on_right"           :	 True	
                                                                ,"gridcolor"            :	 None	
                                                                ,"gridstyle"            :	 None	
                                                                ,"facecolor"            :	"Black"
                                                                ,"figcolor"             :	"gray"
                                                                ,"rc"                   :	"rc"
                                                                ,"axes.edgecolor"       :	"white"
                                                                ,"axes.linewidth"       :	 1.50	
                                                                ,"axes.labelsize"       :	"large"
                                                                ,"axes.labelweight"     :	"semibold"
                                                                ,"axes.grid"            :	 True	
                                                                ,"axes.grid.axis"       :	"both"
                                                                ,"axes.grid.which"      :	"major"
                                                                ,"grid.alpha"           :	 0.90	
                                                                ,"grid.color"           :	"#EBEE24"
                                                                ,"grid.linestyle"       :	":"	
                                                                ,"grid.linewidth"       :	 1.00	
                                                                ,"figure.facecolor"     :	"#0a0a0a"
                                                                ,"patch.linewidth"      :	 1.00	
                                                                ,"lines.linewidth"      :	 1.00	
                                                                ,"font.weight"          :	"medium"
                                                                ,"font.size"            :	 8.00	
                                                                ,"figure.titlesize"     :	"x-large"
                                                                ,"figure.titleweight"   :	"semibold"
                                                                ,"base_mpf_style"       :	"mike"
                                                                }
                                                )
                dfDay           = TS.fGetDayDataFrame( filePath = filePathExcel ,DaySheetName = daySheet )#r"C:\Users\lenovo\Desktop\TGL\BCG\OK BCG.xlsx"  
                dfDay = dfDay.fillna(0)
                dfIBKR30m = ImportData.fun2 (filePath_fun = filePathExcel , bookName = 'IBKR 30m')    #   'YAHOO'      'IBKR 30m'  IBKR 1H
                Fobi_Var.GetHighLow(dfD=dfDay   ,dfT=dfIBKR30m    ,showOutPut=True)

                for indexScope in timeScope:
                #------------------------------------------------
                    # Import  data
                    dft = ImportData.fun2 (filePath_fun = filePathExcel , bookName = bookScope[indexScope]['SheetName'])    #   'YAHOO'      'IBKR 30m'  IBKR 1H
                    if( len(dft.index) == 0 ):
                        print ( "This Sheet : ",bookScope[indexScope]['SheetName']," is Empty")
                    if( len(dft.index) > 0 ):
                        # Replace NaN Values with Zeros in Pandas DataFrame     Help Link :- https://www.geeksforgeeks.org/replace-nan-values-with-zeros-in-pandas-dataframe/
                        dft = dft.fillna(0)
                        TimeStamp_df =TS.fun7(   dfD                = dfDay
                                                ,dfS                = dfTimeStamp 
                                                ,scope              = indexScope # ["5s","1m","5m","30m","1h","1d"]  
                                                ,scopeBook          = {
                                                                        "5s":"5s"
                                                                        ,'5 secs':"5s"
                                                                        ,"1m":"1m"
                                                                        ,'1 min':"1m"
                                                                        ,"5m":"5m"
                                                                        ,'5 mins':"5m"
                                                                        ,"30m":"30m"
                                                                        ,'30 mins':"30m"
                                                                        ,"1h":"1h"
                                                                        ,'1 hour':"1h"
                                                                        ,"1d":"1d" 
                                                                        ,'1 day':"1d" 
                                                                    }   
                                            )
                        

                    #------------------------------------------------
                        # Loop 2:-
                        
                        index = 0
                        for index in range(len(TimeStamp_df.Index1)):
                            
                            # Sampling data

                            df = dft[(TimeStamp_df.Index1[index]):(TimeStamp_df.Index2[index])]
                            if( len(df.index) == 0 ):   # Skip Empty Segment.
                                print (  "Ticker: ",tickerName,"  This Time Segment : " ,TimeStamp_df.Index1[index] ,":"  ,TimeStamp_df.Index2[index]   ," is Empty")
                            if( len(df.index) > 0 ):  
                                print ( "###############################################")
                                print ( "#######","Ticker: ",tickerName,"#######")
                                print (" in Time Segment : " ,TimeStamp_df.Index1[index] ,":"  ,TimeStamp_df.Index2[index]   ," is under Process")
                                print ( "###############################################")                         
                                        
                                dfH = df.High.max()
                                dfL = df.Low.min()
                                dfD = (dfH - dfL) * 0.05 

                                # df = dft['2023-09-20 09:30:00':'2023-09-20 10:00:00']
                                # df = dft
                                # print (df)

                            #------------------------------------------------
                                #Make Chart Style
                                
                                #Make Yellow Color Candel 
                                mco = YellowCandel.fun(dataFrame = df) 
                                
                                #Make Indicator
                                EMA = addIndicator.fun5(dataFrame = df ,scope = indexScope ,style=timeStampSheet)    # need one for IBKR

                                #Make a horizontal lines
                                Fobi_Var.MakeHorizontalLine (
                                                                 style = timeStampSheet
                                                                ,fibonacciIndex = TimeStamp_df.Fibonacci[index]
                                                                ,showOutPut = True
                                                            )
                                #Make a fibonacci lines
                                # Fobi_Var = FibonacciLines.fun2 (     filePath_fun   = filePathExcel
                                #                                     ,Fobi_Input     = Fobi_Var
                                #                                     ,DaySheetName   = daySheet 
                                #                                     ,fibonacciIndex = TimeStamp_df.Fibonacci[index]
                                #                                     ,fibonacciBook  ={
                                #                                                         "Last5Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-61	,	"EndDelta":	-1			},
                                #                                                         "Last1Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-13	,	"EndDelta":	-1			},
                                #                                                         "Last1Month"	:{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-31	,	"EndDelta":	-2			},
                                #                                                         "Last1Week"	    :{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-6	,	"EndDelta":	-2			},
                                #                                                         "Yesterday"	    :{	'SheetName':	'IBKR 4H'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                #                                                         "PreMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"06:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                #                                                         "PreMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"06:00:00"	,	"PeriodEnd":	"08:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"06:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                #                                                         "MarketOpen"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"09:00:00"	,	"PeriodEnd":	"10:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"09:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                #                                                         "Midday"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"10:00:00"	,	"PeriodEnd":	"14:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"10:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                #                                                         "PowerHour"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"14:00:00"	,	"PeriodEnd":	"16:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"14:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                #                                                         "AfterMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"16:00:00"	,	"PeriodEnd":	"18:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"16:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                #                                                         "AfterMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"18:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"18:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                #                                                         "Final"	        :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"20:00:00"	,	"PeriodEnd":	"00:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                #                                                         "Random1"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                #                                                         "Random2"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                #                                                         "Random3"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                #                                                         "Random4"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                #                                                         "Random5"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			}
                                #                                                     }
                                #                                 )

                                
                                

                                #Make Time Lable
                                timeLable = TS.fTimeLable2  (  f_Scope        = TimeStamp_df.Scope[index] # (source=daySheet   ,interval=indexScope   ,inList=list (df.index.map(str)))
                                                            ,f_HourConstant = TimeStamp_df.HourConstant[index]
                                                            ,f_MinConstant  = TimeStamp_df.MinConstant[index]
                                                            ,f_SecConstant  = TimeStamp_df.SecConstant[index]
                                                            ,f_leftSide     = TimeStamp_df.leftSide[index]
                                                            ,source         = "IBKR"
                                                            ,interval       = indexScope
                                                            ,inList         = list (df.index.map(str))
                                                        )

                                #Make Price Label
                                priceLabel = TS.LabelPrice6 (    pMax = dfH + dfD
                                                                ,pMin = dfL - dfD
                                                            )

                                
                                # #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                # setName = '\\' + tickerName + '_' + str("%03d"%imgCount) + '_'  + indexScope + '_' + TimeStamp_df.Name[index] 
                                # save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)

                                #Make a chart
                                fig, axlist = mpf.plot(  data                   = df
                                                        ,title                  = (tickerName + ' ' + indexScope)
                                                        ,type                   = 'candle' 
                                                        # ,mav                    = (20,50)
                                                        ,volume                 = True
                                                        ,show_nontrading        = False
                                                        ,tight_layout           = True
                                                        ,figratio               = (1,1)
                                                        ,figscale               = 3
                                                        ,scale_padding          = 0.30
                                                        ,figsize               = (12,6)
                                                        # ,ylim                   = (((df.Low.min())*0.95) ,((df.High.max())*1.05)) # set min and max of Chart
                                                        ,ylim                   = ((dfL - dfD) ,(dfH + dfD)) # set min and max of Chart (dfH + dfD)
                                                        ,xrotation              = 0
                                                        ,yscale                 = "linear" # y-axis scale: "linear", "log", "symlog", or "logit"
                                                        ,volume_yscale          = "linear" # Volume y-axis scale: "linear", "log", "symlog", or "logit"
                                                        ,style                  = ChartStyle
                                                        ,marketcolor_overrides  = mco
                                                        ,mco_faceonly           = False
                                                        ,addplot                = EMA
                                                        ,hlines                 = Fobi_Var.fibolines
                                                        ,returnfig=True
                                                        # ,savefig                = save # link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                                        # ,marketcolor_overrides = mco  # link https://github.com/matplotlib/mplfinance/blob/master/examples/marketcolor_overrides.ipynb
                                )
                                
                                #Add Time Lable      Help link:   https://github.com/matplotlib/mplfinance/issues/573
                                axlist[-2].set_xticks(timeLable["ticks"])
                                axlist[-2].set_xticklabels(timeLable["tlabs"], ha='center')
                                axlist[-2].set_xticks(timeLable["mitks"],minor=True)
                                axlist[-2].set_xticklabels(timeLable["milab"], ha='center', minor=True, rotation=0) 

                                x2 = axlist[0].secondary_xaxis('top')       # Help Link :-  https://matplotlib.org/stable/gallery/ticks/multilevel_ticks.html#sphx-glr-gallery-ticks-multilevel-ticks-py
                                x2.set_xticks(timeLable["ticks"])           # Help Link :-  https://matplotlib.org/stable/api/axes_api.html
                                x2.set_xticklabels(timeLable["Utlabs"], ha='center')
                                x2.set_xticks(timeLable["mitks"],minor=True)
                                x2.set_xticklabels(timeLable["Umilab"], ha='center', minor=True, rotation=0)
                                
                                #Add Price Lable     Help Link:-   https://github.com/matplotlib/mplfinance/issues/604 
                                axlist[0].set_yticks( priceLabel['ticks'] )
                                axlist[0].set_yticklabels( priceLabel['tlabs'] )
                                                
                                y2 = axlist[0].secondary_yaxis('left')      # Help Link :-  https://github.com/matplotlib/mplfinance/issues/587
                                y2.set_yticks(priceLabel['ticks'])
                                y2.set_yticklabels( priceLabel['tlabs'] )
                                
                                
                                #Saving plot to a file -> Link: https://github.com/matplotlib/mplfinance/blob/master/examples/savefig.ipynb
                                setName = '\\' + tickerName + '_' + str("%03d"%imgCount) + '_'  + indexScope + '_' + TimeStamp_df.Name[index] 
                                save = dict(fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0)
                                
                                
                                #Saving Chart        Help link:   https://github.com/matplotlib/mplfinance/issues/573
                                fig.savefig( fname= (rxChartPath + setName + imageType), dpi= 300, pad_inches= 0, bbox_inches='tight' )
                                imgCount += 1

                                # mpf.show()
                                # matplotlib.pyplot.savefig()
                                # fig.save()
                                
                                # axlist[-2].save()
                                # fig.savefig( 'myplot.pdf', bbox_inches='tight' )           
###_____________________________________________________________________________________________________________________________________________________________________________________










# fun9( )
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


def fun2(    # Set Varibles
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




# fun2()




































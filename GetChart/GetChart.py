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







































